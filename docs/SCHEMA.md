# NCP Schema Reference

This document provides a complete reference for the attributes used in the NCP `schema.json`.

## Root Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `version` | string | The version of the NCP protocol. |
| `schema` | string | The name of the schema type. |
| `commands` | array | An array of command objects. |
| `metadata` | object | Metadata about the protocol. |

## Command Object Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `id` | string | Unique identifier for the command. |
| `category` | string | Functional grouping (e.g., arithmetic, conditional). |
| `type` | string | Computational type (e.g., operator, control_flow). |
| `compute` | object | Execution specification. |
| `i18n` | object | Multi-language variants and templates. |

## Compute Object Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `function` | string | Canonical name of the function in UPPERCASE. |
| `operator` | string | Symbol representation (optional). |
| `formula` | string | Template showing execution with placeholders (optional). |
| `arity` | integer | Number of arguments required. |
| `requires` | string | ID of a command that must precede this one (optional). |

## i18n Object Attributes

Each language code (e.g., `en`, `pt`) contains:

| Attribute | Type | Description |
|-----------|------|-------------|
| `canonical` | string | The official form in that language. |
| `variants` | array | All ways users might express this command. |
| `slash` | string | Quick-access command for power users. |
| `template` | string | Usage template for the command. |
