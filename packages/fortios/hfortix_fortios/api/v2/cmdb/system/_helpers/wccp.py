"""Validation helpers for system/wccp - Auto-generated"""

from typing import Any, TypedDict, NotRequired, Literal

# Import common validators from central _helpers module
from hfortix_fortios._helpers import (
    validate_enable_disable,
    validate_integer_range,
    validate_string_length,
    validate_port_number,
    validate_ip_address,
    validate_ipv6_address,
    validate_mac_address,
)

# ============================================================================
# Required Fields Validation
# Auto-generated from schema
# ============================================================================

# ⚠️  IMPORTANT: FortiOS schemas have known issues with required field marking:

# Do NOT use this list for strict validation - test with the actual FortiOS API!

# Fields marked as required (after filtering false positives)
REQUIRED_FIELDS = [
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "service-id": "",
    "router-id": "0.0.0.0",
    "cache-id": "0.0.0.0",
    "group-address": "0.0.0.0",
    "server-list": "",
    "router-list": "",
    "ports-defined": "",
    "server-type": "forward",
    "ports": "",
    "authentication": "disable",
    "forward-method": "GRE",
    "cache-engine-method": "GRE",
    "service-type": "auto",
    "primary-hash": "dst-ip",
    "priority": 0,
    "protocol": 0,
    "assignment-weight": 0,
    "assignment-bucket-format": "cisco-implementation",
    "return-method": "GRE",
    "assignment-method": "HASH",
    "assignment-srcaddr-mask": "0.0.23.65",
    "assignment-dstaddr-mask": "0.0.0.0",
}

# ============================================================================
# Deprecated Fields
# Auto-generated from schema - warns users about deprecated fields
# ============================================================================

# Deprecated fields with migration guidance
DEPRECATED_FIELDS = {
}

# ============================================================================
# Field Metadata (Type Information & Descriptions)
# Auto-generated from schema - use for IDE autocomplete and documentation
# ============================================================================

# Field types mapping
FIELD_TYPES = {
    "service-id": "string",  # Service ID.
    "router-id": "ipv4-address",  # IP address known to all cache engines. If all cache engines 
    "cache-id": "ipv4-address",  # IP address known to all routers. If the addresses are the sa
    "group-address": "ipv4-address-multicast",  # IP multicast address used by the cache routers. For the Fort
    "server-list": "user",  # IP addresses and netmasks for up to four cache servers.
    "router-list": "user",  # IP addresses of one or more WCCP routers.
    "ports-defined": "option",  # Match method.
    "server-type": "option",  # Cache server type.
    "ports": "user",  # Service ports.
    "authentication": "option",  # Enable/disable MD5 authentication.
    "password": "password",  # Password for MD5 authentication.
    "forward-method": "option",  # Method used to forward traffic to the cache servers.
    "cache-engine-method": "option",  # Method used to forward traffic to the routers or to return t
    "service-type": "option",  # WCCP service type used by the cache server for logical inter
    "primary-hash": "option",  # Hash method.
    "priority": "integer",  # Service priority.
    "protocol": "integer",  # Service protocol.
    "assignment-weight": "integer",  # Assignment of hash weight/ratio for the WCCP cache engine.
    "assignment-bucket-format": "option",  # Assignment bucket format for the WCCP cache engine.
    "return-method": "option",  # Method used to decline a redirected packet and return it to 
    "assignment-method": "option",  # Hash key assignment preference.
    "assignment-srcaddr-mask": "ipv4-netmask-any",  # Assignment source address mask.
    "assignment-dstaddr-mask": "ipv4-netmask-any",  # Assignment destination address mask.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "service-id": "Service ID.",
    "router-id": "IP address known to all cache engines. If all cache engines connect to the same FortiGate interface, use the default 0.0.0.0.",
    "cache-id": "IP address known to all routers. If the addresses are the same, use the default 0.0.0.0.",
    "group-address": "IP multicast address used by the cache routers. For the FortiGate to ignore multicast WCCP traffic, use the default 0.0.0.0.",
    "server-list": "IP addresses and netmasks for up to four cache servers.",
    "router-list": "IP addresses of one or more WCCP routers.",
    "ports-defined": "Match method.",
    "server-type": "Cache server type.",
    "ports": "Service ports.",
    "authentication": "Enable/disable MD5 authentication.",
    "password": "Password for MD5 authentication.",
    "forward-method": "Method used to forward traffic to the cache servers.",
    "cache-engine-method": "Method used to forward traffic to the routers or to return to the cache engine.",
    "service-type": "WCCP service type used by the cache server for logical interception and redirection of traffic.",
    "primary-hash": "Hash method.",
    "priority": "Service priority.",
    "protocol": "Service protocol.",
    "assignment-weight": "Assignment of hash weight/ratio for the WCCP cache engine.",
    "assignment-bucket-format": "Assignment bucket format for the WCCP cache engine.",
    "return-method": "Method used to decline a redirected packet and return it to the FortiGate unit.",
    "assignment-method": "Hash key assignment preference.",
    "assignment-srcaddr-mask": "Assignment source address mask.",
    "assignment-dstaddr-mask": "Assignment destination address mask.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "service-id": {"type": "string", "max_length": 3},
    "priority": {"type": "integer", "min": 0, "max": 255},
    "protocol": {"type": "integer", "min": 0, "max": 255},
    "assignment-weight": {"type": "integer", "min": 0, "max": 255},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
}


# Valid enum values from API documentation
VALID_BODY_PORTS_DEFINED = [
    "source",  # Source port match.
    "destination",  # Destination port match.
]
VALID_BODY_SERVER_TYPE = [
    "forward",  # Forward server.
    "proxy",  # Proxy server.
]
VALID_BODY_AUTHENTICATION = [
    "enable",  # Enable MD5 authentication.
    "disable",  # Disable MD5 authentication.
]
VALID_BODY_FORWARD_METHOD = [
    "GRE",  # GRE encapsulation.
    "L2",  # L2 rewrite.
    "any",  # GRE or L2.
]
VALID_BODY_CACHE_ENGINE_METHOD = [
    "GRE",  # GRE encapsulation.
    "L2",  # L2 rewrite.
]
VALID_BODY_SERVICE_TYPE = [
    "auto",  # auto
    "standard",  # Standard service.
    "dynamic",  # Dynamic service.
]
VALID_BODY_PRIMARY_HASH = [
    "src-ip",  # Source IP hash.
    "dst-ip",  # Destination IP hash.
    "src-port",  # Source port hash.
    "dst-port",  # Destination port hash.
]
VALID_BODY_ASSIGNMENT_BUCKET_FORMAT = [
    "wccp-v2",  # WCCP-v2 bucket format.
    "cisco-implementation",  # Cisco bucket format.
]
VALID_BODY_RETURN_METHOD = [
    "GRE",  # GRE encapsulation.
    "L2",  # L2 rewrite.
    "any",  # GRE or L2.
]
VALID_BODY_ASSIGNMENT_METHOD = [
    "HASH",  # HASH assignment method.
    "MASK",  # MASK assignment method.
    "any",  # HASH or MASK.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_system_wccp_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for system/wccp."""
    # Validate query parameters if present
    if "action" in params:
        value = params.get("action")
        if value and value not in VALID_QUERY_ACTION:
            return (
                False,
                f"Invalid query parameter 'action'='{value}'. Must be one of: {', '.join(VALID_QUERY_ACTION)}",
            )

    return (True, None)


# ============================================================================
# POST Validation
# ============================================================================


def validate_required_fields(payload: dict) -> tuple[bool, str | None]:
    """Validate required fields for system/wccp."""
    # Check always-required fields
    missing_fields = []
    for field in REQUIRED_FIELDS:
        if field not in payload:
            missing_fields.append(field)
    
    if missing_fields:
        # Build enhanced error message
        error_parts = [f"Missing required field(s): {', '.join(missing_fields)}"]
        
        # Add descriptions for first few missing fields
        for field in missing_fields[:3]:
            desc = FIELD_DESCRIPTIONS.get(field)
            if desc:
                error_parts.append(f"  • {field}: {desc}")
        
        if len(missing_fields) > 3:
            error_parts.append(f"  ... and {len(missing_fields) - 3} more")
        
        return (False, "\n".join(error_parts))

    return (True, None)


def validate_system_wccp_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new system/wccp object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "ports-defined" in payload:
        value = payload["ports-defined"]
        if value not in VALID_BODY_PORTS_DEFINED:
            desc = FIELD_DESCRIPTIONS.get("ports-defined", "")
            error_msg = f"Invalid value for 'ports-defined': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PORTS_DEFINED)}"
            error_msg += f"\n  → Example: ports-defined='{{ VALID_BODY_PORTS_DEFINED[0] }}'"
            return (False, error_msg)
    if "server-type" in payload:
        value = payload["server-type"]
        if value not in VALID_BODY_SERVER_TYPE:
            desc = FIELD_DESCRIPTIONS.get("server-type", "")
            error_msg = f"Invalid value for 'server-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SERVER_TYPE)}"
            error_msg += f"\n  → Example: server-type='{{ VALID_BODY_SERVER_TYPE[0] }}'"
            return (False, error_msg)
    if "authentication" in payload:
        value = payload["authentication"]
        if value not in VALID_BODY_AUTHENTICATION:
            desc = FIELD_DESCRIPTIONS.get("authentication", "")
            error_msg = f"Invalid value for 'authentication': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTHENTICATION)}"
            error_msg += f"\n  → Example: authentication='{{ VALID_BODY_AUTHENTICATION[0] }}'"
            return (False, error_msg)
    if "forward-method" in payload:
        value = payload["forward-method"]
        if value not in VALID_BODY_FORWARD_METHOD:
            desc = FIELD_DESCRIPTIONS.get("forward-method", "")
            error_msg = f"Invalid value for 'forward-method': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FORWARD_METHOD)}"
            error_msg += f"\n  → Example: forward-method='{{ VALID_BODY_FORWARD_METHOD[0] }}'"
            return (False, error_msg)
    if "cache-engine-method" in payload:
        value = payload["cache-engine-method"]
        if value not in VALID_BODY_CACHE_ENGINE_METHOD:
            desc = FIELD_DESCRIPTIONS.get("cache-engine-method", "")
            error_msg = f"Invalid value for 'cache-engine-method': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CACHE_ENGINE_METHOD)}"
            error_msg += f"\n  → Example: cache-engine-method='{{ VALID_BODY_CACHE_ENGINE_METHOD[0] }}'"
            return (False, error_msg)
    if "service-type" in payload:
        value = payload["service-type"]
        if value not in VALID_BODY_SERVICE_TYPE:
            desc = FIELD_DESCRIPTIONS.get("service-type", "")
            error_msg = f"Invalid value for 'service-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SERVICE_TYPE)}"
            error_msg += f"\n  → Example: service-type='{{ VALID_BODY_SERVICE_TYPE[0] }}'"
            return (False, error_msg)
    if "primary-hash" in payload:
        value = payload["primary-hash"]
        if value not in VALID_BODY_PRIMARY_HASH:
            desc = FIELD_DESCRIPTIONS.get("primary-hash", "")
            error_msg = f"Invalid value for 'primary-hash': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PRIMARY_HASH)}"
            error_msg += f"\n  → Example: primary-hash='{{ VALID_BODY_PRIMARY_HASH[0] }}'"
            return (False, error_msg)
    if "assignment-bucket-format" in payload:
        value = payload["assignment-bucket-format"]
        if value not in VALID_BODY_ASSIGNMENT_BUCKET_FORMAT:
            desc = FIELD_DESCRIPTIONS.get("assignment-bucket-format", "")
            error_msg = f"Invalid value for 'assignment-bucket-format': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ASSIGNMENT_BUCKET_FORMAT)}"
            error_msg += f"\n  → Example: assignment-bucket-format='{{ VALID_BODY_ASSIGNMENT_BUCKET_FORMAT[0] }}'"
            return (False, error_msg)
    if "return-method" in payload:
        value = payload["return-method"]
        if value not in VALID_BODY_RETURN_METHOD:
            desc = FIELD_DESCRIPTIONS.get("return-method", "")
            error_msg = f"Invalid value for 'return-method': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_RETURN_METHOD)}"
            error_msg += f"\n  → Example: return-method='{{ VALID_BODY_RETURN_METHOD[0] }}'"
            return (False, error_msg)
    if "assignment-method" in payload:
        value = payload["assignment-method"]
        if value not in VALID_BODY_ASSIGNMENT_METHOD:
            desc = FIELD_DESCRIPTIONS.get("assignment-method", "")
            error_msg = f"Invalid value for 'assignment-method': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ASSIGNMENT_METHOD)}"
            error_msg += f"\n  → Example: assignment-method='{{ VALID_BODY_ASSIGNMENT_METHOD[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_system_wccp_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update system/wccp."""
    # Step 1: Validate enum values
    if "ports-defined" in payload:
        value = payload["ports-defined"]
        if value not in VALID_BODY_PORTS_DEFINED:
            return (
                False,
                f"Invalid value for 'ports-defined'='{value}'. Must be one of: {', '.join(VALID_BODY_PORTS_DEFINED)}",
            )
    if "server-type" in payload:
        value = payload["server-type"]
        if value not in VALID_BODY_SERVER_TYPE:
            return (
                False,
                f"Invalid value for 'server-type'='{value}'. Must be one of: {', '.join(VALID_BODY_SERVER_TYPE)}",
            )
    if "authentication" in payload:
        value = payload["authentication"]
        if value not in VALID_BODY_AUTHENTICATION:
            return (
                False,
                f"Invalid value for 'authentication'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTHENTICATION)}",
            )
    if "forward-method" in payload:
        value = payload["forward-method"]
        if value not in VALID_BODY_FORWARD_METHOD:
            return (
                False,
                f"Invalid value for 'forward-method'='{value}'. Must be one of: {', '.join(VALID_BODY_FORWARD_METHOD)}",
            )
    if "cache-engine-method" in payload:
        value = payload["cache-engine-method"]
        if value not in VALID_BODY_CACHE_ENGINE_METHOD:
            return (
                False,
                f"Invalid value for 'cache-engine-method'='{value}'. Must be one of: {', '.join(VALID_BODY_CACHE_ENGINE_METHOD)}",
            )
    if "service-type" in payload:
        value = payload["service-type"]
        if value not in VALID_BODY_SERVICE_TYPE:
            return (
                False,
                f"Invalid value for 'service-type'='{value}'. Must be one of: {', '.join(VALID_BODY_SERVICE_TYPE)}",
            )
    if "primary-hash" in payload:
        value = payload["primary-hash"]
        if value not in VALID_BODY_PRIMARY_HASH:
            return (
                False,
                f"Invalid value for 'primary-hash'='{value}'. Must be one of: {', '.join(VALID_BODY_PRIMARY_HASH)}",
            )
    if "assignment-bucket-format" in payload:
        value = payload["assignment-bucket-format"]
        if value not in VALID_BODY_ASSIGNMENT_BUCKET_FORMAT:
            return (
                False,
                f"Invalid value for 'assignment-bucket-format'='{value}'. Must be one of: {', '.join(VALID_BODY_ASSIGNMENT_BUCKET_FORMAT)}",
            )
    if "return-method" in payload:
        value = payload["return-method"]
        if value not in VALID_BODY_RETURN_METHOD:
            return (
                False,
                f"Invalid value for 'return-method'='{value}'. Must be one of: {', '.join(VALID_BODY_RETURN_METHOD)}",
            )
    if "assignment-method" in payload:
        value = payload["assignment-method"]
        if value not in VALID_BODY_ASSIGNMENT_METHOD:
            return (
                False,
                f"Invalid value for 'assignment-method'='{value}'. Must be one of: {', '.join(VALID_BODY_ASSIGNMENT_METHOD)}",
            )

    return (True, None)


# ============================================================================
# Metadata Access Functions
# Imported from central module to avoid duplication across 1,062 files
# ============================================================================

from hfortix_fortios._helpers.metadata import (
    get_field_description as _get_field_description,
    get_field_type as _get_field_type,
    get_field_constraints as _get_field_constraints,
    get_field_default as _get_field_default,
    get_field_options as _get_field_options,
    get_nested_schema as _get_nested_schema,
    get_all_fields as _get_all_fields,
    get_field_metadata as _get_field_metadata,
    validate_field_value as _validate_field_value,
)

# Wrapper functions that bind module-specific data to central functions
def get_field_description(field_name: str) -> str | None:
    """Get description/help text for a field."""
    return _get_field_description(FIELD_DESCRIPTIONS, field_name)

def get_field_type(field_name: str) -> str | None:
    """Get the type of a field."""
    return _get_field_type(FIELD_TYPES, field_name)

def get_field_constraints(field_name: str) -> dict[str, Any] | None:
    """Get constraints for a field (min/max values, string length)."""
    return _get_field_constraints(FIELD_CONSTRAINTS, field_name)

def get_field_default(field_name: str) -> Any | None:
    """Get default value for a field."""
    return _get_field_default(FIELDS_WITH_DEFAULTS, field_name)

def get_field_options(field_name: str) -> list[str] | None:
    """Get valid enum options for a field."""
    return _get_field_options(globals(), field_name)

def get_nested_schema(field_name: str) -> dict[str, Any] | None:
    """Get schema for nested table/list fields."""
    return _get_nested_schema(NESTED_SCHEMAS, field_name)

def get_all_fields() -> list[str]:
    """Get list of all field names."""
    return _get_all_fields(FIELD_TYPES)

def get_field_metadata(field_name: str) -> dict[str, Any] | None:
    """Get complete metadata for a field (type, description, constraints, defaults, options)."""
    return _get_field_metadata(
        FIELD_TYPES, FIELD_DESCRIPTIONS, FIELD_CONSTRAINTS,
        FIELDS_WITH_DEFAULTS, REQUIRED_FIELDS, NESTED_SCHEMAS,
        globals(), field_name
    )

def validate_field_value(field_name: str, value: Any) -> tuple[bool, str | None]:
    """Validate a single field value against its constraints."""
    return _validate_field_value(
        FIELD_TYPES, FIELD_DESCRIPTIONS, FIELD_CONSTRAINTS,
        globals(), field_name, value
    )


# ============================================================================
# Schema Information
# Metadata about this endpoint schema
# ============================================================================

SCHEMA_INFO = {
    "endpoint": "system/wccp",
    "category": "cmdb",
    "api_path": "system/wccp",
    "mkey": "service-id",
    "mkey_type": "string",
    "help": "Configure WCCP.",
    "total_fields": 23,
    "required_fields_count": 0,
    "fields_with_defaults_count": 22,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
