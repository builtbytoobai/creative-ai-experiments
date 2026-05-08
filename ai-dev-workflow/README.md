# AI Development Workflow Experiment

This experiment documents a reusable AI-assisted development workflow for building software projects faster and more safely.

The goal is to create a repeatable setup where multiple AI tools support different parts of the development process.

---

## Purpose

This workflow helps turn a project idea into a working repo using:

- Claude Code for implementation
- GitHub Issues for task planning
- Git branches and Pull Requests for safe changes
- Claude GitHub Actions for automated assistance and PR review
- ChatGPT for architecture, product, and roadmap review
- Gemini for second-opinion review on UX, usefulness, and product direction

---

## Core idea

Claude builds.

ChatGPT reviews architecture and product direction.

Gemini gives a second opinion on UX and usefulness.

The user makes the final decision.

---

## Workflow stages

1. Capture the project idea
2. Turn the idea into a GitHub Issue
3. Ask Claude Code for an implementation plan
4. Ask ChatGPT to review the plan
5. Ask Gemini for a second opinion when relevant
6. Let Claude Code implement one focused change
7. Open a Pull Request
8. Let Claude GitHub Actions review the PR
9. Merge only after human approval

---

## Files in this experiment

- `roles.md` — defines the role of each AI tool
- `workflow.md` — explains the full development workflow
- `issue-to-pr-flow.md` — documents the GitHub Issue → Branch → PR process
- `external-reviewers.md` — explains how ChatGPT and Gemini are used
- `setup-checklist.md` — reusable setup checklist for new repos

---

## Current status

Experimental workflow documentation.

Tested first on the `AI-Lyric-Generator` repository.