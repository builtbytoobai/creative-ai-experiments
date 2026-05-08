# AI-Assisted Development Workflow

This document describes the full workflow for building a project with AI support.

---

## Main workflow

1. Start with a project idea
2. Create or update a GitHub repo
3. Add repo instructions:
   - `CLAUDE.md`
   - `.ai/`
4. Create a GitHub Issue for one focused task
5. Ask Claude Code to propose a plan
6. Ask ChatGPT to review the plan
7. Ask Gemini for a second opinion if product/UX clarity matters
8. Create a feature branch
9. Let Claude Code implement one focused change
10. Test locally
11. Commit the change
12. Push the branch
13. Open a Pull Request
14. Let Claude GitHub Actions review the PR
15. Review the PR manually
16. Merge into `main`
17. Delete the branch
18. Pull latest `main` locally

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
→ Claude plan
→ ChatGPT review
→ Gemini second opinion
→ Claude implementation
→ PR
→ Claude automatic review
→ human approval
→ merge
```

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

## When not to overuse it

Do not create a full PR flow for tiny local notes, throwaway experiments, or quick private drafts unless the change affects the repo direction.