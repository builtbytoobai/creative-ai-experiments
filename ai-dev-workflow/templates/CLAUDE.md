> **Template** — Copy this file into your new repo root as `CLAUDE.md`. Fill in all `[PLACEHOLDER]` values before starting work with Claude Code. Delete this note when done.

---

# Claude Instructions

This repository uses Claude Code as a development agent.

## Project context

Project name: [PROJECT_NAME]

Purpose:
[SHORT_PROJECT_PURPOSE]

Tech stack:
[TECH_STACK]

Active entry point:
[MAIN_FILE_OR_COMMAND]

Files or folders Claude should avoid unless explicitly asked:
[FILES_TO_AVOID]

---

## Working rules

- Propose a short plan before editing files.
- Work in small, focused changes.
- Change only files related to the task.
- Do not expose secrets, API keys, tokens, or credentials.
- Do not commit `.env`, generated outputs, cache folders, or local config.
- Update README when user-facing behavior changes.
- Update roadmap or notes when project direction changes.
- Prefer readable code over clever code.
- Avoid over-engineering.

---

## Git workflow

Use this workflow:

1. Work on a feature branch.
2. Make one focused change.
3. Run relevant checks or manual tests.
4. Summarize what changed.
5. Suggest a clear commit message.
6. Wait for user approval before committing unless explicitly told otherwise.

---

## Verification

Recommended verification commands:

```bash
[TEST_COMMAND_1]
[TEST_COMMAND_2]
```

If no automated tests exist, explain what was manually checked.

---

## Review checklist

Before finalizing a task, check:

- Does the change solve the requested task?
- Are unrelated files untouched?
- Are secrets protected?
- Is documentation updated if needed?
- Is the code readable and maintainable?
- Are the recommended verification commands still working?