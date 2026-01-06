"""Validation helpers for icap/server - Auto-generated"""

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
    "healthcheck-service",  # ICAP Service name to use for health checks.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "addr-type": "ip4",
    "ip-address": "0.0.0.0",
    "ip6-address": "::",
    "fqdn": "",
    "port": 1344,
    "max-connections": 100,
    "secure": "disable",
    "ssl-cert": "",
    "healthcheck": "disable",
    "healthcheck-service": "",
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
    "name": "string",  # Server name.
    "addr-type": "option",  # Address type of the remote ICAP server: IPv4, IPv6 or FQDN.
    "ip-address": "ipv4-address-any",  # IPv4 address of the ICAP server.
    "ip6-address": "ipv6-address",  # IPv6 address of the ICAP server.
    "fqdn": "string",  # ICAP remote server Fully Qualified Domain Name (FQDN).
    "port": "integer",  # ICAP server port.
    "max-connections": "integer",  # Maximum number of concurrent connections to ICAP server (unl
    "secure": "option",  # Enable/disable secure connection to ICAP server.
    "ssl-cert": "string",  # CA certificate name.
    "healthcheck": "option",  # Enable/disable ICAP remote server health checking. Attempts 
    "healthcheck-service": "string",  # ICAP Service name to use for health checks.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "Server name.",
    "addr-type": "Address type of the remote ICAP server: IPv4, IPv6 or FQDN.",
    "ip-address": "IPv4 address of the ICAP server.",
    "ip6-address": "IPv6 address of the ICAP server.",
    "fqdn": "ICAP remote server Fully Qualified Domain Name (FQDN).",
    "port": "ICAP server port.",
    "max-connections": "Maximum number of concurrent connections to ICAP server (unlimited = 0, default = 100). Must not be less than wad-worker-count.",
    "secure": "Enable/disable secure connection to ICAP server.",
    "ssl-cert": "CA certificate name.",
    "healthcheck": "Enable/disable ICAP remote server health checking. Attempts to connect to the remote ICAP server to verify that the server is operating normally.",
    "healthcheck-service": "ICAP Service name to use for health checks.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 63},
    "fqdn": {"type": "string", "max_length": 255},
    "port": {"type": "integer", "min": 1, "max": 65535},
    "max-connections": {"type": "integer", "min": 0, "max": 4294967295},
    "ssl-cert": {"type": "string", "max_length": 79},
    "healthcheck-service": {"type": "string", "max_length": 127},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
}


# Valid enum values from API documentation
VALID_BODY_ADDR_TYPE = [
    "ip4",  # Use an IPv4 address for the remote ICAP server.
    "ip6",  # Use an IPv6 address for the remote ICAP server.
    "fqdn",  # Use the FQDN for the forwarding proxy server.
]
VALID_BODY_SECURE = [
    "disable",  # Disable connection to secure ICAP server.
    "enable",  # Enable connection to secure ICAP server.
]
VALID_BODY_HEALTHCHECK = [
    "disable",  # Disable health checking.
    "enable",  # Enable health checking.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_icap_server_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for icap/server."""
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
    """Validate required fields for icap/server."""
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


def validate_icap_server_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new icap/server object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "addr-type" in payload:
        value = payload["addr-type"]
        if value not in VALID_BODY_ADDR_TYPE:
            desc = FIELD_DESCRIPTIONS.get("addr-type", "")
            error_msg = f"Invalid value for 'addr-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ADDR_TYPE)}"
            error_msg += f"\n  → Example: addr-type='{{ VALID_BODY_ADDR_TYPE[0] }}'"
            return (False, error_msg)
    if "secure" in payload:
        value = payload["secure"]
        if value not in VALID_BODY_SECURE:
            desc = FIELD_DESCRIPTIONS.get("secure", "")
            error_msg = f"Invalid value for 'secure': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SECURE)}"
            error_msg += f"\n  → Example: secure='{{ VALID_BODY_SECURE[0] }}'"
            return (False, error_msg)
    if "healthcheck" in payload:
        value = payload["healthcheck"]
        if value not in VALID_BODY_HEALTHCHECK:
            desc = FIELD_DESCRIPTIONS.get("healthcheck", "")
            error_msg = f"Invalid value for 'healthcheck': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_HEALTHCHECK)}"
            error_msg += f"\n  → Example: healthcheck='{{ VALID_BODY_HEALTHCHECK[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_icap_server_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update icap/server."""
    # Step 1: Validate enum values
    if "addr-type" in payload:
        value = payload["addr-type"]
        if value not in VALID_BODY_ADDR_TYPE:
            return (
                False,
                f"Invalid value for 'addr-type'='{value}'. Must be one of: {', '.join(VALID_BODY_ADDR_TYPE)}",
            )
    if "secure" in payload:
        value = payload["secure"]
        if value not in VALID_BODY_SECURE:
            return (
                False,
                f"Invalid value for 'secure'='{value}'. Must be one of: {', '.join(VALID_BODY_SECURE)}",
            )
    if "healthcheck" in payload:
        value = payload["healthcheck"]
        if value not in VALID_BODY_HEALTHCHECK:
            return (
                False,
                f"Invalid value for 'healthcheck'='{value}'. Must be one of: {', '.join(VALID_BODY_HEALTHCHECK)}",
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
    "endpoint": "icap/server",
    "category": "cmdb",
    "api_path": "icap/server",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure ICAP servers.",
    "total_fields": 11,
    "required_fields_count": 1,
    "fields_with_defaults_count": 11,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
