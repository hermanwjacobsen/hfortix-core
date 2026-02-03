# Python Keyword Handling in HFortix FortiOS

## Overview

The FortiOS API uses field names that sometimes conflict with Python reserved keywords (e.g., `as`, `class`, `type`, `from`, `import`, `global`). This document explains how HFortix handles these conflicts transparently.

## The Problem

Python reserved keywords cannot be used as parameter names:

```python
# ❌ This would cause a syntax error:
fgt.api.cmdb.router_bgp.put(as="65000")  # SyntaxError: invalid syntax

# ❌ This would also fail:
fgt.api.cmdb.user_radius.post(class=[{"name": "premium"}])  # SyntaxError
```

## The Solution

HFortix automatically handles keyword conflicts in **bidirectional mapping**:

### 1. Parameter Renaming (Generator Level)

The code generator renames conflicting fields using these patterns:

| API Field Name | Python Parameter | Pattern Used |
|----------------|------------------|--------------|
| `as` | `asn` | Custom alias (BGP-specific) |
| `class` | `class_` | Trailing underscore |
| `type` | `type_` | Trailing underscore |
| `from` | `from_` | Trailing underscore |
| `import` | `import_` | Trailing underscore |
| `global` | `global_` | Trailing underscore |

### 2. Bidirectional Automatic Mapping (Runtime)

HFortix provides **bidirectional** keyword mapping:

#### Outbound: Python → API (v0.5.110+)
When sending data to the FortiOS API, parameters are automatically converted:

```python
# You write:
fgt.api.cmdb.router.bgp.put(asn="65000")

# HFortix sends:
{"as": "65000"}
```

#### Inbound: API → Python (v0.5.111+)
When receiving data from the FortiOS API, fields are automatically mapped to Python attributes:

```python
# ✅ You write this (using Python-safe names):
fgt.api.cmdb.router.bgp.put(
    asn="65000",
    router_id="1.1.1.1"
)

# ✅ HFortix automatically sends this to the API:
{
    "as": "65000",           # asn → as
    "router-id": "1.1.1.1"   # router_id → router-id
}

# ✅ When you read the configuration back:
config = fgt.api.cmdb.router.bgp.get()
print(config.asn)           # API returns {"as": "65001"}, you access as .asn
print(config.router_id)     # API returns {"router-id": "..."}, you access as .router_id
```

## Keyword Mapping Reference

### Complete List of Keyword Conversions

```python
PYTHON_KEYWORD_TO_API_FIELD = {
    "asn": "as",           # BGP AS number (special case)
    "class_": "class",     # RADIUS class, traffic class, etc.
    "type_": "type",       # IP pool type, VIP type, address type, etc.
    "from_": "from",       # Source fields
    "import_": "import",   # Import configurations
    "global_": "global",   # Global scope settings
}
```

## Examples

### Example 1: BGP Configuration (Bidirectional)

```python
from hfortix_fortios import FortiOS

fgt = FortiOS(host="192.168.1.99", token="your-api-token")

# ✅ WRITING: Configure BGP with AS number (Python → API)
result = fgt.api.cmdb.router.bgp.put(
    asn="65000",              # Converted to "as" in API
    router_id="10.0.0.1",     # Converted to "router-id" in API
    log_neighbour_changes="enable"
)

# ✅ READING: Get BGP configuration back (API → Python)
config = fgt.api.cmdb.router.bgp.get()
print(config.asn)             # API {"as": "65000"} → access as .asn
print(config.router_id)       # API {"router-id": "..."} → access as .router_id
```

**API Payload Sent (PUT):**
```json
{
    "as": "65000",
    "router-id": "10.0.0.1",
    "log-neighbour-changes": "enable"
}
```

**API Response Received (GET):**
```json
{
    "as": "65000",
    "router-id": "10.0.0.1",
    "log-neighbour-changes": "enable"
}
```

### Example 2: RADIUS Server with Class Attributes

```python
# Configure RADIUS server with class attributes
result = fgt.api.cmdb.user_radius.post(
    name="radius-server-1",
    server="192.168.1.100",
    secret="secret123",
    class_=[                   # Converted to "class" in API
        {"name": "premium"},
        {"name": "standard"}
    ]
)
```

**API Payload Sent:**
```json
{
    "name": "radius-server-1",
    "server": "192.168.1.100",
    "secret": "secret123",
    "class": [
        {"name": "premium"},
        {"name": "standard"}
    ]
}
```

### Example 3: Firewall IP Pool with Type

```python
# Create IP pool with type field
result = fgt.api.cmdb.firewall_ippool.post(
    name="pool1",
    type_="overload",          # Converted to "type" in API
    startip="10.1.1.1",
    endip="10.1.1.100"
)
```

**API Payload Sent:**
```json
{
    "name": "pool1",
    "type": "overload",
    "startip": "10.1.1.1",
    "endip": "10.1.1.100"
}
```

### Example 4: Firewall VIP with Type

```python
# Create VIP with type field
result = fgt.api.cmdb.firewall_vip.post(
    name="web-server-vip",
    type_="static-nat",        # Converted to "type" in API
    extip="203.0.113.10",
    mappedip="192.168.1.50"
)
```

**API Payload Sent:**
```json
{
    "name": "web-server-vip",
    "type": "static-nat",
    "extip": "203.0.113.10",
    "mappedip": "192.168.1.50"
}
```

## How It Works Internally

### Outbound Mapping (Python → API)

**File**: `packages/fortios/hfortix_fortios/_helpers/builders.py`

When you call an API endpoint method, HFortix follows this process:

1. **Parameter Collection**: Collect all parameters (e.g., `asn="65000"`, `router_id="1.1.1.1"`)

2. **Keyword Reverse Mapping**: Check if parameter name is a renamed keyword:
   ```python
   if param_name in PYTHON_KEYWORD_TO_API_FIELD:
       api_key = PYTHON_KEYWORD_TO_API_FIELD[param_name]  # asn → as
   ```

3. **Snake Case to Kebab Case**: Convert underscores to hyphens:
   ```python
   else:
       api_key = param_name.replace("_", "-")  # router_id → router-id
   ```

4. **Send to API**: Final payload uses correct API field names

### Inbound Mapping (API → Python)

**File**: `packages/fortios/hfortix_fortios/models.py`

When you access attributes on a `FortiObject` response:

1. **Attribute Access**: You access `result.asn`

2. **Reverse Mapping Lookup**: Check if Python attribute maps to an API keyword:
   ```python
   API_FIELD_TO_PYTHON_KEYWORD = {
       "as": "asn",
       "class": "class_",
       "type": "type_",
       # ...
   }
   
   reverse_map = {v: k for k, v in API_FIELD_TO_PYTHON_KEYWORD.items()}
   if name in reverse_map:  # "asn" in reverse_map?
       key = reverse_map[name]  # key = "as"
   ```

3. **Data Lookup**: Retrieve value using API field name:
   ```python
   value = self._data.get("as")  # Gets "65000"
   ```

4. **Return Value**: You get the value as if you accessed `.asn`

## Special Case: Parameters That Keep Underscores

### Overview

While most FortiOS API parameters use **kebab-case** (hyphens), a small number of parameters use **snake_case** (underscores). The most notable examples are file upload parameters.

**Version Added**: v0.5.122 (January 20, 2026)

### The NO_HYPHEN_PARAMETERS Whitelist

HFortix maintains a whitelist of parameters that should **NOT** be converted from underscores to hyphens:

```python
# From packages/fortios/hfortix_fortios/_helpers/builders.py
NO_HYPHEN_PARAMETERS = {
    "file_content",      # File upload endpoints
    "key_file_content",  # Certificate import endpoints
}
```

### Why This Matters

Before v0.5.122, these parameters were incorrectly converted, causing HTTP 400 errors:

```python
# ❌ Before v0.5.122 (BROKEN):
result = fgt.api.monitor.system.config_script.upload.post(
    filename="backup.conf",
    file_content=base64_data  # Incorrectly sent as "file-content"
)
# Result: HTTP 400 - Parameter not found

# ✅ After v0.5.122 (FIXED):
result = fgt.api.monitor.system.config_script.upload.post(
    filename="backup.conf",
    file_content=base64_data  # Correctly sent as "file_content"
)
# Result: HTTP 200 - Success
```

### Affected Endpoints (15+)

All endpoints that accept file uploads or certificate imports:

#### System Configuration
- `monitor/system/config-script/upload` - Upload and run config script
- `monitor/system/config/restore` - Restore configuration from file
- `monitor/system/firmware/upgrade` - Upload firmware image

#### VPN Certificates
- `monitor/vpn-certificate/ca/import` - Import CA certificate (`file_content`)
- `monitor/vpn-certificate/local/import` - Import local certificate (`file_content` + `key_file_content`)

#### Firmware Uploads
- `monitor/wifi/firmware/upload` - Upload WiFi firmware
- `monitor/wifi/region-image/upload` - Upload WiFi region image
- `monitor/switch-controller/fsw-firmware/upload` - Upload FortiSwitch firmware
- `monitor/extender-controller/extender/upgrade` - Upload FortiExtender firmware

#### Other Upload Endpoints
- `monitor/license/database/upgrade` - Upload license database
- `monitor/web-ui/language/import` - Import custom language file

### Implementation

The payload builder functions check this whitelist before converting underscores:

```python
# From packages/fortios/hfortix_fortios/_helpers/builders.py

for param_name, value in params.items():
    if value is None:
        continue

    # First, check if this is a Python keyword that needs reverse mapping
    if param_name in PYTHON_KEYWORD_TO_API_FIELD:
        api_key = PYTHON_KEYWORD_TO_API_FIELD[param_name]
    # Check if this parameter should keep underscores (e.g., file_content)
    elif param_name in NO_HYPHEN_PARAMETERS:
        api_key = param_name  # Keep underscore - don't convert
    else:
        # Convert snake_case to kebab-case for FortiOS API
        api_key = param_name.replace("_", "-")
    
    payload[api_key] = value
```

### Usage Example: Certificate Import

```python
import base64
from hfortix_fortios import FortiOS

fgt = FortiOS(host="192.168.1.99", token="your-api-token")

# Read certificate and key files
with open("server.crt", "rb") as f:
    cert_content = base64.b64encode(f.read()).decode()

with open("server.key", "rb") as f:
    key_content = base64.b64encode(f.read()).decode()

# Import certificate with both file_content and key_file_content
result = fgt.api.monitor.vpn_certificate.local_.import_.post(
    certname="my-server-cert",
    file_content=cert_content,      # ✅ Sent as "file_content" (underscore)
    key_file_content=key_content,   # ✅ Sent as "key_file_content" (underscore)
    password="key-password"         # ✅ Sent as "password" (no underscore)
)

print(f"Certificate imported: {result.http_status_code == 200}")
```

**API Payload Sent:**
```json
{
    "certname": "my-server-cert",
    "file_content": "LS0tLS1CRUdJTi...",
    "key_file_content": "LS0tLS1CRUdJTi...",
    "password": "key-password"
}
```

### How to Identify These Parameters

1. **Schema Files**: Check schema files in `/schema/{version}/monitor/` - these parameters are defined with underscores:
   ```json
   "file_content": {
       "name": "file_content",
       "type": "string",
       "summary": "Provided when uploading a file: base64 encoded file data."
   }
   ```

2. **FortiOS API Documentation**: Official docs show these as `file_content` (not `file-content`)

3. **Error Messages**: If you get HTTP 400 with "parameter not found" on a file upload, it might be a missing NO_HYPHEN parameter

### Implementation Locations

**Outbound (v0.5.110+):**
- **File**: `packages/fortios/hfortix_fortios/_helpers/builders.py`
- **Mapping**: `PYTHON_KEYWORD_TO_API_FIELD` dictionary
- **Functions**:
  - `build_cmdb_payload()` - CMDB endpoints (PUT/POST)
  - `build_cmdb_payload_normalized()` - CMDB with list normalization
  - `build_api_payload()` - Generic API endpoints

**Inbound (v0.5.111+):**
- **File**: `packages/fortios/hfortix_fortios/models.py`
- **Mapping**: `API_FIELD_TO_PYTHON_KEYWORD` dictionary
- **Methods**:
  - `FortiObject.__getattr__()` - Attribute access (e.g., `result.asn`)
  - `FortiObject.get_full()` - Raw field access## IDE Support

Your IDE will show the Python-safe parameter names in autocomplete:

```python
# When you type: fgt.api.cmdb.router_bgp.put(
# IDE shows:
#   - asn: str           ← Not 'as' (keyword conflict avoided)
#   - router_id: str     ← Snake case (Pythonic)
#   - log_neighbour_changes: Literal["enable", "disable"]
```

## Type Stubs

The type stub files (`.pyi`) use the Python-safe names:

```python
# From packages/fortios/hfortix_fortios/api/v2/cmdb/router/bgp.pyi
def put(
    self,
    *,
    asn: str,                    # Not 'as'
    router_id: str | None = None,
    # ... other parameters
) -> FortiResponse: ...
```

## Common Fields Affected

Here are the most common endpoints/fields that use keyword conversions:

### `asn` → `as` (1 endpoint)
- **BGP Configuration**: 
  - `api.cmdb.router.bgp` - Router AS number field

### `class_` → `class` (Multiple endpoints)
- **RADIUS Servers**:
  - `api.cmdb.user.radius` - RADIUS class attributes (list of class names)
- **Traffic Shaping**: 
  - `api.cmdb.firewall.shaping_profile` - Traffic class definitions
- **DLP**: 
  - `api.cmdb.dlp.filepattern` - File classification patterns

### `type_` → `type` (Many endpoints - generic field)

> **Note**: The `type_` field is very common across FortiOS. It appears in 100+ endpoints.
> Consider context-specific naming in future versions (see TODO section below).

**Common Examples:**

#### Firewall Objects
- `api.cmdb.firewall.ippool` - Pool type: `overload`, `one-to-one`, `fixed-port-range`, `port-block-allocation`
- `api.cmdb.firewall.vip` - VIP type: `static-nat`, `load-balance`, `server-load-balance`, `dns-translation`, `fqdn`
- `api.cmdb.firewall.vip46` - VIP46 type: `static-nat`, `load-balance`, `server-load-balance`
- `api.cmdb.firewall.vip64` - VIP64 type: `static-nat`, `load-balance`, `server-load-balance`
- `api.cmdb.firewall.multicast_address` - Address type: `multicastrange`, `broadcastmask`
- `api.cmdb.firewall.proxy_address` - Proxy type: `host`, `url`, `category`, `method`, `ua`, `header`, `src-advanced`, `dst-advanced`

#### System & Services  
- `api.cmdb.system.central_management` - Management type: `fortimanager`, `fortiguard`, `none`
- `api.cmdb.system.external_resource` - Resource type: `category`, `address`, `domain`, `malware`
- `api.cmdb.system.interface` - Interface type: `physical`, `vlan`, `aggregate`, `redundant`, `tunnel`, `loopback`, etc.
- `api.cmdb.system.saml` - SAML type: `username`, `email`, `profile-name`

#### Monitoring Endpoints
- `api.monitor.system.certificate.download` - Certificate type
- `api.monitor.system.csf.register_appliance` - Appliance type
- `api.monitor.system.sdn_connector.status` - SDN connector type
- `api.monitor.router.ipv4` - Route type
- `api.monitor.router.ipv6` - Route type  
- `api.monitor.router.statistics` - Statistics type
- `api.monitor.router.charts` - Chart type
- `api.monitor.firmware.extension_device` - Device type
- `api.monitor.extender_controller.extender` - Extender type
- `api.monitor.vpn_certificate.local.import_` - Certificate import type
- `api.monitor.wifi.client` - WiFi client type
- `api.monitor.vpn.ssl.delete` - VPN SSL deletion type
- `api.service.security_rating.report` - Security report type

#### Web Filtering
- `api.cmdb.webfilter.profile` - Multiple type fields:
  - Quota type: `time`, `traffic`
  - Pattern type: `regex`, `literal`
- `api.cmdb.webfilter.urlfilter` - Filter type: `simple`, `regex`, `wildcard`
- `api.cmdb.videofilter.profile` - Video filter type: `category`, `channel`, `title`, `description`

#### Load Balancing & Monitoring
- `api.cmdb.firewall.ldb_monitor` - Monitor type: `PING`, `TCP`, `HTTP`, `HTTPS`, `passive-sip`
- `api.cmdb.firewall.shaping_profile` - Profile type: `policing`, `queuing`
- `api.cmdb.firewall.ssh.host_key` - SSH key type: `RSA`, `DSA`, `ECDSA`, `ED25519`

### `from_`, `import_`, `global_` (Rare)
- Various configuration imports and global settings (less common, scattered across endpoints)

## Version History

- **v0.5.111** (2026-01-18): ✅ **Added bidirectional mapping** - API responses now map keyword fields to Python attributes (e.g., API `{"as": "65001"}` → Python `result.asn`)
- **v0.5.110** (2026-01-18): ✅ Added automatic keyword-to-API-field reverse mapping for outbound requests
- **v0.5.109** (2026-01-18): ✅ Added snake_case to kebab-case conversion
- **Earlier versions**: ❌ Keywords caused API errors (users had to manually use API field names)

## Troubleshooting

### Issue: Parameter not being converted

**Problem**: You're using a keyword field but it's not being converted.

**Solution**: Make sure you're using the correct Python parameter name:
- Use `asn` (not `as`)
- Use `class_` (not `class`)
- Use `type_` (not `type`)

### Issue: Type checker complaining

**Problem**: IDE shows type error for keyword parameter.

**Solution**: Update your type stubs:
```bash
pip install --upgrade hfortix-fortios
```

## Best Practices

1. **Always use Python-safe names**: Use `asn`, `class_`, `type_` in your code
2. **Trust the conversion**: HFortix handles the API mapping automatically
3. **Use IDE autocomplete**: Let your IDE guide you to the correct parameter names
4. **Check type hints**: Type stubs show the correct Python parameter names

## Additional Resources

- [Field Name Conversion Guide](FILTERING_GUIDE.md) - General field name handling
- [API Documentation](API_COVERAGE.md) - Complete API endpoint coverage
- [Error Handling](ERROR_HANDLING_CONFIG.md) - Handling API errors
