# Schema Improvement Suggestions for Fortinet

**Date**: January 19, 2026  
**Project**: hfortix FortiOS SDK  
**Version**: 0.5.118  
**Contact**: Herman W. Jacobsen

---

## Executive Summary

This document outlines schema improvements that would significantly enhance the developer experience for FortiOS API consumers. The primary issue is **missing response field definitions** in monitor endpoint schemas, which prevents type-safe API interactions and IDE autocomplete functionality.

### Impact

- **100+ monitor endpoints** return `FortiObject[Any]` instead of typed responses
- **No IDE autocomplete** for response fields
- **No type checking** for response data access
- **Poor developer experience** compared to CMDB endpoints

### Request

Add `response_fields` sections to monitor endpoint schema files with proper field type definitions, enabling:
- ✅ Full IDE autocomplete for all response fields
- ✅ Type-safe attribute access with validation
- ✅ Literal type checking for enum values
- ✅ Better API documentation

---

## Problem Description

### Current Situation: Missing Schema

Many monitor endpoints completely lack `response_fields` in their schema definitions:

```json
{
  "path": "switch-controller/managed-switch/status",
  "http_methods": ["GET"],
  "fields": {},
  "response_fields": {}  // ❌ Empty - no field definitions
}
```

This results in:

```python
# Developer experience with missing schema
result = fgt.api.monitor.switch_controller.managed_switch.status.get()

# Type shows as FortiObject[Any] - no field information
result.serial     # ❓ No autocomplete, no type checking
result.ports      # ❓ Unknown field structure
result.state      # ❓ Unknown if this field exists
```

### Current Situation: Incomplete Schema

Some endpoints have **partial schema definitions** from OpenAPI specs but are still incomplete. For example, `dhcp-snooping` defines `snooping_entries` as an array but doesn't specify what properties each entry contains:

**OpenAPI Response Schema** (incomplete):
```json
{
  "response": {
    "type": "array",
    "items": {
      "type": "object",
      "properties": {
        "switch_id": {"type": "string"},
        "snooping_entries": {
          "type": "array"  // ❌ No items schema - missing entry structure
        }
      }
    }
  }
}
```

**FortiOS Schema** (what we need):
```json
{
  "path": "switch-controller/managed-switch/dhcp-snooping",
  "response_fields": {}  // ❌ Still empty in actual schema files
}
```

This results in the **same lack of type information** despite having OpenAPI documentation:

```python
result = fgt.api.monitor.switch_controller.managed_switch.dhcp_snooping.get()
for entry in result:
    entry.switch_id          # ✅ Works (defined in OpenAPI)
    entry.snooping_entries   # ✅ Works (defined in OpenAPI)
    
    # But what's inside snooping_entries?
    for server in entry.snooping_entries:
        server.mac   # ❓ No type info - array items not defined
        server.ip    # ❓ No autocomplete
        server.port  # ❓ Field structure unknown
```

### Desired Situation

With proper `response_fields` defined in FortiOS schema files:

```json
{
  "path": "switch-controller/managed-switch/dhcp-snooping",
  "http_methods": ["GET"],
  "response_fields": {
    "switch_id": {
      "type": "string",
      "category": "unitary",
      "help": "Managed switch identifier"
    },
    "snooping_entries": {
      "type": "complex",
      "category": "table",
      "help": "Detected DHCP servers",
      "children": {
        "mac": {"type": "string", "help": "MAC address"},
        "ip": {"type": "string", "help": "IP address"},
        "vlan": {"type": "string", "help": "VLAN name"},
        "port": {"type": "string", "help": "Physical port"},
        "trust": {"type": "string", "help": "Trust status"}
      }
    }
  }
}
```

This enables:

```python
# Enhanced developer experience with complete schema
result = fgt.api.monitor.switch_controller.managed_switch.dhcp_snooping.get()

# Type shows as DhcpSnoopingObject with full field definitions
for entry in result:
    entry.switch_id         # ✅ Autocomplete: str
    entry.snooping_entries  # ✅ Autocomplete: list[DhcpSnoopingSnoopingEntriesItem]
    
    for server in entry.snooping_entries:
        server.mac    # ✅ Autocomplete: str
        server.ip     # ✅ Autocomplete: str
        server.vlan   # ✅ Autocomplete: str
        server.port   # ✅ Autocomplete: str
        server.trust  # ✅ Autocomplete: str
```

---

## OpenAPI vs FortiOS Schema

### The Gap Between Specifications

While some endpoints have OpenAPI/Swagger documentation, this doesn't automatically provide type safety in the SDK because:

1. **Different Schema Formats**: 
   - OpenAPI uses JSON Schema format
   - FortiOS uses internal schema format with `response_fields`
   - SDK generator reads FortiOS schema files, not OpenAPI specs

2. **Incomplete OpenAPI Schemas**:
   - Many array types lack `items` definitions
   - Nested object structures often undefined
   - Example: `snooping_entries` defined as `array` but items not specified

3. **Schema File Location**:
   - OpenAPI specs: Used for documentation generation
   - FortiOS schemas: Used by device for validation and by SDK for type generation
   - **These are separate systems**

### Example: dhcp-snooping Endpoint

**OpenAPI Documentation** (available but incomplete):
```json
{
  "response": {
    "type": "array",
    "items": {
      "type": "object",
      "required": ["switch_id", "snooping_entries"],
      "properties": {
        "switch_id": {
          "type": "string",
          "title": "FortiSwitch ID"
        },
        "snooping_entries": {
          "title": "DHCP Servers",
          "type": "array"
          // ❌ Missing: items.properties for DHCP server entries
        }
      }
    }
  }
}
```

**FortiOS Schema** (what SDK needs):
```json
{
  "path": "switch-controller/managed-switch/dhcp-snooping",
  "http_methods": ["GET"],
  "response_fields": {}
  // ❌ Empty - needs complete field definitions
}
```

**What's Needed** (complete FortiOS schema):
```json
{
  "path": "switch-controller/managed-switch/dhcp-snooping",
  "response_fields": {
    "switch_id": {
      "type": "string",
      "category": "unitary"
    },
    "snooping_entries": {
      "type": "complex",
      "category": "table",
      "children": {
        "mac": {"type": "string"},
        "ip": {"type": "string"},
        "vlan": {"type": "string"},
        "port": {"type": "string"},
        "trust": {"type": "string"}
      }
    }
  }
}
```

---

## Priority Endpoints

### High Priority (17 endpoints)

**Switch Controller Managed Switch** - Most commonly used monitoring endpoints:

1. `switch-controller/managed-switch/dhcp-snooping` - DHCP server detection *(partial OpenAPI, no FortiOS schema)*
2. `switch-controller/managed-switch/faceplate-xml` - Widget rendering
3. `switch-controller/managed-switch/health-status` - Health statistics
4. `switch-controller/managed-switch/port-health` - Port statistics
5. `switch-controller/managed-switch/transceivers` - Transceiver info
6. `switch-controller/managed-switch/bios` - BIOS information
7. `switch-controller/managed-switch/cable-status` - Cable diagnostics
8. `switch-controller/managed-switch/port-stats` - Port statistics
9. `switch-controller/managed-switch/status` - Switch status
10. `switch-controller/managed-switch/models` - Switch models
11. `switch-controller/mclag-icl/eligible-peer` - MCLAG peers
12. `switch-controller/mclag-icl/health-status` - MCLAG health
13. `switch-controller/mclag-icl/stp-status` - STP status
14. `switch-controller/mclag-icl/tier-plus-candidates` - Tier candidates
15. `switch-controller/nac-device/stats` - NAC statistics
16. `switch-controller/recommendation/status` - Recommendation status
17. `switch-controller/isl-lockdown/status` - ISL lockdown status

### Medium Priority (30 endpoints)

**System Status & Monitoring**:
- `system/status` - System overview
- `system/time` - Current time
- `system/performance-status` - Performance metrics
- `system/resource-usage` - Resource utilization
- `system/interface` - Interface status
- `system/available-interfaces` - Available interfaces
- `system/dhcp` - DHCP status
- `system/ha-statistics` - HA statistics
- `system/ha-checksums` - HA checksums
- `system/csf` - CSF status
- `system/config-revision` - Configuration revisions
- `system/config-revision/file` - Config file download
- `system/config-revision/info` - Revision information
- `system/firmware/upgrade-paths` - Upgrade paths
- `system/global-resources` - Global resources

**VPN Monitoring**:
- `vpn/ipsec` - IPsec tunnels
- `vpn/ssl` - SSL VPN sessions
- `vpn/ssl/stats` - SSL VPN statistics
- `vpn-certificate/local` - Local certificates
- `vpn-certificate/remote` - Remote certificates
- `vpn-certificate/ca` - CA certificates
- `vpn-certificate/crl` - Certificate revocation lists
- `vpn/ike/gateway` - IKE gateways

**Firewall Sessions**:
- `firewall/session` - Active sessions
- `firewall/session6` - IPv6 sessions
- `firewall/policy` - Policy hit counts
- `firewall/policy6` - IPv6 policy hits
- `firewall/proxy-policy` - Proxy policy hits

### Lower Priority (50+ endpoints)

Network diagnostics, routing, WiFi, user authentication, logging, and other monitoring endpoints.

---

## Technical Specification

### Field Type Mapping

Monitor endpoint responses should use these field types:

| FortiOS Type | Schema Type | Python Type | Example |
|-------------|-------------|-------------|---------|
| String | `"string"` | `str` | `"port1"`, `"192.168.1.1"` |
| Integer | `"integer"` | `int` | `42`, `1500` |
| Boolean | `"boolean"` | `bool` | `true`, `false` |
| Enum | `"string"` + `options` | `Literal[...]` | `"enable"`, `"disable"` |
| Object | `"complex"` + `children` | `TypedDict` | `{"ip": "1.1.1.1"}` |
| Array | `"table"` + `children` | `list[TypedDict]` | `[{"name": "a"}]` |

### Schema Structure

```json
{
  "response_fields": {
    "field_name": {
      "type": "string|integer|boolean|complex",
      "category": "unitary|table|complex",
      "help": "Field description",
      "options": ["opt1", "opt2"],  // For enums
      "children": {                 // For nested objects
        "nested_field": {
          "type": "string",
          "help": "Nested field description"
        }
      }
    }
  }
}
```

### Example: dhcp-snooping Endpoint

**Before** (current schema):
```json
{
  "path": "switch-controller/managed-switch/dhcp-snooping",
  "module": "switch-controller",
  "name": "dhcp-snooping",
  "full_path": "switch-controller/managed-switch/dhcp-snooping",
  "http_methods": ["GET"],
  "fields": {},
  "response_fields": {}
}
```

**After** (suggested improvement):
```json
{
  "path": "switch-controller/managed-switch/dhcp-snooping",
  "module": "switch-controller",
  "name": "dhcp-snooping",
  "full_path": "switch-controller/managed-switch/dhcp-snooping",
  "http_methods": ["GET"],
  "fields": {},
  "response_fields": {
    "switch_id": {
      "type": "string",
      "category": "unitary",
      "help": "Managed FortiSwitch identifier (serial number or name)"
    },
    "snooping_entries": {
      "type": "complex",
      "category": "table",
      "help": "List of DHCP servers detected by this switch",
      "children": {
        "mac": {
          "type": "string",
          "category": "unitary",
          "help": "MAC address of DHCP server"
        },
        "ip": {
          "type": "string",
          "category": "unitary",
          "help": "IP address of DHCP server"
        },
        "vlan": {
          "type": "string",
          "category": "unitary",
          "help": "VLAN name or ID where DHCP server was detected"
        },
        "port": {
          "type": "string",
          "category": "unitary",
          "help": "Physical switch port where DHCP server was detected"
        },
        "lease_time": {
          "type": "integer",
          "category": "unitary",
          "help": "DHCP lease time in seconds"
        }
      }
    }
  }
}
```

---

## Benefits

### For Developers

1. **IDE Autocomplete**: Full IntelliSense support for all response fields
2. **Type Safety**: Compile-time checking prevents runtime errors
3. **Documentation**: Field descriptions directly in code
4. **Faster Development**: No need to consult API docs for field names

### For Fortinet

1. **Better DX**: Improved developer experience attracts more API consumers
2. **Fewer Support Requests**: Self-documenting API reduces confusion
3. **API Consistency**: Monitor endpoints match CMDB endpoint quality
4. **Competitive Advantage**: Best-in-class API documentation

### Example Impact

```python
# WITHOUT schema (current state)
result = fgt.api.monitor.switch_controller.managed_switch.dhcp_snooping.get()
# ❌ No autocomplete
# ❌ Type: FortiObject[Any]
# ❌ Must check docs for field names
# ❌ Runtime errors if field name wrong

# WITH schema (after improvement)
result = fgt.api.monitor.switch_controller.managed_switch.dhcp_snooping.get()
# ✅ Full autocomplete for switch_id, snooping_entries
# ✅ Type: DhcpSnoopingObject with all fields defined
# ✅ Compile-time errors for typos
# ✅ Self-documenting code
```

---

## Implementation Notes

### Schema Source

Response field definitions can be extracted from multiple sources:

1. **Swagger/OpenAPI Documentation**: 
   - Many endpoints already have response schemas in OpenAPI format
   - **However**: Some schemas are incomplete (e.g., arrays without item definitions)
   - Example: `dhcp-snooping` defines `snooping_entries` as `"type": "array"` but lacks `items.properties`
   - These partial schemas still need completion with full field definitions

2. **API Responses**: Capture actual response JSON and infer types

3. **FortiOS Documentation**: Extract from official API documentation

4. **Internal FortiOS Code**: Use internal schema definitions

**Note**: While OpenAPI/Swagger specs exist for some endpoints, they are often incomplete and don't match the FortiOS internal schema format. The FortiOS schema files (used by the device itself) need `response_fields` sections added.

### Backward Compatibility

Adding `response_fields` is **100% backward compatible**:

- Existing code continues to work
- Dynamic attribute access still works
- Only adds new type information
- No breaking changes

### Gradual Rollout

Suggest implementing in priority order:

1. **Phase 1**: High priority switch-controller endpoints (17 endpoints)
2. **Phase 2**: System status and VPN endpoints (30 endpoints)
3. **Phase 3**: Remaining monitor endpoints (50+ endpoints)

---

## Contact

For questions or to discuss implementation:

- **Project**: hfortix (FortiOS Python SDK)
- **Author**: Herman W. Jacobsen
- **GitHub**: hermanwjacobsen/hfortix
- **PyPI**: https://pypi.org/project/hfortix-fortios/

---

## Appendix: Complete Endpoint List

### Switch Controller (17 endpoints)
- switch-controller/managed-switch/dhcp-snooping
- switch-controller/managed-switch/faceplate-xml
- switch-controller/managed-switch/health-status
- switch-controller/managed-switch/port-health
- switch-controller/managed-switch/transceivers
- switch-controller/managed-switch/bios
- switch-controller/managed-switch/cable-status
- switch-controller/managed-switch/port-stats
- switch-controller/managed-switch/status
- switch-controller/managed-switch/models
- switch-controller/mclag-icl/eligible-peer
- switch-controller/mclag-icl/health-status
- switch-controller/mclag-icl/stp-status
- switch-controller/mclag-icl/tier-plus-candidates
- switch-controller/nac-device/stats
- switch-controller/recommendation/status
- switch-controller/isl-lockdown/status

### System (15 endpoints)
- system/status
- system/time
- system/performance-status
- system/resource-usage
- system/interface
- system/available-interfaces
- system/dhcp
- system/ha-statistics
- system/ha-checksums
- system/csf
- system/config-revision
- system/config-revision/file
- system/config-revision/info
- system/firmware/upgrade-paths
- system/global-resources

### VPN (12 endpoints)
- vpn/ipsec
- vpn/ssl
- vpn/ssl/stats
- vpn-certificate/local
- vpn-certificate/remote
- vpn-certificate/ca
- vpn-certificate/crl
- vpn/ike/gateway

### Firewall (8 endpoints)
- firewall/session
- firewall/session6
- firewall/policy
- firewall/policy6
- firewall/proxy-policy
- firewall/load-balance
- firewall/multicast-session
- firewall/multicast-session6

*(Full list of 100+ endpoints available upon request)*
