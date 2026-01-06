"""
Validation helpers for firewall/service/custom endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification
Customize as needed for endpoint-specific business logic.
"""

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
#
# 1. FALSE POSITIVES: Some fields marked "required" have default values,
#    meaning they're optional (filtered out by generator)
#
# 2. CONDITIONAL REQUIREMENTS: Many endpoints require EITHER field A OR field B:
#    - firewall.policy: requires (srcaddr + dstaddr) OR (srcaddr6 + dstaddr6)
#    - These conditional requirements cannot be expressed in a simple list
#
# 3. SPECIALIZED FEATURES: Fields for WAN optimization, VPN, NAT64, etc.
#    are marked "required" but only apply when using those features
#
# The REQUIRED_FIELDS list below is INFORMATIONAL ONLY and shows fields that:
# - Are marked required in the schema
# - Don't have non-empty default values
# - Aren't specialized feature fields
#
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
    """
    Validate GET request parameters for firewall/service/custom.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_firewall_service_custom_get()
        >>> assert is_valid == True
        
        >>> # Valid - Get specific item by name
        >>> is_valid, error = validate_firewall_service_custom_get(name="test-item")
        >>> assert is_valid == True
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_firewall_service_custom_get(
        ...     filters={"format": "name|type"}
        ... )
        >>> assert is_valid == True
    """
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
    """
    Validate required fields for firewall/service/custom.

    This validator checks:
    1. Always-required fields are present
    2. Mutually exclusive groups have at least one field

    Args:
        payload: The request payload to validate

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "test"}
        >>> is_valid, error = validate_required_fields(payload)
    """
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
    """
    Validate POST request to create new firewall/service/custom object.

    This validator performs two-stage validation:
    1. Required fields check (schema-based)
    2. Field value validation (enums, ranges, formats)

    Args:
        payload: Request body data with configuration
        **params: Query parameters (vdom, etc.)

    Returns:
        Tuple of (is_valid, error_message)
        - is_valid: True if payload is valid, False otherwise
        - error_message: None if valid, detailed error string if invalid

    Examples:
        >>> # ✅ Valid - Minimal required fields
        >>> payload = {
        ... }
        >>> is_valid, error = validate_firewall_service_custom_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "proxy": "{'name': 'enable', 'help': 'Enable setting.', 'label': 'Enable', 'description': 'Enable setting'}",  # Valid enum value
        ... }
        >>> is_valid, error = validate_firewall_service_custom_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["proxy"] = "invalid-value"
        >>> is_valid, error = validate_firewall_service_custom_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_firewall_service_custom_post(payload)
        >>> assert is_valid == False
        >>> assert "Missing required field" in error
    """
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
    """
    Validate PUT request to update firewall/service/custom.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_firewall_service_custom_put(payload)
    """
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
# Provide programmatic access to field metadata for IDE autocomplete,
# documentation generation, and dynamic validation
# ============================================================================


def get_field_description(field_name: str) -> str | None:
    """
    Get description/help text for a field.

    Args:
        field_name: Name of the field

    Returns:
        Description text or None if field doesn't exist

    Example:
        >>> desc = get_field_description("name")
        >>> print(desc)
    """
    return FIELD_DESCRIPTIONS.get(field_name)


def get_field_type(field_name: str) -> str | None:
    """
    Get the type of a field.

    Args:
        field_name: Name of the field

    Returns:
        Field type (e.g., "string", "integer", "option") or None

    Example:
        >>> field_type = get_field_type("status")
        >>> print(field_type)  # "option"
    """
    return FIELD_TYPES.get(field_name)


def get_field_constraints(field_name: str) -> dict[str, Any] | None:
    """
    Get constraints for a field (min/max values, string length).

    Args:
        field_name: Name of the field

    Returns:
        Constraint dict or None

    Example:
        >>> constraints = get_field_constraints("port")
        >>> print(constraints)  # {"type": "integer", "min": 1, "max": 65535}
    """
    return FIELD_CONSTRAINTS.get(field_name)


def get_field_default(field_name: str) -> Any | None:
    """
    Get default value for a field.

    Args:
        field_name: Name of the field

    Returns:
        Default value or None if no default

    Example:
        >>> default = get_field_default("status")
        >>> print(default)  # "enable"
    """
    return FIELDS_WITH_DEFAULTS.get(field_name)


def get_field_options(field_name: str) -> list[str] | None:
    """
    Get valid enum options for a field.

    Args:
        field_name: Name of the field

    Returns:
        List of valid values or None if not an enum field

    Example:
        >>> options = get_field_options("status")
        >>> print(options)  # ["enable", "disable"]
    """
    # Construct the constant name from field name
    # Replace all non-alphanumeric characters with underscores for valid Python identifiers
    import re
    safe_name = re.sub(r'[^a-zA-Z0-9]', '_', field_name)
    constant_name = f"VALID_BODY_{safe_name.upper()}"
    return globals().get(constant_name)


def get_nested_schema(field_name: str) -> dict[str, Any] | None:
    """
    Get schema for nested table/list fields.

    Args:
        field_name: Name of the parent field

    Returns:
        Dict mapping child field names to their metadata

    Example:
        >>> nested = get_nested_schema("members")
        >>> if nested:
        ...     for child_field, child_meta in nested.items():
        ...         print(f"{child_field}: {child_meta['type']}")
    """
    return NESTED_SCHEMAS.get(field_name)


def get_all_fields() -> list[str]:
    """
    Get list of all field names.

    Returns:
        List of all field names in the schema

    Example:
        >>> fields = get_all_fields()
        >>> print(len(fields))
    """
    return list(FIELD_TYPES.keys())


def get_field_metadata(field_name: str) -> dict[str, Any] | None:
    """
    Get complete metadata for a field (type, description, constraints, defaults, options).

    Args:
        field_name: Name of the field

    Returns:
        Dict with all available metadata or None if field doesn't exist

    Example:
        >>> meta = get_field_metadata("status")
        >>> print(meta)
        >>> # {
        >>> #   "type": "option",
        >>> #   "description": "Enable/disable this feature",
        >>> #   "default": "enable",
        >>> #   "options": ["enable", "disable"]
        >>> # }
    """
    if field_name not in FIELD_TYPES:
        return None

    metadata = {
        "name": field_name,
        "type": FIELD_TYPES[field_name],
    }

    # Add description if available
    if field_name in FIELD_DESCRIPTIONS:
        metadata["description"] = FIELD_DESCRIPTIONS[field_name]

    # Add constraints if available
    if field_name in FIELD_CONSTRAINTS:
        metadata["constraints"] = FIELD_CONSTRAINTS[field_name]

    # Add default if available
    if field_name in FIELDS_WITH_DEFAULTS:
        metadata["default"] = FIELDS_WITH_DEFAULTS[field_name]

    # Add required flag
    metadata["required"] = field_name in REQUIRED_FIELDS

    # Add options if available
    options = get_field_options(field_name)
    if options:
        metadata["options"] = options

    # Add nested schema if available
    nested = get_nested_schema(field_name)
    if nested:
        metadata["nested_schema"] = nested

    return metadata


def validate_field_value(field_name: str, value: Any) -> tuple[bool, str | None]:
    """
    Validate a single field value against its constraints.

    Args:
        field_name: Name of the field
        value: Value to validate

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> is_valid, error = validate_field_value("status", "enable")
        >>> if not is_valid:
        ...     print(error)
    """
    # Get field metadata
    field_type = get_field_type(field_name)
    if field_type is None:
        return (False, f"Unknown field: '{field_name}' (not defined in schema)")

    # Get field description for better error context
    description = get_field_description(field_name)

    # Validate enum values
    options = get_field_options(field_name)
    if options and value not in options:
        error_msg = f"Invalid value for '{field_name}': {repr(value)}"
        if description:
            error_msg += f"\n  → Description: {description}"
        error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in options)}"
        if options:
            error_msg += f"\n  → Example: {field_name}={repr(options[0])}"
        return (False, error_msg)

    # Validate constraints
    constraints = get_field_constraints(field_name)
    if constraints:
        constraint_type = constraints.get("type")

        if constraint_type == "integer":
            if not isinstance(value, int):
                error_msg = f"Field '{field_name}' must be an integer"
                if description:
                    error_msg += f"\n  → Description: {description}"
                error_msg += f"\n  → You provided: {type(value).__name__} = {repr(value)}"
                return (False, error_msg)

            min_val = constraints.get("min")
            max_val = constraints.get("max")

            if min_val is not None and value < min_val:
                error_msg = f"Field '{field_name}' value {value} is below minimum {min_val}"
                if description:
                    error_msg += f"\n  → Description: {description}"
                if max_val is not None:
                    error_msg += f"\n  → Valid range: {min_val} to {max_val}"
                return (False, error_msg)

            if max_val is not None and value > max_val:
                error_msg = f"Field '{field_name}' value {value} exceeds maximum {max_val}"
                if description:
                    error_msg += f"\n  → Description: {description}"
                if min_val is not None:
                    error_msg += f"\n  → Valid range: {min_val} to {max_val}"
                return (False, error_msg)

        elif constraint_type == "string":
            if not isinstance(value, str):
                error_msg = f"Field '{field_name}' must be a string"
                if description:
                    error_msg += f"\n  → Description: {description}"
                error_msg += f"\n  → You provided: {type(value).__name__} = {repr(value)}"
                return (False, error_msg)

            max_length = constraints.get("max_length")
            if max_length and len(value) > max_length:
                error_msg = f"Field '{field_name}' length {len(value)} exceeds maximum {max_length}"
                if description:
                    error_msg += f"\n  → Description: {description}"
                error_msg += f"\n  → Your value: {repr(value[:50])}{'...' if len(value) > 50 else ''}"
                return (False, error_msg)

    return (True, None)


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
    """
    Get information about this endpoint schema.

    Returns:
        Dict with schema metadata

    Example:
        >>> info = get_schema_info()
        >>> print(f"Endpoint: {info['endpoint']}")
        >>> print(f"Total fields: {info['total_fields']}")
    """
    return SCHEMA_INFO.copy()
