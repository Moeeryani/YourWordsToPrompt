# Reproducible conformance testing

This is a deterministic **12-case suite** for the original Sovereign Adaptive Compiler. It checks output shape, six mandatory diagnostic fields, question count, relevant cues and the integrity of the official prompt.

**Reference answers are hand-authored illustrations, not actual model outputs.** Passing checks does **not** demonstrate that ChatGPT, Claude, or any other model consistently follows the rules.

## Run locally

Python 3.10+ is sufficient; no dependencies, API keys, accounts or network access.

```bash
python3 -m unittest discover -s tests -v
python3 scripts/check_conformance.py --responses tests/reference_responses.json --json-report conformance-report.json
```

GitHub Actions also runs the unit tests and offline checker on pushes and pull requests.

## The 12 scenarios

| ID | Family | Complexity | Expected behavior |
| --- | --- | --- | --- |
| 01 | Writing | Simple | Short prompt for a polite email; no questions |
| 02 | General | Simple | Basic lunch recipe without a bloated template |
| 03 | Coding | Simple | Direct standalone Python function |
| 04 | Coding | Medium | Inspect existing React code, plan, fix and test |
| 05 | Coding | Complex | Production migration: plan, risks and approval gate |
| 06 | UI/UX | Medium | Visual-only beta design review, novice and desktop/mobile perspectives |
| 07 | UI/UX | Medium | Conceptual immersive design without implementation |
| 08 | Research | Medium | Current eligibility and evidence requirements |
| 09 | Analysis | Medium | Inspect sales/expenses CSV exports before conclusions |
| 10 | Operations | Complex | Support ownership, escalation and incident handoffs |
| 11 | Strategy | Medium | Missing idea: diagnosis and targeted questions |
| 12 | Strategy | Medium | Follow-up after answered clarification: compile without repeating questions |

Source material is `tests/cases.json`. It includes request, conversation context, rough topic cues, and scenario-specific qualitative checks.

## What is actually verified?

- The official compiler's Git blob hash remains pinned to the maintainer-approved version.
- The Agent Skill includes identical canonical instructions.
- Twelve scenario IDs are present with 12 responses.
- Compilation uses the exact heading and one fenced markdown prompt without extra commentary.
- Calibration uses the exact headings, six fields in their specified order, and 1–3 questions (approximated using question marks).
- A few case-specific keyword cues appear in the response.
- Negative tests deliberately break headings, fields, question limits, and relevance cues to confirm that the checker catches those failures.

These tests **cannot** judge reasoning quality, semantic correctness, actual need for calibration, or whether a prompt is truly better. They do not enforce every subtle rule. Human checks listed per case are still needed.

## Evaluate an actual AI model

1. Paste the full text between the outer code fences of `prompts/MASTER_PROMPT.md` into a fresh model session's instructions, without modifying the original.
2. For each scenario in `tests/cases.json`, send its `input` and preserve any provided `context` in order. In particular, scenario 12 starts after a clarification.
3. Save each complete model response under the matching ID in a **separate** JSON file with a top-level `responses` mapping. Use `tests/reference_responses.json` as the **format example**, not as evidence of actual output.
4. Run `python3 scripts/check_conformance.py --responses YOUR_CAPTURE.json --json-report YOUR_REPORT.json`.
5. Manually review every case's `manual_checks` and `docs/quality-checklist.md` requirements. Record failures and unresolved ambiguities. Document model name/version, date, instruction placement, sampling settings if known, and relevant context.
6. For reliability claims, repeat with fresh sessions and publish the sampling method and limitations. Do not mistake authored fixture passes for model conformance.

**Privacy:** Remove credentials and sensitive conversation content from any shared capture. No model APIs or network calls are made by this checker.

## Repository files

- `tests/cases.json`: 12 reproducible scenarios and manual review points.
- `tests/reference_responses.json`: illustrative reference responses with provenance.
- `scripts/check_conformance.py`: dependency-free structural checker and JSON report.
- `tests/test_checker.py`: fixture integrity and negative-condition unit tests.
- `.github/workflows/conformance.yml`: automated GitHub checks.
