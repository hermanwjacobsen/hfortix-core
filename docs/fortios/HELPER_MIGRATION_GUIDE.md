# Helper Module Migration Guide

## Overview

In version 0.4.2 (January 2, 2026), we centralized all helper functions to improve code organization and eliminate duplication.

## What Changed

### Old Structure (Deprecated)
```text
hfortix_fortios/
  api/
    _helpers/
      helpers.py          # Generic helpers
  firewall/
    _helpers.py           # Firewall-specific helpers
```

### New Structure (Current)
```text
hfortix_fortios/
  _helpers/
    __init__.py          # Central re-export point
    builders.py          # build_cmdb_payload, build_cmdb_payload_normalized
    normalizers.py       # normalize_to_name_list, normalize_member_list
    validators.py        # ALL validators (generic + domain-specific)
    converters.py        # convert_boolean_to_str, filter_empty_values
    response.py          # get_name, get_mkey, is_success, get_results
```

## Migration Steps

### 1. Update Imports

**Before:**
```python
from hfortix_fortios.api._helpers import (
    build_cmdb_payload,
    validate_color,
    normalize_to_name_list,
)

from hfortix_fortios.firewall._helpers import (
    validate_policy_id,
    validate_schedule_name,
)
```

**After:**
```python
from hfortix_fortios._helpers import (
    build_cmdb_payload,
    validate_color,
    normalize_to_name_list,
    validate_policy_id,
    validate_schedule_name,
)
```

### 2. Common Import Patterns

#### Firewall Wrappers
```python
# OLD
from hfortix_fortios.api._helpers import build_cmdb_payload_normalized
from hfortix_fortios.firewall._helpers import validate_policy_id

# NEW
from hfortix_fortios._helpers import (
    build_cmdb_payload_normalized,
    validate_policy_id,
)
```

#### API Endpoints
```python
# OLD
from hfortix_fortios.api._helpers import build_cmdb_payload

# NEW
from hfortix_fortios._helpers import build_cmdb_payload
```

#### Response Helpers
```python
# OLD
from hfortix_fortios.api._helpers import get_mkey, is_success, get_results

# NEW
from hfortix_fortios._helpers import get_mkey, is_success, get_results
```

## Available Helper Functions

### Payload Builders (`_helpers.builders`)
- `build_cmdb_payload(**params)` - Build API payload without normalization
- `build_cmdb_payload_normalized(**params)` - Build API payload with list normalization

### Normalizers (`_helpers.normalizers`)
- `normalize_to_name_list(value)` - Convert to `[{'name': '...'}, ...]` format
- `normalize_member_list(value)` - Normalize member lists

### Validators (`_helpers.validators`)

**Generic Validators:**
- `validate_required_fields(payload, required_fields)`
- `validate_color(color)`
- `validate_status(status)`
- `validate_enable_disable(value, field_name)`
- `validate_string_length(value, max_length, field_name)`
- `validate_integer_range(value, min_value, max_value, field_name)`

**Network Validators:**
- `validate_mac_address(mac, allow_wildcard=True)`
- `validate_ip_address(ip, allow_wildcard=True)`
- `validate_ipv6_address(ip, allow_wildcard=True)`
- `validate_ip_network(network, version=4)`
- `validate_port_number(port, field_name="port")`

**Firewall Validators:**
- `validate_policy_id(policy_id, operation="operation")`
- `validate_address_pairs(srcaddr, dstaddr, srcaddr6, dstaddr6)`
- `validate_seq_num(seq_num, operation="operation")`

**Schedule Validators:**
- `validate_schedule_name(name, operation="operation")`
- `validate_time_format(time_str, field_name="time")`
- `validate_day_names(day_str)`

**SSH/SSL Validators:**
- `validate_ssh_host_key_type(key_type)`
- `validate_ssh_host_key_status(status)`
- `validate_ssh_host_key_nid(nid)`
- `validate_ssh_host_key_usage(usage)`
- `validate_ssh_source(source)`
- `validate_ssl_dh_bits(dh_bits)`
- `validate_ssl_cipher_action(action)`

### Converters (`_helpers.converters`)
- `convert_boolean_to_str(value)` - Convert bool to 'enable'/'disable'
- `filter_empty_values(payload)` - Remove None and empty values

### Response Helpers (`_helpers.response`)
- `get_name(response)` - Extract object name from response
- `get_mkey(response)` - Alias for get_name (backward compatibility)
- `get_results(response)` - Extract results array from response
- `is_success(response)` - Check if operation succeeded

## Automated Migration

If you have many files to update, you can use this find/replace pattern:

```bash
# Find all imports from old locations
find . -name "*.py" -exec grep -l "from hfortix_fortios\\.\\(api\\|firewall\\)\\._helpers" {} \;

# Replace with sed (review changes first!)
find . -name "*.py" -exec sed -i 's/from hfortix_fortios\.api\._helpers/from hfortix_fortios._helpers/g' {} \;
find . -name "*.py" -exec sed -i 's/from hfortix_fortios\.firewall\._helpers/from hfortix_fortios._helpers/g' {} \;
```

## Backward Compatibility

**BREAKING CHANGE**: The old `api._helpers` and `firewall._helpers` modules have been completely removed in v0.4.2.

If you need to maintain compatibility with older versions, you can use a try/except:

```python
try:
    # Try new location first (v0.4.2+)
    from hfortix_fortios._helpers import validate_color
except ImportError:
    # Fall back to old location (v0.4.1 and earlier)
    from hfortix_fortios.api._helpers import validate_color
```

However, we recommend updating to the new import style immediately.

## Testing After Migration

After updating your imports, run your tests to verify everything works:

```bash
# Run your test suite
pytest

# Or test specific imports
python -c "from hfortix_fortios._helpers import validate_color, build_cmdb_payload"
```

## Benefits of Centralization

1. **Single Source of Truth**: All helpers in one place
2. **Consistent Imports**: Same pattern across entire codebase
3. **Better Organization**: Logical grouping by function (builders, validators, etc.)
4. **No Duplication**: Eliminates scattered helper files
5. **Scalability**: Easy to add new helpers and find existing ones
6. **Maintainability**: Changes in one place affect entire codebase

## Questions?

If you encounter issues during migration:

1. Check that you're importing from `hfortix_fortios._helpers` (note the underscore)
2. Verify you've updated all old imports
3. Clear Python cache: `find . -type d -name __pycache__ -exec rm -rf {} +`
4. Reinstall the package: `pip install --upgrade --force-reinstall hfortix-fortios`

## Version History

- **v0.4.2** (2026-01-02): Centralized helpers to `_helpers/`
- **v0.4.1** and earlier: Helpers scattered across `api._helpers/` and `firewall._helpers/`
