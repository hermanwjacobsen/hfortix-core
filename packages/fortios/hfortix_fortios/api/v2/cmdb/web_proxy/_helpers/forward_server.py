"""Validation helpers for web_proxy/forward_server - Auto-generated"""

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
    "interface",  # Specify outgoing interface to reach server.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "addr-type": "ip",
    "ip": "0.0.0.0",
    "ipv6": "::",
    "fqdn": "",
    "port": 3128,
    "interface-select-method": "sdwan",
    "interface": "",
    "vrf-select": -1,
    "comment": "",
    "masquerade": "enable",
    "healthcheck": "disable",
    "monitor": "www.google.com",
    "server-down-option": "block",
    "username": "",
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
    "addr-type": "option",  # Address type of the forwarding proxy server: IP or FQDN.
    "ip": "ipv4-address-any",  # Forward proxy server IP address.
    "ipv6": "ipv6-address",  # Forward proxy server IPv6 address.
    "fqdn": "string",  # Forward server Fully Qualified Domain Name (FQDN).
    "port": "integer",  # Port number that the forwarding server expects to receive HT
    "interface-select-method": "option",  # Specify how to select outgoing interface to reach server.
    "interface": "string",  # Specify outgoing interface to reach server.
    "vrf-select": "integer",  # VRF ID used for connection to server.
    "comment": "string",  # Comment.
    "masquerade": "option",  # Enable/disable use of the IP address of the outgoing interfa
    "healthcheck": "option",  # Enable/disable forward server health checking. Attempts to c
    "monitor": "string",  # URL for forward server health check monitoring (default = ww
    "server-down-option": "option",  # Action to take when the forward server is found to be down: 
    "username": "string",  # HTTP authentication user name.
    "password": "password",  # HTTP authentication password.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "Server name.",
    "addr-type": "Address type of the forwarding proxy server: IP or FQDN.",
    "ip": "Forward proxy server IP address.",
    "ipv6": "Forward proxy server IPv6 address.",
    "fqdn": "Forward server Fully Qualified Domain Name (FQDN).",
    "port": "Port number that the forwarding server expects to receive HTTP sessions on (1 - 65535, default = 3128).",
    "interface-select-method": "Specify how to select outgoing interface to reach server.",
    "interface": "Specify outgoing interface to reach server.",
    "vrf-select": "VRF ID used for connection to server.",
    "comment": "Comment.",
    "masquerade": "Enable/disable use of the IP address of the outgoing interface as the client IP address (default = enable)",
    "healthcheck": "Enable/disable forward server health checking. Attempts to connect through the remote forwarding server to a destination to verify that the forwarding server is operating normally.",
    "monitor": "URL for forward server health check monitoring (default = www.google.com).",
    "server-down-option": "Action to take when the forward server is found to be down: block sessions until the server is back up or pass sessions to their destination.",
    "username": "HTTP authentication user name.",
    "password": "HTTP authentication password.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 63},
    "fqdn": {"type": "string", "max_length": 255},
    "port": {"type": "integer", "min": 1, "max": 65535},
    "interface": {"type": "string", "max_length": 15},
    "vrf-select": {"type": "integer", "min": 0, "max": 511},
    "comment": {"type": "string", "max_length": 63},
    "monitor": {"type": "string", "max_length": 255},
    "username": {"type": "string", "max_length": 64},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
}


# Valid enum values from API documentation
VALID_BODY_ADDR_TYPE = [
    "ip",  # Use an IPv4 address for the forwarding proxy server.
    "ipv6",  # Use an IPv6 address for the forwarding proxy server.
    "fqdn",  # Use the FQDN for the forwarding proxy server.
]
VALID_BODY_INTERFACE_SELECT_METHOD = [
    "sdwan",  # Set outgoing interface by SD-WAN or policy routing rules.
    "specify",  # Set outgoing interface manually.
]
VALID_BODY_MASQUERADE = [
    "enable",  # Enable use of the IP address of the outgoing interface as the client IP address.
    "disable",  # Disable use of the IP address of the outgoing interface as the client IP address.
]
VALID_BODY_HEALTHCHECK = [
    "disable",  # Disable health checking.
    "enable",  # Enable health checking.
]
VALID_BODY_SERVER_DOWN_OPTION = [
    "block",  # Block sessions until the server is back up.
    "pass",  # Pass sessions to their destination bypassing the forward server.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_web_proxy_forward_server_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for web_proxy/forward_server."""
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
    """Validate required fields for web_proxy/forward_server."""
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


def validate_web_proxy_forward_server_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new web_proxy/forward_server object."""
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
    if "interface-select-method" in payload:
        value = payload["interface-select-method"]
        if value not in VALID_BODY_INTERFACE_SELECT_METHOD:
            desc = FIELD_DESCRIPTIONS.get("interface-select-method", "")
            error_msg = f"Invalid value for 'interface-select-method': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_INTERFACE_SELECT_METHOD)}"
            error_msg += f"\n  → Example: interface-select-method='{{ VALID_BODY_INTERFACE_SELECT_METHOD[0] }}'"
            return (False, error_msg)
    if "masquerade" in payload:
        value = payload["masquerade"]
        if value not in VALID_BODY_MASQUERADE:
            desc = FIELD_DESCRIPTIONS.get("masquerade", "")
            error_msg = f"Invalid value for 'masquerade': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MASQUERADE)}"
            error_msg += f"\n  → Example: masquerade='{{ VALID_BODY_MASQUERADE[0] }}'"
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
    if "server-down-option" in payload:
        value = payload["server-down-option"]
        if value not in VALID_BODY_SERVER_DOWN_OPTION:
            desc = FIELD_DESCRIPTIONS.get("server-down-option", "")
            error_msg = f"Invalid value for 'server-down-option': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SERVER_DOWN_OPTION)}"
            error_msg += f"\n  → Example: server-down-option='{{ VALID_BODY_SERVER_DOWN_OPTION[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_web_proxy_forward_server_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update web_proxy/forward_server."""
    # Step 1: Validate enum values
    if "addr-type" in payload:
        value = payload["addr-type"]
        if value not in VALID_BODY_ADDR_TYPE:
            return (
                False,
                f"Invalid value for 'addr-type'='{value}'. Must be one of: {', '.join(VALID_BODY_ADDR_TYPE)}",
            )
    if "interface-select-method" in payload:
        value = payload["interface-select-method"]
        if value not in VALID_BODY_INTERFACE_SELECT_METHOD:
            return (
                False,
                f"Invalid value for 'interface-select-method'='{value}'. Must be one of: {', '.join(VALID_BODY_INTERFACE_SELECT_METHOD)}",
            )
    if "masquerade" in payload:
        value = payload["masquerade"]
        if value not in VALID_BODY_MASQUERADE:
            return (
                False,
                f"Invalid value for 'masquerade'='{value}'. Must be one of: {', '.join(VALID_BODY_MASQUERADE)}",
            )
    if "healthcheck" in payload:
        value = payload["healthcheck"]
        if value not in VALID_BODY_HEALTHCHECK:
            return (
                False,
                f"Invalid value for 'healthcheck'='{value}'. Must be one of: {', '.join(VALID_BODY_HEALTHCHECK)}",
            )
    if "server-down-option" in payload:
        value = payload["server-down-option"]
        if value not in VALID_BODY_SERVER_DOWN_OPTION:
            return (
                False,
                f"Invalid value for 'server-down-option'='{value}'. Must be one of: {', '.join(VALID_BODY_SERVER_DOWN_OPTION)}",
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
    "endpoint": "web_proxy/forward_server",
    "category": "cmdb",
    "api_path": "web-proxy/forward-server",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure forward-server addresses.",
    "total_fields": 16,
    "required_fields_count": 1,
    "fields_with_defaults_count": 15,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
