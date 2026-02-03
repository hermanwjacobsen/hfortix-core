# Validator Metadata API - Quick Reference

## Import Examples

```python
# Basic metadata access
from hfortix_fortios.api.v2.cmdb.firewall._helpers.policy import (
    FIELD_TYPES,           # All field types
    FIELD_DESCRIPTIONS,    # All field descriptions
    FIELD_CONSTRAINTS,     # All field constraints
    FIELDS_WITH_DEFAULTS,  # All fields with defaults
    REQUIRED_FIELDS,       # Required fields (filtered)
    NESTED_SCHEMAS,        # Nested table schemas
    SCHEMA_INFO,           # Endpoint metadata
)

# Helper functions
from hfortix_fortios.api.v2.cmdb.firewall._helpers.policy import (
    get_field_type,        # Get type for one field
    get_field_description, # Get description for one field
    get_field_constraints, # Get constraints for one field
    get_field_default,     # Get default for one field
    get_field_options,     # Get enum options for one field
    get_field_metadata,    # Get all metadata for one field
    get_nested_schema,     # Get nested schema for table field
    get_all_fields,        # Get list of all field names
    get_schema_info,       # Get endpoint metadata
    validate_field_value,  # Validate single field value
)

# Validation functions (existing)
from hfortix_fortios.api.v2.cmdb.firewall._helpers.policy import (
    validate_firewall_policy_get,   # Validate GET request
    validate_firewall_policy_post,  # Validate POST request
    validate_firewall_policy_put,   # Validate PUT request
    validate_required_fields,        # Validate required fields
)
```

## Function Reference

### Metadata Access

| Function | Returns | Description |
|----------|---------|-------------|
| `get_field_type(name)` | `str \| None` | Get field type (e.g., "string", "integer", "option") |
| `get_field_description(name)` | `str \| None` | Get field help text from FortiOS API |
| `get_field_constraints(name)` | `dict \| None` | Get min/max values, string lengths |
| `get_field_default(name)` | `Any \| None` | Get default value for field |
| `get_field_options(name)` | `list[str] \| None` | Get enum values for option fields |
| `get_field_metadata(name)` | `dict \| None` | Get all metadata (type, desc, constraints, etc.) |
| `get_nested_schema(name)` | `dict \| None` | Get schema for nested table fields |
| `get_all_fields()` | `list[str]` | Get all field names in schema |
| `get_schema_info()` | `dict` | Get endpoint info (path, mkey, counts) |
| `validate_field_value(name, val)` | `tuple[bool, str \| None]` | Validate single field against constraints |

### Validation Functions

| Function | Returns | Description |
|----------|---------|-------------|
| `validate_{endpoint}_get(**params)` | `tuple[bool, str \| None]` | Validate GET request |
| `validate_{endpoint}_post(payload, **params)` | `tuple[bool, str \| None]` | Validate POST request |
| `validate_{endpoint}_put(payload, **params)` | `tuple[bool, str \| None]` | Validate PUT request |
| `validate_required_fields(payload)` | `tuple[bool, str \| None]` | Check required fields only |

## Constants Reference

### FIELD_TYPES
```python
FIELD_TYPES: dict[str, str]
# Example:
# {
#   "name": "string",
#   "policyid": "integer",
#   "action": "option",
#   "srcaddr": "var-string",
#   ...
# }
```

### FIELD_DESCRIPTIONS
```python
FIELD_DESCRIPTIONS: dict[str, str]
# Example:
# {
#   "name": "Policy name.",
#   "action": "Policy action (accept/deny/ipsec).",
#   ...
# }
```

### FIELD_CONSTRAINTS
```python
FIELD_CONSTRAINTS: dict[str, dict[str, Any]]
# Example:
# {
#   "policyid": {"type": "integer", "min": 0, "max": 4294967294},
#   "name": {"type": "string", "max_length": 79},
#   ...
# }
```

### FIELDS_WITH_DEFAULTS
```python
FIELDS_WITH_DEFAULTS: dict[str, Any]
# Example:
# {
#   "status": "enable",
#   "action": "deny",
#   "logtraffic": "utm",
#   ...
# }
```

### REQUIRED_FIELDS
```python
REQUIRED_FIELDS: list[str]
# Example:
# [
#   "name",
#   "srcintf",
#   "dstintf",
# ]
```

### NESTED_SCHEMAS
```python
NESTED_SCHEMAS: dict[str, dict[str, dict[str, Any]]]
# Example (for table field "members"):
# {
#   "members": {
#     "name": {
#       "type": "string",
#       "help": "Member name",
#       "required": True
#     }
#   }
# }
```

### SCHEMA_INFO
```python
SCHEMA_INFO: dict[str, Any]
# Example:
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
```

### Enum Constants
```python
VALID_BODY_{FIELD_NAME}: list[str]
# Examples:
VALID_BODY_ACTION = ["accept", "deny", "ipsec"]
VALID_BODY_STATUS = ["enable", "disable"]
VALID_BODY_LOGTRAFFIC = ["all", "utm", "disable"]
```

## Common Patterns

### Pattern 1: Get Complete Field Info
```python
meta = get_field_metadata("action")
if meta:
    print(f"Type: {meta['type']}")
    print(f"Description: {meta.get('description', 'N/A')}")
    print(f"Required: {meta.get('required', False)}")
    print(f"Default: {meta.get('default', 'N/A')}")
    if 'options' in meta:
        print(f"Options: {', '.join(meta['options'])}")
```

### Pattern 2: Validate Before API Call
```python
payload = {"name": "test", "action": "accept"}

# Validate each field
errors = []
for field_name, value in payload.items():
    is_valid, error = validate_field_value(field_name, value)
    if not is_valid:
        errors.append(error)

if errors:
    print("Validation errors:")
    for error in errors:
        print(f"  - {error}")
```

### Pattern 3: Build Dynamic Form
```python
for field_name in get_all_fields():
    meta = get_field_metadata(field_name)
    
    form_field = {
        "name": field_name,
        "label": field_name.replace("-", " ").title(),
        "type": meta['type'],
        "description": meta.get('description', ''),
        "required": meta.get('required', False),
    }
    
    if 'default' in meta:
        form_field['default'] = meta['default']
    
    if 'options' in meta:
        form_field['choices'] = meta['options']
    
    if 'constraints' in meta:
        form_field.update(meta['constraints'])
    
    print(form_field)
```

### Pattern 4: Apply Defaults
```python
payload = {"name": "test"}

# Apply all defaults
for field_name in get_all_fields():
    if field_name not in payload:
        default = get_field_default(field_name)
        if default is not None:
            payload[field_name] = default
```

### Pattern 5: Schema Discovery
```python
# Get complete schema
schema = get_runtime_schema()

print(f"Endpoint: {schema['endpoint']}")
print(f"Category: {schema['category']}")
print(f"Total fields: {len(schema['fields'])}")
print(f"Required: {len(schema['required_fields'])}")
print(f"With defaults: {len(schema['fields_with_defaults'])}")

# Export fields
for field_name, field_meta in schema['fields'].items():
    print(f"\n{field_name}:")
    print(f"  Type: {field_meta['type']}")
    print(f"  Description: {field_meta.get('description', 'N/A')}")
```

### Pattern 6: Nested Schema Handling
```python
# Check if field has nested schema
nested = get_nested_schema("service")
if nested:
    print("Service field contains nested fields:")
    for child_name, child_meta in nested.items():
        print(f"  {child_name}: {child_meta['type']}")
        if 'help' in child_meta:
            print(f"    Help: {child_meta['help']}")
```

## Migration from Old Approach

### Before (No Metadata)
```python
# Had to hardcode or guess
payload = {
    "name": "test",
    "action": "accept",  # Is this valid?
    "status": "enable",  # What's the default?
}
# No way to know field types, descriptions, or constraints
```

### After (With Metadata)
```python
# Discover valid options
action_options = get_field_options("action")
print(f"Valid actions: {action_options}")  # ["accept", "deny", "ipsec"]

# Get default values
status_default = get_field_default("status")
print(f"Default status: {status_default}")  # "enable"

# Get field type and description
action_type = get_field_type("action")
action_desc = get_field_description("action")
print(f"Action is {action_type}: {action_desc}")
# "Action is option: Policy action (accept/deny/ipsec)."

# Validate before sending
is_valid, error = validate_field_value("action", "accept")
if not is_valid:
    print(f"Invalid: {error}")
```

## Type Hints

All helper functions include proper type hints:

```python
def get_field_type(field_name: str) -> str | None: ...
def get_field_description(field_name: str) -> str | None: ...
def get_field_constraints(field_name: str) -> dict[str, Any] | None: ...
def get_field_default(field_name: str) -> Any | None: ...
def get_field_options(field_name: str) -> list[str] | None: ...
def get_field_metadata(field_name: str) -> dict[str, Any] | None: ...
def get_nested_schema(field_name: str) -> dict[str, Any] | None: ...
def get_all_fields() -> list[str]: ...
def get_schema_info() -> dict[str, Any]: ...
def get_runtime_schema() -> dict[str, Any]: ...
def validate_field_value(field_name: str, value: Any) -> tuple[bool, str | None]: ...
```

## Coverage

- **909 validators** across all FortiOS categories
- **100% coverage** for type information
- **100% coverage** for field descriptions  
- **100% coverage** for default values
- **100% coverage** for nested schemas
- **2,071 enum constants** for option validation
