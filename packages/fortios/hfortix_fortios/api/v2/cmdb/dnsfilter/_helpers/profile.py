"""Validation helpers for dnsfilter/profile - Auto-generated"""

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
            "options": [{"help": "Allow all domains when FortiGuard DNS servers fail.", "label": "Error Allow", "name": "error-allow"}, {"help": "Disable FortiGuard DNS domain rating.", "label": "Ftgd Disable", "name": "ftgd-disable"}],
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
            "options": [{"help": "IPv4 address type.", "label": "Ipv4", "name": "ipv4"}, {"help": "IPv6 address type.", "label": "Ipv6", "name": "ipv6"}],
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
            "options": [{"help": "Enable this DNS translation.", "label": "Enable", "name": "enable"}, {"help": "Disable this DNS translation.", "label": "Disable", "name": "disable"}],
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
    "enable",  # Enable logging of all domains visited.
    "disable",  # Disable logging of all domains visited.
]
VALID_BODY_SDNS_FTGD_ERR_LOG = [
    "enable",  # Enable FortiGuard SDNS rating error logging.
    "disable",  # Disable FortiGuard SDNS rating error logging.
]
VALID_BODY_SDNS_DOMAIN_LOG = [
    "enable",  # Enable domain filtering and botnet domain logging.
    "disable",  # Disable domain filtering and botnet domain logging.
]
VALID_BODY_BLOCK_ACTION = [
    "block",  # Return NXDOMAIN for blocked domains.
    "redirect",  # Redirect blocked domains to SDNS portal.
    "block-sevrfail",  # Return SERVFAIL for blocked domains.
]
VALID_BODY_BLOCK_BOTNET = [
    "disable",  # Disable blocking botnet C&C DNS lookups.
    "enable",  # Enable blocking botnet C&C DNS lookups.
]
VALID_BODY_SAFE_SEARCH = [
    "disable",  # Disable Google, Bing, YouTube, Qwant, DuckDuckGo safe search.
    "enable",  # Enable Google, Bing, YouTube, Qwant, DuckDuckGo safe search.
]
VALID_BODY_YOUTUBE_RESTRICT = [
    "strict",  # Enable strict safe seach for YouTube.
    "moderate",  # Enable moderate safe search for YouTube.
    "none",  # Disable safe search for YouTube.
]
VALID_BODY_STRIP_ECH = [
    "disable",  # Disable removal of the encrypted client hello service parameter from supporting DNS RRs.
    "enable",  # Enable removal of the encrypted client hello service parameter from supporting DNS RRs.
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
    """Validate GET request parameters for dnsfilter/profile."""
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
    """Validate required fields for dnsfilter/profile."""
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
    """Validate POST request to create new dnsfilter/profile object."""
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
    """Validate PUT request to update dnsfilter/profile."""
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
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
