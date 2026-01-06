"""
Validation helpers for extension_controller/extender_vap endpoint.

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
    "type",  # Wi-Fi VAP type local-vap / lan-extension-vap.
    "ssid",  # Wi-Fi SSID.
    "passphrase",  # Wi-Fi passphrase.
    "sae-password",  # Wi-Fi SAE Password.
    "auth-server-address",  # Wi-Fi Authentication Server Address (IPv4 format).
    "auth-server-secret",  # Wi-Fi Authentication Server Secret.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "type": "",
    "ssid": "",
    "max-clients": 0,
    "broadcast-ssid": "enable",
    "security": "WPA2-Personal",
    "dtim": 1,
    "rts-threshold": 2347,
    "pmf": "disabled",
    "target-wake-time": "enable",
    "bss-color-partial": "enable",
    "mu-mimo": "enable",
    "auth-server-address": "",
    "auth-server-port": 0,
    "auth-server-secret": "",
    "ip-address": "0.0.0.0 0.0.0.0",
    "start-ip": "0.0.0.0",
    "end-ip": "0.0.0.0",
    "allowaccess": "",
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
    "name": "string",  # Wi-Fi VAP name.
    "type": "option",  # Wi-Fi VAP type local-vap / lan-extension-vap.
    "ssid": "string",  # Wi-Fi SSID.
    "max-clients": "integer",  # Wi-Fi max clients (0 - 512), default = 0 (no limit) 
    "broadcast-ssid": "option",  # Wi-Fi broadcast SSID enable / disable.
    "security": "option",  # Wi-Fi security.
    "dtim": "integer",  # Wi-Fi DTIM (1 - 255) default = 1.
    "rts-threshold": "integer",  # Wi-Fi RTS Threshold (256 - 2347), default = 2347 (RTS/CTS di
    "pmf": "option",  # Wi-Fi pmf enable/disable, default = disable.
    "target-wake-time": "option",  # Wi-Fi 802.11AX target wake time enable / disable, default = 
    "bss-color-partial": "option",  # Wi-Fi 802.11AX bss color partial enable / disable, default =
    "mu-mimo": "option",  # Wi-Fi multi-user MIMO enable / disable, default = enable.
    "passphrase": "password",  # Wi-Fi passphrase.
    "sae-password": "password",  # Wi-Fi SAE Password.
    "auth-server-address": "string",  # Wi-Fi Authentication Server Address (IPv4 format).
    "auth-server-port": "integer",  # Wi-Fi Authentication Server Port.
    "auth-server-secret": "string",  # Wi-Fi Authentication Server Secret.
    "ip-address": "ipv4-classnet-host",  # Extender ip address.
    "start-ip": "ipv4-address",  # Start ip address.
    "end-ip": "ipv4-address",  # End ip address.
    "allowaccess": "option",  # Control management access to the managed extender. Separate 
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "Wi-Fi VAP name.",
    "type": "Wi-Fi VAP type local-vap / lan-extension-vap.",
    "ssid": "Wi-Fi SSID.",
    "max-clients": "Wi-Fi max clients (0 - 512), default = 0 (no limit) ",
    "broadcast-ssid": "Wi-Fi broadcast SSID enable / disable.",
    "security": "Wi-Fi security.",
    "dtim": "Wi-Fi DTIM (1 - 255) default = 1.",
    "rts-threshold": "Wi-Fi RTS Threshold (256 - 2347), default = 2347 (RTS/CTS disabled).",
    "pmf": "Wi-Fi pmf enable/disable, default = disable.",
    "target-wake-time": "Wi-Fi 802.11AX target wake time enable / disable, default = enable.",
    "bss-color-partial": "Wi-Fi 802.11AX bss color partial enable / disable, default = enable.",
    "mu-mimo": "Wi-Fi multi-user MIMO enable / disable, default = enable.",
    "passphrase": "Wi-Fi passphrase.",
    "sae-password": "Wi-Fi SAE Password.",
    "auth-server-address": "Wi-Fi Authentication Server Address (IPv4 format).",
    "auth-server-port": "Wi-Fi Authentication Server Port.",
    "auth-server-secret": "Wi-Fi Authentication Server Secret.",
    "ip-address": "Extender ip address.",
    "start-ip": "Start ip address.",
    "end-ip": "End ip address.",
    "allowaccess": "Control management access to the managed extender. Separate entries with a space.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 15},
    "ssid": {"type": "string", "max_length": 32},
    "max-clients": {"type": "integer", "min": 0, "max": 512},
    "dtim": {"type": "integer", "min": 1, "max": 255},
    "rts-threshold": {"type": "integer", "min": 256, "max": 2347},
    "auth-server-address": {"type": "string", "max_length": 63},
    "auth-server-port": {"type": "integer", "min": 1, "max": 65535},
    "auth-server-secret": {"type": "string", "max_length": 63},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
}


# Valid enum values from API documentation
VALID_BODY_TYPE = [
    "local-vap",  # Local VAP.
    "lan-ext-vap",  # Lan Extension VAP.
]
VALID_BODY_BROADCAST_SSID = [
    "disable",  # Disable broadcast SSID.
    "enable",  # Enable broadcast SSID.
]
VALID_BODY_SECURITY = [
    "OPEN",  # Wi-Fi security OPEN
    "WPA2-Personal",  # Wi-Fi security WPA2 Personal
    "WPA-WPA2-Personal",  # Wi-Fi security WPA-WPA2 Personal
    "WPA3-SAE",  # Wi-Fi security WPA3 SAE
    "WPA3-SAE-Transition",  # Wi-Fi security WPA3 SAE Transition
    "WPA2-Enterprise",  # Wi-Fi security WPA2 Enterprise
    "WPA3-Enterprise-only",  # Wi-Fi security WPA3 Enterprise only
    "WPA3-Enterprise-transition",  # Wi-Fi security WPA3 Enterprise Transition
    "WPA3-Enterprise-192-bit",  # Wi-Fi security WPA3 Enterprise 192-bit
]
VALID_BODY_PMF = [
    "disabled",  # Disable PMF (Protected Management Frames).
    "optional",  # Set PMF (Protected Management Frames) optional.
    "required",  # Require PMF (Protected Management Frames).
]
VALID_BODY_TARGET_WAKE_TIME = [
    "disable",  # Disable target wake time.
    "enable",  # Enable target wake time.
]
VALID_BODY_BSS_COLOR_PARTIAL = [
    "disable",  # Disable bss color partial.
    "enable",  # Enable bss color partial.
]
VALID_BODY_MU_MIMO = [
    "disable",  # Disable multi-user MIMO.
    "enable",  # Enable multi-user MIMO.
]
VALID_BODY_ALLOWACCESS = [
    "ping",  # PING access.
    "telnet",  # TELNET access.
    "http",  # HTTP access.
    "https",  # HTTPS access.
    "ssh",  # SSH access.
    "snmp",  # SNMP access.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_extension_controller_extender_vap_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters for extension_controller/extender_vap.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_extension_controller_extender_vap_get()
        >>> assert is_valid == True
        
        >>> # Valid - Get specific item by name
        >>> is_valid, error = validate_extension_controller_extender_vap_get(name="test-item")
        >>> assert is_valid == True
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_extension_controller_extender_vap_get(
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
    Validate required fields for extension_controller/extender_vap.

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


def validate_extension_controller_extender_vap_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new extension_controller/extender_vap object.

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
        ...     "type": True,  # Wi-Fi VAP type local-vap / lan-extension-vap.
        ...     "ssid": True,  # Wi-Fi SSID.
        ... }
        >>> is_valid, error = validate_extension_controller_extender_vap_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "type": True,
        ...     "type": "{'name': 'local-vap', 'help': 'Local VAP.', 'label': 'Local Vap', 'description': 'Local VAP'}",  # Valid enum value
        ... }
        >>> is_valid, error = validate_extension_controller_extender_vap_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["type"] = "invalid-value"
        >>> is_valid, error = validate_extension_controller_extender_vap_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_extension_controller_extender_vap_post(payload)
        >>> assert is_valid == False
        >>> assert "Missing required field" in error
    """
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
    if "broadcast-ssid" in payload:
        value = payload["broadcast-ssid"]
        if value not in VALID_BODY_BROADCAST_SSID:
            desc = FIELD_DESCRIPTIONS.get("broadcast-ssid", "")
            error_msg = f"Invalid value for 'broadcast-ssid': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_BROADCAST_SSID)}"
            error_msg += f"\n  → Example: broadcast-ssid='{{ VALID_BODY_BROADCAST_SSID[0] }}'"
            return (False, error_msg)
    if "security" in payload:
        value = payload["security"]
        if value not in VALID_BODY_SECURITY:
            desc = FIELD_DESCRIPTIONS.get("security", "")
            error_msg = f"Invalid value for 'security': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SECURITY)}"
            error_msg += f"\n  → Example: security='{{ VALID_BODY_SECURITY[0] }}'"
            return (False, error_msg)
    if "pmf" in payload:
        value = payload["pmf"]
        if value not in VALID_BODY_PMF:
            desc = FIELD_DESCRIPTIONS.get("pmf", "")
            error_msg = f"Invalid value for 'pmf': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PMF)}"
            error_msg += f"\n  → Example: pmf='{{ VALID_BODY_PMF[0] }}'"
            return (False, error_msg)
    if "target-wake-time" in payload:
        value = payload["target-wake-time"]
        if value not in VALID_BODY_TARGET_WAKE_TIME:
            desc = FIELD_DESCRIPTIONS.get("target-wake-time", "")
            error_msg = f"Invalid value for 'target-wake-time': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_TARGET_WAKE_TIME)}"
            error_msg += f"\n  → Example: target-wake-time='{{ VALID_BODY_TARGET_WAKE_TIME[0] }}'"
            return (False, error_msg)
    if "bss-color-partial" in payload:
        value = payload["bss-color-partial"]
        if value not in VALID_BODY_BSS_COLOR_PARTIAL:
            desc = FIELD_DESCRIPTIONS.get("bss-color-partial", "")
            error_msg = f"Invalid value for 'bss-color-partial': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_BSS_COLOR_PARTIAL)}"
            error_msg += f"\n  → Example: bss-color-partial='{{ VALID_BODY_BSS_COLOR_PARTIAL[0] }}'"
            return (False, error_msg)
    if "mu-mimo" in payload:
        value = payload["mu-mimo"]
        if value not in VALID_BODY_MU_MIMO:
            desc = FIELD_DESCRIPTIONS.get("mu-mimo", "")
            error_msg = f"Invalid value for 'mu-mimo': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MU_MIMO)}"
            error_msg += f"\n  → Example: mu-mimo='{{ VALID_BODY_MU_MIMO[0] }}'"
            return (False, error_msg)
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

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_extension_controller_extender_vap_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update extension_controller/extender_vap.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_extension_controller_extender_vap_put(payload)
    """
    # Step 1: Validate enum values
    if "type" in payload:
        value = payload["type"]
        if value not in VALID_BODY_TYPE:
            return (
                False,
                f"Invalid value for 'type'='{value}'. Must be one of: {', '.join(VALID_BODY_TYPE)}",
            )
    if "broadcast-ssid" in payload:
        value = payload["broadcast-ssid"]
        if value not in VALID_BODY_BROADCAST_SSID:
            return (
                False,
                f"Invalid value for 'broadcast-ssid'='{value}'. Must be one of: {', '.join(VALID_BODY_BROADCAST_SSID)}",
            )
    if "security" in payload:
        value = payload["security"]
        if value not in VALID_BODY_SECURITY:
            return (
                False,
                f"Invalid value for 'security'='{value}'. Must be one of: {', '.join(VALID_BODY_SECURITY)}",
            )
    if "pmf" in payload:
        value = payload["pmf"]
        if value not in VALID_BODY_PMF:
            return (
                False,
                f"Invalid value for 'pmf'='{value}'. Must be one of: {', '.join(VALID_BODY_PMF)}",
            )
    if "target-wake-time" in payload:
        value = payload["target-wake-time"]
        if value not in VALID_BODY_TARGET_WAKE_TIME:
            return (
                False,
                f"Invalid value for 'target-wake-time'='{value}'. Must be one of: {', '.join(VALID_BODY_TARGET_WAKE_TIME)}",
            )
    if "bss-color-partial" in payload:
        value = payload["bss-color-partial"]
        if value not in VALID_BODY_BSS_COLOR_PARTIAL:
            return (
                False,
                f"Invalid value for 'bss-color-partial'='{value}'. Must be one of: {', '.join(VALID_BODY_BSS_COLOR_PARTIAL)}",
            )
    if "mu-mimo" in payload:
        value = payload["mu-mimo"]
        if value not in VALID_BODY_MU_MIMO:
            return (
                False,
                f"Invalid value for 'mu-mimo'='{value}'. Must be one of: {', '.join(VALID_BODY_MU_MIMO)}",
            )
    if "allowaccess" in payload:
        value = payload["allowaccess"]
        if value not in VALID_BODY_ALLOWACCESS:
            return (
                False,
                f"Invalid value for 'allowaccess'='{value}'. Must be one of: {', '.join(VALID_BODY_ALLOWACCESS)}",
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
    "endpoint": "extension_controller/extender_vap",
    "category": "cmdb",
    "api_path": "extension-controller/extender-vap",
    "mkey": "name",
    "mkey_type": "string",
    "help": "FortiExtender wifi vap configuration.",
    "total_fields": 21,
    "required_fields_count": 6,
    "fields_with_defaults_count": 19,
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
