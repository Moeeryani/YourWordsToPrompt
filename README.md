<div align="center">

# YourWordsToPrompt

### Write what you want. Get the AI prompt you need.

**Turn everyday words or a rough idea into one clear, ready-to-use Master Prompt.**

No prompt engineering knowledge. No generic mega-templates. Only questions that matter.

**[Get started](#quick-start)** · **[See transformations](examples/README.md)** · **[Read the original compiler](prompts/MASTER_PROMPT.md)**

</div>

---

![Your everyday words become an AI prompt, with optional related questions](assets/flow.svg)

*If something important is missing, the compiler may ask 1–2 focused questions to make the prompt fit what you want. Simple requests need no questions. The official specification permits up to three questions per round when necessary.*

## What does it do?

You describe your goal in plain language. **YourWordsToPrompt** follows the **Sovereign Adaptive Compiler** to choose the right task type, assess complexity, omit irrelevant sections, and produce a task-specific Master Prompt you can paste into an AI assistant.

```text
Your words → Task + complexity → Only essential questions (if needed) → One tailored Master Prompt
```

It helps you **write a prompt**; it does not execute that prompt or host a prompt-generation website.

## Quick start

1. Open **[the official Master Prompt](prompts/MASTER_PROMPT.md)**.
2. Copy **only the text inside the large code block**, from `<SYSTEM_ARCHITECTURE>` through `</FINAL_BEHAVIOR_RULES>`. Do not copy the introductory GitHub instructions.
3. Paste it as custom/project instructions into ChatGPT or another compatible AI assistant, or use it as the first chat message.
4. Describe what you want normally: `I want to create a marketing plan for my new bakery.`
5. **If enough information is given**, receive one Master Prompt immediately. **If something critical is missing**, answer up to three focused calibration questions first.
6. Copy the resulting **Lean Master Prompt** into the AI assistant you want to perform the actual task.

> The exact responses depend on the model and context. No model benchmark or universal compatibility guarantee is implied.

## Two possible responses

<details>
<summary><strong>Example A: Clear request → one Master Prompt</strong></summary>

**You type:**

> Write a polite email to reschedule Tuesday's meeting to Thursday.

**Illustrative output:**

### 🚀 The Lean Master Prompt

```markdown
Draft a brief, professional, friendly email asking to move Tuesday's meeting to Thursday. Include a subject line, use a polite tone, and do not invent an explanation for the change. Return only the email.
```

</details>

<details>
<summary><strong>Example B: Missing critical information → targeted questions</strong></summary>

**You type:**

> Help me validate my startup idea.

**Illustrative response:**

### 🛠️ Architectural Diagnosis
- **Task & Complexity:** Strategy / Medium
- **Secondary Task:** Research
- **Activated Dimensions:** Domain, Target Audience, Output Format
- **Pruned:** Detailed financial modeling and pitch-deck creation before the idea is known
- **Planned Prompt Sections:** Idea and audience, validation questions, evidence, decision criteria
- **Missing Critical Information:** What the startup idea does and who it serves

### ❓ Calibration Questions

What is the product or service, and who would use or pay for it?

Once you answer, the compiler produces the Master Prompt.

</details>

## Why it's adaptive

| Feature | How the original Sovereign Adaptive Compiler behaves |
| --- | --- |
| **Task routing** | Coding, UI/UX, Research, Writing, Strategy, Operations, Analysis, General |
| **Independent complexity assessment** | Simple, Medium, or Complex, regardless of domain |
| **Ruthless pruning** | No redundant sections, unnecessary dimensions, or universal templates |
| **Targeted questions** | Maximum three questions in one round; one additional round only if critical gaps remain |
| **Domain-specific rules** | Appropriate guidance for coding, design, research, writing, strategy, operations, and analysis |
| **Strict outputs** | Architectural Diagnosis + Calibration Questions when blocked; otherwise exactly one Lean Master Prompt |
| **High-impact coding safeguards** | Plan and flag risks; wait for approval before major changes where required |

**Short when simple. Structured when necessary.**

## Install / use

- **No installation:** [Copy the official Master Prompt](prompts/MASTER_PROMPT.md) into your AI assistant.
- **Agent Skill:** [`skills/your-words-to-prompt/SKILL.md`](skills/your-words-to-prompt/SKILL.md) holds the full instruction set with skill metadata, for agents that support the [Agent Skills specification](https://agentskills.io/specification). Client-specific installation is not yet verified.
- **Examples:** [Explore prompts and calibration examples](examples/README.md).

## Repository guide

| Location | Purpose |
| --- | --- |
| [`prompts/MASTER_PROMPT.md`](prompts/MASTER_PROMPT.md) | **Authoritative specification supplied by the maintainer** |
| [`skills/your-words-to-prompt/SKILL.md`](skills/your-words-to-prompt/SKILL.md) | Same rules packaged as an agent skill |
| [`examples/README.md`](examples/README.md) | Worked, illustrative interactions |
| [`docs/how-it-works.md`](docs/how-it-works.md) | Explanation of the task router, phases, and pruning |
| [`docs/quality-checklist.md`](docs/quality-checklist.md) | Review criteria and testing scenarios |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | How to propose improvements without changing the contract accidentally |
| [`ROADMAP.md`](ROADMAP.md) | Future possibilities (not shipped features) |

## Limitations and contribution

This is a **prompt-based tool**, not a benchmark-proven optimizer, web app, or autonomous executor. Always review the generated prompt before using it on consequential work. [Report behavior issues or suggest examples](https://github.com/Moeeryani/YourWordsToPrompt/issues) without sharing personal information or credentials.

Contributions are welcome under the [MIT license](LICENSE). If it helps you explain your ideas to AI, consider ⭐ starring the repository.
