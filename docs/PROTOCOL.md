# Natural Commands Protocol - Technical Specification

## Overview

Natural Commands Protocol (NCP) is a **declarative protocol specification** for mapping natural language to computational operations in a deterministic, i18n-native way.

## Core Principles

### 1. Protocol-First Design

NCP is NOT:
- ❌ A software library
- ❌ A specific implementation
- ❌ Tied to any programming language

NCP IS:
- ✅ A JSON specification
- ✅ A standard anyone can implement
- ✅ Language and platform agnostic

### 2. Determinism

**Same input MUST always produce same output.**

This is non-negotiable. NCP is designed for critical calculations where variability is dangerous (finance, legal, medical).

### 3. Zero Syntax for End Users

Users should never see:
- Parentheses `()`
- Brackets `[]`
- Operators as symbols `+`, `-`, `*`
- Function names `IF()`, `SUM()`

Only natural language: `if value greater than 100 then apply discount`

### 4. i18n Native

Multi-language support is not an afterthought—it's built into the protocol structure.

Every command MUST have:
- Canonical form per language
- Multiple natural variants
- Slash command for power users
- Usage template with examples

## Protocol Structure

### Root Schema

```json
{
  "version": "1.0.0",
  "schema": "natural-commands-i18n",
  "commands": [ /* array of command objects */ ],
  "metadata": {
    "categories": [ /* ... */ ],
    "types": [ /* ... */ ],
    "supported_languages": ["en", "pt"],
    "extensible": true
  }
}
```

### Command Structure

Every command in the protocol follows this structure:

```json
{
  "id": "unique_identifier",
  "category": "functional_category",
  "type": "computational_type",
  "compute": {
    "function": "CANONICAL_NAME",
    "operator": "symbol",
    "formula": "Formula({args})",
    "arity": 2,
    "requires": "dependency_id"
  },
  "i18n": {
    "en": {
      "canonical": "add",
      "variants": ["add", "plus", "sum"],
      "slash": "/add",
      "template": "{a} plus {b}"
    }
  }
}
```

## Categories
The protocol organizes commands into functional categories:

| Category | Purpose | Example Commands |
|----------|---------|------------------|
| `arithmetic` | Math operations | add, subtract, multiply |
| `conditional` | Control flow | if, when, while |
| `comparison` | Relational ops | greater than, equal to |
| `date` | Temporal ops | today, days between |
| `function` | Math functions | max, min, average |
| `logical` | Boolean ops | and, or, not |
| `text` | String ops | concat, contains |
| `list` | Array ops | filter, map, sort |

## Types

Types define HOW a command behaves computationally:

- `operator` - Binary/unary operations
- `control_flow` - Flow control (if, else)
- `relational` - Comparisons
- `aggregate` - Operations on lists
- `math` - Mathematical functions
- `literal` - Static values

## Compute Specification

The `compute` object tells implementers how to execute:

### `function` (required)
Canonical name in UPPERCASE (e.g., `ADD`, `MULTIPLY`, `IF`)

### `operator` (optional)
Symbol representation when applicable (e.g., `+`, `-`, `>`)

### `formula` (optional)
Template showing execution with placeholders:
```json
"formula": "IF({condition}, {then}, {else})"
```

### `arity` (required)
Number of arguments:
- `0` - No arguments (e.g., `TODAY()`)
- `1` - Unary
- `2` - Binary
- `-1` - Variadic (any number)

### `requires` (optional)
ID of command that must precede this one (e.g., `else` requires `if`)

## i18n Specification

### `canonical`
The "official" form in that language. Used internally.

### `variants`
ALL ways users might express this command:
- Synonyms
- Colloquialisms
- Abbreviations
- Common misspellings (if appropriate)

**Rule:** More variants = better UX

### `slash`
Quick-access command for power users:
```json
"slash": "/add"
```

### `template`
Shows users how to use the command:
```json
"template": "{a} plus {b}"
```

## Versioning

NCP follows semantic versioning:

- **Major (1.x.x)**: Breaking changes to protocol structure
- **Minor (x.1.x)**: New commands added (backwards compatible)
- **Patch (x.x.1)**: Bug fixes, variant additions

### Stability Guarantees
- Command IDs NEVER change
- `compute.function` names are stable
- New variants can be added without version bump
- Category names are stable

## Implementation Requirements

Any NCP implementation MUST:

1. ✅ Read and parse `schema.json`
2. ✅ Index all variants by language
3. ✅ Match longest variant first (greedy matching)
4. ✅ Respect `arity` for validation
5. ✅ Execute using `compute` specification
6. ✅ Return deterministic results

Any NCP implementation SHOULD:

- Support at least English (`en`)
- Handle unknown commands gracefully
- Provide helpful error messages
- Cache schema for performance

## Extension Guidelines

### Adding Commands

New commands MUST:
- Have unique `id`
- Belong to existing category (or propose new one)
- Define `compute` spec completely
- Provide i18n for at least `en` and one other language
- Include usage examples
- Not duplicate existing functionality

### Adding Languages

New language support MUST:
- Cover ALL existing commands
- Provide comprehensive variants
- Include native speaker review
- Follow language's natural expression patterns

## Governance

- **Maintainers**: Community elected
- **RFC Process**: For major changes
- **Voting**: 1 vote per active contributor
- **Consensus**: 75% approval for breaking changes
