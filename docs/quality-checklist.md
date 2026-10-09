# Prompt quality checklist

Use this checklist when reviewing changes or comparing generated prompts. This is a **manual evaluation guide**, not evidence of benchmark superiority.

## Before judging the output

Record the raw user request, model name/version if known, relevant earlier context, any clarification answers, and the generated prompt. Never publish private data or credentials.

## Evaluation questions

Rate each criterion **Pass / Partial / Fail** and add a concrete observation.

| Criterion | Question |
| --- | --- |
| Intent | Does the prompt preserve what the user actually wants? |
| Specificity | Can an executing assistant act without guessing at essentials? |
| Relevance | Is every requested section or constraint needed for this task? |
| Efficiency | Could the prompt be shorter without harming execution? |
| Questions | Were questions limited to information that materially changes the result? |
| Domain fit | Are technical, design, research, or writing needs handled appropriately? |
| Honesty | Does the prompt avoid fabricated sources, access, tests, and facts? |
| Safety | Are meaningful risks given checks or approval gates when relevant? |
| Output | Is the requested deliverable or format clear? |
| Portability | Can the prompt be pasted and understood without hidden dependencies? |

## Minimum smoke-test set

Run the compiler in a fresh AI chat for each input:

1. "Write a friendly reminder to pay an invoice." — should compile directly.
2. "Give me a recipe for four people using rice and eggs." — should stay simple.
3. "Validate my startup idea." — should ask what the idea is before assuming details.
4. "Review my homepage visuals, not the backend." — should preserve visual-only scope.
5. "Fix the failing tests in my Next.js project." — should ask the executing agent to inspect actual errors and files, not invent a cause.
6. "Migrate production data without downtime." — should request a plan, risk mitigation, and approval before major changes.
7. "Research current funding for early-stage founders in the Gulf." — should require up-to-date evidence and clear eligibility criteria.
8. "Merge my two courses using videos and quizzes." — should ask the executing agent to inspect course materials and preserve alignment.

If a model response differs, document that observation. Do not label example prompts as validated test results unless they were actually tested.

## Suggested comparison method

Compare the same raw input using a generic rewrite instruction and YourWordsToPrompt, keeping model and relevant context as comparable as practical. Use the checklist above, retain both outputs, and identify tradeoffs. Report failures too; do not claim a measured advantage without reproducible evidence.
