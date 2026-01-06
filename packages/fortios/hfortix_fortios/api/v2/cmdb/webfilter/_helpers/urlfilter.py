"""Validation helpers for webfilter/urlfilter - Auto-generated"""

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
    "name",  # Name of URL filter list.
    "entries",  # URL filter entries.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "id": 0,
    "name": "",
    "one-arm-ips-urlfilter": "disable",
    "ip-addr-block": "disable",
    "ip4-mapped-ip6": "disable",
    "include-subdomains": "enable",
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
    "name": "string",  # Name of URL filter list.
    "comment": "var-string",  # Optional comments.
    "one-arm-ips-urlfilter": "option",  # Enable/disable DNS resolver for one-arm IPS URL filter opera
    "ip-addr-block": "option",  # Enable/disable blocking URLs when the hostname appears as an
    "ip4-mapped-ip6": "option",  # Enable/disable matching of IPv4 mapped IPv6 URLs.
    "include-subdomains": "option",  # Enable/disable matching subdomains. Applies only to simple t
    "entries": "string",  # URL filter entries.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "id": "ID.",
    "name": "Name of URL filter list.",
    "comment": "Optional comments.",
    "one-arm-ips-urlfilter": "Enable/disable DNS resolver for one-arm IPS URL filter operation.",
    "ip-addr-block": "Enable/disable blocking URLs when the hostname appears as an IP address.",
    "ip4-mapped-ip6": "Enable/disable matching of IPv4 mapped IPv6 URLs.",
    "include-subdomains": "Enable/disable matching subdomains. Applies only to simple type (default = enable).",
    "entries": "URL filter entries.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "id": {"type": "integer", "min": 0, "max": 4294967295},
    "name": {"type": "string", "max_length": 63},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "entries": {
        "id": {
            "type": "integer",
            "help": "Id.",
            "required": True,
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "url": {
            "type": "string",
            "help": "URL to be filtered.",
            "default": "",
            "max_length": 511,
        },
        "type": {
            "type": "option",
            "help": "Filter type (simple, regex, or wildcard).",
            "default": "simple",
            "options": [{"help": "Simple URL string.", "label": "Simple", "name": "simple"}, {"help": "Regular expression URL string.", "label": "Regex", "name": "regex"}, {"help": "Wildcard URL string.", "label": "Wildcard", "name": "wildcard"}],
        },
        "action": {
            "type": "option",
            "help": "Action to take for URL filter matches.",
            "default": "exempt",
            "options": [{"help": "Exempt matches.", "label": "Exempt", "name": "exempt"}, {"help": "Block matches.", "label": "Block", "name": "block"}, {"help": "Allow matches (no log).", "label": "Allow", "name": "allow"}, {"help": "Allow matches (with log).", "label": "Monitor", "name": "monitor"}],
        },
        "antiphish-action": {
            "type": "option",
            "help": "Action to take for AntiPhishing matches.",
            "default": "block",
            "options": [{"help": "Block matches.", "label": "Block", "name": "block"}, {"help": "Allow matches with log.", "label": "Log", "name": "log"}],
        },
        "status": {
            "type": "option",
            "help": "Enable/disable this URL filter.",
            "default": "enable",
            "options": [{"help": "Enable this URL filter.", "label": "Enable", "name": "enable"}, {"help": "Disable this URL filter.", "label": "Disable", "name": "disable"}],
        },
        "exempt": {
            "type": "option",
            "help": "If action is set to exempt, select the security profile operations that exempt URLs skip. Separate multiple options with a space.",
            "default": "av web-content activex-java-cookie dlp fortiguard range-block antiphish all",
            "options": [{"help": "AntiVirus scanning.", "label": "Av", "name": "av"}, {"help": "Web filter content matching.", "label": "Web Content", "name": "web-content"}, {"help": "ActiveX, Java, and cookie filtering.", "label": "Activex Java Cookie", "name": "activex-java-cookie"}, {"help": "DLP scanning.", "label": "Dlp", "name": "dlp"}, {"help": "FortiGuard web filtering.", "label": "Fortiguard", "name": "fortiguard"}, {"help": "Range block feature.", "label": "Range Block", "name": "range-block"}, {"help": "Pass single connection from all.", "label": "Pass", "name": "pass"}, {"help": "AntiPhish credential checking.", "label": "Antiphish", "name": "antiphish"}, {"help": "Exempt from all security profiles.", "label": "All", "name": "all"}],
        },
        "web-proxy-profile": {
            "type": "string",
            "help": "Web proxy profile.",
            "default": "",
            "max_length": 63,
        },
        "referrer-host": {
            "type": "string",
            "help": "Referrer host name.",
            "default": "",
            "max_length": 255,
        },
        "dns-address-family": {
            "type": "option",
            "help": "Resolve IPv4 address, IPv6 address, or both from DNS server.",
            "default": "ipv4",
            "options": [{"help": "Resolve IPv4 address from DNS server.", "label": "Ipv4", "name": "ipv4"}, {"help": "Resolve IPv6 address from DNS server.", "label": "Ipv6", "name": "ipv6"}, {"help": "Resolve both IPv4 and IPv6 addresses from DNS server.", "label": "Both", "name": "both"}],
        },
        "comment": {
            "type": "var-string",
            "help": "Comment.",
            "max_length": 255,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_ONE_ARM_IPS_URLFILTER = [
    "enable",  # Enable DNS resolver for one-arm IPS URL filter operation.
    "disable",  # Disable DNS resolver for one-arm IPS URL filter operation.
]
VALID_BODY_IP_ADDR_BLOCK = [
    "enable",  # Enable blocking URLs when the hostname appears as an IP address.
    "disable",  # Disable blocking URLs when the hostname appears as an IP address.
]
VALID_BODY_IP4_MAPPED_IP6 = [
    "enable",  # Enable matching IPv4 mapped IPv6 URLs.
    "disable",  # Disable matching IPv4 mapped IPv6 URLs.
]
VALID_BODY_INCLUDE_SUBDOMAINS = [
    "enable",  # Enable matching subdomains. Applies only to simple type.
    "disable",  # Disable matching subdomains. Applies only to simple type.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_webfilter_urlfilter_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for webfilter/urlfilter."""
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
    """Validate required fields for webfilter/urlfilter."""
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


def validate_webfilter_urlfilter_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new webfilter/urlfilter object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "one-arm-ips-urlfilter" in payload:
        value = payload["one-arm-ips-urlfilter"]
        if value not in VALID_BODY_ONE_ARM_IPS_URLFILTER:
            desc = FIELD_DESCRIPTIONS.get("one-arm-ips-urlfilter", "")
            error_msg = f"Invalid value for 'one-arm-ips-urlfilter': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ONE_ARM_IPS_URLFILTER)}"
            error_msg += f"\n  → Example: one-arm-ips-urlfilter='{{ VALID_BODY_ONE_ARM_IPS_URLFILTER[0] }}'"
            return (False, error_msg)
    if "ip-addr-block" in payload:
        value = payload["ip-addr-block"]
        if value not in VALID_BODY_IP_ADDR_BLOCK:
            desc = FIELD_DESCRIPTIONS.get("ip-addr-block", "")
            error_msg = f"Invalid value for 'ip-addr-block': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_IP_ADDR_BLOCK)}"
            error_msg += f"\n  → Example: ip-addr-block='{{ VALID_BODY_IP_ADDR_BLOCK[0] }}'"
            return (False, error_msg)
    if "ip4-mapped-ip6" in payload:
        value = payload["ip4-mapped-ip6"]
        if value not in VALID_BODY_IP4_MAPPED_IP6:
            desc = FIELD_DESCRIPTIONS.get("ip4-mapped-ip6", "")
            error_msg = f"Invalid value for 'ip4-mapped-ip6': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_IP4_MAPPED_IP6)}"
            error_msg += f"\n  → Example: ip4-mapped-ip6='{{ VALID_BODY_IP4_MAPPED_IP6[0] }}'"
            return (False, error_msg)
    if "include-subdomains" in payload:
        value = payload["include-subdomains"]
        if value not in VALID_BODY_INCLUDE_SUBDOMAINS:
            desc = FIELD_DESCRIPTIONS.get("include-subdomains", "")
            error_msg = f"Invalid value for 'include-subdomains': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_INCLUDE_SUBDOMAINS)}"
            error_msg += f"\n  → Example: include-subdomains='{{ VALID_BODY_INCLUDE_SUBDOMAINS[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_webfilter_urlfilter_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update webfilter/urlfilter."""
    # Step 1: Validate enum values
    if "one-arm-ips-urlfilter" in payload:
        value = payload["one-arm-ips-urlfilter"]
        if value not in VALID_BODY_ONE_ARM_IPS_URLFILTER:
            return (
                False,
                f"Invalid value for 'one-arm-ips-urlfilter'='{value}'. Must be one of: {', '.join(VALID_BODY_ONE_ARM_IPS_URLFILTER)}",
            )
    if "ip-addr-block" in payload:
        value = payload["ip-addr-block"]
        if value not in VALID_BODY_IP_ADDR_BLOCK:
            return (
                False,
                f"Invalid value for 'ip-addr-block'='{value}'. Must be one of: {', '.join(VALID_BODY_IP_ADDR_BLOCK)}",
            )
    if "ip4-mapped-ip6" in payload:
        value = payload["ip4-mapped-ip6"]
        if value not in VALID_BODY_IP4_MAPPED_IP6:
            return (
                False,
                f"Invalid value for 'ip4-mapped-ip6'='{value}'. Must be one of: {', '.join(VALID_BODY_IP4_MAPPED_IP6)}",
            )
    if "include-subdomains" in payload:
        value = payload["include-subdomains"]
        if value not in VALID_BODY_INCLUDE_SUBDOMAINS:
            return (
                False,
                f"Invalid value for 'include-subdomains'='{value}'. Must be one of: {', '.join(VALID_BODY_INCLUDE_SUBDOMAINS)}",
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
    "endpoint": "webfilter/urlfilter",
    "category": "cmdb",
    "api_path": "webfilter/urlfilter",
    "mkey": "id",
    "mkey_type": "integer",
    "help": "Configure URL filter lists.",
    "total_fields": 8,
    "required_fields_count": 2,
    "fields_with_defaults_count": 6,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
