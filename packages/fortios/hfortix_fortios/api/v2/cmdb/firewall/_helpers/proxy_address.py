"""Validation helpers for firewall/proxy_address - Auto-generated"""

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
    "host",  # Address object for the host.
    "application",  # SaaS application.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "uuid": "00000000-0000-0000-0000-000000000000",
    "type": "url",
    "host": "",
    "host-regex": "",
    "path": "",
    "query": "",
    "referrer": "disable",
    "method": "",
    "ua": "",
    "ua-min-ver": "",
    "ua-max-ver": "",
    "header-name": "",
    "header": "",
    "case-sensitivity": "disable",
    "color": 0,
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
    "type": "option",  # Proxy address type.
    "host": "string",  # Address object for the host.
    "host-regex": "string",  # Host name as a regular expression.
    "path": "string",  # URL path as a regular expression.
    "query": "string",  # Match the query part of the URL as a regular expression.
    "referrer": "option",  # Enable/disable use of referrer field in the HTTP header to m
    "category": "string",  # FortiGuard category ID.
    "method": "option",  # HTTP request methods to be used.
    "ua": "option",  # Names of browsers to be used as user agent.
    "ua-min-ver": "string",  # Minimum version of the user agent specified in dotted notati
    "ua-max-ver": "string",  # Maximum version of the user agent specified in dotted notati
    "header-name": "string",  # Name of HTTP header.
    "header": "string",  # HTTP header name as a regular expression.
    "case-sensitivity": "option",  # Enable to make the pattern case sensitive.
    "header-group": "string",  # HTTP header group.
    "color": "integer",  # Integer value to determine the color of the icon in the GUI 
    "tagging": "string",  # Config object tagging.
    "comment": "var-string",  # Optional comments.
    "application": "string",  # SaaS application.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "Address name.",
    "uuid": "Universally Unique Identifier (UUID; automatically assigned but can be manually reset).",
    "type": "Proxy address type.",
    "host": "Address object for the host.",
    "host-regex": "Host name as a regular expression.",
    "path": "URL path as a regular expression.",
    "query": "Match the query part of the URL as a regular expression.",
    "referrer": "Enable/disable use of referrer field in the HTTP header to match the address.",
    "category": "FortiGuard category ID.",
    "method": "HTTP request methods to be used.",
    "ua": "Names of browsers to be used as user agent.",
    "ua-min-ver": "Minimum version of the user agent specified in dotted notation. For example, use 90.0.1 with the ua field set to \"chrome\" to require Google Chrome's minimum version must be 90.0.1.",
    "ua-max-ver": "Maximum version of the user agent specified in dotted notation. For example, use 120 with the ua field set to \"chrome\" to require Google Chrome's maximum version must be 120.",
    "header-name": "Name of HTTP header.",
    "header": "HTTP header name as a regular expression.",
    "case-sensitivity": "Enable to make the pattern case sensitive.",
    "header-group": "HTTP header group.",
    "color": "Integer value to determine the color of the icon in the GUI (1 - 32, default = 0, which sets value to 1).",
    "tagging": "Config object tagging.",
    "comment": "Optional comments.",
    "application": "SaaS application.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 79},
    "host": {"type": "string", "max_length": 79},
    "host-regex": {"type": "string", "max_length": 255},
    "path": {"type": "string", "max_length": 255},
    "query": {"type": "string", "max_length": 255},
    "ua-min-ver": {"type": "string", "max_length": 63},
    "ua-max-ver": {"type": "string", "max_length": 63},
    "header-name": {"type": "string", "max_length": 79},
    "header": {"type": "string", "max_length": 255},
    "color": {"type": "integer", "min": 0, "max": 32},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "category": {
        "id": {
            "type": "integer",
            "help": "FortiGuard category ID.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
    },
    "header-group": {
        "id": {
            "type": "integer",
            "help": "ID.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "header-name": {
            "type": "string",
            "help": "HTTP header.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
        "header": {
            "type": "string",
            "help": "HTTP header regular expression.",
            "required": True,
            "default": "",
            "max_length": 255,
        },
        "case-sensitivity": {
            "type": "option",
            "help": "Case sensitivity in pattern.",
            "default": "disable",
            "options": [{"help": "Case insensitive in pattern.", "label": "Disable", "name": "disable"}, {"help": "Case sensitive in pattern.", "label": "Enable", "name": "enable"}],
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
    "application": {
        "name": {
            "type": "string",
            "help": "SaaS application name.",
            "default": "",
            "max_length": 79,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_TYPE = [
    "host-regex",  # Host regular expression.
    "url",  # HTTP URL.
    "category",  # FortiGuard URL catgegory.
    "method",  # HTTP request method.
    "ua",  # HTTP request user agent.
    "header",  # HTTP request header.
    "src-advanced",  # HTTP advanced source criteria.
    "dst-advanced",  # HTTP advanced destination criteria.
    "saas",  # SaaS application.
]
VALID_BODY_REFERRER = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_METHOD = [
    "get",  # GET method.
    "post",  # POST method.
    "put",  # PUT method.
    "head",  # HEAD method.
    "connect",  # CONNECT method.
    "trace",  # TRACE method.
    "options",  # OPTIONS method.
    "delete",  # DELETE method.
    "update",  # UPDATE method.
    "patch",  # PATCH method.
    "other",  # Other methods.
]
VALID_BODY_UA = [
    "chrome",  # Google Chrome.
    "ms",  # Microsoft Internet Explorer or EDGE.
    "firefox",  # Mozilla Firefox.
    "safari",  # Apple Safari.
    "ie",  # Microsoft Internet Explorer.
    "edge",  # Microsoft Edge.
    "other",  # Other browsers.
]
VALID_BODY_CASE_SENSITIVITY = [
    "disable",  # Case insensitive in pattern.
    "enable",  # Case sensitive in pattern.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_firewall_proxy_address_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for firewall/proxy_address."""
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
    """Validate required fields for firewall/proxy_address."""
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


def validate_firewall_proxy_address_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new firewall/proxy_address object."""
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
    if "referrer" in payload:
        value = payload["referrer"]
        if value not in VALID_BODY_REFERRER:
            desc = FIELD_DESCRIPTIONS.get("referrer", "")
            error_msg = f"Invalid value for 'referrer': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_REFERRER)}"
            error_msg += f"\n  → Example: referrer='{{ VALID_BODY_REFERRER[0] }}'"
            return (False, error_msg)
    if "method" in payload:
        value = payload["method"]
        if value not in VALID_BODY_METHOD:
            desc = FIELD_DESCRIPTIONS.get("method", "")
            error_msg = f"Invalid value for 'method': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_METHOD)}"
            error_msg += f"\n  → Example: method='{{ VALID_BODY_METHOD[0] }}'"
            return (False, error_msg)
    if "ua" in payload:
        value = payload["ua"]
        if value not in VALID_BODY_UA:
            desc = FIELD_DESCRIPTIONS.get("ua", "")
            error_msg = f"Invalid value for 'ua': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_UA)}"
            error_msg += f"\n  → Example: ua='{{ VALID_BODY_UA[0] }}'"
            return (False, error_msg)
    if "case-sensitivity" in payload:
        value = payload["case-sensitivity"]
        if value not in VALID_BODY_CASE_SENSITIVITY:
            desc = FIELD_DESCRIPTIONS.get("case-sensitivity", "")
            error_msg = f"Invalid value for 'case-sensitivity': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CASE_SENSITIVITY)}"
            error_msg += f"\n  → Example: case-sensitivity='{{ VALID_BODY_CASE_SENSITIVITY[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_firewall_proxy_address_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update firewall/proxy_address."""
    # Step 1: Validate enum values
    if "type" in payload:
        value = payload["type"]
        if value not in VALID_BODY_TYPE:
            return (
                False,
                f"Invalid value for 'type'='{value}'. Must be one of: {', '.join(VALID_BODY_TYPE)}",
            )
    if "referrer" in payload:
        value = payload["referrer"]
        if value not in VALID_BODY_REFERRER:
            return (
                False,
                f"Invalid value for 'referrer'='{value}'. Must be one of: {', '.join(VALID_BODY_REFERRER)}",
            )
    if "method" in payload:
        value = payload["method"]
        if value not in VALID_BODY_METHOD:
            return (
                False,
                f"Invalid value for 'method'='{value}'. Must be one of: {', '.join(VALID_BODY_METHOD)}",
            )
    if "ua" in payload:
        value = payload["ua"]
        if value not in VALID_BODY_UA:
            return (
                False,
                f"Invalid value for 'ua'='{value}'. Must be one of: {', '.join(VALID_BODY_UA)}",
            )
    if "case-sensitivity" in payload:
        value = payload["case-sensitivity"]
        if value not in VALID_BODY_CASE_SENSITIVITY:
            return (
                False,
                f"Invalid value for 'case-sensitivity'='{value}'. Must be one of: {', '.join(VALID_BODY_CASE_SENSITIVITY)}",
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
    "endpoint": "firewall/proxy_address",
    "category": "cmdb",
    "api_path": "firewall/proxy-address",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure web proxy address.",
    "total_fields": 21,
    "required_fields_count": 2,
    "fields_with_defaults_count": 16,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
