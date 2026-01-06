"""
Validation helpers for switch_controller/lldp_profile endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification
Customize as needed for endpoint-specific business logic.
"""

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
#
# 1. FALSE POSITIVES: Some fields marked "required" have default values,
#    meaning they're optional (filtered out by generator)
#
# 2. CONDITIONAL REQUIREMENTS: Many endpoints require EITHER field A OR field B:
#    - firewall.policy: requires (srcaddr + dstaddr) OR (srcaddr6 + dstaddr6)
#    - These conditional requirements cannot be expressed in a simple list
#
# 3. SPECIALIZED FEATURES: Fields for WAN optimization, VPN, NAT64, etc.
#    are marked "required" but only apply when using those features
#
# The REQUIRED_FIELDS list below is INFORMATIONAL ONLY and shows fields that:
# - Are marked required in the schema
# - Don't have non-empty default values
# - Aren't specialized feature fields
#
# Do NOT use this list for strict validation - test with the actual FortiOS API!

# Fields marked as required (after filtering false positives)
REQUIRED_FIELDS = [
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "med-tlvs": "",
    "802.1-tlvs": "",
    "802.3-tlvs": "",
    "auto-isl": "enable",
    "auto-isl-hello-timer": 3,
    "auto-isl-receive-timeout": 60,
    "auto-isl-port-group": 0,
    "auto-mclag-icl": "disable",
    "auto-isl-auth": "legacy",
    "auto-isl-auth-user": "",
    "auto-isl-auth-identity": "",
    "auto-isl-auth-reauth": 3600,
    "auto-isl-auth-encrypt": "none",
    "auto-isl-auth-macsec-profile": "",
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
    "name": "string",  # Profile name.
    "med-tlvs": "option",  # Transmitted LLDP-MED TLVs (type-length-value descriptions).
    "802.1-tlvs": "option",  # Transmitted IEEE 802.1 TLVs.
    "802.3-tlvs": "option",  # Transmitted IEEE 802.3 TLVs.
    "auto-isl": "option",  # Enable/disable auto inter-switch LAG.
    "auto-isl-hello-timer": "integer",  # Auto inter-switch LAG hello timer duration (1 - 30 sec, defa
    "auto-isl-receive-timeout": "integer",  # Auto inter-switch LAG timeout if no response is received (3 
    "auto-isl-port-group": "integer",  # Auto inter-switch LAG port group ID (0 - 9).
    "auto-mclag-icl": "option",  # Enable/disable MCLAG inter chassis link.
    "auto-isl-auth": "option",  # Auto inter-switch LAG authentication mode.
    "auto-isl-auth-user": "string",  # Auto inter-switch LAG authentication user certificate.
    "auto-isl-auth-identity": "string",  # Auto inter-switch LAG authentication identity.
    "auto-isl-auth-reauth": "integer",  # Auto inter-switch LAG authentication reauth period in second
    "auto-isl-auth-encrypt": "option",  # Auto inter-switch LAG encryption mode.
    "auto-isl-auth-macsec-profile": "string",  # Auto inter-switch LAG macsec profile for encryption.
    "med-network-policy": "string",  # Configuration method to edit Media Endpoint Discovery (MED) 
    "med-location-service": "string",  # Configuration method to edit Media Endpoint Discovery (MED) 
    "custom-tlvs": "string",  # Configuration method to edit custom TLV entries.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "Profile name.",
    "med-tlvs": "Transmitted LLDP-MED TLVs (type-length-value descriptions).",
    "802.1-tlvs": "Transmitted IEEE 802.1 TLVs.",
    "802.3-tlvs": "Transmitted IEEE 802.3 TLVs.",
    "auto-isl": "Enable/disable auto inter-switch LAG.",
    "auto-isl-hello-timer": "Auto inter-switch LAG hello timer duration (1 - 30 sec, default = 3).",
    "auto-isl-receive-timeout": "Auto inter-switch LAG timeout if no response is received (3 - 90 sec, default = 9).",
    "auto-isl-port-group": "Auto inter-switch LAG port group ID (0 - 9).",
    "auto-mclag-icl": "Enable/disable MCLAG inter chassis link.",
    "auto-isl-auth": "Auto inter-switch LAG authentication mode.",
    "auto-isl-auth-user": "Auto inter-switch LAG authentication user certificate.",
    "auto-isl-auth-identity": "Auto inter-switch LAG authentication identity.",
    "auto-isl-auth-reauth": "Auto inter-switch LAG authentication reauth period in seconds(10 - 3600, default = 3600).",
    "auto-isl-auth-encrypt": "Auto inter-switch LAG encryption mode.",
    "auto-isl-auth-macsec-profile": "Auto inter-switch LAG macsec profile for encryption.",
    "med-network-policy": "Configuration method to edit Media Endpoint Discovery (MED) network policy type-length-value (TLV) categories.",
    "med-location-service": "Configuration method to edit Media Endpoint Discovery (MED) location service type-length-value (TLV) categories.",
    "custom-tlvs": "Configuration method to edit custom TLV entries.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 63},
    "auto-isl-hello-timer": {"type": "integer", "min": 1, "max": 30},
    "auto-isl-receive-timeout": {"type": "integer", "min": 0, "max": 90},
    "auto-isl-port-group": {"type": "integer", "min": 0, "max": 9},
    "auto-isl-auth-user": {"type": "string", "max_length": 63},
    "auto-isl-auth-identity": {"type": "string", "max_length": 63},
    "auto-isl-auth-reauth": {"type": "integer", "min": 180, "max": 3600},
    "auto-isl-auth-macsec-profile": {"type": "string", "max_length": 63},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "med-network-policy": {
        "name": {
            "type": "string",
            "help": "Policy type name.",
            "default": "",
            "max_length": 63,
        },
        "status": {
            "type": "option",
            "help": "Enable or disable this TLV.",
            "default": "disable",
            "options": [{"help": "Do not transmit this network policy TLV.", "label": "Disable", "name": "disable"}, {"help": "Transmit this TLV if a VLAN has been addded to the port.", "label": "Enable", "name": "enable"}],
        },
        "vlan-intf": {
            "type": "string",
            "help": "VLAN interface to advertise; if configured on port.",
            "default": "",
            "max_length": 15,
        },
        "assign-vlan": {
            "type": "option",
            "help": "Enable/disable VLAN assignment when this profile is applied on managed FortiSwitch port.",
            "default": "disable",
            "options": [{"help": "Disable VLAN assignment when this profile is applied on port.", "label": "Disable", "name": "disable"}, {"help": "Enable VLAN assignment when this profile is applied on port.", "label": "Enable", "name": "enable"}],
        },
        "priority": {
            "type": "integer",
            "help": "Advertised Layer 2 priority (0 - 7; from lowest to highest priority).",
            "default": 0,
            "min_value": 0,
            "max_value": 7,
        },
        "dscp": {
            "type": "integer",
            "help": "Advertised Differentiated Services Code Point (DSCP) value, a packet header value indicating the level of service requested for traffic, such as high priority or best effort delivery.",
            "default": 0,
            "min_value": 0,
            "max_value": 63,
        },
    },
    "med-location-service": {
        "name": {
            "type": "string",
            "help": "Location service type name.",
            "default": "",
            "max_length": 63,
        },
        "status": {
            "type": "option",
            "help": "Enable or disable this TLV.",
            "default": "disable",
            "options": [{"help": "Do not transmit this location service TLV.", "label": "Disable", "name": "disable"}, {"help": "Transmit this location service TLV.", "label": "Enable", "name": "enable"}],
        },
        "sys-location-id": {
            "type": "string",
            "help": "Location service ID.",
            "default": "",
            "max_length": 63,
        },
    },
    "custom-tlvs": {
        "name": {
            "type": "string",
            "help": "TLV name (not sent).",
            "default": "",
            "max_length": 63,
        },
        "oui": {
            "type": "user",
            "help": "Organizationally unique identifier (OUI), a 3-byte hexadecimal number, for this TLV.",
            "required": True,
            "default": "000000",
        },
        "subtype": {
            "type": "integer",
            "help": "Organizationally defined subtype (0 - 255).",
            "default": 0,
            "min_value": 0,
            "max_value": 255,
        },
        "information-string": {
            "type": "user",
            "help": "Organizationally defined information string (0 - 507 hexadecimal bytes).",
            "default": "",
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_MED_TLVS = [
    "inventory-management",  # Inventory management TLVs.
    "network-policy",  # Network policy TLVs.
    "power-management",  # Power manangement TLVs.
    "location-identification",  # Location identificaion TLVs.
]
VALID_BODY_802_1_TLVS = [
    "port-vlan-id",  # Port native VLAN TLV.
]
VALID_BODY_802_3_TLVS = [
    "max-frame-size",  # Maximum frame size TLV.
    "power-negotiation",  # PoE+ classification TLV.
]
VALID_BODY_AUTO_ISL = [
    "disable",  # Disable automatic MCLAG inter chassis link.
    "enable",  # Enable automatic MCLAG inter chassis link.
]
VALID_BODY_AUTO_MCLAG_ICL = [
    "disable",  # Disable auto inter-switch-LAG.
    "enable",  # Enable auto inter-switch-LAG.
]
VALID_BODY_AUTO_ISL_AUTH = [
    "legacy",  # No auto inter-switch-LAG authentication.
    "strict",  # Strict auto inter-switch-LAG authentication.
    "relax",  # Relax auto inter-switch-LAG authentication.
]
VALID_BODY_AUTO_ISL_AUTH_ENCRYPT = [
    "none",  # No auto inter-switch-LAG encryption.
    "mixed",  # Mixed auto inter-switch-LAG encryption.
    "must",  # Must auto inter-switch-LAG encryption.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_switch_controller_lldp_profile_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters for switch_controller/lldp_profile.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_switch_controller_lldp_profile_get()
        >>> assert is_valid == True
        
        >>> # Valid - Get specific item by name
        >>> is_valid, error = validate_switch_controller_lldp_profile_get(name="test-item")
        >>> assert is_valid == True
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_switch_controller_lldp_profile_get(
        ...     filters={"format": "name|type"}
        ... )
        >>> assert is_valid == True
    """
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
    """
    Validate required fields for switch_controller/lldp_profile.

    This validator checks:
    1. Always-required fields are present
    2. Mutually exclusive groups have at least one field

    Args:
        payload: The request payload to validate

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "test"}
        >>> is_valid, error = validate_required_fields(payload)
    """
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


def validate_switch_controller_lldp_profile_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new switch_controller/lldp_profile object.

    This validator performs two-stage validation:
    1. Required fields check (schema-based)
    2. Field value validation (enums, ranges, formats)

    Args:
        payload: Request body data with configuration
        **params: Query parameters (vdom, etc.)

    Returns:
        Tuple of (is_valid, error_message)
        - is_valid: True if payload is valid, False otherwise
        - error_message: None if valid, detailed error string if invalid

    Examples:
        >>> # ✅ Valid - Minimal required fields
        >>> payload = {
        ... }
        >>> is_valid, error = validate_switch_controller_lldp_profile_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "med-tlvs": "{'name': 'inventory-management', 'help': 'Inventory management TLVs.', 'label': 'Inventory Management', 'description': 'Inventory management TLVs'}",  # Valid enum value
        ... }
        >>> is_valid, error = validate_switch_controller_lldp_profile_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["med-tlvs"] = "invalid-value"
        >>> is_valid, error = validate_switch_controller_lldp_profile_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_switch_controller_lldp_profile_post(payload)
        >>> assert is_valid == False
        >>> assert "Missing required field" in error
    """
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "med-tlvs" in payload:
        value = payload["med-tlvs"]
        if value not in VALID_BODY_MED_TLVS:
            desc = FIELD_DESCRIPTIONS.get("med-tlvs", "")
            error_msg = f"Invalid value for 'med-tlvs': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MED_TLVS)}"
            error_msg += f"\n  → Example: med-tlvs='{{ VALID_BODY_MED_TLVS[0] }}'"
            return (False, error_msg)
    if "802.1-tlvs" in payload:
        value = payload["802.1-tlvs"]
        if value not in VALID_BODY_802_1_TLVS:
            desc = FIELD_DESCRIPTIONS.get("802.1-tlvs", "")
            error_msg = f"Invalid value for '802.1-tlvs': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_802_1_TLVS)}"
            error_msg += f"\n  → Example: 802.1-tlvs='{{ VALID_BODY_802_1_TLVS[0] }}'"
            return (False, error_msg)
    if "802.3-tlvs" in payload:
        value = payload["802.3-tlvs"]
        if value not in VALID_BODY_802_3_TLVS:
            desc = FIELD_DESCRIPTIONS.get("802.3-tlvs", "")
            error_msg = f"Invalid value for '802.3-tlvs': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_802_3_TLVS)}"
            error_msg += f"\n  → Example: 802.3-tlvs='{{ VALID_BODY_802_3_TLVS[0] }}'"
            return (False, error_msg)
    if "auto-isl" in payload:
        value = payload["auto-isl"]
        if value not in VALID_BODY_AUTO_ISL:
            desc = FIELD_DESCRIPTIONS.get("auto-isl", "")
            error_msg = f"Invalid value for 'auto-isl': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTO_ISL)}"
            error_msg += f"\n  → Example: auto-isl='{{ VALID_BODY_AUTO_ISL[0] }}'"
            return (False, error_msg)
    if "auto-mclag-icl" in payload:
        value = payload["auto-mclag-icl"]
        if value not in VALID_BODY_AUTO_MCLAG_ICL:
            desc = FIELD_DESCRIPTIONS.get("auto-mclag-icl", "")
            error_msg = f"Invalid value for 'auto-mclag-icl': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTO_MCLAG_ICL)}"
            error_msg += f"\n  → Example: auto-mclag-icl='{{ VALID_BODY_AUTO_MCLAG_ICL[0] }}'"
            return (False, error_msg)
    if "auto-isl-auth" in payload:
        value = payload["auto-isl-auth"]
        if value not in VALID_BODY_AUTO_ISL_AUTH:
            desc = FIELD_DESCRIPTIONS.get("auto-isl-auth", "")
            error_msg = f"Invalid value for 'auto-isl-auth': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTO_ISL_AUTH)}"
            error_msg += f"\n  → Example: auto-isl-auth='{{ VALID_BODY_AUTO_ISL_AUTH[0] }}'"
            return (False, error_msg)
    if "auto-isl-auth-encrypt" in payload:
        value = payload["auto-isl-auth-encrypt"]
        if value not in VALID_BODY_AUTO_ISL_AUTH_ENCRYPT:
            desc = FIELD_DESCRIPTIONS.get("auto-isl-auth-encrypt", "")
            error_msg = f"Invalid value for 'auto-isl-auth-encrypt': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTO_ISL_AUTH_ENCRYPT)}"
            error_msg += f"\n  → Example: auto-isl-auth-encrypt='{{ VALID_BODY_AUTO_ISL_AUTH_ENCRYPT[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_switch_controller_lldp_profile_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update switch_controller/lldp_profile.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_switch_controller_lldp_profile_put(payload)
    """
    # Step 1: Validate enum values
    if "med-tlvs" in payload:
        value = payload["med-tlvs"]
        if value not in VALID_BODY_MED_TLVS:
            return (
                False,
                f"Invalid value for 'med-tlvs'='{value}'. Must be one of: {', '.join(VALID_BODY_MED_TLVS)}",
            )
    if "802.1-tlvs" in payload:
        value = payload["802.1-tlvs"]
        if value not in VALID_BODY_802_1_TLVS:
            return (
                False,
                f"Invalid value for '802.1-tlvs'='{value}'. Must be one of: {', '.join(VALID_BODY_802_1_TLVS)}",
            )
    if "802.3-tlvs" in payload:
        value = payload["802.3-tlvs"]
        if value not in VALID_BODY_802_3_TLVS:
            return (
                False,
                f"Invalid value for '802.3-tlvs'='{value}'. Must be one of: {', '.join(VALID_BODY_802_3_TLVS)}",
            )
    if "auto-isl" in payload:
        value = payload["auto-isl"]
        if value not in VALID_BODY_AUTO_ISL:
            return (
                False,
                f"Invalid value for 'auto-isl'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTO_ISL)}",
            )
    if "auto-mclag-icl" in payload:
        value = payload["auto-mclag-icl"]
        if value not in VALID_BODY_AUTO_MCLAG_ICL:
            return (
                False,
                f"Invalid value for 'auto-mclag-icl'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTO_MCLAG_ICL)}",
            )
    if "auto-isl-auth" in payload:
        value = payload["auto-isl-auth"]
        if value not in VALID_BODY_AUTO_ISL_AUTH:
            return (
                False,
                f"Invalid value for 'auto-isl-auth'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTO_ISL_AUTH)}",
            )
    if "auto-isl-auth-encrypt" in payload:
        value = payload["auto-isl-auth-encrypt"]
        if value not in VALID_BODY_AUTO_ISL_AUTH_ENCRYPT:
            return (
                False,
                f"Invalid value for 'auto-isl-auth-encrypt'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTO_ISL_AUTH_ENCRYPT)}",
            )

    return (True, None)


# ============================================================================
# Metadata Access Functions
# Provide programmatic access to field metadata for IDE autocomplete,
# documentation generation, and dynamic validation
# ============================================================================


def get_field_description(field_name: str) -> str | None:
    """
    Get description/help text for a field.

    Args:
        field_name: Name of the field

    Returns:
        Description text or None if field doesn't exist

    Example:
        >>> desc = get_field_description("name")
        >>> print(desc)
    """
    return FIELD_DESCRIPTIONS.get(field_name)


def get_field_type(field_name: str) -> str | None:
    """
    Get the type of a field.

    Args:
        field_name: Name of the field

    Returns:
        Field type (e.g., "string", "integer", "option") or None

    Example:
        >>> field_type = get_field_type("status")
        >>> print(field_type)  # "option"
    """
    return FIELD_TYPES.get(field_name)


def get_field_constraints(field_name: str) -> dict[str, Any] | None:
    """
    Get constraints for a field (min/max values, string length).

    Args:
        field_name: Name of the field

    Returns:
        Constraint dict or None

    Example:
        >>> constraints = get_field_constraints("port")
        >>> print(constraints)  # {"type": "integer", "min": 1, "max": 65535}
    """
    return FIELD_CONSTRAINTS.get(field_name)


def get_field_default(field_name: str) -> Any | None:
    """
    Get default value for a field.

    Args:
        field_name: Name of the field

    Returns:
        Default value or None if no default

    Example:
        >>> default = get_field_default("status")
        >>> print(default)  # "enable"
    """
    return FIELDS_WITH_DEFAULTS.get(field_name)


def get_field_options(field_name: str) -> list[str] | None:
    """
    Get valid enum options for a field.

    Args:
        field_name: Name of the field

    Returns:
        List of valid values or None if not an enum field

    Example:
        >>> options = get_field_options("status")
        >>> print(options)  # ["enable", "disable"]
    """
    # Construct the constant name from field name
    # Replace all non-alphanumeric characters with underscores for valid Python identifiers
    import re
    safe_name = re.sub(r'[^a-zA-Z0-9]', '_', field_name)
    constant_name = f"VALID_BODY_{safe_name.upper()}"
    return globals().get(constant_name)


def get_nested_schema(field_name: str) -> dict[str, Any] | None:
    """
    Get schema for nested table/list fields.

    Args:
        field_name: Name of the parent field

    Returns:
        Dict mapping child field names to their metadata

    Example:
        >>> nested = get_nested_schema("members")
        >>> if nested:
        ...     for child_field, child_meta in nested.items():
        ...         print(f"{child_field}: {child_meta['type']}")
    """
    return NESTED_SCHEMAS.get(field_name)


def get_all_fields() -> list[str]:
    """
    Get list of all field names.

    Returns:
        List of all field names in the schema

    Example:
        >>> fields = get_all_fields()
        >>> print(len(fields))
    """
    return list(FIELD_TYPES.keys())


def get_field_metadata(field_name: str) -> dict[str, Any] | None:
    """
    Get complete metadata for a field (type, description, constraints, defaults, options).

    Args:
        field_name: Name of the field

    Returns:
        Dict with all available metadata or None if field doesn't exist

    Example:
        >>> meta = get_field_metadata("status")
        >>> print(meta)
        >>> # {
        >>> #   "type": "option",
        >>> #   "description": "Enable/disable this feature",
        >>> #   "default": "enable",
        >>> #   "options": ["enable", "disable"]
        >>> # }
    """
    if field_name not in FIELD_TYPES:
        return None

    metadata = {
        "name": field_name,
        "type": FIELD_TYPES[field_name],
    }

    # Add description if available
    if field_name in FIELD_DESCRIPTIONS:
        metadata["description"] = FIELD_DESCRIPTIONS[field_name]

    # Add constraints if available
    if field_name in FIELD_CONSTRAINTS:
        metadata["constraints"] = FIELD_CONSTRAINTS[field_name]

    # Add default if available
    if field_name in FIELDS_WITH_DEFAULTS:
        metadata["default"] = FIELDS_WITH_DEFAULTS[field_name]

    # Add required flag
    metadata["required"] = field_name in REQUIRED_FIELDS

    # Add options if available
    options = get_field_options(field_name)
    if options:
        metadata["options"] = options

    # Add nested schema if available
    nested = get_nested_schema(field_name)
    if nested:
        metadata["nested_schema"] = nested

    return metadata


def validate_field_value(field_name: str, value: Any) -> tuple[bool, str | None]:
    """
    Validate a single field value against its constraints.

    Args:
        field_name: Name of the field
        value: Value to validate

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> is_valid, error = validate_field_value("status", "enable")
        >>> if not is_valid:
        ...     print(error)
    """
    # Get field metadata
    field_type = get_field_type(field_name)
    if field_type is None:
        return (False, f"Unknown field: '{field_name}' (not defined in schema)")

    # Get field description for better error context
    description = get_field_description(field_name)

    # Validate enum values
    options = get_field_options(field_name)
    if options and value not in options:
        error_msg = f"Invalid value for '{field_name}': {repr(value)}"
        if description:
            error_msg += f"\n  → Description: {description}"
        error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in options)}"
        if options:
            error_msg += f"\n  → Example: {field_name}={repr(options[0])}"
        return (False, error_msg)

    # Validate constraints
    constraints = get_field_constraints(field_name)
    if constraints:
        constraint_type = constraints.get("type")

        if constraint_type == "integer":
            if not isinstance(value, int):
                error_msg = f"Field '{field_name}' must be an integer"
                if description:
                    error_msg += f"\n  → Description: {description}"
                error_msg += f"\n  → You provided: {type(value).__name__} = {repr(value)}"
                return (False, error_msg)

            min_val = constraints.get("min")
            max_val = constraints.get("max")

            if min_val is not None and value < min_val:
                error_msg = f"Field '{field_name}' value {value} is below minimum {min_val}"
                if description:
                    error_msg += f"\n  → Description: {description}"
                if max_val is not None:
                    error_msg += f"\n  → Valid range: {min_val} to {max_val}"
                return (False, error_msg)

            if max_val is not None and value > max_val:
                error_msg = f"Field '{field_name}' value {value} exceeds maximum {max_val}"
                if description:
                    error_msg += f"\n  → Description: {description}"
                if min_val is not None:
                    error_msg += f"\n  → Valid range: {min_val} to {max_val}"
                return (False, error_msg)

        elif constraint_type == "string":
            if not isinstance(value, str):
                error_msg = f"Field '{field_name}' must be a string"
                if description:
                    error_msg += f"\n  → Description: {description}"
                error_msg += f"\n  → You provided: {type(value).__name__} = {repr(value)}"
                return (False, error_msg)

            max_length = constraints.get("max_length")
            if max_length and len(value) > max_length:
                error_msg = f"Field '{field_name}' length {len(value)} exceeds maximum {max_length}"
                if description:
                    error_msg += f"\n  → Description: {description}"
                error_msg += f"\n  → Your value: {repr(value[:50])}{'...' if len(value) > 50 else ''}"
                return (False, error_msg)

    return (True, None)


# ============================================================================
# Schema Information
# Metadata about this endpoint schema
# ============================================================================

SCHEMA_INFO = {
    "endpoint": "switch_controller/lldp_profile",
    "category": "cmdb",
    "api_path": "switch-controller/lldp-profile",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure FortiSwitch LLDP profiles.",
    "total_fields": 18,
    "required_fields_count": 0,
    "fields_with_defaults_count": 15,
}


def get_schema_info() -> dict[str, Any]:
    """
    Get information about this endpoint schema.

    Returns:
        Dict with schema metadata

    Example:
        >>> info = get_schema_info()
        >>> print(f"Endpoint: {info['endpoint']}")
        >>> print(f"Total fields: {info['total_fields']}")
    """
    return SCHEMA_INFO.copy()
