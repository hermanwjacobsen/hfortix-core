"""Validation helpers for router/rip - Auto-generated"""

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
    "default-information-originate": "disable",
    "default-metric": 1,
    "max-out-metric": 0,
    "update-timer": 30,
    "timeout-timer": 180,
    "garbage-timer": 120,
    "version": "2",
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
    "default-information-originate": "option",  # Enable/disable generation of default route.
    "default-metric": "integer",  # Default metric.
    "max-out-metric": "integer",  # Maximum metric allowed to output(0 means 'not set').
    "distance": "string",  # Distance.
    "distribute-list": "string",  # Distribute list.
    "neighbor": "string",  # Neighbor.
    "network": "string",  # Network.
    "offset-list": "string",  # Offset list.
    "passive-interface": "string",  # Passive interface configuration.
    "redistribute": "string",  # Redistribute configuration.
    "update-timer": "integer",  # Update timer in seconds.
    "timeout-timer": "integer",  # Timeout timer in seconds.
    "garbage-timer": "integer",  # Garbage timer in seconds.
    "version": "option",  # RIP version.
    "interface": "string",  # RIP interface configuration.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "default-information-originate": "Enable/disable generation of default route.",
    "default-metric": "Default metric.",
    "max-out-metric": "Maximum metric allowed to output(0 means 'not set').",
    "distance": "Distance.",
    "distribute-list": "Distribute list.",
    "neighbor": "Neighbor.",
    "network": "Network.",
    "offset-list": "Offset list.",
    "passive-interface": "Passive interface configuration.",
    "redistribute": "Redistribute configuration.",
    "update-timer": "Update timer in seconds.",
    "timeout-timer": "Timeout timer in seconds.",
    "garbage-timer": "Garbage timer in seconds.",
    "version": "RIP version.",
    "interface": "RIP interface configuration.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "default-metric": {"type": "integer", "min": 1, "max": 16},
    "max-out-metric": {"type": "integer", "min": 0, "max": 15},
    "update-timer": {"type": "integer", "min": 1, "max": 2147483647},
    "timeout-timer": {"type": "integer", "min": 5, "max": 2147483647},
    "garbage-timer": {"type": "integer", "min": 5, "max": 2147483647},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "distance": {
        "id": {
            "type": "integer",
            "help": "Distance ID.",
            "required": True,
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "prefix": {
            "type": "ipv4-classnet-any",
            "help": "Distance prefix.",
            "default": "0.0.0.0 0.0.0.0",
        },
        "distance": {
            "type": "integer",
            "help": "Distance (1 - 255).",
            "required": True,
            "default": 0,
            "min_value": 1,
            "max_value": 255,
        },
        "access-list": {
            "type": "string",
            "help": "Access list for route destination.",
            "default": "",
            "max_length": 35,
        },
    },
    "distribute-list": {
        "id": {
            "type": "integer",
            "help": "Distribute list ID.",
            "required": True,
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "status": {
            "type": "option",
            "help": "Status.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "direction": {
            "type": "option",
            "help": "Distribute list direction.",
            "required": True,
            "default": "out",
            "options": [{"help": "Filter incoming packets.", "label": "In", "name": "in"}, {"help": "Filter outgoing packets.", "label": "Out", "name": "out"}],
        },
        "listname": {
            "type": "string",
            "help": "Distribute access/prefix list name.",
            "required": True,
            "default": "",
            "max_length": 35,
        },
        "interface": {
            "type": "string",
            "help": "Distribute list interface name.",
            "default": "",
            "max_length": 15,
        },
    },
    "neighbor": {
        "id": {
            "type": "integer",
            "help": "Neighbor entry ID.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "ip": {
            "type": "ipv4-address",
            "help": "IP address.",
            "required": True,
            "default": "0.0.0.0",
        },
    },
    "network": {
        "id": {
            "type": "integer",
            "help": "Network entry ID.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "prefix": {
            "type": "ipv4-classnet",
            "help": "Network prefix.",
            "default": "0.0.0.0 0.0.0.0",
        },
    },
    "offset-list": {
        "id": {
            "type": "integer",
            "help": "Offset-list ID.",
            "required": True,
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "status": {
            "type": "option",
            "help": "Status.",
            "default": "enable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "direction": {
            "type": "option",
            "help": "Offset list direction.",
            "required": True,
            "default": "out",
            "options": [{"help": "Filter incoming packets.", "label": "In", "name": "in"}, {"help": "Filter outgoing packets.", "label": "Out", "name": "out"}],
        },
        "access-list": {
            "type": "string",
            "help": "Access list name.",
            "required": True,
            "default": "",
            "max_length": 35,
        },
        "offset": {
            "type": "integer",
            "help": "Offset.",
            "required": True,
            "default": 0,
            "min_value": 1,
            "max_value": 16,
        },
        "interface": {
            "type": "string",
            "help": "Interface name.",
            "default": "",
            "max_length": 15,
        },
    },
    "passive-interface": {
        "name": {
            "type": "string",
            "help": "Passive interface name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "redistribute": {
        "name": {
            "type": "string",
            "help": "Redistribute name.",
            "required": True,
            "default": "",
            "max_length": 35,
        },
        "status": {
            "type": "option",
            "help": "Status.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "metric": {
            "type": "integer",
            "help": "Redistribute metric setting.",
            "default": 0,
            "min_value": 1,
            "max_value": 16,
        },
        "routemap": {
            "type": "string",
            "help": "Route map name.",
            "default": "",
            "max_length": 35,
        },
    },
    "interface": {
        "name": {
            "type": "string",
            "help": "Interface name.",
            "default": "",
            "max_length": 35,
        },
        "auth-keychain": {
            "type": "string",
            "help": "Authentication key-chain name.",
            "default": "",
            "max_length": 35,
        },
        "auth-mode": {
            "type": "option",
            "help": "Authentication mode.",
            "default": "none",
            "options": [{"help": "None.", "label": "None", "name": "none"}, {"help": "Text.", "label": "Text", "name": "text"}, {"help": "MD5.", "label": "Md5", "name": "md5"}],
        },
        "auth-string": {
            "type": "password",
            "help": "Authentication string/password.",
            "max_length": 16,
        },
        "receive-version": {
            "type": "option",
            "help": "Receive version.",
            "default": "",
            "options": [{"help": "Version 1.", "label": "1", "name": "1"}, {"help": "Version 2.", "label": "2", "name": "2"}],
        },
        "send-version": {
            "type": "option",
            "help": "Send version.",
            "default": "",
            "options": [{"help": "Version 1.", "label": "1", "name": "1"}, {"help": "Version 2.", "label": "2", "name": "2"}],
        },
        "send-version2-broadcast": {
            "type": "option",
            "help": "Enable/disable broadcast version 1 compatible packets.",
            "default": "disable",
            "options": [{"help": "Disable broadcasting.", "label": "Disable", "name": "disable"}, {"help": "Enable broadcasting.", "label": "Enable", "name": "enable"}],
        },
        "split-horizon-status": {
            "type": "option",
            "help": "Enable/disable split horizon.",
            "default": "enable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "split-horizon": {
            "type": "option",
            "help": "Enable/disable split horizon.",
            "default": "poisoned",
            "options": [{"help": "Poisoned.", "label": "Poisoned", "name": "poisoned"}, {"help": "Regular.", "label": "Regular", "name": "regular"}],
        },
        "flags": {
            "type": "integer",
            "help": "Flags.",
            "default": 8,
            "min_value": 0,
            "max_value": 255,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_DEFAULT_INFORMATION_ORIGINATE = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_VERSION = [
    "1",  # Version 1.
    "2",  # Version 2.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_router_rip_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for router/rip."""
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
    """Validate required fields for router/rip."""
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


def validate_router_rip_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new router/rip object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "default-information-originate" in payload:
        value = payload["default-information-originate"]
        if value not in VALID_BODY_DEFAULT_INFORMATION_ORIGINATE:
            desc = FIELD_DESCRIPTIONS.get("default-information-originate", "")
            error_msg = f"Invalid value for 'default-information-originate': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DEFAULT_INFORMATION_ORIGINATE)}"
            error_msg += f"\n  → Example: default-information-originate='{{ VALID_BODY_DEFAULT_INFORMATION_ORIGINATE[0] }}'"
            return (False, error_msg)
    if "version" in payload:
        value = payload["version"]
        if value not in VALID_BODY_VERSION:
            desc = FIELD_DESCRIPTIONS.get("version", "")
            error_msg = f"Invalid value for 'version': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_VERSION)}"
            error_msg += f"\n  → Example: version='{{ VALID_BODY_VERSION[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_router_rip_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update router/rip."""
    # Step 1: Validate enum values
    if "default-information-originate" in payload:
        value = payload["default-information-originate"]
        if value not in VALID_BODY_DEFAULT_INFORMATION_ORIGINATE:
            return (
                False,
                f"Invalid value for 'default-information-originate'='{value}'. Must be one of: {', '.join(VALID_BODY_DEFAULT_INFORMATION_ORIGINATE)}",
            )
    if "version" in payload:
        value = payload["version"]
        if value not in VALID_BODY_VERSION:
            return (
                False,
                f"Invalid value for 'version'='{value}'. Must be one of: {', '.join(VALID_BODY_VERSION)}",
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
    "endpoint": "router/rip",
    "category": "cmdb",
    "api_path": "router/rip",
    "help": "Configure RIP.",
    "total_fields": 15,
    "required_fields_count": 0,
    "fields_with_defaults_count": 7,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
