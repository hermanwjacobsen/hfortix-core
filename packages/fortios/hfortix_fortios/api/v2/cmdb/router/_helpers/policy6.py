"""Validation helpers for router/policy6 - Auto-generated"""

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
    "seq-num": 0,
    "input-device-negate": "disable",
    "src-negate": "disable",
    "dst-negate": "disable",
    "action": "permit",
    "protocol": 0,
    "start-port": 1,
    "end-port": 65535,
    "start-source-port": 1,
    "end-source-port": 65535,
    "gateway": "::",
    "output-device": "",
    "tos": "",
    "tos-mask": "",
    "status": "enable",
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
    "seq-num": "integer",  # Sequence number(1-65535).
    "input-device": "string",  # Incoming interface name.
    "input-device-negate": "option",  # Enable/disable negation of input device match.
    "src": "string",  # Source IPv6 prefix.
    "srcaddr": "string",  # Source address name.
    "src-negate": "option",  # Enable/disable negating source address match.
    "dst": "string",  # Destination IPv6 prefix.
    "dstaddr": "string",  # Destination address name.
    "dst-negate": "option",  # Enable/disable negating destination address match.
    "action": "option",  # Action of the policy route.
    "protocol": "integer",  # Protocol number (0 - 255).
    "start-port": "integer",  # Start destination port number (1 - 65535).
    "end-port": "integer",  # End destination port number (1 - 65535).
    "start-source-port": "integer",  # Start source port number (1 - 65535).
    "end-source-port": "integer",  # End source port number (1 - 65535).
    "gateway": "ipv6-address",  # IPv6 address of the gateway.
    "output-device": "string",  # Outgoing interface name.
    "tos": "user",  # Type of service bit pattern.
    "tos-mask": "user",  # Type of service evaluated bits.
    "status": "option",  # Enable/disable this policy route.
    "comments": "var-string",  # Optional comments.
    "internet-service-id": "string",  # Destination Internet Service ID.
    "internet-service-custom": "string",  # Custom Destination Internet Service name.
    "internet-service-fortiguard": "string",  # FortiGuard Destination Internet Service name.
    "users": "string",  # List of users.
    "groups": "string",  # List of user groups.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "seq-num": "Sequence number(1-65535).",
    "input-device": "Incoming interface name.",
    "input-device-negate": "Enable/disable negation of input device match.",
    "src": "Source IPv6 prefix.",
    "srcaddr": "Source address name.",
    "src-negate": "Enable/disable negating source address match.",
    "dst": "Destination IPv6 prefix.",
    "dstaddr": "Destination address name.",
    "dst-negate": "Enable/disable negating destination address match.",
    "action": "Action of the policy route.",
    "protocol": "Protocol number (0 - 255).",
    "start-port": "Start destination port number (1 - 65535).",
    "end-port": "End destination port number (1 - 65535).",
    "start-source-port": "Start source port number (1 - 65535).",
    "end-source-port": "End source port number (1 - 65535).",
    "gateway": "IPv6 address of the gateway.",
    "output-device": "Outgoing interface name.",
    "tos": "Type of service bit pattern.",
    "tos-mask": "Type of service evaluated bits.",
    "status": "Enable/disable this policy route.",
    "comments": "Optional comments.",
    "internet-service-id": "Destination Internet Service ID.",
    "internet-service-custom": "Custom Destination Internet Service name.",
    "internet-service-fortiguard": "FortiGuard Destination Internet Service name.",
    "users": "List of users.",
    "groups": "List of user groups.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "seq-num": {"type": "integer", "min": 1, "max": 65535},
    "protocol": {"type": "integer", "min": 0, "max": 255},
    "start-port": {"type": "integer", "min": 1, "max": 65535},
    "end-port": {"type": "integer", "min": 1, "max": 65535},
    "start-source-port": {"type": "integer", "min": 1, "max": 65535},
    "end-source-port": {"type": "integer", "min": 1, "max": 65535},
    "output-device": {"type": "string", "max_length": 35},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "input-device": {
        "name": {
            "type": "string",
            "help": "Interface name.",
            "default": "",
            "max_length": 79,
        },
    },
    "src": {
        "addr6": {
            "type": "string",
            "help": "IPv6 address prefix.",
            "default": "",
            "max_length": 79,
        },
    },
    "srcaddr": {
        "name": {
            "type": "string",
            "help": "Address/group name.",
            "default": "",
            "max_length": 79,
        },
    },
    "dst": {
        "addr6": {
            "type": "string",
            "help": "IPv6 address prefix.",
            "default": "",
            "max_length": 79,
        },
    },
    "dstaddr": {
        "name": {
            "type": "string",
            "help": "Address/group name.",
            "default": "",
            "max_length": 79,
        },
    },
    "internet-service-id": {
        "id": {
            "type": "integer",
            "help": "Destination Internet Service ID.",
            "required": True,
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
    },
    "internet-service-custom": {
        "name": {
            "type": "string",
            "help": "Custom Destination Internet Service name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "internet-service-fortiguard": {
        "name": {
            "type": "string",
            "help": "FortiGuard Destination Internet Service name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "users": {
        "name": {
            "type": "string",
            "help": "User name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "groups": {
        "name": {
            "type": "string",
            "help": "Group name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_INPUT_DEVICE_NEGATE = [
    "enable",  # Enable negation of input device match.
    "disable",  # Disable negation of input device match.
]
VALID_BODY_SRC_NEGATE = [
    "enable",  # Enable source address negation.
    "disable",  # Disable source address negation.
]
VALID_BODY_DST_NEGATE = [
    "enable",  # Enable destination address negation.
    "disable",  # Disable destination address negation.
]
VALID_BODY_ACTION = [
    "deny",  # Do not search policy route table.
    "permit",  # Use this policy route for forwarding.
]
VALID_BODY_STATUS = [
    "enable",  # Enable this policy route.
    "disable",  # Disable this policy route.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_router_policy6_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for router/policy6."""
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
    """Validate required fields for router/policy6."""
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


def validate_router_policy6_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new router/policy6 object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "input-device-negate" in payload:
        value = payload["input-device-negate"]
        if value not in VALID_BODY_INPUT_DEVICE_NEGATE:
            desc = FIELD_DESCRIPTIONS.get("input-device-negate", "")
            error_msg = f"Invalid value for 'input-device-negate': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_INPUT_DEVICE_NEGATE)}"
            error_msg += f"\n  → Example: input-device-negate='{{ VALID_BODY_INPUT_DEVICE_NEGATE[0] }}'"
            return (False, error_msg)
    if "src-negate" in payload:
        value = payload["src-negate"]
        if value not in VALID_BODY_SRC_NEGATE:
            desc = FIELD_DESCRIPTIONS.get("src-negate", "")
            error_msg = f"Invalid value for 'src-negate': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SRC_NEGATE)}"
            error_msg += f"\n  → Example: src-negate='{{ VALID_BODY_SRC_NEGATE[0] }}'"
            return (False, error_msg)
    if "dst-negate" in payload:
        value = payload["dst-negate"]
        if value not in VALID_BODY_DST_NEGATE:
            desc = FIELD_DESCRIPTIONS.get("dst-negate", "")
            error_msg = f"Invalid value for 'dst-negate': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DST_NEGATE)}"
            error_msg += f"\n  → Example: dst-negate='{{ VALID_BODY_DST_NEGATE[0] }}'"
            return (False, error_msg)
    if "action" in payload:
        value = payload["action"]
        if value not in VALID_BODY_ACTION:
            desc = FIELD_DESCRIPTIONS.get("action", "")
            error_msg = f"Invalid value for 'action': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ACTION)}"
            error_msg += f"\n  → Example: action='{{ VALID_BODY_ACTION[0] }}'"
            return (False, error_msg)
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


def validate_router_policy6_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update router/policy6."""
    # Step 1: Validate enum values
    if "input-device-negate" in payload:
        value = payload["input-device-negate"]
        if value not in VALID_BODY_INPUT_DEVICE_NEGATE:
            return (
                False,
                f"Invalid value for 'input-device-negate'='{value}'. Must be one of: {', '.join(VALID_BODY_INPUT_DEVICE_NEGATE)}",
            )
    if "src-negate" in payload:
        value = payload["src-negate"]
        if value not in VALID_BODY_SRC_NEGATE:
            return (
                False,
                f"Invalid value for 'src-negate'='{value}'. Must be one of: {', '.join(VALID_BODY_SRC_NEGATE)}",
            )
    if "dst-negate" in payload:
        value = payload["dst-negate"]
        if value not in VALID_BODY_DST_NEGATE:
            return (
                False,
                f"Invalid value for 'dst-negate'='{value}'. Must be one of: {', '.join(VALID_BODY_DST_NEGATE)}",
            )
    if "action" in payload:
        value = payload["action"]
        if value not in VALID_BODY_ACTION:
            return (
                False,
                f"Invalid value for 'action'='{value}'. Must be one of: {', '.join(VALID_BODY_ACTION)}",
            )
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
    "endpoint": "router/policy6",
    "category": "cmdb",
    "api_path": "router/policy6",
    "mkey": "seq-num",
    "mkey_type": "integer",
    "help": "Configure IPv6 routing policies.",
    "total_fields": 26,
    "required_fields_count": 0,
    "fields_with_defaults_count": 15,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
