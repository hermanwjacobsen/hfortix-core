# Generator Bug Fix: Array Type Handling

## Issue Summary

The type stub generator (`.pyi` files) was incorrectly converting `"type": "array"` from JSON schemas to `str` instead of `list[Any]`. This caused type checking errors when using array fields.

**Example:**
```python
# Schema definition:
{
    "id_list": {
        "type": "array",
        "python_type": "List"
    }
}

# Generated (WRONG):
id_list: str | None = ...

# Generated (FIXED):
id_list: list[Any] | None = ...
```

## Root Causes

### 1. Missing Type Mapping in `_to_python_type()`

**File:** `.dev/generator/generators/pyi_generator.py`

The `_to_python_type()` function didn't have a mapping for `'array'` type, causing it to fall back to the default `'str'`.

**Fix:** Added array type mapping
```python
def _to_python_type(fortios_type: str) -> str:
    """Convert FortiOS type to Python type."""
    type_map = {
        'integer': 'int',
        'string': 'str',
        'option': 'str',
        # ... other types ...
        'array': 'list[Any]',  # ✅ ADDED
        'boolean': 'bool',
    }
    return type_map.get(fortios_type, 'str')
```

### 2. Missing Array Handling in Template

**File:** `.dev/generator/templates/endpoint_class.pyi.j2`

The Jinja2 template had conditionals to handle:
- `field.category == 'table'` (nested structures)
- `field.category == 'complex'` (nested objects)
- `field.type in ['integer', 'int']`
- `field.type == 'boolean'`
- `field.options` (enums)

But **no check for `field.type == 'array'`** for simple arrays without nested structure.

**Fix:** Added array type checks in **6 locations**:

1. **Payload TypedDict** (line ~193)
2. **Response TypedDict** (line ~226)
3. **Object Class** (line ~394)
4. **POST Method Signature** (line ~648)
5. **PUT Method Signature** (line ~704)
6. **SET Method Signature** (line ~788)

```jinja
{% elif field.type in ['integer', 'int'] %}
    {{ field_snake }}: int{% if field.is_list %} | list[int]{% endif %} | None = ...,
{% elif field.type == 'boolean' %}
    {{ field_snake }}: bool | None = ...,
{% elif field.type == 'array' %}
{# Simple array fields without nested structure #}
    {{ field_snake }}: list[Any] | None = ...,
{% else %}
    {{ field_snake }}: str{% if field.is_list %} | list[str]{% endif %} | None = ...,
{% endif %}
```

## Files Modified

1. `.dev/generator/generators/pyi_generator.py`
   - Added `'array': 'list[Any]'` to type mapping

2. `.dev/generator/templates/endpoint_class.pyi.j2`
   - Added `{% elif field.type == 'array' %}` check in 6 locations
   - Also added missing `{% elif field.type == 'boolean' %}` in SET method

## Testing

After regenerating the `.pyi` files, the `id_list` field in `monitor/system/config_script/delete.pyi` should show:

```python
class SystemConfigScriptDeletePayload(TypedDict, total=False):
    """Payload type for SystemConfigScriptDelete operations."""
    id_list: list[Any]  # ✅ Correct (was: str ❌)

def get(
    self,
    *,
    id_list: list[Any] | None = ...,  # ✅ Correct
    ...
) -> SystemConfigScriptDeleteObject: ...
```

## Related Issues

This is the same category of bug as the `NO_HYPHEN_PARAMETERS` issue where the library has special cases that need explicit handling:
- `file_content` → must stay as underscore (not `file-content`)
- `key_file_content` → must stay as underscore
- `id_list` → must stay as underscore (not `id-list`)

## Impact

This fix ensures that:
1. Type checkers (Pylance, mypy) correctly validate array parameters
2. IDE autocomplete shows the correct type
3. Users get proper type hints when using array fields
4. The generated stubs match the actual runtime behavior

## Next Steps

1. ✅ Update generator code
2. ✅ Update template  
3. ⏳ Regenerate all `.pyi` files
4. ⏳ Test with affected endpoints
5. ⏳ Update version and changelog
