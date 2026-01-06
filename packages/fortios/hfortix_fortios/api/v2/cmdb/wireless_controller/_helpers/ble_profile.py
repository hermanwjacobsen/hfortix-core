"""Validation helpers for wireless_controller/ble_profile - Auto-generated"""

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
    "advertising": "",
    "ibeacon-uuid": "005ea414-cbd1-11e5-9956-625662870761",
    "major-id": 1000,
    "minor-id": 2000,
    "eddystone-namespace": "0102030405",
    "eddystone-instance": "abcdef",
    "eddystone-url": "http://www.fortinet.com",
    "txpower": "0",
    "beacon-interval": 100,
    "ble-scanning": "disable",
    "scan-type": "active",
    "scan-threshold": "-90",
    "scan-period": 4000,
    "scan-time": 1000,
    "scan-interval": 50,
    "scan-window": 50,
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
    "name": "string",  # Bluetooth Low Energy profile name.
    "comment": "string",  # Comment.
    "advertising": "option",  # Advertising type.
    "ibeacon-uuid": "string",  # Universally Unique Identifier (UUID; automatically assigned 
    "major-id": "integer",  # Major ID.
    "minor-id": "integer",  # Minor ID.
    "eddystone-namespace": "string",  # Eddystone namespace ID.
    "eddystone-instance": "string",  # Eddystone instance ID.
    "eddystone-url": "string",  # Eddystone URL.
    "txpower": "option",  # Transmit power level (default = 0).
    "beacon-interval": "integer",  # Beacon interval (default = 100 msec).
    "ble-scanning": "option",  # Enable/disable Bluetooth Low Energy (BLE) scanning.
    "scan-type": "option",  # Scan Type (default = active).
    "scan-threshold": "string",  # Minimum signal level/threshold in dBm required for the AP to
    "scan-period": "integer",  # Scan Period (default = 4000 msec).
    "scan-time": "integer",  # Scan Time (default = 1000 msec).
    "scan-interval": "integer",  # Scan Interval (default = 50 msec).
    "scan-window": "integer",  # Scan Windows (default = 50 msec).
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "Bluetooth Low Energy profile name.",
    "comment": "Comment.",
    "advertising": "Advertising type.",
    "ibeacon-uuid": "Universally Unique Identifier (UUID; automatically assigned but can be manually reset).",
    "major-id": "Major ID.",
    "minor-id": "Minor ID.",
    "eddystone-namespace": "Eddystone namespace ID.",
    "eddystone-instance": "Eddystone instance ID.",
    "eddystone-url": "Eddystone URL.",
    "txpower": "Transmit power level (default = 0).",
    "beacon-interval": "Beacon interval (default = 100 msec).",
    "ble-scanning": "Enable/disable Bluetooth Low Energy (BLE) scanning.",
    "scan-type": "Scan Type (default = active).",
    "scan-threshold": "Minimum signal level/threshold in dBm required for the AP to report detected BLE device (-95 to -20, default = -90).",
    "scan-period": "Scan Period (default = 4000 msec).",
    "scan-time": "Scan Time (default = 1000 msec).",
    "scan-interval": "Scan Interval (default = 50 msec).",
    "scan-window": "Scan Windows (default = 50 msec).",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 35},
    "comment": {"type": "string", "max_length": 63},
    "ibeacon-uuid": {"type": "string", "max_length": 63},
    "major-id": {"type": "integer", "min": 0, "max": 65535},
    "minor-id": {"type": "integer", "min": 0, "max": 65535},
    "eddystone-namespace": {"type": "string", "max_length": 20},
    "eddystone-instance": {"type": "string", "max_length": 12},
    "eddystone-url": {"type": "string", "max_length": 127},
    "beacon-interval": {"type": "integer", "min": 40, "max": 3500},
    "scan-threshold": {"type": "string", "max_length": 7},
    "scan-period": {"type": "integer", "min": 1000, "max": 10000},
    "scan-time": {"type": "integer", "min": 1000, "max": 10000},
    "scan-interval": {"type": "integer", "min": 10, "max": 1000},
    "scan-window": {"type": "integer", "min": 10, "max": 1000},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
}


# Valid enum values from API documentation
VALID_BODY_ADVERTISING = [
    "ibeacon",  # iBeacon advertising.
    "eddystone-uid",  # Eddystone UID advertising.
    "eddystone-url",  # Eddystone URL advertising.
]
VALID_BODY_TXPOWER = [
    "0",  # Transmit power level 0 (-21 dBm)
    "1",  # Transmit power level 1 (-18 dBm)
    "2",  # Transmit power level 2 (-15 dBm)
    "3",  # Transmit power level 3 (-12 dBm)
    "4",  # Transmit power level 4 (-9 dBm)
    "5",  # Transmit power level 5 (-6 dBm)
    "6",  # Transmit power level 6 (-3 dBm)
    "7",  # Transmit power level 7 (0 dBm)
    "8",  # Transmit power level 8 (1 dBm)
    "9",  # Transmit power level 9 (2 dBm)
    "10",  # Transmit power level 10 (3 dBm)
    "11",  # Transmit power level 11 (4 dBm)
    "12",  # Transmit power level 12 (5 dBm)
    "13",  # Transmit power level 13 (8 dBm)
    "14",  # Transmit power level 14 (11 dBm)
    "15",  # Transmit power level 15 (14 dBm)
    "16",  # Transmit power level 16 (17 dBm)
    "17",  # Transmit power level 17 (20 dBm)
]
VALID_BODY_BLE_SCANNING = [
    "enable",  # Enable BLE scanning.
    "disable",  # Disable BLE scanning.
]
VALID_BODY_SCAN_TYPE = [
    "active",  # Active BLE scanning.
    "passive",  # Passive BLE scanning.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_wireless_controller_ble_profile_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for wireless_controller/ble_profile."""
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
    """Validate required fields for wireless_controller/ble_profile."""
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


def validate_wireless_controller_ble_profile_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new wireless_controller/ble_profile object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "advertising" in payload:
        value = payload["advertising"]
        if value not in VALID_BODY_ADVERTISING:
            desc = FIELD_DESCRIPTIONS.get("advertising", "")
            error_msg = f"Invalid value for 'advertising': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ADVERTISING)}"
            error_msg += f"\n  → Example: advertising='{{ VALID_BODY_ADVERTISING[0] }}'"
            return (False, error_msg)
    if "txpower" in payload:
        value = payload["txpower"]
        if value not in VALID_BODY_TXPOWER:
            desc = FIELD_DESCRIPTIONS.get("txpower", "")
            error_msg = f"Invalid value for 'txpower': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_TXPOWER)}"
            error_msg += f"\n  → Example: txpower='{{ VALID_BODY_TXPOWER[0] }}'"
            return (False, error_msg)
    if "ble-scanning" in payload:
        value = payload["ble-scanning"]
        if value not in VALID_BODY_BLE_SCANNING:
            desc = FIELD_DESCRIPTIONS.get("ble-scanning", "")
            error_msg = f"Invalid value for 'ble-scanning': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_BLE_SCANNING)}"
            error_msg += f"\n  → Example: ble-scanning='{{ VALID_BODY_BLE_SCANNING[0] }}'"
            return (False, error_msg)
    if "scan-type" in payload:
        value = payload["scan-type"]
        if value not in VALID_BODY_SCAN_TYPE:
            desc = FIELD_DESCRIPTIONS.get("scan-type", "")
            error_msg = f"Invalid value for 'scan-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SCAN_TYPE)}"
            error_msg += f"\n  → Example: scan-type='{{ VALID_BODY_SCAN_TYPE[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_wireless_controller_ble_profile_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update wireless_controller/ble_profile."""
    # Step 1: Validate enum values
    if "advertising" in payload:
        value = payload["advertising"]
        if value not in VALID_BODY_ADVERTISING:
            return (
                False,
                f"Invalid value for 'advertising'='{value}'. Must be one of: {', '.join(VALID_BODY_ADVERTISING)}",
            )
    if "txpower" in payload:
        value = payload["txpower"]
        if value not in VALID_BODY_TXPOWER:
            return (
                False,
                f"Invalid value for 'txpower'='{value}'. Must be one of: {', '.join(VALID_BODY_TXPOWER)}",
            )
    if "ble-scanning" in payload:
        value = payload["ble-scanning"]
        if value not in VALID_BODY_BLE_SCANNING:
            return (
                False,
                f"Invalid value for 'ble-scanning'='{value}'. Must be one of: {', '.join(VALID_BODY_BLE_SCANNING)}",
            )
    if "scan-type" in payload:
        value = payload["scan-type"]
        if value not in VALID_BODY_SCAN_TYPE:
            return (
                False,
                f"Invalid value for 'scan-type'='{value}'. Must be one of: {', '.join(VALID_BODY_SCAN_TYPE)}",
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
    "endpoint": "wireless_controller/ble_profile",
    "category": "cmdb",
    "api_path": "wireless-controller/ble-profile",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure Bluetooth Low Energy profile.",
    "total_fields": 18,
    "required_fields_count": 0,
    "fields_with_defaults_count": 18,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
