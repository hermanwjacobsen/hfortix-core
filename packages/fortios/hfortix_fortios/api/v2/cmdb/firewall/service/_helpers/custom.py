"""Validation helpers for firewall/service/custom - Auto-generated"""

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
    "uuid": "00000000-0000-0000-0000-000000000000",
    "proxy": "disable",
    "category": "",
    "protocol": "TCP/UDP/UDP-Lite/SCTP",
    "helper": "auto",
    "iprange": "",
    "fqdn": "",
    "protocol-number": 0,
    "icmptype": "",
    "icmpcode": "",
    "tcp-portrange": "",
    "udp-portrange": "",
    "udplite-portrange": "",
    "sctp-portrange": "",
    "tcp-halfclose-timer": 0,
    "tcp-halfopen-timer": 0,
    "tcp-timewait-timer": 0,
    "tcp-rst-timer": 0,
    "udp-idle-timer": 0,
    "session-ttl": "",
    "check-reset-range": "default",
    "color": 0,
    "app-service-type": "disable",
    "fabric-object": "disable",
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
    "name": "string",  # Custom service name.
    "uuid": "uuid",  # Universally Unique Identifier (UUID; automatically assigned 
    "proxy": "option",  # Enable/disable web proxy service.
    "category": "string",  # Service category.
    "protocol": "option",  # Protocol type based on IANA numbers.
    "helper": "option",  # Helper name.
    "iprange": "user",  # Start and end of the IP range associated with service.
    "fqdn": "string",  # Fully qualified domain name.
    "protocol-number": "integer",  # IP protocol number.
    "icmptype": "integer",  # ICMP type.
    "icmpcode": "integer",  # ICMP code.
    "tcp-portrange": "user",  # Multiple TCP port ranges.
    "udp-portrange": "user",  # Multiple UDP port ranges.
    "udplite-portrange": "user",  # Multiple UDP-Lite port ranges.
    "sctp-portrange": "user",  # Multiple SCTP port ranges.
    "tcp-halfclose-timer": "integer",  # Wait time to close a TCP session waiting for an unanswered F
    "tcp-halfopen-timer": "integer",  # Wait time to close a TCP session waiting for an unanswered o
    "tcp-timewait-timer": "integer",  # Set the length of the TCP TIME-WAIT state in seconds (1 - 30
    "tcp-rst-timer": "integer",  # Set the length of the TCP CLOSE state in seconds (5 - 300 se
    "udp-idle-timer": "integer",  # Number of seconds before an idle UDP/UDP-Lite connection tim
    "session-ttl": "user",  # Session TTL (300 - 2764800, 0 = default).
    "check-reset-range": "option",  # Configure the type of ICMP error message verification.
    "comment": "var-string",  # Comment.
    "color": "integer",  # Color of icon on the GUI.
    "app-service-type": "option",  # Application service type.
    "app-category": "string",  # Application category ID.
    "application": "string",  # Application ID.
    "fabric-object": "option",  # Security Fabric global object setting.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "Custom service name.",
    "uuid": "Universally Unique Identifier (UUID; automatically assigned but can be manually reset).",
    "proxy": "Enable/disable web proxy service.",
    "category": "Service category.",
    "protocol": "Protocol type based on IANA numbers.",
    "helper": "Helper name.",
    "iprange": "Start and end of the IP range associated with service.",
    "fqdn": "Fully qualified domain name.",
    "protocol-number": "IP protocol number.",
    "icmptype": "ICMP type.",
    "icmpcode": "ICMP code.",
    "tcp-portrange": "Multiple TCP port ranges.",
    "udp-portrange": "Multiple UDP port ranges.",
    "udplite-portrange": "Multiple UDP-Lite port ranges.",
    "sctp-portrange": "Multiple SCTP port ranges.",
    "tcp-halfclose-timer": "Wait time to close a TCP session waiting for an unanswered FIN packet (1 - 86400 sec, 0 = default).",
    "tcp-halfopen-timer": "Wait time to close a TCP session waiting for an unanswered open session packet (1 - 86400 sec, 0 = default).",
    "tcp-timewait-timer": "Set the length of the TCP TIME-WAIT state in seconds (1 - 300 sec, 0 = default).",
    "tcp-rst-timer": "Set the length of the TCP CLOSE state in seconds (5 - 300 sec, 0 = default).",
    "udp-idle-timer": "Number of seconds before an idle UDP/UDP-Lite connection times out (0 - 86400 sec, 0 = default).",
    "session-ttl": "Session TTL (300 - 2764800, 0 = default).",
    "check-reset-range": "Configure the type of ICMP error message verification.",
    "comment": "Comment.",
    "color": "Color of icon on the GUI.",
    "app-service-type": "Application service type.",
    "app-category": "Application category ID.",
    "application": "Application ID.",
    "fabric-object": "Security Fabric global object setting.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 79},
    "category": {"type": "string", "max_length": 63},
    "fqdn": {"type": "string", "max_length": 255},
    "protocol-number": {"type": "integer", "min": 0, "max": 254},
    "icmptype": {"type": "integer", "min": 0, "max": 4294967295},
    "icmpcode": {"type": "integer", "min": 0, "max": 255},
    "tcp-halfclose-timer": {"type": "integer", "min": 0, "max": 86400},
    "tcp-halfopen-timer": {"type": "integer", "min": 0, "max": 86400},
    "tcp-timewait-timer": {"type": "integer", "min": 0, "max": 300},
    "tcp-rst-timer": {"type": "integer", "min": 5, "max": 300},
    "udp-idle-timer": {"type": "integer", "min": 0, "max": 86400},
    "color": {"type": "integer", "min": 0, "max": 32},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "app-category": {
        "id": {
            "type": "integer",
            "help": "Application category id.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
    },
    "application": {
        "id": {
            "type": "integer",
            "help": "Application id.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_PROXY = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_PROTOCOL = [
    "TCP/UDP/UDP-Lite/SCTP",  # TCP, UDP, UDP-Lite and SCTP.
    "ICMP",  # ICMP.
    "ICMP6",  # ICMP6.
    "IP",  # IP.
    "HTTP",  # HTTP - for web proxy.
    "FTP",  # FTP - for web proxy.
    "CONNECT",  # Connect - for web proxy.
    "SOCKS-TCP",  # Socks TCP - for web proxy.
    "SOCKS-UDP",  # Socks UDP - for web proxy.
    "ALL",  # All - for web proxy.
]
VALID_BODY_HELPER = [
    "auto",  # Automatically select helper based on protocol and port.
    "disable",  # Disable helper.
    "ftp",  # FTP.
    "tftp",  # TFTP.
    "ras",  # RAS.
    "h323",  # H323.
    "tns",  # TNS.
    "mms",  # MMS.
    "sip",  # SIP.
    "pptp",  # PPTP.
    "rtsp",  # RTSP.
    "dns-udp",  # DNS UDP.
    "dns-tcp",  # DNS TCP.
    "pmap",  # PMAP.
    "rsh",  # RSH.
    "dcerpc",  # DCERPC.
    "mgcp",  # MGCP.
]
VALID_BODY_CHECK_RESET_RANGE = [
    "disable",  # Disable RST range check.
    "strict",  # Check RST range strictly.
    "default",  # Using system default setting.
]
VALID_BODY_APP_SERVICE_TYPE = [
    "disable",  # Disable application type.
    "app-id",  # Application ID.
    "app-category",  # Applicatin category.
]
VALID_BODY_FABRIC_OBJECT = [
    "enable",  # Object is set as a security fabric-wide global object.
    "disable",  # Object is local to this security fabric member.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_firewall_service_custom_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for firewall/service/custom."""
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
    """Validate required fields for firewall/service/custom."""
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


def validate_firewall_service_custom_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new firewall/service/custom object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "proxy" in payload:
        value = payload["proxy"]
        if value not in VALID_BODY_PROXY:
            desc = FIELD_DESCRIPTIONS.get("proxy", "")
            error_msg = f"Invalid value for 'proxy': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PROXY)}"
            error_msg += f"\n  → Example: proxy='{{ VALID_BODY_PROXY[0] }}'"
            return (False, error_msg)
    if "protocol" in payload:
        value = payload["protocol"]
        if value not in VALID_BODY_PROTOCOL:
            desc = FIELD_DESCRIPTIONS.get("protocol", "")
            error_msg = f"Invalid value for 'protocol': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PROTOCOL)}"
            error_msg += f"\n  → Example: protocol='{{ VALID_BODY_PROTOCOL[0] }}'"
            return (False, error_msg)
    if "helper" in payload:
        value = payload["helper"]
        if value not in VALID_BODY_HELPER:
            desc = FIELD_DESCRIPTIONS.get("helper", "")
            error_msg = f"Invalid value for 'helper': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_HELPER)}"
            error_msg += f"\n  → Example: helper='{{ VALID_BODY_HELPER[0] }}'"
            return (False, error_msg)
    if "check-reset-range" in payload:
        value = payload["check-reset-range"]
        if value not in VALID_BODY_CHECK_RESET_RANGE:
            desc = FIELD_DESCRIPTIONS.get("check-reset-range", "")
            error_msg = f"Invalid value for 'check-reset-range': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CHECK_RESET_RANGE)}"
            error_msg += f"\n  → Example: check-reset-range='{{ VALID_BODY_CHECK_RESET_RANGE[0] }}'"
            return (False, error_msg)
    if "app-service-type" in payload:
        value = payload["app-service-type"]
        if value not in VALID_BODY_APP_SERVICE_TYPE:
            desc = FIELD_DESCRIPTIONS.get("app-service-type", "")
            error_msg = f"Invalid value for 'app-service-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_APP_SERVICE_TYPE)}"
            error_msg += f"\n  → Example: app-service-type='{{ VALID_BODY_APP_SERVICE_TYPE[0] }}'"
            return (False, error_msg)
    if "fabric-object" in payload:
        value = payload["fabric-object"]
        if value not in VALID_BODY_FABRIC_OBJECT:
            desc = FIELD_DESCRIPTIONS.get("fabric-object", "")
            error_msg = f"Invalid value for 'fabric-object': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FABRIC_OBJECT)}"
            error_msg += f"\n  → Example: fabric-object='{{ VALID_BODY_FABRIC_OBJECT[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_firewall_service_custom_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update firewall/service/custom."""
    # Step 1: Validate enum values
    if "proxy" in payload:
        value = payload["proxy"]
        if value not in VALID_BODY_PROXY:
            return (
                False,
                f"Invalid value for 'proxy'='{value}'. Must be one of: {', '.join(VALID_BODY_PROXY)}",
            )
    if "protocol" in payload:
        value = payload["protocol"]
        if value not in VALID_BODY_PROTOCOL:
            return (
                False,
                f"Invalid value for 'protocol'='{value}'. Must be one of: {', '.join(VALID_BODY_PROTOCOL)}",
            )
    if "helper" in payload:
        value = payload["helper"]
        if value not in VALID_BODY_HELPER:
            return (
                False,
                f"Invalid value for 'helper'='{value}'. Must be one of: {', '.join(VALID_BODY_HELPER)}",
            )
    if "check-reset-range" in payload:
        value = payload["check-reset-range"]
        if value not in VALID_BODY_CHECK_RESET_RANGE:
            return (
                False,
                f"Invalid value for 'check-reset-range'='{value}'. Must be one of: {', '.join(VALID_BODY_CHECK_RESET_RANGE)}",
            )
    if "app-service-type" in payload:
        value = payload["app-service-type"]
        if value not in VALID_BODY_APP_SERVICE_TYPE:
            return (
                False,
                f"Invalid value for 'app-service-type'='{value}'. Must be one of: {', '.join(VALID_BODY_APP_SERVICE_TYPE)}",
            )
    if "fabric-object" in payload:
        value = payload["fabric-object"]
        if value not in VALID_BODY_FABRIC_OBJECT:
            return (
                False,
                f"Invalid value for 'fabric-object'='{value}'. Must be one of: {', '.join(VALID_BODY_FABRIC_OBJECT)}",
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
    "endpoint": "firewall/service/custom",
    "category": "cmdb",
    "api_path": "firewall.service/custom",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure custom services.",
    "total_fields": 28,
    "required_fields_count": 0,
    "fields_with_defaults_count": 25,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
