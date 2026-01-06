"""Validation helpers for switch_controller/vlan_policy - Auto-generated"""

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
    "fortilink",  # FortiLink interface for which this VLAN policy belongs to.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "description": "",
    "fortilink": "",
    "vlan": "",
    "allowed-vlans-all": "disable",
    "discard-mode": "none",
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
    "name": "string",  # VLAN policy name.
    "description": "string",  # Description for the VLAN policy.
    "fortilink": "string",  # FortiLink interface for which this VLAN policy belongs to.
    "vlan": "string",  # Native VLAN to be applied when using this VLAN policy.
    "allowed-vlans": "string",  # Allowed VLANs to be applied when using this VLAN policy.
    "untagged-vlans": "string",  # Untagged VLANs to be applied when using this VLAN policy.
    "allowed-vlans-all": "option",  # Enable/disable all defined VLANs when using this VLAN policy
    "discard-mode": "option",  # Discard mode to be applied when using this VLAN policy.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "VLAN policy name.",
    "description": "Description for the VLAN policy.",
    "fortilink": "FortiLink interface for which this VLAN policy belongs to.",
    "vlan": "Native VLAN to be applied when using this VLAN policy.",
    "allowed-vlans": "Allowed VLANs to be applied when using this VLAN policy.",
    "untagged-vlans": "Untagged VLANs to be applied when using this VLAN policy.",
    "allowed-vlans-all": "Enable/disable all defined VLANs when using this VLAN policy.",
    "discard-mode": "Discard mode to be applied when using this VLAN policy.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 63},
    "description": {"type": "string", "max_length": 63},
    "fortilink": {"type": "string", "max_length": 15},
    "vlan": {"type": "string", "max_length": 15},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "allowed-vlans": {
        "vlan-name": {
            "type": "string",
            "help": "VLAN name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "untagged-vlans": {
        "vlan-name": {
            "type": "string",
            "help": "VLAN name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_ALLOWED_VLANS_ALL = [
    "enable",  # Enable all defined VLANs.
    "disable",  # Disable all defined VLANs.
]
VALID_BODY_DISCARD_MODE = [
    "none",  # Discard disabled.
    "all-untagged",  # Discard all frames that are untagged.
    "all-tagged",  # Discard all frames that are tagged.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_switch_controller_vlan_policy_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for switch_controller/vlan_policy."""
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
    """Validate required fields for switch_controller/vlan_policy."""
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


def validate_switch_controller_vlan_policy_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new switch_controller/vlan_policy object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "allowed-vlans-all" in payload:
        value = payload["allowed-vlans-all"]
        if value not in VALID_BODY_ALLOWED_VLANS_ALL:
            desc = FIELD_DESCRIPTIONS.get("allowed-vlans-all", "")
            error_msg = f"Invalid value for 'allowed-vlans-all': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ALLOWED_VLANS_ALL)}"
            error_msg += f"\n  → Example: allowed-vlans-all='{{ VALID_BODY_ALLOWED_VLANS_ALL[0] }}'"
            return (False, error_msg)
    if "discard-mode" in payload:
        value = payload["discard-mode"]
        if value not in VALID_BODY_DISCARD_MODE:
            desc = FIELD_DESCRIPTIONS.get("discard-mode", "")
            error_msg = f"Invalid value for 'discard-mode': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DISCARD_MODE)}"
            error_msg += f"\n  → Example: discard-mode='{{ VALID_BODY_DISCARD_MODE[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_switch_controller_vlan_policy_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update switch_controller/vlan_policy."""
    # Step 1: Validate enum values
    if "allowed-vlans-all" in payload:
        value = payload["allowed-vlans-all"]
        if value not in VALID_BODY_ALLOWED_VLANS_ALL:
            return (
                False,
                f"Invalid value for 'allowed-vlans-all'='{value}'. Must be one of: {', '.join(VALID_BODY_ALLOWED_VLANS_ALL)}",
            )
    if "discard-mode" in payload:
        value = payload["discard-mode"]
        if value not in VALID_BODY_DISCARD_MODE:
            return (
                False,
                f"Invalid value for 'discard-mode'='{value}'. Must be one of: {', '.join(VALID_BODY_DISCARD_MODE)}",
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
    "endpoint": "switch_controller/vlan_policy",
    "category": "cmdb",
    "api_path": "switch-controller/vlan-policy",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure VLAN policy to be applied on the managed FortiSwitch ports through dynamic-port-policy.",
    "total_fields": 8,
    "required_fields_count": 1,
    "fields_with_defaults_count": 6,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
