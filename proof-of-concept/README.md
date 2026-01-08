# NCP Proof of Concept

This directory contains minimal implementations that prove the Natural Commands Protocol (NCP) works as specified.

## Files

### 1. `simple_parser.py`
A minimal Python parser (<100 lines) that reads the `spec/commands.json` file and executes basic arithmetic operations.

**How to run:**
```bash
python3 proof-of-concept/simple_parser.py
```

### 2. `llm_grounding_test.py`
A simulation proving how NCP grounding reduces LLM hallucination and ensures 100% format consistency.

**How to run:**
```bash
python3 proof-of-concept/llm_grounding_test.py
```

## Purpose
These are not production-ready libraries. They are reference implementations designed to demonstrate the core principles of the protocol:
- Determinism
- Schema-based execution
- Format consistency
