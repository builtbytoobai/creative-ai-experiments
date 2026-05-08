# AI-Assisted Development Workflow

This document describes the full workflow for building a project with AI support.

---

## Main workflow

1. Start with a project idea
2. Create or update a GitHub repo
3. Add repo instructions: `CLAUDE.md` and `.ai/`
4. Create a GitHub Issue for one focused task
5. Ask Claude Code to propose a plan
6. Ask ChatGPT to review the plan if the change is consequential
7. Ask Gemini for a second opinion if product or UX clarity matters
8. Create a feature branch
9. Let Claude Code implement one focused change
10. Test locally
11. Commit and push the branch
12. Open a Pull Request
13. Let Claude GitHub Actions review the PR automatically
14. Review the PR manually
15. Merge into `main`
16. Delete the branch and pull latest `main`

---

## Rule

One focused change per branch.

One clear PR per task.

No uncontrolled changes directly on `main`.

---

## Ideal loop

```txt
Idea
→ Issue
→ Claude Code plan
→ ChatGPT review (if needed)
→ Gemini second opinion (if needed)
→ Claude Code implementation
→ PR
→ Claude GitHub Actions auto-review
→ human approval
→ merge
```

---

## Handoff protocol

Each handoff in the loop requires specific inputs to produce useful outputs. Passing incomplete information degrades the quality of any review or implementation.

### Idea → GitHub Issue

Include:
- the goal in one or two sentences
- why this matters now
- what is in scope and out of scope
- acceptance criteria
- suggested branch name

### GitHub Issue → Claude Code (planning)

Ask Claude to read `CLAUDE.md`, `.ai/project-brief.md`, and the Issue, then give you:
- interpretation of the task
- proposed implementation plan
- files likely affected
- risks and scope concerns
- suggested test commands
- suggested commit message

Do not ask Claude to edit files at this stage.

### Claude Code plan → ChatGPT (architecture review)

Paste:
- project name and one-line purpose
- relevant README or roadmap summary
- Claude's full plan output

Ask ChatGPT to approve, approve with changes, or reject, and to identify risks, challenge scope, and confirm this is the right thing to build now.

See `external-reviewers.md` for the full copy-paste prompt.

### Claude Code plan → Gemini (UX/product review)

Paste:
- project name and target user description
- the idea, feature description, or Claude's plan
- any existing UX or onboarding context

Ask Gemini to assess product clarity, flag what might confuse users, and suggest the most valuable next step.

See `external-reviewers.md` for the full copy-paste prompt.

### Approved plan → Claude Code (implementation)

Tell Claude:
- the plan is approved
- include any changes requested by ChatGPT or Gemini
- do not commit yet
- after editing, summarize files changed and test commands

### Implementation → Pull Request

PR body should include:
- summary of what changed and why
- list of files changed
- test commands
- related GitHub Issue number
- known limitations, if any

### Pull Request → Claude GitHub Actions

This happens automatically when a PR is opened. Claude GitHub Actions reviews the PR and leaves comments. No prompt needed.

### Claude GitHub Actions review → merge decision

Read the automated review. If it flags issues, address them before merging. If the review is clean, merge the PR and delete the branch.

---

## When to use this workflow

Use this workflow when:

- building a new feature
- refactoring architecture
- improving documentation
- testing product ideas
- adding AI workflows
- preparing a repo for public use

---

## When not to use the full loop

Do not create a full PR flow for tiny local notes, throwaway experiments, or quick private drafts that do not affect repo direction.

Skip ChatGPT and Gemini review for low-risk tasks that are already clearly scoped. See `external-reviewers.md` for guidance on when to skip external review.
