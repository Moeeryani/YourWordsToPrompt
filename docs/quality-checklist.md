# Compiler conformance and quality checklist

Use this for **manual checks and reproducible experiments**, not as evidence of benchmark superiority. The authority for behavior is [the official Master Prompt](../prompts/MASTER_PROMPT.md).

## Structural conformance

For each sample, verify:

- [ ] The primary task family is one of Coding, UI/UX, Research, Writing, Strategy, Operations, Analysis, General.
- [ ] Task complexity is assessed independently of the domain.
- [ ] A secondary task family is used only when beneficial.
- [ ] Irrelevant cognitive dimensions, risk sections, assumptions, file lists, and plans are pruned.
- [ ] When essential information is missing, the response uses exactly **Architectural Diagnosis** with the six required fields and **Calibration Questions**.
- [ ] Questions are limited to **1–3 high-value grouped items**, with no more than one extra clarification round.
- [ ] Once information suffices, the response uses exactly `### 🚀 The Lean Master Prompt` and **one fenced markdown block**.
- [ ] No internal dimension selection or pruning analysis appears in the compiled final prompt.
- [ ] High-impact coding includes a review-and-approval checkpoint.
- [ ] The generated prompt does not invent files, access, facts, tests, sources, or credentials.

## Quality ratings

Record **Pass / Partial / Fail** with concrete evidence for: intent fidelity, missing information handling, relevance, brevity, domain fit, execution-readiness, risks, and output format.

## Minimum exploratory inputs

1. "Write a polite reminder about an unpaid invoice." → Simple Writing: compile directly.
2. "Suggest a three-ingredient lunch with eggs and rice." → Simple General: no unnecessary sections.
3. "Tell me if my startup idea will succeed." → Strategy: ask what the idea is.
4. "Evaluate only my website's visual design." → UI/UX: no unrelated backend scope.
5. "Fix a failing test in my Python repo." → Coding: refer to actual repo inspection, don't invent the failure.
6. "Move our production database with no downtime." → Complex Coding: propose plan and require approval.
7. "Find current AI startup grants in the Gulf." → Research: require reliable, current evidence.
8. "Merge two training courses using existing videos and questions." → Strategy/Analysis: have the executing agent review course materials before planning changes.

## Testing notes

Save the input, relevant conversation context, output, model/version and date (if known), and explicit limitations. Compare like-for-like cases; report failures as well as strengths. Do not publish private information or make performance claims without evidence.
