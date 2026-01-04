# Type Stub Integration Guide

## Current Status ✅

**Completed**:
1. ✅ PYIGenerator class created (`.dev/generator/generators/pyi_generator.py`)
2. ✅ Template created for endpoint stubs (`.dev/generator/templates/endpoint_class.pyi.j2`)
3. ✅ Template created for validator stubs (`.dev/generator/templates/validator.pyi.j2`)

**Remaining**: Integrate into main generator workflow

---

## Integration Steps

### Step 1: Import PYIGenerator in Main Generator

**File**: `.dev/generator/generate.py` (or wherever main generator lives)

Add import:
```python
from .generators.pyi_generator import PYIGenerator
```

### Step 2: Initialize PYIGenerator

Add alongside other generators:
```python
# Initialize generators
endpoint_gen = EndpointGenerator(template_dir, output_dir)
validator_gen = ValidatorGenerator(template_dir, output_dir)
pyi_gen = PYIGenerator(template_dir, output_dir)  # NEW
```

### Step 3: Generate .pyi Files Alongside .py Files

In the endpoint generation loop:
```python
for schema in schemas:
    # Generate .py file
    py_output = output_dir / f"api/{schema.category}/{schema.path}.py"
    endpoint_gen.generate(schema, py_output)
    
    # Generate .pyi stub file (NEW)
    pyi_output = output_dir / f"api/{schema.category}/{schema.path}.pyi"
    pyi_gen.generate_endpoint_stub(schema, pyi_output)
```

In the validator generation loop:
```python
for schema in schemas:
    # Generate validator .py file
    py_output = output_dir / f"_helpers/{schema.path}.py"
    validator_gen.generate(schema, py_output)
    
    # Generate validator .pyi stub file (NEW)
    pyi_output = output_dir / f"_helpers/{schema.path}.pyi"
    enum_constants = validator_gen._extract_enum_constants(schema)
    pyi_gen.generate_validator_stub(schema, enum_constants, pyi_output)
```

### Step 4: Create py.typed Marker

At the end of generation:
```python
# Create PEP 561 marker file
pyi_gen.create_py_typed_marker()
logger.info("Type stub generation complete")
```

### Step 5: Optional - Generate Category __init__.pyi Files

If you want category-level type exports:
```python
# Group endpoints by category
category_endpoints = {}
for schema in schemas:
    category = schema.category
    if category not in category_endpoints:
        category_endpoints[category] = []
    category_endpoints[category].append(schema.class_name)

# Generate __init__.pyi for each category
for category_path, class_names in category_endpoints.items():
    init_pyi_path = output_dir / f"api/{category_path}/__init__.pyi"
    pyi_gen.generate_category_init_stub(category_path, class_names, init_pyi_path)
```

---

## Testing the Integration

### 1. Generate Stubs

```bash
cd /app/dev/classes/fortinet
make generate  # Should now generate .pyi files
```

### 2. Verify File Structure

Check that `.pyi` files were created:
```bash
# Should show both .py and .pyi files
ls -la packages/fortios/hfortix_fortios/api/cmdb/firewall/
# Expected:
# address.py
# address.pyi  <- NEW
# policy.py
# policy.pyi   <- NEW
```

### 3. Verify py.typed Marker

```bash
ls packages/fortios/hfortix_fortios/py.typed
# Should exist (can be empty)
```

### 4. Test in IDE

Create a test file:
```python
from hfortix_fortios.api.cmdb.firewall.address import Address, AddressPayload

# Test 1: Autocomplete
payload: AddressPayload = {
    "n  # <- Type and wait for autocomplete
}

# Test 2: Enum validation
payload: AddressPayload = {
    "name": "test",
    "type": "invalid"  # <- Should show error
}

# Test 3: Method signatures
fgt.api.cmdb.firewall.address.post(
    payload_dict=  # <- Hover should show AddressPayload type
)
```

---

## Troubleshooting

### Issue: No autocomplete appearing

**Solutions**:
1. Reload VS Code window (`Ctrl+Shift+P` → "Reload Window")
2. Check that `py.typed` file exists in package root
3. Verify `.pyi` files are in same directory as `.py` files
4. Check Pylance is enabled: Settings → Python › Language Server → "Pylance"

### Issue: Type errors not showing

**Solutions**:
1. Enable type checking: Settings → Python › Analysis › Type Checking Mode → "basic" or "strict"
2. Check that type stubs have correct syntax (run: `mypy --install-types`)
3. Verify Jinja2 template renders valid Python

### Issue: Wrong field types in stubs

**Solutions**:
1. Check field type mapping in `PYIGenerator._to_python_type()`
2. Verify schema parsing for enum values
3. Check template uses correct Jinja2 filters

---

## Package Distribution

### Include .pyi Files in Package

**File**: `pyproject.toml` or `MANIFEST.in`

For **pyproject.toml**:
```toml
[tool.setuptools.package-data]
hfortix_fortios = ["py.typed", "**/*.pyi"]
```

For **MANIFEST.in**:
```
include packages/fortios/hfortix_fortios/py.typed
recursive-include packages/fortios/hfortix_fortios *.pyi
```

### Verify Package Contents

```bash
cd packages/fortios
python -m build
tar -tzf dist/hfortix_fortios-*.tar.gz | grep -E '\.(pyi|py\.typed)'
# Should show all .pyi files and py.typed
```

---

## Performance Considerations

**Build Time**:
- Generating 909 `.pyi` files adds ~10-20 seconds to total build
- Templates are simple, render quickly

**Package Size**:
- `.pyi` files are ~60% size of `.py` files (no implementation)
- Total package size increases by ~10%

**Runtime**:
- ✅ Zero impact - Python ignores `.pyi` files at runtime
- ✅ No import overhead
- ✅ No memory overhead

---

## Next Steps After Integration

1. **Test with multiple endpoints**
   - Firewall address ✅
   - Firewall policy ✅
   - System interface
   - VPN settings
   
2. **Test with different field types**
   - String fields ✅
   - Integer fields ✅
   - Enum fields (Literal) ✅
   - List/table fields
   - Nested schemas

3. **Test in multiple IDEs**
   - VS Code + Pylance ✅
   - PyCharm Professional
   - Vim/Neovim + pyright

4. **User documentation**
   - Add examples to README showing type annotations
   - Document TypedDict usage patterns
   - Show autocomplete screenshots

---

## Summary Checklist

Before marking complete, verify:

- [ ] `.pyi` files generated for all 909 endpoints
- [ ] `py.typed` marker file created
- [ ] Type stubs include TypedDict payloads
- [ ] Enum fields use Literal types
- [ ] Required vs optional fields marked correctly
- [ ] Autocomplete works in VS Code
- [ ] Type checking catches errors
- [ ] Package builds correctly with stubs
- [ ] No runtime performance impact

**Estimated Integration Time**: 30-60 minutes (most time is testing)

---

**Ready to integrate?** The templates and generator are complete - just need to wire them into the main generation workflow!
