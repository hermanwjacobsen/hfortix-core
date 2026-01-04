"""
Validation helpers for firewall/address endpoint.

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
    "interface",  # Name of interface whose IP address is to be used.
    "filter",  # Match criteria filter.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "uuid": "00000000-0000-0000-0000-000000000000",
    "subnet": "0.0.0.0 0.0.0.0",
    "type": "ipmask",
    "route-tag": 0,
    "sub-type": "sdn",
    "clearpass-spt": "unknown",
    "start-ip": "0.0.0.0",
    "end-ip": "0.0.0.0",
    "fqdn": "",
    "country": "",
    "wildcard-fqdn": "",
    "cache-ttl": 0,
    "wildcard": "0.0.0.0 0.0.0.0",
    "sdn": "",
    "interface": "",
    "tenant": "",
    "organization": "",
    "epg-name": "",
    "subnet-name": "",
    "sdn-tag": "",
    "policy-group": "",
    "obj-tag": "",
    "obj-type": "ip",
    "tag-detection-level": "",
    "tag-type": "",
    "hw-vendor": "",
    "hw-model": "",
    "os": "",
    "sw-version": "",
    "associated-interface": "",
    "color": 0,
    "sdn-addr-type": "private",
    "node-ip-only": "disable",
    "allow-routing": "disable",
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
    "name": "string",  # Address name.
    "uuid": "uuid",  # Universally Unique Identifier (UUID; automatically assigned 
    "subnet": "ipv4-classnet-any",  # IP address and subnet mask of address.
    "type": "option",  # Type of address.
    "route-tag": "integer",  # route-tag address.
    "sub-type": "option",  # Sub-type of address.
    "clearpass-spt": "option",  # SPT (System Posture Token) value.
    "macaddr": "string",  # Multiple MAC address ranges.
    "start-ip": "ipv4-address-any",  # First IP address (inclusive) in the range for the address.
    "end-ip": "ipv4-address-any",  # Final IP address (inclusive) in the range for the address.
    "fqdn": "string",  # Fully Qualified Domain Name address.
    "country": "string",  # IP addresses associated to a specific country.
    "wildcard-fqdn": "string",  # Fully Qualified Domain Name with wildcard characters.
    "cache-ttl": "integer",  # Defines the minimal TTL of individual IP addresses in FQDN c
    "wildcard": "ipv4-classnet-any",  # IP address and wildcard netmask.
    "sdn": "string",  # SDN.
    "fsso-group": "string",  # FSSO group(s).
    "sso-attribute-value": "string",  # RADIUS attributes value.
    "interface": "string",  # Name of interface whose IP address is to be used.
    "tenant": "string",  # Tenant.
    "organization": "string",  # Organization domain name (Syntax: organization/domain).
    "epg-name": "string",  # Endpoint group name.
    "subnet-name": "string",  # Subnet name.
    "sdn-tag": "string",  # SDN Tag.
    "policy-group": "string",  # Policy group name.
    "obj-tag": "string",  # Tag of dynamic address object.
    "obj-type": "option",  # Object type.
    "tag-detection-level": "string",  # Tag detection level of dynamic address object.
    "tag-type": "string",  # Tag type of dynamic address object.
    "hw-vendor": "string",  # Dynamic address matching hardware vendor.
    "hw-model": "string",  # Dynamic address matching hardware model.
    "os": "string",  # Dynamic address matching operating system.
    "sw-version": "string",  # Dynamic address matching software version.
    "comment": "var-string",  # Comment.
    "associated-interface": "string",  # Network interface associated with address.
    "color": "integer",  # Color of icon on the GUI.
    "filter": "var-string",  # Match criteria filter.
    "sdn-addr-type": "option",  # Type of addresses to collect.
    "node-ip-only": "option",  # Enable/disable collection of node addresses only in Kubernet
    "obj-id": "var-string",  # Object ID for NSX.
    "list": "string",  # IP address list.
    "tagging": "string",  # Config object tagging.
    "allow-routing": "option",  # Enable/disable use of this address in routing configurations
    "fabric-object": "option",  # Security Fabric global object setting.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "Address name.",
    "uuid": "Universally Unique Identifier (UUID; automatically assigned but can be manually reset).",
    "subnet": "IP address and subnet mask of address.",
    "type": "Type of address.",
    "route-tag": "route-tag address.",
    "sub-type": "Sub-type of address.",
    "clearpass-spt": "SPT (System Posture Token) value.",
    "macaddr": "Multiple MAC address ranges.",
    "start-ip": "First IP address (inclusive) in the range for the address.",
    "end-ip": "Final IP address (inclusive) in the range for the address.",
    "fqdn": "Fully Qualified Domain Name address.",
    "country": "IP addresses associated to a specific country.",
    "wildcard-fqdn": "Fully Qualified Domain Name with wildcard characters.",
    "cache-ttl": "Defines the minimal TTL of individual IP addresses in FQDN cache measured in seconds.",
    "wildcard": "IP address and wildcard netmask.",
    "sdn": "SDN.",
    "fsso-group": "FSSO group(s).",
    "sso-attribute-value": "RADIUS attributes value.",
    "interface": "Name of interface whose IP address is to be used.",
    "tenant": "Tenant.",
    "organization": "Organization domain name (Syntax: organization/domain).",
    "epg-name": "Endpoint group name.",
    "subnet-name": "Subnet name.",
    "sdn-tag": "SDN Tag.",
    "policy-group": "Policy group name.",
    "obj-tag": "Tag of dynamic address object.",
    "obj-type": "Object type.",
    "tag-detection-level": "Tag detection level of dynamic address object.",
    "tag-type": "Tag type of dynamic address object.",
    "hw-vendor": "Dynamic address matching hardware vendor.",
    "hw-model": "Dynamic address matching hardware model.",
    "os": "Dynamic address matching operating system.",
    "sw-version": "Dynamic address matching software version.",
    "comment": "Comment.",
    "associated-interface": "Network interface associated with address.",
    "color": "Color of icon on the GUI.",
    "filter": "Match criteria filter.",
    "sdn-addr-type": "Type of addresses to collect.",
    "node-ip-only": "Enable/disable collection of node addresses only in Kubernetes.",
    "obj-id": "Object ID for NSX.",
    "list": "IP address list.",
    "tagging": "Config object tagging.",
    "allow-routing": "Enable/disable use of this address in routing configurations.",
    "fabric-object": "Security Fabric global object setting.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 79},
    "route-tag": {"type": "integer", "min": 1, "max": 4294967295},
    "fqdn": {"type": "string", "max_length": 255},
    "country": {"type": "string", "max_length": 2},
    "wildcard-fqdn": {"type": "string", "max_length": 255},
    "cache-ttl": {"type": "integer", "min": 0, "max": 86400},
    "sdn": {"type": "string", "max_length": 35},
    "interface": {"type": "string", "max_length": 35},
    "tenant": {"type": "string", "max_length": 35},
    "organization": {"type": "string", "max_length": 35},
    "epg-name": {"type": "string", "max_length": 255},
    "subnet-name": {"type": "string", "max_length": 255},
    "sdn-tag": {"type": "string", "max_length": 15},
    "policy-group": {"type": "string", "max_length": 15},
    "obj-tag": {"type": "string", "max_length": 255},
    "tag-detection-level": {"type": "string", "max_length": 15},
    "tag-type": {"type": "string", "max_length": 63},
    "hw-vendor": {"type": "string", "max_length": 35},
    "hw-model": {"type": "string", "max_length": 35},
    "os": {"type": "string", "max_length": 35},
    "sw-version": {"type": "string", "max_length": 35},
    "associated-interface": {"type": "string", "max_length": 35},
    "color": {"type": "integer", "min": 0, "max": 32},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "macaddr": {
        "macaddr": {
            "type": "string",
            "help": "MAC address ranges <start>[-<end>] separated by space.",
            "required": True,
            "default": "",
            "max_length": 127,
        },
    },
    "fsso-group": {
        "name": {
            "type": "string",
            "help": "FSSO group name.",
            "default": "",
            "max_length": 511,
        },
    },
    "sso-attribute-value": {
        "name": {
            "type": "string",
            "help": "RADIUS attribute value.",
            "default": "",
            "max_length": 511,
        },
    },
    "list": {
        "ip": {
            "type": "string",
            "help": "IP.",
            "required": True,
            "default": "",
            "max_length": 35,
        },
    },
    "tagging": {
        "name": {
            "type": "string",
            "help": "Tagging entry name.",
            "default": "",
            "max_length": 63,
        },
        "category": {
            "type": "string",
            "help": "Tag category.",
            "default": "",
            "max_length": 63,
        },
        "tags": {
            "type": "string",
            "help": "Tags.",
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_TYPE = [
    "ipmask",
    "iprange",
    "fqdn",
    "geography",
    "wildcard",
    "dynamic",
    "interface-subnet",
    "mac",
    "route-tag",
]
VALID_BODY_SUB_TYPE = [
    "sdn",
    "clearpass-spt",
    "fsso",
    "rsso",
    "ems-tag",
    "fortivoice-tag",
    "fortinac-tag",
    "swc-tag",
    "device-identification",
    "external-resource",
    "obsolete",
]
VALID_BODY_CLEARPASS_SPT = [
    "unknown",
    "healthy",
    "quarantine",
    "checkup",
    "transient",
    "infected",
]
VALID_BODY_OBJ_TYPE = [
    "ip",
    "mac",
]
VALID_BODY_SDN_ADDR_TYPE = [
    "private",
    "public",
    "all",
]
VALID_BODY_NODE_IP_ONLY = [
    "enable",
    "disable",
]
VALID_BODY_ALLOW_ROUTING = [
    "enable",
    "disable",
]
VALID_BODY_FABRIC_OBJECT = [
    "enable",
    "disable",
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_firewall_address_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters for firewall/address.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_firewall_address_get()
        >>> assert is_valid == True
        
        >>> # Valid - Get specific item by name
        >>> is_valid, error = validate_firewall_address_get(name="test-item")
        >>> assert is_valid == True
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_firewall_address_get(
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
    Validate required fields for firewall/address.

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


def validate_firewall_address_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new firewall/address object.

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
        ...     "interface": True,  # Name of interface whose IP address is to be used.
        ...     "filter": True,  # Match criteria filter.
        ... }
        >>> is_valid, error = validate_firewall_address_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "interface": True,
        ...     "type": "ipmask",  # Valid enum value
        ... }
        >>> is_valid, error = validate_firewall_address_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["type"] = "invalid-value"
        >>> is_valid, error = validate_firewall_address_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_firewall_address_post(payload)
        >>> assert is_valid == False
        >>> assert "Missing required field" in error
    """
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "type" in payload:
        value = payload["type"]
        if value not in VALID_BODY_TYPE:
            desc = FIELD_DESCRIPTIONS.get("type", "")
            error_msg = f"Invalid value for 'type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_TYPE)}"
            error_msg += f"\n  → Example: type='{{ VALID_BODY_TYPE[0] }}'"
            return (False, error_msg)
    if "sub-type" in payload:
        value = payload["sub-type"]
        if value not in VALID_BODY_SUB_TYPE:
            desc = FIELD_DESCRIPTIONS.get("sub-type", "")
            error_msg = f"Invalid value for 'sub-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SUB_TYPE)}"
            error_msg += f"\n  → Example: sub-type='{{ VALID_BODY_SUB_TYPE[0] }}'"
            return (False, error_msg)
    if "clearpass-spt" in payload:
        value = payload["clearpass-spt"]
        if value not in VALID_BODY_CLEARPASS_SPT:
            desc = FIELD_DESCRIPTIONS.get("clearpass-spt", "")
            error_msg = f"Invalid value for 'clearpass-spt': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CLEARPASS_SPT)}"
            error_msg += f"\n  → Example: clearpass-spt='{{ VALID_BODY_CLEARPASS_SPT[0] }}'"
            return (False, error_msg)
    if "obj-type" in payload:
        value = payload["obj-type"]
        if value not in VALID_BODY_OBJ_TYPE:
            desc = FIELD_DESCRIPTIONS.get("obj-type", "")
            error_msg = f"Invalid value for 'obj-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_OBJ_TYPE)}"
            error_msg += f"\n  → Example: obj-type='{{ VALID_BODY_OBJ_TYPE[0] }}'"
            return (False, error_msg)
    if "sdn-addr-type" in payload:
        value = payload["sdn-addr-type"]
        if value not in VALID_BODY_SDN_ADDR_TYPE:
            desc = FIELD_DESCRIPTIONS.get("sdn-addr-type", "")
            error_msg = f"Invalid value for 'sdn-addr-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SDN_ADDR_TYPE)}"
            error_msg += f"\n  → Example: sdn-addr-type='{{ VALID_BODY_SDN_ADDR_TYPE[0] }}'"
            return (False, error_msg)
    if "node-ip-only" in payload:
        value = payload["node-ip-only"]
        if value not in VALID_BODY_NODE_IP_ONLY:
            desc = FIELD_DESCRIPTIONS.get("node-ip-only", "")
            error_msg = f"Invalid value for 'node-ip-only': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_NODE_IP_ONLY)}"
            error_msg += f"\n  → Example: node-ip-only='{{ VALID_BODY_NODE_IP_ONLY[0] }}'"
            return (False, error_msg)
    if "allow-routing" in payload:
        value = payload["allow-routing"]
        if value not in VALID_BODY_ALLOW_ROUTING:
            desc = FIELD_DESCRIPTIONS.get("allow-routing", "")
            error_msg = f"Invalid value for 'allow-routing': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ALLOW_ROUTING)}"
            error_msg += f"\n  → Example: allow-routing='{{ VALID_BODY_ALLOW_ROUTING[0] }}'"
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


def validate_firewall_address_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update firewall/address.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_firewall_address_put(payload)
    """
    # Step 1: Validate enum values
    if "type" in payload:
        value = payload["type"]
        if value not in VALID_BODY_TYPE:
            return (
                False,
                f"Invalid value for 'type'='{value}'. Must be one of: {', '.join(VALID_BODY_TYPE)}",
            )
    if "sub-type" in payload:
        value = payload["sub-type"]
        if value not in VALID_BODY_SUB_TYPE:
            return (
                False,
                f"Invalid value for 'sub-type'='{value}'. Must be one of: {', '.join(VALID_BODY_SUB_TYPE)}",
            )
    if "clearpass-spt" in payload:
        value = payload["clearpass-spt"]
        if value not in VALID_BODY_CLEARPASS_SPT:
            return (
                False,
                f"Invalid value for 'clearpass-spt'='{value}'. Must be one of: {', '.join(VALID_BODY_CLEARPASS_SPT)}",
            )
    if "obj-type" in payload:
        value = payload["obj-type"]
        if value not in VALID_BODY_OBJ_TYPE:
            return (
                False,
                f"Invalid value for 'obj-type'='{value}'. Must be one of: {', '.join(VALID_BODY_OBJ_TYPE)}",
            )
    if "sdn-addr-type" in payload:
        value = payload["sdn-addr-type"]
        if value not in VALID_BODY_SDN_ADDR_TYPE:
            return (
                False,
                f"Invalid value for 'sdn-addr-type'='{value}'. Must be one of: {', '.join(VALID_BODY_SDN_ADDR_TYPE)}",
            )
    if "node-ip-only" in payload:
        value = payload["node-ip-only"]
        if value not in VALID_BODY_NODE_IP_ONLY:
            return (
                False,
                f"Invalid value for 'node-ip-only'='{value}'. Must be one of: {', '.join(VALID_BODY_NODE_IP_ONLY)}",
            )
    if "allow-routing" in payload:
        value = payload["allow-routing"]
        if value not in VALID_BODY_ALLOW_ROUTING:
            return (
                False,
                f"Invalid value for 'allow-routing'='{value}'. Must be one of: {', '.join(VALID_BODY_ALLOW_ROUTING)}",
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
    "endpoint": "firewall/address",
    "category": "cmdb",
    "api_path": "firewall/address",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure IPv4 addresses.",
    "total_fields": 44,
    "required_fields_count": 2,
    "fields_with_defaults_count": 36,
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
