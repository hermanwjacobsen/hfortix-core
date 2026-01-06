"""Validation helpers for switch_controller/flow_tracking - Auto-generated"""

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
    "sample-mode": "perimeter",
    "sample-rate": 512,
    "format": "netflow9",
    "level": "ip",
    "max-export-pkt-size": 512,
    "template-export-period": 5,
    "timeout-general": 3600,
    "timeout-icmp": 300,
    "timeout-max": 604800,
    "timeout-tcp": 3600,
    "timeout-tcp-fin": 300,
    "timeout-tcp-rst": 120,
    "timeout-udp": 300,
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
    "sample-mode": "option",  # Configure sample mode for the flow tracking.
    "sample-rate": "integer",  # Configure sample rate for the perimeter and device-ingress s
    "format": "option",  # Configure flow tracking protocol.
    "collectors": "string",  # Configure collectors for the flow.
    "level": "option",  # Configure flow tracking level.
    "max-export-pkt-size": "integer",  # Configure flow max export packet size (512-9216, default=512
    "template-export-period": "integer",  # Configure template export period (1-60, default=5 minutes).
    "timeout-general": "integer",  # Configure flow session general timeout (60-604800, default=3
    "timeout-icmp": "integer",  # Configure flow session ICMP timeout (60-604800, default=300 
    "timeout-max": "integer",  # Configure flow session max timeout (60-604800, default=60480
    "timeout-tcp": "integer",  # Configure flow session TCP timeout (60-604800, default=3600 
    "timeout-tcp-fin": "integer",  # Configure flow session TCP FIN timeout (60-604800, default=3
    "timeout-tcp-rst": "integer",  # Configure flow session TCP RST timeout (60-604800, default=1
    "timeout-udp": "integer",  # Configure flow session UDP timeout (60-604800, default=300 s
    "aggregates": "string",  # Configure aggregates in which all traffic sessions matching 
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "sample-mode": "Configure sample mode for the flow tracking.",
    "sample-rate": "Configure sample rate for the perimeter and device-ingress sampling(0 - 99999).",
    "format": "Configure flow tracking protocol.",
    "collectors": "Configure collectors for the flow.",
    "level": "Configure flow tracking level.",
    "max-export-pkt-size": "Configure flow max export packet size (512-9216, default=512 bytes).",
    "template-export-period": "Configure template export period (1-60, default=5 minutes).",
    "timeout-general": "Configure flow session general timeout (60-604800, default=3600 seconds).",
    "timeout-icmp": "Configure flow session ICMP timeout (60-604800, default=300 seconds).",
    "timeout-max": "Configure flow session max timeout (60-604800, default=604800 seconds).",
    "timeout-tcp": "Configure flow session TCP timeout (60-604800, default=3600 seconds).",
    "timeout-tcp-fin": "Configure flow session TCP FIN timeout (60-604800, default=300 seconds).",
    "timeout-tcp-rst": "Configure flow session TCP RST timeout (60-604800, default=120 seconds).",
    "timeout-udp": "Configure flow session UDP timeout (60-604800, default=300 seconds).",
    "aggregates": "Configure aggregates in which all traffic sessions matching the IP Address will be grouped into the same flow.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "sample-rate": {"type": "integer", "min": 0, "max": 99999},
    "max-export-pkt-size": {"type": "integer", "min": 512, "max": 9216},
    "template-export-period": {"type": "integer", "min": 1, "max": 60},
    "timeout-general": {"type": "integer", "min": 60, "max": 604800},
    "timeout-icmp": {"type": "integer", "min": 60, "max": 604800},
    "timeout-max": {"type": "integer", "min": 60, "max": 604800},
    "timeout-tcp": {"type": "integer", "min": 60, "max": 604800},
    "timeout-tcp-fin": {"type": "integer", "min": 60, "max": 604800},
    "timeout-tcp-rst": {"type": "integer", "min": 60, "max": 604800},
    "timeout-udp": {"type": "integer", "min": 60, "max": 604800},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "collectors": {
        "name": {
            "type": "string",
            "help": "Collector name.",
            "default": "",
            "max_length": 63,
        },
        "ip": {
            "type": "ipv4-address-any",
            "help": "Collector IP address.",
            "default": "0.0.0.0",
        },
        "port": {
            "type": "integer",
            "help": "Collector port number(0-65535, default:0, netflow:2055, ipfix:4739).",
            "default": 0,
            "min_value": 0,
            "max_value": 65535,
        },
        "transport": {
            "type": "option",
            "help": "Collector L4 transport protocol for exporting packets.",
            "default": "udp",
            "options": [{"help": "UDP protocol.", "label": "Udp", "name": "udp"}, {"help": "TCP protocol.", "label": "Tcp", "name": "tcp"}, {"help": "SCTP protocol.", "label": "Sctp", "name": "sctp"}],
        },
    },
    "aggregates": {
        "id": {
            "type": "integer",
            "help": "Aggregate id.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "ip": {
            "type": "ipv4-classnet",
            "help": "IP address to group all matching traffic sessions to a flow.",
            "required": True,
            "default": "0.0.0.0 0.0.0.0",
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_SAMPLE_MODE = [
    "local",  # Set local mode which samples on the specific switch port.
    "perimeter",  # Set perimeter mode which samples on all switch fabric ports and fortilink port at the ingress.
    "device-ingress",  # Set device -ingress mode which samples across all switch ports at the ingress.
]
VALID_BODY_FORMAT = [
    "netflow1",  # Netflow version 1 sampling.
    "netflow5",  # Netflow version 5 sampling.
    "netflow9",  # Netflow version 9 sampling.
    "ipfix",  # Ipfix sampling.
]
VALID_BODY_LEVEL = [
    "vlan",  # Collects srcip/dstip/srcport/dstport/protocol/tos/vlan from the sample packet.
    "ip",  # Collects srcip/dstip from the sample packet.
    "port",  # Collects srcip/dstip/srcport/dstport/protocol from the sample packet.
    "proto",  # Collects srcip/dstip/protocol from the sample packet.
    "mac",  # Collects smac/dmac from the sample packet.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_switch_controller_flow_tracking_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for switch_controller/flow_tracking."""
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
    """Validate required fields for switch_controller/flow_tracking."""
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


def validate_switch_controller_flow_tracking_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new switch_controller/flow_tracking object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "sample-mode" in payload:
        value = payload["sample-mode"]
        if value not in VALID_BODY_SAMPLE_MODE:
            desc = FIELD_DESCRIPTIONS.get("sample-mode", "")
            error_msg = f"Invalid value for 'sample-mode': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SAMPLE_MODE)}"
            error_msg += f"\n  → Example: sample-mode='{{ VALID_BODY_SAMPLE_MODE[0] }}'"
            return (False, error_msg)
    if "format" in payload:
        value = payload["format"]
        if value not in VALID_BODY_FORMAT:
            desc = FIELD_DESCRIPTIONS.get("format", "")
            error_msg = f"Invalid value for 'format': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FORMAT)}"
            error_msg += f"\n  → Example: format='{{ VALID_BODY_FORMAT[0] }}'"
            return (False, error_msg)
    if "level" in payload:
        value = payload["level"]
        if value not in VALID_BODY_LEVEL:
            desc = FIELD_DESCRIPTIONS.get("level", "")
            error_msg = f"Invalid value for 'level': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LEVEL)}"
            error_msg += f"\n  → Example: level='{{ VALID_BODY_LEVEL[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_switch_controller_flow_tracking_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update switch_controller/flow_tracking."""
    # Step 1: Validate enum values
    if "sample-mode" in payload:
        value = payload["sample-mode"]
        if value not in VALID_BODY_SAMPLE_MODE:
            return (
                False,
                f"Invalid value for 'sample-mode'='{value}'. Must be one of: {', '.join(VALID_BODY_SAMPLE_MODE)}",
            )
    if "format" in payload:
        value = payload["format"]
        if value not in VALID_BODY_FORMAT:
            return (
                False,
                f"Invalid value for 'format'='{value}'. Must be one of: {', '.join(VALID_BODY_FORMAT)}",
            )
    if "level" in payload:
        value = payload["level"]
        if value not in VALID_BODY_LEVEL:
            return (
                False,
                f"Invalid value for 'level'='{value}'. Must be one of: {', '.join(VALID_BODY_LEVEL)}",
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
    "endpoint": "switch_controller/flow_tracking",
    "category": "cmdb",
    "api_path": "switch-controller/flow-tracking",
    "help": "Configure FortiSwitch flow tracking and export via ipfix/netflow.",
    "total_fields": 15,
    "required_fields_count": 0,
    "fields_with_defaults_count": 13,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
