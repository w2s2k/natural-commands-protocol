# NCP Architecture Decisions

## Why JSON?
JSON was chosen as the protocol format because it is:
- Language-agnostic
- Human-readable
- Easy to parse in any environment
- Widely supported by LLMs for grounding

## Why Arity?
Explicit arity in the `compute` specification allows for:
- Immediate validation of expressions
- Deterministic AST construction
- Clear error messaging when arguments are missing

## i18n Design Rationale
Multi-language support is a first-class citizen in NCP. By embedding i18n directly into the command objects, we ensure that:
- Every command is available in every supported language
- Language-specific nuances (variants) are preserved
- The protocol remains consistent across different locales

## Determinism by Design
NCP achieves determinism by:
- Mapping natural language to a fixed set of computational functions
- Using a greedy matching algorithm for variants
- Providing a clear execution specification in the `compute` object

## Future Extensions
The protocol is designed to be extensible. Future versions may include:
- Support for more complex data types
- Advanced control flow structures
- Integration with more external tools and APIs
