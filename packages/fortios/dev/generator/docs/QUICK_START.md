# Quick Start: Using Validator Metadata

## Basic Usage

### Get Field Information
```python
from hfortix_fortios.api.v2.cmdb.firewall._helpers.policy import get_field_metadata

# Get everything about a field
meta = get_field_metadata("action")
print(f"Type: {meta['type']}")
print(f"Description: {meta['description']}")
print(f"Options: {meta['options']}")
print(f"Default: {meta['default']}")
print(f"Required: {meta['required']}")
```

### Validate Before API Call
```python
from hfortix_fortios.api.v2.cmdb.firewall._helpers.policy import validate_field_value

# Check if value is valid
is_valid, error = validate_field_value("action", "accept")
if not is_valid:
    print(f"Error: {error}")
```

### Build Payload with Defaults
```python
from hfortix_fortios.api.v2.cmdb.firewall._helpers.policy import (
    FIELDS_WITH_DEFAULTS,
    REQUIRED_FIELDS,
)

# Start with defaults
payload = FIELDS_WITH_DEFAULTS.copy()

# Add required fields
for field in REQUIRED_FIELDS:
    if field not in payload:
        print(f"Need to provide: {field}")

payload['name'] = 'my-policy'
payload['srcintf'] = 'port1'
payload['dstintf'] = 'port2'
```

### Explore All Fields
```python
from hfortix_fortios.api.v2.cmdb.firewall._helpers.policy import (
    get_all_fields,
    get_field_type,
    get_field_description,
)

# List all available fields
for field_name in get_all_fields():
    field_type = get_field_type(field_name)
    description = get_field_description(field_name)
    print(f"{field_name} ({field_type}): {description}")
```

### Get Enum Options
```python
from hfortix_fortios.api.v2.cmdb.firewall._helpers.policy import get_field_options

# What are valid values for this field?
options = get_field_options("logtraffic")
print(f"Valid options: {options}")
# ['all', 'utm', 'disable']
```

## Common Patterns

### Pattern: Dynamic Form Generation
```python
from hfortix_fortios.api.v2.cmdb.firewall._helpers.policy import (
    get_all_fields,
    get_field_metadata,
)

for field_name in get_all_fields():
    meta = get_field_metadata(field_name)
    
    # Determine input type
    if meta['type'] == 'option' and 'options' in meta:
        input_type = 'select'
        choices = meta['options']
    elif meta['type'] == 'integer':
        input_type = 'number'
        constraints = meta.get('constraints', {})
        min_val = constraints.get('min')
        max_val = constraints.get('max')
    else:
        input_type = 'text'
        max_length = meta.get('constraints', {}).get('max_length')
    
    # Create form field...
```

### Pattern: Validation Before Submit
```python
from hfortix_fortios.api.v2.cmdb.firewall._helpers.policy import validate_field_value

payload = {
    "name": "test-policy",
    "action": "accept",
    "srcintf": "port1",
    "dstintf": "port2",
}

# Validate all fields
errors = []
for field_name, value in payload.items():
    is_valid, error = validate_field_value(field_name, value)
    if not is_valid:
        errors.append(f"{field_name}: {error}")

if errors:
    print("Validation errors:")
    for error in errors:
        print(f"  - {error}")
else:
    # Safe to submit
    result = fgt.api.cmdb.firewall.policy.post(payload)
```

### Pattern: Discover Required Fields
```python
from hfortix_fortios.api.v2.cmdb.firewall._helpers.policy import (
    REQUIRED_FIELDS,
    get_field_description,
)

print("Required fields:")
for field in REQUIRED_FIELDS:
    desc = get_field_description(field)
    print(f"  - {field}: {desc}")
```

### Pattern: Get Field Constraints
```python
from hfortix_fortios.api.v2.cmdb.firewall._helpers.policy import get_field_constraints

# Check integer ranges
port_constraints = get_field_constraints("dstport")
if port_constraints:
    print(f"Port range: {port_constraints['min']} - {port_constraints['max']}")

# Check string lengths
name_constraints = get_field_constraints("name")
if name_constraints:
    print(f"Name max length: {name_constraints['max_length']}")
```

### Pattern: Handle Nested Tables
```python
from hfortix_fortios.api.v2.cmdb.firewall._helpers.addrgrp import get_nested_schema

# For fields that are tables/lists
members_schema = get_nested_schema("member")
if members_schema:
    print("Member table has these fields:")
    for child_field, child_meta in members_schema.items():
        print(f"  {child_field}: {child_meta['type']}")
```

## All Available Functions

```python
# Individual field access
get_field_type(field_name)         # Get type ("string", "integer", "option", etc.)
get_field_description(field_name)  # Get help text
get_field_default(field_name)      # Get default value
get_field_options(field_name)      # Get enum options
get_field_constraints(field_name)  # Get min/max/length constraints
get_field_metadata(field_name)     # Get all metadata at once

# Schema access
get_all_fields()                   # List all field names
get_nested_schema(field_name)      # Get schema for table fields
get_schema_info()                  # Get endpoint metadata

# Validation
validate_field_value(field_name, value)  # Validate single field
```

## All Available Constants

```python
# Lists
REQUIRED_FIELDS                    # List of required field names
VALID_BODY_{FIELD_NAME}            # Enum constants (e.g., VALID_BODY_ACTION)

# Dicts
FIELDS_WITH_DEFAULTS               # Field name -> default value
FIELD_TYPES                        # Field name -> type
FIELD_DESCRIPTIONS                 # Field name -> description
FIELD_CONSTRAINTS                  # Field name -> constraints dict
NESTED_SCHEMAS                     # Field name -> nested schema dict
SCHEMA_INFO                        # Endpoint metadata dict
```

## Import Patterns

### Import Only What You Need
```python
from hfortix_fortios.api.v2.cmdb.firewall._helpers.policy import (
    get_field_metadata,
    validate_field_value,
)
```

### Import Constants
```python
from hfortix_fortios.api.v2.cmdb.firewall._helpers.policy import (
    REQUIRED_FIELDS,
    FIELDS_WITH_DEFAULTS,
    FIELD_TYPES,
)
```

### Import Validation
```python
from hfortix_fortios.api.v2.cmdb.firewall._helpers.policy import (
    validate_firewall_policy_post,
    validate_firewall_policy_put,
    validate_field_value,
)
```

## Where to Find Validators

All validators are in `_helpers` subdirectories:

```
packages/fortios/hfortix_fortios/api/v2/
├── cmdb/
│   ├── firewall/
│   │   └── _helpers/
│   │       ├── policy.py
│   │       ├── address.py
│   │       └── ...
│   ├── system/
│   │   └── _helpers/
│   │       ├── interface.py
│   │       └── ...
│   └── ...
├── monitor/
│   └── ...
└── service/
    └── ...
```

Pattern: `hfortix_fortios.api.v2.{category}.{path}._helpers.{endpoint}`

Examples:
- `hfortix_fortios.api.v2.cmdb.firewall._helpers.policy`
- `hfortix_fortios.api.v2.cmdb.system._helpers.interface`
- `hfortix_fortios.api.v2.cmdb.firewall._helpers.address`
