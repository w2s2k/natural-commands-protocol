# NCP Implementation Guide

## Minimum Viable Implementation

To implement NCP, you need 4 components:

### 1. Schema Loader

```python
import json

class SchemaLoader:
    def __init__(self, schema_path):
        with open(schema_path) as f:
            self.schema = json.load(f)
        self.commands = self.schema['commands']
```

### 2. Variant Indexer

```python
class VariantIndex:
    def __init__(self, schema, lang='en'):
        self.index = {}
        
        for cmd in schema['commands']:
            if lang not in cmd['i18n']:
                continue
            
            for variant in cmd['i18n'][lang]['variants']:
                # Store longest matches first
                self.index[variant.lower()] = cmd
        
        # Sort by length (longest first)
        self.index = dict(sorted(
            self.index.items(),
            key=lambda x: len(x[0]),
            reverse=True
        ))
```

### 3. Parser

```python
class NCPParser:
    def parse(self, input_text):
        tokens = input_text.lower().split()
        matched_commands = []
        
        i = 0
        while i < len(tokens):
            # Try to match longest variant
            for variant, command in self.index.items():
                if self._starts_with(tokens, i, variant):
                    matched_commands.append(command)
                    i += len(variant.split())
                    break
            else:
                i += 1
        
        return self._build_ast(matched_commands)
```

### 4. Executor

```python
class Executor:
    def execute(self, ast, context):
        if ast['type'] == 'operation':
            operator = ast['operator']
            
            if operator == '+':
                return self._sum(ast['args'], context)
            elif operator == '-':
                return self._subtract(ast['args'], context)
            # ... etc
```

## Full Example

See `/proof-of-concept/simple_parser.py` for a complete minimal implementation in ~100 lines.

## Best Practices

### Performance

- Cache schema in memory
- Build variant index once at startup
- Use trie structures for large schemas
- Consider JIT compilation for frequently-used expressions

### Error Handling

- Never crash on unknown input
- Provide suggestions for close matches
- Show available commands when unclear
- Log parsing failures for improvement

### Testing

- Test all commands from schema
- Test all variants
- Test arity validation
- Test with multiple languages
- Test edge cases (empty input, very long input)
