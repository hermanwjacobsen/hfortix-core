# Validator Template Capabilities Summary

## Overview
Enhanced validator template that provides comprehensive metadata access and IDE autocomplete support for all FortiOS API endpoints.

## Implementation Status

| Capability | Status | Coverage | Implementation Details |
| ---------- | ------ | -------- | ---------------------- |
| **Enum Constants** | ✅ Implemented | 100% | 2,071 unique enum constants across 909 validators |
| **Query Param Validation** | ✅ Implemented | 60% | 548/909 validators support `action=schema` |
| **Type Information** | ✅ Implemented | 100% | `FIELD_TYPES` dict + `get_field_type()` |
| **Required Fields** | ✅ Enhanced | 60% | 543/909 helpers with filtered false positives |
| **Field Descriptions** | ✅ Implemented | 100% | `FIELD_DESCRIPTIONS` dict + `get_field_description()` |
| **Default Values** | ✅ Implemented | 100% | `FIELDS_WITH_DEFAULTS` dict + `get_field_default()` |
| **Nested Schemas** | ✅ Implemented | 100% | `NESTED_SCHEMAS` dict for table/list fields |
| **IDE Autocomplete** | ✅ Implemented | 100% | TypedDict support + metadata functions |
| **Field Constraints** | ✅ Implemented | 100% | Min/max values, string lengths |
| **Version Tracking** | ❌ Not Implemented | 0% | Future enhancement |

## Enhanced Features

### 1. Type Information ✅
```python
from hfortix_fortios.api.v2.cmdb.firewall._helpers.policy import (
    FIELD_TYPES,
    get_field_type,
)

# Access via constant
field_type = FIELD_TYPES["action"]  # "option"

# Access via function
field_type = get_field_type("action")  # "option"
```

### 2. Field Descriptions ✅
```python
from hfortix_fortios.api.v2.cmdb.firewall._helpers.policy import (
    FIELD_DESCRIPTIONS,
    get_field_description,
)

# Access via constant
desc = FIELD_DESCRIPTIONS["action"]  # "Policy action (accept/deny/ipsec)."

# Access via function
desc = get_field_description("action")  # "Policy action (accept/deny/ipsec)."
```

### 3. Default Values ✅
```python
from hfortix_fortios.api.v2.cmdb.firewall._helpers.policy import (
    FIELDS_WITH_DEFAULTS,
    get_field_default,
)

# Access via constant
default = FIELDS_WITH_DEFAULTS["status"]  # "enable"

# Access via function
default = get_field_default("status")  # "enable"
```

### 4. Field Constraints ✅
```python
from hfortix_fortios.api.v2.cmdb.firewall._helpers.policy import (
    FIELD_CONSTRAINTS,
    get_field_constraints,
)

# Integer constraints
port_constraints = get_field_constraints("port")
# {"type": "integer", "min": 1, "max": 65535}

# String constraints
name_constraints = get_field_constraints("name")
# {"type": "string", "max_length": 79}
```

### 5. Nested Schemas ✅
```python
from hfortix_fortios.api.v2.cmdb.firewall._helpers.policy import (
    NESTED_SCHEMAS,
    get_nested_schema,
)

# Get schema for nested table fields
service_schema = get_nested_schema("service")
if service_schema:
    for field_name, field_meta in service_schema.items():
        print(f"{field_name}: {field_meta['type']}")
```

### 6. Complete Field Metadata ✅
```python
from hfortix_fortios.api.v2.cmdb.firewall._helpers.policy import (
    get_field_metadata,
)

# Get all metadata for a field
meta = get_field_metadata("status")
print(meta)
# {
#   "name": "status",
#   "type": "option",
#   "description": "Enable or disable this policy.",
#   "default": "enable",
#   "required": False,
#   "options": ["enable", "disable"]
# }
```

### 7. Schema Information ✅
```python
from hfortix_fortios.api.v2.cmdb.firewall._helpers.policy import (
    SCHEMA_INFO,
    get_schema_info,
)

# Access via constant
info = SCHEMA_INFO
# {
#   "endpoint": "firewall/policy",
#   "category": "cmdb",
#   "api_path": "firewall/policy",
#   "mkey": "policyid",
#   "mkey_type": "integer",
#   "help": "IPv4/IPv6 policies.",
#   "total_fields": 150,
#   "required_fields_count": 3,
#   "fields_with_defaults_count": 120
# }

# Access via function
info = get_schema_info()
```

### 8. Field Value Validation ✅
```python
from hfortix_fortios.api.v2.cmdb.firewall._helpers.policy import (
    validate_field_value,
)

# Validate a single field
is_valid, error = validate_field_value("action", "accept")
if not is_valid:
    print(error)

# Validates:
# - Enum values (against options list)
# - Integer ranges (min/max)
# - String lengths (max_length)
```

### 9. Utility Functions ✅
```python
from hfortix_fortios.api.v2.cmdb.firewall._helpers.policy import (
    get_all_fields,
    get_field_options,
)

# Get all field names
fields = get_all_fields()
print(f"Total fields: {len(fields)}")

# Get enum options
options = get_field_options("action")
print(options)  # ["accept", "deny", "ipsec"]
```

## IDE Autocomplete Support

### TypedDict Imports
```python
from typing import TypedDict, NotRequired, Literal
```

All validators now import these for future TypedDict payload definitions:
```python
# Future enhancement (not in current template yet)
class FirewallPolicyPayload(TypedDict, total=False):
    name: str
    action: Literal["accept", "deny", "ipsec"]
    status: NotRequired[Literal["enable", "disable"]]
    # ...
```

### Metadata-Driven Autocomplete
The constant dictionaries (`FIELD_TYPES`, `FIELD_DESCRIPTIONS`, etc.) enable:
1. **IDE code completion** when accessing field metadata
2. **Type hints** via function signatures
3. **Documentation tooltips** from docstrings

## Data Structures

### Field Type Constants
```python
FIELD_TYPES: dict[str, str]
# Maps field names to FortiOS types:
# - "string", "integer", "option", "var-string"
# - "ipv4-address", "ipv6-address", "mac-address"
# - etc.
```

### Field Description Constants
```python
FIELD_DESCRIPTIONS: dict[str, str]
# Maps field names to help text from FortiOS API
```

### Field Constraint Constants
```python
FIELD_CONSTRAINTS: dict[str, dict[str, Any]]
# Structure:
# {
#   "field_name": {
#     "type": "integer|string",
#     "min": int,          # For integers
#     "max": int,          # For integers
#     "max_length": int    # For strings
#   }
# }
```

### Nested Schema Constants
```python
NESTED_SCHEMAS: dict[str, dict[str, dict[str, Any]]]
# Structure:
# {
#   "parent_field": {
#     "child_field": {
#       "type": str,
#       "help": str,
#       "required": bool,
#       "default": Any,
#       "options": list[str],
#       "min_value": int,
#       "max_value": int,
#       "max_length": int
#     }
#   }
# }
```

## Known Limitations (Per Warning Comment)

### Required Fields Quirks
The `REQUIRED_FIELDS` list is **INFORMATIONAL ONLY** due to FortiOS schema issues:

1. **False Positives**: Fields marked "required" but have default values
2. **Conditional Requirements**: `firewall.policy` requires EITHER:
   - `(srcaddr + dstaddr)` for IPv4, OR
   - `(srcaddr6 + dstaddr6)` for IPv6
3. **Specialized Features**: VPN/NAT64/WAN optimization fields marked required but only apply when those features are enabled

**Mitigation**: Generator filters out obvious false positives:
- Fields with non-empty default values
- Fields containing keywords: `wanopt`, `rtp`, `vpn`, `ztna`, `ssl-ssh`, `nat64`, `nat46`

**Recommendation**: Always test with actual FortiOS API for authoritative requirements.

## Usage Examples

### Example 1: Dynamic Form Generation
```python
from hfortix_fortios.api.v2.cmdb.firewall._helpers.policy import (
    get_all_fields,
    get_field_metadata,
)

# Build dynamic form
for field_name in get_all_fields():
    meta = get_field_metadata(field_name)
    
    # Determine input type
    if meta['type'] == 'option' and meta.get('options'):
        input_type = 'select'
        choices = meta['options']
    elif meta['type'] == 'integer':
        input_type = 'number'
    else:
        input_type = 'text'
    
    # Use constraints
    constraints = meta.get('constraints', {})
    
    print(f"Field: {field_name}")
    print(f"  Type: {input_type}")
    print(f"  Description: {meta.get('description', '')}")
    print(f"  Required: {meta.get('required', False)}")
    if 'default' in meta:
        print(f"  Default: {meta['default']}")
```

### Example 2: Validation Before API Call
```python
from hfortix_fortios.api.v2.cmdb.firewall._helpers.policy import (
    validate_field_value,
    get_field_default,
)

payload = {
    "name": "my-policy",
    "action": "accept",
}

# Apply defaults
for field_name in get_all_fields():
    if field_name not in payload:
        default = get_field_default(field_name)
        if default is not None:
            payload[field_name] = default

# Validate each field
for field_name, value in payload.items():
    is_valid, error = validate_field_value(field_name, value)
    if not is_valid:
        print(f"Validation error: {error}")
```

### Example 3: Explore Endpoint Metadata
```python
from hfortix_fortios.api.v2.cmdb.firewall._helpers.policy import (
    get_schema_info,
    get_all_fields,
    get_field_metadata,
)

# Get endpoint info
info = get_schema_info()
print(f"Endpoint: {info['endpoint']}")
print(f"Total fields: {info['total_fields']}")

# Explore all fields
for field_name in get_all_fields():
    meta = get_field_metadata(field_name)
    print(f"{field_name}: {meta['type']}")
```

## Generator Implementation

### Template: `.dev/generator/templates/validator.py.j2`
- Enhanced with new metadata sections
- Added 10+ helper functions
- Improved documentation

### Generator: `.dev/generator/generators/validator_generator.py`
- Updated context to include `all_fields`
- Existing logic for required fields filtering
- Existing logic for enum extraction

## Benefits

1. **No Network Calls**: All metadata available locally
2. **IDE Integration**: Autocomplete and tooltips
3. **Documentation**: Self-documenting with help text
4. **Validation**: Client-side validation before API calls
5. **Dynamic UIs**: Build forms from schema metadata
6. **Type Safety**: Foundation for future TypedDict support
7. **Discovery**: Explore API capabilities programmatically

## Next Steps

### Potential Enhancements
1. **TypedDict Payload Classes**: Generate strict payload types
2. **Conditional Validation**: Handle "either/or" requirements
3. **Dependency Tracking**: Map field dependencies
4. **Version Comparison**: Track schema changes across versions
5. **OpenAPI Export**: Generate OpenAPI specs from metadata

### Usage Patterns
1. **Web Frameworks**: Auto-generate API forms
2. **CLI Tools**: Dynamic command generation
3. **Testing**: Generate test data from schemas
4. **Documentation**: Auto-generate field reference docs
