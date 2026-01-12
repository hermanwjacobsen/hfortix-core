# HFortix FortiOS Test Documentation

Comprehensive test suite for `hfortix_fortios` and `hfortix_core` Python packages.

## Overview

| Metric | Count |
|--------|-------|
| **Total Test Files** | 22 |
| **Total Test Functions** | 366 |
| **Modules Tested** | 25+ |
| **Functions/Classes Covered** | 150+ |

## Test Files Summary

### hfortix_fortios - Validators (`_helpers/validators.py`)

| Test File | Functions Tested | Test Count |
|-----------|-----------------|------------|
| `test_generic_validators.py` | `validate_required_fields`, `validate_color`, `validate_status`, `validate_enable_disable`, `validate_string_length`, `validate_integer_range` | 6 |
| `test_network_validators.py` | `validate_mac_address`, `validate_ip_address`, `validate_ipv6_address`, `validate_ip_network`, `validate_port_number` | 5 |
| `test_firewall_validators.py` | `validate_policy_id`, `validate_address_pairs`, `validate_seq_num` | 3 |
| `test_schedule_validators.py` | `validate_schedule_name`, `validate_time_format`, `validate_day_names` | 3 |
| `test_ssh_ssl_validators.py` | `validate_ssh_host_key_type`, `validate_ssh_host_key_status`, `validate_ssh_host_key_nid`, `validate_ssh_host_key_usage`, `validate_ssh_source`, `validate_ssl_dh_bits`, `validate_ssl_cipher_action` | 7 |

### hfortix_fortios - Validation (`_helpers/validation.py`)

| Test File | Functions Tested | Test Count |
|-----------|-----------------|------------|
| `test_endpoint_validators.py` | `validate_required_fields`, `validate_enum_field`, `validate_query_parameter`, `validate_multiple_enums`, `validate_multiple_query_params` | 5 |

### hfortix_fortios - Helper Modules

| Test File | Module | Functions Tested | Test Count |
|-----------|--------|-----------------|------------|
| `test_normalizers.py` | `_helpers/normalizers.py` | `normalize_to_name_list`, `normalize_member_list`, `normalize_table_field` | 26 |
| `test_converters.py` | `_helpers/converters.py` | `convert_boolean_to_str`, `filter_empty_values` | 17 |
| `test_builders.py` | `_helpers/builders.py` | `build_cmdb_payload`, `build_cmdb_payload_normalized`, `build_api_payload` | 24 |
| `test_response_helpers.py` | `_helpers/response.py` | `get_name`, `get_mkey`, `get_results`, `is_success` | 23 |
| `test_metadata.py` | `_helpers/metadata.py` | `get_field_description`, `get_field_type`, `get_field_constraints`, `get_field_default`, `get_field_options`, `get_nested_schema`, `get_all_fields`, `get_field_metadata`, `validate_field_value` | 36 |

### hfortix_fortios - Top-Level Modules

| Test File | Module | Functions/Classes Tested | Test Count |
|-----------|--------|-------------------------|------------|
| `test_formatting.py` | `formatting.py` | `to_json`, `to_csv`, `to_dict`, `to_multiline`, `to_list`, `to_quoted`, `to_table`, `to_yaml`, `to_xml`, `to_key_value`, `to_markdown_table`, `to_dictlist`, `to_listdict` | 69 |
| `test_models.py` | `models.py` | `FortiObject` class (all methods), `process_response` | 31 |

### hfortix_core - Utility Modules

| Test File | Module | Functions/Classes Tested | Test Count |
|-----------|--------|-------------------------|------------|
| `test_cache.py` | `cache.py` | `TTLCache` class, `CacheEntry` class | 16 |
| `test_deprecation.py` | `deprecation.py` | `warn_deprecated_field`, `check_deprecated_fields`, `DeprecationWarning` | 12 |
| `test_exceptions.py` | `exceptions.py` | `get_error_description`, `get_http_status_description`, `raise_for_status`, `is_retryable_error`, `get_retry_delay`, exception hierarchy | 31 |

---

## Detailed Test Coverage

### 1. Generic Validators (`test_generic_validators.py`)

Tests basic validation functions used across all FortiOS objects.

```python
# Functions tested:
validate_required_fields(payload, required_fields)  # Check required fields present
validate_color(color)                               # Color index 0-32
validate_status(status)                             # 'enable' or 'disable'
validate_enable_disable(value, field_name)          # Same with field context
validate_string_length(value, max_length, field)    # String length limits
validate_integer_range(value, min, max, field)      # Integer range validation
```

### 2. Network Validators (`test_network_validators.py`)

Tests network-related validation functions.

```python
# Functions tested:
validate_mac_address(mac, allow_wildcard)     # MAC format xx:xx:xx:xx:xx:xx
validate_ip_address(ip, allow_wildcard)       # IPv4 address validation
validate_ipv6_address(ip, allow_wildcard)     # IPv6 address validation
validate_ip_network(network, version)         # CIDR notation validation
validate_port_number(port, field_name)        # Port range 0-4294967295
```

### 3. Firewall Validators (`test_firewall_validators.py`)

Tests firewall policy-specific validators.

```python
# Functions tested:
validate_policy_id(policy_id, operation)      # Policy ID 0-4294967295
validate_address_pairs(srcaddr, dstaddr, srcaddr6, dstaddr6)  # Address pair completeness
validate_seq_num(seq_num, operation)          # Sequence number validation
```

### 4. Schedule Validators (`test_schedule_validators.py`)

Tests schedule object validators.

```python
# Functions tested:
validate_schedule_name(name, operation)       # Max 31 characters
validate_time_format(time_str, field_name)    # HH:MM format
validate_day_names(day_str)                   # Day name validation
```

### 5. SSH/SSL Validators (`test_ssh_ssl_validators.py`)

Tests SSH/SSL proxy configuration validators.

```python
# Functions tested:
validate_ssh_host_key_type(key_type)     # RSA, DSA, ECDSA, ED25519, etc.
validate_ssh_host_key_status(status)     # 'trusted' or 'revoked'
validate_ssh_host_key_nid(nid)           # '256', '384', '521'
validate_ssh_host_key_usage(usage)       # 'transparent-proxy' or 'access-proxy'
validate_ssh_source(source)              # 'built-in' or 'user'
validate_ssl_dh_bits(dh_bits)            # '768', '1024', '1536', '2048'
validate_ssl_cipher_action(action)       # 'bypass' or 'drop'
```

### 6. Endpoint Validators (`test_endpoint_validators.py`)

Tests validation functions for API endpoint parameters.

```python
# Functions tested:
validate_required_fields(payload, required, descriptions)  # With descriptions
validate_enum_field(field, value, valid_values)           # Enum value check
validate_query_parameter(param, value, valid_values)      # Query param check
validate_multiple_enums(payload, enum_fields)             # Batch enum validation
validate_multiple_query_params(params, valid_params)      # Batch param validation
```

### 7. Normalizers (`test_normalizers.py`)

Tests data normalization for FortiOS API payloads.

```python
# Functions tested:
normalize_to_name_list(value)                    # Convert to [{"name": x}] format
normalize_member_list(value)                     # Normalize member fields
normalize_table_field(value, mkey, required)     # Normalize table/list fields
```

### 8. Converters (`test_converters.py`)

Tests data type conversion utilities.

```python
# Functions tested:
convert_boolean_to_str(value)    # True -> 'enable', False -> 'disable'
filter_empty_values(payload)     # Remove None, [], {} but keep 0, '', False
```

### 9. Builders (`test_builders.py`)

Tests payload builder functions.

```python
# Functions tested:
build_cmdb_payload(**params)                    # Build CMDB API payload
build_cmdb_payload_normalized(**params)         # With field normalization
build_api_payload(**params)                     # High-level payload builder
```

### 10. Response Helpers (`test_response_helpers.py`)

Tests API response processing utilities.

```python
# Functions tested:
get_name(response)       # Extract object name/mkey
get_mkey(response)       # Get primary key value
get_results(response)    # Extract results array
is_success(response)     # Check if response successful
```

### 11. Metadata (`test_metadata.py`)

Tests schema metadata introspection functions.

```python
# Functions tested:
get_field_description(descriptions, field)      # Get field help text
get_field_type(types, field)                    # Get field data type
get_field_constraints(constraints, field)       # Get validation constraints
get_field_default(defaults, field)              # Get default value
get_field_options(globals_dict, field)          # Get enum options
get_nested_schema(schemas, field)               # Get nested table schema
get_all_fields(types)                           # List all field names
get_field_metadata(...)                         # Complete field metadata
validate_field_value(...)                       # Validate against schema
```

### 12. Formatting (`test_formatting.py`)

Tests data output formatting utilities.

```python
# Functions tested:
to_json(data, indent)           # JSON string output
to_csv(data, separator)         # Comma-separated values
to_dict(data)                   # Dictionary conversion
to_multiline(data, separator)   # Newline-separated output
to_list(data, delimiter)        # List conversion
to_quoted(data, quote, sep)     # Quoted string output
to_table(data, headers, delim)  # Table format
to_yaml(data, indent)           # YAML-like output
to_xml(data, root, indent)      # XML format
to_key_value(data, sep, delim)  # key=value pairs
to_markdown_table(data)         # Markdown table
to_dictlist(data)               # Columnar to row format
to_listdict(data)               # Row to columnar format
```

### 13. Models (`test_models.py`)

Tests FortiObject wrapper class and response processing.

```python
# Classes/Functions tested:
FortiObject(data)               # Wrapper for API response objects
  .name, .policyid, etc.        # Attribute access
  .__contains__, .__getitem__   # Dict-like interface
  .keys(), .values(), .items()  # Iteration methods
  .get(key), .get_full(key)     # Data access methods
  .to_dict(), .json             # Data export
  .__repr__, .__str__           # String representations

process_response(result, mode, unwrap_single)  # Response post-processing
```

### 14. Cache (`test_cache.py`)

Tests TTL-based caching utilities from hfortix_core.

```python
# Classes tested:
CacheEntry(value, ttl_seconds)  # Single cache entry
  .value                        # Cached value
  .expiry                       # Expiration timestamp
  .is_expired()                 # Check if expired

TTLCache(default_ttl)           # TTL cache implementation
  .get(key)                     # Get cached value
  .set(key, value, ttl)         # Store value
  .invalidate(key)              # Remove entry
  .clear()                      # Clear all entries
  .cleanup()                    # Remove expired entries
  .__len__, .__contains__       # Length and membership
```

### 15. Deprecation (`test_deprecation.py`)

Tests deprecation warning utilities from hfortix_core.

```python
# Functions tested:
warn_deprecated_field(field, endpoint, reason, alternative, removal_version)
check_deprecated_fields(payload, deprecated_fields, endpoint)

# Classes tested:
DeprecationWarning              # Custom warning class
```

### 16. Exceptions (`test_exceptions.py`)

Tests exception hierarchy and helper functions from hfortix_core.

```python
# Functions tested:
get_error_description(error_code)       # FortiOS error code lookup
get_http_status_description(status)     # HTTP status description
raise_for_status(response, endpoint, method, params)  # Auto-raise exceptions
is_retryable_error(error)               # Check if error is retryable
get_retry_delay(error, attempt, base, max)  # Calculate retry delay

# Exception hierarchy tested:
FortinetError (base)
├── APIError
│   ├── RetryableError
│   │   ├── RateLimitError
│   │   ├── ServerError
│   │   ├── ServiceUnavailableError
│   │   ├── CircuitBreakerOpenError
│   │   └── TimeoutError
│   └── NonRetryableError
│       ├── BadRequestError
│       ├── ResourceNotFoundError
│       ├── MethodNotAllowedError
│       ├── DuplicateEntryError
│       ├── EntryInUseError
│       ├── InvalidValueError
│       └── PermissionDeniedError
├── AuthenticationError
└── AuthorizationError
```

---

## Running Tests

Tests are maintained in a separate repository. Each test file includes a `run_all_tests()` function that prints detailed results.

### Run All Tests

```bash
cd /path/to/test/pytest/validators
for f in test_*.py; do python "$f"; done
```

### Run Individual Test File

```bash
python test_validators.py
python test_formatting.py
python test_models.py
```

### Example Output

```bash
python test_cache.py

# Output:
# ============================================================
# CACHE TESTS
# ============================================================
#
# ✅ CacheEntry - creation
# ✅ CacheEntry - not expired
# ✅ CacheEntry - expired
# ✅ TTLCache - creation
# ...
# ============================================================
# ALL CACHE TESTS PASSED!
# ============================================================
```

---

## Test File Structure

```
pytest/validators/
├── README.md
├── test_builders.py
├── test_cache.py
├── test_converters.py
├── test_deprecation.py
├── test_endpoint_validators.py
├── test_exceptions.py
├── test_firewall_validators.py
├── test_formatting.py
├── test_generic_validators.py
├── test_metadata.py
├── test_models.py
├── test_network_validators.py
├── test_normalizers.py
├── test_response_helpers.py
├── test_schedule_validators.py
└── test_ssh_ssl_validators.py
```

---

## Modules NOT Tested (and Why)

| Module | Reason |
|--------|--------|
| `types.py` | TypedDict definitions only - no runtime code |
| `_protocols.py` | Protocol definitions for type hints only |
| `help.py` | Requires live endpoint class instances |
| `client.py` | Requires FortiGate API connection |
| `performance_test.py` | Requires live API connection |
| `metadata_mixin.py` | Mixin class - requires endpoint classes |

---

## Dependencies

- Python 3.12+
- `hfortix_fortios` >= 0.5.50
- `hfortix_core` >= 0.5.50

---

## Last Updated

January 12, 2026
