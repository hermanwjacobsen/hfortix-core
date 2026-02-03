# Schema-Only Generator Migration

**Date**: 2025-01-XX  
**Status**: ✅ Complete  
**Version**: v1.7.0 Schema-Only Mode

## Overview

The code generator has been refactored to use **ONLY** pre-existing schemas from the `/schema/7.6.5/` directory. The old schema download functionality has been completely removed to prevent accidental regeneration with outdated schemas.

## What Changed

### Removed Features
- ❌ `--host` argument (FortiGate hostname)
- ❌ `--token` argument (FortiGate API token)
- ❌ `--force` argument (force schema re-download)
- ❌ `SchemaDownloader` class integration
- ❌ All schema download/fetch logic

### New Behavior
- ✅ Generator uses **ONLY** schemas from `/schema/{version}/` directory
- ✅ Default version changed from `7.6` to `7.6.5` (matches schema directory)
- ✅ Enhanced error handling if schema files are missing
- ✅ Cleaner command-line interface focused on code generation

## Why This Change?

### Schema Quality Comparison

**OLD Schemas** (downloaded from API):
- 954 endpoints
- 13 metadata fields per field
- No type safety (generic "string" types)
- No validation patterns
- No examples or relationships
- Version not tracked

**NEW v1.7.0 Schemas** (`/schema/7.6.5/`):
- **1,348 endpoints** (+41% coverage, +394 new endpoints)
- **38 metadata fields** per field
- **Type safety**: `python_type`, `pydantic_type` with proper typing
- **Validation**: `min_length`, `max_length`, `pattern`, `enum` constraints
- **Documentation**: `examples`, `relationships`, detailed descriptions
- **Version tracked**: Committed to git with version metadata

### Impact Metrics
- ⭐ **Code Quality**: 5/5 (types, validation, documentation)
- ⭐ **Type Safety**: 5/5 (Pydantic models, proper types)
- ⭐ **Validation**: 5/5 (regex patterns, constraints)
- ⭐ **Documentation**: 5/5 (examples, relationships)
- ⭐ **API Coverage**: 5/5 (+41% more endpoints)

## Usage Examples

### Before (REMOVED)
```bash
# ❌ OLD - No longer supported
python3 generate.py --host 192.168.1.99 --token abc123 --endpoint cmdb.firewall.policy
python3 generate.py --force --all  # Force re-download schemas
```

### After (CURRENT)
```bash
# ✅ NEW - Schema-only approach
python3 generate.py --endpoint cmdb.firewall.policy
python3 generate.py --category cmdb
python3 generate.py --all
python3 generate.py --version 7.6.5 --endpoint cmdb.firewall.address
python3 generate.py --from-file .dev/endpoints_all.json
```

## How to Update Schemas

Since the generator no longer downloads schemas, updates must be done manually:

1. **Run the schema fetcher** (separate tool):
   ```bash
   cd /app/dev/classes/fortinet/schema
   python3 fetch_schemas.py --version 7.6.5 --host YOUR_HOST --token YOUR_TOKEN
   ```

2. **Commit the updated schemas**:
   ```bash
   git add schema/7.6.5/
   git commit -m "Update schemas to FortiOS 7.6.5 build XXXX"
   ```

3. **Generate code from new schemas**:
   ```bash
   cd .dev/generator
   python3 generate.py --all
   ```

## Testing

The refactored generator has been tested and verified:

```bash
# Test single endpoint generation
python3 generate.py --version 7.6.5 --endpoint cmdb.firewall.address

# Output shows successful generation:
# ✅ Generated endpoint class
# ✅ Generated validator with enhanced v1.7.0 features
# ✅ Generated test with HTTP 500/503 error handling
```

## Files Modified

- `.dev/generator/generate.py`:
  - Removed `SchemaDownloader` import
  - Updated `CodeGenerator.__init__()` signature (5 params instead of 8)
  - Removed `self.downloader`, `self.force_download` attributes
  - Updated `generate_endpoint()` to find schemas from disk
  - Updated `generate_category()` to use existing schemas only
  - Updated `generate_all()` to skip download logic
  - Updated `_generate_category_stubs()` for new paths
  - Removed `--host`, `--token`, `--force` CLI arguments
  - Updated help examples

## Benefits

1. **Prevents Accidents**: No way to accidentally regenerate with old schemas
2. **Version Control**: Schemas tracked in git with clear versioning
3. **Type Safety**: All generated code uses enhanced Pydantic types
4. **Better Validation**: Regex patterns and constraints from v1.7.0 schemas
5. **Improved Docs**: Examples and relationships in generated validators
6. **Simpler CLI**: Fewer arguments, clearer purpose

## Backwards Compatibility

⚠️ **Breaking Change**: The old command-line arguments are no longer supported.

**Migration Guide**:
- Remove `--host` and `--token` from any scripts
- Remove `--force` flags
- Ensure schemas exist in `/schema/7.6.5/` before running generator
- Update default version from `7.6` to `7.6.5` if needed

## Related Documentation

- Schema v1.7.0 features: See `/schema/7.6.5/README.md`
- Test improvements: See `.dev/generator/templates/test_basic.py.j2` (HTTP 500/503 handling)
- Schema comparison: See archive analysis showing 41% coverage improvement

## Validation

✅ All lint errors resolved  
✅ Generator tested with real endpoint (`cmdb.firewall.address`)  
✅ Generated code uses v1.7.0 schema features (Pydantic types, validation)  
✅ Generated tests include HTTP 500/503 error handling  
✅ Help text updated with correct examples  
✅ No references to removed parameters remain  

---

**Conclusion**: The generator is now simpler, safer, and produces higher-quality code by using only the enhanced v1.7.0 schemas. Future updates to schemas should be done via the dedicated schema fetcher tool, ensuring all changes are version-controlled and reviewed before code generation.
