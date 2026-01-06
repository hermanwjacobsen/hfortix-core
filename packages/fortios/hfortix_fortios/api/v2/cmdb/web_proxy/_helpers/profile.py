"""
Validation helpers for web_proxy/profile endpoint.

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
    "header-client-ip": "pass",
    "header-via-request": "pass",
    "header-via-response": "pass",
    "header-client-cert": "pass",
    "header-x-forwarded-for": "pass",
    "header-x-forwarded-client-cert": "pass",
    "header-front-end-https": "pass",
    "header-x-authenticated-user": "pass",
    "header-x-authenticated-groups": "pass",
    "strip-encoding": "disable",
    "log-header-change": "disable",
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
    "header-client-ip": "option",  # Action to take on the HTTP client-IP header in forwarded req
    "header-via-request": "option",  # Action to take on the HTTP via header in forwarded requests:
    "header-via-response": "option",  # Action to take on the HTTP via header in forwarded responses
    "header-client-cert": "option",  # Action to take on the HTTP Client-Cert/Client-Cert-Chain hea
    "header-x-forwarded-for": "option",  # Action to take on the HTTP x-forwarded-for header in forward
    "header-x-forwarded-client-cert": "option",  # Action to take on the HTTP x-forwarded-client-cert header in
    "header-front-end-https": "option",  # Action to take on the HTTP front-end-HTTPS header in forward
    "header-x-authenticated-user": "option",  # Action to take on the HTTP x-authenticated-user header in fo
    "header-x-authenticated-groups": "option",  # Action to take on the HTTP x-authenticated-groups header in 
    "strip-encoding": "option",  # Enable/disable stripping unsupported encoding from the reque
    "log-header-change": "option",  # Enable/disable logging HTTP header changes.
    "headers": "string",  # Configure HTTP forwarded requests headers.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "Profile name.",
    "header-client-ip": "Action to take on the HTTP client-IP header in forwarded requests: forwards (pass), adds, or removes the HTTP header.",
    "header-via-request": "Action to take on the HTTP via header in forwarded requests: forwards (pass), adds, or removes the HTTP header.",
    "header-via-response": "Action to take on the HTTP via header in forwarded responses: forwards (pass), adds, or removes the HTTP header.",
    "header-client-cert": "Action to take on the HTTP Client-Cert/Client-Cert-Chain headers in forwarded responses: forwards (pass), adds, or removes the HTTP header.",
    "header-x-forwarded-for": "Action to take on the HTTP x-forwarded-for header in forwarded requests: forwards (pass), adds, or removes the HTTP header.",
    "header-x-forwarded-client-cert": "Action to take on the HTTP x-forwarded-client-cert header in forwarded requests: forwards (pass), adds, or removes the HTTP header.",
    "header-front-end-https": "Action to take on the HTTP front-end-HTTPS header in forwarded requests: forwards (pass), adds, or removes the HTTP header.",
    "header-x-authenticated-user": "Action to take on the HTTP x-authenticated-user header in forwarded requests: forwards (pass), adds, or removes the HTTP header.",
    "header-x-authenticated-groups": "Action to take on the HTTP x-authenticated-groups header in forwarded requests: forwards (pass), adds, or removes the HTTP header.",
    "strip-encoding": "Enable/disable stripping unsupported encoding from the request header.",
    "log-header-change": "Enable/disable logging HTTP header changes.",
    "headers": "Configure HTTP forwarded requests headers.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 63},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "headers": {
        "id": {
            "type": "integer",
            "help": "HTTP forwarded header id.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "name": {
            "type": "string",
            "help": "HTTP forwarded header name.",
            "default": "",
            "max_length": 79,
        },
        "dstaddr": {
            "type": "string",
            "help": "Destination address and address group names.",
        },
        "dstaddr6": {
            "type": "string",
            "help": "Destination address and address group names (IPv6).",
        },
        "action": {
            "type": "option",
            "help": "Configure adding, removing, or logging of the HTTP header entry in HTTP requests and responses.",
            "default": "add-to-request",
            "options": [{"help": "Add the HTTP header to request.", "label": "Add To Request", "name": "add-to-request"}, {"help": "Add the HTTP header to response.", "label": "Add To Response", "name": "add-to-response"}, {"help": "Remove the HTTP header from request.", "label": "Remove From Request", "name": "remove-from-request"}, {"help": "Remove the HTTP header from response.", "label": "Remove From Response", "name": "remove-from-response"}, {"help": "Record the HTTP header in utm-webfilter log.", "label": "Monitor Request", "name": "monitor-request"}, {"help": "Record the HTTP header in utm-webfilter log.", "label": "Monitor Response", "name": "monitor-response"}],
        },
        "content": {
            "type": "string",
            "help": "HTTP header content (max length: 3999 characters).",
            "default": "",
            "max_length": 3999,
        },
        "base64-encoding": {
            "type": "option",
            "help": "Enable/disable use of base64 encoding of HTTP content.",
            "default": "disable",
            "options": [{"help": "Disable use of base64 encoding of HTTP content.", "label": "Disable", "name": "disable"}, {"help": "Enable use of base64 encoding of HTTP content.", "label": "Enable", "name": "enable"}],
        },
        "add-option": {
            "type": "option",
            "help": "Configure options to append content to existing HTTP header or add new HTTP header.",
            "default": "new",
            "options": [{"help": "Append content to existing HTTP header or create new header if HTTP header is not found.", "label": "Append", "name": "append"}, {"help": "Create new header only if existing HTTP header is not found.", "label": "New On Not Found", "name": "new-on-not-found"}, {"help": "Create new header regardless if existing HTTP header is found or not.", "label": "New", "name": "new"}, {"help": "Replace content to existing HTTP header or create new header if HTTP header is not found.", "label": "Replace", "name": "replace"}, {"help": "Replace content to existing HTTP header.", "label": "Replace When Match", "name": "replace-when-match"}],
        },
        "protocol": {
            "type": "option",
            "help": "Configure protocol(s) to take add-option action on (HTTP, HTTPS, or both).",
            "default": "https http",
            "options": [{"help": "Perform add-option action on HTTPS.", "label": "Https", "name": "https"}, {"help": "Perform add-option action on HTTP.", "label": "Http", "name": "http"}],
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_HEADER_CLIENT_IP = [
    "pass",  # Forward the same HTTP header.
    "add",  # Add the HTTP header.
    "remove",  # Remove the HTTP header.
]
VALID_BODY_HEADER_VIA_REQUEST = [
    "pass",  # Forward the same HTTP header.
    "add",  # Add the HTTP header.
    "remove",  # Remove the HTTP header.
]
VALID_BODY_HEADER_VIA_RESPONSE = [
    "pass",  # Forward the same HTTP header.
    "add",  # Add the HTTP header.
    "remove",  # Remove the HTTP header.
]
VALID_BODY_HEADER_CLIENT_CERT = [
    "pass",  # Forward the same HTTP header.
    "add",  # Add the HTTP header.
    "remove",  # Remove the HTTP header.
]
VALID_BODY_HEADER_X_FORWARDED_FOR = [
    "pass",  # Forward the same HTTP header.
    "add",  # Add the HTTP header.
    "remove",  # Remove the HTTP header.
]
VALID_BODY_HEADER_X_FORWARDED_CLIENT_CERT = [
    "pass",  # Forward the same HTTP header.
    "add",  # Add the HTTP header.
    "remove",  # Remove the HTTP header.
]
VALID_BODY_HEADER_FRONT_END_HTTPS = [
    "pass",  # Forward the same HTTP header.
    "add",  # Add the HTTP header.
    "remove",  # Remove the HTTP header.
]
VALID_BODY_HEADER_X_AUTHENTICATED_USER = [
    "pass",  # Forward the same HTTP header.
    "add",  # Add the HTTP header.
    "remove",  # Remove the HTTP header.
]
VALID_BODY_HEADER_X_AUTHENTICATED_GROUPS = [
    "pass",  # Forward the same HTTP header.
    "add",  # Add the HTTP header.
    "remove",  # Remove the HTTP header.
]
VALID_BODY_STRIP_ENCODING = [
    "enable",  # Enable stripping of unsupported encoding from the request header.
    "disable",  # Disable stripping of unsupported encoding from the request header.
]
VALID_BODY_LOG_HEADER_CHANGE = [
    "enable",  # Enable Enable/disable logging HTTP header changes.
    "disable",  # Disable Enable/disable logging HTTP header changes.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_web_proxy_profile_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters for web_proxy/profile.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_web_proxy_profile_get()
        >>> assert is_valid == True
        
        >>> # Valid - Get specific item by name
        >>> is_valid, error = validate_web_proxy_profile_get(name="test-item")
        >>> assert is_valid == True
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_web_proxy_profile_get(
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
    Validate required fields for web_proxy/profile.

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


def validate_web_proxy_profile_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new web_proxy/profile object.

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
        >>> is_valid, error = validate_web_proxy_profile_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "header-client-ip": "{'name': 'pass', 'help': 'Forward the same HTTP header.', 'label': 'Pass', 'description': 'Forward the same HTTP header'}",  # Valid enum value
        ... }
        >>> is_valid, error = validate_web_proxy_profile_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["header-client-ip"] = "invalid-value"
        >>> is_valid, error = validate_web_proxy_profile_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_web_proxy_profile_post(payload)
        >>> assert is_valid == False
        >>> assert "Missing required field" in error
    """
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "header-client-ip" in payload:
        value = payload["header-client-ip"]
        if value not in VALID_BODY_HEADER_CLIENT_IP:
            desc = FIELD_DESCRIPTIONS.get("header-client-ip", "")
            error_msg = f"Invalid value for 'header-client-ip': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_HEADER_CLIENT_IP)}"
            error_msg += f"\n  → Example: header-client-ip='{{ VALID_BODY_HEADER_CLIENT_IP[0] }}'"
            return (False, error_msg)
    if "header-via-request" in payload:
        value = payload["header-via-request"]
        if value not in VALID_BODY_HEADER_VIA_REQUEST:
            desc = FIELD_DESCRIPTIONS.get("header-via-request", "")
            error_msg = f"Invalid value for 'header-via-request': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_HEADER_VIA_REQUEST)}"
            error_msg += f"\n  → Example: header-via-request='{{ VALID_BODY_HEADER_VIA_REQUEST[0] }}'"
            return (False, error_msg)
    if "header-via-response" in payload:
        value = payload["header-via-response"]
        if value not in VALID_BODY_HEADER_VIA_RESPONSE:
            desc = FIELD_DESCRIPTIONS.get("header-via-response", "")
            error_msg = f"Invalid value for 'header-via-response': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_HEADER_VIA_RESPONSE)}"
            error_msg += f"\n  → Example: header-via-response='{{ VALID_BODY_HEADER_VIA_RESPONSE[0] }}'"
            return (False, error_msg)
    if "header-client-cert" in payload:
        value = payload["header-client-cert"]
        if value not in VALID_BODY_HEADER_CLIENT_CERT:
            desc = FIELD_DESCRIPTIONS.get("header-client-cert", "")
            error_msg = f"Invalid value for 'header-client-cert': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_HEADER_CLIENT_CERT)}"
            error_msg += f"\n  → Example: header-client-cert='{{ VALID_BODY_HEADER_CLIENT_CERT[0] }}'"
            return (False, error_msg)
    if "header-x-forwarded-for" in payload:
        value = payload["header-x-forwarded-for"]
        if value not in VALID_BODY_HEADER_X_FORWARDED_FOR:
            desc = FIELD_DESCRIPTIONS.get("header-x-forwarded-for", "")
            error_msg = f"Invalid value for 'header-x-forwarded-for': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_HEADER_X_FORWARDED_FOR)}"
            error_msg += f"\n  → Example: header-x-forwarded-for='{{ VALID_BODY_HEADER_X_FORWARDED_FOR[0] }}'"
            return (False, error_msg)
    if "header-x-forwarded-client-cert" in payload:
        value = payload["header-x-forwarded-client-cert"]
        if value not in VALID_BODY_HEADER_X_FORWARDED_CLIENT_CERT:
            desc = FIELD_DESCRIPTIONS.get("header-x-forwarded-client-cert", "")
            error_msg = f"Invalid value for 'header-x-forwarded-client-cert': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_HEADER_X_FORWARDED_CLIENT_CERT)}"
            error_msg += f"\n  → Example: header-x-forwarded-client-cert='{{ VALID_BODY_HEADER_X_FORWARDED_CLIENT_CERT[0] }}'"
            return (False, error_msg)
    if "header-front-end-https" in payload:
        value = payload["header-front-end-https"]
        if value not in VALID_BODY_HEADER_FRONT_END_HTTPS:
            desc = FIELD_DESCRIPTIONS.get("header-front-end-https", "")
            error_msg = f"Invalid value for 'header-front-end-https': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_HEADER_FRONT_END_HTTPS)}"
            error_msg += f"\n  → Example: header-front-end-https='{{ VALID_BODY_HEADER_FRONT_END_HTTPS[0] }}'"
            return (False, error_msg)
    if "header-x-authenticated-user" in payload:
        value = payload["header-x-authenticated-user"]
        if value not in VALID_BODY_HEADER_X_AUTHENTICATED_USER:
            desc = FIELD_DESCRIPTIONS.get("header-x-authenticated-user", "")
            error_msg = f"Invalid value for 'header-x-authenticated-user': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_HEADER_X_AUTHENTICATED_USER)}"
            error_msg += f"\n  → Example: header-x-authenticated-user='{{ VALID_BODY_HEADER_X_AUTHENTICATED_USER[0] }}'"
            return (False, error_msg)
    if "header-x-authenticated-groups" in payload:
        value = payload["header-x-authenticated-groups"]
        if value not in VALID_BODY_HEADER_X_AUTHENTICATED_GROUPS:
            desc = FIELD_DESCRIPTIONS.get("header-x-authenticated-groups", "")
            error_msg = f"Invalid value for 'header-x-authenticated-groups': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_HEADER_X_AUTHENTICATED_GROUPS)}"
            error_msg += f"\n  → Example: header-x-authenticated-groups='{{ VALID_BODY_HEADER_X_AUTHENTICATED_GROUPS[0] }}'"
            return (False, error_msg)
    if "strip-encoding" in payload:
        value = payload["strip-encoding"]
        if value not in VALID_BODY_STRIP_ENCODING:
            desc = FIELD_DESCRIPTIONS.get("strip-encoding", "")
            error_msg = f"Invalid value for 'strip-encoding': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_STRIP_ENCODING)}"
            error_msg += f"\n  → Example: strip-encoding='{{ VALID_BODY_STRIP_ENCODING[0] }}'"
            return (False, error_msg)
    if "log-header-change" in payload:
        value = payload["log-header-change"]
        if value not in VALID_BODY_LOG_HEADER_CHANGE:
            desc = FIELD_DESCRIPTIONS.get("log-header-change", "")
            error_msg = f"Invalid value for 'log-header-change': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LOG_HEADER_CHANGE)}"
            error_msg += f"\n  → Example: log-header-change='{{ VALID_BODY_LOG_HEADER_CHANGE[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_web_proxy_profile_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update web_proxy/profile.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_web_proxy_profile_put(payload)
    """
    # Step 1: Validate enum values
    if "header-client-ip" in payload:
        value = payload["header-client-ip"]
        if value not in VALID_BODY_HEADER_CLIENT_IP:
            return (
                False,
                f"Invalid value for 'header-client-ip'='{value}'. Must be one of: {', '.join(VALID_BODY_HEADER_CLIENT_IP)}",
            )
    if "header-via-request" in payload:
        value = payload["header-via-request"]
        if value not in VALID_BODY_HEADER_VIA_REQUEST:
            return (
                False,
                f"Invalid value for 'header-via-request'='{value}'. Must be one of: {', '.join(VALID_BODY_HEADER_VIA_REQUEST)}",
            )
    if "header-via-response" in payload:
        value = payload["header-via-response"]
        if value not in VALID_BODY_HEADER_VIA_RESPONSE:
            return (
                False,
                f"Invalid value for 'header-via-response'='{value}'. Must be one of: {', '.join(VALID_BODY_HEADER_VIA_RESPONSE)}",
            )
    if "header-client-cert" in payload:
        value = payload["header-client-cert"]
        if value not in VALID_BODY_HEADER_CLIENT_CERT:
            return (
                False,
                f"Invalid value for 'header-client-cert'='{value}'. Must be one of: {', '.join(VALID_BODY_HEADER_CLIENT_CERT)}",
            )
    if "header-x-forwarded-for" in payload:
        value = payload["header-x-forwarded-for"]
        if value not in VALID_BODY_HEADER_X_FORWARDED_FOR:
            return (
                False,
                f"Invalid value for 'header-x-forwarded-for'='{value}'. Must be one of: {', '.join(VALID_BODY_HEADER_X_FORWARDED_FOR)}",
            )
    if "header-x-forwarded-client-cert" in payload:
        value = payload["header-x-forwarded-client-cert"]
        if value not in VALID_BODY_HEADER_X_FORWARDED_CLIENT_CERT:
            return (
                False,
                f"Invalid value for 'header-x-forwarded-client-cert'='{value}'. Must be one of: {', '.join(VALID_BODY_HEADER_X_FORWARDED_CLIENT_CERT)}",
            )
    if "header-front-end-https" in payload:
        value = payload["header-front-end-https"]
        if value not in VALID_BODY_HEADER_FRONT_END_HTTPS:
            return (
                False,
                f"Invalid value for 'header-front-end-https'='{value}'. Must be one of: {', '.join(VALID_BODY_HEADER_FRONT_END_HTTPS)}",
            )
    if "header-x-authenticated-user" in payload:
        value = payload["header-x-authenticated-user"]
        if value not in VALID_BODY_HEADER_X_AUTHENTICATED_USER:
            return (
                False,
                f"Invalid value for 'header-x-authenticated-user'='{value}'. Must be one of: {', '.join(VALID_BODY_HEADER_X_AUTHENTICATED_USER)}",
            )
    if "header-x-authenticated-groups" in payload:
        value = payload["header-x-authenticated-groups"]
        if value not in VALID_BODY_HEADER_X_AUTHENTICATED_GROUPS:
            return (
                False,
                f"Invalid value for 'header-x-authenticated-groups'='{value}'. Must be one of: {', '.join(VALID_BODY_HEADER_X_AUTHENTICATED_GROUPS)}",
            )
    if "strip-encoding" in payload:
        value = payload["strip-encoding"]
        if value not in VALID_BODY_STRIP_ENCODING:
            return (
                False,
                f"Invalid value for 'strip-encoding'='{value}'. Must be one of: {', '.join(VALID_BODY_STRIP_ENCODING)}",
            )
    if "log-header-change" in payload:
        value = payload["log-header-change"]
        if value not in VALID_BODY_LOG_HEADER_CHANGE:
            return (
                False,
                f"Invalid value for 'log-header-change'='{value}'. Must be one of: {', '.join(VALID_BODY_LOG_HEADER_CHANGE)}",
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
    "endpoint": "web_proxy/profile",
    "category": "cmdb",
    "api_path": "web-proxy/profile",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure web proxy profiles.",
    "total_fields": 13,
    "required_fields_count": 0,
    "fields_with_defaults_count": 12,
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
