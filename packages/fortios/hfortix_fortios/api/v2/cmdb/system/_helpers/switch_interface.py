"""Validation helpers for system/switch_interface - Auto-generated"""

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
    "name",  # Interface name (name cannot be in use by any other interfaces, VLANs, or inter-VDOM links).
    "vdom",  # VDOM that the software switch belongs to.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "vdom": "",
    "span-dest-port": "",
    "type": "switch",
    "intra-switch-policy": "implicit",
    "mac-ttl": 300,
    "span": "disable",
    "span-direction": "both",
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
    "name": "string",  # Interface name (name cannot be in use by any other interface
    "vdom": "string",  # VDOM that the software switch belongs to.
    "span-dest-port": "string",  # SPAN destination port name. All traffic on the SPAN source p
    "span-source-port": "string",  # Physical interface name. Port spanning echoes all traffic on
    "member": "string",  # Names of the interfaces that belong to the virtual switch.
    "type": "option",  # Type of switch based on functionality: switch for normal fun
    "intra-switch-policy": "option",  # Allow any traffic between switch interfaces or require firew
    "mac-ttl": "integer",  # Duration for which MAC addresses are held in the ARP table (
    "span": "option",  # Enable/disable port spanning. Port spanning echoes traffic r
    "span-direction": "option",  # The direction in which the SPAN port operates, either: rx, t
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "Interface name (name cannot be in use by any other interfaces, VLANs, or inter-VDOM links).",
    "vdom": "VDOM that the software switch belongs to.",
    "span-dest-port": "SPAN destination port name. All traffic on the SPAN source ports is echoed to the SPAN destination port.",
    "span-source-port": "Physical interface name. Port spanning echoes all traffic on the SPAN source ports to the SPAN destination port.",
    "member": "Names of the interfaces that belong to the virtual switch.",
    "type": "Type of switch based on functionality: switch for normal functionality, or hub to duplicate packets to all port members.",
    "intra-switch-policy": "Allow any traffic between switch interfaces or require firewall policies to allow traffic between switch interfaces.",
    "mac-ttl": "Duration for which MAC addresses are held in the ARP table (300 - 8640000 sec, default = 300).",
    "span": "Enable/disable port spanning. Port spanning echoes traffic received by the software switch to the span destination port.",
    "span-direction": "The direction in which the SPAN port operates, either: rx, tx, or both.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 15},
    "vdom": {"type": "string", "max_length": 31},
    "span-dest-port": {"type": "string", "max_length": 15},
    "mac-ttl": {"type": "integer", "min": 300, "max": 8640000},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "span-source-port": {
        "interface-name": {
            "type": "string",
            "help": "Physical interface name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "member": {
        "interface-name": {
            "type": "string",
            "help": "Interface name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_TYPE = [
    "switch",  # Switch for normal switch functionality (available in NAT mode only).
    "hub",  # Hub to duplicate packets to all member ports.
]
VALID_BODY_INTRA_SWITCH_POLICY = [
    "implicit",  # Traffic between switch members is implicitly allowed.
    "explicit",  # Traffic between switch members must match firewall policies.
]
VALID_BODY_SPAN = [
    "disable",  # Disable port spanning.
    "enable",  # Enable port spanning.
]
VALID_BODY_SPAN_DIRECTION = [
    "rx",  # Copies only received packets from source SPAN ports to the destination SPAN port.
    "tx",  # Copies only transmitted packets from source SPAN ports to the destination SPAN port.
    "both",  # Copies both received and transmitted packets from source SPAN ports to the destination SPAN port.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_system_switch_interface_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for system/switch_interface."""
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
    """Validate required fields for system/switch_interface."""
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


def validate_system_switch_interface_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new system/switch_interface object."""
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
    if "intra-switch-policy" in payload:
        value = payload["intra-switch-policy"]
        if value not in VALID_BODY_INTRA_SWITCH_POLICY:
            desc = FIELD_DESCRIPTIONS.get("intra-switch-policy", "")
            error_msg = f"Invalid value for 'intra-switch-policy': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_INTRA_SWITCH_POLICY)}"
            error_msg += f"\n  → Example: intra-switch-policy='{{ VALID_BODY_INTRA_SWITCH_POLICY[0] }}'"
            return (False, error_msg)
    if "span" in payload:
        value = payload["span"]
        if value not in VALID_BODY_SPAN:
            desc = FIELD_DESCRIPTIONS.get("span", "")
            error_msg = f"Invalid value for 'span': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SPAN)}"
            error_msg += f"\n  → Example: span='{{ VALID_BODY_SPAN[0] }}'"
            return (False, error_msg)
    if "span-direction" in payload:
        value = payload["span-direction"]
        if value not in VALID_BODY_SPAN_DIRECTION:
            desc = FIELD_DESCRIPTIONS.get("span-direction", "")
            error_msg = f"Invalid value for 'span-direction': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SPAN_DIRECTION)}"
            error_msg += f"\n  → Example: span-direction='{{ VALID_BODY_SPAN_DIRECTION[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_system_switch_interface_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update system/switch_interface."""
    # Step 1: Validate enum values
    if "type" in payload:
        value = payload["type"]
        if value not in VALID_BODY_TYPE:
            return (
                False,
                f"Invalid value for 'type'='{value}'. Must be one of: {', '.join(VALID_BODY_TYPE)}",
            )
    if "intra-switch-policy" in payload:
        value = payload["intra-switch-policy"]
        if value not in VALID_BODY_INTRA_SWITCH_POLICY:
            return (
                False,
                f"Invalid value for 'intra-switch-policy'='{value}'. Must be one of: {', '.join(VALID_BODY_INTRA_SWITCH_POLICY)}",
            )
    if "span" in payload:
        value = payload["span"]
        if value not in VALID_BODY_SPAN:
            return (
                False,
                f"Invalid value for 'span'='{value}'. Must be one of: {', '.join(VALID_BODY_SPAN)}",
            )
    if "span-direction" in payload:
        value = payload["span-direction"]
        if value not in VALID_BODY_SPAN_DIRECTION:
            return (
                False,
                f"Invalid value for 'span-direction'='{value}'. Must be one of: {', '.join(VALID_BODY_SPAN_DIRECTION)}",
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
    "endpoint": "system/switch_interface",
    "category": "cmdb",
    "api_path": "system/switch-interface",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure software switch interfaces by grouping physical and WiFi interfaces.",
    "total_fields": 10,
    "required_fields_count": 2,
    "fields_with_defaults_count": 8,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
