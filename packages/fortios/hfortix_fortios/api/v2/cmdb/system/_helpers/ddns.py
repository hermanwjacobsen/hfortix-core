"""
Validation helpers for system/ddns endpoint.

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
    "ddns-server",  # Select a DDNS service provider.
    "monitor-interface",  # Monitored interface.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "ddnsid": 0,
    "ddns-server": "",
    "addr-type": "ipv4",
    "server-type": "ipv4",
    "ddns-zone": "",
    "ddns-ttl": 300,
    "ddns-auth": "disable",
    "ddns-keyname": "",
    "ddns-domain": "",
    "ddns-username": "",
    "ddns-sn": "",
    "use-public-ip": "disable",
    "update-interval": 0,
    "clear-text": "disable",
    "ssl-certificate": "Fortinet_Factory",
    "bound-ip": "",
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
    "ddnsid": "integer",  # DDNS ID.
    "ddns-server": "option",  # Select a DDNS service provider.
    "addr-type": "option",  # Address type of interface address in DDNS update.
    "server-type": "option",  # Address type of the DDNS server.
    "ddns-server-addr": "string",  # Generic DDNS server IP/FQDN list.
    "ddns-zone": "string",  # Zone of your domain name (for example, DDNS.com).
    "ddns-ttl": "integer",  # Time-to-live for DDNS packets.
    "ddns-auth": "option",  # Enable/disable TSIG authentication for your DDNS server.
    "ddns-keyname": "string",  # DDNS update key name.
    "ddns-key": "password_aes256",  # DDNS update key (base 64 encoding).
    "ddns-domain": "string",  # Your fully qualified domain name. For example, yourname.ddns
    "ddns-username": "string",  # DDNS user name.
    "ddns-sn": "string",  # DDNS Serial Number.
    "ddns-password": "password",  # DDNS password.
    "use-public-ip": "option",  # Enable/disable use of public IP address.
    "update-interval": "integer",  # DDNS update interval (60 - 2592000 sec, 0 means default).
    "clear-text": "option",  # Enable/disable use of clear text connections.
    "ssl-certificate": "string",  # Name of local certificate for SSL connections.
    "bound-ip": "string",  # Bound IP address.
    "monitor-interface": "string",  # Monitored interface.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "ddnsid": "DDNS ID.",
    "ddns-server": "Select a DDNS service provider.",
    "addr-type": "Address type of interface address in DDNS update.",
    "server-type": "Address type of the DDNS server.",
    "ddns-server-addr": "Generic DDNS server IP/FQDN list.",
    "ddns-zone": "Zone of your domain name (for example, DDNS.com).",
    "ddns-ttl": "Time-to-live for DDNS packets.",
    "ddns-auth": "Enable/disable TSIG authentication for your DDNS server.",
    "ddns-keyname": "DDNS update key name.",
    "ddns-key": "DDNS update key (base 64 encoding).",
    "ddns-domain": "Your fully qualified domain name. For example, yourname.ddns.com.",
    "ddns-username": "DDNS user name.",
    "ddns-sn": "DDNS Serial Number.",
    "ddns-password": "DDNS password.",
    "use-public-ip": "Enable/disable use of public IP address.",
    "update-interval": "DDNS update interval (60 - 2592000 sec, 0 means default).",
    "clear-text": "Enable/disable use of clear text connections.",
    "ssl-certificate": "Name of local certificate for SSL connections.",
    "bound-ip": "Bound IP address.",
    "monitor-interface": "Monitored interface.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "ddnsid": {"type": "integer", "min": 0, "max": 4294967295},
    "ddns-zone": {"type": "string", "max_length": 64},
    "ddns-ttl": {"type": "integer", "min": 60, "max": 86400},
    "ddns-keyname": {"type": "string", "max_length": 64},
    "ddns-domain": {"type": "string", "max_length": 64},
    "ddns-username": {"type": "string", "max_length": 64},
    "ddns-sn": {"type": "string", "max_length": 64},
    "update-interval": {"type": "integer", "min": 60, "max": 2592000},
    "ssl-certificate": {"type": "string", "max_length": 35},
    "bound-ip": {"type": "string", "max_length": 46},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "ddns-server-addr": {
        "addr": {
            "type": "string",
            "help": "IP address or FQDN of the server.",
            "required": True,
            "default": "",
            "max_length": 256,
        },
    },
    "monitor-interface": {
        "interface-name": {
            "type": "string",
            "help": "Interface name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_DDNS_SERVER = [
    "dyndns.org",  # members.dyndns.org and dnsalias.com
    "dyns.net",  # www.dyns.net
    "tzo.com",  # rh.tzo.com
    "vavic.com",  # Peanut Hull
    "dipdns.net",  # dipdnsserver.dipdns.com
    "now.net.cn",  # ip.todayisp.com
    "dhs.org",  # members.dhs.org
    "easydns.com",  # members.easydns.com
    "genericDDNS",  # Generic DDNS based on RFC2136.
    "FortiGuardDDNS",  # FortiGuard DDNS service.
    "noip.com",  # dynupdate.no-ip.com
]
VALID_BODY_ADDR_TYPE = [
    "ipv4",  # Use IPv4 address of the interface.
    "ipv6",  # Use IPv6 address of the interface.
]
VALID_BODY_SERVER_TYPE = [
    "ipv4",  # Use IPv4 addressing.
    "ipv6",  # Use IPv6 addressing.
]
VALID_BODY_DDNS_AUTH = [
    "disable",  # Disable DDNS authentication.
    "tsig",  # Enable TSIG authentication based on RFC2845.
]
VALID_BODY_USE_PUBLIC_IP = [
    "disable",  # Disable use of public IP address.
    "enable",  # Enable use of public IP address.
]
VALID_BODY_CLEAR_TEXT = [
    "disable",  # Disable use of clear text connections.
    "enable",  # Enable use of clear text connections.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_system_ddns_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters for system/ddns.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_system_ddns_get()
        >>> assert is_valid == True
        
        >>> # Valid - Get specific item by ddnsid
        >>> is_valid, error = validate_system_ddns_get(ddnsid="test-item")
        >>> assert is_valid == True
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_system_ddns_get(
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
    Validate required fields for system/ddns.

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


def validate_system_ddns_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new system/ddns object.

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
        ...     "ddns-server": True,  # Select a DDNS service provider.
        ...     "monitor-interface": True,  # Monitored interface.
        ... }
        >>> is_valid, error = validate_system_ddns_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "ddns-server": True,
        ...     "ddns-server": "{'name': 'dyndns.org', 'help': 'members.dyndns.org and dnsalias.com', 'label': 'Dyndns.Org'}",  # Valid enum value
        ... }
        >>> is_valid, error = validate_system_ddns_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["ddns-server"] = "invalid-value"
        >>> is_valid, error = validate_system_ddns_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_system_ddns_post(payload)
        >>> assert is_valid == False
        >>> assert "Missing required field" in error
    """
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "ddns-server" in payload:
        value = payload["ddns-server"]
        if value not in VALID_BODY_DDNS_SERVER:
            desc = FIELD_DESCRIPTIONS.get("ddns-server", "")
            error_msg = f"Invalid value for 'ddns-server': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DDNS_SERVER)}"
            error_msg += f"\n  → Example: ddns-server='{{ VALID_BODY_DDNS_SERVER[0] }}'"
            return (False, error_msg)
    if "addr-type" in payload:
        value = payload["addr-type"]
        if value not in VALID_BODY_ADDR_TYPE:
            desc = FIELD_DESCRIPTIONS.get("addr-type", "")
            error_msg = f"Invalid value for 'addr-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ADDR_TYPE)}"
            error_msg += f"\n  → Example: addr-type='{{ VALID_BODY_ADDR_TYPE[0] }}'"
            return (False, error_msg)
    if "server-type" in payload:
        value = payload["server-type"]
        if value not in VALID_BODY_SERVER_TYPE:
            desc = FIELD_DESCRIPTIONS.get("server-type", "")
            error_msg = f"Invalid value for 'server-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SERVER_TYPE)}"
            error_msg += f"\n  → Example: server-type='{{ VALID_BODY_SERVER_TYPE[0] }}'"
            return (False, error_msg)
    if "ddns-auth" in payload:
        value = payload["ddns-auth"]
        if value not in VALID_BODY_DDNS_AUTH:
            desc = FIELD_DESCRIPTIONS.get("ddns-auth", "")
            error_msg = f"Invalid value for 'ddns-auth': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DDNS_AUTH)}"
            error_msg += f"\n  → Example: ddns-auth='{{ VALID_BODY_DDNS_AUTH[0] }}'"
            return (False, error_msg)
    if "use-public-ip" in payload:
        value = payload["use-public-ip"]
        if value not in VALID_BODY_USE_PUBLIC_IP:
            desc = FIELD_DESCRIPTIONS.get("use-public-ip", "")
            error_msg = f"Invalid value for 'use-public-ip': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_USE_PUBLIC_IP)}"
            error_msg += f"\n  → Example: use-public-ip='{{ VALID_BODY_USE_PUBLIC_IP[0] }}'"
            return (False, error_msg)
    if "clear-text" in payload:
        value = payload["clear-text"]
        if value not in VALID_BODY_CLEAR_TEXT:
            desc = FIELD_DESCRIPTIONS.get("clear-text", "")
            error_msg = f"Invalid value for 'clear-text': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CLEAR_TEXT)}"
            error_msg += f"\n  → Example: clear-text='{{ VALID_BODY_CLEAR_TEXT[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_system_ddns_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update system/ddns.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_system_ddns_put(payload)
    """
    # Step 1: Validate enum values
    if "ddns-server" in payload:
        value = payload["ddns-server"]
        if value not in VALID_BODY_DDNS_SERVER:
            return (
                False,
                f"Invalid value for 'ddns-server'='{value}'. Must be one of: {', '.join(VALID_BODY_DDNS_SERVER)}",
            )
    if "addr-type" in payload:
        value = payload["addr-type"]
        if value not in VALID_BODY_ADDR_TYPE:
            return (
                False,
                f"Invalid value for 'addr-type'='{value}'. Must be one of: {', '.join(VALID_BODY_ADDR_TYPE)}",
            )
    if "server-type" in payload:
        value = payload["server-type"]
        if value not in VALID_BODY_SERVER_TYPE:
            return (
                False,
                f"Invalid value for 'server-type'='{value}'. Must be one of: {', '.join(VALID_BODY_SERVER_TYPE)}",
            )
    if "ddns-auth" in payload:
        value = payload["ddns-auth"]
        if value not in VALID_BODY_DDNS_AUTH:
            return (
                False,
                f"Invalid value for 'ddns-auth'='{value}'. Must be one of: {', '.join(VALID_BODY_DDNS_AUTH)}",
            )
    if "use-public-ip" in payload:
        value = payload["use-public-ip"]
        if value not in VALID_BODY_USE_PUBLIC_IP:
            return (
                False,
                f"Invalid value for 'use-public-ip'='{value}'. Must be one of: {', '.join(VALID_BODY_USE_PUBLIC_IP)}",
            )
    if "clear-text" in payload:
        value = payload["clear-text"]
        if value not in VALID_BODY_CLEAR_TEXT:
            return (
                False,
                f"Invalid value for 'clear-text'='{value}'. Must be one of: {', '.join(VALID_BODY_CLEAR_TEXT)}",
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
    "endpoint": "system/ddns",
    "category": "cmdb",
    "api_path": "system/ddns",
    "mkey": "ddnsid",
    "mkey_type": "integer",
    "help": "Configure DDNS.",
    "total_fields": 20,
    "required_fields_count": 2,
    "fields_with_defaults_count": 16,
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
