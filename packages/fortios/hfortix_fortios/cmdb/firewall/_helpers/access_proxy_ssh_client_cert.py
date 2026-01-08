"""Validation helpers for firewall/access_proxy_ssh_client_cert - Auto-generated"""

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

# Import central validation functions (avoid duplication across 1,062 files)
from hfortix_fortios._helpers.validation import (
    validate_required_fields as _validate_required_fields,
    validate_enum_field as _validate_enum_field,
    validate_query_parameter as _validate_query_parameter,
)

# ============================================================================
# Required Fields Validation
# Auto-generated from schema
# ============================================================================

# ⚠️  IMPORTANT: FortiOS schemas have known issues with required field marking:

# Do NOT use this list for strict validation - test with the actual FortiOS API!

# Fields marked as required (after filtering false positives)
REQUIRED_FIELDS = [
    "auth-ca",  # Name of the SSH server public key authentication CA.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "source-address": "disable",
    "permit-x11-forwarding": "enable",
    "permit-agent-forwarding": "enable",
    "permit-port-forwarding": "enable",
    "permit-pty": "enable",
    "permit-user-rc": "enable",
    "auth-ca": "",
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
    "name": "string",  # SSH client certificate name.
    "source-address": "option",  # Enable/disable appending source-address certificate critical
    "permit-x11-forwarding": "option",  # Enable/disable appending permit-x11-forwarding certificate e
    "permit-agent-forwarding": "option",  # Enable/disable appending permit-agent-forwarding certificate
    "permit-port-forwarding": "option",  # Enable/disable appending permit-port-forwarding certificate 
    "permit-pty": "option",  # Enable/disable appending permit-pty certificate extension.
    "permit-user-rc": "option",  # Enable/disable appending permit-user-rc certificate extensio
    "cert-extension": "string",  # Configure certificate extension for user certificate.
    "auth-ca": "string",  # Name of the SSH server public key authentication CA.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "SSH client certificate name.",
    "source-address": "Enable/disable appending source-address certificate critical option. This option ensure certificate only accepted from FortiGate source address.",
    "permit-x11-forwarding": "Enable/disable appending permit-x11-forwarding certificate extension.",
    "permit-agent-forwarding": "Enable/disable appending permit-agent-forwarding certificate extension.",
    "permit-port-forwarding": "Enable/disable appending permit-port-forwarding certificate extension.",
    "permit-pty": "Enable/disable appending permit-pty certificate extension.",
    "permit-user-rc": "Enable/disable appending permit-user-rc certificate extension.",
    "cert-extension": "Configure certificate extension for user certificate.",
    "auth-ca": "Name of the SSH server public key authentication CA.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 79},
    "auth-ca": {"type": "string", "max_length": 79},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "cert-extension": {
        "name": {
            "type": "string",
            "help": "Name of certificate extension.",
            "required": True,
            "default": "",
            "max_length": 127,
        },
        "critical": {
            "type": "option",
            "help": "Critical option.",
            "default": "no",
            "options": ["no", "yes"],
        },
        "type": {
            "type": "option",
            "help": "Type of certificate extension.",
            "default": "fixed",
            "options": ["fixed", "user"],
        },
        "data": {
            "type": "string",
            "help": "Data of certificate extension.",
            "default": "",
            "max_length": 127,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_SOURCE_ADDRESS = [
    "enable",
    "disable",
]
VALID_BODY_PERMIT_X11_FORWARDING = [
    "enable",
    "disable",
]
VALID_BODY_PERMIT_AGENT_FORWARDING = [
    "enable",
    "disable",
]
VALID_BODY_PERMIT_PORT_FORWARDING = [
    "enable",
    "disable",
]
VALID_BODY_PERMIT_PTY = [
    "enable",
    "disable",
]
VALID_BODY_PERMIT_USER_RC = [
    "enable",
    "disable",
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_firewall_access_proxy_ssh_client_cert_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for firewall/access_proxy_ssh_client_cert."""
    # Validate query parameters using central function
    if "action" in params:
        is_valid, error = _validate_query_parameter(
            "action",
            params.get("action"),
            VALID_QUERY_ACTION
        )
        if not is_valid:
            return (False, error)

    return (True, None)


# ============================================================================
# POST Validation
# ============================================================================


def validate_firewall_access_proxy_ssh_client_cert_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new firewall/access_proxy_ssh_client_cert object."""
    # Step 1: Validate required fields using central function
    is_valid, error = _validate_required_fields(
        payload,
        REQUIRED_FIELDS,
        FIELD_DESCRIPTIONS
    )
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values using central function
    if "source-address" in payload:
        is_valid, error = _validate_enum_field(
            "source-address",
            payload["source-address"],
            VALID_BODY_SOURCE_ADDRESS,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "permit-x11-forwarding" in payload:
        is_valid, error = _validate_enum_field(
            "permit-x11-forwarding",
            payload["permit-x11-forwarding"],
            VALID_BODY_PERMIT_X11_FORWARDING,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "permit-agent-forwarding" in payload:
        is_valid, error = _validate_enum_field(
            "permit-agent-forwarding",
            payload["permit-agent-forwarding"],
            VALID_BODY_PERMIT_AGENT_FORWARDING,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "permit-port-forwarding" in payload:
        is_valid, error = _validate_enum_field(
            "permit-port-forwarding",
            payload["permit-port-forwarding"],
            VALID_BODY_PERMIT_PORT_FORWARDING,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "permit-pty" in payload:
        is_valid, error = _validate_enum_field(
            "permit-pty",
            payload["permit-pty"],
            VALID_BODY_PERMIT_PTY,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "permit-user-rc" in payload:
        is_valid, error = _validate_enum_field(
            "permit-user-rc",
            payload["permit-user-rc"],
            VALID_BODY_PERMIT_USER_RC,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_firewall_access_proxy_ssh_client_cert_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update firewall/access_proxy_ssh_client_cert."""
    # Validate enum values using central function
    if "source-address" in payload:
        is_valid, error = _validate_enum_field(
            "source-address",
            payload["source-address"],
            VALID_BODY_SOURCE_ADDRESS,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "permit-x11-forwarding" in payload:
        is_valid, error = _validate_enum_field(
            "permit-x11-forwarding",
            payload["permit-x11-forwarding"],
            VALID_BODY_PERMIT_X11_FORWARDING,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "permit-agent-forwarding" in payload:
        is_valid, error = _validate_enum_field(
            "permit-agent-forwarding",
            payload["permit-agent-forwarding"],
            VALID_BODY_PERMIT_AGENT_FORWARDING,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "permit-port-forwarding" in payload:
        is_valid, error = _validate_enum_field(
            "permit-port-forwarding",
            payload["permit-port-forwarding"],
            VALID_BODY_PERMIT_PORT_FORWARDING,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "permit-pty" in payload:
        is_valid, error = _validate_enum_field(
            "permit-pty",
            payload["permit-pty"],
            VALID_BODY_PERMIT_PTY,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "permit-user-rc" in payload:
        is_valid, error = _validate_enum_field(
            "permit-user-rc",
            payload["permit-user-rc"],
            VALID_BODY_PERMIT_USER_RC,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)

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
    "endpoint": "firewall/access_proxy_ssh_client_cert",
    "category": "cmdb",
    "api_path": "firewall/access-proxy-ssh-client-cert",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure Access Proxy SSH client certificate.",
    "total_fields": 9,
    "required_fields_count": 1,
    "fields_with_defaults_count": 8,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
