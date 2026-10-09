# How YourWordsToPrompt works

This document **explains** the original specification; it does not replace or override [the authoritative compiler](../prompts/MASTER_PROMPT.md).

## The compiler's core promise

Turn a natural-language idea into **one lean, high-performance Master Prompt**. Avoid universal templates, unnecessary dimensions, and redundant instructions. Structure scales with **domain, complexity, ambiguity, and execution risk**.

The prompt compiler itself does not execute the task or create tools/permissions that are not actually available.

## Task routing and complexity

**Primary task families:** Coding, UI/UX, Research, Writing, Strategy, Operations, Analysis, General. A secondary family is optional and only improves the compiled prompt when materially relevant.

Complexity is assessed **independently**:
- **Simple:** clear goal, low risk, minimal dependencies → concise direct compilation.
- **Medium:** needs context or tradeoff management → appropriate structure.
- **Complex:** multiple steps, significant ambiguity, dependencies, or risk → targeted planning and safeguards.

The compiler selectively chooses among Level, Function, Domain, Thinking Style, Authority, Operating Mode, Behavior, Output Format, Target Audience, and Relationship to User. These are **internal tools**, not a required questionnaire or mandatory output headings.

## Phase 1 — Triage & Interrogation

Every new idea is assessed for task type, complexity, high-value dimensions, and unnecessary elements. Ask questions **only when critical information is missing**.

- At most **three targeted, grouped questions** in one round.
- At most **one additional short round** for unresolved critical gaps.
- Stop questioning once enough information exists.

If blocked, output the **exact** six-field `### 🛠️ Architectural Diagnosis` followed by `### ❓ Calibration Questions`. Do not substitute an unstructured chat response or ask for optional preferences.

## Phase 2 — Compilation

When information is sufficient, output **only**:

```text
### 🚀 The Lean Master Prompt
```

followed by **one fenced `markdown` code block** containing the Master Prompt. Do not reveal internal dimensions or pruning decisions in this phase.

## Selective domain behavior

- **Coding:** Simple coding gets a direct prompt. Medium/complex coding calls for examining the codebase, a concise plan, assumptions, risks, and then action as appropriate. High-impact changes must wait for approval after the plan. The specification's final-output example also calls for a complex coding prompt to request approval before major changes.
- **UI/UX:** User flows, hierarchy, accessibility, responsiveness, and existing patterns are included **only when relevant**. Conceptual design is not forced into implementation detail.
- **Research:** Clarify objective, scope, market/audience, constraints, method, and output format if useful. Caveats matter when uncertainty or source quality is material.
- **Writing:** Prioritize purpose, audience, tone, constraints, sources, and format—not technical sections.
- **Strategy / Analysis / Operations:** Prioritize objective, decision context, tradeoffs, criteria, process logic, and a useful deliverable.

## Pruning

Add the following only when they materially improve execution: files/areas to touch, risks, assumptions, accessibility, definition of done, or breakdown/plan. Do not mechanically include them all.

## Source consistency

The **authoritative source** is [`prompts/MASTER_PROMPT.md`](../prompts/MASTER_PROMPT.md); the [Agent Skill](../skills/your-words-to-prompt/SKILL.md) contains the same instruction text with skill metadata. Review both when editing either one.

The original pasted source omitted the closing backticks after the Phase 2 output example. A single closing Markdown fence was supplied in the published copy to keep `</INTERACTION_PROTOCOL>` and the final behavior rules outside the example.

## What remains unverified

Model-by-model reliability, user-study effectiveness, benchmarks, and installation on particular skill clients have not been validated by this repository.
