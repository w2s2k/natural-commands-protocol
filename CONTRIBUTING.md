# Contributing to Natural Commands Protocol
Thank you for your interest in improving NCP!

## How to Contribute

### 1. Adding New Commands

Before proposing a new command:

1. **Check if it already exists** - Search the schema
2. **Identify the category** - Which category does it fit?
3. **Define clear semantics** - What does it compute exactly?

Then open an issue with:

```markdown
## Proposed Command

**ID**: `op_exponent`
**Category**: `arithmetic`
**Type**: `operator`

**Purpose**: Calculate exponential power

**Compute**:
- Function: `EXPONENT`
- Operator: `**`
- Formula: `Math.pow({base}, {exponent})`
- Arity: `2`

**i18n (English)**:
- Canonical: `to the power of`
- Variants: `to the power of`, `raised to`, `power`, `exp`
- Slash: `/power`
- Template: `{base} to the power of {exponent}`

**i18n (Portuguese)**:
- Canonical: `elevado a`
- Variants: `elevado a`, `à potência de`, `potência`
- Slash: `/potencia`
- Template: `{base} elevado a {expoente}`

**Use Cases**:
- Scientific calculations
- Financial compound interest
- Growth rate modeling
```

### 2. Adding New Languages

To add language support:

1. Fork the repository
2. Add your language code to ALL commands
3. Provide comprehensive variants (10+ per command)
4. Include native speaker review
5. Submit PR with examples

Template:
```json
"i18n": {
  "en": { /* existing */ },
  "pt": { /* existing */ },
  "es": {
    "canonical": "sumar",
    "variants": ["sumar", "más", "agregar", "adicionar"],
    "slash": "/sumar",
    "template": "{a} más {b}"
  }
}
```

### 3. Improving Documentation

- Fix typos or unclear explanations
- Add more examples
- Translate documentation
- Improve diagrams

### 4. Reporting Issues
- Use for bugs in schema
- NOT for implementation bugs (that's up to implementers)
- Include which command is affected
- Suggest fix if possible

## Pull Request Process

1. Fork the repo
2. Create feature branch (`git checkout -b feature/new-command`)
3. Make changes
4. Validate JSON (`python -m json.tool spec/commands.json`)
5. Update CHANGELOG.md
6. Submit PR

### PR Checklist

- [ ] JSON is valid
- [ ] All commands have unique IDs
- [ ] i18n provided for en + pt (minimum)
- [ ] Examples included
- [ ] CHANGELOG.md updated
- [ ] No breaking changes (or clearly marked)

## Code of Conduct

Be respectful, inclusive, and professional.

Full CoC: [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)
