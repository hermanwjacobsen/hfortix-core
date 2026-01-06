"""Validation helpers for webfilter/fortiguard - Auto-generated"""

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
    "cache-mode": "ttl",
    "cache-prefix-match": "enable",
    "cache-mem-permille": 1,
    "ovrd-auth-port-http": 8008,
    "ovrd-auth-port-https": 8010,
    "ovrd-auth-port-https-flow": 8015,
    "ovrd-auth-port-warning": 8020,
    "ovrd-auth-https": "enable",
    "warn-auth-https": "enable",
    "close-ports": "disable",
    "request-packet-size-limit": 0,
    "embed-image": "enable",
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
    "cache-mode": "option",  # Cache entry expiration mode.
    "cache-prefix-match": "option",  # Enable/disable prefix matching in the cache.
    "cache-mem-permille": "integer",  # Maximum permille of available memory allocated to caching (1
    "ovrd-auth-port-http": "integer",  # Port to use for FortiGuard Web Filter HTTP override authenti
    "ovrd-auth-port-https": "integer",  # Port to use for FortiGuard Web Filter HTTPS override authent
    "ovrd-auth-port-https-flow": "integer",  # Port to use for FortiGuard Web Filter HTTPS override authent
    "ovrd-auth-port-warning": "integer",  # Port to use for FortiGuard Web Filter Warning override authe
    "ovrd-auth-https": "option",  # Enable/disable use of HTTPS for override authentication.
    "warn-auth-https": "option",  # Enable/disable use of HTTPS for warning and authentication.
    "close-ports": "option",  # Close ports used for HTTP/HTTPS override authentication and 
    "request-packet-size-limit": "integer",  # Limit size of URL request packets sent to FortiGuard server 
    "embed-image": "option",  # Enable/disable embedding images into replacement messages (d
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "cache-mode": "Cache entry expiration mode.",
    "cache-prefix-match": "Enable/disable prefix matching in the cache.",
    "cache-mem-permille": "Maximum permille of available memory allocated to caching (1 - 150).",
    "ovrd-auth-port-http": "Port to use for FortiGuard Web Filter HTTP override authentication.",
    "ovrd-auth-port-https": "Port to use for FortiGuard Web Filter HTTPS override authentication in proxy mode.",
    "ovrd-auth-port-https-flow": "Port to use for FortiGuard Web Filter HTTPS override authentication in flow mode.",
    "ovrd-auth-port-warning": "Port to use for FortiGuard Web Filter Warning override authentication.",
    "ovrd-auth-https": "Enable/disable use of HTTPS for override authentication.",
    "warn-auth-https": "Enable/disable use of HTTPS for warning and authentication.",
    "close-ports": "Close ports used for HTTP/HTTPS override authentication and disable user overrides.",
    "request-packet-size-limit": "Limit size of URL request packets sent to FortiGuard server (0 for default).",
    "embed-image": "Enable/disable embedding images into replacement messages (default = enable).",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "cache-mem-permille": {"type": "integer", "min": 1, "max": 150},
    "ovrd-auth-port-http": {"type": "integer", "min": 0, "max": 65535},
    "ovrd-auth-port-https": {"type": "integer", "min": 0, "max": 65535},
    "ovrd-auth-port-https-flow": {"type": "integer", "min": 0, "max": 65535},
    "ovrd-auth-port-warning": {"type": "integer", "min": 0, "max": 65535},
    "request-packet-size-limit": {"type": "integer", "min": 576, "max": 10000},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
}


# Valid enum values from API documentation
VALID_BODY_CACHE_MODE = [
    "ttl",  # Expire cache items by time-to-live.
    "db-ver",  # Expire cache items when the server DB version changes.
]
VALID_BODY_CACHE_PREFIX_MATCH = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_OVRD_AUTH_HTTPS = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_WARN_AUTH_HTTPS = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_CLOSE_PORTS = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_EMBED_IMAGE = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_webfilter_fortiguard_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for webfilter/fortiguard."""
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
    """Validate required fields for webfilter/fortiguard."""
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


def validate_webfilter_fortiguard_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new webfilter/fortiguard object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "cache-mode" in payload:
        value = payload["cache-mode"]
        if value not in VALID_BODY_CACHE_MODE:
            desc = FIELD_DESCRIPTIONS.get("cache-mode", "")
            error_msg = f"Invalid value for 'cache-mode': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CACHE_MODE)}"
            error_msg += f"\n  → Example: cache-mode='{{ VALID_BODY_CACHE_MODE[0] }}'"
            return (False, error_msg)
    if "cache-prefix-match" in payload:
        value = payload["cache-prefix-match"]
        if value not in VALID_BODY_CACHE_PREFIX_MATCH:
            desc = FIELD_DESCRIPTIONS.get("cache-prefix-match", "")
            error_msg = f"Invalid value for 'cache-prefix-match': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CACHE_PREFIX_MATCH)}"
            error_msg += f"\n  → Example: cache-prefix-match='{{ VALID_BODY_CACHE_PREFIX_MATCH[0] }}'"
            return (False, error_msg)
    if "ovrd-auth-https" in payload:
        value = payload["ovrd-auth-https"]
        if value not in VALID_BODY_OVRD_AUTH_HTTPS:
            desc = FIELD_DESCRIPTIONS.get("ovrd-auth-https", "")
            error_msg = f"Invalid value for 'ovrd-auth-https': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_OVRD_AUTH_HTTPS)}"
            error_msg += f"\n  → Example: ovrd-auth-https='{{ VALID_BODY_OVRD_AUTH_HTTPS[0] }}'"
            return (False, error_msg)
    if "warn-auth-https" in payload:
        value = payload["warn-auth-https"]
        if value not in VALID_BODY_WARN_AUTH_HTTPS:
            desc = FIELD_DESCRIPTIONS.get("warn-auth-https", "")
            error_msg = f"Invalid value for 'warn-auth-https': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WARN_AUTH_HTTPS)}"
            error_msg += f"\n  → Example: warn-auth-https='{{ VALID_BODY_WARN_AUTH_HTTPS[0] }}'"
            return (False, error_msg)
    if "close-ports" in payload:
        value = payload["close-ports"]
        if value not in VALID_BODY_CLOSE_PORTS:
            desc = FIELD_DESCRIPTIONS.get("close-ports", "")
            error_msg = f"Invalid value for 'close-ports': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CLOSE_PORTS)}"
            error_msg += f"\n  → Example: close-ports='{{ VALID_BODY_CLOSE_PORTS[0] }}'"
            return (False, error_msg)
    if "embed-image" in payload:
        value = payload["embed-image"]
        if value not in VALID_BODY_EMBED_IMAGE:
            desc = FIELD_DESCRIPTIONS.get("embed-image", "")
            error_msg = f"Invalid value for 'embed-image': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_EMBED_IMAGE)}"
            error_msg += f"\n  → Example: embed-image='{{ VALID_BODY_EMBED_IMAGE[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_webfilter_fortiguard_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update webfilter/fortiguard."""
    # Step 1: Validate enum values
    if "cache-mode" in payload:
        value = payload["cache-mode"]
        if value not in VALID_BODY_CACHE_MODE:
            return (
                False,
                f"Invalid value for 'cache-mode'='{value}'. Must be one of: {', '.join(VALID_BODY_CACHE_MODE)}",
            )
    if "cache-prefix-match" in payload:
        value = payload["cache-prefix-match"]
        if value not in VALID_BODY_CACHE_PREFIX_MATCH:
            return (
                False,
                f"Invalid value for 'cache-prefix-match'='{value}'. Must be one of: {', '.join(VALID_BODY_CACHE_PREFIX_MATCH)}",
            )
    if "ovrd-auth-https" in payload:
        value = payload["ovrd-auth-https"]
        if value not in VALID_BODY_OVRD_AUTH_HTTPS:
            return (
                False,
                f"Invalid value for 'ovrd-auth-https'='{value}'. Must be one of: {', '.join(VALID_BODY_OVRD_AUTH_HTTPS)}",
            )
    if "warn-auth-https" in payload:
        value = payload["warn-auth-https"]
        if value not in VALID_BODY_WARN_AUTH_HTTPS:
            return (
                False,
                f"Invalid value for 'warn-auth-https'='{value}'. Must be one of: {', '.join(VALID_BODY_WARN_AUTH_HTTPS)}",
            )
    if "close-ports" in payload:
        value = payload["close-ports"]
        if value not in VALID_BODY_CLOSE_PORTS:
            return (
                False,
                f"Invalid value for 'close-ports'='{value}'. Must be one of: {', '.join(VALID_BODY_CLOSE_PORTS)}",
            )
    if "embed-image" in payload:
        value = payload["embed-image"]
        if value not in VALID_BODY_EMBED_IMAGE:
            return (
                False,
                f"Invalid value for 'embed-image'='{value}'. Must be one of: {', '.join(VALID_BODY_EMBED_IMAGE)}",
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
    "endpoint": "webfilter/fortiguard",
    "category": "cmdb",
    "api_path": "webfilter/fortiguard",
    "help": "Configure FortiGuard Web Filter service.",
    "total_fields": 12,
    "required_fields_count": 0,
    "fields_with_defaults_count": 12,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
