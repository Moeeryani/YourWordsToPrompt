<div align="center">

# YourWordsToPrompt

### Your words. A better AI prompt.

**Write what you want in everyday language. Get a clear, ready-to-use prompt tailored to your task.**

No prompt-engineering experience. No bloated templates. No unnecessary questions.

**[Get started](#get-started-in-30-seconds)** · **[See examples](examples/README.md)** · **[How it works](docs/how-it-works.md)**

</div>

---

## From your words to a useful prompt

| Your words | YourWordsToPrompt helps you create |
| --- | --- |
| "I have an app idea. Help me figure out whether people would use it." | A focused validation prompt covering target users, assumptions, research, and decision criteria. |
| "Check my website's design before launch. Be really critical." | A UI/UX audit prompt with scope, user perspectives, evaluation criteria, and prioritized findings. |
| "Help me write an email asking for an extension, but make it polite." | A concise writing prompt with audience, intent, tone, and output format. |

**One input style, different levels of detail.** A simple request gets a simple prompt. A high-stakes or complex request gets the structure it actually needs.

## Get started in 30 seconds

You don't need to install anything or run code.

1. **Open the [Master Prompt](prompts/MASTER_PROMPT.md)** and copy its contents.
2. **Paste it into ChatGPT, Claude, or another AI assistant** as project/custom instructions, or as the first message in a new chat if your assistant doesn't support custom instructions.
3. **Write your idea normally.** For example: `I want to launch an online bakery but I don't know where to start.`
4. **Get your ready-to-use prompt.** If an essential detail is missing, the assistant asks a small number of focused questions first.
5. **Copy the generated prompt into your preferred AI assistant** to perform the actual task.

> **Important:** This repository currently provides instructions for an AI assistant—not a hosted prompt-conversion website. Outputs vary by model and context.

### The idea in one line

```text
Your everyday words → Understand the task → Ask only if necessary → Ready-to-use AI prompt
```

## What makes it adaptive?

| Your request | What the compiler does |
| --- | --- |
| **Simple and clear** | Writes one short, useful prompt immediately. |
| **Important details missing** | Asks up to three targeted questions, rather than a lengthy questionnaire. |
| **Complex or high-impact** | Includes relevant constraints, planning, deliverables, and safeguards. |
| **Different domains** | Adapts to coding, UI/UX, research, writing, strategy, analysis, and operations. |

The goal is **not** to make every prompt longer. The goal is to make every instruction earn its place.

## Ways to use it

- **Copy and paste:** Use [the complete Master Prompt](prompts/MASTER_PROMPT.md) in any compatible conversational AI.
- **As an agent skill:** See [`skills/your-words-to-prompt/SKILL.md`](skills/your-words-to-prompt/SKILL.md), packaged using the [Agent Skills format](https://agentskills.io/specification). Installation depends on the agent you use.
- **Learn by example:** Explore [realistic transformations](examples/README.md), including when the assistant should ask questions instead of guessing.

## Example: a UI/UX audit

**You say:**

> I built a website. I want someone to review all the design and tell me what looks unprofessional before beta launch.

**An illustrative compiled prompt:**

> Act as a senior product and UI/UX designer. Review the website's visual design across every accessible page and responsive breakpoint. Assess hierarchy, typography, consistency, spacing, navigation clarity, forms, feedback states, accessibility, and first-time usability. Consider both confident and low-tech users. Identify specific problems, explain their impact, and recommend concrete improvements. Prioritize findings by severity and show the affected page or component. Do not invent observations for pages you cannot access.

For a website audit, an assistant may first ask for the website URL if it is needed and unavailable. **[See more examples →](examples/README.md)**

## Project files

| File | Purpose |
| --- | --- |
| [`prompts/MASTER_PROMPT.md`](prompts/MASTER_PROMPT.md) | The copy-and-paste prompt; primary behavioral reference. |
| [`skills/your-words-to-prompt/SKILL.md`](skills/your-words-to-prompt/SKILL.md) | A portable skill adaptation for compatible agents. |
| [`examples/README.md`](examples/README.md) | Simple, ambiguous, and complex sample transformations. |
| [`docs/how-it-works.md`](docs/how-it-works.md) | Design decisions and the two possible response flows. |
| [`docs/quality-checklist.md`](docs/quality-checklist.md) | A transparent way to evaluate generated prompts. |
| [`ROADMAP.md`](ROADMAP.md) | Planned improvements, not shipped features. |

## What it does *not* do

YourWordsToPrompt does not guarantee better model performance for every task, conduct research on its own, deploy code, or magically execute the generated prompt. It is an **adaptive prompt compiler**: it helps you tell an AI assistant what you want with less effort. Treat examples as illustrations, not measured benchmark results.

## Contributing

Issues, examples, documentation improvements, accessibility feedback, and model-specific compatibility reports are welcome. Start with [CONTRIBUTING.md](CONTRIBUTING.md). Please don't include private chat logs, credentials, or confidential prompts in public issues.

If this project helps you explain what you want to AI more clearly, consider ⭐ starring the repository so others can discover it.

## License

[MIT](LICENSE) © 2026 Moeeryani.
