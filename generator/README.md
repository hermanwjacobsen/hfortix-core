# HFortix Code Generator Tools

This directory contains tools used during the code generation process for the HFortix FortiOS library.

## Files

### `scan_underscore_fields.py`
Scans all schema files to identify fields where the FortiOS API expects underscores (not hyphens).

**Usage:**
```bash
# View results without updating
python3 generator/scan_underscore_fields.py

# Automatically update field_overrides.py
python3 generator/scan_underscore_fields.py --update
```

**Output:**
- Lists all fields with underscores by API type (CMDB, Monitor, Log, Service)
- Shows statistics and summary
- Optionally updates `packages/fortios/hfortix_fortios/_helpers/field_overrides.py`

### `update_field_overrides.py`
Main entry point for generator integration. Updates `field_overrides.py` from schema files.

**Usage:**
```bash
# Standalone
python3 generator/update_field_overrides.py

# With custom paths
python3 generator/update_field_overrides.py --schema-path schema/7.6.5 --output packages/fortios/hfortix_fortios/_helpers/field_overrides.py

# Quiet mode
python3 generator/update_field_overrides.py --quiet
```

**Integration:**
```python
from generator.update_field_overrides import update_from_schemas

# In your generator code
success = update_from_schemas(
    schema_base_path='schema/7.6.5',
    verbose=True
)

if success:
    # Continue with API code generation
    generate_api_code()
```

## Generator Workflow

The recommended generator workflow is:

1. **Download/Generate Schemas** → `schema/7.6.5/`
2. **Update Field Overrides** → Run `update_field_overrides.py`
3. **Generate API Code** → Generate Python endpoint files
4. **Run Tests** → Verify everything works
5. **Commit** → Include updated `field_overrides.py`

### Step-by-step Example

```bash
# Step 1: Ensure schemas are present
ls schema/7.6.5/cmdb/ schema/7.6.5/monitor/

# Step 2: Update field overrides from schemas
python3 generator/update_field_overrides.py

# Step 3: (Your generator runs here to create API code)
# python3 generator/generate_api.py

# Step 4: Test the results
python3 test_underscore_preservation.py
python3 test_id_list_bug_fix.py

# Step 5: Review and commit
git diff packages/fortios/hfortix_fortios/_helpers/field_overrides.py
git add packages/fortios/hfortix_fortios/_helpers/field_overrides.py
git commit -m "Update field overrides from schemas"
```

## What Gets Generated

### `CMDB_BODY_FIELD_NO_HYPHEN`
Fields in CMDB endpoints where the API expects underscores:
```python
CMDB_BODY_FIELD_NO_HYPHEN = {
    "block_ack_flood",
    "block_ack_flood_thresh",
    "block_ack_flood_time",
    "switch_dhcp_opt43_key",
}
```

### `MONITOR_BODY_FIELD_NO_HYPHEN`
Fields in Monitor endpoints where the API expects underscores:
```python
MONITOR_BODY_FIELD_NO_HYPHEN = {
    "id_list",
    "file_content",
    "ems_id",
    "account_id",
    # ... 196 more fields
}
```

## Why This Exists

The FortiOS API is inconsistent with field naming:
- **Most fields** use kebab-case: `source-ip`, `https-port`
- **Some fields** use snake_case: `id_list`, `file_content`
- **Same logical field** can vary: `ems-id` (CMDB) vs `ems_id` (Monitor)

These tools ensure the library correctly handles both formats based on actual schema data.

## Maintenance

- **When to run**: After updating schemas to a new FortiOS version
- **Frequency**: Once per schema version update
- **Auto-update**: Can be integrated into CI/CD pipeline

## Related Files

- Input: `schema/7.6.5/**/*.json` - Schema files (1,350+ files)
- Output: `packages/fortios/hfortix_fortios/_helpers/field_overrides.py` - Field mapping rules
- Tests: `test_underscore_preservation.py`, `test_id_list_bug_fix.py`
- Docs: `docs/fortios/UNDERSCORE_HYPHEN_INCONSISTENCY.md`

## Version History

- **v0.5.129** (2026-01-20): Created automated scanner and updater
  - Scans all schemas to find underscore fields
  - Auto-updates field_overrides.py
  - Replaces manual maintenance with schema-driven approach
