---

## Reusable templates

This experiment includes starter templates in:

```txt
ai-dev-workflow/templates/
```

Recommended use for a new repo:

1. Copy `templates/CLAUDE.md` into the repo root as `CLAUDE.md`.
2. Create a `.ai/` folder.
3. Copy these files into `.ai/`:
   - `project-brief.md`
   - `agent-workflow.md`
   - `coding-rules.md`
   - `task-template.md`
4. Optionally copy:
   - `issue-template.md`
   - `pr-template.md`
5. Replace all placeholder values like:
   - `[PROJECT_NAME]`
   - `[TECH_STACK]`
   - `[TEST_COMMAND_1]`
6. Install Claude GitHub Actions with:

```bash
claude
```

Then inside Claude Code:

```txt
/install-github-app
```