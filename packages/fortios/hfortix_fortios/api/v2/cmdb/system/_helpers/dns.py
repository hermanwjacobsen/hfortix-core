"""
Validation helpers for system/dns endpoint.

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
    "interface",  # Specify outgoing interface to reach server.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "primary": "0.0.0.0",
    "secondary": "0.0.0.0",
    "protocol": "cleartext",
    "ssl-certificate": "Fortinet_Factory",
    "ip6-primary": "::",
    "ip6-secondary": "::",
    "timeout": 5,
    "retry": 2,
    "dns-cache-limit": 5000,
    "dns-cache-ttl": 1800,
    "cache-notfound-responses": "disable",
    "source-ip": "0.0.0.0",
    "source-ip-interface": "",
    "root-servers": "",
    "interface-select-method": "auto",
    "interface": "",
    "vrf-select": 0,
    "server-select-method": "least-rtt",
    "alt-primary": "0.0.0.0",
    "alt-secondary": "0.0.0.0",
    "log": "disable",
    "fqdn-cache-ttl": 0,
    "fqdn-max-refresh": 3600,
    "fqdn-min-refresh": 60,
    "hostname-ttl": 86400,
    "hostname-limit": 5000,
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
    "primary": "ipv4-address",  # Primary DNS server IP address.
    "secondary": "ipv4-address",  # Secondary DNS server IP address.
    "protocol": "option",  # DNS transport protocols.
    "ssl-certificate": "string",  # Name of local certificate for SSL connections.
    "server-hostname": "string",  # DNS server host name list.
    "domain": "string",  # Search suffix list for hostname lookup.
    "ip6-primary": "ipv6-address",  # Primary DNS server IPv6 address.
    "ip6-secondary": "ipv6-address",  # Secondary DNS server IPv6 address.
    "timeout": "integer",  # DNS query timeout interval in seconds (1 - 10).
    "retry": "integer",  # Number of times to retry (0 - 5).
    "dns-cache-limit": "integer",  # Maximum number of records in the DNS cache.
    "dns-cache-ttl": "integer",  # Duration in seconds that the DNS cache retains information.
    "cache-notfound-responses": "option",  # Enable/disable response from the DNS server when a record is
    "source-ip": "ipv4-address",  # IP address used by the DNS server as its source IP.
    "source-ip-interface": "string",  # IP address of the specified interface as the source IP addre
    "root-servers": "user",  # Configure up to two preferred servers that serve the DNS roo
    "interface-select-method": "option",  # Specify how to select outgoing interface to reach server.
    "interface": "string",  # Specify outgoing interface to reach server.
    "vrf-select": "integer",  # VRF ID used for connection to server.
    "server-select-method": "option",  # Specify how configured servers are prioritized.
    "alt-primary": "ipv4-address",  # Alternate primary DNS server. This is not used as a failover
    "alt-secondary": "ipv4-address",  # Alternate secondary DNS server. This is not used as a failov
    "log": "option",  # Local DNS log setting.
    "fqdn-cache-ttl": "integer",  # FQDN cache time to live in seconds (0 - 86400, default = 0).
    "fqdn-max-refresh": "integer",  # FQDN cache maximum refresh time in seconds (3600 - 86400, de
    "fqdn-min-refresh": "integer",  # FQDN cache minimum refresh time in seconds (10 - 3600, defau
    "hostname-ttl": "integer",  # TTL of hostname table entries (60 - 86400).
    "hostname-limit": "integer",  # Limit of the number of hostname table entries (0 - 50000).
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "primary": "Primary DNS server IP address.",
    "secondary": "Secondary DNS server IP address.",
    "protocol": "DNS transport protocols.",
    "ssl-certificate": "Name of local certificate for SSL connections.",
    "server-hostname": "DNS server host name list.",
    "domain": "Search suffix list for hostname lookup.",
    "ip6-primary": "Primary DNS server IPv6 address.",
    "ip6-secondary": "Secondary DNS server IPv6 address.",
    "timeout": "DNS query timeout interval in seconds (1 - 10).",
    "retry": "Number of times to retry (0 - 5).",
    "dns-cache-limit": "Maximum number of records in the DNS cache.",
    "dns-cache-ttl": "Duration in seconds that the DNS cache retains information.",
    "cache-notfound-responses": "Enable/disable response from the DNS server when a record is not in cache.",
    "source-ip": "IP address used by the DNS server as its source IP.",
    "source-ip-interface": "IP address of the specified interface as the source IP address.",
    "root-servers": "Configure up to two preferred servers that serve the DNS root zone (default uses all 13 root servers).",
    "interface-select-method": "Specify how to select outgoing interface to reach server.",
    "interface": "Specify outgoing interface to reach server.",
    "vrf-select": "VRF ID used for connection to server.",
    "server-select-method": "Specify how configured servers are prioritized.",
    "alt-primary": "Alternate primary DNS server. This is not used as a failover DNS server.",
    "alt-secondary": "Alternate secondary DNS server. This is not used as a failover DNS server.",
    "log": "Local DNS log setting.",
    "fqdn-cache-ttl": "FQDN cache time to live in seconds (0 - 86400, default = 0).",
    "fqdn-max-refresh": "FQDN cache maximum refresh time in seconds (3600 - 86400, default = 3600).",
    "fqdn-min-refresh": "FQDN cache minimum refresh time in seconds (10 - 3600, default = 60).",
    "hostname-ttl": "TTL of hostname table entries (60 - 86400).",
    "hostname-limit": "Limit of the number of hostname table entries (0 - 50000).",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "ssl-certificate": {"type": "string", "max_length": 35},
    "timeout": {"type": "integer", "min": 1, "max": 10},
    "retry": {"type": "integer", "min": 0, "max": 5},
    "dns-cache-limit": {"type": "integer", "min": 0, "max": 4294967295},
    "dns-cache-ttl": {"type": "integer", "min": 60, "max": 86400},
    "source-ip-interface": {"type": "string", "max_length": 15},
    "interface": {"type": "string", "max_length": 15},
    "vrf-select": {"type": "integer", "min": 0, "max": 511},
    "fqdn-cache-ttl": {"type": "integer", "min": 0, "max": 86400},
    "fqdn-max-refresh": {"type": "integer", "min": 3600, "max": 86400},
    "fqdn-min-refresh": {"type": "integer", "min": 10, "max": 3600},
    "hostname-ttl": {"type": "integer", "min": 60, "max": 86400},
    "hostname-limit": {"type": "integer", "min": 0, "max": 50000},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "server-hostname": {
        "hostname": {
            "type": "string",
            "help": "DNS server host name list separated by space (maximum 4 domains).",
            "required": True,
            "default": "",
            "max_length": 127,
        },
    },
    "domain": {
        "domain": {
            "type": "string",
            "help": "DNS search domain list separated by space (maximum 8 domains).",
            "required": True,
            "default": "",
            "max_length": 127,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_PROTOCOL = [
    "cleartext",
    "dot",
    "doh",
]
VALID_BODY_CACHE_NOTFOUND_RESPONSES = [
    "disable",
    "enable",
]
VALID_BODY_INTERFACE_SELECT_METHOD = [
    "auto",
    "sdwan",
    "specify",
]
VALID_BODY_SERVER_SELECT_METHOD = [
    "least-rtt",
    "failover",
]
VALID_BODY_LOG = [
    "disable",
    "error",
    "all",
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_system_dns_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters for system/dns.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_system_dns_get()
        >>> assert is_valid == True
        
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_system_dns_get(
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
    Validate required fields for system/dns.

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


def validate_system_dns_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new system/dns object.

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
        ...     "interface": True,  # Specify outgoing interface to reach server.
        ... }
        >>> is_valid, error = validate_system_dns_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "interface": True,
        ...     "protocol": "cleartext",  # Valid enum value
        ... }
        >>> is_valid, error = validate_system_dns_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["protocol"] = "invalid-value"
        >>> is_valid, error = validate_system_dns_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_system_dns_post(payload)
        >>> assert is_valid == False
        >>> assert "Missing required field" in error
    """
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
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
    if "cache-notfound-responses" in payload:
        value = payload["cache-notfound-responses"]
        if value not in VALID_BODY_CACHE_NOTFOUND_RESPONSES:
            desc = FIELD_DESCRIPTIONS.get("cache-notfound-responses", "")
            error_msg = f"Invalid value for 'cache-notfound-responses': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CACHE_NOTFOUND_RESPONSES)}"
            error_msg += f"\n  → Example: cache-notfound-responses='{{ VALID_BODY_CACHE_NOTFOUND_RESPONSES[0] }}'"
            return (False, error_msg)
    if "interface-select-method" in payload:
        value = payload["interface-select-method"]
        if value not in VALID_BODY_INTERFACE_SELECT_METHOD:
            desc = FIELD_DESCRIPTIONS.get("interface-select-method", "")
            error_msg = f"Invalid value for 'interface-select-method': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_INTERFACE_SELECT_METHOD)}"
            error_msg += f"\n  → Example: interface-select-method='{{ VALID_BODY_INTERFACE_SELECT_METHOD[0] }}'"
            return (False, error_msg)
    if "server-select-method" in payload:
        value = payload["server-select-method"]
        if value not in VALID_BODY_SERVER_SELECT_METHOD:
            desc = FIELD_DESCRIPTIONS.get("server-select-method", "")
            error_msg = f"Invalid value for 'server-select-method': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SERVER_SELECT_METHOD)}"
            error_msg += f"\n  → Example: server-select-method='{{ VALID_BODY_SERVER_SELECT_METHOD[0] }}'"
            return (False, error_msg)
    if "log" in payload:
        value = payload["log"]
        if value not in VALID_BODY_LOG:
            desc = FIELD_DESCRIPTIONS.get("log", "")
            error_msg = f"Invalid value for 'log': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LOG)}"
            error_msg += f"\n  → Example: log='{{ VALID_BODY_LOG[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_system_dns_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update system/dns.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_system_dns_put(payload)
    """
    # Step 1: Validate enum values
    if "protocol" in payload:
        value = payload["protocol"]
        if value not in VALID_BODY_PROTOCOL:
            return (
                False,
                f"Invalid value for 'protocol'='{value}'. Must be one of: {', '.join(VALID_BODY_PROTOCOL)}",
            )
    if "cache-notfound-responses" in payload:
        value = payload["cache-notfound-responses"]
        if value not in VALID_BODY_CACHE_NOTFOUND_RESPONSES:
            return (
                False,
                f"Invalid value for 'cache-notfound-responses'='{value}'. Must be one of: {', '.join(VALID_BODY_CACHE_NOTFOUND_RESPONSES)}",
            )
    if "interface-select-method" in payload:
        value = payload["interface-select-method"]
        if value not in VALID_BODY_INTERFACE_SELECT_METHOD:
            return (
                False,
                f"Invalid value for 'interface-select-method'='{value}'. Must be one of: {', '.join(VALID_BODY_INTERFACE_SELECT_METHOD)}",
            )
    if "server-select-method" in payload:
        value = payload["server-select-method"]
        if value not in VALID_BODY_SERVER_SELECT_METHOD:
            return (
                False,
                f"Invalid value for 'server-select-method'='{value}'. Must be one of: {', '.join(VALID_BODY_SERVER_SELECT_METHOD)}",
            )
    if "log" in payload:
        value = payload["log"]
        if value not in VALID_BODY_LOG:
            return (
                False,
                f"Invalid value for 'log'='{value}'. Must be one of: {', '.join(VALID_BODY_LOG)}",
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
    constant_name = f"VALID_BODY_{field_name.replace('-', '_').upper()}"
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
    "endpoint": "system/dns",
    "category": "cmdb",
    "api_path": "system/dns",
    "help": "Configure DNS.",
    "total_fields": 28,
    "required_fields_count": 1,
    "fields_with_defaults_count": 26,
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
