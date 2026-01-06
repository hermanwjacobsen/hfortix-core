"""Validation helpers for wireless_controller/qos_profile - Auto-generated"""

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
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "comment": "",
    "uplink": 0,
    "downlink": 0,
    "uplink-sta": 0,
    "downlink-sta": 0,
    "burst": "disable",
    "wmm": "enable",
    "wmm-uapsd": "enable",
    "call-admission-control": "disable",
    "call-capacity": 10,
    "bandwidth-admission-control": "disable",
    "bandwidth-capacity": 2000,
    "dscp-wmm-mapping": "disable",
    "wmm-dscp-marking": "disable",
    "wmm-vo-dscp": 48,
    "wmm-vi-dscp": 32,
    "wmm-be-dscp": 0,
    "wmm-bk-dscp": 8,
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
    "name": "string",  # WiFi QoS profile name.
    "comment": "string",  # Comment.
    "uplink": "integer",  # Maximum uplink bandwidth for Virtual Access Points (VAPs) (0
    "downlink": "integer",  # Maximum downlink bandwidth for Virtual Access Points (VAPs) 
    "uplink-sta": "integer",  # Maximum uplink bandwidth for clients (0 - 2097152 Kbps, defa
    "downlink-sta": "integer",  # Maximum downlink bandwidth for clients (0 - 2097152 Kbps, de
    "burst": "option",  # Enable/disable client rate burst.
    "wmm": "option",  # Enable/disable WiFi multi-media (WMM) control.
    "wmm-uapsd": "option",  # Enable/disable WMM Unscheduled Automatic Power Save Delivery
    "call-admission-control": "option",  # Enable/disable WMM call admission control.
    "call-capacity": "integer",  # Maximum number of Voice over WLAN (VoWLAN) phones allowed (0
    "bandwidth-admission-control": "option",  # Enable/disable WMM bandwidth admission control.
    "bandwidth-capacity": "integer",  # Maximum bandwidth capacity allowed (1 - 600000 Kbps, default
    "dscp-wmm-mapping": "option",  # Enable/disable Differentiated Services Code Point (DSCP) map
    "dscp-wmm-vo": "string",  # DSCP mapping for voice access (default = 48 56).
    "dscp-wmm-vi": "string",  # DSCP mapping for video access (default = 32 40).
    "dscp-wmm-be": "string",  # DSCP mapping for best effort access (default = 0 24).
    "dscp-wmm-bk": "string",  # DSCP mapping for background access (default = 8 16).
    "wmm-dscp-marking": "option",  # Enable/disable WMM Differentiated Services Code Point (DSCP)
    "wmm-vo-dscp": "integer",  # DSCP marking for voice access (default = 48).
    "wmm-vi-dscp": "integer",  # DSCP marking for video access (default = 32).
    "wmm-be-dscp": "integer",  # DSCP marking for best effort access (default = 0).
    "wmm-bk-dscp": "integer",  # DSCP marking for background access (default = 8).
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "WiFi QoS profile name.",
    "comment": "Comment.",
    "uplink": "Maximum uplink bandwidth for Virtual Access Points (VAPs) (0 - 2097152 Kbps, default = 0, 0 means no limit).",
    "downlink": "Maximum downlink bandwidth for Virtual Access Points (VAPs) (0 - 2097152 Kbps, default = 0, 0 means no limit).",
    "uplink-sta": "Maximum uplink bandwidth for clients (0 - 2097152 Kbps, default = 0, 0 means no limit).",
    "downlink-sta": "Maximum downlink bandwidth for clients (0 - 2097152 Kbps, default = 0, 0 means no limit).",
    "burst": "Enable/disable client rate burst.",
    "wmm": "Enable/disable WiFi multi-media (WMM) control.",
    "wmm-uapsd": "Enable/disable WMM Unscheduled Automatic Power Save Delivery (U-APSD) power save mode.",
    "call-admission-control": "Enable/disable WMM call admission control.",
    "call-capacity": "Maximum number of Voice over WLAN (VoWLAN) phones allowed (0 - 60, default = 10).",
    "bandwidth-admission-control": "Enable/disable WMM bandwidth admission control.",
    "bandwidth-capacity": "Maximum bandwidth capacity allowed (1 - 600000 Kbps, default = 2000).",
    "dscp-wmm-mapping": "Enable/disable Differentiated Services Code Point (DSCP) mapping.",
    "dscp-wmm-vo": "DSCP mapping for voice access (default = 48 56).",
    "dscp-wmm-vi": "DSCP mapping for video access (default = 32 40).",
    "dscp-wmm-be": "DSCP mapping for best effort access (default = 0 24).",
    "dscp-wmm-bk": "DSCP mapping for background access (default = 8 16).",
    "wmm-dscp-marking": "Enable/disable WMM Differentiated Services Code Point (DSCP) marking.",
    "wmm-vo-dscp": "DSCP marking for voice access (default = 48).",
    "wmm-vi-dscp": "DSCP marking for video access (default = 32).",
    "wmm-be-dscp": "DSCP marking for best effort access (default = 0).",
    "wmm-bk-dscp": "DSCP marking for background access (default = 8).",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 35},
    "comment": {"type": "string", "max_length": 63},
    "uplink": {"type": "integer", "min": 0, "max": 2097152},
    "downlink": {"type": "integer", "min": 0, "max": 2097152},
    "uplink-sta": {"type": "integer", "min": 0, "max": 2097152},
    "downlink-sta": {"type": "integer", "min": 0, "max": 2097152},
    "call-capacity": {"type": "integer", "min": 0, "max": 60},
    "bandwidth-capacity": {"type": "integer", "min": 1, "max": 600000},
    "wmm-vo-dscp": {"type": "integer", "min": 0, "max": 63},
    "wmm-vi-dscp": {"type": "integer", "min": 0, "max": 63},
    "wmm-be-dscp": {"type": "integer", "min": 0, "max": 63},
    "wmm-bk-dscp": {"type": "integer", "min": 0, "max": 63},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "dscp-wmm-vo": {
        "id": {
            "type": "integer",
            "help": "DSCP WMM mapping numbers (0 - 63).",
            "default": 0,
            "min_value": 0,
            "max_value": 63,
        },
    },
    "dscp-wmm-vi": {
        "id": {
            "type": "integer",
            "help": "DSCP WMM mapping numbers (0 - 63).",
            "default": 0,
            "min_value": 0,
            "max_value": 63,
        },
    },
    "dscp-wmm-be": {
        "id": {
            "type": "integer",
            "help": "DSCP WMM mapping numbers (0 - 63).",
            "default": 0,
            "min_value": 0,
            "max_value": 63,
        },
    },
    "dscp-wmm-bk": {
        "id": {
            "type": "integer",
            "help": "DSCP WMM mapping numbers (0 - 63).",
            "default": 0,
            "min_value": 0,
            "max_value": 63,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_BURST = [
    "enable",  # Enable client rate burst.
    "disable",  # Disable client rate burst.
]
VALID_BODY_WMM = [
    "enable",  # Enable WiFi multi-media (WMM) control.
    "disable",  # Disable WiFi multi-media (WMM) control.
]
VALID_BODY_WMM_UAPSD = [
    "enable",  # Enable WMM Unscheduled Automatic Power Save Delivery (U-APSD) power save mode.
    "disable",  # Disable WMM Unscheduled Automatic Power Save Delivery (U-APSD) power save mode.
]
VALID_BODY_CALL_ADMISSION_CONTROL = [
    "enable",  # Enable WMM call admission control.
    "disable",  # Disable WMM call admission control.
]
VALID_BODY_BANDWIDTH_ADMISSION_CONTROL = [
    "enable",  # Enable WMM bandwidth admission control.
    "disable",  # Disable WMM bandwidth admission control.
]
VALID_BODY_DSCP_WMM_MAPPING = [
    "enable",  # Enable Differentiated Services Code Point (DSCP) mapping.
    "disable",  # Disable Differentiated Services Code Point (DSCP) mapping.
]
VALID_BODY_WMM_DSCP_MARKING = [
    "enable",  # Enable WMM Differentiated Services Code Point (DSCP) marking.
    "disable",  # Disable WMM Differentiated Services Code Point (DSCP) marking.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_wireless_controller_qos_profile_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for wireless_controller/qos_profile."""
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
    """Validate required fields for wireless_controller/qos_profile."""
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


def validate_wireless_controller_qos_profile_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new wireless_controller/qos_profile object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "burst" in payload:
        value = payload["burst"]
        if value not in VALID_BODY_BURST:
            desc = FIELD_DESCRIPTIONS.get("burst", "")
            error_msg = f"Invalid value for 'burst': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_BURST)}"
            error_msg += f"\n  → Example: burst='{{ VALID_BODY_BURST[0] }}'"
            return (False, error_msg)
    if "wmm" in payload:
        value = payload["wmm"]
        if value not in VALID_BODY_WMM:
            desc = FIELD_DESCRIPTIONS.get("wmm", "")
            error_msg = f"Invalid value for 'wmm': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WMM)}"
            error_msg += f"\n  → Example: wmm='{{ VALID_BODY_WMM[0] }}'"
            return (False, error_msg)
    if "wmm-uapsd" in payload:
        value = payload["wmm-uapsd"]
        if value not in VALID_BODY_WMM_UAPSD:
            desc = FIELD_DESCRIPTIONS.get("wmm-uapsd", "")
            error_msg = f"Invalid value for 'wmm-uapsd': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WMM_UAPSD)}"
            error_msg += f"\n  → Example: wmm-uapsd='{{ VALID_BODY_WMM_UAPSD[0] }}'"
            return (False, error_msg)
    if "call-admission-control" in payload:
        value = payload["call-admission-control"]
        if value not in VALID_BODY_CALL_ADMISSION_CONTROL:
            desc = FIELD_DESCRIPTIONS.get("call-admission-control", "")
            error_msg = f"Invalid value for 'call-admission-control': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CALL_ADMISSION_CONTROL)}"
            error_msg += f"\n  → Example: call-admission-control='{{ VALID_BODY_CALL_ADMISSION_CONTROL[0] }}'"
            return (False, error_msg)
    if "bandwidth-admission-control" in payload:
        value = payload["bandwidth-admission-control"]
        if value not in VALID_BODY_BANDWIDTH_ADMISSION_CONTROL:
            desc = FIELD_DESCRIPTIONS.get("bandwidth-admission-control", "")
            error_msg = f"Invalid value for 'bandwidth-admission-control': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_BANDWIDTH_ADMISSION_CONTROL)}"
            error_msg += f"\n  → Example: bandwidth-admission-control='{{ VALID_BODY_BANDWIDTH_ADMISSION_CONTROL[0] }}'"
            return (False, error_msg)
    if "dscp-wmm-mapping" in payload:
        value = payload["dscp-wmm-mapping"]
        if value not in VALID_BODY_DSCP_WMM_MAPPING:
            desc = FIELD_DESCRIPTIONS.get("dscp-wmm-mapping", "")
            error_msg = f"Invalid value for 'dscp-wmm-mapping': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DSCP_WMM_MAPPING)}"
            error_msg += f"\n  → Example: dscp-wmm-mapping='{{ VALID_BODY_DSCP_WMM_MAPPING[0] }}'"
            return (False, error_msg)
    if "wmm-dscp-marking" in payload:
        value = payload["wmm-dscp-marking"]
        if value not in VALID_BODY_WMM_DSCP_MARKING:
            desc = FIELD_DESCRIPTIONS.get("wmm-dscp-marking", "")
            error_msg = f"Invalid value for 'wmm-dscp-marking': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WMM_DSCP_MARKING)}"
            error_msg += f"\n  → Example: wmm-dscp-marking='{{ VALID_BODY_WMM_DSCP_MARKING[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_wireless_controller_qos_profile_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update wireless_controller/qos_profile."""
    # Step 1: Validate enum values
    if "burst" in payload:
        value = payload["burst"]
        if value not in VALID_BODY_BURST:
            return (
                False,
                f"Invalid value for 'burst'='{value}'. Must be one of: {', '.join(VALID_BODY_BURST)}",
            )
    if "wmm" in payload:
        value = payload["wmm"]
        if value not in VALID_BODY_WMM:
            return (
                False,
                f"Invalid value for 'wmm'='{value}'. Must be one of: {', '.join(VALID_BODY_WMM)}",
            )
    if "wmm-uapsd" in payload:
        value = payload["wmm-uapsd"]
        if value not in VALID_BODY_WMM_UAPSD:
            return (
                False,
                f"Invalid value for 'wmm-uapsd'='{value}'. Must be one of: {', '.join(VALID_BODY_WMM_UAPSD)}",
            )
    if "call-admission-control" in payload:
        value = payload["call-admission-control"]
        if value not in VALID_BODY_CALL_ADMISSION_CONTROL:
            return (
                False,
                f"Invalid value for 'call-admission-control'='{value}'. Must be one of: {', '.join(VALID_BODY_CALL_ADMISSION_CONTROL)}",
            )
    if "bandwidth-admission-control" in payload:
        value = payload["bandwidth-admission-control"]
        if value not in VALID_BODY_BANDWIDTH_ADMISSION_CONTROL:
            return (
                False,
                f"Invalid value for 'bandwidth-admission-control'='{value}'. Must be one of: {', '.join(VALID_BODY_BANDWIDTH_ADMISSION_CONTROL)}",
            )
    if "dscp-wmm-mapping" in payload:
        value = payload["dscp-wmm-mapping"]
        if value not in VALID_BODY_DSCP_WMM_MAPPING:
            return (
                False,
                f"Invalid value for 'dscp-wmm-mapping'='{value}'. Must be one of: {', '.join(VALID_BODY_DSCP_WMM_MAPPING)}",
            )
    if "wmm-dscp-marking" in payload:
        value = payload["wmm-dscp-marking"]
        if value not in VALID_BODY_WMM_DSCP_MARKING:
            return (
                False,
                f"Invalid value for 'wmm-dscp-marking'='{value}'. Must be one of: {', '.join(VALID_BODY_WMM_DSCP_MARKING)}",
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
    "endpoint": "wireless_controller/qos_profile",
    "category": "cmdb",
    "api_path": "wireless-controller/qos-profile",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure WiFi quality of service (QoS) profiles.",
    "total_fields": 23,
    "required_fields_count": 0,
    "fields_with_defaults_count": 19,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
