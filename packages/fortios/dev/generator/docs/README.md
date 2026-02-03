# FortiOS API Code Generator

**Simplified, unified generator for FortiOS API client code.**

## Quick Start

```bash
# Generate everything
python generate.py --all --version 7.6.5

# Generate single category
python generate.py --category cmdb --version 7.6.5

# Generate single endpoint
python generate.py --endpoint cmdb.firewall.policy --version 7.6.5
```

## Architecture

```
.dev/generator/
├── generate.py          # Main entry point - orchestrates everything
├── generators/          # Individual generators
│   ├── endpoint_generator.py    # Generates endpoint classes
│   ├── validator_generator.py   # Generates validation helpers
│   ├── pyi_generator.py         # Generates type stubs
│   └── log_generator.py         # LOG category (special handling)
├── utils/               # Shared utilities
│   ├── naming.py        # ALL naming conversions
│   └── paths.py         # Path handling
├── templates/           # Jinja2 templates
└── docs/                # Documentation
```

## What Gets Generated

For each endpoint (e.g., `cmdb.firewall.address`):

1. **Endpoint class** (`firewall/address.py`)
   - GET, POST, PUT, DELETE methods
   - Docstrings with examples
   - Type hints

2. **Validator helper** (`firewall/_helpers/address.py`)
   - Field validation
   - Enum constants
   - Default values

3. **Type stub** (`firewall/address.pyi`)
   - TypedDict for payloads
   - Literal types for enums
   - Full type coverage

4. **Tests** (`.tests/pytests/api/cmdb/firewall/auto_test_address.py`)
   - Basic smoke tests
   - GET/POST/PUT/DELETE tests
   - Validator tests

5. **Init files** (`firewall/__init__.py`)
   - Auto-generated imports
   - Category wrapper classes

## Generator Flow

```python
# In generate.py
def generate_all():
    """Run all generators in correct order."""
    
    # 1. Download/load schemas
    schemas = load_schemas()
    
    # 2. Generate endpoints
    for schema in schemas:
        endpoint_gen.generate(schema)
    
    # 3. Generate validators
    for schema in schemas:
        validator_gen.generate(schema)
    
    # 4. Generate stubs
    for schema in schemas:
        stub_gen.generate(schema)
    
    # 5. Generate tests
    for schema in schemas:
        test_gen.generate(schema)
    
    # 6. Generate __init__.py files
    init_gen.generate_all_categories()
```

## Key Features

### ✅ Unified Naming
All naming conversions in `utils/naming.py`:
- `to_class_name()` - PascalCase
- `to_module_name()` - snake_case
- `to_constant_name()` - SCREAMING_SNAKE_CASE
- `kebab_to_snake()` - Handle API names
- `fix_api_path()` - Convert back to API format

### ✅ Smart Path Handling
`utils/paths.py` handles:
- Nested directories
- Naming conflicts
- Helper directories
- Cross-platform paths

### ✅ Category-Aware
Handles special cases:
- **CMDB**: Full CRUD
- **Monitor**: Read-only
- **Service**: Mixed
- **LOG**: Path parameters (nested classes)

### ✅ Template-Based
Clean separation:
- Logic in generators
- Structure in templates
- Easy to customize

## Troubleshooting

### Issue: Missing api_type in client.get()
**Fixed!** All generators now include the api_type parameter:
```python
self._client.get("log", path, **kwargs)  # ✅ Correct
```

### Issue: Tests fail on HTTP 424
**Fixed!** Tests now skip unavailable endpoints:
```python
if any(code in str(e) for code in ["400", "404", "405", "424", ...]):
    pytest.skip(f"Endpoint not available: {e}")
```

## Recent Improvements

- ✅ Consolidated two LOG generators into one
- ✅ Fixed client.get() signature across all generators
- ✅ Added HTTP 424 handling to tests
- ✅ Created unified naming utilities
- ✅ Simplified path handling

## Next Steps

See `REFACTOR_PROGRESS.md` for ongoing refactoring work.
