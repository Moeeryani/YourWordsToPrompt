# How YourWordsToPrompt works

YourWordsToPrompt is an **instruction set** for a conversational AI model. It converts a user's everyday request into a new prompt the user can reuse. It does not run a hosted service or perform the requested work by itself.

## The adaptation loop

1. **Understand the task.** Identify the primary task family (coding, UI/UX, research, writing, strategy, operations, analysis, or general).
2. **Measure complexity separately.** A technically sophisticated topic may still require a simple prompt; a seemingly ordinary task may have significant risks.
3. **Select only useful instructions.** Include scope, role, constraints, process, output, or checks when they improve the result. Remove everything else.
4. **Check for real blockers.** If one key detail is missing, ask for it. If the task can be compiled without guessing, compile immediately.
5. **Produce one executable prompt.** The user receives a clear Master Prompt rather than a collection of interchangeable templates.

## Two response paths

**Enough information → compilation**

Example request: "Write a polite note asking my instructor for the course syllabus."

The compiler should produce a short writing prompt immediately, without asking the user for a full communication strategy.

**Critical information missing → targeted questions**

Example request: "Evaluate my idea's market fit."

The compiler cannot evaluate an unspecified idea. It should ask what the idea is and who might use or buy it, then compile once answered.

Clarification is limited to up to three focused questions per round, with one optional additional short round for remaining blockers.

## Complexity is not length

The goal is not to maximize output tokens. A high-quality short prompt can be better than a massive generic template if it is appropriate to the task.

- For **simple** requests, make the goal and output explicit.
- For **medium** requests, capture constraints and important tradeoffs.
- For **complex or high-impact** requests, add sequencing, verification, assumptions, and approval gates when appropriate.

## Domain sensitivity

- Coding prompts may need repository inspection, tests, and review before critical changes.
- Design prompts may need accessibility, user journeys, and responsive-state checks.
- Research prompts may need reliable sources and explicit uncertainty.
- Writing prompts usually need reader, purpose, tone, and format.
- Strategy prompts benefit from decision criteria and tradeoffs.

These are **options**, never mandatory universal sections.

## What the compiler cannot guarantee

Language models may misunderstand requests, vary by provider, or ask a question the user considers unnecessary. The compiler does not grant browsing, repository access, or execution permissions. Always review the final prompt before using it for consequential tasks.

## Keep the two distributions aligned

- The maintained **copy-and-paste** instruction set lives in **prompts/MASTER_PROMPT.md**.
- The **skills/your-words-to-prompt/SKILL.md** file is a compact, independently usable adaptation following the Agent Skills format.

When editing behaviors, check both files and update examples when appropriate.
