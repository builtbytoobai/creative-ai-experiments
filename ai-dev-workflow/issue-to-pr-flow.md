# Issue to Pull Request Flow

This is the standard GitHub workflow for making safe, reviewable changes.

---

## 1. Start from main

```bash
git checkout main
git pull
```

This makes sure your local `main` branch matches the latest version on GitHub.

---

## 2. Create a branch

Use a clear branch name:

```bash
git checkout -b feature/example-feature
```

Examples:

```txt
feature/model-comparison
docs/add-setup-guide
fix/input-validation
experiment/ai-dev-workflow
```

The branch is an isolated workspace for one focused change.

---

## 3. Ask Claude Code for a plan

Prompt:

```txt
Read CLAUDE.md and .ai/.

You are on a feature branch.

Task:
[describe the task]

Do not edit files yet.

First give me:
- summary of the task
- implementation plan
- files likely affected
- test commands
- suggested commit message
```

---

## 4. Review the plan

Before implementation, review the plan.

Use ChatGPT for:

- architecture review
- roadmap fit
- scope control
- edge cases
- maintainability

Use Gemini for:

- UX perspective
- product usefulness
- beginner friendliness
- second opinion

Do not implement until the task is clear.

---

## 5. Let Claude implement

Prompt:

```txt
Approved. Implement this as one focused change.

Do not commit yet.

After editing, summarize:
- files changed
- key implementation details
- test commands
```

---

## 6. Test locally

Run relevant commands.

Examples:

```bash
python main.py
python app.py
python ai_lyric_generator_v3.py --list-options
```

The exact test command depends on the repo.

---

## 7. Review changes locally

Check changed files:

```bash
git status
```

Review the diff:

```bash
git diff
```

Make sure there are no unrelated changes.

---

## 8. Commit

```bash
git add .
git commit -m "Clear commit message"
```

Good commit messages are short, specific, and action-based.

Examples:

```txt
Add model comparison mode
Improve input validation
Add external review workflow
Update README setup guide
```

---

## 9. Push branch

```bash
git push -u origin branch-name
```

Example:

```bash
git push -u origin feature/model-comparison
```

---

## 10. Open Pull Request

Create a PR on GitHub.

The PR should include:

- summary
- files changed
- test commands
- related issue
- known limitations, if any

---

## 11. Review and merge

Before merging, check:

- Files changed
- Claude automatic review
- local test results
- no secrets exposed
- no unrelated changes
- documentation updated if needed

Then merge the PR.

---

## 12. Clean up locally

After merging:

```bash
git checkout main
git pull
git branch -d branch-name
git fetch --prune
```

If branch deletion fails because of Windows or OneDrive locking files, check:

```bash
git branch
```

If the branch is gone from the list, cleanup is good enough.

---

## Core rule

One issue.

One branch.

One focused change.

One PR.