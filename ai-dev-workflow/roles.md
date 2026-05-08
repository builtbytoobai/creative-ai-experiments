# AI Tool Roles

This workflow uses different AI tools for different jobs.

## Claude Code

Claude Code is the primary development agent.

Use Claude Code for:

- reading the repo
- understanding existing code
- proposing implementation plans
- editing files
- creating focused changes
- helping with GitHub Issues
- helping with Pull Requests
- suggesting commit messages

Claude Code should work in small, reviewable changes.

Claude should not make large unrelated changes.

## Claude GitHub Actions

Claude GitHub Actions provides GitHub-based automation.

Use it for:

- responding to `@claude` in Issues and PRs
- reviewing Pull Requests automatically
- helping with issue planning
- giving repo-aware feedback inside GitHub

## ChatGPT

ChatGPT is the external architecture, product, and roadmap reviewer.

Use ChatGPT for:

- reviewing Claude's implementation plans
- checking architecture decisions
- identifying risks and edge cases
- deciding whether a feature is worth building now
- reviewing roadmap priorities
- avoiding over-engineering

ChatGPT should challenge the plan before implementation.

## Gemini

Gemini is the external second-opinion reviewer.

Use Gemini for:

- UX perspective
- product usefulness
- user clarity
- onboarding quality
- alternative product directions
- prompt-system review
- whether the idea feels useful to real users

Gemini should help judge whether the project makes sense from a user perspective.

## User

The user is the final decision-maker.

The user decides:

- what gets built
- what gets rejected
- what gets merged
- when a repo should be continued, archived, or deleted