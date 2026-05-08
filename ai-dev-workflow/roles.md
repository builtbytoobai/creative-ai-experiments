# AI Tool Roles

This workflow assigns each AI tool a specific job. No tool does everything.

The user is always the final decision-maker.

---

## The User

The user controls what gets built, approved, and shipped.

The user decides:

- what tasks are created
- when a plan is approved
- when implementation looks correct
- what gets merged
- when a repo is continued, paused, or archived

No AI tool takes action without user approval. The workflow is designed to give the user better information and faster execution — not to replace judgment.

---

## Claude Code

Claude Code is the primary implementation agent.

Use Claude Code for:

- reading and understanding the repo
- proposing implementation plans before editing
- editing files and creating focused changes
- helping write and refine GitHub Issues
- suggesting commit messages
- answering questions about the codebase

Claude Code should always propose a plan first and wait for approval before making changes.

Claude Code should not make large unrelated changes or commit without permission.

---

## Claude GitHub Actions

Claude GitHub Actions is a separate tool from Claude Code. It runs inside GitHub, not on your machine.

Use it for:

- responding to `@claude` mentions in GitHub Issues and Pull Requests
- automatically reviewing Pull Requests when opened
- giving repo-aware feedback without leaving GitHub
- helping with issue planning in the GitHub UI

Claude GitHub Actions does not edit files or run local commands. It reads the repo and responds in comments.

The distinction matters: Claude Code is your local development agent. Claude GitHub Actions is your GitHub-native reviewer.

---

## ChatGPT

ChatGPT is the external architecture, product, and roadmap reviewer.

Use ChatGPT for:

- reviewing Claude Code implementation plans before work starts
- checking architecture decisions and identifying risks
- evaluating whether a feature fits the current roadmap
- challenging scope and avoiding over-engineering
- reviewing important PRs before merge

ChatGPT should challenge the plan before implementation. Its job is to catch problems early, not after code is written.

---

## Gemini

Gemini is the external second-opinion reviewer for product and UX.

Use Gemini for:

- whether the project or feature makes sense to real users
- UX clarity and onboarding quality
- whether an idea is useful and worth building
- alternative product directions
- prompt-system and workflow clarity

Gemini should help judge whether the project feels useful and understandable from a user perspective.

---

## Summary

| Tool | Job | When |
|---|---|---|
| User | Decide, approve, and direct | Always |
| Claude Code | Plan and implement | Local development |
| Claude GitHub Actions | Review and assist | Inside GitHub |
| ChatGPT | Architecture and roadmap review | Before implementation |
| Gemini | UX and product review | When usefulness is uncertain |
