# FortiOS API Generator

**Regenerable, schema-driven code generator for FortiOS API client**

**Last Updated:** January 7, 2026

## ⚠️ Scope

**Fully Supported Categories:**
- ✅ **CMDB** - Configuration endpoints (full CRUD + schemas)
- ✅ **Monitor** - Monitoring endpoints (typically GET, some POST)
- ✅ **Service** - Service endpoints (if schemas available)
- ✅ **LOG** - Log endpoints with path parameters (specialized generator)

**Current Status (Schema v1.7.0 for FortiOS 7.6.5):**
- **CMDB:** 561 endpoints generated ✅
- **Monitor:** 490 endpoints generated ✅
- **Log:** 286 endpoints generated ✅
- **Service:** 11 endpoints generated ✅
- **TOTAL:** 1,348 endpoints across all categories
- **Tests:** 4,488 collected
- **Implementation Files:** 2,129 .py files with 2,129 .pyi stubs (100% coverage)

**Latest Features (Jan 2026):**
- 🔍 **Runtime Schema Introspection** - `get_schema()` method on all endpoints
- 🎯 **Enhanced Query Parameters** - Explicit `filter`, `count`, `start` parameters
- 📊 **100% Coverage** - All 1,348 endpoints updated with new features

---

## 📚 Documentation

**Start Here:**
- **[DOCS_INDEX.md](DOCS_INDEX.md)** - 📑 Complete documentation index
- **[QUICK_START.md](QUICK_START.md)** - ⚡ Get started in 5 minutes

**New Features (Jan 2026):**
- **[docs/QUERY_PARAMS_AND_SCHEMA_FEATURES.md](docs/QUERY_PARAMS_AND_SCHEMA_FEATURES.md)** - 🔍 Query params & schema guide
- **[docs/QUICK_REFERENCE_QUERY_PARAMS.md](docs/QUICK_REFERENCE_QUERY_PARAMS.md)** - 📋 Quick reference

**Quick Reference:**
- **[QUICKREF.md](QUICKREF.md)** - 🛠 Command reference
- **[WORKFLOW_GUIDE.md](WORKFLOW_GUIDE.md)** - 📖 Development workflow
- **[EDGE_CASES.md](EDGE_CASES.md)** - ⚙️ Known edge cases

**API Reference:**
- **[VALIDATOR_API_REFERENCE.md](VALIDATOR_API_REFERENCE.md)** - Validator API
- **[VALIDATOR_CAPABILITIES.md](VALIDATOR_CAPABILITIES.md)** - What validators can do
- **[ACTION_METHODS_IMPLEMENTATION.md](ACTION_METHODS_IMPLEMENTATION.md)** - Action methods

**Advanced:**
- **[docs/GENERATOR_DESIGN.md](docs/GENERATOR_DESIGN.md)** - Architecture
- **[docs/LOG_CATEGORY_NOTES.md](docs/LOG_CATEGORY_NOTES.md)** - LOG category design
- **[CHANGELOG.md](CHANGELOG.md)** - Change history

---

## Directory Structure

```
.dev/generator/
├── README.md                      # This file - main documentation
├── generate.py                    # Main generator orchestrator
├── regenerate_all.sh             # ONE-CLICK complete regeneration script ⭐
├── regenerate_category.sh        # Regenerate specific category
│
├── generators/                    # Code generators
│   ├── endpoint_generator.py     # CMDB/Monitor endpoint classes
│   ├── validator_generator.py    # Pydantic validators from schemas
│   ├── pyi_generator.py          # Type stub (.pyi) generator
│   ├── log_generator.py          # LOG category endpoint generator
│   └── regenerate_init_files.py  # __init__.py file generator
│
├── schema_management/             # Schema tools & storage
│   ├── README.md                 # Schema management docs
│   ├── download_schemas.py       # Download schemas from FortiGate
│   ├── schema_parser.py          # Parse JSON schemas
│   ├── swagger_parser.py         # Parse Swagger docs (LOG endpoints)
│   └── swagger/                  # Swagger documentation files
│
├── helpers/                       # Helper utilities
│   └── generate_tests.py         # Test file generator
│
├── templates/                     # Jinja2 templates
│   ├── endpoint_template.j2      # Endpoint class template
│   ├── validator_template.j2     # Validator class template
│   └── ...
│
└── docs/                          # Extended documentation
    ├── NAMING_COLLISION_SOLUTION.md  # How _base pattern works
    ├── GENERATOR_DESIGN.md       # Architecture & design
    ├── FORTIOS_FILTERING.md      # Filtering capabilities
    └── ...
```

---

## 🚀 Quick Start

### ONE COMMAND - Complete Regeneration

The generator now features auto-detection - just run it with no arguments:

```bash
cd /app/dev/classes/fortinet/.dev/generator

# Auto-detect latest version and regenerate everything
python3 generate.py
```

That's it! The generator will:
1. Auto-detect the latest FortiOS version (from `schema_management/schema/`)
2. Generate all 1065+ endpoints across all categories (CMDB, MONITOR, LOG, SERVICE)
3. Generate validators, type stubs, tests, and __init__ files
4. Display progress with ✅ confirmations

### Advanced Usage

```bash
# List available FortiOS versions
python3 generate.py --list-versions

# Use specific version
python3 generate.py --version 7.4.8

# Generate single category
python3 generate.py --category cmdb

# Generate single endpoint
python3 generate.py --endpoint cmdb.firewall.policy --version 7.6.5

# Generate from endpoint list file
python3 generate.py --from-file .dev/endpoints_all.json
```

### Legacy Shell Scripts (Still Available)

```bash
### Legacy Shell Scripts (Still Available)

```bash
# Complete regeneration using shell script
./regenerate_all.sh

# Regenerate specific category
./regenerate_category.sh cmdb
```

**What the generator does:**

1. ✅ Auto-detects schemas in `schema_management/schema/{version}/`
2. ✅ Deletes old generated code
3. ✅ Generates all endpoints
4. ✅ Generates all `__init__.py` files  
5. ✅ Generates all type stubs (`.pyi`)
6. ✅ Generates all tests
7. ✅ Verifies structure

### Download Schemas

To get schemas from a FortiGate device:

```bash
cd schema_management
python download_schemas.py --host 192.168.1.99 --username admin --version 7.6.5
```

---

## Key Features

### _base Pattern for Collision Prevention

The generator uses a `_base.py` naming pattern to prevent Python import shadowing when an endpoint has both a main endpoint and sub-endpoints:

**Example:** `monitor/firewall/gtp`
- Has GET method: `/api/v2/monitor/firewall/gtp`
- Has sub-endpoint: `/api/v2/monitor/firewall/gtp/runtime-statistics`

**Generated Structure:**
```
monitor/firewall/
├── gtp_base.py              # Main endpoint class with get() method
└── gtp/                     # Sub-endpoints directory
    ├── __init__.py          # Wrapper: class Gtp(GtpBase) + sub-endpoints
    └── runtime_statistics.py
```

See [docs/NAMING_COLLISION_SOLUTION.md](docs/NAMING_COLLISION_SOLUTION.md) for details.

### Automatic Test Generation

Every endpoint gets a full test suite automatically:
- GET/POST/PUT/DELETE/UPDATE tests
- VDOM parameter tests  
- Response validation
- Error handling

### Type Safety

All endpoints include:
- Type stubs (`.pyi` files) for IDE autocomplete
- Pydantic validators for runtime validation
- Proper type hints throughout

---

## Testing

Run all tests:

```bash
cd /app/dev/classes/fortinet
.venv/bin/python .tests/pytests/__runtests__.py
```

Current status: **3,486 passing, 1,002 skipped, 0 failures** ✅

---

## Contributing

When modifying the generator:

1. **Update templates** in `templates/` directory
2. **Test with single endpoint** first
3. **Run regeneration** with `./regenerate_all.sh`
4. **Verify tests pass** with `__runtests__.py`
5. **Update docs** if behavior changes

---

## Troubleshooting

### Import Errors After Regeneration

Clear Python cache:
```bash
find packages/fortios -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
```

### Tests Failing

Check if `__init__.py` files were regenerated:
```bash
cd .dev/generator
python generators/regenerate_init_files.py
```

### Schema Download Issues

Verify FortiGate API access:
```bash
curl -k https://192.168.1.99/api/v2/cmdb/system/interface?access_token=YOUR_TOKEN
```

---

## Documentation Index

**Quick Reference:**
- [QUICKREF.md](QUICKREF.md) - Command cheat sheet
- [QUICK_START.md](QUICK_START.md) - 5-minute getting started

**Generator:**
- [docs/GENERATOR_DESIGN.md](docs/GENERATOR_DESIGN.md) - Architecture
- [docs/NAMING_COLLISION_SOLUTION.md](docs/NAMING_COLLISION_SOLUTION.md) - _base pattern

**FortiOS API:**
- [docs/FORTIOS_FILTERING.md](docs/FORTIOS_FILTERING.md) - Query parameters
- [docs/FORTIOS_ADVANCED_FEATURES.md](docs/FORTIOS_ADVANCED_FEATURES.md) - Advanced features

**Development:**
- [WORKFLOW_GUIDE.md](WORKFLOW_GUIDE.md) - Development workflow
- [VALIDATOR_CAPABILITIES.md](VALIDATOR_CAPABILITIES.md) - Validator features

---

## License

See main project LICENSE file.
