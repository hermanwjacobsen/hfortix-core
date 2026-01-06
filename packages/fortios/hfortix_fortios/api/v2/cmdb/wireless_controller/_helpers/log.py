"""Validation helpers for wireless_controller/log - Auto-generated"""

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
    "status": "enable",
    "addrgrp-log": "notification",
    "ble-log": "notification",
    "clb-log": "notification",
    "dhcp-starv-log": "notification",
    "led-sched-log": "notification",
    "radio-event-log": "notification",
    "rogue-event-log": "notification",
    "sta-event-log": "notification",
    "sta-locate-log": "notification",
    "wids-log": "notification",
    "wtp-event-log": "notification",
    "wtp-fips-event-log": "notification",
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
    "status": "option",  # Enable/disable wireless event logging.
    "addrgrp-log": "option",  # Lowest severity level to log address group message.
    "ble-log": "option",  # Lowest severity level to log BLE detection message.
    "clb-log": "option",  # Lowest severity level to log client load balancing message.
    "dhcp-starv-log": "option",  # Lowest severity level to log DHCP starvation event message.
    "led-sched-log": "option",  # Lowest severity level to log LED schedule event message.
    "radio-event-log": "option",  # Lowest severity level to log radio event message.
    "rogue-event-log": "option",  # Lowest severity level to log rogue AP event message.
    "sta-event-log": "option",  # Lowest severity level to log station event message.
    "sta-locate-log": "option",  # Lowest severity level to log station locate message.
    "wids-log": "option",  # Lowest severity level to log WIDS message.
    "wtp-event-log": "option",  # Lowest severity level to log WTP event message.
    "wtp-fips-event-log": "option",  # Lowest severity level to log FAP fips event message.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "status": "Enable/disable wireless event logging.",
    "addrgrp-log": "Lowest severity level to log address group message.",
    "ble-log": "Lowest severity level to log BLE detection message.",
    "clb-log": "Lowest severity level to log client load balancing message.",
    "dhcp-starv-log": "Lowest severity level to log DHCP starvation event message.",
    "led-sched-log": "Lowest severity level to log LED schedule event message.",
    "radio-event-log": "Lowest severity level to log radio event message.",
    "rogue-event-log": "Lowest severity level to log rogue AP event message.",
    "sta-event-log": "Lowest severity level to log station event message.",
    "sta-locate-log": "Lowest severity level to log station locate message.",
    "wids-log": "Lowest severity level to log WIDS message.",
    "wtp-event-log": "Lowest severity level to log WTP event message.",
    "wtp-fips-event-log": "Lowest severity level to log FAP fips event message.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
}


# Valid enum values from API documentation
VALID_BODY_STATUS = [
    "enable",  # Enable wireless event logging.
    "disable",  # Disable wireless event logging.
]
VALID_BODY_ADDRGRP_LOG = [
    "emergency",  # Emergency level.
    "alert",  # Alert level.
    "critical",  # Critical level.
    "error",  # Error level.
    "warning",  # Warning level.
    "notification",  # Notification level.
    "information",  # Information level.
    "debug",  # Debug level.
]
VALID_BODY_BLE_LOG = [
    "emergency",  # Emergency level.
    "alert",  # Alert level.
    "critical",  # Critical level.
    "error",  # Error level.
    "warning",  # Warning level.
    "notification",  # Notification level.
    "information",  # Information level.
    "debug",  # Debug level.
]
VALID_BODY_CLB_LOG = [
    "emergency",  # Emergency level.
    "alert",  # Alert level.
    "critical",  # Critical level.
    "error",  # Error level.
    "warning",  # Warning level.
    "notification",  # Notification level.
    "information",  # Information level.
    "debug",  # Debug level.
]
VALID_BODY_DHCP_STARV_LOG = [
    "emergency",  # Emergency level.
    "alert",  # Alert level.
    "critical",  # Critical level.
    "error",  # Error level.
    "warning",  # Warning level.
    "notification",  # Notification level.
    "information",  # Information level.
    "debug",  # Debug level.
]
VALID_BODY_LED_SCHED_LOG = [
    "emergency",  # Emergency level.
    "alert",  # Alert level.
    "critical",  # Critical level.
    "error",  # Error level.
    "warning",  # Warning level.
    "notification",  # Notification level.
    "information",  # Information level.
    "debug",  # Debug level.
]
VALID_BODY_RADIO_EVENT_LOG = [
    "emergency",  # Emergency level.
    "alert",  # Alert level.
    "critical",  # Critical level.
    "error",  # Error level.
    "warning",  # Warning level.
    "notification",  # Notification level.
    "information",  # Information level.
    "debug",  # Debug level.
]
VALID_BODY_ROGUE_EVENT_LOG = [
    "emergency",  # Emergency level.
    "alert",  # Alert level.
    "critical",  # Critical level.
    "error",  # Error level.
    "warning",  # Warning level.
    "notification",  # Notification level.
    "information",  # Information level.
    "debug",  # Debug level.
]
VALID_BODY_STA_EVENT_LOG = [
    "emergency",  # Emergency level.
    "alert",  # Alert level.
    "critical",  # Critical level.
    "error",  # Error level.
    "warning",  # Warning level.
    "notification",  # Notification level.
    "information",  # Information level.
    "debug",  # Debug level.
]
VALID_BODY_STA_LOCATE_LOG = [
    "emergency",  # Emergency level.
    "alert",  # Alert level.
    "critical",  # Critical level.
    "error",  # Error level.
    "warning",  # Warning level.
    "notification",  # Notification level.
    "information",  # Information level.
    "debug",  # Debug level.
]
VALID_BODY_WIDS_LOG = [
    "emergency",  # Emergency level.
    "alert",  # Alert level.
    "critical",  # Critical level.
    "error",  # Error level.
    "warning",  # Warning level.
    "notification",  # Notification level.
    "information",  # Information level.
    "debug",  # Debug level.
]
VALID_BODY_WTP_EVENT_LOG = [
    "emergency",  # Emergency level.
    "alert",  # Alert level.
    "critical",  # Critical level.
    "error",  # Error level.
    "warning",  # Warning level.
    "notification",  # Notification level.
    "information",  # Information level.
    "debug",  # Debug level.
]
VALID_BODY_WTP_FIPS_EVENT_LOG = [
    "emergency",  # Emergency level.
    "alert",  # Alert level.
    "critical",  # Critical level.
    "error",  # Error level.
    "warning",  # Warning level.
    "notification",  # Notification level.
    "information",  # Information level.
    "debug",  # Debug level.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_wireless_controller_log_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for wireless_controller/log."""
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
    """Validate required fields for wireless_controller/log."""
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


def validate_wireless_controller_log_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new wireless_controller/log object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "status" in payload:
        value = payload["status"]
        if value not in VALID_BODY_STATUS:
            desc = FIELD_DESCRIPTIONS.get("status", "")
            error_msg = f"Invalid value for 'status': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_STATUS)}"
            error_msg += f"\n  → Example: status='{{ VALID_BODY_STATUS[0] }}'"
            return (False, error_msg)
    if "addrgrp-log" in payload:
        value = payload["addrgrp-log"]
        if value not in VALID_BODY_ADDRGRP_LOG:
            desc = FIELD_DESCRIPTIONS.get("addrgrp-log", "")
            error_msg = f"Invalid value for 'addrgrp-log': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ADDRGRP_LOG)}"
            error_msg += f"\n  → Example: addrgrp-log='{{ VALID_BODY_ADDRGRP_LOG[0] }}'"
            return (False, error_msg)
    if "ble-log" in payload:
        value = payload["ble-log"]
        if value not in VALID_BODY_BLE_LOG:
            desc = FIELD_DESCRIPTIONS.get("ble-log", "")
            error_msg = f"Invalid value for 'ble-log': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_BLE_LOG)}"
            error_msg += f"\n  → Example: ble-log='{{ VALID_BODY_BLE_LOG[0] }}'"
            return (False, error_msg)
    if "clb-log" in payload:
        value = payload["clb-log"]
        if value not in VALID_BODY_CLB_LOG:
            desc = FIELD_DESCRIPTIONS.get("clb-log", "")
            error_msg = f"Invalid value for 'clb-log': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CLB_LOG)}"
            error_msg += f"\n  → Example: clb-log='{{ VALID_BODY_CLB_LOG[0] }}'"
            return (False, error_msg)
    if "dhcp-starv-log" in payload:
        value = payload["dhcp-starv-log"]
        if value not in VALID_BODY_DHCP_STARV_LOG:
            desc = FIELD_DESCRIPTIONS.get("dhcp-starv-log", "")
            error_msg = f"Invalid value for 'dhcp-starv-log': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DHCP_STARV_LOG)}"
            error_msg += f"\n  → Example: dhcp-starv-log='{{ VALID_BODY_DHCP_STARV_LOG[0] }}'"
            return (False, error_msg)
    if "led-sched-log" in payload:
        value = payload["led-sched-log"]
        if value not in VALID_BODY_LED_SCHED_LOG:
            desc = FIELD_DESCRIPTIONS.get("led-sched-log", "")
            error_msg = f"Invalid value for 'led-sched-log': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LED_SCHED_LOG)}"
            error_msg += f"\n  → Example: led-sched-log='{{ VALID_BODY_LED_SCHED_LOG[0] }}'"
            return (False, error_msg)
    if "radio-event-log" in payload:
        value = payload["radio-event-log"]
        if value not in VALID_BODY_RADIO_EVENT_LOG:
            desc = FIELD_DESCRIPTIONS.get("radio-event-log", "")
            error_msg = f"Invalid value for 'radio-event-log': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_RADIO_EVENT_LOG)}"
            error_msg += f"\n  → Example: radio-event-log='{{ VALID_BODY_RADIO_EVENT_LOG[0] }}'"
            return (False, error_msg)
    if "rogue-event-log" in payload:
        value = payload["rogue-event-log"]
        if value not in VALID_BODY_ROGUE_EVENT_LOG:
            desc = FIELD_DESCRIPTIONS.get("rogue-event-log", "")
            error_msg = f"Invalid value for 'rogue-event-log': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ROGUE_EVENT_LOG)}"
            error_msg += f"\n  → Example: rogue-event-log='{{ VALID_BODY_ROGUE_EVENT_LOG[0] }}'"
            return (False, error_msg)
    if "sta-event-log" in payload:
        value = payload["sta-event-log"]
        if value not in VALID_BODY_STA_EVENT_LOG:
            desc = FIELD_DESCRIPTIONS.get("sta-event-log", "")
            error_msg = f"Invalid value for 'sta-event-log': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_STA_EVENT_LOG)}"
            error_msg += f"\n  → Example: sta-event-log='{{ VALID_BODY_STA_EVENT_LOG[0] }}'"
            return (False, error_msg)
    if "sta-locate-log" in payload:
        value = payload["sta-locate-log"]
        if value not in VALID_BODY_STA_LOCATE_LOG:
            desc = FIELD_DESCRIPTIONS.get("sta-locate-log", "")
            error_msg = f"Invalid value for 'sta-locate-log': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_STA_LOCATE_LOG)}"
            error_msg += f"\n  → Example: sta-locate-log='{{ VALID_BODY_STA_LOCATE_LOG[0] }}'"
            return (False, error_msg)
    if "wids-log" in payload:
        value = payload["wids-log"]
        if value not in VALID_BODY_WIDS_LOG:
            desc = FIELD_DESCRIPTIONS.get("wids-log", "")
            error_msg = f"Invalid value for 'wids-log': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WIDS_LOG)}"
            error_msg += f"\n  → Example: wids-log='{{ VALID_BODY_WIDS_LOG[0] }}'"
            return (False, error_msg)
    if "wtp-event-log" in payload:
        value = payload["wtp-event-log"]
        if value not in VALID_BODY_WTP_EVENT_LOG:
            desc = FIELD_DESCRIPTIONS.get("wtp-event-log", "")
            error_msg = f"Invalid value for 'wtp-event-log': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WTP_EVENT_LOG)}"
            error_msg += f"\n  → Example: wtp-event-log='{{ VALID_BODY_WTP_EVENT_LOG[0] }}'"
            return (False, error_msg)
    if "wtp-fips-event-log" in payload:
        value = payload["wtp-fips-event-log"]
        if value not in VALID_BODY_WTP_FIPS_EVENT_LOG:
            desc = FIELD_DESCRIPTIONS.get("wtp-fips-event-log", "")
            error_msg = f"Invalid value for 'wtp-fips-event-log': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WTP_FIPS_EVENT_LOG)}"
            error_msg += f"\n  → Example: wtp-fips-event-log='{{ VALID_BODY_WTP_FIPS_EVENT_LOG[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_wireless_controller_log_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update wireless_controller/log."""
    # Step 1: Validate enum values
    if "status" in payload:
        value = payload["status"]
        if value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid value for 'status'='{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )
    if "addrgrp-log" in payload:
        value = payload["addrgrp-log"]
        if value not in VALID_BODY_ADDRGRP_LOG:
            return (
                False,
                f"Invalid value for 'addrgrp-log'='{value}'. Must be one of: {', '.join(VALID_BODY_ADDRGRP_LOG)}",
            )
    if "ble-log" in payload:
        value = payload["ble-log"]
        if value not in VALID_BODY_BLE_LOG:
            return (
                False,
                f"Invalid value for 'ble-log'='{value}'. Must be one of: {', '.join(VALID_BODY_BLE_LOG)}",
            )
    if "clb-log" in payload:
        value = payload["clb-log"]
        if value not in VALID_BODY_CLB_LOG:
            return (
                False,
                f"Invalid value for 'clb-log'='{value}'. Must be one of: {', '.join(VALID_BODY_CLB_LOG)}",
            )
    if "dhcp-starv-log" in payload:
        value = payload["dhcp-starv-log"]
        if value not in VALID_BODY_DHCP_STARV_LOG:
            return (
                False,
                f"Invalid value for 'dhcp-starv-log'='{value}'. Must be one of: {', '.join(VALID_BODY_DHCP_STARV_LOG)}",
            )
    if "led-sched-log" in payload:
        value = payload["led-sched-log"]
        if value not in VALID_BODY_LED_SCHED_LOG:
            return (
                False,
                f"Invalid value for 'led-sched-log'='{value}'. Must be one of: {', '.join(VALID_BODY_LED_SCHED_LOG)}",
            )
    if "radio-event-log" in payload:
        value = payload["radio-event-log"]
        if value not in VALID_BODY_RADIO_EVENT_LOG:
            return (
                False,
                f"Invalid value for 'radio-event-log'='{value}'. Must be one of: {', '.join(VALID_BODY_RADIO_EVENT_LOG)}",
            )
    if "rogue-event-log" in payload:
        value = payload["rogue-event-log"]
        if value not in VALID_BODY_ROGUE_EVENT_LOG:
            return (
                False,
                f"Invalid value for 'rogue-event-log'='{value}'. Must be one of: {', '.join(VALID_BODY_ROGUE_EVENT_LOG)}",
            )
    if "sta-event-log" in payload:
        value = payload["sta-event-log"]
        if value not in VALID_BODY_STA_EVENT_LOG:
            return (
                False,
                f"Invalid value for 'sta-event-log'='{value}'. Must be one of: {', '.join(VALID_BODY_STA_EVENT_LOG)}",
            )
    if "sta-locate-log" in payload:
        value = payload["sta-locate-log"]
        if value not in VALID_BODY_STA_LOCATE_LOG:
            return (
                False,
                f"Invalid value for 'sta-locate-log'='{value}'. Must be one of: {', '.join(VALID_BODY_STA_LOCATE_LOG)}",
            )
    if "wids-log" in payload:
        value = payload["wids-log"]
        if value not in VALID_BODY_WIDS_LOG:
            return (
                False,
                f"Invalid value for 'wids-log'='{value}'. Must be one of: {', '.join(VALID_BODY_WIDS_LOG)}",
            )
    if "wtp-event-log" in payload:
        value = payload["wtp-event-log"]
        if value not in VALID_BODY_WTP_EVENT_LOG:
            return (
                False,
                f"Invalid value for 'wtp-event-log'='{value}'. Must be one of: {', '.join(VALID_BODY_WTP_EVENT_LOG)}",
            )
    if "wtp-fips-event-log" in payload:
        value = payload["wtp-fips-event-log"]
        if value not in VALID_BODY_WTP_FIPS_EVENT_LOG:
            return (
                False,
                f"Invalid value for 'wtp-fips-event-log'='{value}'. Must be one of: {', '.join(VALID_BODY_WTP_FIPS_EVENT_LOG)}",
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
    "endpoint": "wireless_controller/log",
    "category": "cmdb",
    "api_path": "wireless-controller/log",
    "help": "Configure wireless controller event log filters.",
    "total_fields": 13,
    "required_fields_count": 0,
    "fields_with_defaults_count": 13,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
