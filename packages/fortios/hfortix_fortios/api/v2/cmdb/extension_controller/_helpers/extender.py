"""
Validation helpers for extension_controller/extender endpoint.

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
    "name",  # FortiExtender entry name.
    "id",  # FortiExtender serial number.
    "extension-type",  # Extension type for this FortiExtender.
    "login-password",  # Set the managed extender's administrator password.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "id": "",
    "authorized": "discovered",
    "ext-name": "",
    "description": "",
    "vdom": 1,
    "device-id": 1026,
    "extension-type": "",
    "profile": "",
    "override-allowaccess": "disable",
    "allowaccess": "",
    "override-login-password-change": "disable",
    "login-password-change": "no",
    "override-enforce-bandwidth": "disable",
    "enforce-bandwidth": "disable",
    "bandwidth-limit": 1024,
    "firmware-provision-latest": "disable",
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
    "name": "string",  # FortiExtender entry name.
    "id": "string",  # FortiExtender serial number.
    "authorized": "option",  # FortiExtender Administration (enable or disable).
    "ext-name": "string",  # FortiExtender name.
    "description": "string",  # Description.
    "vdom": "integer",  # VDOM.
    "device-id": "integer",  # Device ID.
    "extension-type": "option",  # Extension type for this FortiExtender.
    "profile": "string",  # FortiExtender profile configuration.
    "override-allowaccess": "option",  # Enable to override the extender profile management access co
    "allowaccess": "option",  # Control management access to the managed extender. Separate 
    "override-login-password-change": "option",  # Enable to override the extender profile login-password (admi
    "login-password-change": "option",  # Change or reset the administrator password of a managed exte
    "login-password": "password",  # Set the managed extender's administrator password.
    "override-enforce-bandwidth": "option",  # Enable to override the extender profile enforce-bandwidth se
    "enforce-bandwidth": "option",  # Enable/disable enforcement of bandwidth on LAN extension int
    "bandwidth-limit": "integer",  # FortiExtender LAN extension bandwidth limit (Mbps).
    "wan-extension": "string",  # FortiExtender wan extension configuration.
    "firmware-provision-latest": "option",  # Enable/disable one-time automatic provisioning of the latest
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "FortiExtender entry name.",
    "id": "FortiExtender serial number.",
    "authorized": "FortiExtender Administration (enable or disable).",
    "ext-name": "FortiExtender name.",
    "description": "Description.",
    "vdom": "VDOM.",
    "device-id": "Device ID.",
    "extension-type": "Extension type for this FortiExtender.",
    "profile": "FortiExtender profile configuration.",
    "override-allowaccess": "Enable to override the extender profile management access configuration.",
    "allowaccess": "Control management access to the managed extender. Separate entries with a space.",
    "override-login-password-change": "Enable to override the extender profile login-password (administrator password) setting.",
    "login-password-change": "Change or reset the administrator password of a managed extender (yes, default, or no, default = no).",
    "login-password": "Set the managed extender's administrator password.",
    "override-enforce-bandwidth": "Enable to override the extender profile enforce-bandwidth setting.",
    "enforce-bandwidth": "Enable/disable enforcement of bandwidth on LAN extension interface.",
    "bandwidth-limit": "FortiExtender LAN extension bandwidth limit (Mbps).",
    "wan-extension": "FortiExtender wan extension configuration.",
    "firmware-provision-latest": "Enable/disable one-time automatic provisioning of the latest firmware version.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 19},
    "id": {"type": "string", "max_length": 19},
    "ext-name": {"type": "string", "max_length": 31},
    "description": {"type": "string", "max_length": 255},
    "vdom": {"type": "integer", "min": 0, "max": 4294967295},
    "device-id": {"type": "integer", "min": 0, "max": 4294967295},
    "profile": {"type": "string", "max_length": 31},
    "bandwidth-limit": {"type": "integer", "min": 1, "max": 16776000},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "wan-extension": {
        "modem1-extension": {
            "type": "string",
            "help": "FortiExtender interface name.",
            "default": "",
            "max_length": 31,
        },
        "modem2-extension": {
            "type": "string",
            "help": "FortiExtender interface name.",
            "default": "",
            "max_length": 31,
        },
        "modem1-pdn1-interface": {
            "type": "string",
            "help": "FortiExtender interface name.",
            "default": "",
            "max_length": 31,
        },
        "modem1-pdn2-interface": {
            "type": "string",
            "help": "FortiExtender interface name.",
            "default": "",
            "max_length": 31,
        },
        "modem1-pdn3-interface": {
            "type": "string",
            "help": "FortiExtender interface name.",
            "default": "",
            "max_length": 31,
        },
        "modem1-pdn4-interface": {
            "type": "string",
            "help": "FortiExtender interface name.",
            "default": "",
            "max_length": 31,
        },
        "modem2-pdn1-interface": {
            "type": "string",
            "help": "FortiExtender interface name.",
            "default": "",
            "max_length": 31,
        },
        "modem2-pdn2-interface": {
            "type": "string",
            "help": "FortiExtender interface name.",
            "default": "",
            "max_length": 31,
        },
        "modem2-pdn3-interface": {
            "type": "string",
            "help": "FortiExtender interface name.",
            "default": "",
            "max_length": 31,
        },
        "modem2-pdn4-interface": {
            "type": "string",
            "help": "FortiExtender interface name.",
            "default": "",
            "max_length": 31,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_AUTHORIZED = [
    "discovered",  # Controller discovered this FortiExtender.
    "disable",  # Controller is configured to not provide service to this FortiExtender.
    "enable",  # Controller is configured to provide service to this FortiExtender.
]
VALID_BODY_EXTENSION_TYPE = [
    "wan-extension",  # FortiExtender WAN extension mode.
    "lan-extension",  # FortiExtender LAN extension mode.
]
VALID_BODY_OVERRIDE_ALLOWACCESS = [
    "enable",  # Override the extender profile management access configuration.
    "disable",  # Use the extender profile management access configuration.
]
VALID_BODY_ALLOWACCESS = [
    "ping",  # PING access.
    "telnet",  # TELNET access.
    "http",  # HTTP access.
    "https",  # HTTPS access.
    "ssh",  # SSH access.
    "snmp",  # SNMP access.
]
VALID_BODY_OVERRIDE_LOGIN_PASSWORD_CHANGE = [
    "enable",  # Override the WTP profile login-password (administrator password) setting.
    "disable",  # Use the the WTP profile login-password (administrator password) setting.
]
VALID_BODY_LOGIN_PASSWORD_CHANGE = [
    "yes",  # Change the managed extender's administrator password. Use the login-password option to set the password.
    "default",  # Keep the managed extender's administrator password set to the factory default.
    "no",  # Do not change the managed extender's administrator password.
]
VALID_BODY_OVERRIDE_ENFORCE_BANDWIDTH = [
    "enable",  # Enable override of FortiExtender profile bandwidth setting.
    "disable",  # Disable override of FortiExtender profile bandwidth setting.
]
VALID_BODY_ENFORCE_BANDWIDTH = [
    "enable",  # Enable to enforce bandwidth limit on LAN extension interface.
    "disable",  # Disable to enforce bandwidth limit on LAN extension interface.
]
VALID_BODY_FIRMWARE_PROVISION_LATEST = [
    "disable",  # Do not automatically provision the latest available firmware.
    "once",  # Automatically attempt a one-time upgrade to the latest available firmware version.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_extension_controller_extender_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters for extension_controller/extender.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_extension_controller_extender_get()
        >>> assert is_valid == True
        
        >>> # Valid - Get specific item by name
        >>> is_valid, error = validate_extension_controller_extender_get(name="test-item")
        >>> assert is_valid == True
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_extension_controller_extender_get(
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
    Validate required fields for extension_controller/extender.

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


def validate_extension_controller_extender_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new extension_controller/extender object.

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
        ...     "name": True,  # FortiExtender entry name.
        ...     "id": True,  # FortiExtender serial number.
        ... }
        >>> is_valid, error = validate_extension_controller_extender_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "name": True,
        ...     "authorized": "{'name': 'discovered', 'help': 'Controller discovered this FortiExtender.', 'label': 'Discovered', 'description': 'Controller discovered this FortiExtender'}",  # Valid enum value
        ... }
        >>> is_valid, error = validate_extension_controller_extender_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["authorized"] = "invalid-value"
        >>> is_valid, error = validate_extension_controller_extender_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_extension_controller_extender_post(payload)
        >>> assert is_valid == False
        >>> assert "Missing required field" in error
    """
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "authorized" in payload:
        value = payload["authorized"]
        if value not in VALID_BODY_AUTHORIZED:
            desc = FIELD_DESCRIPTIONS.get("authorized", "")
            error_msg = f"Invalid value for 'authorized': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTHORIZED)}"
            error_msg += f"\n  → Example: authorized='{{ VALID_BODY_AUTHORIZED[0] }}'"
            return (False, error_msg)
    if "extension-type" in payload:
        value = payload["extension-type"]
        if value not in VALID_BODY_EXTENSION_TYPE:
            desc = FIELD_DESCRIPTIONS.get("extension-type", "")
            error_msg = f"Invalid value for 'extension-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_EXTENSION_TYPE)}"
            error_msg += f"\n  → Example: extension-type='{{ VALID_BODY_EXTENSION_TYPE[0] }}'"
            return (False, error_msg)
    if "override-allowaccess" in payload:
        value = payload["override-allowaccess"]
        if value not in VALID_BODY_OVERRIDE_ALLOWACCESS:
            desc = FIELD_DESCRIPTIONS.get("override-allowaccess", "")
            error_msg = f"Invalid value for 'override-allowaccess': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_OVERRIDE_ALLOWACCESS)}"
            error_msg += f"\n  → Example: override-allowaccess='{{ VALID_BODY_OVERRIDE_ALLOWACCESS[0] }}'"
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
    if "override-login-password-change" in payload:
        value = payload["override-login-password-change"]
        if value not in VALID_BODY_OVERRIDE_LOGIN_PASSWORD_CHANGE:
            desc = FIELD_DESCRIPTIONS.get("override-login-password-change", "")
            error_msg = f"Invalid value for 'override-login-password-change': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_OVERRIDE_LOGIN_PASSWORD_CHANGE)}"
            error_msg += f"\n  → Example: override-login-password-change='{{ VALID_BODY_OVERRIDE_LOGIN_PASSWORD_CHANGE[0] }}'"
            return (False, error_msg)
    if "login-password-change" in payload:
        value = payload["login-password-change"]
        if value not in VALID_BODY_LOGIN_PASSWORD_CHANGE:
            desc = FIELD_DESCRIPTIONS.get("login-password-change", "")
            error_msg = f"Invalid value for 'login-password-change': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LOGIN_PASSWORD_CHANGE)}"
            error_msg += f"\n  → Example: login-password-change='{{ VALID_BODY_LOGIN_PASSWORD_CHANGE[0] }}'"
            return (False, error_msg)
    if "override-enforce-bandwidth" in payload:
        value = payload["override-enforce-bandwidth"]
        if value not in VALID_BODY_OVERRIDE_ENFORCE_BANDWIDTH:
            desc = FIELD_DESCRIPTIONS.get("override-enforce-bandwidth", "")
            error_msg = f"Invalid value for 'override-enforce-bandwidth': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_OVERRIDE_ENFORCE_BANDWIDTH)}"
            error_msg += f"\n  → Example: override-enforce-bandwidth='{{ VALID_BODY_OVERRIDE_ENFORCE_BANDWIDTH[0] }}'"
            return (False, error_msg)
    if "enforce-bandwidth" in payload:
        value = payload["enforce-bandwidth"]
        if value not in VALID_BODY_ENFORCE_BANDWIDTH:
            desc = FIELD_DESCRIPTIONS.get("enforce-bandwidth", "")
            error_msg = f"Invalid value for 'enforce-bandwidth': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ENFORCE_BANDWIDTH)}"
            error_msg += f"\n  → Example: enforce-bandwidth='{{ VALID_BODY_ENFORCE_BANDWIDTH[0] }}'"
            return (False, error_msg)
    if "firmware-provision-latest" in payload:
        value = payload["firmware-provision-latest"]
        if value not in VALID_BODY_FIRMWARE_PROVISION_LATEST:
            desc = FIELD_DESCRIPTIONS.get("firmware-provision-latest", "")
            error_msg = f"Invalid value for 'firmware-provision-latest': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FIRMWARE_PROVISION_LATEST)}"
            error_msg += f"\n  → Example: firmware-provision-latest='{{ VALID_BODY_FIRMWARE_PROVISION_LATEST[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_extension_controller_extender_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update extension_controller/extender.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_extension_controller_extender_put(payload)
    """
    # Step 1: Validate enum values
    if "authorized" in payload:
        value = payload["authorized"]
        if value not in VALID_BODY_AUTHORIZED:
            return (
                False,
                f"Invalid value for 'authorized'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTHORIZED)}",
            )
    if "extension-type" in payload:
        value = payload["extension-type"]
        if value not in VALID_BODY_EXTENSION_TYPE:
            return (
                False,
                f"Invalid value for 'extension-type'='{value}'. Must be one of: {', '.join(VALID_BODY_EXTENSION_TYPE)}",
            )
    if "override-allowaccess" in payload:
        value = payload["override-allowaccess"]
        if value not in VALID_BODY_OVERRIDE_ALLOWACCESS:
            return (
                False,
                f"Invalid value for 'override-allowaccess'='{value}'. Must be one of: {', '.join(VALID_BODY_OVERRIDE_ALLOWACCESS)}",
            )
    if "allowaccess" in payload:
        value = payload["allowaccess"]
        if value not in VALID_BODY_ALLOWACCESS:
            return (
                False,
                f"Invalid value for 'allowaccess'='{value}'. Must be one of: {', '.join(VALID_BODY_ALLOWACCESS)}",
            )
    if "override-login-password-change" in payload:
        value = payload["override-login-password-change"]
        if value not in VALID_BODY_OVERRIDE_LOGIN_PASSWORD_CHANGE:
            return (
                False,
                f"Invalid value for 'override-login-password-change'='{value}'. Must be one of: {', '.join(VALID_BODY_OVERRIDE_LOGIN_PASSWORD_CHANGE)}",
            )
    if "login-password-change" in payload:
        value = payload["login-password-change"]
        if value not in VALID_BODY_LOGIN_PASSWORD_CHANGE:
            return (
                False,
                f"Invalid value for 'login-password-change'='{value}'. Must be one of: {', '.join(VALID_BODY_LOGIN_PASSWORD_CHANGE)}",
            )
    if "override-enforce-bandwidth" in payload:
        value = payload["override-enforce-bandwidth"]
        if value not in VALID_BODY_OVERRIDE_ENFORCE_BANDWIDTH:
            return (
                False,
                f"Invalid value for 'override-enforce-bandwidth'='{value}'. Must be one of: {', '.join(VALID_BODY_OVERRIDE_ENFORCE_BANDWIDTH)}",
            )
    if "enforce-bandwidth" in payload:
        value = payload["enforce-bandwidth"]
        if value not in VALID_BODY_ENFORCE_BANDWIDTH:
            return (
                False,
                f"Invalid value for 'enforce-bandwidth'='{value}'. Must be one of: {', '.join(VALID_BODY_ENFORCE_BANDWIDTH)}",
            )
    if "firmware-provision-latest" in payload:
        value = payload["firmware-provision-latest"]
        if value not in VALID_BODY_FIRMWARE_PROVISION_LATEST:
            return (
                False,
                f"Invalid value for 'firmware-provision-latest'='{value}'. Must be one of: {', '.join(VALID_BODY_FIRMWARE_PROVISION_LATEST)}",
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
    "endpoint": "extension_controller/extender",
    "category": "cmdb",
    "api_path": "extension-controller/extender",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Extender controller configuration.",
    "total_fields": 19,
    "required_fields_count": 4,
    "fields_with_defaults_count": 17,
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
