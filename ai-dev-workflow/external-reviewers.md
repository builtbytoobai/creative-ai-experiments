# External Reviewers

This workflow uses ChatGPT and Gemini as external reviewers alongside Claude Code.

They do not replace Claude Code. They improve the decisions made before and after implementation.

---

## Why external review matters

Claude Code is an excellent builder but it works inside your repo and your current context. It can miss broader risks, roadmap misalignment, or product-level problems.

External reviewers provide an outside perspective:

- ChatGPT challenges the plan before any code is written.
- Gemini asks whether the result is useful and clear to real users.

Together they reduce the chance of building the wrong thing correctly.

---

## ChatGPT Review Role

ChatGPT is used as an external architecture, product, and roadmap reviewer.

Use ChatGPT for:

- reviewing Claude Code implementation plans
- checking architecture decisions
- identifying risks and edge cases
- evaluating roadmap fit
- avoiding over-engineering
- reviewing whether a feature should be built now or later
- improving GitHub Issues before Claude implements them
- reviewing important PRs before merge

ChatGPT should challenge the plan before implementation.

---

## ChatGPT review prompt

```txt
Review this Claude Code implementation plan as an external architecture, product, and roadmap reviewer.

Project:
[project name]

Current state:
[paste repo summary or relevant README/roadmap]

Claude plan:
[paste Claude's plan]

Review for:
- product value
- architecture quality
- maintainability
- implementation risk
- missing edge cases
- over-engineering
- roadmap alignment

Give me:
- approve / approve with changes / reject
- what is strong
- what should change before implementation
- edge cases
- acceptance criteria
- test commands
- whether this should be built now
```

---

## Gemini Review Role

Gemini is used as an external second-opinion reviewer for product and UX.

Use Gemini for:

- user experience perspective
- product usefulness
- product clarity
- onboarding quality
- beginner friendliness
- alternative product directions
- whether an idea makes sense to real users
- whether a workflow feels easy to understand

Gemini should help judge whether the project feels useful, clear, and understandable.

---

## Gemini review prompt

```txt
Review this project idea or feature as an external UX, product, and usefulness reviewer.

Project:
[project name]

Target user:
[describe user]

Current idea or feature:
[paste idea, README, roadmap, issue, or plan]

Review for:
- usefulness
- clarity
- user experience
- onboarding
- product potential
- what might confuse users
- what should be simplified
- what would make this more valuable

Give me:
- overall assessment
- strengths
- weaknesses
- missing pieces
- suggested improvements
- product opportunities
- best next step
```

---

## When to use ChatGPT

Use ChatGPT when the question is:

- Is this architecture good?
- Is this too much scope?
- Does this fit the roadmap?
- What edge cases are missing?
- Should Claude implement this?
- Is this PR safe to merge?

---

## When to use Gemini

Use Gemini when the question is:

- Would this make sense to a new user?
- Is this product idea useful?
- Is the UX clear?
- What would make this more valuable?
- What might confuse people?
- Does this feel like something people would actually use?

---

## When not to use external reviewers

Skip ChatGPT and Gemini for:

- small documentation fixes with no architectural impact
- quick typo or formatting corrections
- tasks that are already clearly scoped and low risk
- experiments that are throwaway and not heading toward production

External review adds value when a decision is consequential. It adds friction when the task is already obvious.

---

## Decision rule

Claude can build.

ChatGPT can challenge the plan.

Gemini can give a second opinion.

The user decides.
