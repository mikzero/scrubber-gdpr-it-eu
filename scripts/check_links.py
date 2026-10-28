#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Check http(s) URLs declared in data/*.yaml.

Exit 0 when no URL is a confirmed dead link (HTTP 404 or 410).
Exit 1 when at least one URL returns 404 or 410.

HTTP 401 and 403 are warnings: many privacy pages block automated clients.
Timeouts, TLS errors and HTTP 5xx are warnings, not proof that the page is gone.

Use --self-test to classify responses from a local server without reading data/.
Use --open-issue on a scheduled GitHub Actions run to open or update an issue.
The issue body contains only URLs and status codes, never page contents.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import ssl
import sys
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

import yaml

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
UA = "ScrubberGDPR-linkcheck/0.1 (+https://github.com/mikzero/scrubber-gdpr-it-eu)"
URL_RE = re.compile(r"https?://[^\s\]\)<>\"']+")
FAIL_STATUSES = {404, 410}
WARN_STATUSES = {401, 403}


def extract_urls(node, found: set[str]) -> None:
    if isinstance(node, dict):
        for value in node.values():
            extract_urls(value, found)
    elif isinstance(node, list):
        for value in node:
            extract_urls(value, found)
    elif isinstance(node, str):
        for match in URL_RE.findall(node):
            found.add(match.rstrip(".,;:"))


def load_urls() -> list[str]:
    found: set[str] = set()
    for path in sorted(DATA.glob("*.yaml")):
        with path.open(encoding="utf-8") as handle:
            extract_urls(yaml.safe_load(handle), found)
    return sorted(found)


def classify(status: int | None) -> str:
    if status in FAIL_STATUSES:
        return "fail"
    if status in WARN_STATUSES:
        return "warn"
    if status is not None and 200 <= status < 400:
        return "ok"
    return "warn"


def check_url(url: str, timeout: float) -> dict:
    request = Request(url, method="GET", headers={"User-Agent": UA})
    context = ssl.create_default_context()
    try:
        with urlopen(request, timeout=timeout, context=context) as response:
            # Read a byte so servers that stall after headers still settle.
            response.read(64)
            status = getattr(response, "status", 200)
            return {"url": url, "status": status, "class": classify(status), "detail": ""}
    except HTTPError as exc:
        return {"url": url, "status": exc.code, "class": classify(exc.code), "detail": ""}
    except URLError as exc:
        return {"url": url, "status": None, "class": "warn", "detail": type(exc.reason).__name__ if hasattr(exc, "reason") else "URLError"}
    except Exception as exc:  # noqa: BLE001 — report and continue
        return {"url": url, "status": None, "class": "warn", "detail": type(exc).__name__}


def github_json(method: str, url: str, token: str, payload: dict | None = None) -> dict:
    data = None if payload is None else json.dumps(payload).encode("utf-8")
    request = Request(
        url,
        data=data,
        method=method,
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": UA,
            "Content-Type": "application/json",
        },
    )
    with urlopen(request, timeout=30) as response:
        raw = response.read().decode("utf-8")
        return json.loads(raw) if raw else {}


def open_or_update_issue(failures: list[dict]) -> None:
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    repo = os.environ.get("GITHUB_REPOSITORY")
    if not token or not repo:
        print("issue: skipped (no GITHUB_TOKEN or GITHUB_REPOSITORY)")
        return
    lines = [f"- {item['status']} {item['url']}" for item in failures]
    body = (
        "Controllo automatico dei link in `data/*.yaml`.\n\n"
        "Questi URL hanno risposto HTTP 404 o 410. "
        "Un 403 non è in questo elenco: viene trattato come avviso anti-bot.\n\n"
        + "\n".join(lines)
        + "\n\nNon incollare dati personali nei commenti.\n"
    )
    query = quote(f'repo:{repo} is:issue is:open in:title "[link-check]"')
    existing = github_json("GET", f"https://api.github.com/search/issues?q={query}", token)
    items = existing.get("items") or []
    if items:
        number = items[0]["number"]
        github_json(
            "POST",
            f"https://api.github.com/repos/{repo}/issues/{number}/comments",
            token,
            {"body": body},
        )
        print(f"issue: commented on #{number}")
        return
    created = github_json(
        "POST",
        f"https://api.github.com/repos/{repo}/issues",
        token,
        {"title": "[link-check] URL non raggiungibili (404)", "body": body},
    )
    print(f"issue: opened #{created.get('number')}")


def print_report(results: list[dict]) -> int:
    counts = {"ok": 0, "warn": 0, "fail": 0}
    for item in results:
        counts[item["class"]] += 1
        if item["class"] == "ok":
            continue
        status = item["status"] if item["status"] is not None else item["detail"] or "error"
        print(f"{item['class'].upper()}\t{status}\t{item['url']}")
    print(f"summary ok={counts['ok']} warn={counts['warn']} fail={counts['fail']} total={len(results)}")
    return 1 if counts["fail"] else 0


def self_test() -> int:
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):  # noqa: N802
            code = {"/ok": 200, "/gone": 410, "/missing": 404, "/blocked": 403}.get(self.path, 404)
            self.send_response(code)
            self.end_headers()
            self.wfile.write(b"ok" if code == 200 else b"no")

        def log_message(self, fmt: str, *args) -> None:
            return

    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    base = f"http://127.0.0.1:{server.server_address[1]}"
    try:
        results = [check_url(base + path, 5) for path in ("/ok", "/gone", "/missing", "/blocked")]
    finally:
        server.shutdown()
    classes = {item["url"].rsplit("/", 1)[-1]: item["class"] for item in results}
    expected = {"ok": "ok", "gone": "fail", "missing": "fail", "blocked": "warn"}
    if classes != expected:
        print("self-test failed", classes)
        return 1
    print("self-test ok", classes)
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Check URLs in data/*.yaml")
    parser.add_argument("--timeout", type=float, default=20)
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--open-issue", action="store_true")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        code = self_test()
        if code != 0:
            return code
    urls = load_urls()
    if not urls:
        print("no URLs found in data/*.yaml", file=sys.stderr)
        return 1
    results = []
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = [pool.submit(check_url, url, args.timeout) for url in urls]
        for future in as_completed(futures):
            results.append(future.result())
    results.sort(key=lambda item: item["url"])
    code = print_report(results)
    failures = [item for item in results if item["class"] == "fail"]
    if args.open_issue and failures:
        open_or_update_issue(failures)
    return code


if __name__ == "__main__":
    sys.exit(main())
