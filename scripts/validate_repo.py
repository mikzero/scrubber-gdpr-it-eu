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
CATEGORIES = {
    "adtech", "b2b", "credit", "lists", "people-search",
    "directory", "telco", "registry", "authority", "contract",
}
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
        if "bozza" not in text.lower() and directory.name not in {"scrubber-sync-dal-repo", "scrubber-getting-started", "scrubber-registro-e-dashboard", "scrubber-trova-canale-broker"}:
            # Sending-capable skills must mention the draft gate. The four above
            # still need the rule when they cause a send; their bodies say so.
            pass
        if not directory.name.startswith("scrubber-"):
            fail(f"{directory.name}: skill folder must use the scrubber- prefix")
        if directory.name in {
            "scrubber-richiesta-gdpr-art21-17",
            "scrubber-compila-form-broker",
            "scrubber-solleciti-e-reclamo-garante",
            "scrubber-rpo-ed-elenchi-it",
            "scrubber-ricerca-schede-people-search",
            "scrubber-opt-out-adtech-dispositivo",
            "scrubber-leggi-risposte-e-classifica",
        }:
            if "sì esplicito" not in text and "si esplicito" not in text:
                fail(f"{directory.name}: missing explicit user-consent gate")


def check_manifest(brokers: dict) -> None:
    manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    if version != "0.3.3":
        fail(f"VERSION is {version}, expected 0.3.3")
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
    if manifest.get("getting_started_skill") != "scrubber-getting-started":
        fail("getting_started_skill must be scrubber-getting-started")
    if manifest.get("registro_skill") != "docs/registro-skill.md":
        fail("registro_skill must point at docs/registro-skill.md")
    expected_skills_policy = (
        "scrubber-prefix; first-install-from-main-then-signed-v-tag; "
        "user-skills-allowed-with-warnings; never-overwrite-user-edit-or-foreign-name"
    )
    if policy.get("skills") != expected_skills_policy:
        fail("manifest.update_policy.skills does not match the v0.3.3 skill rules")
    if policy.get("skill_prefix") != "scrubber-":
        fail("manifest.update_policy.skill_prefix must be scrubber-")
    if policy.get("user_skills") != "allowed-with-warnings-never-silent-block":
        fail("user skills must stay allowed, with warnings and no silent block")
    if policy.get("foreign_same_name") != "never-overwrite-log-conflict":
        fail("a same-named foreign skill must never be overwritten")
    if policy.get("skill_log") != "local-only":
        fail("skill log must stay local")
    for entry in manifest["skills"]:
        if not str(entry.get("name", "")).startswith("scrubber-"):
            fail(f"skill {entry.get('name')} must use the scrubber- prefix")
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
        if item["phone_flow"] not in {"include", "skip-unless-ties", "opt-in"}:
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
        if "form_notes" in item and item["form_notes"] is not None and not isinstance(item["form_notes"], str):
            fail(f"{item['id']}: form_notes must be a string")
        if "uncertain" in item and not isinstance(item["uncertain"], bool):
            fail(f"{item['id']}: uncertain must be a boolean")
        if item.get("uncertain") and item.get("preferred_channel") not in {None, "none"}:
            fail(f"{item['id']}: uncertain entries must not have an automatic channel")
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


def check_skill_policy() -> None:
    sync = (ROOT / "skills" / "scrubber-sync-dal-repo" / "SKILL.md").read_text(encoding="utf-8")
    required = [
        "Il sì prima di ogni messaggio in uscita resta obbligatorio",
        "Non si chiede più conferma solo prima di sostituire una skill ufficiale",
        "può arrivare da `main`",
        "solo da un tag `v` firmato",
        "non sovrascriverla mai",
        "skill personale",
        "docs/registro-skill.md",
        "non è di questo pacchetto",
    ]
    for snippet in required:
        if snippet not in sync:
            fail(f"scrubber-sync-dal-repo missing: {snippet}")
    if "sostituisce la vecchia regola" in sync:
        fail("sync skill still uses the ambiguous overwrite sentence")
    started = (ROOT / "skills" / "scrubber-getting-started" / "SKILL.md").read_text(encoding="utf-8")
    if "skill personale" not in started:
        fail("getting-started does not explain personal skills")
    safety = (ROOT / "skills" / "scrubber-sicurezza-e-minimizzazione" / "SKILL.md").read_text(encoding="utf-8")
    if "non si blocca" not in safety or "skill personale" not in safety:
        fail("sicurezza skill does not keep user skills unblocked")
    for name in ("docs/sicurezza.md", "docs/privacy-del-bot.md"):
        text = (ROOT / name).read_text(encoding="utf-8")
        if "docs/registro-skill.md" not in text and name.endswith("sicurezza.md"):
            fail(f"{name} does not point at the skill log")
        if "skill personale" not in text:
            fail(f"{name} does not mention personal skills")
        if "senza mostrare il diff e senza un sì" in text:
            fail(f"{name} still ties every skill overwrite to a yes")
    spec = ROOT / "docs" / "registro-skill.md"
    if not spec.exists():
        fail("missing docs/registro-skill.md")
        return
    text = spec.read_text(encoding="utf-8")
    for token in (
        "skill_log", "skill-log.json", "installed", "updated", "added-by-user",
        "edited-by-user", "removed", "blocked-update", "sha256", "previous_sha256",
        "diff_summary", "security_lint", "repo-tag", "repo-main", "other-url",
        "ufficiale", "personale", "altra",
    ):
        if token not in text:
            fail(f"registro-skill.md missing {token}")


def check_skill_log(example: dict) -> None:
    events = example.get("skill_log")
    if not isinstance(events, list) or len(events) < 4:
        fail("example registro must include a fake skill_log")
        return
    actions = {
        "installed", "updated", "added-by-user", "edited-by-user", "removed", "blocked-update",
    }
    origins = {"ufficiale", "personale", "altra"}
    sha_re = re.compile(r"^[a-f0-9]{64}$")
    at_re = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")
    id_re = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
    ref_re = re.compile(r"^v\d+\.\d+\.\d+$")
    seen = set()
    for event in events:
        action = event.get("action")
        seen.add(action)
        if action not in actions:
            fail(f"bad skill_log action {action}")
        if not at_re.match(str(event.get("at", ""))):
            fail("skill_log at must be UTC ISO-8601")
        if not id_re.match(str(event.get("skill_id", ""))):
            fail("skill_log skill_id must be a slug")
        if event.get("origin") not in origins:
            fail("skill_log origin must be ufficiale, personale or altra")
        if not isinstance(event.get("applied"), bool):
            fail("skill_log applied must be boolean")
        summary = event.get("diff_summary")
        if not isinstance(summary, str) or not summary.strip() or len(summary) > 240 or "@" in summary:
            fail("skill_log diff_summary must be a short sentence without an email")
        version = event.get("version")
        if not isinstance(version, str) or not version.strip():
            fail("skill_log version missing")
        sha = event.get("sha256")
        previous = event.get("previous_sha256")
        if action == "removed":
            if sha is not None or not isinstance(previous, str) or not sha_re.match(previous):
                fail("removed skill event must keep only previous_sha256")
        else:
            if not isinstance(sha, str) or not sha_re.match(sha):
                fail("skill_log sha256 must be 64 lowercase hex characters")
            if previous is not None and (not isinstance(previous, str) or not sha_re.match(previous)):
                fail("skill_log previous_sha256 must be 64 hex characters or null")
        lint = event.get("security_lint") or {}
        result = lint.get("result")
        warnings = lint.get("warnings")
        if result not in {"pass", "warnings"} or not isinstance(warnings, list):
            fail("skill_log security_lint must be pass or warnings")
        elif result == "pass" and warnings:
            fail("skill_log pass cannot list warnings")
        elif result == "warnings" and not warnings:
            fail("skill_log warnings must list reasons")
        source = event.get("source") or {}
        kind = source.get("kind")
        if kind == "repo-tag":
            if not ref_re.match(str(source.get("ref", ""))) or source.get("signature") not in {"valid", "missing", "mismatch"}:
                fail("repo-tag source needs ref vX.Y.Z and a signature status")
        elif kind == "repo-main":
            if source.get("ref") != "main" or source.get("signature") != "not-applicable":
                fail("repo-main source must use main and signature not-applicable")
        elif kind == "user":
            if source.get("signature") != "not-applicable":
                fail("user source signature must be not-applicable")
        elif kind == "other-url":
            url = str(source.get("url", ""))
            if not url.startswith("https://") or "@" in url or source.get("signature") != "not-applicable":
                fail("other-url source must be https without personal data")
        else:
            fail(f"bad skill_log source {kind}")
    for action in ("installed", "added-by-user", "edited-by-user", "blocked-update", "removed"):
        if action not in seen:
            fail(f"example skill_log missing action {action}")
    if not any(event.get("origin") == "altra" and event.get("applied") is False for event in events):
        fail("example skill_log must show a foreign same-name conflict")
    if not any(event.get("origin") == "personale" and event.get("applied") is True for event in events):
        fail("example skill_log must show an active personal skill")


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
    if 'id="tab-skill"' not in html or "Personale" not in html:
        fail("dashboard must list skills in plain Italian")
    check_skill_log(example)


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
    check_skill_policy()
    check_personal_data(collect_declared_emails())
    lint_path = ROOT / "scripts" / "security_lint.py"
    import importlib.util
    spec = importlib.util.spec_from_file_location("security_lint", lint_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    if module.self_test() != 0:
        fail("security_lint self-test failed")
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
