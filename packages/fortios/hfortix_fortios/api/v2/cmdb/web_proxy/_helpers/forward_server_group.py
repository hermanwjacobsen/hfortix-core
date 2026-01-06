"""Validation helpers for web_proxy/forward_server_group - Auto-generated"""

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
    "affinity": "enable",
    "ldb-method": "weighted",
    "group-down-option": "block",
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
    "name": "string",  # Configure a forward server group consisting one or multiple 
    "affinity": "option",  # Enable/disable affinity, attaching a source-ip's traffic to 
    "ldb-method": "option",  # Load balance method: weighted or least-session.
    "group-down-option": "option",  # Action to take when all of the servers in the forward server
    "server-list": "string",  # Add web forward servers to a list to form a server group. Op
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "Configure a forward server group consisting one or multiple forward servers. Supports failover and load balancing.",
    "affinity": "Enable/disable affinity, attaching a source-ip's traffic to the assigned forwarding server until the forward-server-affinity-timeout is reached (under web-proxy global).",
    "ldb-method": "Load balance method: weighted or least-session.",
    "group-down-option": "Action to take when all of the servers in the forward server group are down: block sessions until at least one server is back up or pass sessions to their destination.",
    "server-list": "Add web forward servers to a list to form a server group. Optionally assign weights to each server.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 63},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "server-list": {
        "name": {
            "type": "string",
            "help": "Forward server name.",
            "default": "",
            "max_length": 63,
        },
        "weight": {
            "type": "integer",
            "help": "Optionally assign a weight of the forwarding server for weighted load balancing (1 - 100, default = 10).",
            "default": 10,
            "min_value": 1,
            "max_value": 100,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_AFFINITY = [
    "enable",  # Enable affinity.
    "disable",  # Disable affinity.
]
VALID_BODY_LDB_METHOD = [
    "weighted",  # Load balance traffic to forward servers based on assigned weights. Weights are ratios of total number of sessions.
    "least-session",  # Send new sessions to the server with lowest session count.
    "active-passive",  # Send new sessions to the next active server in the list. Servers are selected with highest weight first and then in order as they are configured. Traffic switches back to the first server upon failure recovery.
]
VALID_BODY_GROUP_DOWN_OPTION = [
    "block",  # Block sessions until at least one server in the group is back up.
    "pass",  # Pass sessions to their destination bypassing servers in the forward server group.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_web_proxy_forward_server_group_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for web_proxy/forward_server_group."""
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
    """Validate required fields for web_proxy/forward_server_group."""
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


def validate_web_proxy_forward_server_group_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new web_proxy/forward_server_group object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "affinity" in payload:
        value = payload["affinity"]
        if value not in VALID_BODY_AFFINITY:
            desc = FIELD_DESCRIPTIONS.get("affinity", "")
            error_msg = f"Invalid value for 'affinity': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AFFINITY)}"
            error_msg += f"\n  → Example: affinity='{{ VALID_BODY_AFFINITY[0] }}'"
            return (False, error_msg)
    if "ldb-method" in payload:
        value = payload["ldb-method"]
        if value not in VALID_BODY_LDB_METHOD:
            desc = FIELD_DESCRIPTIONS.get("ldb-method", "")
            error_msg = f"Invalid value for 'ldb-method': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LDB_METHOD)}"
            error_msg += f"\n  → Example: ldb-method='{{ VALID_BODY_LDB_METHOD[0] }}'"
            return (False, error_msg)
    if "group-down-option" in payload:
        value = payload["group-down-option"]
        if value not in VALID_BODY_GROUP_DOWN_OPTION:
            desc = FIELD_DESCRIPTIONS.get("group-down-option", "")
            error_msg = f"Invalid value for 'group-down-option': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GROUP_DOWN_OPTION)}"
            error_msg += f"\n  → Example: group-down-option='{{ VALID_BODY_GROUP_DOWN_OPTION[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_web_proxy_forward_server_group_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update web_proxy/forward_server_group."""
    # Step 1: Validate enum values
    if "affinity" in payload:
        value = payload["affinity"]
        if value not in VALID_BODY_AFFINITY:
            return (
                False,
                f"Invalid value for 'affinity'='{value}'. Must be one of: {', '.join(VALID_BODY_AFFINITY)}",
            )
    if "ldb-method" in payload:
        value = payload["ldb-method"]
        if value not in VALID_BODY_LDB_METHOD:
            return (
                False,
                f"Invalid value for 'ldb-method'='{value}'. Must be one of: {', '.join(VALID_BODY_LDB_METHOD)}",
            )
    if "group-down-option" in payload:
        value = payload["group-down-option"]
        if value not in VALID_BODY_GROUP_DOWN_OPTION:
            return (
                False,
                f"Invalid value for 'group-down-option'='{value}'. Must be one of: {', '.join(VALID_BODY_GROUP_DOWN_OPTION)}",
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
    "endpoint": "web_proxy/forward_server_group",
    "category": "cmdb",
    "api_path": "web-proxy/forward-server-group",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure a forward server group consisting or multiple forward servers. Supports failover and load balancing.",
    "total_fields": 5,
    "required_fields_count": 0,
    "fields_with_defaults_count": 4,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
