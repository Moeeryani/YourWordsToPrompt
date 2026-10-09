#!/usr/bin/env python3
"""Offline 12-case compiler conformance checker; NOT a live model benchmark."""
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
APPROVED_SHA = "819450e4d4583a99ddeb68a19bb78686fef597d2"
FENCE = chr(96) * 3
HEAD = "### 🚀 The Lean Master Prompt"
DIAG = "### 🛠️ Architectural Diagnosis"
QUEST = "### ❓ Calibration Questions"
FIELDS = ("Task & Complexity", "Secondary Task", "Activated Dimensions", "Pruned",
          "Planned Prompt Sections", "Missing Critical Information")
DOMAINS = {"Coding", "UI/UX", "Research", "Writing", "Strategy", "Operations", "Analysis", "General"}
COMPILE = re.compile(r"\A" + re.escape(HEAD) + r"\n+" + re.escape(FENCE) +
                     r"markdown\n([\s\S]+?)\n" + re.escape(FENCE) + r"\s*\Z")


def source_errors(root=ROOT):
    errors = []
    raw = (root / "prompts/MASTER_PROMPT.md").read_bytes()
    actual = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\x00" + raw).hexdigest()
    if actual != APPROVED_SHA:
        errors.append("Official Master Prompt was changed without updating approved version pin.")
    master = raw.decode("utf-8")
    marker = chr(96) * 4 + "text\n"
    parts = master.split(marker, 1)
    if len(parts) != 2 or ("\n" + chr(96)*4) not in parts[1]:
        errors.append("Cannot find official compiler text block.")
        return errors
    canonical = parts[1].split("\n" + chr(96)*4, 1)[0]
    if not canonical.startswith("<SYSTEM_ARCHITECTURE>") or not canonical.endswith("</FINAL_BEHAVIOR_RULES>"):
        errors.append("Compiler architecture/end rules missing.")
    skill = (root / "skills/your-words-to-prompt/SKILL.md").read_text(encoding="utf-8")
    if not skill.startswith("---\n") or not skill.endswith(canonical + "\n"):
        errors.append("Agent Skill differs from canonical compiler text.")
    return errors


def manifest_errors(cases, responses):
    errors = []
    ids = [c["id"] for c in cases]
    if len(cases) != 12 or len(set(ids)) != 12:
        errors.append("Manifest must have exactly 12 unique cases.")
    if set(ids) != set(responses):
        errors.append("Response IDs must match case IDs exactly.")
    for i, case in enumerate(cases, 1):
        ident = case["id"]
        if not ident.startswith(f"{i:02d}-"):
            errors.append(f"{ident}: ID order is wrong.")
        if case.get("domain") not in DOMAINS or case.get("complexity") not in ("Simple","Medium","Complex"):
            errors.append(f"{ident}: invalid family/complexity.")
        if case.get("phase") not in ("compile", "clarify"):
            errors.append(f"{ident}: invalid phase.")
        if not case.get("input") or not isinstance(case.get("context"), list):
            errors.append(f"{ident}: input/context missing.")
        if not isinstance(case.get("manual_checks"), list) or not case["manual_checks"]:
            errors.append(f"{ident}: manual checks missing.")
        if not isinstance(case.get("check_patterns"), list):
            errors.append(f"{ident}: regex patterns missing.")
    return errors


def response_errors(case, response):
    if not isinstance(response, str) or not response.strip():
        return ["Missing response."]
    text = response.strip()
    errors = []
    if case["phase"] == "compile":
        match = COMPILE.fullmatch(text)
        if not match:
            return ["Compilation needs exact heading, one fenced markdown block, no other prose."]
        body = match.group(1)
        if DIAG in body or QUEST in body:
            errors.append("Calibration sections leaked into compiled prompt.")
        for pattern in case.get("check_patterns", []):
            if not re.search(pattern, body, re.IGNORECASE):
                errors.append("Missing expected topic cue: " + pattern)
    else:
        if HEAD in text or FENCE in text:
            errors.append("Clarification includes a compiled prompt.")
        if not text.startswith(DIAG + "\n") or text.count(DIAG) != 1:
            errors.append("Missing or duplicated exact diagnosis heading.")
        if text.count(QUEST) != 1 or text.count("\n### ") != 1:
            errors.append("Wrong calibration heading structure.")
        sections = text.split(QUEST, 1)
        front = sections[0]
        positions = []
        for field in FIELDS:
            matches = list(re.finditer(r"(?m)^- \*\*" + re.escape(field) + r":\*\* \S.*$", front))
            if len(matches) != 1:
                errors.append("Missing or duplicated diagnosis field: " + field)
            else:
                positions.append(matches[0].start())
        if len(positions) == 6 and positions != sorted(positions):
            errors.append("Diagnosis fields not in official order.")
        tail = sections[1].strip() if len(sections) == 2 else ""
        if not (1 <= tail.count("?") <= 3):
            errors.append("Expected 1–3 questions using question-mark heuristic.")
    return errors


def evaluate(cases, responses, check_source=True):
    manifest = manifest_errors(cases, responses)
    source = source_errors() if check_source else []
    rows = [{"id": c["id"], "phase": c["phase"], "issues": response_errors(c, responses.get(c["id"])),
             "manual_review_required": c["manual_checks"]} for c in cases]
    passes = sum(not row["issues"] for row in rows)
    return {"suite": "Sovereign Adaptive Compiler offline conformance",
            "provenance": "Fixture responses are manually authored, not model outputs.",
            "models_called": 0, "model_reliability_verified": False, "manual_review_done": False,
            "count": len(rows), "automated_passes": passes, "automated_failures": len(rows)-passes,
            "manifest_issues": manifest, "source_issues": source, "results": rows,
            "success": passes == len(rows) and not manifest and not source}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cases", type=Path, default=ROOT / "tests/cases.json")
    parser.add_argument("--responses", type=Path, default=ROOT / "tests/reference_responses.json")
    parser.add_argument("--json-report", type=Path)
    args = parser.parse_args()
    try:
        cases = json.loads(args.cases.read_text(encoding="utf-8"))["cases"]
        responses = json.loads(args.responses.read_text(encoding="utf-8"))["responses"]
        result = evaluate(cases, responses)
    except (OSError, UnicodeError, ValueError, KeyError, TypeError) as err:
        print("Input or source validation error:", err, file=sys.stderr)
        return 2
    print(f"Offline fixture checks: {result['automated_passes']}/{result['count']} passed.")
    for message in result["manifest_issues"] + result["source_issues"]:
        print("ERROR:", message)
    for row in result["results"]:
        if row["issues"]:
            print("FAIL:", row["id"], "; ".join(row["issues"]))
    print("No AI model was called; these are structural/keyword checks only.")
    print("Manual quality reviews and model-run experiments remain necessary.")
    if args.json_report:
        args.json_report.parent.mkdir(parents=True, exist_ok=True)
        args.json_report.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print("Saved report:", args.json_report)
    return 0 if result["success"] else 1


if __name__ == "__main__":
    sys.exit(main())
