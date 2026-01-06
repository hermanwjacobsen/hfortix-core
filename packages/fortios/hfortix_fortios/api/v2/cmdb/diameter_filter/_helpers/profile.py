"""Validation helpers for diameter_filter/profile - Auto-generated"""

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
    "name",  # Profile name.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "monitor-all-messages": "disable",
    "log-packet": "disable",
    "track-requests-answers": "enable",
    "missing-request-action": "block",
    "protocol-version-invalid": "block",
    "message-length-invalid": "block",
    "request-error-flag-set": "block",
    "cmd-flags-reserve-set": "block",
    "command-code-invalid": "block",
    "command-code-range": "",
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
    "name": "string",  # Profile name.
    "comment": "var-string",  # Comment.
    "monitor-all-messages": "option",  # Enable/disable logging for all User Name and Result Code AVP
    "log-packet": "option",  # Enable/disable packet log for triggered diameter settings.
    "track-requests-answers": "option",  # Enable/disable validation that each answer has a correspondi
    "missing-request-action": "option",  # Action to be taken for answers without corresponding request
    "protocol-version-invalid": "option",  # Action to be taken for invalid protocol version.
    "message-length-invalid": "option",  # Action to be taken for invalid message length.
    "request-error-flag-set": "option",  # Action to be taken for request messages with error flag set.
    "cmd-flags-reserve-set": "option",  # Action to be taken for messages with cmd flag reserve bits s
    "command-code-invalid": "option",  # Action to be taken for messages with invalid command code.
    "command-code-range": "user",  # Valid range for command codes (0-16777215).
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "Profile name.",
    "comment": "Comment.",
    "monitor-all-messages": "Enable/disable logging for all User Name and Result Code AVP messages.",
    "log-packet": "Enable/disable packet log for triggered diameter settings.",
    "track-requests-answers": "Enable/disable validation that each answer has a corresponding request.",
    "missing-request-action": "Action to be taken for answers without corresponding request.",
    "protocol-version-invalid": "Action to be taken for invalid protocol version.",
    "message-length-invalid": "Action to be taken for invalid message length.",
    "request-error-flag-set": "Action to be taken for request messages with error flag set.",
    "cmd-flags-reserve-set": "Action to be taken for messages with cmd flag reserve bits set.",
    "command-code-invalid": "Action to be taken for messages with invalid command code.",
    "command-code-range": "Valid range for command codes (0-16777215).",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 47},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
}


# Valid enum values from API documentation
VALID_BODY_MONITOR_ALL_MESSAGES = [
    "disable",  # Disable.
    "enable",  # Enable.
]
VALID_BODY_LOG_PACKET = [
    "disable",  # Disable.
    "enable",  # Enable.
]
VALID_BODY_TRACK_REQUESTS_ANSWERS = [
    "disable",  # Disable.
    "enable",  # Enable.
]
VALID_BODY_MISSING_REQUEST_ACTION = [
    "allow",  # Allow or pass matching traffic.
    "block",  # Block or drop matching traffic.
    "reset",  # Reset sessions for matching traffic.
    "monitor",  # Allow and log matching traffic.
]
VALID_BODY_PROTOCOL_VERSION_INVALID = [
    "allow",  # Allow or pass matching traffic.
    "block",  # Block or drop matching traffic.
    "reset",  # Reset sessions for matching traffic.
    "monitor",  # Allow and log matching traffic.
]
VALID_BODY_MESSAGE_LENGTH_INVALID = [
    "allow",  # Allow or pass matching traffic.
    "block",  # Block or drop matching traffic.
    "reset",  # Reset sessions for matching traffic.
    "monitor",  # Allow and log matching traffic.
]
VALID_BODY_REQUEST_ERROR_FLAG_SET = [
    "allow",  # Allow or pass matching traffic.
    "block",  # Block or drop matching traffic.
    "reset",  # Reset sessions for matching traffic.
    "monitor",  # Allow and log matching traffic.
]
VALID_BODY_CMD_FLAGS_RESERVE_SET = [
    "allow",  # Allow or pass matching traffic.
    "block",  # Block or drop matching traffic.
    "reset",  # Reset sessions for matching traffic.
    "monitor",  # Allow and log matching traffic.
]
VALID_BODY_COMMAND_CODE_INVALID = [
    "allow",  # Allow or pass matching traffic.
    "block",  # Block or drop matching traffic.
    "reset",  # Reset sessions for matching traffic.
    "monitor",  # Allow and log matching traffic.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_diameter_filter_profile_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for diameter_filter/profile."""
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
    """Validate required fields for diameter_filter/profile."""
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


def validate_diameter_filter_profile_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new diameter_filter/profile object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "monitor-all-messages" in payload:
        value = payload["monitor-all-messages"]
        if value not in VALID_BODY_MONITOR_ALL_MESSAGES:
            desc = FIELD_DESCRIPTIONS.get("monitor-all-messages", "")
            error_msg = f"Invalid value for 'monitor-all-messages': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MONITOR_ALL_MESSAGES)}"
            error_msg += f"\n  → Example: monitor-all-messages='{{ VALID_BODY_MONITOR_ALL_MESSAGES[0] }}'"
            return (False, error_msg)
    if "log-packet" in payload:
        value = payload["log-packet"]
        if value not in VALID_BODY_LOG_PACKET:
            desc = FIELD_DESCRIPTIONS.get("log-packet", "")
            error_msg = f"Invalid value for 'log-packet': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LOG_PACKET)}"
            error_msg += f"\n  → Example: log-packet='{{ VALID_BODY_LOG_PACKET[0] }}'"
            return (False, error_msg)
    if "track-requests-answers" in payload:
        value = payload["track-requests-answers"]
        if value not in VALID_BODY_TRACK_REQUESTS_ANSWERS:
            desc = FIELD_DESCRIPTIONS.get("track-requests-answers", "")
            error_msg = f"Invalid value for 'track-requests-answers': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_TRACK_REQUESTS_ANSWERS)}"
            error_msg += f"\n  → Example: track-requests-answers='{{ VALID_BODY_TRACK_REQUESTS_ANSWERS[0] }}'"
            return (False, error_msg)
    if "missing-request-action" in payload:
        value = payload["missing-request-action"]
        if value not in VALID_BODY_MISSING_REQUEST_ACTION:
            desc = FIELD_DESCRIPTIONS.get("missing-request-action", "")
            error_msg = f"Invalid value for 'missing-request-action': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MISSING_REQUEST_ACTION)}"
            error_msg += f"\n  → Example: missing-request-action='{{ VALID_BODY_MISSING_REQUEST_ACTION[0] }}'"
            return (False, error_msg)
    if "protocol-version-invalid" in payload:
        value = payload["protocol-version-invalid"]
        if value not in VALID_BODY_PROTOCOL_VERSION_INVALID:
            desc = FIELD_DESCRIPTIONS.get("protocol-version-invalid", "")
            error_msg = f"Invalid value for 'protocol-version-invalid': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PROTOCOL_VERSION_INVALID)}"
            error_msg += f"\n  → Example: protocol-version-invalid='{{ VALID_BODY_PROTOCOL_VERSION_INVALID[0] }}'"
            return (False, error_msg)
    if "message-length-invalid" in payload:
        value = payload["message-length-invalid"]
        if value not in VALID_BODY_MESSAGE_LENGTH_INVALID:
            desc = FIELD_DESCRIPTIONS.get("message-length-invalid", "")
            error_msg = f"Invalid value for 'message-length-invalid': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MESSAGE_LENGTH_INVALID)}"
            error_msg += f"\n  → Example: message-length-invalid='{{ VALID_BODY_MESSAGE_LENGTH_INVALID[0] }}'"
            return (False, error_msg)
    if "request-error-flag-set" in payload:
        value = payload["request-error-flag-set"]
        if value not in VALID_BODY_REQUEST_ERROR_FLAG_SET:
            desc = FIELD_DESCRIPTIONS.get("request-error-flag-set", "")
            error_msg = f"Invalid value for 'request-error-flag-set': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_REQUEST_ERROR_FLAG_SET)}"
            error_msg += f"\n  → Example: request-error-flag-set='{{ VALID_BODY_REQUEST_ERROR_FLAG_SET[0] }}'"
            return (False, error_msg)
    if "cmd-flags-reserve-set" in payload:
        value = payload["cmd-flags-reserve-set"]
        if value not in VALID_BODY_CMD_FLAGS_RESERVE_SET:
            desc = FIELD_DESCRIPTIONS.get("cmd-flags-reserve-set", "")
            error_msg = f"Invalid value for 'cmd-flags-reserve-set': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CMD_FLAGS_RESERVE_SET)}"
            error_msg += f"\n  → Example: cmd-flags-reserve-set='{{ VALID_BODY_CMD_FLAGS_RESERVE_SET[0] }}'"
            return (False, error_msg)
    if "command-code-invalid" in payload:
        value = payload["command-code-invalid"]
        if value not in VALID_BODY_COMMAND_CODE_INVALID:
            desc = FIELD_DESCRIPTIONS.get("command-code-invalid", "")
            error_msg = f"Invalid value for 'command-code-invalid': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_COMMAND_CODE_INVALID)}"
            error_msg += f"\n  → Example: command-code-invalid='{{ VALID_BODY_COMMAND_CODE_INVALID[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_diameter_filter_profile_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update diameter_filter/profile."""
    # Step 1: Validate enum values
    if "monitor-all-messages" in payload:
        value = payload["monitor-all-messages"]
        if value not in VALID_BODY_MONITOR_ALL_MESSAGES:
            return (
                False,
                f"Invalid value for 'monitor-all-messages'='{value}'. Must be one of: {', '.join(VALID_BODY_MONITOR_ALL_MESSAGES)}",
            )
    if "log-packet" in payload:
        value = payload["log-packet"]
        if value not in VALID_BODY_LOG_PACKET:
            return (
                False,
                f"Invalid value for 'log-packet'='{value}'. Must be one of: {', '.join(VALID_BODY_LOG_PACKET)}",
            )
    if "track-requests-answers" in payload:
        value = payload["track-requests-answers"]
        if value not in VALID_BODY_TRACK_REQUESTS_ANSWERS:
            return (
                False,
                f"Invalid value for 'track-requests-answers'='{value}'. Must be one of: {', '.join(VALID_BODY_TRACK_REQUESTS_ANSWERS)}",
            )
    if "missing-request-action" in payload:
        value = payload["missing-request-action"]
        if value not in VALID_BODY_MISSING_REQUEST_ACTION:
            return (
                False,
                f"Invalid value for 'missing-request-action'='{value}'. Must be one of: {', '.join(VALID_BODY_MISSING_REQUEST_ACTION)}",
            )
    if "protocol-version-invalid" in payload:
        value = payload["protocol-version-invalid"]
        if value not in VALID_BODY_PROTOCOL_VERSION_INVALID:
            return (
                False,
                f"Invalid value for 'protocol-version-invalid'='{value}'. Must be one of: {', '.join(VALID_BODY_PROTOCOL_VERSION_INVALID)}",
            )
    if "message-length-invalid" in payload:
        value = payload["message-length-invalid"]
        if value not in VALID_BODY_MESSAGE_LENGTH_INVALID:
            return (
                False,
                f"Invalid value for 'message-length-invalid'='{value}'. Must be one of: {', '.join(VALID_BODY_MESSAGE_LENGTH_INVALID)}",
            )
    if "request-error-flag-set" in payload:
        value = payload["request-error-flag-set"]
        if value not in VALID_BODY_REQUEST_ERROR_FLAG_SET:
            return (
                False,
                f"Invalid value for 'request-error-flag-set'='{value}'. Must be one of: {', '.join(VALID_BODY_REQUEST_ERROR_FLAG_SET)}",
            )
    if "cmd-flags-reserve-set" in payload:
        value = payload["cmd-flags-reserve-set"]
        if value not in VALID_BODY_CMD_FLAGS_RESERVE_SET:
            return (
                False,
                f"Invalid value for 'cmd-flags-reserve-set'='{value}'. Must be one of: {', '.join(VALID_BODY_CMD_FLAGS_RESERVE_SET)}",
            )
    if "command-code-invalid" in payload:
        value = payload["command-code-invalid"]
        if value not in VALID_BODY_COMMAND_CODE_INVALID:
            return (
                False,
                f"Invalid value for 'command-code-invalid'='{value}'. Must be one of: {', '.join(VALID_BODY_COMMAND_CODE_INVALID)}",
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
    "endpoint": "diameter_filter/profile",
    "category": "cmdb",
    "api_path": "diameter-filter/profile",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure Diameter filter profiles.",
    "total_fields": 12,
    "required_fields_count": 1,
    "fields_with_defaults_count": 11,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
