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
            "options": [{"help": "Traffic log.", "label": "Traffic", "name": "traffic"}, {"help": "Event log.", "label": "Event", "name": "event"}, {"help": "Antivirus log.", "label": "Virus", "name": "virus"}, {"help": "Web filter log.", "label": "Webfilter", "name": "webfilter"}, {"help": "Attack log.", "label": "Attack", "name": "attack"}, {"help": "Antispam log.", "label": "Spam", "name": "spam"}, {"help": "Anomaly log.", "label": "Anomaly", "name": "anomaly"}, {"help": "VoIP log.", "label": "Voip", "name": "voip"}, {"help": "DLP log.", "label": "Dlp", "name": "dlp"}, {"help": "Application control log.", "label": "App Ctrl", "name": "app-ctrl"}, {"help": "Web application firewall log.", "label": "Waf", "name": "waf"}, {"help": "GTP log.", "label": "Gtp", "name": "gtp"}, {"help": "DNS detail log.", "label": "Dns", "name": "dns"}, {"help": "SSH log.", "label": "Ssh", "name": "ssh"}, {"help": "SSL log.", "label": "Ssl", "name": "ssl"}, {"help": "File filter log.", "label": "File Filter", "name": "file-filter"}, {"help": "ICAP log.", "label": "Icap", "name": "icap"}, {"help": "Virtual patch log.", "label": "Virtual Patch", "name": "virtual-patch"}, {"help": "Debug log.", "label": "Debug", "name": "debug"}],
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
            "options": [{"help": "Include logs that match the filter.", "label": "Include", "name": "include"}, {"help": "Exclude logs that match the filter.", "label": "Exclude", "name": "exclude"}],
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_SEVERITY = [
    "emergency",  # Emergency level.
    "alert",  # Alert level.
    "critical",  # Critical level.
    "error",  # Error level.
    "warning",  # Warning level.
    "notification",  # Notification level.
    "information",  # Information level.
    "debug",  # Debug level.
]
VALID_BODY_FORWARD_TRAFFIC = [
    "enable",  # Enable forward traffic logging.
    "disable",  # Disable forward traffic logging.
]
VALID_BODY_LOCAL_TRAFFIC = [
    "enable",  # Enable local in or out traffic logging.
    "disable",  # Disable local in or out traffic logging.
]
VALID_BODY_MULTICAST_TRAFFIC = [
    "enable",  # Enable multicast traffic logging.
    "disable",  # Disable multicast traffic logging.
]
VALID_BODY_SNIFFER_TRAFFIC = [
    "enable",  # Enable sniffer traffic logging.
    "disable",  # Disable sniffer traffic logging.
]
VALID_BODY_ZTNA_TRAFFIC = [
    "enable",  # Enable ztna traffic logging.
    "disable",  # Disable ztna traffic logging.
]
VALID_BODY_HTTP_TRANSACTION = [
    "enable",  # Enable http transaction logging.
    "disable",  # Disable http transaction logging.
]
VALID_BODY_ANOMALY = [
    "enable",  # Enable anomaly logging.
    "disable",  # Disable anomaly logging.
]
VALID_BODY_VOIP = [
    "enable",  # Enable VoIP logging.
    "disable",  # Disable VoIP logging.
]
VALID_BODY_GTP = [
    "enable",  # Enable GTP messages logging.
    "disable",  # Disable GTP messages logging.
]
VALID_BODY_FORTI_SWITCH = [
    "enable",  # Enable Forti-Switch logging.
    "disable",  # Disable Forti-Switch logging.
]
VALID_BODY_DEBUG = [
    "enable",  # Enable Debug logging.
    "disable",  # Disable Debug logging.
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
    """Validate required fields for log/syslogd3/override_filter."""
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


def validate_log_syslogd3_override_filter_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new log/syslogd3/override_filter object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "severity" in payload:
        value = payload["severity"]
        if value not in VALID_BODY_SEVERITY:
            desc = FIELD_DESCRIPTIONS.get("severity", "")
            error_msg = f"Invalid value for 'severity': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SEVERITY)}"
            error_msg += f"\n  → Example: severity='{{ VALID_BODY_SEVERITY[0] }}'"
            return (False, error_msg)
    if "forward-traffic" in payload:
        value = payload["forward-traffic"]
        if value not in VALID_BODY_FORWARD_TRAFFIC:
            desc = FIELD_DESCRIPTIONS.get("forward-traffic", "")
            error_msg = f"Invalid value for 'forward-traffic': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FORWARD_TRAFFIC)}"
            error_msg += f"\n  → Example: forward-traffic='{{ VALID_BODY_FORWARD_TRAFFIC[0] }}'"
            return (False, error_msg)
    if "local-traffic" in payload:
        value = payload["local-traffic"]
        if value not in VALID_BODY_LOCAL_TRAFFIC:
            desc = FIELD_DESCRIPTIONS.get("local-traffic", "")
            error_msg = f"Invalid value for 'local-traffic': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LOCAL_TRAFFIC)}"
            error_msg += f"\n  → Example: local-traffic='{{ VALID_BODY_LOCAL_TRAFFIC[0] }}'"
            return (False, error_msg)
    if "multicast-traffic" in payload:
        value = payload["multicast-traffic"]
        if value not in VALID_BODY_MULTICAST_TRAFFIC:
            desc = FIELD_DESCRIPTIONS.get("multicast-traffic", "")
            error_msg = f"Invalid value for 'multicast-traffic': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MULTICAST_TRAFFIC)}"
            error_msg += f"\n  → Example: multicast-traffic='{{ VALID_BODY_MULTICAST_TRAFFIC[0] }}'"
            return (False, error_msg)
    if "sniffer-traffic" in payload:
        value = payload["sniffer-traffic"]
        if value not in VALID_BODY_SNIFFER_TRAFFIC:
            desc = FIELD_DESCRIPTIONS.get("sniffer-traffic", "")
            error_msg = f"Invalid value for 'sniffer-traffic': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SNIFFER_TRAFFIC)}"
            error_msg += f"\n  → Example: sniffer-traffic='{{ VALID_BODY_SNIFFER_TRAFFIC[0] }}'"
            return (False, error_msg)
    if "ztna-traffic" in payload:
        value = payload["ztna-traffic"]
        if value not in VALID_BODY_ZTNA_TRAFFIC:
            desc = FIELD_DESCRIPTIONS.get("ztna-traffic", "")
            error_msg = f"Invalid value for 'ztna-traffic': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ZTNA_TRAFFIC)}"
            error_msg += f"\n  → Example: ztna-traffic='{{ VALID_BODY_ZTNA_TRAFFIC[0] }}'"
            return (False, error_msg)
    if "http-transaction" in payload:
        value = payload["http-transaction"]
        if value not in VALID_BODY_HTTP_TRANSACTION:
            desc = FIELD_DESCRIPTIONS.get("http-transaction", "")
            error_msg = f"Invalid value for 'http-transaction': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_HTTP_TRANSACTION)}"
            error_msg += f"\n  → Example: http-transaction='{{ VALID_BODY_HTTP_TRANSACTION[0] }}'"
            return (False, error_msg)
    if "anomaly" in payload:
        value = payload["anomaly"]
        if value not in VALID_BODY_ANOMALY:
            desc = FIELD_DESCRIPTIONS.get("anomaly", "")
            error_msg = f"Invalid value for 'anomaly': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ANOMALY)}"
            error_msg += f"\n  → Example: anomaly='{{ VALID_BODY_ANOMALY[0] }}'"
            return (False, error_msg)
    if "voip" in payload:
        value = payload["voip"]
        if value not in VALID_BODY_VOIP:
            desc = FIELD_DESCRIPTIONS.get("voip", "")
            error_msg = f"Invalid value for 'voip': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_VOIP)}"
            error_msg += f"\n  → Example: voip='{{ VALID_BODY_VOIP[0] }}'"
            return (False, error_msg)
    if "gtp" in payload:
        value = payload["gtp"]
        if value not in VALID_BODY_GTP:
            desc = FIELD_DESCRIPTIONS.get("gtp", "")
            error_msg = f"Invalid value for 'gtp': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GTP)}"
            error_msg += f"\n  → Example: gtp='{{ VALID_BODY_GTP[0] }}'"
            return (False, error_msg)
    if "forti-switch" in payload:
        value = payload["forti-switch"]
        if value not in VALID_BODY_FORTI_SWITCH:
            desc = FIELD_DESCRIPTIONS.get("forti-switch", "")
            error_msg = f"Invalid value for 'forti-switch': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FORTI_SWITCH)}"
            error_msg += f"\n  → Example: forti-switch='{{ VALID_BODY_FORTI_SWITCH[0] }}'"
            return (False, error_msg)
    if "debug" in payload:
        value = payload["debug"]
        if value not in VALID_BODY_DEBUG:
            desc = FIELD_DESCRIPTIONS.get("debug", "")
            error_msg = f"Invalid value for 'debug': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DEBUG)}"
            error_msg += f"\n  → Example: debug='{{ VALID_BODY_DEBUG[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_log_syslogd3_override_filter_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update log/syslogd3/override_filter."""
    # Step 1: Validate enum values
    if "severity" in payload:
        value = payload["severity"]
        if value not in VALID_BODY_SEVERITY:
            return (
                False,
                f"Invalid value for 'severity'='{value}'. Must be one of: {', '.join(VALID_BODY_SEVERITY)}",
            )
    if "forward-traffic" in payload:
        value = payload["forward-traffic"]
        if value not in VALID_BODY_FORWARD_TRAFFIC:
            return (
                False,
                f"Invalid value for 'forward-traffic'='{value}'. Must be one of: {', '.join(VALID_BODY_FORWARD_TRAFFIC)}",
            )
    if "local-traffic" in payload:
        value = payload["local-traffic"]
        if value not in VALID_BODY_LOCAL_TRAFFIC:
            return (
                False,
                f"Invalid value for 'local-traffic'='{value}'. Must be one of: {', '.join(VALID_BODY_LOCAL_TRAFFIC)}",
            )
    if "multicast-traffic" in payload:
        value = payload["multicast-traffic"]
        if value not in VALID_BODY_MULTICAST_TRAFFIC:
            return (
                False,
                f"Invalid value for 'multicast-traffic'='{value}'. Must be one of: {', '.join(VALID_BODY_MULTICAST_TRAFFIC)}",
            )
    if "sniffer-traffic" in payload:
        value = payload["sniffer-traffic"]
        if value not in VALID_BODY_SNIFFER_TRAFFIC:
            return (
                False,
                f"Invalid value for 'sniffer-traffic'='{value}'. Must be one of: {', '.join(VALID_BODY_SNIFFER_TRAFFIC)}",
            )
    if "ztna-traffic" in payload:
        value = payload["ztna-traffic"]
        if value not in VALID_BODY_ZTNA_TRAFFIC:
            return (
                False,
                f"Invalid value for 'ztna-traffic'='{value}'. Must be one of: {', '.join(VALID_BODY_ZTNA_TRAFFIC)}",
            )
    if "http-transaction" in payload:
        value = payload["http-transaction"]
        if value not in VALID_BODY_HTTP_TRANSACTION:
            return (
                False,
                f"Invalid value for 'http-transaction'='{value}'. Must be one of: {', '.join(VALID_BODY_HTTP_TRANSACTION)}",
            )
    if "anomaly" in payload:
        value = payload["anomaly"]
        if value not in VALID_BODY_ANOMALY:
            return (
                False,
                f"Invalid value for 'anomaly'='{value}'. Must be one of: {', '.join(VALID_BODY_ANOMALY)}",
            )
    if "voip" in payload:
        value = payload["voip"]
        if value not in VALID_BODY_VOIP:
            return (
                False,
                f"Invalid value for 'voip'='{value}'. Must be one of: {', '.join(VALID_BODY_VOIP)}",
            )
    if "gtp" in payload:
        value = payload["gtp"]
        if value not in VALID_BODY_GTP:
            return (
                False,
                f"Invalid value for 'gtp'='{value}'. Must be one of: {', '.join(VALID_BODY_GTP)}",
            )
    if "forti-switch" in payload:
        value = payload["forti-switch"]
        if value not in VALID_BODY_FORTI_SWITCH:
            return (
                False,
                f"Invalid value for 'forti-switch'='{value}'. Must be one of: {', '.join(VALID_BODY_FORTI_SWITCH)}",
            )
    if "debug" in payload:
        value = payload["debug"]
        if value not in VALID_BODY_DEBUG:
            return (
                False,
                f"Invalid value for 'debug'='{value}'. Must be one of: {', '.join(VALID_BODY_DEBUG)}",
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
