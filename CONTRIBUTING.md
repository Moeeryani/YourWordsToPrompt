# Contributing to YourWordsToPrompt

Thanks for helping make prompt creation simpler and more useful.

## Good contributions

- Clearer beginner onboarding or more accessible documentation.
- Realistic raw-request → compiled-prompt examples.
- Reports of prompts that are too long, ask unnecessary questions, or miss important details.
- Improvements to domain-specific behavior or multilingual phrasing.
- Compatibility notes based on actual tests with a named AI assistant.

Please do not submit confidential prompts, personal data, passwords, private URLs, or API keys.

## Before changing the compiler

1. Read **prompts/MASTER_PROMPT.md** and **docs/how-it-works.md**.
2. Explain the user problem and what is currently going wrong.
3. Make a targeted change rather than adding a universal template.
4. Compare behavior on at least one **simple**, one **ambiguous**, and one **complex** request.
5. Keep **skills/your-words-to-prompt/SKILL.md** behaviorally aligned when changing core rules.
6. Describe what you actually tested and what remains unverified.

Use **docs/quality-checklist.md** for review criteria.

## Pull requests

- Keep one main purpose per pull request.
- Link a relevant issue when available.
- Explain the before/after behavior using a privacy-safe example.
- Prefer reproducible examples over anecdotal superiority claims.
- Be respectful in discussion; see **CODE_OF_CONDUCT.md**.

## Reporting issues

Use the repository's issue templates. Include:
- What you asked in everyday language.
- What you expected the compiler to do.
- What actually happened (remove private information).
- Which AI model or interface you tested, if known.

You do not need to know prompt-engineering terminology to contribute.
