"""Validation helpers for firewall/ldb_monitor - Auto-generated"""

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
    "type",  # Select the Monitor type used by the health check monitor to check the health of the server (PING | TCP | HTTP | HTTPS | DNS).
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "type": "",
    "interval": 10,
    "timeout": 2,
    "retry": 3,
    "port": 0,
    "src-ip": "0.0.0.0",
    "http-get": "",
    "http-match": "",
    "http-max-redirects": 0,
    "dns-protocol": "udp",
    "dns-request-domain": "",
    "dns-match-ip": "0.0.0.0",
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
    "name": "string",  # Monitor name.
    "type": "option",  # Select the Monitor type used by the health check monitor to 
    "interval": "integer",  # Time between health checks (5 - 65535 sec, default = 10).
    "timeout": "integer",  # Time to wait to receive response to a health check from a se
    "retry": "integer",  # Number health check attempts before the server is considered
    "port": "integer",  # Service port used to perform the health check. If 0, health 
    "src-ip": "ipv4-address",  # Source IP for ldb-monitor.
    "http-get": "string",  # Request URI used to send a GET request to check the health o
    "http-match": "string",  # String to match the value expected in response to an HTTP-GE
    "http-max-redirects": "integer",  # The maximum number of HTTP redirects to be allowed (0 - 5, d
    "dns-protocol": "option",  # Select the protocol used by the DNS health check monitor to 
    "dns-request-domain": "string",  # Fully qualified domain name to resolve for the DNS probe.
    "dns-match-ip": "ipv4-address",  # Response IP expected from DNS server.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "Monitor name.",
    "type": "Select the Monitor type used by the health check monitor to check the health of the server (PING | TCP | HTTP | HTTPS | DNS).",
    "interval": "Time between health checks (5 - 65535 sec, default = 10).",
    "timeout": "Time to wait to receive response to a health check from a server. Reaching the timeout means the health check failed (1 - 255 sec, default = 2).",
    "retry": "Number health check attempts before the server is considered down (1 - 255, default = 3).",
    "port": "Service port used to perform the health check. If 0, health check monitor inherits port configured for the server (0 - 65535, default = 0).",
    "src-ip": "Source IP for ldb-monitor.",
    "http-get": "Request URI used to send a GET request to check the health of an HTTP server. Optionally provide a hostname before the first '/' and it will be used as the HTTP Host Header.",
    "http-match": "String to match the value expected in response to an HTTP-GET request.",
    "http-max-redirects": "The maximum number of HTTP redirects to be allowed (0 - 5, default = 0).",
    "dns-protocol": "Select the protocol used by the DNS health check monitor to check the health of the server (UDP | TCP).",
    "dns-request-domain": "Fully qualified domain name to resolve for the DNS probe.",
    "dns-match-ip": "Response IP expected from DNS server.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 35},
    "interval": {"type": "integer", "min": 5, "max": 65535},
    "timeout": {"type": "integer", "min": 1, "max": 255},
    "retry": {"type": "integer", "min": 1, "max": 255},
    "port": {"type": "integer", "min": 0, "max": 65535},
    "http-get": {"type": "string", "max_length": 255},
    "http-match": {"type": "string", "max_length": 255},
    "http-max-redirects": {"type": "integer", "min": 0, "max": 5},
    "dns-request-domain": {"type": "string", "max_length": 255},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
}


# Valid enum values from API documentation
VALID_BODY_TYPE = [
    "ping",  # PING health monitor.
    "tcp",  # TCP-connect health monitor.
    "http",  # HTTP-GET health monitor.
    "https",  # HTTP-GET health monitor with SSL.
    "dns",  # DNS health monitor.
]
VALID_BODY_DNS_PROTOCOL = [
    "udp",  # UDP.
    "tcp",  # TCP.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_firewall_ldb_monitor_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for firewall/ldb_monitor."""
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
    """Validate required fields for firewall/ldb_monitor."""
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


def validate_firewall_ldb_monitor_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new firewall/ldb_monitor object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "type" in payload:
        value = payload["type"]
        if value not in VALID_BODY_TYPE:
            desc = FIELD_DESCRIPTIONS.get("type", "")
            error_msg = f"Invalid value for 'type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_TYPE)}"
            error_msg += f"\n  → Example: type='{{ VALID_BODY_TYPE[0] }}'"
            return (False, error_msg)
    if "dns-protocol" in payload:
        value = payload["dns-protocol"]
        if value not in VALID_BODY_DNS_PROTOCOL:
            desc = FIELD_DESCRIPTIONS.get("dns-protocol", "")
            error_msg = f"Invalid value for 'dns-protocol': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DNS_PROTOCOL)}"
            error_msg += f"\n  → Example: dns-protocol='{{ VALID_BODY_DNS_PROTOCOL[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_firewall_ldb_monitor_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update firewall/ldb_monitor."""
    # Step 1: Validate enum values
    if "type" in payload:
        value = payload["type"]
        if value not in VALID_BODY_TYPE:
            return (
                False,
                f"Invalid value for 'type'='{value}'. Must be one of: {', '.join(VALID_BODY_TYPE)}",
            )
    if "dns-protocol" in payload:
        value = payload["dns-protocol"]
        if value not in VALID_BODY_DNS_PROTOCOL:
            return (
                False,
                f"Invalid value for 'dns-protocol'='{value}'. Must be one of: {', '.join(VALID_BODY_DNS_PROTOCOL)}",
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
    "endpoint": "firewall/ldb_monitor",
    "category": "cmdb",
    "api_path": "firewall/ldb-monitor",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure server load balancing health monitors.",
    "total_fields": 13,
    "required_fields_count": 1,
    "fields_with_defaults_count": 13,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
