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
            "options": [{"help": "Certificate extension, server ignores the unsupported certificate extension.", "label": "No", "name": "no"}, {"help": "Critical option, server refuses to authorize if it cannnot recognize the critical option.", "label": "Yes", "name": "yes"}],
        },
        "type": {
            "type": "option",
            "help": "Type of certificate extension.",
            "default": "fixed",
            "options": [{"help": "Fixed certificate extension entry.", "label": "Fixed", "name": "fixed"}, {"help": "Certificate extension entry filled with authenticated username.", "label": "User", "name": "user"}],
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
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_PERMIT_X11_FORWARDING = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_PERMIT_AGENT_FORWARDING = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_PERMIT_PORT_FORWARDING = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_PERMIT_PTY = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_PERMIT_USER_RC = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
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
    """Validate required fields for firewall/access_proxy_ssh_client_cert."""
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


def validate_firewall_access_proxy_ssh_client_cert_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new firewall/access_proxy_ssh_client_cert object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "source-address" in payload:
        value = payload["source-address"]
        if value not in VALID_BODY_SOURCE_ADDRESS:
            desc = FIELD_DESCRIPTIONS.get("source-address", "")
            error_msg = f"Invalid value for 'source-address': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SOURCE_ADDRESS)}"
            error_msg += f"\n  → Example: source-address='{{ VALID_BODY_SOURCE_ADDRESS[0] }}'"
            return (False, error_msg)
    if "permit-x11-forwarding" in payload:
        value = payload["permit-x11-forwarding"]
        if value not in VALID_BODY_PERMIT_X11_FORWARDING:
            desc = FIELD_DESCRIPTIONS.get("permit-x11-forwarding", "")
            error_msg = f"Invalid value for 'permit-x11-forwarding': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PERMIT_X11_FORWARDING)}"
            error_msg += f"\n  → Example: permit-x11-forwarding='{{ VALID_BODY_PERMIT_X11_FORWARDING[0] }}'"
            return (False, error_msg)
    if "permit-agent-forwarding" in payload:
        value = payload["permit-agent-forwarding"]
        if value not in VALID_BODY_PERMIT_AGENT_FORWARDING:
            desc = FIELD_DESCRIPTIONS.get("permit-agent-forwarding", "")
            error_msg = f"Invalid value for 'permit-agent-forwarding': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PERMIT_AGENT_FORWARDING)}"
            error_msg += f"\n  → Example: permit-agent-forwarding='{{ VALID_BODY_PERMIT_AGENT_FORWARDING[0] }}'"
            return (False, error_msg)
    if "permit-port-forwarding" in payload:
        value = payload["permit-port-forwarding"]
        if value not in VALID_BODY_PERMIT_PORT_FORWARDING:
            desc = FIELD_DESCRIPTIONS.get("permit-port-forwarding", "")
            error_msg = f"Invalid value for 'permit-port-forwarding': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PERMIT_PORT_FORWARDING)}"
            error_msg += f"\n  → Example: permit-port-forwarding='{{ VALID_BODY_PERMIT_PORT_FORWARDING[0] }}'"
            return (False, error_msg)
    if "permit-pty" in payload:
        value = payload["permit-pty"]
        if value not in VALID_BODY_PERMIT_PTY:
            desc = FIELD_DESCRIPTIONS.get("permit-pty", "")
            error_msg = f"Invalid value for 'permit-pty': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PERMIT_PTY)}"
            error_msg += f"\n  → Example: permit-pty='{{ VALID_BODY_PERMIT_PTY[0] }}'"
            return (False, error_msg)
    if "permit-user-rc" in payload:
        value = payload["permit-user-rc"]
        if value not in VALID_BODY_PERMIT_USER_RC:
            desc = FIELD_DESCRIPTIONS.get("permit-user-rc", "")
            error_msg = f"Invalid value for 'permit-user-rc': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PERMIT_USER_RC)}"
            error_msg += f"\n  → Example: permit-user-rc='{{ VALID_BODY_PERMIT_USER_RC[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_firewall_access_proxy_ssh_client_cert_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update firewall/access_proxy_ssh_client_cert."""
    # Step 1: Validate enum values
    if "source-address" in payload:
        value = payload["source-address"]
        if value not in VALID_BODY_SOURCE_ADDRESS:
            return (
                False,
                f"Invalid value for 'source-address'='{value}'. Must be one of: {', '.join(VALID_BODY_SOURCE_ADDRESS)}",
            )
    if "permit-x11-forwarding" in payload:
        value = payload["permit-x11-forwarding"]
        if value not in VALID_BODY_PERMIT_X11_FORWARDING:
            return (
                False,
                f"Invalid value for 'permit-x11-forwarding'='{value}'. Must be one of: {', '.join(VALID_BODY_PERMIT_X11_FORWARDING)}",
            )
    if "permit-agent-forwarding" in payload:
        value = payload["permit-agent-forwarding"]
        if value not in VALID_BODY_PERMIT_AGENT_FORWARDING:
            return (
                False,
                f"Invalid value for 'permit-agent-forwarding'='{value}'. Must be one of: {', '.join(VALID_BODY_PERMIT_AGENT_FORWARDING)}",
            )
    if "permit-port-forwarding" in payload:
        value = payload["permit-port-forwarding"]
        if value not in VALID_BODY_PERMIT_PORT_FORWARDING:
            return (
                False,
                f"Invalid value for 'permit-port-forwarding'='{value}'. Must be one of: {', '.join(VALID_BODY_PERMIT_PORT_FORWARDING)}",
            )
    if "permit-pty" in payload:
        value = payload["permit-pty"]
        if value not in VALID_BODY_PERMIT_PTY:
            return (
                False,
                f"Invalid value for 'permit-pty'='{value}'. Must be one of: {', '.join(VALID_BODY_PERMIT_PTY)}",
            )
    if "permit-user-rc" in payload:
        value = payload["permit-user-rc"]
        if value not in VALID_BODY_PERMIT_USER_RC:
            return (
                False,
                f"Invalid value for 'permit-user-rc'='{value}'. Must be one of: {', '.join(VALID_BODY_PERMIT_USER_RC)}",
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
