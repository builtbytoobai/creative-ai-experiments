# Coding Rules

## General rules

- Keep changes small and reviewable.
- Prefer clear code over clever code.
- Avoid unrelated refactors.
- Do not introduce unnecessary dependencies.
- Do not hardcode secrets.
- Keep generated files out of Git unless explicitly needed.

## Documentation rules

Update README when:

- setup changes
- user-facing behavior changes
- commands change
- new features are added

Update roadmap or notes when:

- project direction changes
- a major feature is completed
- future plans change

## Git rules

Use clear commit messages.

Good examples:

```txt
Add setup checklist
Improve input validation
Update README usage examples
Add external review workflow
```

Avoid vague messages:

```txt
update
fix
stuff
changes
```

## Security rules

Never commit:

```txt
.env
API keys
tokens
passwords
private credentials
local cache folders
```

Use `.env.example` for placeholders only.