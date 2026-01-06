"""
Validation helpers for system/ntp endpoint.

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
    "key",  # Key for authentication.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "ntpsync": "disable",
    "type": "fortiguard",
    "syncinterval": 60,
    "source-ip": "0.0.0.0",
    "source-ip6": "::",
    "server-mode": "disable",
    "authentication": "disable",
    "key-type": "MD5",
    "key-id": 0,
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
    "ntpsync": "option",  # Enable/disable setting the FortiGate system time by synchron
    "type": "option",  # Use the FortiGuard NTP server or any other available NTP Ser
    "syncinterval": "integer",  # NTP synchronization interval (1 - 1440 min).
    "ntpserver": "string",  # Configure the FortiGate to connect to any available third-pa
    "source-ip": "ipv4-address",  # Source IP address for communication to the NTP server.
    "source-ip6": "ipv6-address",  # Source IPv6 address for communication to the NTP server.
    "server-mode": "option",  # Enable/disable FortiGate NTP Server Mode. Your FortiGate bec
    "authentication": "option",  # Enable/disable authentication.
    "key-type": "option",  # Key type for authentication (MD5, SHA1, SHA256).
    "key": "password",  # Key for authentication.
    "key-id": "integer",  # Key ID for authentication.
    "interface": "string",  # FortiGate interface(s) with NTP server mode enabled. Devices
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "ntpsync": "Enable/disable setting the FortiGate system time by synchronizing with an NTP Server.",
    "type": "Use the FortiGuard NTP server or any other available NTP Server.",
    "syncinterval": "NTP synchronization interval (1 - 1440 min).",
    "ntpserver": "Configure the FortiGate to connect to any available third-party NTP server.",
    "source-ip": "Source IP address for communication to the NTP server.",
    "source-ip6": "Source IPv6 address for communication to the NTP server.",
    "server-mode": "Enable/disable FortiGate NTP Server Mode. Your FortiGate becomes an NTP server for other devices on your network. The FortiGate relays NTP requests to its configured NTP server.",
    "authentication": "Enable/disable authentication.",
    "key-type": "Key type for authentication (MD5, SHA1, SHA256).",
    "key": "Key for authentication.",
    "key-id": "Key ID for authentication.",
    "interface": "FortiGate interface(s) with NTP server mode enabled. Devices on your network can contact these interfaces for NTP services.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "syncinterval": {"type": "integer", "min": 1, "max": 1440},
    "key-id": {"type": "integer", "min": 0, "max": 4294967295},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "ntpserver": {
        "id": {
            "type": "integer",
            "help": "NTP server ID.",
            "required": True,
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "server": {
            "type": "string",
            "help": "IP address or hostname of the NTP Server.",
            "required": True,
            "default": "",
            "max_length": 63,
        },
        "ntpv3": {
            "type": "option",
            "help": "Enable to use NTPv3 instead of NTPv4.",
            "default": "disable",
            "options": [{"help": "Enable NTPv3.", "label": "Enable", "name": "enable"}, {"help": "Disable NTPv3 (use NTPv4).", "label": "Disable", "name": "disable"}],
        },
        "authentication": {
            "type": "option",
            "help": "Enable/disable authentication.",
            "default": "disable",
            "options": [{"help": "Enable authentication.", "label": "Enable", "name": "enable"}, {"help": "Disable authentication.", "label": "Disable", "name": "disable"}],
        },
        "key-type": {
            "type": "option",
            "help": "Select NTP authentication type.",
            "default": "MD5",
            "options": [{"help": "Enable MD5(NTPv3) authentication.", "label": "Md5", "name": "MD5"}, {"help": "Enable SHA1(NTPv4) authentication.", "label": "Sha1", "name": "SHA1"}, {"help": "Enable SHA256(NTPv4) authentication.", "label": "Sha256", "name": "SHA256"}],
        },
        "key": {
            "type": "password",
            "help": "Key for MD5(NTPv3)/SHA1(NTPv4)/SHA256(NTPv4) authentication.",
            "required": True,
            "max_length": 64,
        },
        "key-id": {
            "type": "integer",
            "help": "Key ID for authentication.",
            "required": True,
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "ip-type": {
            "type": "option",
            "help": "Choose to connect to IPv4 or/and IPv6 NTP server.",
            "default": "Both",
            "options": [{"help": "Enable look up for IPv6 NTP server.", "label": "Ipv6", "name": "IPv6"}, {"help": "Enable look up for IPv4 NTP server.", "label": "Ipv4", "name": "IPv4"}, {"help": "Enable look up for both IPv4 and IPv6 NTP server.", "label": "Both", "name": "Both"}],
        },
        "interface-select-method": {
            "type": "option",
            "help": "Specify how to select outgoing interface to reach server.",
            "default": "auto",
            "options": [{"help": "Set outgoing interface automatically.", "label": "Auto", "name": "auto"}, {"help": "Set outgoing interface by SD-WAN or policy routing rules.", "label": "Sdwan", "name": "sdwan"}, {"help": "Set outgoing interface manually.", "label": "Specify", "name": "specify"}],
        },
        "interface": {
            "type": "string",
            "help": "Specify outgoing interface to reach server.",
            "required": True,
            "default": "",
            "max_length": 15,
        },
        "vrf-select": {
            "type": "integer",
            "help": "VRF ID used for connection to server.",
            "default": 0,
            "min_value": 0,
            "max_value": 511,
        },
    },
    "interface": {
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
VALID_BODY_NTPSYNC = [
    "enable",  # Enable synchronization with NTP Server.
    "disable",  # Disable synchronization with NTP Server.
]
VALID_BODY_TYPE = [
    "fortiguard",  # Use the FortiGuard NTP server.
    "custom",  # Use any other available NTP server.
]
VALID_BODY_SERVER_MODE = [
    "enable",  # Enable FortiGate NTP Server Mode.
    "disable",  # Disable FortiGate NTP Server Mode.
]
VALID_BODY_AUTHENTICATION = [
    "enable",  # Enable authentication.
    "disable",  # Disable authentication.
]
VALID_BODY_KEY_TYPE = [
    "MD5",  # Use MD5 to authenticate the message.
    "SHA1",  # Use SHA1 to authenticate the message.
    "SHA256",  # Use SHA256 to authenticate the message.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_system_ntp_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters for system/ntp.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_system_ntp_get()
        >>> assert is_valid == True
        
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_system_ntp_get(
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
    Validate required fields for system/ntp.

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


def validate_system_ntp_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new system/ntp object.

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
        ...     "key": True,  # Key for authentication.
        ... }
        >>> is_valid, error = validate_system_ntp_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "key": True,
        ...     "ntpsync": "{'name': 'enable', 'help': 'Enable synchronization with NTP Server.', 'label': 'Enable', 'description': 'Enable synchronization with NTP Server'}",  # Valid enum value
        ... }
        >>> is_valid, error = validate_system_ntp_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["ntpsync"] = "invalid-value"
        >>> is_valid, error = validate_system_ntp_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_system_ntp_post(payload)
        >>> assert is_valid == False
        >>> assert "Missing required field" in error
    """
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "ntpsync" in payload:
        value = payload["ntpsync"]
        if value not in VALID_BODY_NTPSYNC:
            desc = FIELD_DESCRIPTIONS.get("ntpsync", "")
            error_msg = f"Invalid value for 'ntpsync': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_NTPSYNC)}"
            error_msg += f"\n  → Example: ntpsync='{{ VALID_BODY_NTPSYNC[0] }}'"
            return (False, error_msg)
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
    if "server-mode" in payload:
        value = payload["server-mode"]
        if value not in VALID_BODY_SERVER_MODE:
            desc = FIELD_DESCRIPTIONS.get("server-mode", "")
            error_msg = f"Invalid value for 'server-mode': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SERVER_MODE)}"
            error_msg += f"\n  → Example: server-mode='{{ VALID_BODY_SERVER_MODE[0] }}'"
            return (False, error_msg)
    if "authentication" in payload:
        value = payload["authentication"]
        if value not in VALID_BODY_AUTHENTICATION:
            desc = FIELD_DESCRIPTIONS.get("authentication", "")
            error_msg = f"Invalid value for 'authentication': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTHENTICATION)}"
            error_msg += f"\n  → Example: authentication='{{ VALID_BODY_AUTHENTICATION[0] }}'"
            return (False, error_msg)
    if "key-type" in payload:
        value = payload["key-type"]
        if value not in VALID_BODY_KEY_TYPE:
            desc = FIELD_DESCRIPTIONS.get("key-type", "")
            error_msg = f"Invalid value for 'key-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_KEY_TYPE)}"
            error_msg += f"\n  → Example: key-type='{{ VALID_BODY_KEY_TYPE[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_system_ntp_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update system/ntp.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_system_ntp_put(payload)
    """
    # Step 1: Validate enum values
    if "ntpsync" in payload:
        value = payload["ntpsync"]
        if value not in VALID_BODY_NTPSYNC:
            return (
                False,
                f"Invalid value for 'ntpsync'='{value}'. Must be one of: {', '.join(VALID_BODY_NTPSYNC)}",
            )
    if "type" in payload:
        value = payload["type"]
        if value not in VALID_BODY_TYPE:
            return (
                False,
                f"Invalid value for 'type'='{value}'. Must be one of: {', '.join(VALID_BODY_TYPE)}",
            )
    if "server-mode" in payload:
        value = payload["server-mode"]
        if value not in VALID_BODY_SERVER_MODE:
            return (
                False,
                f"Invalid value for 'server-mode'='{value}'. Must be one of: {', '.join(VALID_BODY_SERVER_MODE)}",
            )
    if "authentication" in payload:
        value = payload["authentication"]
        if value not in VALID_BODY_AUTHENTICATION:
            return (
                False,
                f"Invalid value for 'authentication'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTHENTICATION)}",
            )
    if "key-type" in payload:
        value = payload["key-type"]
        if value not in VALID_BODY_KEY_TYPE:
            return (
                False,
                f"Invalid value for 'key-type'='{value}'. Must be one of: {', '.join(VALID_BODY_KEY_TYPE)}",
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
    "endpoint": "system/ntp",
    "category": "cmdb",
    "api_path": "system/ntp",
    "help": "Configure system NTP information.",
    "total_fields": 12,
    "required_fields_count": 1,
    "fields_with_defaults_count": 9,
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
