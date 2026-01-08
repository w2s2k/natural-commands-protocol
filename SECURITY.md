# Security Policy

## Supported Versions

| Version | Supported |
|---------|-----------|
| 1.x.x   | ✅ Yes    |
| < 1.0   | ❌ No     |

## What is a "Security Issue" in NCP?

Since NCP is a protocol specification licensed under CC-BY-4.0 (not executable code), security issues are:

### In Scope

✅ **Ambiguous command definitions** that could lead to misinterpretation
✅ **Injection vulnerabilities** in formula templates
✅ **Arity mismatches** that could cause unexpected behavior
✅ **Variant collisions** where two commands share variants

### Out of Scope

❌ Implementation bugs (report to implementation maintainers)
❌ LLM hallucinations (NCP reduces but doesn't eliminate)
❌ User input validation (implementer's responsibility)

## Reporting a Vulnerability

**DO NOT** open a public issue for security concerns.

Instead, email: **security@ncp-protocol.org** (or create private security advisory on GitHub)

Include:

1. Affected command ID(s)
2. Description of the vulnerability
3. Potential impact
4. Suggested fix (if any)

## Response Timeline

The NCP security team will respond to all reports within 48 hours and provide a resolution timeline within 7 days.

