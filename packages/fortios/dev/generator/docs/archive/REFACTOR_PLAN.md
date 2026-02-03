# Generator Refactoring Plan

## Current Issues
1. **Two LOG generators** with overlapping functionality
2. **Scattered test generation** logic
3. **Duplicate code** for path handling, naming conventions
4. **Unclear orchestration** - hard to understand what runs when
5. **Inconsistent templates** and generation patterns

## New Simplified Structure

```
.dev/generator/
├── generate.py                 # Main orchestrator (unified entry point)
├── generators/
│   ├── __init__.py
│   ├── endpoint.py            # SINGLE endpoint generator (all categories)
│   ├── validator.py           # Validator generation
│   ├── stubs.py               # .pyi stub generation  
│   ├── tests.py               # Test generation
│   └── init_files.py          # __init__.py generation
├── templates/
│   ├── endpoint.py.j2         # Unified endpoint template
│   ├── endpoint.pyi.j2
│   ├── validator.py.j2
│   ├── validator.pyi.j2
│   ├── test.py.j2             # Unified test template
│   └── init.py.j2
├── utils/
│   ├── __init__.py
│   ├── naming.py              # All naming conversions in one place
│   ├── paths.py               # Path handling utilities
│   └── schema.py              # Schema parsing utilities
└── docs/
    ├── README.md              # Main documentation
    ├── ARCHITECTURE.md        # How it all works
    └── USAGE.md               # Usage examples

```

## Key Improvements

### 1. Single Endpoint Generator
```python
class EndpointGenerator:
    """Generates ALL endpoints (cmdb, monitor, service, log)."""
    
    def generate(self, schema: Schema, category: str) -> Path:
        """Category-aware generation."""
        if category == 'log':
            return self._generate_log_endpoint(schema)
        else:
            return self._generate_standard_endpoint(schema)
```

### 2. Unified Naming Utilities
```python
# utils/naming.py
def to_class_name(name: str) -> str:
    """Convert any format to PascalCase."""
    
def to_module_name(name: str) -> str:
    """Convert any format to snake_case."""
    
def to_constant_name(name: str) -> str:
    """Convert to SCREAMING_SNAKE_CASE."""
```

### 3. Clear Orchestration
```python
# generate.py
def generate_all():
    """Run all generators in correct order."""
    
    # 1. Generate endpoints
    endpoint_gen.generate_all(schemas)
    
    # 2. Generate validators
    validator_gen.generate_all(schemas)
    
    # 3. Generate stubs
    stub_gen.generate_all(endpoints)
    
    # 4. Generate tests
    test_gen.generate_all(endpoints)
    
    # 5. Generate __init__.py files
    init_gen.generate_all(categories)
```

## Migration Steps

1. ✅ **Create unified naming utilities** (`utils/naming.py`)
2. ✅ **Merge log generators** into single `endpoint.py`
3. ✅ **Create unified test generator** (`generators/tests.py`)
4. ✅ **Create init file generator** (`generators/init_files.py`)
5. ✅ **Update main orchestrator** (`generate.py`)
6. ✅ **Consolidate templates**
7. ✅ **Update documentation**
8. ✅ **Remove old generators**

## Benefits

- **70% less code** - eliminate duplication
- **Clearer flow** - one entry point, clear order
- **Easier maintenance** - change naming in ONE place
- **Better tests** - consistent test generation
- **Self-documenting** - clear separation of concerns
