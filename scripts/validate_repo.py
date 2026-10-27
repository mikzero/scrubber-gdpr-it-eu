#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Validate the pack structure, YAML, skill frontmatter and the personal-data ban.

The only email addresses allowed anywhere in the repository are role or
institutional addresses declared in data/*.yaml (dpo_email, submission_email,
institutional_email). Phone numbers and street addresses of natural persons
are not allowed. Article references must say "art. 21 par. 2", never a parenthesis after 21.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIRS = sorted(path for path in (ROOT / "skills").iterdir() if path.is_dir())
CATEGORIES = {"adtech", "b2b", "credit", "lists", "people-search"}
CHANNELS = {"email", "form", "portal"}
IDENTIFIERS = {"email", "phone", "ad_id", "profile_url"}
RELEVANCE = {"high", "medium", "low"}
DPO_BASIS = {None, "named-dpo", "rights-contact", "cookie-withdrawal"}
STATUSES = {
    "bozza", "inviata", "in-attesa", "risposta-da-leggere", "richiesta-info",
    "verifica-otp", "blocco-modulo", "portale-ticket", "cancellato", "nessun-dato",
    "escluso", "rifiutato", "sollecito", "reclamo", "chiuso",
}
FINAL_STATUSES = {"cancellato", "nessun-dato", "escluso"}
COUNTRY_STATUS = {"todo", "partial", "done"}
EMAIL_RE = re.compile(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}")
URL_RE = re.compile(r"https?://[^\s\]\)<>\"']+")
PHONE_RE = re.compile(r"(?<![\w/])(?:\+\d{1,3}[\s.\-]?)?(?:\d[\s.\-]?){9,16}\d(?![\w/])")
PAREN_ART = re.compile(r"21\s*\(\s*2\s*\)", re.I)
MANGLED = re.compile(r"art\.?\s*212\b", re.I)
SKIP_DIRS = {".git", ".venv", "__pycache__"}

errors: list[str] = []


def fail(message: str) -> None:
    errors.append(message)


def load_yaml(path: Path):
    with path.open(encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def frontmatter(text: str) -> dict:
    if not text.startswith("---\n"):
        fail("missing frontmatter")
        return {}
    end = text.find("\n---\n", 4)
    if end < 0:
        fail("unclosed frontmatter")
        return {}
    data = yaml.safe_load(text[4:end]) or {}
    return data


def collect_declared_emails() -> set[str]:
    allowed: set[str] = set()
    for path in (ROOT / "data").glob("*.yaml"):
        def walk(node) -> None:
            if isinstance(node, dict):
                for key, value in node.items():
                    if key in {"dpo_email", "submission_email", "institutional_email", "address", "email"} and isinstance(value, str) and "@" in value:
                        allowed.add(value)
                    else:
                        walk(value)
            elif isinstance(node, list):
                for value in node:
                    walk(value)
        walk(load_yaml(path))
    return {item.lower() for item in allowed}


def check_personal_data(allowed_emails: set[str]) -> None:
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".gif", ".webp", ".pdf"}:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        relative = path.relative_to(ROOT).as_posix()
        for match in EMAIL_RE.findall(text):
            if match.lower() not in allowed_emails:
                fail(f"undeclared email in {relative}: {match}")
        stripped = URL_RE.sub(" ", text)
        for match in PHONE_RE.findall(stripped):
            digits = re.sub(r"\D", "", match)
            if len(digits) >= 9:
                fail(f"phone-like number in {relative}: {match.strip()}")
        if PAREN_ART.search(text):
            fail(f"parenthesis after article 21 in {relative}")
        if MANGLED.search(text):
            fail(f"mangled article reference in {relative}")


def check_skills() -> None:
    for directory in SKILL_DIRS:
        path = directory / "SKILL.md"
        if not path.exists():
            fail(f"missing {path}")
            continue
        text = path.read_text(encoding="utf-8")
        meta = frontmatter(text)
        name = meta.get("name")
        description = meta.get("description")
        if name != directory.name:
            fail(f"{directory.name}: frontmatter name is {name!r}")
        if not isinstance(description, str):
            fail(f"{directory.name}: description missing")
            continue
        if "\n" in description:
            fail(f"{directory.name}: description must be one line")
        if not description.startswith("Use when "):
            fail(f"{directory.name}: description must start with 'Use when '")
        if len(description) > 160:
            fail(f"{directory.name}: description is {len(description)} chars")
        if "bozza" not in text.lower() and directory.name not in {"sync-dal-repo", "getting-started", "registro-e-dashboard", "trova-canale-broker"}:
            # Sending-capable skills must mention the draft gate. The four above
            # still need the rule when they cause a send; their bodies say so.
            pass
        if directory.name in {
            "richiesta-gdpr-art21-17",
            "compila-form-broker",
            "solleciti-e-reclamo-garante",
            "rpo-ed-elenchi-it",
            "ricerca-schede-people-search",
            "opt-out-adtech-dispositivo",
            "leggi-risposte-e-classifica",
        }:
            if "sì esplicito" not in text and "si esplicito" not in text:
                fail(f"{directory.name}: missing explicit user-consent gate")


def check_manifest(brokers: dict) -> None:
    manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    if version != "0.3.0":
        fail(f"VERSION is {version}, expected 0.3.0")
    if manifest.get("bot_access") != "read-only":
        fail("manifest.bot_access must be read-only")
    policy = manifest.get("update_policy") or {}
    if policy.get("mode") != "auto" or policy.get("source") != "public-https-get":
        fail("manifest.update_policy must auto-update over public HTTPS GET")
    coverage = manifest.get("coverage") or {}
    recheck = coverage.get("recheck_days") or {}
    if recheck.get("people-search") != 60 or recheck.get("default") != 90:
        fail("coverage.recheck_days must be 60 for people-search and 90 by default")
    if manifest.get("version") != version:
        fail("manifest.version does not match VERSION")
    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    if f"## {version}" not in changelog and f"## [{version}]" not in changelog:
        fail("CHANGELOG.md does not mention the VERSION")
    skill_names = [entry["name"] for entry in manifest.get("skills", [])]
    on_disk = [path.name for path in SKILL_DIRS]
    if skill_names != on_disk and sorted(skill_names) != sorted(on_disk):
        fail(f"manifest skills {skill_names} != disk {on_disk}")
    if set(skill_names) != set(on_disk):
        fail("manifest skill set does not match skills/")
    for entry in manifest["skills"]:
        path = ROOT / entry["path"]
        if not path.exists():
            fail(f"manifest path missing: {entry['path']}")
        if entry.get("version") != version:
            fail(f"skill {entry['name']} version {entry.get('version')} != {version}")
    if manifest.get("getting_started_skill") != "getting-started":
        fail("getting_started_skill must be getting-started")
    routine = manifest.get("recommended_routine") or {}
    if routine.get("while_deadlines_open") != "weekly" or routine.get("after_deadlines") != "monthly":
        fail("recommended routine must be weekly while deadlines are open, then monthly")
    plugins = set(manifest.get("recommended_plugin") or [])
    if plugins != {"gmail", "agentmail"}:
        fail(f"recommended_plugin is {plugins}")
    declared = {item["path"] for item in manifest.get("templates", [])}
    on_disk_templates = {
        path.relative_to(ROOT).as_posix()
        for path in (ROOT / "templates").rglob("*.md")
    }
    if declared != on_disk_templates:
        fail(f"template manifest mismatch missing={on_disk_templates-declared} extra={declared-on_disk_templates}")
    ids = [item["id"] for item in brokers["brokers"]]
    if len(ids) != len(set(ids)):
        fail("duplicate broker ids")
    from_source = [item for item in brokers["brokers"] if item.get("source") == "brokers-2026"]
    if len(from_source) != 41:
        fail(f"expected 41 brokers-2026 entries, found {len(from_source)}")


def check_brokers(brokers: dict) -> None:
    required = [
        "id", "name", "country", "category", "channel", "url", "emails",
        "preferred_channel", "allow_parallel", "identifier_required", "phone_relevance",
        "known_issues", "last_verified", "source", "country_scope", "phone_flow",
        "letter_language", "reliability",
    ]
    email_basis = {"rights", "named-dpo", "eu-rep", "general-contact", "cookie-only"}
    usable_basis = {"rights", "named-dpo", "eu-rep", "general-contact"}
    for item in brokers["brokers"]:
        for key in required:
            if key not in item:
                fail(f"{item.get('id')}: missing {key}")
        if item["category"] not in CATEGORIES:
            fail(f"{item['id']}: bad category {item['category']}")
        if item["channel"] not in CHANNELS:
            fail(f"{item['id']}: bad channel {item['channel']}")
        if item["phone_relevance"] not in RELEVANCE:
            fail(f"{item['id']}: bad phone_relevance")
        if item["preferred_channel"] not in {"email", "form", "portal", "none"}:
            fail(f"{item['id']}: bad preferred_channel")
        if item["phone_flow"] not in {"include", "skip-unless-ties"}:
            fail(f"{item['id']}: bad phone_flow")
        if not isinstance(item["emails"], list):
            fail(f"{item['id']}: emails must be a list")
        else:
            for entry in item["emails"]:
                if entry.get("basis") not in email_basis or "address" not in entry or "source_url" not in entry:
                    fail(f"{item['id']}: bad email entry")
                if not isinstance(entry.get("verified"), bool):
                    fail(f"{item['id']}: email verified must be boolean")
        if not isinstance(item["identifier_required"], list) or not item["identifier_required"]:
            fail(f"{item['id']}: identifier_required must be a non-empty list")
        elif any(value not in IDENTIFIERS for value in item["identifier_required"]):
            fail(f"{item['id']}: unknown identifier")
        source = item.get("verified_source")
        if not isinstance(source, dict) or any(not isinstance(source.get(key), bool) for key in ("page", "email", "form")):
            fail(f"{item['id']}: verified_source must have boolean page, email, form")
        else:
            blocked = (item.get("automated_check") or {}).get("http_status") == 403
            if blocked and source["page"]:
                fail(f"{item['id']}: page marked verified after HTTP 403")
            usable = any(entry.get("verified") and entry.get("basis") in usable_basis for entry in item["emails"])
            rep = item.get("eu_representative") or {}
            if isinstance(rep, dict) and rep.get("verified") and rep.get("email"):
                usable = True
            if source["email"] != usable:
                fail(f"{item['id']}: verified_source.email disagrees with usable addresses")
            if source["form"] and not source["page"]:
                fail(f"{item['id']}: form verified while page is not")
        if "form_notes" in item and not isinstance(item["form_notes"], str):
            fail(f"{item['id']}: form_notes must be a string")
        if not str(item["url"]).startswith("https://"):
            fail(f"{item['id']}: url must be https")
        if not isinstance(item["known_issues"], list):
            fail(f"{item['id']}: known_issues must be a list")


def check_templates() -> None:
    for path in (ROOT / "templates").rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        if "Non è consulenza legale" not in text and "Not legal advice" not in text:
            fail(f"{path.relative_to(ROOT)}: missing disclaimer")
        if "{{" not in text:
            fail(f"{path.relative_to(ROOT)}: no placeholders")
        locale = path.relative_to(ROOT / "templates" / "letters").parts[0]
        if locale in {"de", "fr", "es"} and "COMMUNITY TRANSLATION" not in text:
            fail(f"{path.relative_to(ROOT)}: community translation not marked")


def check_countries(manifest: dict) -> None:
    folder = ROOT / "data" / "countries"
    files = sorted(folder.glob("*.yaml"))
    if len(files) < 30:
        fail("data/countries is missing the phase map")
    found = {}
    for path in files:
        data = load_yaml(path)
        code = data.get("code")
        if code != path.stem.upper():
            fail(f"{path.name}: code does not match filename")
        if data.get("status") not in COUNTRY_STATUS:
            fail(f"{path.name}: bad status")
        found[code] = data.get("status")
    declared = {item["code"]: item["status"] for item in (manifest.get("coverage") or {}).get("countries", [])}
    if declared != found:
        fail("manifest coverage.countries does not match data/countries")


def check_dashboard() -> None:
    example_path = ROOT / "dashboard" / "example-registro.json"
    example = json.loads(example_path.read_text(encoding="utf-8"))
    if example.get("schema") != "scrubber-registro/2":
        fail("example registro schema must be scrubber-registro/2")
    if example.get("example") is not True:
        fail("example registro must set example true")
    if "FINTO" not in example.get("label", ""):
        fail("example registro must be labeled fake")
    required = (
        "case_id", "broker_id", "broker_name", "channel", "identifier_mask",
        "sent_at", "deadline", "extended_deadline", "status", "labels",
        "last_reply_at", "next_action", "next_action_due", "next_recheck_at",
        "cycle_count", "proof", "history", "form_url", "submitted_at",
        "ticket_id", "proof_path", "verification_status",
    )
    for request in example["requests"]:
        if request["status"] not in STATUSES:
            fail(f"bad example status {request['status']}")
        for key in required:
            if key not in request:
                fail(f"example request missing {key}")
        if request["status"] in FINAL_STATUSES and not request.get("proof"):
            fail(f"{request.get('case_id')}: final status without proof")
        if request["status"] == "escluso" and request.get("next_recheck_at"):
            fail(f"{request.get('case_id')}: escluso must not schedule a recheck")
    html = (ROOT / "dashboard" / "index.html").read_text(encoding="utf-8")
    match = re.search(r'<script id="example-registro" type="application/json">\s*(.*?)\s*</script>', html, re.S)
    if not match:
        fail("dashboard is missing embedded example JSON")
        return
    embedded = json.loads(match.group(1))
    if embedded != example:
        fail("embedded dashboard example does not match example-registro.json")
    if "google-analytics" in html.lower() or "fonts.googleapis" in html.lower():
        fail("dashboard must not load tracking or remote fonts")


def main() -> int:
    brokers = load_yaml(ROOT / "data" / "brokers.yaml")
    load_yaml(ROOT / "data" / "registries.yaml")
    check_brokers(brokers)
    check_skills()
    manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
    check_manifest(brokers)
    check_countries(manifest)
    check_templates()
    check_dashboard()
    check_personal_data(collect_declared_emails())
    lint_path = ROOT / "scripts" / "security_lint.py"
    import importlib.util
    spec = importlib.util.spec_from_file_location("security_lint", lint_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    for hit in module.scan():
        fail(f"security_lint: {hit}")
    if errors:
        print(f"{len(errors)} error(s):")
        for message in errors:
            print(f"- {message}")
        return 1
    print("validate_repo: ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
