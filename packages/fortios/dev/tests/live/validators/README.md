# Validator & Helper Tests

Comprehensive tests for all hfortix_fortios validators and helper functions.

## Test Files Created

### 1. Generic Validators (`test_generic_validators.py`)
Tests for basic field validation functions:
- ✅ `validate_required_fields()` - Check required fields are present
- ✅ `validate_color()` - Color index (0-32) validation
- ✅ `validate_status()` - Status field (enable/disable) validation
- ✅ `validate_enable_disable()` - Enable/disable value validation
- ✅ `validate_string_length()` - String length limit validation
- ✅ `validate_integer_range()` - Integer range validation

### 2. Network Validators (`test_network_validators.py`)
Tests for network-related validation functions:
- ✅ `validate_mac_address()` - MAC address format validation
- ✅ `validate_ip_address()` - IPv4 address format validation
- ✅ `validate_ipv6_address()` - IPv6 address format validation
- ✅ `validate_ip_network()` - IP network/subnet CIDR validation
- ✅ `validate_port_number()` - Port number range validation (0-4294967295)

### 3. Firewall Validators (`test_firewall_validators.py`)
Tests for firewall-specific validation functions:
- ✅ `validate_policy_id()` - Policy ID validation (0-4294967295)
- ✅ `validate_address_pairs()` - Complete address pair validation
- ✅ `validate_seq_num()` - Sequence number validation (0-4294967295)

### 4. Schedule Validators (`test_schedule_validators.py`)
Tests for schedule-related validation functions:
- ✅ `validate_schedule_name()` - Schedule name validation (max 31 chars)
- ✅ `validate_time_format()` - Time format validation (HH:MM)
- ✅ `validate_day_names()` - Day names validation for recurring schedules

### 5. SSH/SSL Proxy Validators (`test_ssh_ssl_validators.py`)
Tests for SSH and SSL proxy validation functions:
- ✅ `validate_ssh_host_key_type()` - SSH host key type validation
- ✅ `validate_ssh_host_key_status()` - SSH host key status validation
- ✅ `validate_ssh_host_key_nid()` - SSH ECDSA key NID validation
- ✅ `validate_ssh_host_key_usage()` - SSH host key usage validation
- ✅ `validate_ssh_source()` - SSH local CA/key source validation
- ✅ `validate_ssl_dh_bits()` - SSL Diffie-Hellman bits validation
- ✅ `validate_ssl_cipher_action()` - SSL cipher action validation

### 6. Endpoint Validators (`test_endpoint_validators.py`)
Tests for endpoint-specific validation functions (from `validation.py`):
- ✅ `validate_required_fields()` - Enhanced required fields validation with descriptions
- ✅ `validate_enum_field()` - Enum field validation with detailed error messages
- ✅ `validate_query_parameter()` - Query parameter validation
- ✅ `validate_multiple_enums()` - Batch enum field validation
- ✅ `validate_multiple_query_params()` - Batch query parameter validation

### 7. Normalizers (`test_normalizers.py`)
Tests for list normalization functions:
- ✅ `normalize_to_name_list()` - Convert various formats to [{'name': '...'}]
- ✅ `normalize_member_list()` - Normalize member lists (alias for groups)
- ✅ `normalize_table_field()` - Universal table field normalizer with schema awareness

### 8. Converters (`test_converters.py`)
Tests for data conversion functions:
- ✅ `convert_boolean_to_str()` - Convert bool to 'enable'/'disable'
- ✅ `filter_empty_values()` - Remove None and empty values from payloads

### 9. Builders (`test_builders.py`)
Tests for payload building functions:
- ✅ `build_cmdb_payload()` - Build CMDB API payloads (snake_case to kebab-case)
- ✅ `build_cmdb_payload_normalized()` - Build with auto-normalization
- ✅ `build_api_payload()` - Universal API payload builder with auto-normalization

### 10. Response Helpers (`test_response_helpers.py`)
Tests for response parsing functions:
- ✅ `get_name()` - Extract object name/mkey from response
- ✅ `get_mkey()` - Alias for get_name()
- ✅ `get_results()` - Extract results from response
- ✅ `is_success()` - Check if response indicates success

### 11. Metadata Functions (`test_metadata.py`)
Tests for schema metadata accessor functions:
- ✅ `get_field_description()` - Get field description/help text
- ✅ `get_field_type()` - Get field type (string, option, integer, table)
- ✅ `get_field_constraints()` - Get field constraints (min/max, length)
- ✅ `get_field_default()` - Get field default value
- ✅ `get_field_options()` - Get valid enum options
- ✅ `get_nested_schema()` - Get nested table schema
- ✅ `get_all_fields()` - Get list of all field names
- ✅ `get_field_metadata()` - Get complete field metadata
- ✅ `validate_field_value()` - Validate a field value against constraints

### 12. Formatting Functions (`test_formatting.py`)
Tests for data formatting utilities:
- ✅ `to_json()` - Convert any data to formatted JSON string
- ✅ `to_csv()` - Convert data to comma-separated string
- ✅ `to_dict()` - Convert any data to dictionary
- ✅ `to_multiline()` - Convert data to newline-separated string
- ✅ `to_list()` - Convert any data to list
- ✅ `to_quoted()` - Convert data to quoted string representation
- ✅ `to_table()` - Convert data to table format
- ✅ `to_yaml()` - Convert data to YAML-like format
- ✅ `to_xml()` - Convert data to simple XML format
- ✅ `to_key_value()` - Convert data to key=value pairs
- ✅ `to_markdown_table()` - Convert data to Markdown table
- ✅ `to_dictlist()` - Convert columnar dict to list of dicts
- ✅ `to_listdict()` - Convert list of dicts to columnar dict

### 13. Models (`test_models.py`)
Tests for FortiObject class and response processing:
- ✅ `FortiObject` - Zero-maintenance wrapper for API responses
  - Attribute access, dict-like interface, member_table auto-wrapping
  - get_full(), to_dict(), json property
  - repr, str, len, keys, values, items, get, contains
- ✅ `process_response()` - Process API response into FortiObjects (response_mode removed in 0.5.71)

## Test Coverage

**Total Functions Tested:** 75

**Categories:**
- Generic Field Validators: 6
- Network Validators: 5
- Firewall-specific Validators: 3
- Schedule Validators: 3
- SSH/SSL Proxy Validators: 7
- Endpoint Validators: 5
- Normalizers: 3
- Converters: 2
- Builders: 3
- Response Helpers: 4
- Metadata Functions: 9
- Formatting Functions: 13
- Models (FortiObject + process_response): 12

## Parallel Execution

**IMPORTANT:** Validator tests can be run in parallel since they:
- ✅ Don't make API calls to FortiGate
- ✅ Don't modify any external state
- ✅ Are pure validation logic tests
- ✅ Have no dependencies between tests

All other tests (CMDB, endpoints) should run **sequentially** to avoid overwhelming the FortiGate API.

To enable parallel execution for validators only, the test runner should:
1. Identify validator tests (in `pytest/validators/` folder)
2. Run validator tests in parallel using multiprocessing/threading
3. Run all other tests sequentially

## Running the Tests

Run all validator tests:
```bash
python run_tests.py
```

Run individual test files:
```bash
python pytest/validators/test_generic_validators.py
python pytest/validators/test_network_validators.py
python pytest/validators/test_firewall_validators.py
python pytest/validators/test_schedule_validators.py
python pytest/validators/test_ssh_ssl_validators.py
```

## Test Structure

Each test file follows the same pattern:
1. **Valid cases**: Test with correct values
2. **Invalid cases**: Test with incorrect values and verify proper exceptions
3. **Edge cases**: Test boundary conditions and special values
4. **Optional values**: Test that None is handled correctly for optional fields

## Source

All validators are from:
- `hfortix_fortios._helpers.validators`

Documentation: See the validators.py file for detailed docstrings on each validator function.
