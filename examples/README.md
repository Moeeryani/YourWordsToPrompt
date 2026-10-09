# Examples — everyday words to a lean Master Prompt

Examples are **illustrative**, not automatically generated or benchmarked. Each follows the two-phase output contract in the [official compiler](../prompts/MASTER_PROMPT.md). The compiler chooses **one path**: calibration when essential facts are missing, or direct compilation otherwise.

## 1. Simple writing — no interrogation

**Your words:** "Write a polite email asking to reschedule Tuesday's meeting to Thursday."

**Illustrative compiler output:**

### 🚀 The Lean Master Prompt

```markdown
Draft a short, polite email to my manager asking to move our Tuesday meeting to Thursday. Include a subject line and a friendly professional tone. Don't invent a reason for the change. Return just the email.
```

**Why:** Enough information already exists. A lengthy diagnosis would waste effort.

## 2. Strategy with critical missing information — ask first

**Your words:** "Help me figure out whether my startup idea would work."

**Illustrative compiler response:**

### 🛠️ Architectural Diagnosis
- **Task & Complexity:** Strategy / Medium
- **Secondary Task:** Research
- **Activated Dimensions:** Domain, Target Audience, Output Format
- **Pruned:** Detailed financial forecasting and fundraising materials before the idea is defined
- **Planned Prompt Sections:** Product idea, customer segment, validation method, decision criteria
- **Missing Critical Information:** The actual idea and intended customer

### ❓ Calibration Questions

What does the business offer, and who is the intended customer?

**Why:** This is a true blocker. Once the answer arrives, the compiler should stop asking and produce one final prompt.

## 3. Coding — inspect, plan, verify

**Your words:** "My React checkout form clears itself after validation errors. Fix it and test it."

**Illustrative compiler output:**

### 🚀 The Lean Master Prompt

```markdown
Act as a senior React engineer. Inspect the existing checkout code, validation logic, state management, and test setup. Identify why values disappear after validation errors. Outline a concise plan and any assumptions or regression risks, then implement the smallest safe fix. Test validation failures, retries, and successful submission using the repository's test conventions. Report the cause, changes, and real test results; never claim tests passed if they were not run. Before any major changes, request approval.
```

**Why:** Codebase inspection and testing matter. Invented file paths would not.

## 4. Visual-only UI/UX — honor scope

**Your words:** "Check the visual design of all pages on my beta website for both beginners and tech-savvy people. Not backend."

**Illustrative compiler output:**

### 🚀 The Lean Master Prompt

```markdown
Act as a senior UI designer. Audit the visual design of all accessible pages and important interface states in my beta website. Assess visual hierarchy, typography, spacing, color, consistency, clarity, usability for novice and experienced users, and accessibility/responsive details where they affect the design. Report specific issues page by page with severity, evidence, and concrete design improvements. Identify pages you cannot access; do not invent findings. Exclude backend, security, and infrastructure work. Ask for the website URL only if you need it to start the actual audit.
```

**Why:** A visual-only request should not expand into unrelated development.

## 5. Research — clarify evidence standards

**Your words:** "Compare the most relevant startup funding options for an AI startup in Gulf countries."

**Illustrative compiler output:**

### 🚀 The Lean Master Prompt

```markdown
Act as a startup funding researcher. Compare grants, accelerators, investment programs, and other appropriate early-stage AI startup funding options in GCC countries. Prioritize relevance to an early-stage startup and eligibility for applicants without an established Gulf entity where applicable. Verify current requirements, application dates, incorporation constraints, funding terms, and stages using credible primary sources. Distinguish confirmed details from unknowns. Return a concise comparison table, a prioritized shortlist with rationale, and application next steps. Do not invent deadlines or award amounts.
```

**Why:** Research claims and eligibility conditions need evidence; this is not a generic writing prompt.

## 6. High-impact coding — propose a plan, wait for approval

**Your words:** "Migrate our production Postgres database to a new provider without downtime."

**Illustrative compiler output:**

### 🚀 The Lean Master Prompt

```markdown
Act as a senior database reliability engineer. Inspect the current production Postgres topology, replication support, size, dependencies, backup process, and recovery constraints. Propose a concise migration plan covering rehearsal, data consistency, monitoring, cutover, rollback, and verification. Explicitly identify risks, assumptions, and any conditions that make zero downtime unrealistic. Present the plan and WAIT FOR APPROVAL before executing any major or production-changing steps. Once authorized, follow only the approved plan and report verification outcomes.
```

**Why:** High-impact changes require explicit review instead of blind execution.

---

See [how the compiler chooses instructions](../docs/how-it-works.md). To contribute a new example, supply a privacy-safe raw request, the illustrative response, and a brief rationale. Do not present hypothetical outputs as measured test results.
