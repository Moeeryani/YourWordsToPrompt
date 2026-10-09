# Examples: everyday words → better prompts

These are **illustrative examples**, not automatic test outputs or benchmark claims. Real outputs can vary across models. The important distinction is *how much structure the task actually needs*.

## 1. Simple writing task — compile immediately

**Your words**

> Write a friendly email to my manager asking to move our Tuesday meeting to Thursday.

**Illustrative Master Prompt**

> Draft a short, friendly, professional email to my manager asking to reschedule our Tuesday meeting to Thursday. Make the request polite, avoid giving an invented reason, and include a subject line. Return only the email.

**Why:** The request is clear. Asking about five tone preferences would add friction.

## 2. A coding task — preserve the workflow

**Your words**

> My React checkout form loses everything when there's an error. Fix it properly and add tests.

**Illustrative Master Prompt**

> Act as a senior React engineer. Inspect the existing checkout form, state-management approach, error handling, and test conventions. Identify why field values disappear after validation or submission failures. Implement the smallest robust fix while preserving entered values and avoiding regressions. Add tests covering validation failures, network failures, retries, and successful submission. Run the relevant test suite and report the root cause, files changed, and test results. Do not claim tests passed unless they ran.

**Why:** The prompt calls for codebase inspection and verification. It does not invent files or a framework beyond React.

## 3. A product idea — clarify the one blocker

**Your words**

> Help me figure out if my business idea would work.

**Appropriate next response**

### 🛠️ Architectural Diagnosis
- **Task & Complexity:** Strategy / Medium
- **Secondary Task:** Research
- **Activated Dimensions:** Domain, Audience, Output, Decision criteria
- **Pruned:** Financial forecasting and investor-pitch production before the idea is defined
- **Planned Prompt Sections:** Idea, target customer, validation approach, decision criteria
- **Missing Critical Information:** What the business idea is

### ❓ Calibration Questions

What does your business do, and who do you expect would pay for it?

**Why:** A business idea cannot be validated without knowing what it is. The assistant should not fabricate an industry.

## 4. A visual-only website audit — honor the boundary

**Your words**

> I want an expert to check my website's UI design before launch, every screen, even for people who aren't good with technology. No backend review.

**Illustrative Master Prompt**

> Act as a senior UI designer reviewing a pre-launch website. Inspect every accessible page, important UI state, and responsive layout. Evaluate visual hierarchy, typography, spacing, color and contrast, consistency, affordances, accessibility, and comprehension for both technically confident and low-tech users. Report issues page-by-page with evidence, severity, and specific visual recommendations. Separate confirmed observations from areas you could not access. Focus **only on interface design**; do not expand the work into backend architecture or product strategy. If the website URL is unavailable, request it before performing the review.

**Why:** Visual-design scope is explicitly preserved.

## 5. Research task — request evidence, not certainty

**Your words**

> Compare the best ways to fund a small AI startup in the Gulf.

**Illustrative Master Prompt**

> Act as a startup funding researcher. Research relevant accelerators, grants, startup programs, and angel/VC pathways for an early-stage AI startup seeking opportunities in GCC countries. Use current primary sources where available. For each opportunity, compare eligibility, geographic and incorporation requirements, funding terms, deadlines, stage fit, and application process. Distinguish verified requirements from interpretations or unknowns. Finish with a prioritized shortlist and concrete next steps. Do not invent open calls, deadlines, or funding amounts.

**Why:** Funding criteria change, so the execution prompt explicitly asks for verification.

## 6. High-impact infrastructure change — include a checkpoint

**Your words**

> Migrate our production Postgres database to a new provider without downtime.

**Illustrative Master Prompt**

> Act as a senior database reliability engineer. First inspect the current topology, data volume, replication options, dependencies, backup strategy, and rollback constraints. Propose a migration plan addressing data integrity, replication/cutover, observability, rehearsal, rollback, and verification. Identify assumptions and risks. **Do not change production systems or execute a cutover until the plan is reviewed and approved.** When authorized, execute only the approved steps and provide verification results.

**Why:** Safety and review add value here but would be unnecessary for the simple email example.

---

Have a better example? Please contribute one with a **raw request**, a **representative compiled prompt or clarification**, and a short explanation of the adaptation. Remove personal data and secrets before sharing.
