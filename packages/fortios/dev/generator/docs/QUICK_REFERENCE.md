# Generator Quick Reference

**Last Updated:** January 2026  
**Schema Version:** v1.7.0 for FortiOS 7.6.5  
**Total Endpoints:** 1,348 (CMDB: 561, Monitor: 490, Log: 286, Service: 11)

---

## 📋 Table of Contents

1. [Generator Commands](#-generator-commands)
2. [Query Parameters](#-query-parameters)
3. [Filter Operators](#-filter-operators)
4. [Pagination](#-pagination)
5. [Validator Metadata](#-validator-metadata)
6. [Common Patterns](#-common-patterns)

---

## 🚀 Generator Commands

### Basic Usage

```bash
cd /app/dev/classes/fortinet/.dev/generator

# Generate single endpoint
python3 generate.py --endpoint cmdb.firewall.policy

# Generate entire category
python3 generate.py --category cmdb

# Generate all endpoints (1,348 total)
python3 generate.py --all

# Specify FortiOS version
python3 generate.py --version 7.6.5 --endpoint cmdb.firewall.address
```

### Command Arguments

| Argument | Required | Default | Description |
|----------|----------|---------|-------------|
| `--endpoint` | Yes* | - | Single endpoint (e.g., `cmdb.firewall.policy`) |
| `--category` | Yes* | - | Category (`cmdb`, `monitor`, `log`, `service`) |
| `--all` | Yes* | - | Generate all endpoints |
| `--from-file` | Yes* | - | Generate from list file (.txt or .json) |
| `--version` | No | `7.6.5` | FortiOS version (must match schema dir) |
| `--output-dir` | No | `packages/fortios/...` | Output directory |
| `--list-versions` | No | - | Show available schema versions |

\* Exactly one of `--endpoint`, `--category`, `--all`, or `--from-file` is required.

### Regeneration Scripts

```bash
# Regenerate single category
./regenerate_category.sh cmdb 7.6.5
./regenerate_category.sh monitor 7.6.5

# Regenerate everything (deletes + regenerates)
./regenerate_all.sh
```

### Generated Output

For each endpoint (e.g., `cmdb.firewall.address`):

| File | Purpose |
|------|---------|
| `firewall/address.py` | Endpoint class with CRUD methods |
| `firewall/address.pyi` | Type stubs for IDE support |
| `firewall/_helpers/address.py` | Validator with metadata |
| `auto_test_address.py` | Auto-generated tests |

---

## 🔍 Query Parameters

### get_schema() Method

```python
# Get endpoint schema from live firewall
schema = fgt.api.cmdb.firewall.policy.get_schema()

# Available on all CMDB endpoints
schema = fgt.api.cmdb.<category>.<endpoint>.get_schema()
```

**Returns:** Field definitions, types, enums, validation rules, defaults

### Filter Parameter

```python
# Single filter
result = fgt.api.cmdb.firewall.address.get(filter=["name==test"])

# Multiple filters (AND logic)
result = fgt.api.cmdb.firewall.policy.get(
    filter=["status==enable", "action==accept"]
)

# OR logic (comma within string)
result = fgt.api.cmdb.firewall.address.get(filter=["name==web,name==mail"])

# Combined AND/OR
result = fgt.api.cmdb.firewall.policy.get(
    filter=["status==enable", "name==web,name==mail"]
)
```

---

## ⚖️ Filter Operators

| Operator | Meaning | Example |
|----------|---------|---------|
| `==` | Equals | `"name==test"` |
| `!=` | Not equals | `"status!=disable"` |
| `=@` | Contains | `"comment=@prod"` |
| `!@` | Not contains | `"name!@temp"` |
| `<=` | Less/equal | `"policyid<=100"` |
| `<` | Less than | `"sessions<1000"` |
| `>=` | Greater/equal | `"policyid>=1"` |
| `>` | Greater than | `"sessions>5000"` |

---

## 📄 Pagination

```python
# First 100 results
result = fgt.api.cmdb.firewall.policy.get(count=100)

# Skip first 100, get next 100
result = fgt.api.cmdb.firewall.policy.get(start=100, count=100)

# Filter + pagination
result = fgt.api.cmdb.firewall.policy.get(
    filter=["status==enable"],
    start=0,
    count=100
)
```

### Get All Results (Paginated)

```python
def get_all(endpoint, page_size=100):
    """Fetch all results with pagination."""
    results = []
    start = 0
    while True:
        page = endpoint.get(start=start, count=page_size)
        if not page:
            break
        results.extend(page if isinstance(page, list) else [page])
        if len(page) < page_size:
            break
        start += page_size
    return results

all_policies = get_all(fgt.api.cmdb.firewall.policy)
```

---

## 🔧 Validator Metadata

### Import Helper Functions

```python
from hfortix_fortios.api.v2.cmdb.firewall._helpers.policy import (
    # Metadata access
    get_field_type,        # Get field type ("string", "integer", "option")
    get_field_description, # Get field help text
    get_field_constraints, # Get min/max, string lengths
    get_field_default,     # Get default value
    get_field_options,     # Get enum options
    get_field_metadata,    # Get all metadata at once
    get_all_fields,        # List all field names
    get_schema_info,       # Get endpoint info
    
    # Validation
    validate_field_value,  # Validate single field
    
    # Constants
    FIELD_TYPES,
    FIELD_DESCRIPTIONS,
    FIELDS_WITH_DEFAULTS,
    REQUIRED_FIELDS,
    NESTED_SCHEMAS,
    SCHEMA_INFO,
)
```

### Common Operations

```python
# Get field type
field_type = get_field_type("action")  # "option"

# Get enum options
options = get_field_options("action")  # ["accept", "deny", "ipsec"]

# Validate a value
is_valid, error = validate_field_value("action", "accept")

# Get all metadata for a field
meta = get_field_metadata("status")
# {
#   "name": "status",
#   "type": "option",
#   "description": "Enable or disable this policy.",
#   "default": "enable",
#   "options": ["enable", "disable"]
# }

# Get endpoint info
info = get_schema_info()
# {
#   "endpoint": "firewall/policy",
#   "mkey": "policyid",
#   "mkey_type": "integer",
#   "total_fields": 184
# }
```

---

## 🎯 Common Patterns

### Basic CRUD Operations

```python
from hfortix_fortios import FortiOS

fgt = FortiOS(host="192.168.1.99", token="your-token")

# GET all
policies = fgt.api.cmdb.firewall.policy.get()

# GET one by mkey
policy = fgt.api.cmdb.firewall.policy.get(policyid=1)

# POST (create)
result = fgt.api.cmdb.firewall.address.post(
    name="test-addr",
    subnet="10.0.0.0/24"
)

# PUT (update)
result = fgt.api.cmdb.firewall.address.put(
    name="test-addr",
    comment="Updated comment"
)

# DELETE
result = fgt.api.cmdb.firewall.address.delete(name="test-addr")

# Check existence
exists = fgt.api.cmdb.firewall.address.exists(name="test-addr")
```

### Object Mode vs Dict Mode

```python
# Dict mode (default) - returns dictionaries
fgt = FortiOS(host="...", token="...", response_mode="dict")
policy = fgt.api.cmdb.firewall.policy.get(policyid=1)
print(policy["name"])  # Dictionary access

# Object mode - returns FortiObject with attribute access
fgt = FortiOS(host="...", token="...", response_mode="object")
policy = fgt.api.cmdb.firewall.policy.get(policyid=1)
print(policy.name)  # Attribute access
print(policy.srcaddr[0].name)  # Nested access
```

### Raw JSON Response

```python
# Get raw API response with metadata
raw = fgt.api.cmdb.firewall.policy.get(policyid=1, raw_json=True)
print(raw["http_status"])  # 200
print(raw["results"])      # Actual data
```

### Validation Before Submit

```python
from hfortix_fortios.api.v2.cmdb.firewall._helpers.policy import (
    validate_field_value,
    REQUIRED_FIELDS,
)

payload = {
    "name": "test-policy",
    "action": "accept",
    "srcintf": [{"name": "port1"}],
    "dstintf": [{"name": "port2"}],
    "schedule": "always",
}

# Validate required fields
for field in REQUIRED_FIELDS:
    if field not in payload:
        print(f"Missing required field: {field}")

# Validate field values
for field_name, value in payload.items():
    is_valid, error = validate_field_value(field_name, value)
    if not is_valid:
        print(f"Invalid {field_name}: {error}")
```

---

## 📁 File Locations

| Item | Path |
|------|------|
| Generator | `.dev/generator/generate.py` |
| Templates | `.dev/generator/templates/` |
| Schemas | `schema/7.6.5/` |
| Generated Code | `packages/fortios/hfortix_fortios/api/v2/` |
| Tests | `packages/fortios/hfortix_fortios/api/v2/tests/` |

---

## 🔗 Related Documentation

- [WORKFLOW_GUIDE.md](WORKFLOW_GUIDE.md) - Development workflow
- [EDGE_CASES.md](EDGE_CASES.md) - Known edge cases
- [GENERATOR_DESIGN.md](GENERATOR_DESIGN.md) - Architecture details
- [FORTIOS_API_GUIDE.md](FORTIOS_API_GUIDE.md) - FortiOS API reference
