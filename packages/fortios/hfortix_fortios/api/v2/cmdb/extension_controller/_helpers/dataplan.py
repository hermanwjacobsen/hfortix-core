"""Validation helpers for extension_controller/dataplan - Auto-generated"""

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
    "slot",  # SIM slot configuration.
    "iccid",  # ICCID configuration.
    "carrier",  # Carrier configuration.
    "username",  # Username.
    "password",  # Password.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "modem-id": "all",
    "type": "generic",
    "slot": "",
    "iccid": "",
    "carrier": "",
    "apn": "",
    "auth-type": "none",
    "username": "",
    "pdn": "ipv4-only",
    "signal-threshold": 100,
    "signal-period": 3600,
    "capacity": 0,
    "monthly-fee": 0,
    "billing-date": 1,
    "overage": "disable",
    "preferred-subnet": 0,
    "private-network": "disable",
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
    "name": "string",  # FortiExtender data plan name.
    "modem-id": "option",  # Dataplan's modem specifics, if any.
    "type": "option",  # Type preferences configuration.
    "slot": "option",  # SIM slot configuration.
    "iccid": "string",  # ICCID configuration.
    "carrier": "string",  # Carrier configuration.
    "apn": "string",  # APN configuration.
    "auth-type": "option",  # Authentication type.
    "username": "string",  # Username.
    "password": "password",  # Password.
    "pdn": "option",  # PDN type.
    "signal-threshold": "integer",  # Signal threshold. Specify the range between 50 - 100, where 
    "signal-period": "integer",  # Signal period (600 to 18000 seconds).
    "capacity": "integer",  # Capacity in MB (0 - 102400000).
    "monthly-fee": "integer",  # Monthly fee of dataplan (0 - 100000, in local currency).
    "billing-date": "integer",  # Billing day of the month (1 - 31).
    "overage": "option",  # Enable/disable dataplan overage detection.
    "preferred-subnet": "integer",  # Preferred subnet mask (0 - 32).
    "private-network": "option",  # Enable/disable dataplan private network support.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "FortiExtender data plan name.",
    "modem-id": "Dataplan's modem specifics, if any.",
    "type": "Type preferences configuration.",
    "slot": "SIM slot configuration.",
    "iccid": "ICCID configuration.",
    "carrier": "Carrier configuration.",
    "apn": "APN configuration.",
    "auth-type": "Authentication type.",
    "username": "Username.",
    "password": "Password.",
    "pdn": "PDN type.",
    "signal-threshold": "Signal threshold. Specify the range between 50 - 100, where 50/100 means -50/-100 dBm.",
    "signal-period": "Signal period (600 to 18000 seconds).",
    "capacity": "Capacity in MB (0 - 102400000).",
    "monthly-fee": "Monthly fee of dataplan (0 - 100000, in local currency).",
    "billing-date": "Billing day of the month (1 - 31).",
    "overage": "Enable/disable dataplan overage detection.",
    "preferred-subnet": "Preferred subnet mask (0 - 32).",
    "private-network": "Enable/disable dataplan private network support.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 31},
    "iccid": {"type": "string", "max_length": 31},
    "carrier": {"type": "string", "max_length": 31},
    "apn": {"type": "string", "max_length": 63},
    "username": {"type": "string", "max_length": 127},
    "signal-threshold": {"type": "integer", "min": 50, "max": 100},
    "signal-period": {"type": "integer", "min": 600, "max": 18000},
    "capacity": {"type": "integer", "min": 0, "max": 102400000},
    "monthly-fee": {"type": "integer", "min": 0, "max": 1000000},
    "billing-date": {"type": "integer", "min": 1, "max": 31},
    "preferred-subnet": {"type": "integer", "min": 0, "max": 32},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
}


# Valid enum values from API documentation
VALID_BODY_MODEM_ID = [
    "modem1",  # Modem one.
    "modem2",  # Modem two.
    "all",  # All modems.
]
VALID_BODY_TYPE = [
    "carrier",  # Assign by SIM carrier.
    "slot",  # Assign to SIM slot 1 or 2.
    "iccid",  # Assign to a specific SIM by ICCID.
    "generic",  # Compatible with any SIM. Assigned if no other dataplan matches the chosen SIM.
]
VALID_BODY_SLOT = [
    "sim1",  # Sim slot one.
    "sim2",  # Sim slot two.
]
VALID_BODY_AUTH_TYPE = [
    "none",  # No authentication.
    "pap",  # PAP.
    "chap",  # CHAP.
]
VALID_BODY_PDN = [
    "ipv4-only",  # IPv4 only PDN activation.
    "ipv6-only",  # IPv6 only PDN activation.
    "ipv4-ipv6",  # Both IPv4 and IPv6 PDN activations.
]
VALID_BODY_OVERAGE = [
    "disable",  # Disable dataplan overage detection.
    "enable",  # Enable dataplan overage detection.
]
VALID_BODY_PRIVATE_NETWORK = [
    "disable",  # Disable dataplan private network support.
    "enable",  # Enable dataplan private network support.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_extension_controller_dataplan_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for extension_controller/dataplan."""
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
    """Validate required fields for extension_controller/dataplan."""
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


def validate_extension_controller_dataplan_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new extension_controller/dataplan object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "modem-id" in payload:
        value = payload["modem-id"]
        if value not in VALID_BODY_MODEM_ID:
            desc = FIELD_DESCRIPTIONS.get("modem-id", "")
            error_msg = f"Invalid value for 'modem-id': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MODEM_ID)}"
            error_msg += f"\n  → Example: modem-id='{{ VALID_BODY_MODEM_ID[0] }}'"
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
    if "slot" in payload:
        value = payload["slot"]
        if value not in VALID_BODY_SLOT:
            desc = FIELD_DESCRIPTIONS.get("slot", "")
            error_msg = f"Invalid value for 'slot': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SLOT)}"
            error_msg += f"\n  → Example: slot='{{ VALID_BODY_SLOT[0] }}'"
            return (False, error_msg)
    if "auth-type" in payload:
        value = payload["auth-type"]
        if value not in VALID_BODY_AUTH_TYPE:
            desc = FIELD_DESCRIPTIONS.get("auth-type", "")
            error_msg = f"Invalid value for 'auth-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTH_TYPE)}"
            error_msg += f"\n  → Example: auth-type='{{ VALID_BODY_AUTH_TYPE[0] }}'"
            return (False, error_msg)
    if "pdn" in payload:
        value = payload["pdn"]
        if value not in VALID_BODY_PDN:
            desc = FIELD_DESCRIPTIONS.get("pdn", "")
            error_msg = f"Invalid value for 'pdn': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PDN)}"
            error_msg += f"\n  → Example: pdn='{{ VALID_BODY_PDN[0] }}'"
            return (False, error_msg)
    if "overage" in payload:
        value = payload["overage"]
        if value not in VALID_BODY_OVERAGE:
            desc = FIELD_DESCRIPTIONS.get("overage", "")
            error_msg = f"Invalid value for 'overage': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_OVERAGE)}"
            error_msg += f"\n  → Example: overage='{{ VALID_BODY_OVERAGE[0] }}'"
            return (False, error_msg)
    if "private-network" in payload:
        value = payload["private-network"]
        if value not in VALID_BODY_PRIVATE_NETWORK:
            desc = FIELD_DESCRIPTIONS.get("private-network", "")
            error_msg = f"Invalid value for 'private-network': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PRIVATE_NETWORK)}"
            error_msg += f"\n  → Example: private-network='{{ VALID_BODY_PRIVATE_NETWORK[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_extension_controller_dataplan_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update extension_controller/dataplan."""
    # Step 1: Validate enum values
    if "modem-id" in payload:
        value = payload["modem-id"]
        if value not in VALID_BODY_MODEM_ID:
            return (
                False,
                f"Invalid value for 'modem-id'='{value}'. Must be one of: {', '.join(VALID_BODY_MODEM_ID)}",
            )
    if "type" in payload:
        value = payload["type"]
        if value not in VALID_BODY_TYPE:
            return (
                False,
                f"Invalid value for 'type'='{value}'. Must be one of: {', '.join(VALID_BODY_TYPE)}",
            )
    if "slot" in payload:
        value = payload["slot"]
        if value not in VALID_BODY_SLOT:
            return (
                False,
                f"Invalid value for 'slot'='{value}'. Must be one of: {', '.join(VALID_BODY_SLOT)}",
            )
    if "auth-type" in payload:
        value = payload["auth-type"]
        if value not in VALID_BODY_AUTH_TYPE:
            return (
                False,
                f"Invalid value for 'auth-type'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_TYPE)}",
            )
    if "pdn" in payload:
        value = payload["pdn"]
        if value not in VALID_BODY_PDN:
            return (
                False,
                f"Invalid value for 'pdn'='{value}'. Must be one of: {', '.join(VALID_BODY_PDN)}",
            )
    if "overage" in payload:
        value = payload["overage"]
        if value not in VALID_BODY_OVERAGE:
            return (
                False,
                f"Invalid value for 'overage'='{value}'. Must be one of: {', '.join(VALID_BODY_OVERAGE)}",
            )
    if "private-network" in payload:
        value = payload["private-network"]
        if value not in VALID_BODY_PRIVATE_NETWORK:
            return (
                False,
                f"Invalid value for 'private-network'='{value}'. Must be one of: {', '.join(VALID_BODY_PRIVATE_NETWORK)}",
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
    "endpoint": "extension_controller/dataplan",
    "category": "cmdb",
    "api_path": "extension-controller/dataplan",
    "mkey": "name",
    "mkey_type": "string",
    "help": "FortiExtender dataplan configuration.",
    "total_fields": 19,
    "required_fields_count": 5,
    "fields_with_defaults_count": 18,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
