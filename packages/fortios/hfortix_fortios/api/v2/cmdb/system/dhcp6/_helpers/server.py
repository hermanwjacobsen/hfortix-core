"""
Validation helpers for system/dhcp6/server endpoint.

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
    "interface",  # DHCP server can assign IP configurations to clients connected to this interface.
    "upstream-interface",  # Interface name from where delegated information is provided.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "id": 0,
    "status": "enable",
    "rapid-commit": "disable",
    "lease-time": 604800,
    "dns-service": "specify",
    "dns-search-list": "specify",
    "dns-server1": "::",
    "dns-server2": "::",
    "dns-server3": "::",
    "dns-server4": "::",
    "domain": "",
    "subnet": "::/0",
    "interface": "",
    "delegated-prefix-route": "disable",
    "upstream-interface": "",
    "delegated-prefix-iaid": 0,
    "ip-mode": "range",
    "prefix-mode": "dhcp6",
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
    "id": "integer",  # ID.
    "status": "option",  # Enable/disable this DHCPv6 configuration.
    "rapid-commit": "option",  # Enable/disable allow/disallow rapid commit.
    "lease-time": "integer",  # Lease time in seconds, 0 means unlimited.
    "dns-service": "option",  # Options for assigning DNS servers to DHCPv6 clients.
    "dns-search-list": "option",  # DNS search list options.
    "dns-server1": "ipv6-address",  # DNS server 1.
    "dns-server2": "ipv6-address",  # DNS server 2.
    "dns-server3": "ipv6-address",  # DNS server 3.
    "dns-server4": "ipv6-address",  # DNS server 4.
    "domain": "string",  # Domain name suffix for the IP addresses that the DHCP server
    "subnet": "ipv6-prefix",  # Subnet or subnet-id if the IP mode is delegated.
    "interface": "string",  # DHCP server can assign IP configurations to clients connecte
    "delegated-prefix-route": "option",  # Enable/disable automatically adding of routing for delegated
    "options": "string",  # DHCPv6 options.
    "upstream-interface": "string",  # Interface name from where delegated information is provided.
    "delegated-prefix-iaid": "integer",  # IAID of obtained delegated-prefix from the upstream interfac
    "ip-mode": "option",  # Method used to assign client IP.
    "prefix-mode": "option",  # Assigning a prefix from a DHCPv6 client or RA.
    "prefix-range": "string",  # DHCP prefix configuration.
    "ip-range": "string",  # DHCP IP range configuration.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "id": "ID.",
    "status": "Enable/disable this DHCPv6 configuration.",
    "rapid-commit": "Enable/disable allow/disallow rapid commit.",
    "lease-time": "Lease time in seconds, 0 means unlimited.",
    "dns-service": "Options for assigning DNS servers to DHCPv6 clients.",
    "dns-search-list": "DNS search list options.",
    "dns-server1": "DNS server 1.",
    "dns-server2": "DNS server 2.",
    "dns-server3": "DNS server 3.",
    "dns-server4": "DNS server 4.",
    "domain": "Domain name suffix for the IP addresses that the DHCP server assigns to clients.",
    "subnet": "Subnet or subnet-id if the IP mode is delegated.",
    "interface": "DHCP server can assign IP configurations to clients connected to this interface.",
    "delegated-prefix-route": "Enable/disable automatically adding of routing for delegated prefix.",
    "options": "DHCPv6 options.",
    "upstream-interface": "Interface name from where delegated information is provided.",
    "delegated-prefix-iaid": "IAID of obtained delegated-prefix from the upstream interface.",
    "ip-mode": "Method used to assign client IP.",
    "prefix-mode": "Assigning a prefix from a DHCPv6 client or RA.",
    "prefix-range": "DHCP prefix configuration.",
    "ip-range": "DHCP IP range configuration.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "id": {"type": "integer", "min": 0, "max": 4294967295},
    "lease-time": {"type": "integer", "min": 300, "max": 8640000},
    "domain": {"type": "string", "max_length": 35},
    "interface": {"type": "string", "max_length": 15},
    "upstream-interface": {"type": "string", "max_length": 15},
    "delegated-prefix-iaid": {"type": "integer", "min": 0, "max": 4294967295},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "options": {
        "id": {
            "type": "integer",
            "help": "ID.",
            "required": True,
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "code": {
            "type": "integer",
            "help": "DHCPv6 option code.",
            "required": True,
            "default": 0,
            "min_value": 0,
            "max_value": 255,
        },
        "type": {
            "type": "option",
            "help": "DHCPv6 option type.",
            "default": "hex",
            "options": [{"help": "DHCPv6 option in hex.", "label": "Hex", "name": "hex"}, {"help": "DHCPv6 option in string.", "label": "String", "name": "string"}, {"help": "DHCPv6 option in IP6.", "label": "Ip6", "name": "ip6"}, {"help": "DHCPv6 option in domain search option format.", "label": "Fqdn", "name": "fqdn"}],
        },
        "value": {
            "type": "string",
            "help": "DHCPv6 option value (hexadecimal value must be even).",
            "default": "",
            "max_length": 312,
        },
        "ip6": {
            "type": "user",
            "help": "DHCP option IP6s.",
            "default": "",
        },
        "vci-match": {
            "type": "option",
            "help": "Enable/disable vendor class option matching. When enabled only DHCP requests with a matching VCI are served with this option.",
            "default": "disable",
            "options": [{"help": "Disable VCI matching.", "label": "Disable", "name": "disable"}, {"help": "Enable VCI matching.", "label": "Enable", "name": "enable"}],
        },
        "vci-string": {
            "type": "string",
            "help": "One or more VCI strings in quotes separated by spaces.",
        },
    },
    "prefix-range": {
        "id": {
            "type": "integer",
            "help": "ID.",
            "required": True,
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "start-prefix": {
            "type": "ipv6-address",
            "help": "Start of prefix range.",
            "required": True,
            "default": "::",
        },
        "end-prefix": {
            "type": "ipv6-address",
            "help": "End of prefix range.",
            "required": True,
            "default": "::",
        },
        "prefix-length": {
            "type": "integer",
            "help": "Prefix length.",
            "required": True,
            "default": 0,
            "min_value": 1,
            "max_value": 128,
        },
    },
    "ip-range": {
        "id": {
            "type": "integer",
            "help": "ID.",
            "required": True,
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "start-ip": {
            "type": "ipv6-address",
            "help": "Start of IP range.",
            "required": True,
            "default": "::",
        },
        "end-ip": {
            "type": "ipv6-address",
            "help": "End of IP range.",
            "required": True,
            "default": "::",
        },
        "vci-match": {
            "type": "option",
            "help": "Enable/disable vendor class option matching. When enabled only DHCP requests with a matching VC are served with this range.",
            "default": "disable",
            "options": [{"help": "Disable VCI matching.", "label": "Disable", "name": "disable"}, {"help": "Enable VCI matching.", "label": "Enable", "name": "enable"}],
        },
        "vci-string": {
            "type": "string",
            "help": "One or more VCI strings in quotes separated by spaces.",
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_STATUS = [
    "disable",  # Enable this DHCPv6 server configuration.
    "enable",  # Disable this DHCPv6 server configuration.
]
VALID_BODY_RAPID_COMMIT = [
    "disable",  # Do not allow rapid commit.
    "enable",  # Allow rapid commit.
]
VALID_BODY_DNS_SERVICE = [
    "delegated",  # Delegated DNS settings.
    "default",  # Clients are assigned the FortiGate's configured DNS servers.
    "specify",  # Specify up to 3 DNS servers in the DHCPv6 server configuration.
]
VALID_BODY_DNS_SEARCH_LIST = [
    "delegated",  # Delegated the DNS search list.
    "specify",  # Specify the DNS search list.
]
VALID_BODY_DELEGATED_PREFIX_ROUTE = [
    "disable",  # Disable automatically adding of routing for delegated prefix.
    "enable",  # Enable automatically adding of routing for delegated prefix.
]
VALID_BODY_IP_MODE = [
    "range",  # Use range defined by start IP/end IP to assign client IP.
    "delegated",  # Use delegated prefix method to assign client IP.
]
VALID_BODY_PREFIX_MODE = [
    "dhcp6",  # Use delegated prefix from a DHCPv6 client.
    "ra",  # Use prefix from RA.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_system_dhcp6_server_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters for system/dhcp6/server.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_system_dhcp6_server_get()
        >>> assert is_valid == True
        
        >>> # Valid - Get specific item by id
        >>> is_valid, error = validate_system_dhcp6_server_get(id="test-item")
        >>> assert is_valid == True
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_system_dhcp6_server_get(
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
    Validate required fields for system/dhcp6/server.

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


def validate_system_dhcp6_server_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new system/dhcp6/server object.

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
        ...     "interface": True,  # DHCP server can assign IP configurations to client
        ...     "upstream-interface": True,  # Interface name from where delegated information is
        ... }
        >>> is_valid, error = validate_system_dhcp6_server_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "interface": True,
        ...     "status": "{'name': 'disable', 'help': 'Enable this DHCPv6 server configuration.', 'label': 'Disable', 'description': 'Enable this DHCPv6 server configuration'}",  # Valid enum value
        ... }
        >>> is_valid, error = validate_system_dhcp6_server_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["status"] = "invalid-value"
        >>> is_valid, error = validate_system_dhcp6_server_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_system_dhcp6_server_post(payload)
        >>> assert is_valid == False
        >>> assert "Missing required field" in error
    """
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "status" in payload:
        value = payload["status"]
        if value not in VALID_BODY_STATUS:
            desc = FIELD_DESCRIPTIONS.get("status", "")
            error_msg = f"Invalid value for 'status': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_STATUS)}"
            error_msg += f"\n  → Example: status='{{ VALID_BODY_STATUS[0] }}'"
            return (False, error_msg)
    if "rapid-commit" in payload:
        value = payload["rapid-commit"]
        if value not in VALID_BODY_RAPID_COMMIT:
            desc = FIELD_DESCRIPTIONS.get("rapid-commit", "")
            error_msg = f"Invalid value for 'rapid-commit': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_RAPID_COMMIT)}"
            error_msg += f"\n  → Example: rapid-commit='{{ VALID_BODY_RAPID_COMMIT[0] }}'"
            return (False, error_msg)
    if "dns-service" in payload:
        value = payload["dns-service"]
        if value not in VALID_BODY_DNS_SERVICE:
            desc = FIELD_DESCRIPTIONS.get("dns-service", "")
            error_msg = f"Invalid value for 'dns-service': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DNS_SERVICE)}"
            error_msg += f"\n  → Example: dns-service='{{ VALID_BODY_DNS_SERVICE[0] }}'"
            return (False, error_msg)
    if "dns-search-list" in payload:
        value = payload["dns-search-list"]
        if value not in VALID_BODY_DNS_SEARCH_LIST:
            desc = FIELD_DESCRIPTIONS.get("dns-search-list", "")
            error_msg = f"Invalid value for 'dns-search-list': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DNS_SEARCH_LIST)}"
            error_msg += f"\n  → Example: dns-search-list='{{ VALID_BODY_DNS_SEARCH_LIST[0] }}'"
            return (False, error_msg)
    if "delegated-prefix-route" in payload:
        value = payload["delegated-prefix-route"]
        if value not in VALID_BODY_DELEGATED_PREFIX_ROUTE:
            desc = FIELD_DESCRIPTIONS.get("delegated-prefix-route", "")
            error_msg = f"Invalid value for 'delegated-prefix-route': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DELEGATED_PREFIX_ROUTE)}"
            error_msg += f"\n  → Example: delegated-prefix-route='{{ VALID_BODY_DELEGATED_PREFIX_ROUTE[0] }}'"
            return (False, error_msg)
    if "ip-mode" in payload:
        value = payload["ip-mode"]
        if value not in VALID_BODY_IP_MODE:
            desc = FIELD_DESCRIPTIONS.get("ip-mode", "")
            error_msg = f"Invalid value for 'ip-mode': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_IP_MODE)}"
            error_msg += f"\n  → Example: ip-mode='{{ VALID_BODY_IP_MODE[0] }}'"
            return (False, error_msg)
    if "prefix-mode" in payload:
        value = payload["prefix-mode"]
        if value not in VALID_BODY_PREFIX_MODE:
            desc = FIELD_DESCRIPTIONS.get("prefix-mode", "")
            error_msg = f"Invalid value for 'prefix-mode': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PREFIX_MODE)}"
            error_msg += f"\n  → Example: prefix-mode='{{ VALID_BODY_PREFIX_MODE[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_system_dhcp6_server_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update system/dhcp6/server.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_system_dhcp6_server_put(payload)
    """
    # Step 1: Validate enum values
    if "status" in payload:
        value = payload["status"]
        if value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid value for 'status'='{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )
    if "rapid-commit" in payload:
        value = payload["rapid-commit"]
        if value not in VALID_BODY_RAPID_COMMIT:
            return (
                False,
                f"Invalid value for 'rapid-commit'='{value}'. Must be one of: {', '.join(VALID_BODY_RAPID_COMMIT)}",
            )
    if "dns-service" in payload:
        value = payload["dns-service"]
        if value not in VALID_BODY_DNS_SERVICE:
            return (
                False,
                f"Invalid value for 'dns-service'='{value}'. Must be one of: {', '.join(VALID_BODY_DNS_SERVICE)}",
            )
    if "dns-search-list" in payload:
        value = payload["dns-search-list"]
        if value not in VALID_BODY_DNS_SEARCH_LIST:
            return (
                False,
                f"Invalid value for 'dns-search-list'='{value}'. Must be one of: {', '.join(VALID_BODY_DNS_SEARCH_LIST)}",
            )
    if "delegated-prefix-route" in payload:
        value = payload["delegated-prefix-route"]
        if value not in VALID_BODY_DELEGATED_PREFIX_ROUTE:
            return (
                False,
                f"Invalid value for 'delegated-prefix-route'='{value}'. Must be one of: {', '.join(VALID_BODY_DELEGATED_PREFIX_ROUTE)}",
            )
    if "ip-mode" in payload:
        value = payload["ip-mode"]
        if value not in VALID_BODY_IP_MODE:
            return (
                False,
                f"Invalid value for 'ip-mode'='{value}'. Must be one of: {', '.join(VALID_BODY_IP_MODE)}",
            )
    if "prefix-mode" in payload:
        value = payload["prefix-mode"]
        if value not in VALID_BODY_PREFIX_MODE:
            return (
                False,
                f"Invalid value for 'prefix-mode'='{value}'. Must be one of: {', '.join(VALID_BODY_PREFIX_MODE)}",
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
    "endpoint": "system/dhcp6/server",
    "category": "cmdb",
    "api_path": "system.dhcp6/server",
    "mkey": "id",
    "mkey_type": "integer",
    "help": "Configure DHCPv6 servers.",
    "total_fields": 21,
    "required_fields_count": 2,
    "fields_with_defaults_count": 18,
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
