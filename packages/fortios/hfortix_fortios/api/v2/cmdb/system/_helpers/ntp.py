"""Validation helpers for system/ntp - Auto-generated"""

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
    """Validate GET request parameters for system/ntp."""
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
    """Validate required fields for system/ntp."""
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
    """Validate POST request to create new system/ntp object."""
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
    """Validate PUT request to update system/ntp."""
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
    "endpoint": "system/ntp",
    "category": "cmdb",
    "api_path": "system/ntp",
    "help": "Configure system NTP information.",
    "total_fields": 12,
    "required_fields_count": 1,
    "fields_with_defaults_count": 9,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
