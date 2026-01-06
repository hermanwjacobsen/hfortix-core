"""Validation helpers for extension_controller/extender_vap - Auto-generated"""

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
    """Validate GET request parameters for extension_controller/extender_vap."""
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
    """Validate required fields for extension_controller/extender_vap."""
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
    """Validate POST request to create new extension_controller/extender_vap object."""
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
    """Validate PUT request to update extension_controller/extender_vap."""
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
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
