# Generator Backup - Pre-Protocol Refactoring

**Backup Date:** 2026-01-07 14:51:51  
**Reason:** Protocol-based overload refactoring implementation

## What Changed

This backup was created before implementing the Protocol-based type hint refactoring that eliminates duplicate `@overload` decorators from generated endpoint files.

### Before (this backup)
- Template generates ~263 lines of `@overload` decorators per endpoint
- Each endpoint file contains 6 overloads for GET, 4 for POST, 4 for PUT, 4 for DELETE
- Total duplication across 500+ endpoints: ~131,500 lines of boilerplate

### After (updated generator)
- Endpoint classes inherit from `CRUDEndpoint` protocol
- All overloads defined once in `packages/fortios/hfortix_fortios/_protocols.py`
- Generated files contain only implementation methods
- 90%+ reduction in generated code size

## Files Backed Up

- `generators/` - All generator Python modules including:
  - `endpoint_generator.py` - Main endpoint class generator
  - `model_generator.py` - Pydantic model generator
  - `validator_generator.py` - Validator generator
  - Other supporting generators
  
- `templates/` - All Jinja2 templates including:
  - `endpoint_class.py.j2` - Endpoint class template (contains overload generation)
  - `endpoint_class.pyi.j2` - Type stub template
  - `pydantic_model.py.j2` - Model template
  - Other templates

## How to Restore

If you need to revert to the old generator:

```bash
cd /app/dev/classes/fortinet/.dev/generator

# Restore templates
cp -r archive/pre-protocol-refactor-20260107_145151/templates/* templates/

# Restore generators
cp -r archive/pre-protocol-refactor-20260107_145151/generators/* generators/
```

## Testing After Restore

```bash
# Regenerate a test endpoint
python generate.py --version 7.6.5 --endpoint firewall.address

# Verify overloads are present
grep -A 5 "@overload" packages/fortios/hfortix_fortios/api/v2/cmdb/firewall/address.py
```

## Related Documentation

- `/app/dev/classes/fortinet/REFACTORING_OVERLOADS_GUIDE.md` - Implementation guide
- `/app/dev/classes/fortinet/REFACTORING_VISUAL_COMPARISON.md` - Before/after comparison
- `/app/dev/classes/fortinet/packages/fortios/hfortix_fortios/_protocols.py` - Protocol definitions

## Generator Version

This backup represents the generator state as of:
- Last significant update: Pydantic model integration (2026-01-06)
- Feature level: Full CRUD + validators + models + type hints with overloads
