"""Validation helpers for firewall/DoS_policy - Auto-generated"""

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
    "interface",  # Incoming interface name from available interfaces.
    "srcaddr",  # Source address name from available addresses.
    "dstaddr",  # Destination address name from available addresses.
    "service",  # Service object from available options.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "policyid": 0,
    "status": "enable",
    "name": "",
    "interface": "",
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
    "policyid": "integer",  # Policy ID.
    "status": "option",  # Enable/disable this policy.
    "name": "string",  # Policy name.
    "comments": "var-string",  # Comment.
    "interface": "string",  # Incoming interface name from available interfaces.
    "srcaddr": "string",  # Source address name from available addresses.
    "dstaddr": "string",  # Destination address name from available addresses.
    "service": "string",  # Service object from available options.
    "anomaly": "string",  # Anomaly name.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "policyid": "Policy ID.",
    "status": "Enable/disable this policy.",
    "name": "Policy name.",
    "comments": "Comment.",
    "interface": "Incoming interface name from available interfaces.",
    "srcaddr": "Source address name from available addresses.",
    "dstaddr": "Destination address name from available addresses.",
    "service": "Service object from available options.",
    "anomaly": "Anomaly name.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "policyid": {"type": "integer", "min": 0, "max": 9999},
    "name": {"type": "string", "max_length": 35},
    "interface": {"type": "string", "max_length": 35},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "srcaddr": {
        "name": {
            "type": "string",
            "help": "Address name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "dstaddr": {
        "name": {
            "type": "string",
            "help": "Address name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "service": {
        "name": {
            "type": "string",
            "help": "Service name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "anomaly": {
        "name": {
            "type": "string",
            "help": "Anomaly name.",
            "default": "",
            "max_length": 63,
        },
        "status": {
            "type": "option",
            "help": "Enable/disable this anomaly.",
            "default": "disable",
            "options": [{"help": "Disable this status.", "label": "Disable", "name": "disable"}, {"help": "Enable this status.", "label": "Enable", "name": "enable"}],
        },
        "log": {
            "type": "option",
            "help": "Enable/disable anomaly logging.",
            "default": "disable",
            "options": [{"help": "Enable anomaly logging.", "label": "Enable", "name": "enable"}, {"help": "Disable anomaly logging.", "label": "Disable", "name": "disable"}],
        },
        "action": {
            "type": "option",
            "help": "Action taken when the threshold is reached.",
            "default": "pass",
            "options": [{"help": "Allow traffic but record a log message if logging is enabled.", "label": "Pass", "name": "pass"}, {"help": "Block traffic if this anomaly is found.", "label": "Block", "name": "block"}],
        },
        "quarantine": {
            "type": "option",
            "help": "Quarantine method.",
            "default": "none",
            "options": [{"help": "Quarantine is disabled.", "label": "None", "name": "none"}, {"help": "Block all traffic sent from attacker\u0027s IP address. The attacker\u0027s IP address is also added to the banned user list. The target\u0027s address is not affected.", "label": "Attacker", "name": "attacker"}],
        },
        "quarantine-expiry": {
            "type": "user",
            "help": "Duration of quarantine. (Format ###d##h##m, minimum 1m, maximum 364d23h59m, default = 5m). Requires quarantine set to attacker.",
            "default": "5m",
        },
        "quarantine-log": {
            "type": "option",
            "help": "Enable/disable quarantine logging.",
            "default": "enable",
            "options": [{"help": "Disable quarantine logging.", "label": "Disable", "name": "disable"}, {"help": "Enable quarantine logging.", "label": "Enable", "name": "enable"}],
        },
        "threshold": {
            "type": "integer",
            "help": "Anomaly threshold. Number of detected instances (packets per second or concurrent session number) that triggers the anomaly action.",
            "default": 0,
            "min_value": 1,
            "max_value": 2147483647,
        },
        "threshold(default)": {
            "type": "integer",
            "help": "Number of detected instances (packets per second or concurrent session number) which triggers action (1 - 2147483647, default = 1000). Note that each anomaly has a different threshold value assigned to it.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_STATUS = [
    "enable",  # Enable this policy.
    "disable",  # Disable this policy.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_firewall_DoS_policy_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for firewall/DoS_policy."""
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
    """Validate required fields for firewall/DoS_policy."""
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


def validate_firewall_DoS_policy_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new firewall/DoS_policy object."""
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

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_firewall_DoS_policy_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update firewall/DoS_policy."""
    # Step 1: Validate enum values
    if "status" in payload:
        value = payload["status"]
        if value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid value for 'status'='{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
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
    "endpoint": "firewall/DoS_policy",
    "category": "cmdb",
    "api_path": "firewall/DoS-policy",
    "mkey": "policyid",
    "mkey_type": "integer",
    "help": "Configure IPv4 DoS policies.",
    "total_fields": 9,
    "required_fields_count": 4,
    "fields_with_defaults_count": 4,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
