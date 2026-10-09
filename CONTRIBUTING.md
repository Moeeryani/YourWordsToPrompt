# Contributing to YourWordsToPrompt

Thank you for helping make plain-language prompt creation accessible.

## Most valuable contributions

- Beginner-friendly examples covering simple, ambiguous, and complex requests.
- Issues demonstrating missing intent, unnecessary questions, or template bloat.
- Documentation, accessibility, and language improvements.
- Reproducible conformance reports using [the quality checklist](docs/quality-checklist.md).

Never include private chat logs, user data, passwords, or API keys in public submissions.

## Source of truth — please read before editing

[`prompts/MASTER_PROMPT.md`](prompts/MASTER_PROMPT.md) contains the **maintainer-supplied Sovereign Adaptive Compiler** and is the project's authoritative specification.

Changes to its architecture, dimensions, routing, complexity model, pruning, domain rules, phases, output contracts, or final behavior are **product decisions**—propose them in an issue first. Don't quietly rewrite them while simplifying documentation.

[`skills/your-words-to-prompt/SKILL.md`](skills/your-words-to-prompt/SKILL.md) must remain behaviorally identical to the authoritative instructions apart from its skill metadata and short packaging notes.

For documentation/example pull requests:
1. Preserve the distinction between **calibration** and **compilation**.
2. Use the **exact response headings** and six diagnostic fields.
3. Respect the **1–3 question** limit and **one optional additional round**.
4. Avoid unnecessary sections; mirror domain-specific behaviors.
5. Add concrete, privacy-safe before/after examples.
6. Disclose tests actually performed; don't claim model-independent guarantees.

## Pull requests

Explain the user problem, show before/after behavior, and reference relevant files. Keep changes focused and follow [the Code of Conduct](CODE_OF_CONDUCT.md).

## Issue reports

Include the raw request (redacted), desired behavior, actual response, and model/client version when known. You don't need prompt-engineering expertise to contribute.
