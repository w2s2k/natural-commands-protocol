import json
import sys

def validate_schema(path):
    try:
        with open(path, 'r') as f:
            data = json.load(f)
        
        if 'commands' not in data:
            print("❌ Missing 'commands' array")
            return False
        
        ids = set()
        for cmd in data['commands']:
            # Check required fields
            required = ['id', 'category', 'type', 'compute', 'i18n']
            for field in required:
                if field not in cmd:
                    print(f"❌ Command {cmd.get('id', 'unknown')} missing field: {field}")
                    return False
            
            # Check unique IDs
            if cmd['id'] in ids:
                print(f"❌ Duplicate command ID: {cmd['id']}')
                return False
            ids.add(cmd['id'])
            
            # Check i18n
            if 'en' not in cmd['i18n'] or 'pt' not in cmd['i18n']:
                print(f"❌ Command {cmd['id']} missing required languages (en, pt)")
                return False
        
        print(f"✅ Schema validated: {len(ids)} commands found")
        return True
    except Exception as e:
        print(f"❌ Validation error: {str(e)}")
        return False

if __name__ == "__main__":
    if validate_schema('spec/commands.json'):
        sys.exit(0)
    else:
        sys.exit(1)
