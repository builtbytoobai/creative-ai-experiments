# Creative AI Experiments

Small experiments exploring AI, creativity, storytelling, and code.

Built by curiosity. Powered by AI.

---

## 📌 About

This repository is a sandbox for small creative AI experiments.

The goal is to test ideas quickly, document what I learn, and turn small concepts into working prototypes over time.

---

## 📁 Structure

```bash
creative-ai-experiments/
│
├── experiments/          # small creative AI scripts and prototypes
├── notes/                # experiment notes and findings
├── ai-dev-workflow/      # reusable AI-assisted development workflow blueprint
│   ├── templates/        # copy these into new repos to adopt the workflow
│   └── *.md              # workflow documentation and role guides
├── .ai/                  # live workflow context for this repo
├── CLAUDE.md             # Claude Code instructions for this repo
├── .gitignore
└── README.md
```

---

## 🔬 Current Experiments

### Mood Color Mapper

A small Python experiment that maps moods to colors, feelings, and creative directions.

### AI Review Script

`experiments/review.py` — runs ChatGPT and Gemini reviews in parallel against any repo file, eliminating the manual copy-paste step when doing external reviews. Requires `OPENAI_API_KEY` and `GEMINI_API_KEY` in a local `.env` file.

### AI Development Workflow

This repo includes an experiment called `ai-dev-workflow`.

It documents a reusable AI-assisted development workflow for future repos and app ideas.

The workflow uses:

- Claude Code as builder and implementation agent
- GitHub Issues for task planning
- Git branches and Pull Requests for safe changes
- Claude GitHub Actions for `@claude` issue/PR assistance and automatic PR review
- ChatGPT for architecture, product, and roadmap review
- Gemini for UX, usefulness, and second-opinion review

The goal is to make it faster to go from idea → repo → issue → implementation → review → merge.

See:

```txt
ai-dev-workflow/
```

---

## 🧪 Experiment Ideas

- AI-assisted writing tools
- Lyric and storytelling generators
- Prompt experiments
- Creative automation scripts
- Small Python prototypes
- Music and mood-based tools

---

## 🧠 Philosophy

Start small.

Make it work.

Document the process.

Improve later.
