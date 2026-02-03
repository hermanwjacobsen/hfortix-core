# Code Generator Quick Reference

## ✅ Current Usage (Schema-Only Mode)

The generator now uses **ONLY** pre-existing schemas from `/schema/7.6.5/`.  
No more downloading schemas from FortiGate API during code generation.

### Basic Commands

```bash
# Generate single endpoint
python3 generate.py --endpoint cmdb.firewall.policy

# Generate entire category
python3 generate.py --category cmdb

# Generate all endpoints
python3 generate.py --all

# Generate from file
python3 generate.py --from-file .dev/endpoints_all.json

# Specify FortiOS version (must match schema directory)
python3 generate.py --version 7.6.5 --endpoint cmdb.firewall.address
```

### Available Arguments

| Argument | Required | Default | Description |
|----------|----------|---------|-------------|
| `--endpoint` | Yes* | - | Single endpoint (e.g., `cmdb.firewall.policy`) |
| `--category` | Yes* | - | Category (`cmdb`, `monitor`, `log`, `service`) |
| `--all` | Yes* | - | Generate all endpoints |
| `--from-file` | Yes* | - | Generate from list file (.txt or .json) |
| `--version` | No | `7.6.5` | FortiOS version (must match schema dir) |
| `--output-dir` | No | `packages/fortios/...` | Output directory |
| `--template-dir` | No | `.dev/generator/templates` | Template directory |
| `--schema-dir` | No | `schema/` | Schema root directory |
| `--max-errors` | No | `10` | Max errors to display (0 = all) |

\* Exactly one of `--endpoint`, `--category`, `--all`, or `--from-file` is required.

## ❌ Removed (Old Download Mode)

These arguments are **no longer supported**:

```bash
# ❌ REMOVED - No longer works
--host 192.168.1.99        # FortiGate hostname
--token abc123             # API token
--force                    # Force schema re-download
```

## 📋 Common Workflows

### Generate New Endpoint

```bash
# 1. Ensure schema exists
ls schema/7.6.5/cmdb/firewall/policy.json

# 2. Generate code
python3 generate.py --endpoint cmdb.firewall.policy

# 3. Review generated files
ls -l packages/fortios/hfortix_fortios/api/v2/cmdb/firewall/policy.py
ls -l .tests/pytests/api/cmdb/firewall/auto_test_policy.py
```

### Regenerate Entire Category

```bash
# Generate all CMDB endpoints (561 endpoints)
python3 generate.py --category cmdb

# Generate all Monitor endpoints (490 endpoints)
python3 generate.py --category monitor

# Generate all Log endpoints (286 endpoints)
python3 generate.py --category log
```

### Regenerate Everything

```bash
# Full regeneration (1,348 endpoints)
python3 generate.py --all

# This will:
# - Generate all endpoint classes (.py)
# - Generate all type stubs (.pyi)
# - Generate all validators (_helpers/*.py)
# - Generate all tests (auto_test_*.py)
# - Regenerate all __init__.py files
```

### Generate from Custom List

```bash
# Create custom endpoint list
cat > my_endpoints.txt << EOF
cmdb.firewall.policy
cmdb.firewall.address
cmdb.firewall.addrgrp
EOF

# Generate only those endpoints
python3 generate.py --from-file my_endpoints.txt
```

## 🔧 Schema Updates

To update schemas (requires FortiGate access):

```bash
# 1. Run schema fetcher (separate tool)
cd schema
python3 fetch_schemas.py --version 7.6.5 --host YOUR_HOST --token YOUR_TOKEN

# 2. Review changes
git diff schema/7.6.5/

# 3. Commit schemas
git add schema/7.6.5/
git commit -m "Update schemas to FortiOS 7.6.5 build XXXX"

# 4. Regenerate code from new schemas
cd ../.dev/generator
python3 generate.py --all
```

## 📊 What Gets Generated

For each endpoint, the generator creates:

1. **Endpoint Class** (`packages/fortios/.../endpoint.py`)
   - CRUD methods (get, create, update, delete)
   - Async variants
   - Type hints with Pydantic models

2. **Type Stub** (`packages/fortios/.../endpoint.pyi`)
   - Static type information for IDEs

3. **Validator** (`packages/fortios/.../_helpers/endpoint.py`)
   - Field validation with regex patterns
   - Type enforcement
   - Required field tracking
   - Rich metadata comments

4. **Validator Stub** (`packages/fortios/.../_helpers/endpoint.pyi`)
   - Type information for validators

5. **Test File** (`.tests/pytests/api/.../auto_test_endpoint.py`)
   - Basic CRUD tests
   - Error handling (400/404/405/424/500/503)
   - Pytest fixtures

6. **Init Files** (`__init__.py` in each category)
   - Auto-imports all endpoints
   - Type annotations

## 🎯 Best Practices

1. **Always check schema exists** before generating:
   ```bash
   ls schema/7.6.5/cmdb/firewall/policy.json || echo "Schema missing!"
   ```

2. **Use `--from-file`** for selective regeneration:
   ```bash
   # Only regenerate modified schemas
   python3 generate.py --from-file updated_endpoints.txt
   ```

3. **Review generated code** for quality:
   ```bash
   # Check validator has proper types
   grep "pydantic_type" packages/fortios/.../helpers/endpoint.py
   
   # Check test has error handling
   grep "500.*503" .tests/pytests/api/.../auto_test_endpoint.py
   ```

4. **Commit schemas separately** from generated code:
   ```bash
   git add schema/7.6.5/
   git commit -m "Update schemas"
   
   git add packages/ .tests/
   git commit -m "Regenerate code from updated schemas"
   ```

## 🚨 Troubleshooting

### Error: Schema file not found

```bash
# Problem: Schema doesn't exist for that endpoint
❌ Error: Schema file not found for endpoint cmdb.firewall.xyz

# Solution: Check schema exists
ls schema/7.6.5/cmdb/firewall/xyz.json
# If missing, run schema fetcher or check endpoint name
```

### Error: Invalid version directory

```bash
# Problem: Version directory doesn't exist
❌ Error: Schema directory not found: schema/7.6.5

# Solution: Create directory or check version
ls -ld schema/7.6.5/
# Update --version argument to match existing directory
```

### Error: Template not found

```bash
# Problem: Template files missing
❌ Error: Template not found: templates/endpoint.py.j2

# Solution: Check template directory
ls .dev/generator/templates/
# Use --template-dir if templates are elsewhere
```

## 📝 Version History

- **v1.7.0** (Current): Schema-only mode, enhanced schemas (1,348 endpoints)
- **v1.6.x**: Dual-mode (download + existing schemas) - deprecated
- **v1.5.x**: Download-only mode (954 endpoints) - removed

---

For more details, see `SCHEMA_ONLY_MIGRATION.md`
