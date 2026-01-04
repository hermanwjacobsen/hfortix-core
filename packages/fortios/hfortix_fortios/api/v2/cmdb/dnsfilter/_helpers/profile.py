"""
Validation helpers for dnsfilter/profile endpoint.

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
    "name",  # Profile name.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "log-all-domain": "disable",
    "sdns-ftgd-err-log": "enable",
    "sdns-domain-log": "enable",
    "block-action": "redirect",
    "redirect-portal": "0.0.0.0",
    "redirect-portal6": "::",
    "block-botnet": "disable",
    "safe-search": "disable",
    "youtube-restrict": "strict",
    "strip-ech": "enable",
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
    "domain-filter": "string",  # Domain filter settings.
    "ftgd-dns": "string",  # FortiGuard DNS Filter settings.
    "log-all-domain": "option",  # Enable/disable logging of all domains visited (detailed DNS 
    "sdns-ftgd-err-log": "option",  # Enable/disable FortiGuard SDNS rating error logging.
    "sdns-domain-log": "option",  # Enable/disable domain filtering and botnet domain logging.
    "block-action": "option",  # Action to take for blocked domains.
    "redirect-portal": "ipv4-address",  # IPv4 address of the SDNS redirect portal.
    "redirect-portal6": "ipv6-address",  # IPv6 address of the SDNS redirect portal.
    "block-botnet": "option",  # Enable/disable blocking botnet C&C DNS lookups.
    "safe-search": "option",  # Enable/disable Google, Bing, YouTube, Qwant, DuckDuckGo safe
    "youtube-restrict": "option",  # Set safe search for YouTube restriction level.
    "external-ip-blocklist": "string",  # One or more external IP block lists.
    "dns-translation": "string",  # DNS translation settings.
    "transparent-dns-database": "string",  # Transparent DNS database zones.
    "strip-ech": "option",  # Enable/disable removal of the encrypted client hello service
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "Profile name.",
    "comment": "Comment.",
    "domain-filter": "Domain filter settings.",
    "ftgd-dns": "FortiGuard DNS Filter settings.",
    "log-all-domain": "Enable/disable logging of all domains visited (detailed DNS logging).",
    "sdns-ftgd-err-log": "Enable/disable FortiGuard SDNS rating error logging.",
    "sdns-domain-log": "Enable/disable domain filtering and botnet domain logging.",
    "block-action": "Action to take for blocked domains.",
    "redirect-portal": "IPv4 address of the SDNS redirect portal.",
    "redirect-portal6": "IPv6 address of the SDNS redirect portal.",
    "block-botnet": "Enable/disable blocking botnet C&C DNS lookups.",
    "safe-search": "Enable/disable Google, Bing, YouTube, Qwant, DuckDuckGo safe search.",
    "youtube-restrict": "Set safe search for YouTube restriction level.",
    "external-ip-blocklist": "One or more external IP block lists.",
    "dns-translation": "DNS translation settings.",
    "transparent-dns-database": "Transparent DNS database zones.",
    "strip-ech": "Enable/disable removal of the encrypted client hello service parameter from supporting DNS RRs.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 47},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "domain-filter": {
        "domain-filter-table": {
            "type": "integer",
            "help": "DNS domain filter table ID.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
    },
    "ftgd-dns": {
        "options": {
            "type": "option",
            "help": "FortiGuard DNS filter options.",
            "default": "",
            "options": ["error-allow", "ftgd-disable"],
        },
        "filters": {
            "type": "string",
            "help": "FortiGuard DNS domain filters.",
        },
    },
    "external-ip-blocklist": {
        "name": {
            "type": "string",
            "help": "External domain block list name.",
            "default": "",
            "max_length": 79,
        },
    },
    "dns-translation": {
        "id": {
            "type": "integer",
            "help": "ID.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "addr-type": {
            "type": "option",
            "help": "DNS translation type (IPv4 or IPv6).",
            "required": True,
            "default": "ipv4",
            "options": ["ipv4", "ipv6"],
        },
        "src": {
            "type": "ipv4-address",
            "help": "IPv4 address or subnet on the internal network to compare with the resolved address in DNS query replies. If the resolved address matches, the resolved address is substituted with dst.",
            "default": "0.0.0.0",
        },
        "dst": {
            "type": "ipv4-address",
            "help": "IPv4 address or subnet on the external network to substitute for the resolved address in DNS query replies. Can be single IP address or subnet on the external network, but number of addresses must equal number of mapped IP addresses in src.",
            "default": "0.0.0.0",
        },
        "netmask": {
            "type": "ipv4-netmask",
            "help": "If src and dst are subnets rather than single IP addresses, enter the netmask for both src and dst.",
            "default": "255.255.255.255",
        },
        "status": {
            "type": "option",
            "help": "Enable/disable this DNS translation entry.",
            "default": "enable",
            "options": ["enable", "disable"],
        },
        "src6": {
            "type": "ipv6-address",
            "help": "IPv6 address or subnet on the internal network to compare with the resolved address in DNS query replies. If the resolved address matches, the resolved address is substituted with dst6.",
            "default": "::",
        },
        "dst6": {
            "type": "ipv6-address",
            "help": "IPv6 address or subnet on the external network to substitute for the resolved address in DNS query replies. Can be single IP address or subnet on the external network, but number of addresses must equal number of mapped IP addresses in src6.",
            "default": "::",
        },
        "prefix": {
            "type": "integer",
            "help": "If src6 and dst6 are subnets rather than single IP addresses, enter the prefix for both src6 and dst6 (1 - 128, default = 128).",
            "default": 128,
            "min_value": 1,
            "max_value": 128,
        },
    },
    "transparent-dns-database": {
        "name": {
            "type": "string",
            "help": "DNS database zone name.",
            "default": "",
            "max_length": 79,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_LOG_ALL_DOMAIN = [
    "enable",
    "disable",
]
VALID_BODY_SDNS_FTGD_ERR_LOG = [
    "enable",
    "disable",
]
VALID_BODY_SDNS_DOMAIN_LOG = [
    "enable",
    "disable",
]
VALID_BODY_BLOCK_ACTION = [
    "block",
    "redirect",
    "block-sevrfail",
]
VALID_BODY_BLOCK_BOTNET = [
    "disable",
    "enable",
]
VALID_BODY_SAFE_SEARCH = [
    "disable",
    "enable",
]
VALID_BODY_YOUTUBE_RESTRICT = [
    "strict",
    "moderate",
    "none",
]
VALID_BODY_STRIP_ECH = [
    "disable",
    "enable",
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_dnsfilter_profile_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters for dnsfilter/profile.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_dnsfilter_profile_get()
        >>> assert is_valid == True
        
        >>> # Valid - Get specific item by name
        >>> is_valid, error = validate_dnsfilter_profile_get(name="test-item")
        >>> assert is_valid == True
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_dnsfilter_profile_get(
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
    Validate required fields for dnsfilter/profile.

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


def validate_dnsfilter_profile_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new dnsfilter/profile object.

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
        ...     "name": True,  # Profile name.
        ... }
        >>> is_valid, error = validate_dnsfilter_profile_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "name": True,
        ...     "log-all-domain": "enable",  # Valid enum value
        ... }
        >>> is_valid, error = validate_dnsfilter_profile_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["log-all-domain"] = "invalid-value"
        >>> is_valid, error = validate_dnsfilter_profile_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_dnsfilter_profile_post(payload)
        >>> assert is_valid == False
        >>> assert "Missing required field" in error
    """
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "log-all-domain" in payload:
        value = payload["log-all-domain"]
        if value not in VALID_BODY_LOG_ALL_DOMAIN:
            desc = FIELD_DESCRIPTIONS.get("log-all-domain", "")
            error_msg = f"Invalid value for 'log-all-domain': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LOG_ALL_DOMAIN)}"
            error_msg += f"\n  → Example: log-all-domain='{{ VALID_BODY_LOG_ALL_DOMAIN[0] }}'"
            return (False, error_msg)
    if "sdns-ftgd-err-log" in payload:
        value = payload["sdns-ftgd-err-log"]
        if value not in VALID_BODY_SDNS_FTGD_ERR_LOG:
            desc = FIELD_DESCRIPTIONS.get("sdns-ftgd-err-log", "")
            error_msg = f"Invalid value for 'sdns-ftgd-err-log': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SDNS_FTGD_ERR_LOG)}"
            error_msg += f"\n  → Example: sdns-ftgd-err-log='{{ VALID_BODY_SDNS_FTGD_ERR_LOG[0] }}'"
            return (False, error_msg)
    if "sdns-domain-log" in payload:
        value = payload["sdns-domain-log"]
        if value not in VALID_BODY_SDNS_DOMAIN_LOG:
            desc = FIELD_DESCRIPTIONS.get("sdns-domain-log", "")
            error_msg = f"Invalid value for 'sdns-domain-log': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SDNS_DOMAIN_LOG)}"
            error_msg += f"\n  → Example: sdns-domain-log='{{ VALID_BODY_SDNS_DOMAIN_LOG[0] }}'"
            return (False, error_msg)
    if "block-action" in payload:
        value = payload["block-action"]
        if value not in VALID_BODY_BLOCK_ACTION:
            desc = FIELD_DESCRIPTIONS.get("block-action", "")
            error_msg = f"Invalid value for 'block-action': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_BLOCK_ACTION)}"
            error_msg += f"\n  → Example: block-action='{{ VALID_BODY_BLOCK_ACTION[0] }}'"
            return (False, error_msg)
    if "block-botnet" in payload:
        value = payload["block-botnet"]
        if value not in VALID_BODY_BLOCK_BOTNET:
            desc = FIELD_DESCRIPTIONS.get("block-botnet", "")
            error_msg = f"Invalid value for 'block-botnet': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_BLOCK_BOTNET)}"
            error_msg += f"\n  → Example: block-botnet='{{ VALID_BODY_BLOCK_BOTNET[0] }}'"
            return (False, error_msg)
    if "safe-search" in payload:
        value = payload["safe-search"]
        if value not in VALID_BODY_SAFE_SEARCH:
            desc = FIELD_DESCRIPTIONS.get("safe-search", "")
            error_msg = f"Invalid value for 'safe-search': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SAFE_SEARCH)}"
            error_msg += f"\n  → Example: safe-search='{{ VALID_BODY_SAFE_SEARCH[0] }}'"
            return (False, error_msg)
    if "youtube-restrict" in payload:
        value = payload["youtube-restrict"]
        if value not in VALID_BODY_YOUTUBE_RESTRICT:
            desc = FIELD_DESCRIPTIONS.get("youtube-restrict", "")
            error_msg = f"Invalid value for 'youtube-restrict': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_YOUTUBE_RESTRICT)}"
            error_msg += f"\n  → Example: youtube-restrict='{{ VALID_BODY_YOUTUBE_RESTRICT[0] }}'"
            return (False, error_msg)
    if "strip-ech" in payload:
        value = payload["strip-ech"]
        if value not in VALID_BODY_STRIP_ECH:
            desc = FIELD_DESCRIPTIONS.get("strip-ech", "")
            error_msg = f"Invalid value for 'strip-ech': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_STRIP_ECH)}"
            error_msg += f"\n  → Example: strip-ech='{{ VALID_BODY_STRIP_ECH[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_dnsfilter_profile_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update dnsfilter/profile.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_dnsfilter_profile_put(payload)
    """
    # Step 1: Validate enum values
    if "log-all-domain" in payload:
        value = payload["log-all-domain"]
        if value not in VALID_BODY_LOG_ALL_DOMAIN:
            return (
                False,
                f"Invalid value for 'log-all-domain'='{value}'. Must be one of: {', '.join(VALID_BODY_LOG_ALL_DOMAIN)}",
            )
    if "sdns-ftgd-err-log" in payload:
        value = payload["sdns-ftgd-err-log"]
        if value not in VALID_BODY_SDNS_FTGD_ERR_LOG:
            return (
                False,
                f"Invalid value for 'sdns-ftgd-err-log'='{value}'. Must be one of: {', '.join(VALID_BODY_SDNS_FTGD_ERR_LOG)}",
            )
    if "sdns-domain-log" in payload:
        value = payload["sdns-domain-log"]
        if value not in VALID_BODY_SDNS_DOMAIN_LOG:
            return (
                False,
                f"Invalid value for 'sdns-domain-log'='{value}'. Must be one of: {', '.join(VALID_BODY_SDNS_DOMAIN_LOG)}",
            )
    if "block-action" in payload:
        value = payload["block-action"]
        if value not in VALID_BODY_BLOCK_ACTION:
            return (
                False,
                f"Invalid value for 'block-action'='{value}'. Must be one of: {', '.join(VALID_BODY_BLOCK_ACTION)}",
            )
    if "block-botnet" in payload:
        value = payload["block-botnet"]
        if value not in VALID_BODY_BLOCK_BOTNET:
            return (
                False,
                f"Invalid value for 'block-botnet'='{value}'. Must be one of: {', '.join(VALID_BODY_BLOCK_BOTNET)}",
            )
    if "safe-search" in payload:
        value = payload["safe-search"]
        if value not in VALID_BODY_SAFE_SEARCH:
            return (
                False,
                f"Invalid value for 'safe-search'='{value}'. Must be one of: {', '.join(VALID_BODY_SAFE_SEARCH)}",
            )
    if "youtube-restrict" in payload:
        value = payload["youtube-restrict"]
        if value not in VALID_BODY_YOUTUBE_RESTRICT:
            return (
                False,
                f"Invalid value for 'youtube-restrict'='{value}'. Must be one of: {', '.join(VALID_BODY_YOUTUBE_RESTRICT)}",
            )
    if "strip-ech" in payload:
        value = payload["strip-ech"]
        if value not in VALID_BODY_STRIP_ECH:
            return (
                False,
                f"Invalid value for 'strip-ech'='{value}'. Must be one of: {', '.join(VALID_BODY_STRIP_ECH)}",
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
    "endpoint": "dnsfilter/profile",
    "category": "cmdb",
    "api_path": "dnsfilter/profile",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure DNS domain filter profile.",
    "total_fields": 17,
    "required_fields_count": 1,
    "fields_with_defaults_count": 11,
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
