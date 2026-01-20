# NO_HYPHEN_PARAMETERS - Complete Documentation

## Overview

The `NO_HYPHEN_PARAMETERS` set contains all FortiOS API parameters that **must preserve underscores** when sent to the API. This is a comprehensive whitelist of exceptions to the library's normal snake_case → kebab-case parameter conversion.

## Background

### The Problem

The hfortix library follows Python naming conventions by using `snake_case` for parameter names, but the FortiOS API typically expects parameters in `kebab-case` format:

```python
# Python code (snake_case)
result = fgt.api.monitor.system.interface.get(interface_name="port1")

# Sent to API (kebab-case)
GET /api/v2/monitor/system/interface?interface-name=port1
```

However, **162 parameters** across the FortiOS API are exceptions to this rule - they contain underscores in the schema and the API expects them to remain as underscores.

### The Solution

All parameters in `NO_HYPHEN_PARAMETERS` bypass the kebab-case conversion and are sent to the API exactly as written in Python code.

## Analysis Summary

- **Analysis Date**: January 20, 2026
- **FortiOS Versions Analyzed**: 7.4.8 and 7.6.5
- **Total Schema Files Scanned**: 2,591+
- **Total Unique Parameters**: 435
- **Parameters with Underscores**: 212
- **Request Parameters with Underscores**: 162
- **Format Conflicts Found**: **0** ✅

**Critical Finding**: No parameter exists in both underscore and hyphen formats across different endpoints, eliminating the risk of conflicts.

## Complete Parameter List (162 parameters)

### File Operations (36+ endpoints)
- `file_content` - File upload/import operations (firmware, certificates, configs, etc.)
- `key_file_content` - Certificate private key import
- `file_format` - Backup file format specification
- `file_id` - File identifier for upgrades

### Authentication & Registration (20+ parameters)
- `account_id` / `account_password` - VM license downloads
- `reseller_id` / `reseller_name` - FortiCare reseller info
- `registration_code` - License registration
- `old_password` / `new_password` - Password changes
- `is_government` - Government account flag
- `agreement_accepted` - Terms acceptance

### Network & Flow (30+ parameters)
- `ip_version` - **Most common** (32 endpoints)
- `ip_address` / `ip_addresses` / `ip_mask`
- `ipv4_mask` / `ipv6_prefix` / `ipv6_only` / `is_ipv6`
- `source_ip` / `source_port` / `destination_port`
- `addr_from` / `addr_to` - Address ranges
- `port_from` / `port_to` - Port ranges
- `saddr_from` / `saddr_to` - Source address ranges
- `daddr_from` / `daddr_to` - Destination address ranges
- `sport_from` / `sport_to` - Source port ranges
- `dport_from` / `dport_to` - Destination port ranges

### Device & Hardware (20+ parameters)
- `serial_no` - Device serial number
- `switch_id` / `switch_ids` - Switch controller operations
- `wtp_id` - WiFi access point ID
- `radio_id` - WiFi radio ID
- `ems_id` - Endpoint Management Server ID
- `vcluster_id` - Virtual cluster ID
- `mac_address` - MAC address lookup

### Certificates & PKI (15+ parameters)
- `acme_ca_url` / `acme_domain` / `acme_email` - ACME certificate automation
- `acme_renew_window` / `acme_rsa_key_size`
- `scep_url` / `scep_password` / `scep_ca_id` - SCEP enrollment
- `common_name` / `subject_alt_name` - Certificate attributes
- `import_method` - Certificate import method

### Query & Filtering (20+ parameters)
- `query_id` / `query_type` - User/device queries
- `filter_logic` - Query filter logic
- `cache_query` - Query caching
- `timestamp_from` / `timestamp_to` - Time ranges
- `search_tables` / `skip_tables` - Table filtering
- `view_type` / `view_level` - View configuration

### FortiView & Reporting (15+ parameters)
- `report_by` / `report_type` / `report_types`
- `report_name` - Report identifier
- `sort_by` - Sorting criteria
- `chart_only` - Chart data only
- `time_period` - Report time period

### Configuration & System (20+ parameters)
- `config_id` / `config_ids` - Configuration revision IDs
- `id_list` - List of IDs (config scripts, etc.)
- `event_log_message` - Event logging
- `all_vdoms` - All VDOM flag
- `vdom_name` - VDOM name
- `session_id` - Session identifier

### HA & Clustering (10+ parameters)
- `parent_peer1` / `parent_peer2` - MCLAG ICL peers
- `isl_port_group` - Inter-switch link port group
- `is_tier2` - MCLAG tier flag
- `mgmt_ip` / `mgmt_port` / `mgmt_url_parameters` - Management settings

### WiFi & Wireless (15+ parameters)
- `ap_interface` - Access point interface
- `image_id` / `image_type` - Firmware image info
- `region_name` / `region_id` - Regional settings
- `platform_type` - Platform identifier
- `indoor_outdoor` - AP deployment type
- `managed_ssid_only` - SSID filtering
- `start_vlan_id` / `end_vlan_id` - VLAN ranges
- `with_triangulation` / `with_stats` - Data inclusion flags

### Firewall & Policy (15+ parameters)
- `policy_type` - Policy type filter
- `protocol_number` / `protocol_option`
- `interface_name` / `intf_name`
- `shaper_name` - Traffic shaper
- `ips_sensor` - IPS sensor name
- `gtp_profile` - GTP profile
- `user_type` / `user_group` / `user_db` / `user_name`

### FortiToken & 2FA (10+ parameters)
- `sms_phone` / `sms_method` / `sms_server` - SMS provisioning
- `phone_number_list` / `phone_user_list`
- `email_list` - Email provisioning
- `vpn_name` - VPN identifier
- `key_length` / `mpsk_profile` - Key generation

### GTP & Mobile (10+ parameters)
- `cteid_addr` / `cteid_addr6` - Control TEID addresses
- `fteid_addr` / `fteid_addr6` - Forwarding TEID addresses
- `ms_addr` / `ms_addr6` - Mobile station addresses

### External Services (15+ parameters)
- `proxy_url` - Proxy configuration
- `ldap_filter` - LDAP query filter
- `skip_schema` / `server_info_only` - LDAP options
- `auth_type` / `server_name` - Authentication
- `client_name` / `group_name` - SCIM operations
- `endpoint_ip` - ClearPass integration

### Miscellaneous (20+ parameters)
- `lang_name` / `lang_comments` - Language customization
- `usb_filename` - USB operations
- `license_key` - License operations
- `health_check_name` - SD-WAN health checks
- `service_type` - FortiGuard services
- `count_only` / `counts_only` / `total_only` - Count flags
- `key_only` / `status_only` / `summary_only` - Output filtering
- `include_*` flags (ha, fsso, aggregate, dynamic, vlan, notes, ttl, unrated)
- `skip_*` flags (detect, eos, vpn_child)
- `with_*` flags (ca, cert, crl, remote)
- `confirm_*` flags (not_ga_certified, not_signed, password_mask)
- `find_all_references` / `check_status_only` / `format_partition`
- `ignore_*` flags (invalid_signature, admin_lockout_upon_update, admin_lockout_upon_downgrade)

## Most Common Parameters (Top 10)

1. **file_content** - 36 endpoints
   - File uploads, firmware, certificates, configurations
   
2. **ip_version** - 32 endpoints
   - IPv4/IPv6 specification across many categories

3. **report_by** - 9 endpoints
   - FortiView reporting

4. **is_government** - 9 endpoints
   - Registration and licensing

5. **ems_id** - 8 endpoints
   - Endpoint Management Server operations

6. **config_id** - 8 endpoints
   - Configuration revision management

7. **serial_no** - 8 endpoints
   - HA peer operations

8. **sort_by** - 7 endpoints
   - FortiView sorting

9. **ip_mask** - 7 endpoints
   - Router statistics and charts

10. **lang_name** - 6 endpoints
    - Web UI custom languages

## Usage in Code

### Automatic Handling

The library automatically preserves these parameters:

```python
# Python code
result = fgt.api.monitor.system.config_script.upload.post(
    filename="test.conf",
    file_content=base64_content  # Preserved as-is
)

# Sent to API
POST /api/v2/monitor/system/config-script/upload
{
    "filename": "test.conf",
    "file_content": "..."  # NOT converted to "file-content"
}
```

### Where It's Applied

The whitelist is used in three locations:

1. **`client.py`** - `convert_field_names()` function
   ```python
   key if key in NO_HYPHEN_PARAMETERS else key.replace("_", "-")
   ```

2. **`_helpers/builders.py`** - `build_cmdb_payload()`
3. **`_helpers/builders.py`** - `build_cmdb_payload_normalized()`
4. **`_helpers/builders.py`** - `build_api_payload()`

## Schema Verification

All parameters have been verified in FortiOS schema files (7.4.8 and 7.6.5):

```bash
# Example verification
$ grep -r '"file_content"' schema/
schema/7.6.5/monitor/system.config-script.upload.json:    "file_content": {
schema/7.6.5/monitor/vpn-certificate.ca.import.json:    "file_content": {
# ... 36 total matches
```

## Endpoint Examples by Category

### Monitor Endpoints
- `monitor/system/config-script/upload` - `file_content`, `id_list`
- `monitor/system/firmware/upgrade` - `file_content`, `file_id`, `ignore_invalid_signature`
- `monitor/system/vmlicense/download-eval` - `account_id`, `account_password`, `is_government`
- `monitor/vpn-certificate/local/import` - `file_content`, `key_file_content`, `acme_*` params
- `monitor/wifi/firmware/upload` - `file_content`, `image_id`
- `monitor/user/device/query` - `query_id`, `query_type`, `filter_logic`, `timestamp_from`, `timestamp_to`

### CMDB Endpoints
- Most CMDB endpoints use kebab-case exclusively
- Exception: query parameters may use underscores

### Service Endpoints
- `service/sniffer/*` - Standard kebab-case

## Version History

- **v0.5.124** (2026-01-20): Comprehensive update - added all 162 underscore parameters
- **v0.5.123** (2026-01-20): Added `id_list`
- **v0.5.122** (2026-01-20): Initial whitelist with `file_content`, `key_file_content`

## Testing

To verify a parameter should be in the whitelist:

```python
import json
from pathlib import Path

param_name = "your_param_name"

for schema_file in Path("schema").rglob("*.json"):
    with open(schema_file) as f:
        data = json.load(f)
    if "request_fields" in data and param_name in data["request_fields"]:
        print(f"Found in: {data.get('path')}")
        print(f"  File: {schema_file}")
```

## Maintenance

When FortiOS releases new versions:

1. Run the parameter analysis script on new schemas
2. Compare with existing `NO_HYPHEN_PARAMETERS`
3. Add any new parameters found in `request_fields`
4. Verify no format conflicts exist
5. Update this documentation
6. Increment library version

## Related Documentation

- `docs/fortios/PYTHON_KEYWORD_HANDLING.md` - Python keyword mapping
- `CHANGELOG.md` - Version history
- `packages/fortios/hfortix_fortios/_helpers/field_overrides.py` - Implementation
