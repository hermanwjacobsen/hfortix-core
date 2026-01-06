"""Validation helpers for switch_controller/initial_config/template - Auto-generated"""

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
    "name",  # Initial config template name.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "vlanid": 0,
    "ip": "0.0.0.0 0.0.0.0",
    "allowaccess": "",
    "auto-ip": "enable",
    "dhcp-server": "disable",
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
    "name": "string",  # Initial config template name.
    "vlanid": "integer",  # Unique VLAN ID.
    "ip": "ipv4-classnet-host",  # Interface IPv4 address and subnet mask.
    "allowaccess": "option",  # Permitted types of management access to this interface.
    "auto-ip": "option",  # Automatically allocate interface address and subnet block.
    "dhcp-server": "option",  # Enable/disable a DHCP server on this interface.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "Initial config template name.",
    "vlanid": "Unique VLAN ID.",
    "ip": "Interface IPv4 address and subnet mask.",
    "allowaccess": "Permitted types of management access to this interface.",
    "auto-ip": "Automatically allocate interface address and subnet block.",
    "dhcp-server": "Enable/disable a DHCP server on this interface.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 63},
    "vlanid": {"type": "integer", "min": 1, "max": 4094},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
}


# Valid enum values from API documentation
VALID_BODY_ALLOWACCESS = [
    "ping",  # PING access.
    "https",  # HTTPS access.
    "ssh",  # SSH access.
    "snmp",  # SNMP access.
    "http",  # HTTP access.
    "telnet",  # TELNET access.
    "fgfm",  # FortiManager access.
    "radius-acct",  # RADIUS accounting access.
    "probe-response",  # Probe access.
    "fabric",  # Security Fabric access.
    "ftm",  # FTM access.
]
VALID_BODY_AUTO_IP = [
    "enable",  # Enable auto-ip status.
    "disable",  # Disable auto-ip status.
]
VALID_BODY_DHCP_SERVER = [
    "enable",  # Enable DHCP server.
    "disable",  # Disable DHCP server.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_switch_controller_initial_config_template_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for switch_controller/initial_config/template."""
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
    """Validate required fields for switch_controller/initial_config/template."""
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


def validate_switch_controller_initial_config_template_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new switch_controller/initial_config/template object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "allowaccess" in payload:
        value = payload["allowaccess"]
        if value not in VALID_BODY_ALLOWACCESS:
            desc = FIELD_DESCRIPTIONS.get("allowaccess", "")
            error_msg = f"Invalid value for 'allowaccess': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ALLOWACCESS)}"
            error_msg += f"\n  → Example: allowaccess='{{ VALID_BODY_ALLOWACCESS[0] }}'"
            return (False, error_msg)
    if "auto-ip" in payload:
        value = payload["auto-ip"]
        if value not in VALID_BODY_AUTO_IP:
            desc = FIELD_DESCRIPTIONS.get("auto-ip", "")
            error_msg = f"Invalid value for 'auto-ip': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTO_IP)}"
            error_msg += f"\n  → Example: auto-ip='{{ VALID_BODY_AUTO_IP[0] }}'"
            return (False, error_msg)
    if "dhcp-server" in payload:
        value = payload["dhcp-server"]
        if value not in VALID_BODY_DHCP_SERVER:
            desc = FIELD_DESCRIPTIONS.get("dhcp-server", "")
            error_msg = f"Invalid value for 'dhcp-server': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DHCP_SERVER)}"
            error_msg += f"\n  → Example: dhcp-server='{{ VALID_BODY_DHCP_SERVER[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_switch_controller_initial_config_template_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update switch_controller/initial_config/template."""
    # Step 1: Validate enum values
    if "allowaccess" in payload:
        value = payload["allowaccess"]
        if value not in VALID_BODY_ALLOWACCESS:
            return (
                False,
                f"Invalid value for 'allowaccess'='{value}'. Must be one of: {', '.join(VALID_BODY_ALLOWACCESS)}",
            )
    if "auto-ip" in payload:
        value = payload["auto-ip"]
        if value not in VALID_BODY_AUTO_IP:
            return (
                False,
                f"Invalid value for 'auto-ip'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTO_IP)}",
            )
    if "dhcp-server" in payload:
        value = payload["dhcp-server"]
        if value not in VALID_BODY_DHCP_SERVER:
            return (
                False,
                f"Invalid value for 'dhcp-server'='{value}'. Must be one of: {', '.join(VALID_BODY_DHCP_SERVER)}",
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
    "endpoint": "switch_controller/initial_config/template",
    "category": "cmdb",
    "api_path": "switch-controller.initial-config/template",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure template for auto-generated VLANs.",
    "total_fields": 6,
    "required_fields_count": 1,
    "fields_with_defaults_count": 6,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
