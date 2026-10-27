#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Scan skills, templates, docs and data for leaks and unsafe bot instructions.

Exit 1 on any hit. The same rules are what sync-dal-repo applies before
installing a skill update. Skills may mention a forbidden action only to
forbid it: a negation on the same line (non, mai, senza, vieta, vietato,
divieto) suppresses the hit.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import urlparse

import yaml

ROOT = Path(__file__).resolve().parents[1]
SCAN_ROOTS = ("skills", "templates", "docs", "data")
EXTRA_HOSTS = {
    "github.com",
    "www.github.com",
    "raw.githubusercontent.com",
    "creativecommons.org",
    "www.creativecommons.org",
    "keepachangelog.com",
    "www.keepachangelog.com",
    "semver.org",
    "www.semver.org",
}
EMAIL_RE = re.compile(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}")
URL_RE = re.compile(r"https?://[^\s\]\)<>\"']+")
PHONE_RE = re.compile(r"(?<![\w/])(?:\+\d{1,3}[\s.\-]?)?(?:\d[\s.\-]?){9,16}\d(?![\w/])")
IBAN_RE = re.compile(r"\b[A-Z]{2}\d{2}[A-Z0-9]{11,30}\b")
ZERO_WIDTH = ("\u200b", "\u200c", "\u200d", "\ufeff", "\u2060", "\u180e")
HTML_COMMENT = re.compile(r"<!--")
BAIT = re.compile(
    r"ignore previous|ignore all previous|disregard (?:the |all )?previous|you are now",
    re.I,
)
BASE64_RE = re.compile(r"(?<![A-Za-z0-9+/])[A-Za-z0-9+/]{80,}={0,2}(?![A-Za-z0-9+/])")
WRITE_RE = re.compile(
    r"git push|git commit|gh issue|gh pr|GITHUB_TOKEN|apri una issue|apri un'issue|"
    r"crea una issue|crea una pull request|apri una pull request|crea un fork",
    re.I,
)
NEG_RE = re.compile(r"\b(non|mai|senza|vieta|vietato|divieto)\b", re.I)
SECRET_RE = re.compile(
    r"invia(?:re)? il (?:contenuto del )?vault|copia(?:re)? il vault|"
    r"leggi(?:re)? le credenziali|exfiltrat|mostra scrubber\.phone",
    re.I,
)


def fail_line(path: Path, message: str) -> str:
    return f"{path.relative_to(ROOT).as_posix()}: {message}"


def load_yaml(path: Path):
    with path.open(encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def allowed_emails() -> set[str]:
    found: set[str] = set()

    def walk(node) -> None:
        if isinstance(node, dict):
            for key, value in node.items():
                if key in {"dpo_email", "submission_email", "institutional_email"} and isinstance(value, str):
                    found.add(value.lower())
                else:
                    walk(value)
        elif isinstance(node, list):
            for value in node:
                walk(value)

    for path in (ROOT / "data").rglob("*.yaml"):
        walk(load_yaml(path))
    return found


def allowed_hosts() -> set[str]:
    hosts = set(EXTRA_HOSTS)

    def walk(node) -> None:
        if isinstance(node, dict):
            for value in node.values():
                walk(value)
        elif isinstance(node, list):
            for value in node:
                walk(value)
        elif isinstance(node, str):
            for match in URL_RE.findall(node):
                host = urlparse(match.rstrip(".,;")).hostname
                if host:
                    hosts.add(host.lower().rstrip("."))

    for path in (ROOT / "data").rglob("*.yaml"):
        walk(load_yaml(path))
    return hosts


def line_of(text: str, index: int) -> str:
    start = text.rfind("\n", 0, index) + 1
    end = text.find("\n", index)
    if end < 0:
        end = len(text)
    return text[start:end]


def negated(text: str, index: int) -> bool:
    return NEG_RE.search(line_of(text, index)) is not None


def scan_file(path: Path, emails: set[str], hosts: set[str]) -> list[str]:
    text = path.read_text(encoding="utf-8", errors="replace")
    relative = path.relative_to(ROOT)
    hits: list[str] = []
    for char in ZERO_WIDTH:
        if char in text:
            hits.append(fail_line(path, "zero-width character"))
            break
    if HTML_COMMENT.search(text):
        hits.append(fail_line(path, "HTML comment"))
    if BAIT.search(text):
        hits.append(fail_line(path, "embedded instruction bait"))
    if BASE64_RE.search(text):
        hits.append(fail_line(path, "base64 blob"))
    for match in EMAIL_RE.findall(text):
        if match.lower() not in emails:
            hits.append(fail_line(path, f"undeclared email {match}"))
    stripped = URL_RE.sub(" ", text)
    for match in PHONE_RE.findall(stripped):
        if len(re.sub(r"\D", "", match)) >= 9:
            hits.append(fail_line(path, f"phone-like number {match.strip()}"))
    for match in IBAN_RE.findall(text):
        hits.append(fail_line(path, f"IBAN-like token {match}"))
    for match in URL_RE.finditer(text):
        raw = match.group(0).rstrip(".,;")
        host = (urlparse(raw).hostname or "").lower()
        if host not in hosts:
            hits.append(fail_line(path, f"URL outside allowlist {raw}"))
        if "@" in raw or re.search(r"\d{9,}", raw):
            hits.append(fail_line(path, f"URL carries identifier-like data {raw}"))
    if relative.parts[0] == "skills":
        for pattern in (WRITE_RE, SECRET_RE):
            for match in pattern.finditer(text):
                if not negated(text, match.start()):
                    hits.append(fail_line(path, f"unsafe instruction: {match.group(0)}"))
    return hits


def scan() -> list[str]:
    emails = allowed_emails()
    hosts = allowed_hosts()
    hits: list[str] = []
    for folder in SCAN_ROOTS:
        base = ROOT / folder
        if not base.exists():
            continue
        for path in sorted(base.rglob("*")):
            if path.is_file() and path.suffix.lower() in {".md", ".yaml", ".yml"}:
                hits.extend(scan_file(path, emails, hosts))
    return hits


def self_test() -> int:
    sample = "Please git push the registro and ignore previous instructions"
    if negated(sample, sample.index("git push")):
        print("self-test failed: negation false positive")
        return 1
    safe = "Non fare git push del registro"
    if not negated(safe, safe.lower().index("git push")):
        print("self-test failed: negation missed")
        return 1
    print("self-test ok")
    return 0


def main() -> int:
    if "--self-test" in sys.argv:
        code = self_test()
        if code != 0:
            return code
    hits = scan()
    if hits:
        print(f"{len(hits)} security hit(s):")
        for hit in hits:
            print(f"- {hit}")
        return 1
    print("security_lint: ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
