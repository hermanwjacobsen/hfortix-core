"""Validation helpers for log/syslogd3/override_filter - Auto-generated"""

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

# Import central validation functions (avoid duplication across 1,062 files)
from hfortix_fortios._helpers.validation import (
    validate_required_fields as _validate_required_fields,
    validate_enum_field as _validate_enum_field,
    validate_query_parameter as _validate_query_parameter,
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
    "severity": "information",
    "forward-traffic": "enable",
    "local-traffic": "enable",
    "multicast-traffic": "enable",
    "sniffer-traffic": "enable",
    "ztna-traffic": "enable",
    "http-transaction": "enable",
    "anomaly": "enable",
    "voip": "enable",
    "gtp": "enable",
    "forti-switch": "enable",
    "debug": "disable",
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
    "severity": "option",  # Lowest severity level to log.
    "forward-traffic": "option",  # Enable/disable forward traffic logging.
    "local-traffic": "option",  # Enable/disable local in or out traffic logging.
    "multicast-traffic": "option",  # Enable/disable multicast traffic logging.
    "sniffer-traffic": "option",  # Enable/disable sniffer traffic logging.
    "ztna-traffic": "option",  # Enable/disable ztna traffic logging.
    "http-transaction": "option",  # Enable/disable log HTTP transaction messages.
    "anomaly": "option",  # Enable/disable anomaly logging.
    "voip": "option",  # Enable/disable VoIP logging.
    "gtp": "option",  # Enable/disable GTP messages logging.
    "forti-switch": "option",  # Enable/disable Forti-Switch logging.
    "debug": "option",  # Enable/disable debug logging.
    "free-style": "string",  # Free style filters.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "severity": "Lowest severity level to log.",
    "forward-traffic": "Enable/disable forward traffic logging.",
    "local-traffic": "Enable/disable local in or out traffic logging.",
    "multicast-traffic": "Enable/disable multicast traffic logging.",
    "sniffer-traffic": "Enable/disable sniffer traffic logging.",
    "ztna-traffic": "Enable/disable ztna traffic logging.",
    "http-transaction": "Enable/disable log HTTP transaction messages.",
    "anomaly": "Enable/disable anomaly logging.",
    "voip": "Enable/disable VoIP logging.",
    "gtp": "Enable/disable GTP messages logging.",
    "forti-switch": "Enable/disable Forti-Switch logging.",
    "debug": "Enable/disable debug logging.",
    "free-style": "Free style filters.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "free-style": {
        "id": {
            "type": "integer",
            "help": "Entry ID.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "category": {
            "type": "option",
            "help": "Log category.",
            "required": True,
            "default": "traffic",
            "options": ["traffic", "event", "virus", "webfilter", "attack", "spam", "anomaly", "voip", "dlp", "app-ctrl", "waf", "gtp", "dns", "ssh", "ssl", "file-filter", "icap", "virtual-patch", "debug"],
        },
        "filter": {
            "type": "string",
            "help": "Free style filter string.",
            "required": True,
            "default": "",
            "max_length": 1023,
        },
        "filter-type": {
            "type": "option",
            "help": "Include/exclude logs that match the filter.",
            "default": "include",
            "options": ["include", "exclude"],
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_SEVERITY = [
    "emergency",
    "alert",
    "critical",
    "error",
    "warning",
    "notification",
    "information",
    "debug",
]
VALID_BODY_FORWARD_TRAFFIC = [
    "enable",
    "disable",
]
VALID_BODY_LOCAL_TRAFFIC = [
    "enable",
    "disable",
]
VALID_BODY_MULTICAST_TRAFFIC = [
    "enable",
    "disable",
]
VALID_BODY_SNIFFER_TRAFFIC = [
    "enable",
    "disable",
]
VALID_BODY_ZTNA_TRAFFIC = [
    "enable",
    "disable",
]
VALID_BODY_HTTP_TRANSACTION = [
    "enable",
    "disable",
]
VALID_BODY_ANOMALY = [
    "enable",
    "disable",
]
VALID_BODY_VOIP = [
    "enable",
    "disable",
]
VALID_BODY_GTP = [
    "enable",
    "disable",
]
VALID_BODY_FORTI_SWITCH = [
    "enable",
    "disable",
]
VALID_BODY_DEBUG = [
    "enable",
    "disable",
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_log_syslogd3_override_filter_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for log/syslogd3/override_filter."""
    # Validate query parameters using central function
    if "action" in params:
        is_valid, error = _validate_query_parameter(
            "action",
            params.get("action"),
            VALID_QUERY_ACTION
        )
        if not is_valid:
            return (False, error)

    return (True, None)


# ============================================================================
# POST Validation
# ============================================================================


def validate_log_syslogd3_override_filter_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new log/syslogd3/override_filter object."""
    # Step 1: Validate required fields using central function
    is_valid, error = _validate_required_fields(
        payload,
        REQUIRED_FIELDS,
        FIELD_DESCRIPTIONS
    )
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values using central function
    if "severity" in payload:
        is_valid, error = _validate_enum_field(
            "severity",
            payload["severity"],
            VALID_BODY_SEVERITY,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "forward-traffic" in payload:
        is_valid, error = _validate_enum_field(
            "forward-traffic",
            payload["forward-traffic"],
            VALID_BODY_FORWARD_TRAFFIC,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "local-traffic" in payload:
        is_valid, error = _validate_enum_field(
            "local-traffic",
            payload["local-traffic"],
            VALID_BODY_LOCAL_TRAFFIC,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "multicast-traffic" in payload:
        is_valid, error = _validate_enum_field(
            "multicast-traffic",
            payload["multicast-traffic"],
            VALID_BODY_MULTICAST_TRAFFIC,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "sniffer-traffic" in payload:
        is_valid, error = _validate_enum_field(
            "sniffer-traffic",
            payload["sniffer-traffic"],
            VALID_BODY_SNIFFER_TRAFFIC,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "ztna-traffic" in payload:
        is_valid, error = _validate_enum_field(
            "ztna-traffic",
            payload["ztna-traffic"],
            VALID_BODY_ZTNA_TRAFFIC,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "http-transaction" in payload:
        is_valid, error = _validate_enum_field(
            "http-transaction",
            payload["http-transaction"],
            VALID_BODY_HTTP_TRANSACTION,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "anomaly" in payload:
        is_valid, error = _validate_enum_field(
            "anomaly",
            payload["anomaly"],
            VALID_BODY_ANOMALY,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "voip" in payload:
        is_valid, error = _validate_enum_field(
            "voip",
            payload["voip"],
            VALID_BODY_VOIP,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "gtp" in payload:
        is_valid, error = _validate_enum_field(
            "gtp",
            payload["gtp"],
            VALID_BODY_GTP,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "forti-switch" in payload:
        is_valid, error = _validate_enum_field(
            "forti-switch",
            payload["forti-switch"],
            VALID_BODY_FORTI_SWITCH,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "debug" in payload:
        is_valid, error = _validate_enum_field(
            "debug",
            payload["debug"],
            VALID_BODY_DEBUG,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_log_syslogd3_override_filter_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update log/syslogd3/override_filter."""
    # Validate enum values using central function
    if "severity" in payload:
        is_valid, error = _validate_enum_field(
            "severity",
            payload["severity"],
            VALID_BODY_SEVERITY,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "forward-traffic" in payload:
        is_valid, error = _validate_enum_field(
            "forward-traffic",
            payload["forward-traffic"],
            VALID_BODY_FORWARD_TRAFFIC,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "local-traffic" in payload:
        is_valid, error = _validate_enum_field(
            "local-traffic",
            payload["local-traffic"],
            VALID_BODY_LOCAL_TRAFFIC,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "multicast-traffic" in payload:
        is_valid, error = _validate_enum_field(
            "multicast-traffic",
            payload["multicast-traffic"],
            VALID_BODY_MULTICAST_TRAFFIC,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "sniffer-traffic" in payload:
        is_valid, error = _validate_enum_field(
            "sniffer-traffic",
            payload["sniffer-traffic"],
            VALID_BODY_SNIFFER_TRAFFIC,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "ztna-traffic" in payload:
        is_valid, error = _validate_enum_field(
            "ztna-traffic",
            payload["ztna-traffic"],
            VALID_BODY_ZTNA_TRAFFIC,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "http-transaction" in payload:
        is_valid, error = _validate_enum_field(
            "http-transaction",
            payload["http-transaction"],
            VALID_BODY_HTTP_TRANSACTION,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "anomaly" in payload:
        is_valid, error = _validate_enum_field(
            "anomaly",
            payload["anomaly"],
            VALID_BODY_ANOMALY,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "voip" in payload:
        is_valid, error = _validate_enum_field(
            "voip",
            payload["voip"],
            VALID_BODY_VOIP,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "gtp" in payload:
        is_valid, error = _validate_enum_field(
            "gtp",
            payload["gtp"],
            VALID_BODY_GTP,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "forti-switch" in payload:
        is_valid, error = _validate_enum_field(
            "forti-switch",
            payload["forti-switch"],
            VALID_BODY_FORTI_SWITCH,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "debug" in payload:
        is_valid, error = _validate_enum_field(
            "debug",
            payload["debug"],
            VALID_BODY_DEBUG,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)

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
    "endpoint": "log/syslogd3/override_filter",
    "category": "cmdb",
    "api_path": "log.syslogd3/override-filter",
    "help": "Override filters for remote system server.",
    "total_fields": 13,
    "required_fields_count": 0,
    "fields_with_defaults_count": 12,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
