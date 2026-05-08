# Setup Checklist — Applying the AI Dev Workflow to a New Repo

Use this checklist when starting a new project and you want to apply the builtbytoobai AI-assisted development workflow.

Follow the steps in order. Each step should take under five minutes.

---

## Purpose

This checklist ensures a new repo has everything needed to use the full workflow:

- Claude Code as the implementation agent
- GitHub Issues for task planning
- Feature branches and Pull Requests for safe changes
- Claude GitHub Actions for automated PR review
- ChatGPT and Gemini as external reviewers

---

## Prerequisites

Before you start:

- [ ] Git is installed locally
- [ ] GitHub repo exists (public or private)
- [ ] Claude Code is installed (`npm install -g @anthropic-ai/claude-code` or via the desktop app)
- [ ] You have access to ChatGPT and Gemini for external review

---

## Step 1 — Copy repo instructions

1. Copy `templates/CLAUDE.md` from this directory into the new repo root as `CLAUDE.md`.
2. Open it and fill in:
   - `[PROJECT_NAME]`
   - `[SHORT_PROJECT_PURPOSE]`
   - `[TECH_STACK]`
   - `[MAIN_FILE_OR_COMMAND]`
   - `[FILES_TO_AVOID]`
   - `[TEST_COMMAND_1]` and `[TEST_COMMAND_2]`

---

## Step 2 — Set up the .ai/ folder

1. Create a `.ai/` folder in the repo root.
2. Copy these files from `templates/` into `.ai/`:
   - `project-brief.md`
   - `agent-workflow.md`
   - `coding-rules.md`
   - `task-template.md`
3. Fill in the `[PLACEHOLDER]` values in each file.

---

## Step 3 — Set up GitHub templates (optional)

1. Create a `.github/` folder in the repo root if it does not exist.
2. Copy `templates/issue-template.md` into `.github/ISSUE_TEMPLATE/task.md`.
3. Copy `templates/pr-template.md` into `.github/pull_request_template.md`.

These templates make GitHub Issues and PRs consistent with the workflow.

---

## Step 4 — Install Claude GitHub Actions

Inside Claude Code, run:

```txt
/install-github-app
```

This installs the Claude GitHub App, which enables:

- `@claude` mentions in Issues and PRs
- Automatic PR review from Claude

---

## Step 5 — Verify setup

After completing the steps above, confirm:

- [ ] `CLAUDE.md` exists in the repo root with no unfilled `[PLACEHOLDER]` values
- [ ] `.ai/project-brief.md`, `.ai/agent-workflow.md`, `.ai/coding-rules.md`, and `.ai/task-template.md` exist and are filled in
- [ ] Claude Code can read and summarize the repo (run: `@claude summarize this repo`)
- [ ] Claude GitHub Actions responds to `@claude` in a test Issue or PR comment
- [ ] You can create a GitHub Issue, open a branch, and open a PR following `issue-to-pr-flow.md`

---

## You are ready when

- Claude Code understands the project from `CLAUDE.md` and `.ai/`
- GitHub Issues are being used to plan tasks
- Changes are going through feature branches and PRs
- Claude is reviewing PRs automatically
