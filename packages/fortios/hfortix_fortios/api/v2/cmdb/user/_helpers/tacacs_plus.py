"""Validation helpers for user/tacacs_plus - Auto-generated"""

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
    "server",  # Primary TACACS+ server CN domain name or IP address.
    "interface",  # Specify outgoing interface to reach server.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "server": "",
    "secondary-server": "",
    "tertiary-server": "",
    "port": 49,
    "status-ttl": 300,
    "authen-type": "auto",
    "authorization": "disable",
    "source-ip": "",
    "interface-select-method": "auto",
    "interface": "",
    "vrf-select": 0,
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
    "name": "string",  # TACACS+ server entry name.
    "server": "string",  # Primary TACACS+ server CN domain name or IP address.
    "secondary-server": "string",  # Secondary TACACS+ server CN domain name or IP address.
    "tertiary-server": "string",  # Tertiary TACACS+ server CN domain name or IP address.
    "port": "integer",  # Port number of the TACACS+ server.
    "key": "password",  # Key to access the primary server.
    "secondary-key": "password",  # Key to access the secondary server.
    "tertiary-key": "password",  # Key to access the tertiary server.
    "status-ttl": "integer",  # Time for which server reachability is cached so that when a 
    "authen-type": "option",  # Allowed authentication protocols/methods.
    "authorization": "option",  # Enable/disable TACACS+ authorization.
    "source-ip": "string",  # Source IP address for communications to TACACS+ server.
    "interface-select-method": "option",  # Specify how to select outgoing interface to reach server.
    "interface": "string",  # Specify outgoing interface to reach server.
    "vrf-select": "integer",  # VRF ID used for connection to server.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "TACACS+ server entry name.",
    "server": "Primary TACACS+ server CN domain name or IP address.",
    "secondary-server": "Secondary TACACS+ server CN domain name or IP address.",
    "tertiary-server": "Tertiary TACACS+ server CN domain name or IP address.",
    "port": "Port number of the TACACS+ server.",
    "key": "Key to access the primary server.",
    "secondary-key": "Key to access the secondary server.",
    "tertiary-key": "Key to access the tertiary server.",
    "status-ttl": "Time for which server reachability is cached so that when a server is unreachable, it will not be retried for at least this period of time (0 = cache disabled, default = 300).",
    "authen-type": "Allowed authentication protocols/methods.",
    "authorization": "Enable/disable TACACS+ authorization.",
    "source-ip": "Source IP address for communications to TACACS+ server.",
    "interface-select-method": "Specify how to select outgoing interface to reach server.",
    "interface": "Specify outgoing interface to reach server.",
    "vrf-select": "VRF ID used for connection to server.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 35},
    "server": {"type": "string", "max_length": 63},
    "secondary-server": {"type": "string", "max_length": 63},
    "tertiary-server": {"type": "string", "max_length": 63},
    "port": {"type": "integer", "min": 1, "max": 65535},
    "status-ttl": {"type": "integer", "min": 0, "max": 600},
    "source-ip": {"type": "string", "max_length": 63},
    "interface": {"type": "string", "max_length": 15},
    "vrf-select": {"type": "integer", "min": 0, "max": 511},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
}


# Valid enum values from API documentation
VALID_BODY_AUTHEN_TYPE = [
    "mschap",  # MSCHAP.
    "chap",  # CHAP.
    "pap",  # PAP.
    "ascii",  # ASCII.
    "auto",  # Use PAP, MSCHAP, and CHAP (in that order).
]
VALID_BODY_AUTHORIZATION = [
    "enable",  # Enable TACACS+ authorization.
    "disable",  # Disable TACACS+ authorization.
]
VALID_BODY_INTERFACE_SELECT_METHOD = [
    "auto",  # Set outgoing interface automatically.
    "sdwan",  # Set outgoing interface by SD-WAN or policy routing rules.
    "specify",  # Set outgoing interface manually.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_user_tacacs_plus_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for user/tacacs_plus."""
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
    """Validate required fields for user/tacacs_plus."""
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


def validate_user_tacacs_plus_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new user/tacacs_plus object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "authen-type" in payload:
        value = payload["authen-type"]
        if value not in VALID_BODY_AUTHEN_TYPE:
            desc = FIELD_DESCRIPTIONS.get("authen-type", "")
            error_msg = f"Invalid value for 'authen-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTHEN_TYPE)}"
            error_msg += f"\n  → Example: authen-type='{{ VALID_BODY_AUTHEN_TYPE[0] }}'"
            return (False, error_msg)
    if "authorization" in payload:
        value = payload["authorization"]
        if value not in VALID_BODY_AUTHORIZATION:
            desc = FIELD_DESCRIPTIONS.get("authorization", "")
            error_msg = f"Invalid value for 'authorization': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTHORIZATION)}"
            error_msg += f"\n  → Example: authorization='{{ VALID_BODY_AUTHORIZATION[0] }}'"
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

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_user_tacacs_plus_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update user/tacacs_plus."""
    # Step 1: Validate enum values
    if "authen-type" in payload:
        value = payload["authen-type"]
        if value not in VALID_BODY_AUTHEN_TYPE:
            return (
                False,
                f"Invalid value for 'authen-type'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTHEN_TYPE)}",
            )
    if "authorization" in payload:
        value = payload["authorization"]
        if value not in VALID_BODY_AUTHORIZATION:
            return (
                False,
                f"Invalid value for 'authorization'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTHORIZATION)}",
            )
    if "interface-select-method" in payload:
        value = payload["interface-select-method"]
        if value not in VALID_BODY_INTERFACE_SELECT_METHOD:
            return (
                False,
                f"Invalid value for 'interface-select-method'='{value}'. Must be one of: {', '.join(VALID_BODY_INTERFACE_SELECT_METHOD)}",
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
    "endpoint": "user/tacacs_plus",
    "category": "cmdb",
    "api_path": "user/tacacs+",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure TACACS+ server entries.",
    "total_fields": 15,
    "required_fields_count": 2,
    "fields_with_defaults_count": 12,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
