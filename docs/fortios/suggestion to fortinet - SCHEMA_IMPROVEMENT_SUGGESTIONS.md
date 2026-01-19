# Schema Improvement Suggestions for Fortinet

## Overview

This document contains suggestions for improving the FortiOS REST API schema definitions to provide better type safety, IDE autocomplete support, and developer experience.

## Critical Issue: Missing Response Field Definitions in Monitor Endpoints

### Problem

Many **monitor endpoints** in the FortiOS REST API schema lack response field definitions (`fields` property in schema JSON). This prevents:

1. **Type-safe development** - Developers cannot get autocomplete for response fields
2. **API documentation** - No programmatic way to discover what fields are returned
3. **Validation** - Cannot validate response structure at compile-time
4. **IDE support** - Type checkers like Pylance show `FortiObject[Any]` instead of specific typed objects

### Impact

Without response field definitions, developers must:
- Rely on trial-and-error to discover available fields
- Use generic attribute access (`getattr()`) with string literals
- Cannot benefit from IDE autocomplete and type checking
- Risk runtime errors from typos in field names

### Examples of Affected Endpoints

#### Switch Controller Managed Switch Endpoints

All of the following endpoints lack response field definitions:

| Endpoint | Method | Description | Access Group |
|----------|--------|-------------|--------------|
| `/switch-controller/managed-switch/faceplate-xml` | GET | Retrieve XML for rendering FortiSwitch faceplate widget | wifi |
| `/switch-controller/managed-switch/factory-reset` | POST | Send 'Factory Reset' command to a given FortiSwitch | wifi |
| `/switch-controller/managed-switch/dhcp-snooping` | GET | Retrieve DHCP servers monitored by FortiSwitches | wifi |
| `/switch-controller/managed-switch/transceivers` | GET | Get a list of transceivers being used by managed FortiSwitches | any |
| `/switch-controller/managed-switch/bios` | GET | Get a list of BIOS info by managed FortiSwitches | any |
| `/switch-controller/managed-switch/health-status` | GET | Retrieve health-check statistics for managed FortiSwitches | wifi |
| `/switch-controller/managed-switch/port-health` | GET | Retrieve port health statistics for managed FortiSwitches | wifi |

### Current State

**Schema example** (switch-controller/managed-switch/dhcp-snooping):
```json
{
  "path": "switch-controller/managed-switch/dhcp-snooping",
  "http_methods": ["GET"],
  "has_mkey": false,
  "fields": null,  // ❌ No field definitions!
  "capabilities": {
    "endpoint_type": "singleton",
    "crud": {
      "read": true
    }
  }
}
```

**Resulting type stub**:
```python
def get(self, ...) -> FortiObject[Any]:  # ❌ Generic, no field autocomplete
    ...
```

### Desired State

**Enhanced schema** (with response fields):
```json
{
  "path": "switch-controller/managed-switch/dhcp-snooping",
  "http_methods": ["GET"],
  "has_mkey": false,
  "fields": {
    "switch_id": {
      "type": "string",
      "category": "unitary",
      "description": "Managed switch identifier"
    },
    "snooping_entries": {
      "type": "table",
      "category": "table",
      "description": "List of detected DHCP servers",
      "children": {
        "mac": {
          "type": "string",
          "description": "MAC address of DHCP server"
        },
        "ip": {
          "type": "string",
          "description": "IP address of DHCP server"
        },
        "vlan": {
          "type": "integer",
          "description": "VLAN ID"
        },
        "port": {
          "type": "string",
          "description": "Switch port"
        }
      }
    }
  }
}
```

**Resulting type stub** (with full type safety):
```python
class DhcpSnoopingObject(FortiObject):
    @property
    def switch_id(self) -> str: ...  # ✅ Typed property with autocomplete
    
    @property
    def snooping_entries(self) -> list[DhcpSnoopingSnoopingEntriesObject]: ...

def get(self, ...) -> DhcpSnoopingObject:  # ✅ Specific typed object
    ...
```

## Recommendation

### Priority 1: Monitor Endpoints

Add response field definitions to **all monitor endpoints**, especially:

1. **Switch controller endpoints** (listed above)
2. **System status/statistics endpoints**
3. **VPN status endpoints**
4. **Firewall session monitoring**
5. **Network diagnostics endpoints**

### Priority 2: Service Endpoints

Review and add field definitions for service endpoints that currently lack them.

### Implementation Approach

For each endpoint missing field definitions:

1. **Document actual API response** - Capture real response from FortiOS device
2. **Identify field types** - Determine whether each field is:
   - `string`, `integer`, `boolean` (unitary types)
   - `complex` (nested object)
   - `table` (array of objects)
3. **Add field metadata**:
   - `type`: Field data type
   - `category`: `unitary`, `complex`, or `table`
   - `description`: Human-readable field description
   - `children`: For complex/table types, define nested structure
   - `readonly`: Whether field is read-only
4. **Update Swagger/OpenAPI spec** - Include in official API documentation

## Benefits

Adding response field definitions will:

✅ **Enable IDE autocomplete** - Developers see available fields while typing
✅ **Catch errors at compile-time** - Type checkers detect typos and invalid field access
✅ **Improve documentation** - Programmatic API field discovery
✅ **Enhance SDK quality** - Generated SDKs provide better type safety
✅ **Reduce support burden** - Developers spend less time guessing field names
✅ **Better developer experience** - Modern IDE tooling works correctly

## Current Workaround

In the hfortix SDK, we've implemented:

1. **`FortiObject.__iter__`** - Allows iteration over list responses from monitor endpoints
2. **`FortiObject[Any]`** - Generic type parameter for endpoints without field definitions
3. **Dynamic attribute access** - `getattr()` fallback for unknown fields

However, these are **runtime solutions** that cannot provide compile-time type safety or IDE autocomplete.

## Contact

If you need examples of actual response structures from specific endpoints to help populate schema field definitions, please contact the hfortix maintainers. We have test suites that capture real FortiOS API responses.

---

**Document Version:** 1.0
**Date:** January 19, 2026
**Affected FortiOS Versions:** 7.6.5 (likely affects other versions)
**SDK Version:** hfortix 0.5.117+
