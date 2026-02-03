# FortiOS API Generator Design Document

**Version:** 0.5.0  
**Target FortiOS Version:** 7.6  
**Date:** January 3, 2026  
**Status:** Design Phase

---

## Table of Contents

1. [Overview](#overview)
2. [Design Principles](#design-principles)
3. [Old Implementation Analysis](#old-implementation-analysis)
4. [Enhanced Architecture](#enhanced-architecture)
5. [Generator Components](#generator-components)
6. [Generated Code Structure](#generated-code-structure)
7. [Feature Enhancements](#feature-enhancements)
8. [Implementation Roadmap](#implementation-roadmap)
9. [Examples](#examples)

---

## Overview

This document outlines the complete design for regenerating the FortiOS API from schema files downloaded directly from FortiGate devices. The goal is to preserve the excellent "dual approach" from the old implementation while significantly enhancing validators, type safety, and developer experience.

### Goals

- ✅ **Preserve what worked:** Clean API class structure, flexible parameters, comprehensive docs
- ✅ **Enhance validation:** Better error messages, field dependencies, context-aware suggestions
- ✅ **Improve type safety:** Literal types for enums, TypedDict support, better IDE autocomplete
- ✅ **Add convenience:** `set()` method (upsert), better batch operations, cleaner API
- ✅ **Schema-driven:** All metadata from FortiOS 7.6 schemas, not hardcoded

---

## Design Principles

### 1. **Schema is Source of Truth**
Everything generated from actual FortiOS schemas - no hardcoded values, no assumptions.

### 2. **Dual Approach (Keep What Works)**
- **API Endpoint Classes** (`address.py`) - Clean CRUD methods with flexible parameters
- **Validation Helpers** (`_validators/address.py`) - Separate, opt-in validation logic

### 3. **Developer Experience First**
- IDE autocomplete with Literal types
- Helpful error messages with suggestions
- Comprehensive docstrings with real help text from schemas
- Both `individual_params` and `payload_dict` approaches

### 4. **Type Safety Without Sacrifice**
- Full type hints for mypy/pyright
- Runtime validation optional (opt-in)
- TypedDict for payload dictionaries
- Overloads for sync/async clarity

### 5. **Future-Proof**
- Version metadata in all generated files
- Delta-based versioning support (future: 7.4, 7.8)
- Easy to regenerate when schemas change

### 6. **Leverage Existing Core Features** ✅ NEW
The `hfortix_core` package already provides production-ready features:
- **Audit logging** via `AuditHandler` protocol
- **Request hooks** via `BeforeRequestHook` and `AfterRequestHook`
- **Dry-run mode** via `read_only=True`
- **Adaptive retry** with backpressure detection
- **Circuit breaker** for resilience
- **Rich exceptions** with context and suggestions

Generators should reference and document these features, not duplicate them.

---

## Old Implementation Analysis

### What Worked Great ✅

**1. Dual Approach Structure:**
```
api/v2/cmdb/firewall/
├── address.py          # API endpoint class (712 lines)
└── _helpers/
    └── address.py      # Validators (779 lines)
```

**2. Flexible Parameter Design:**
```python
# Both approaches supported:
address.post(name="server1", subnet="192.168.1.0 255.255.255.0")
address.post(payload_dict={"name": "server1", "subnet": "..."})
```

**3. Clean Method Signatures:**
- Every field as optional parameter with type hints
- Automatic snake_case → kebab-case conversion
- Support for sync/async via `Union[dict, Coroutine]`

**4. Comprehensive Documentation:**
- Usage examples in class docstring
- Every parameter documented
- Common query parameters explained

**5. Helper Methods:**
- `exists()` - Check if object exists
- Smart async/sync detection

### What Needs Enhancement ❌

**1. Generic Help Text:**
- Docstrings don't use schema `help` field
- Missing field-specific descriptions
- No dependency hints

**2. No Literal Types:**
```python
# Current (weak):
type: str | None = None

# Needed (strong):
type: Literal["ipmask", "iprange", "fqdn", ...] | None = None
```

**3. Validators Hidden:**
- In `_helpers/` folder (not discoverable)
- Not called automatically (users don't know they exist)
- POST and PUT validators nearly identical (duplication)

**4. No TypedDict:**
- `payload_dict: dict[str, Any]` too loose
- No autocomplete for dictionary approach

**5. Limited Field Intelligence:**
- No dependency tracking (e.g., `type=ipmask` requires `subnet`)
- No conflict detection (e.g., `subnet` conflicts with `start-ip`)

---

## Core Package Integration

The `hfortix_core` package already provides production-ready infrastructure that generated code should leverage:

### Available Features (No Need to Implement)

#### 1. **Audit Logging** ✅
```python
# Already available - just document in generated code
from hfortix_core.audit import AuditHandler

class MyAuditHandler:
    def log_operation(self, operation: dict) -> None:
        # operation includes: method, endpoint, data, params, status_code, 
        # duration_ms, success, error, timestamp, request_id, etc.
        pass

fgt = FortiOS("...", token="...", audit_handler=MyAuditHandler())
```

#### 2. **Request Hooks** ✅
```python
# Already available - document for validation use cases
from hfortix_core.hooks import BeforeRequestHook, AfterRequestHook

class ValidationHook:
    def before_request(self, context: dict) -> dict:
        # Validate, transform, or cancel requests
        if not context['data'].get('required_field'):
            raise ValueError("Missing required field!")
        return context

fgt = FortiOS("...", token="...", before_request_hooks=[ValidationHook()])
```

#### 3. **Read-Only Mode (Dry-Run)** ✅
```python
# Already available - perfect for testing
fgt = FortiOS("...", token="...", read_only=True)

# GET works normally, POST/PUT/DELETE are simulated
result = fgt.api.cmdb.firewall.address.post(name="test", ...)  # Not actually sent
```

#### 4. **Adaptive Retry & Circuit Breaker** ✅
```python
# Already available - resilient by default
fgt = FortiOS(
    "...", token="...",
    adaptive_retry=True,              # Smart backoff
    circuit_breaker_threshold=10,     # Open after 10 failures
    circuit_breaker_timeout=30.0,     # Wait 30s before retry
    retry_strategy="exponential",     # or "linear"
    retry_jitter=True,                # Prevent thundering herd
)
```

#### 5. **Rich Exception Handling** ✅
```python
# Already available - context-aware errors
from hfortix_core.exceptions import (
    ResourceNotFoundError,          # 404 errors
    PermissionDeniedError,          # 403 errors
    ValidationError,                # 400 errors
    ResourceConflictError,          # 409 errors
    APIError,                       # Generic with metadata
)

# All exceptions include:
# - http_status, error_code
# - endpoint, method, params (sanitized)
# - hint (suggested resolution)
# - request_id, timestamp
```

### Generator Responsibilities

✅ **Should Do:**
- Reference core features in docstrings
- Document how to use `audit_handler`, `read_only`, hooks
- Leverage existing exception types
- Use `IHTTPClient` protocol (already defined)

❌ **Should NOT Do:**
- Re-implement audit logging
- Re-implement retry logic
- Re-implement circuit breaker
- Re-implement exception sanitization
- Create new base exception classes

### Example: Generated Docstring Should Reference Core Features

```python
def post(...):
    """
    Create a new firewall address object.
    
    ... (field documentation)
    
    Advanced Usage:
        # Audit all operations
        >>> handler = MyAuditHandler()
        >>> fgt = FortiOS("...", token="...", audit_handler=handler)
        >>> fgt.api.cmdb.firewall.address.post(name="test", ...)
        
        # Dry-run mode (test without executing)
        >>> fgt = FortiOS("...", token="...", read_only=True)
        >>> fgt.api.cmdb.firewall.address.post(name="test", ...)  # Simulated
        
        # Validation hook
        >>> def validate(ctx): 
        ...     if not ctx['data'].get('name'):
        ...         raise ValueError("Name required")
        ...     return ctx
        >>> fgt = FortiOS("...", token="...", before_request_hooks=[validate])
    
    Raises:
        ResourceNotFoundError: Object not found (404)
        PermissionDeniedError: Insufficient permissions (403)
        ValidationError: Invalid request data (400)
        ResourceConflictError: Object already exists (409)
    """
```

---

## Query Parameters and .get() Behavior

### Critical Design Decision: .get() Returns All or Specific

**No mkey parameter → Returns ALL results:**
```python
# Get all firewall addresses
addresses = fgt.api.cmdb.firewall.address.get()
# Returns: {"results": [...], "http_status": 200, ...}
```

**With mkey parameter → Returns SPECIFIC object:**
```python
# Get specific address by name
address = fgt.api.cmdb.firewall.address.get(name="server1")
# Returns: {"results": {...}, "http_status": 200, ...}
```

### FortiOS Query Parameters

FortiOS API supports rich query capabilities via URL parameters:

1. **Filtering** - `filter=[key][operator][pattern]`
2. **Sorting** - `sort=[key],[order]`  
3. **Paging** - `start=[index]&count=[max]`
4. **Formatting** - `format=[field1]|[field2]`

**Applied in order:** Filter → Sort → Page → Format

**See:** `FORTIOS_FILTERING.md` for complete documentation.

### Generated .get() Method Signature

All query parameters passed via `**kwargs`:

```python
def get(
    self,
    name: str | None = None,  # mkey parameter (from schema.mkey)
    payload_dict: dict[str, Any] | None = None,
    vdom: str | bool | None = None,
    raw_json: bool = False,
    **kwargs: Any,  # ALL query parameters
) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
    """
    Get address configuration.
    
    Args:
        name: Address name (optional for list, required for specific)
        vdom: Virtual domain name
        raw_json: Return full API response or just results
        **kwargs: Additional query parameters:
            filter: Filter results (e.g., 'type==ipmask')
            sort: Sort results (e.g., 'name,asc')
            start: Starting entry index for paging
            count: Maximum number of entries
            format: Fields to return (e.g., 'name|type')
    
    Query Parameter Examples:
        # Get all addresses
        >>> addresses = fgt.api.cmdb.firewall.address.get()
        
        # Get specific address
        >>> address = fgt.api.cmdb.firewall.address.get(name="server1")
        
        # Get addresses with filtering
        >>> ipmask_addrs = fgt.api.cmdb.firewall.address.get(
        ...     filter="type==ipmask"
        ... )
        
        # Get addresses with complex filter (AND + OR)
        >>> filtered = fgt.api.cmdb.firewall.address.get(
        ...     filter="type==ipmask&filter=name=@server"
        ... )
        
        # Get addresses sorted by name (descending)
        >>> sorted_addrs = fgt.api.cmdb.firewall.address.get(
        ...     sort="name,dsc"
        ... )
        
        # Get addresses with paging (50 results starting at index 10)
        >>> page_addrs = fgt.api.cmdb.firewall.address.get(
        ...     start=10,
        ...     count=50
        ... )
        
        # Get addresses with specific fields only
        >>> minimal_addrs = fgt.api.cmdb.firewall.address.get(
        ...     format="name|type|subnet"
        ... )
        
        # Combine all parameters
        >>> result = fgt.api.cmdb.firewall.address.get(
        ...     filter="type==ipmask",
        ...     sort="name,asc",
        ...     start=0,
        ...     count=100,
        ...     format="name|subnet"
        ... )
    
    For detailed filtering documentation, see:
        docs/fortios/FILTERING_GUIDE.md
    
    Returns:
        API response dictionary (sync) or Coroutine (async)
    """
    params = payload_dict.copy() if payload_dict else {}
    
    # Build endpoint based on mkey presence
    if name:
        endpoint = f"/firewall/address/{name}"
    else:
        endpoint = "/firewall/address"
    
    # Add all query parameters from kwargs
    params.update(kwargs)
    
    return self._client.get("cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json)
```

### Implementation Notes

1. ✅ **mkey-specific parameter** (name, policyid, seq_num, etc. from schema)
2. ✅ **No mkey → list all, With mkey → get specific**
3. ✅ **All query params via `**kwargs`** (filter, sort, start, count, format)
4. ✅ **Document query capabilities in docstrings**
5. ✅ **Reference FORTIOS_FILTERING.md** for complete docs
6. ❌ **No helper methods for v0.5.0** (raw FortiOS syntax only)

**Future (v0.6.0+):** Consider Python-friendly query builder:
```python
# Future enhancement - not in scope for v0.5.0
addresses = fgt.api.cmdb.firewall.address.query() \
    .filter(type="ipmask") \
    .filter(name__contains="server") \
    .sort("name", ascending=True) \
    .limit(100) \
    .execute()
```

---

## Enhanced Architecture

### File Structure (Per Endpoint)

```
api/v2/cmdb/firewall/
├── address.py              # API endpoint class (ENHANCED)
├── address.pyi             # Type stubs with Literal types (NEW)
└── _validators/            # Renamed from _helpers (clearer)
    ├── __init__.py
    ├── address.py          # Validation functions (ENHANCED)
    └── address_types.py    # TypedDict + Literal exports (NEW)
```

### Key Enhancements

1. **Type Stubs (`.pyi`)** - Literal types for perfect IDE autocomplete
2. **TypedDict** - Type-safe dictionary approach
3. **Smart Validators** - Context-aware with field dependencies
4. **HELP_TEXT Constants** - Expose schema help text
5. **set() Method** - Idempotent create-or-update (upsert)
6. **Better Error Messages** - Suggestions, did-you-mean, dependency hints
7. **Query Parameters** - Full FortiOS filtering/sorting/paging/formatting support

---

## Generator Components

### 1. Schema Downloader (`download_schemas.py`)

**Purpose:** Fetch all schemas from FortiGate 7.6

**Process:**
```python
# For each endpoint (548+ total):
# GET /api/v2/cmdb/{category}/{endpoint}?action=schema&vdom=root

# Store as:
# .dev/schemas/v7.6/firewall/address.json
# .dev/schemas/v7.6/system/interface.json
# ... etc

# Create index:
# .dev/schemas/v7.6/index.json
```

**Features:**
- Progress tracking
- Error handling with retry
- Schema validation
- Automatic categorization

---

### 2. Schema Parser (`schema_parser.py`)

**Purpose:** Extract all metadata from schema JSON

**Extracts:**
- Field names, types, constraints (min/max, size)
- Required fields with context
- Enum values with descriptions
- Default values
- Help text for every field
- Nested objects (child tables)
- Datasources (cross-references)
- mkey (primary key) information

**Output:**
```python
{
    "endpoint": "firewall.address",
    "path": "/api/v2/cmdb/firewall/address",
    "mkey": "name",
    "fields": {
        "name": {
            "type": "string",
            "required": True,
            "max_length": 79,
            "help": "Address name.",
        },
        "type": {
            "type": "option",
            "required": False,
            "default": "ipmask",
            "options": [
                {"value": "ipmask", "help": "IP address and netmask"},
                {"value": "iprange", "help": "Range of IP addresses"},
                # ...
            ],
            "help": "Type of address.",
        },
        # ... all fields
    },
    "dependencies": {
        "type": {
            "ipmask": {"required": ["subnet"], "conflicts": ["start-ip", "end-ip"]},
            "iprange": {"required": ["start-ip", "end-ip"], "conflicts": ["subnet"]},
            # ...
        }
    }
}
```

---

### 3. API Endpoint Generator (`generate_endpoint.py`)

**Purpose:** Generate clean API endpoint classes

**Generates:**

**3.1. Class Docstring:**
```python
"""
FortiOS CMDB - Firewall Address

Configuration endpoint for managing firewall address objects.

API Endpoints:
    GET    /api/v2/cmdb/firewall/address
    POST   /api/v2/cmdb/firewall/address
    PUT    /api/v2/cmdb/firewall/address/{name}
    DELETE /api/v2/cmdb/firewall/address/{name}

Example Usage:
    >>> # Create or update address (idempotent)
    >>> result = fgt.api.cmdb.firewall.address.set(
    ...     name="server1",
    ...     type="ipmask",
    ...     subnet="192.168.1.100 255.255.255.255"
    ... )
    
    >>> # Check if exists
    >>> if fgt.api.cmdb.firewall.address.exists("server1"):
    ...     print("Address exists")
    
    >>> # List all addresses
    >>> addresses = fgt.api.cmdb.firewall.address.get()

Schema Version: FortiOS 7.6
Generated: 2026-01-03
"""
```

**3.2. CRUD Methods with Enhanced Docstrings:**
```python
def post(
    self,
    payload_dict: "AddressConfig | dict[str, Any] | None" = None,
    # Schema help: Address name
    name: str | None = None,
    # Schema help: Type of address. Determines how the address is defined.
    # Valid: ipmask, iprange, fqdn, geography, wildcard, dynamic, 
    #        interface-subnet, mac, route-tag
    # Default: ipmask
    type: str | None = None,  # See address.pyi for Literal type
    # Schema help: IP address and subnet mask of address.
    # Required when: type=ipmask
    # Format: <ip> <netmask> (e.g., 192.168.1.0 255.255.255.0)
    subnet: str | None = None,
    # ... all other fields with schema help comments
) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
    """
    Create a new firewall address object.
    
    Required Fields:
        name: Address name (max 79 chars)
    
    Conditional Requirements:
        When type=ipmask: subnet is required
        When type=iprange: start-ip and end-ip are required
        When type=fqdn: fqdn is required
    
    Common Patterns:
        # IP/Mask address
        >>> address.post(name="net1", type="ipmask", 
        ...              subnet="192.168.1.0 255.255.255.0")
        
        # IP range
        >>> address.post(name="range1", type="iprange",
        ...              start_ip="10.0.0.1", end_ip="10.0.0.254")
        
        # FQDN
        >>> address.post(name="website", type="fqdn",
        ...              fqdn="example.com")
    
    Returns:
        API response dictionary (sync) or Coroutine (async)
    """
```

**3.3. NEW: set() Method (Upsert):**
```python
def set(
    self,
    name: str,
    payload_dict: "AddressConfig | dict[str, Any] | None" = None,
    # ... all same parameters as post/put ...
    vdom: str | bool | None = None,
    raw_json: bool = False,
    **kwargs: Any,
) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
    """
    Create or update a firewall address object (idempotent operation).
    
    This method automatically determines whether to create (POST) or 
    update (PUT) based on whether the object currently exists.
    
    Safe to run multiple times - idempotent behavior ensures the object
    exists with the specified configuration regardless of current state.
    
    Args:
        name: Address name (required)
        payload_dict: Optional dictionary of all parameters
        ... (all other parameters)
    
    Returns:
        API response dictionary (sync) or Coroutine (async)
    
    Example (Sync):
        >>> # Creates if doesn't exist, updates if exists
        >>> result = fgt.api.cmdb.firewall.address.set(
        ...     name="server1",
        ...     subnet="192.168.1.100 255.255.255.255"
        ... )
        
    Example (Async):
        >>> result = await fgt.api.cmdb.firewall.address.set(
        ...     name="server1",
        ...     subnet="192.168.1.100 255.255.255.255"
        ... )
    
    Note:
        Uses exists() + put()/post() internally. Makes 2 API calls:
        1. GET to check existence
        2. PUT (if exists) or POST (if not)
    """
    import inspect
    from typing import Any, cast
    
    # Check if object exists
    exists_result = self.exists(name=name, vdom=vdom)
    
    # Handle async mode
    if inspect.iscoroutine(exists_result):
        async def _async():
            obj_exists = await cast(Coroutine[Any, Any, bool], exists_result)
            if obj_exists:
                return await self.put(
                    name=name, payload_dict=payload_dict, vdom=vdom,
                    raw_json=raw_json, **kwargs
                )
            else:
                return await self.post(
                    name=name, payload_dict=payload_dict, vdom=vdom,
                    raw_json=raw_json, **kwargs
                )
        return _async()
    
    # Sync mode
    if exists_result:
        return self.put(
            name=name, payload_dict=payload_dict, vdom=vdom,
            raw_json=raw_json, **kwargs
        )
    else:
        return self.post(
            name=name, payload_dict=payload_dict, vdom=vdom,
            raw_json=raw_json, **kwargs
        )
```

---

### 4. Type Stub Generator (`generate_type_stubs.py`)

**Purpose:** Generate `.pyi` files with Literal types for IDE autocomplete

**Generates:**

```python
# address.pyi
from typing import Literal, TypedDict, Union, Any
from collections.abc import Coroutine

# Literal type aliases for enums
AddressType = Literal[
    "ipmask",           # IP address and netmask
    "iprange",          # Range of IP addresses
    "fqdn",             # Fully qualified domain name
    "geography",        # Country-based address
    "wildcard",         # IP with wildcard netmask
    "dynamic",          # Dynamic address object
    "interface-subnet", # Interface subnet
    "mac",              # MAC address
    "route-tag",        # Route tag address
]

AddressSubType = Literal[
    "sdn", "clearpass-spt", "fsso", "rsso", "ems-tag",
    "fortivoice-tag", "fortinac-tag", "swc-tag",
    "device-identification", "external-resource", "obsolete"
]

# ... more Literal types for all enums

# TypedDict for type-safe dictionary usage
class AddressConfig(TypedDict, total=False):
    """Type-safe configuration for firewall address objects."""
    name: str                    # Address name
    type: AddressType            # Type of address
    subnet: str                  # IP and subnet mask (for type=ipmask)
    start_ip: str                # Start IP (for type=iprange)
    end_ip: str                  # End IP (for type=iprange)
    fqdn: str                    # FQDN (for type=fqdn)
    # ... all other fields with precise types

# Method stubs with Literal types
class Address:
    def post(
        self,
        payload_dict: AddressConfig | dict[str, Any] | None = None,
        name: str | None = None,
        type: AddressType | None = None,  # <-- Literal type here!
        subnet: str | None = None,
        # ... all parameters
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    # ... all other methods
```

---

### 5. Validator Generator (`generate_validators.py`)

**Purpose:** Generate enhanced validation functions with context

**Generates:**

**5.1. Help Text Constants:**
```python
# _validators/address.py

# Schema-derived help text for all fields
HELP_TEXT = {
    "name": "Address name.",
    "type": "Type of address. Determines how the address is defined.",
    "subnet": "IP address and subnet mask of address. Required when type=ipmask. Format: <ip> <netmask>",
    "start-ip": "First IP address (inclusive) in the range for the address. Required when type=iprange.",
    # ... all fields
}

# Export for use in applications
__all__ = ["HELP_TEXT", "validate_address_post", "validate_address_put", ...]
```

**5.2. Enum Values with Descriptions:**
```python
# Valid enum values with inline help
VALID_TYPE_VALUES = [
    "ipmask",           # IP address and netmask
    "iprange",          # Range of IP addresses
    "fqdn",             # Fully qualified domain name
    "geography",        # Country-based address
    "wildcard",         # IP with wildcard netmask
    "dynamic",          # Dynamic address object
    "interface-subnet", # Interface subnet
    "mac",              # MAC address
    "route-tag",        # Route tag address
]
```

**5.3. Field Dependencies and Conflicts:**
```python
# Smart dependency tracking from schema analysis
FIELD_DEPENDENCIES = {
    "type": {
        "ipmask": {
            "required": ["subnet"],
            "optional": [],
            "conflicts": ["start-ip", "end-ip", "fqdn", "wildcard-fqdn", "country"],
            "help": "When type=ipmask, you must provide 'subnet' (format: <ip> <netmask>)",
        },
        "iprange": {
            "required": ["start-ip", "end-ip"],
            "optional": [],
            "conflicts": ["subnet", "fqdn", "wildcard-fqdn", "country"],
            "help": "When type=iprange, you must provide both 'start-ip' and 'end-ip'",
        },
        "fqdn": {
            "required": ["fqdn"],
            "optional": ["cache-ttl"],
            "conflicts": ["subnet", "start-ip", "end-ip", "country"],
            "help": "When type=fqdn, you must provide 'fqdn' (fully qualified domain name)",
        },
        "geography": {
            "required": ["country"],
            "optional": [],
            "conflicts": ["subnet", "start-ip", "end-ip", "fqdn"],
            "help": "When type=geography, you must provide 'country' (ISO 3166-1 alpha-2 code)",
        },
        # ... all type values
    }
}
```

**5.4. Smart Validation Functions:**
```python
def validate_address_post(payload: dict[str, Any]) -> tuple[bool, str | None]:
    """
    Validate POST request payload with context-aware checking.
    
    Performs multi-stage validation:
    1. Required fields validation
    2. Field dependency validation (type-specific)
    3. Conflict detection
    4. Value validation (enums, ranges, formats)
    
    Args:
        payload: The request payload to validate
        
    Returns:
        Tuple of (is_valid, error_message)
        
    Example:
        >>> is_valid, error = validate_address_post({
        ...     "name": "server1",
        ...     "type": "ipmask",
        ...     "subnet": "192.168.1.0 255.255.255.0"
        ... })
        >>> if not is_valid:
        ...     print(f"Validation failed: {error}")
    """
    if not payload:
        return (False, "Payload cannot be empty")
    
    # Stage 1: Required fields
    if "name" not in payload:
        return (False, "Missing required field 'name'. Help: Address name (max 79 chars)")
    
    # Stage 2: Field dependencies based on 'type'
    address_type = payload.get("type", "ipmask")  # default
    if address_type in FIELD_DEPENDENCIES:
        deps = FIELD_DEPENDENCIES[address_type]
        
        # Check required fields for this type
        for field in deps["required"]:
            if field not in payload:
                return (
                    False,
                    f"Missing required field '{field}' for type='{address_type}'. "
                    f"{deps['help']}"
                )
        
        # Check for conflicts
        for field in deps["conflicts"]:
            if field in payload and payload.get(field) is not None:
                return (
                    False,
                    f"Field '{field}' conflicts with type='{address_type}'. "
                    f"Remove '{field}' or change type. {deps['help']}"
                )
    
    # Stage 3: Validate type enum
    if "type" in payload:
        value = payload["type"]
        if value not in VALID_TYPE_VALUES:
            # Smart suggestion
            suggestion = _get_close_match(value, VALID_TYPE_VALUES)
            if suggestion:
                return (
                    False,
                    f"Invalid type '{value}'. Did you mean '{suggestion}'? "
                    f"Valid values: {', '.join(VALID_TYPE_VALUES)}"
                )
            else:
                return (
                    False,
                    f"Invalid type '{value}'. Must be one of: {', '.join(VALID_TYPE_VALUES)}"
                )
    
    # Stage 4: Validate string lengths, ranges, etc.
    # ... (existing validation logic)
    
    return (True, None)


def _get_close_match(value: str, valid_values: list[str]) -> str | None:
    """Find closest match using fuzzy matching (did-you-mean)."""
    from difflib import get_close_matches
    matches = get_close_matches(value, valid_values, n=1, cutoff=0.6)
    return matches[0] if matches else None
```

---

### 6. TypedDict Generator (`generate_typeddict.py`)

**Purpose:** Generate TypedDict classes for type-safe dictionary usage

**Generates:**

```python
# _validators/address_types.py
from typing import TypedDict, Literal

# Import Literal type aliases from stub file
AddressType = Literal["ipmask", "iprange", "fqdn", "geography", ...]
AddressSubType = Literal["sdn", "clearpass-spt", "fsso", ...]

class AddressConfig(TypedDict, total=False):
    """
    Type-safe configuration dictionary for firewall address objects.
    
    All fields are optional (total=False) to allow partial updates.
    Use for type checking when passing dictionaries to post()/put()/set().
    
    Example:
        >>> config: AddressConfig = {
        ...     "name": "server1",
        ...     "type": "ipmask",
        ...     "subnet": "192.168.1.100 255.255.255.255"
        ... }
        >>> result = fgt.api.cmdb.firewall.address.post(payload_dict=config)
    """
    # Primary fields
    name: str                    # Address name (max 79 chars)
    type: AddressType            # Type of address (default: ipmask)
    
    # Type-specific fields
    subnet: str                  # IP and subnet mask (required for type=ipmask)
    start_ip: str                # Start IP (required for type=iprange)
    end_ip: str                  # End IP (required for type=iprange)
    fqdn: str                    # FQDN (required for type=fqdn)
    country: str                 # Country code (required for type=geography)
    
    # Optional fields
    comment: str                 # Comment (max 255 chars)
    color: int                   # GUI icon color (0-32)
    uuid: str                    # UUID (auto-assigned)
    
    # ... all other fields with precise types and descriptions
```

---

## Feature Enhancements

### Priority 1: Must Have (v0.5.0)

#### 1. **set() Method - Idempotent Upsert** ⭐⭐⭐
**What:** Create-or-update method that checks existence automatically

**Why:** Infrastructure-as-Code workflows need idempotent operations

**Example:**
```python
# Old way (manual):
if fgt.api.cmdb.firewall.address.exists("server1"):
    result = fgt.api.cmdb.firewall.address.put(name="server1", subnet="...")
else:
    result = fgt.api.cmdb.firewall.address.post(name="server1", subnet="...")

# New way (automatic):
result = fgt.api.cmdb.firewall.address.set(name="server1", subnet="...")
```

#### 2. **Smart Validation with Field Dependencies** ⭐⭐⭐
**What:** Context-aware validation that understands field relationships

**Why:** Prevent common mistakes, provide helpful guidance

**Example:**
```python
# User tries:
address.post(name="test", type="ipmask", start_ip="10.0.0.1")

# Old error:
# "Invalid payload"

# New error:
# "Field 'start-ip' conflicts with type='ipmask'. When type=ipmask, you must 
#  provide 'subnet' field instead. Remove 'start-ip' or change type to 'iprange'."
```

#### 3. **Better Error Messages with Suggestions** ⭐⭐⭐
**What:** Fuzzy matching for typos, did-you-mean suggestions

**Why:** Faster development, fewer docs lookups

**Example:**
```python
# User types:
address.post(name="test", type="ipmak")

# Old error:
# "Invalid type 'ipmak'. Must be one of: ipmask, iprange, ..."

# New error:
# "Invalid type 'ipmak'. Did you mean 'ipmask'? 
#  Valid values: ipmask, iprange, fqdn, geography, wildcard, dynamic, 
#  interface-subnet, mac, route-tag"
```

#### 4. **Literal Types for Enums** ⭐⭐⭐
**What:** Type stubs with Literal types for perfect autocomplete

**Why:** IDE shows valid values, catches errors before runtime

**Example:**
```python
# In IDE, typing "type=" shows dropdown with:
# - ipmask
# - iprange
# - fqdn
# - geography
# ... etc

# Mypy catches invalid values:
address.post(name="test", type="invalid")  # Error: Literal["ipmask", "iprange", ...] expected
```

#### 5. **Schema Help Text Integration** ⭐⭐⭐
**What:** All docstrings and comments use actual schema help text

**Why:** Accurate, detailed documentation from source of truth

**Example:**
```python
def post(
    self,
    # Schema help: IP address and subnet mask of address.
    # Required when: type=ipmask
    # Format: <ip> <netmask> (e.g., 192.168.1.0 255.255.255.0)
    subnet: str | None = None,
```

---

### Priority 2: Nice to Have (v0.6.0)

#### 6. **Query Builder for Filtering** ⭐⭐
**What:** Fluent API for building filter expressions

**Why:** Filter syntax is cryptic and error-prone

**Example:**
```python
# Current (error-prone):
addresses = fgt.api.cmdb.firewall.address.get(
    filter="type==ipmask,subnet@@192.168.1"
)

# Future (type-safe):
addresses = fgt.api.cmdb.firewall.address.query() \
    .filter(type="ipmask") \
    .filter(subnet__contains="192.168.1") \
    .sort("name", ascending=True) \
    .limit(100) \
    .execute()
```

#### 7. **Batch Operations** ⭐⭐
**What:** Process multiple objects efficiently

**Why:** Common use case for configuration management

**Example:**
```python
addresses = [
    {"name": "server1", "subnet": "192.168.1.1 255.255.255.255"},
    {"name": "server2", "subnet": "192.168.1.2 255.255.255.255"},
    {"name": "server3", "subnet": "192.168.1.3 255.255.255.255"},
]

# Creates or updates all
results = fgt.api.cmdb.firewall.address.set_batch(
    addresses,
    continue_on_error=True
)
```

#### 8. **Export/Import Configuration** ⭐
**What:** Save and restore configurations to/from files

**Why:** Backup, migration, version control

**Example:**
```python
# Export current config
fgt.api.cmdb.firewall.address.export_config("addresses_backup.json")

# Import from file (merge or replace)
fgt.api.cmdb.firewall.address.import_config(
    "addresses_backup.json",
    merge=True  # Keep existing, add new
)
```

#### 9. **Schema Introspection at Runtime** ⭐⭐
**What:** Access schema metadata programmatically

**Why:** Dynamic UIs, API explorers, automated testing

**Example:**
```python
# Get schema for endpoint
schema = fgt.api.cmdb.firewall.address.schema

print(schema["fields"]["type"]["options"])
# [
#   {"value": "ipmask", "help": "IP address and netmask"},
#   {"value": "iprange", "help": "Range of IP addresses"},
#   ...
# ]
```

---

### Priority 3: Future Enhancements (v0.7.0+)

#### 10. **Change Detection/Diff** ⭐
**What:** Preview changes before applying

**Why:** Safe updates, audit trails

**Example:**
```python
diff = fgt.api.cmdb.firewall.address.diff(
    name="server1",
    payload_dict={"subnet": "192.168.2.0 255.255.255.0", "comment": "Updated"}
)

print(diff)
# {
#   "modified": {
#     "subnet": {"old": "192.168.1.0 255.255.255.0", "new": "192.168.2.0 255.255.255.0"}
#   },
#   "added": {
#     "comment": "Updated"
#   },
#   "unchanged": {
#     "name": "server1",
#     "type": "ipmask"
#   }
# }
```

#### 11. **Async Batch Operations** ⭐
**What:** Process multiple requests concurrently in async mode

**Why:** Faster bulk operations

**Example:**
```python
# Process 100 addresses concurrently (10 at a time)
results = await fgt.api.cmdb.firewall.address.set_concurrent(
    addresses,
    max_concurrent=10
)
```

#### 12. **Validation Modes** ⭐
**What:** Choose strictness level (strict, warn, off)

**Why:** Development vs production needs

**Example:**
```python
# Strict mode (default) - raise on validation errors
address = Address(client, validation_mode="strict")

# Warn mode - log warnings but continue
address = Address(client, validation_mode="warn")

# Off mode - skip validation entirely
address = Address(client, validation_mode="off")
```

#### 13. **Field Value Suggestions** ⭐⭐
**What:** Show common/valid values for fields

**Why:** Helpful for complex fields

**Example:**
```python
# Get suggestions for subnet field
suggestions = fgt.api.cmdb.firewall.address.suggest("subnet")
# Returns:
# {
#   "format": "<ip> <netmask>",
#   "examples": [
#     "192.168.1.0 255.255.255.0",
#     "10.0.0.0 255.255.255.0",
#     "172.16.0.0 255.255.0.0"
#   ],
#   "help": "IP address and subnet mask of address."
# }
```

#### 14. **Relationship Traversal** ⭐⭐
**What:** Follow datasource references automatically

**Why:** Understand object relationships

**Example:**
```python
# Get address and its referenced objects
address = fgt.api.cmdb.firewall.address.get(
    name="server1",
    expand_references=True
)

# Returns address with expanded 'interface' reference:
# {
#   "name": "server1",
#   "interface": {
#     "name": "port1",
#     "ip": "192.168.1.1",
#     "type": "physical",
#     ...  # Full interface object
#   }
# }
```

#### 15. **Transaction Support** ⭐
**What:** Group multiple operations, rollback on failure

**Why:** Atomic configuration changes

**Example:**
```python
with fgt.api.transaction() as txn:
    txn.add(fgt.api.cmdb.firewall.address.post(name="addr1", ...))
    txn.add(fgt.api.cmdb.firewall.address.post(name="addr2", ...))
    txn.add(fgt.api.cmdb.firewall.policy.post(name="policy1", ...))
    # If any fails, all rollback

# Or async:
async with fgt.api.transaction() as txn:
    await txn.add(...)
```

---

## Generated Code Structure

### Complete Example: firewall.address

**Directory Structure:**
```
packages/fortios/hfortix_fortios/api/v2/cmdb/firewall/
├── __init__.py
├── address.py              # Main API class
├── address.pyi             # Type stubs
└── _validators/
    ├── __init__.py
    ├── address.py          # Validation functions
    └── address_types.py    # TypedDict definitions
```

**Generated Metadata:**
```python
# At top of each generated file:
"""
Auto-generated from FortiOS 7.6 schema.
Generated: 2026-01-03 10:30:00 UTC
Schema Hash: a1b2c3d4e5f6...
Generator Version: 0.5.0

DO NOT EDIT MANUALLY - Regenerate from schema
"""
```

---

## Implementation Roadmap

### Phase 1: Foundation (Week 1)
- [ ] Create schema downloader script
- [ ] Build enhanced schema parser
- [ ] Design generator templates
- [ ] Set up project structure

### Phase 2: Core Generators (Week 2)
- [ ] Implement API endpoint generator
- [ ] Implement type stub generator
- [ ] Implement validator generator
- [ ] Implement TypedDict generator

### Phase 3: Testing (Week 3)
- [ ] Generate firewall.address (proof of concept)
- [ ] Test all CRUD operations
- [ ] Verify validators
- [ ] Check type hints with mypy
- [ ] Iterate and refine

### Phase 4: Full Generation (Week 4)
- [ ] Generate all 548+ CMDB endpoints
- [ ] Update __init__.py files
- [ ] Create comprehensive tests
- [ ] Update documentation

### Phase 5: Enhancements (Week 5)
- [ ] Add set() method
- [ ] Add smart validation
- [ ] Add better error messages
- [ ] Add schema introspection

### Phase 6: Release (Week 6)
- [ ] Version 0.5.0 release
- [ ] Update examples
- [ ] Migration guide
- [ ] Announcement

---

## Examples

### Example 1: Basic Usage with set()

```python
from hfortix_fortios import FortiOS

fgt = FortiOS(host="192.168.1.99", token="your-token")

# Idempotent create-or-update
result = fgt.api.cmdb.firewall.address.set(
    name="server1",
    type="ipmask",
    subnet="192.168.1.100 255.255.255.255",
    comment="Web server"
)

# Check existence
if fgt.api.cmdb.firewall.address.exists("server1"):
    print("Address created successfully")
```

### Example 2: Type-Safe Dictionary Approach

```python
from hfortix_fortios import FortiOS
from hfortix_fortios.api.v2.cmdb.firewall._validators.address_types import AddressConfig

fgt = FortiOS(host="192.168.1.99", token="your-token")

# Type-safe dictionary (IDE autocomplete works!)
config: AddressConfig = {
    "name": "server1",
    "type": "ipmask",  # IDE shows valid values
    "subnet": "192.168.1.100 255.255.255.255",
    "comment": "Web server"
}

result = fgt.api.cmdb.firewall.address.set(payload_dict=config)
```

### Example 3: Smart Validation Errors

```python
# Attempt with conflicting fields
try:
    result = fgt.api.cmdb.firewall.address.post(
        name="test",
        type="ipmask",
        start_ip="10.0.0.1",  # Conflicts with type=ipmask
        end_ip="10.0.0.254"
    )
except ValueError as e:
    print(e)
    # Output:
    # "Field 'start-ip' conflicts with type='ipmask'. When type=ipmask, 
    #  you must provide 'subnet' field. Remove 'start-ip' or change type 
    #  to 'iprange'."
```

### Example 4: Async Usage

```python
import asyncio
from hfortix_fortios import FortiOS

async def main():
    fgt = FortiOS(host="192.168.1.99", token="your-token", async_mode=True)
    
    # All methods work with await
    result = await fgt.api.cmdb.firewall.address.set(
        name="server1",
        subnet="192.168.1.100 255.255.255.255"
    )
    
    exists = await fgt.api.cmdb.firewall.address.exists("server1")
    print(f"Exists: {exists}")

asyncio.run(main())
```

### Example 5: Batch Operations (Future)

```python
# Create multiple addresses efficiently
addresses = [
    {"name": f"server{i}", "subnet": f"192.168.1.{i} 255.255.255.255"}
    for i in range(1, 11)
]

results = fgt.api.cmdb.firewall.address.set_batch(
    addresses,
    continue_on_error=True
)

# Check results
for i, result in enumerate(results):
    if result.get("status") == "success":
        print(f"✓ {addresses[i]['name']} created/updated")
    else:
        print(f"✗ {addresses[i]['name']} failed: {result.get('error')}")
```

---

## Summary

This design preserves the excellent dual approach from the old implementation while adding significant enhancements:

**Preserved:**
- ✅ Clean API class structure
- ✅ Flexible parameter design (individual params + payload_dict)
- ✅ Comprehensive documentation
- ✅ Async/sync support
- ✅ exists() method

**Enhanced:**
- 🆕 set() method for idempotent operations
- 🆕 Literal types for perfect IDE autocomplete
- 🆕 TypedDict for type-safe dictionaries
- 🆕 Smart validation with field dependencies
- 🆕 Better error messages with suggestions
- 🆕 Schema help text throughout
- 🆕 HELP_TEXT constants for runtime access
- 🆕 Context-aware validation

**Future:**
- 🔮 Query builder
- 🔮 Batch operations
- 🔮 Export/import
- 🔮 Schema introspection
- 🔮 Many more enhancements

This approach ensures we keep what worked great while making the library even more powerful and user-friendly!
