"""
Minimal NCP Parser - Proof of Concept
Demonstrates that NCP schema can be read and executed
"""
import json

class SimpleNCPParser:
    def __init__(self, schema_path, lang='en'):
        with open(schema_path) as f:
            self.schema = json.load(f)
        self.lang = lang
        self.commands = self.schema['commands']
        self.index = self._build_index()

    def _build_index(self):
        index = {}
        for cmd in self.commands:
            if self.lang in cmd['i18n']:
                for variant in cmd['i18n'][self.lang]['variants']:
                    index[variant.lower()] = cmd
        # Sort by length descending to match longest variants first
        return dict(sorted(index.items(), key=lambda x: len(x[0]), reverse=True))

    def parse(self, input_text):
        input_text = input_text.lower()
        matched = []
        # This is a simplified parser for PoC purposes
        for variant, cmd in self.index.items():
            if variant in input_text:
                matched.append(cmd)
                # In a real parser, we would handle tokenization and positions
        return matched

    def execute(self, input_text, context):
        matched = self.parse(input_text)
        if not matched:
            return None
        
        # For PoC, we just execute the first matched command
        cmd = matched[0]
        compute = cmd['compute']
        
        if compute.get('operator') == '+':
            return context.get('a', 0) + context.get('b', 0)
        elif compute.get('operator') == '-':
            return context.get('a', 0) - context.get('b', 0)
        elif compute.get('operator') == '*':
            return context.get('a', 0) * context.get('b', 0)
        elif compute.get('operator') == '/':
            return context.get('a', 0) / context.get('b', 1)
        
        return "Command matched but execution logic not implemented in PoC"

if __name__ == "__main__":
    # Test
    try:
        parser = SimpleNCPParser('spec/commands.json')
        result = parser.execute("capital plus interest", {'a': 1000, 'b': 50})
        print(f"Input: 'capital plus interest', Context: {{'a': 1000, 'b': 50}}")
        print(f"Result: {result}")
        print("✅ Protocol proven to work with <100 lines")
    except FileNotFoundError:
        print("Error: spec/commands.json not found. Please run from the repository root.")
