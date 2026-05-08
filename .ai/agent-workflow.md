# Agent Workflow

This file describes how AI agents should support this project.

---

## Roles

### Claude Code

Claude Code is the builder and implementation agent.

Use Claude for:

- reading the repo
- proposing implementation plans
- editing files
- creating focused changes
- helping with GitHub Issues and Pull Requests

### ChatGPT

ChatGPT is the architecture, product, and roadmap reviewer.

Use ChatGPT for:

- reviewing Claude's plan
- checking architecture decisions
- identifying risks
- challenging scope
- reviewing roadmap fit

### Gemini

Gemini is the second-opinion reviewer for UX, usefulness, product clarity, and alternative perspectives.

Use Gemini for:

- UX perspective
- product usefulness
- onboarding clarity
- second opinion on project direction

---

## Standard flow

1. Create a clear GitHub Issue.
2. Ask Claude Code for a plan.
3. Review the plan with ChatGPT if the change is important.
4. Ask Gemini for product/UX second opinion if relevant.
5. Approve Claude to implement one focused change.
6. Test locally.
7. Commit and push.
8. Open PR.
9. Review.
10. Merge only after human approval.

---

## Rule

AI tools assist.

The user decides.