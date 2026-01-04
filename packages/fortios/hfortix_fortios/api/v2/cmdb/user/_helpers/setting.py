"""
Validation helpers for user/setting endpoint.

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
    "auth-type": "http https ftp telnet",
    "auth-cert": "",
    "auth-ca-cert": "",
    "auth-secure-http": "disable",
    "auth-http-basic": "disable",
    "auth-ssl-allow-renegotiation": "disable",
    "auth-src-mac": "enable",
    "auth-on-demand": "implicitly",
    "auth-timeout": 5,
    "auth-timeout-type": "idle-timeout",
    "auth-portal-timeout": 3,
    "radius-ses-timeout-act": "hard-timeout",
    "auth-blackout-time": 0,
    "auth-invalid-max": 5,
    "auth-lockout-threshold": 3,
    "auth-lockout-duration": 0,
    "per-policy-disclaimer": "disable",
    "auth-ssl-min-proto-version": "default",
    "auth-ssl-max-proto-version": "",
    "auth-ssl-sigalgs": "all",
    "default-user-password-policy": "",
    "cors": "disable",
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
    "auth-type": "option",  # Supported firewall policy authentication protocols/methods.
    "auth-cert": "string",  # HTTPS server certificate for policy authentication.
    "auth-ca-cert": "string",  # HTTPS CA certificate for policy authentication.
    "auth-secure-http": "option",  # Enable/disable redirecting HTTP user authentication to more 
    "auth-http-basic": "option",  # Enable/disable use of HTTP basic authentication for identity
    "auth-ssl-allow-renegotiation": "option",  # Allow/forbid SSL re-negotiation for HTTPS authentication.
    "auth-src-mac": "option",  # Enable/disable source MAC for user identity.
    "auth-on-demand": "option",  # Always/implicitly trigger firewall authentication on demand.
    "auth-timeout": "integer",  # Time in minutes before the firewall user authentication time
    "auth-timeout-type": "option",  # Control if authenticated users have to login again after a h
    "auth-portal-timeout": "integer",  # Time in minutes before captive portal user have to re-authen
    "radius-ses-timeout-act": "option",  # Set the RADIUS session timeout to a hard timeout or to ignor
    "auth-blackout-time": "integer",  # Time in seconds an IP address is denied access after failing
    "auth-invalid-max": "integer",  # Maximum number of failed authentication attempts before the 
    "auth-lockout-threshold": "integer",  # Maximum number of failed login attempts before login lockout
    "auth-lockout-duration": "integer",  # Lockout period in seconds after too many login failures.
    "per-policy-disclaimer": "option",  # Enable/disable per policy disclaimer.
    "auth-ports": "string",  # Set up non-standard ports for authentication with HTTP, HTTP
    "auth-ssl-min-proto-version": "option",  # Minimum supported protocol version for SSL/TLS connections (
    "auth-ssl-max-proto-version": "option",  # Maximum supported protocol version for SSL/TLS connections (
    "auth-ssl-sigalgs": "option",  # Set signature algorithms related to HTTPS authentication (af
    "default-user-password-policy": "string",  # Default password policy to apply to all local users unless o
    "cors": "option",  # Enable/disable allowed origins white list for CORS.
    "cors-allowed-origins": "string",  # Allowed origins white list for CORS.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "auth-type": "Supported firewall policy authentication protocols/methods.",
    "auth-cert": "HTTPS server certificate for policy authentication.",
    "auth-ca-cert": "HTTPS CA certificate for policy authentication.",
    "auth-secure-http": "Enable/disable redirecting HTTP user authentication to more secure HTTPS.",
    "auth-http-basic": "Enable/disable use of HTTP basic authentication for identity-based firewall policies.",
    "auth-ssl-allow-renegotiation": "Allow/forbid SSL re-negotiation for HTTPS authentication.",
    "auth-src-mac": "Enable/disable source MAC for user identity.",
    "auth-on-demand": "Always/implicitly trigger firewall authentication on demand.",
    "auth-timeout": "Time in minutes before the firewall user authentication timeout requires the user to re-authenticate.",
    "auth-timeout-type": "Control if authenticated users have to login again after a hard timeout, after an idle timeout, or after a session timeout.",
    "auth-portal-timeout": "Time in minutes before captive portal user have to re-authenticate (1 - 30 min, default 3 min).",
    "radius-ses-timeout-act": "Set the RADIUS session timeout to a hard timeout or to ignore RADIUS server session timeouts.",
    "auth-blackout-time": "Time in seconds an IP address is denied access after failing to authenticate five times within one minute.",
    "auth-invalid-max": "Maximum number of failed authentication attempts before the user is blocked.",
    "auth-lockout-threshold": "Maximum number of failed login attempts before login lockout is triggered.",
    "auth-lockout-duration": "Lockout period in seconds after too many login failures.",
    "per-policy-disclaimer": "Enable/disable per policy disclaimer.",
    "auth-ports": "Set up non-standard ports for authentication with HTTP, HTTPS, FTP, and TELNET.",
    "auth-ssl-min-proto-version": "Minimum supported protocol version for SSL/TLS connections (default is to follow system global setting).",
    "auth-ssl-max-proto-version": "Maximum supported protocol version for SSL/TLS connections (default is no limit).",
    "auth-ssl-sigalgs": "Set signature algorithms related to HTTPS authentication (affects TLS version <= 1.2 only, default is to enable all).",
    "default-user-password-policy": "Default password policy to apply to all local users unless otherwise specified, as defined in config user password-policy.",
    "cors": "Enable/disable allowed origins white list for CORS.",
    "cors-allowed-origins": "Allowed origins white list for CORS.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "auth-cert": {"type": "string", "max_length": 35},
    "auth-ca-cert": {"type": "string", "max_length": 35},
    "auth-timeout": {"type": "integer", "min": 1, "max": 1440},
    "auth-portal-timeout": {"type": "integer", "min": 1, "max": 30},
    "auth-blackout-time": {"type": "integer", "min": 0, "max": 3600},
    "auth-invalid-max": {"type": "integer", "min": 1, "max": 100},
    "auth-lockout-threshold": {"type": "integer", "min": 1, "max": 10},
    "auth-lockout-duration": {"type": "integer", "min": 0, "max": 4294967295},
    "default-user-password-policy": {"type": "string", "max_length": 35},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "auth-ports": {
        "id": {
            "type": "integer",
            "help": "ID.",
            "required": True,
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "type": {
            "type": "option",
            "help": "Service type.",
            "default": "http",
            "options": ["http", "https", "ftp", "telnet"],
        },
        "port": {
            "type": "integer",
            "help": "Non-standard port for firewall user authentication.",
            "default": 1024,
            "min_value": 1,
            "max_value": 65535,
        },
    },
    "cors-allowed-origins": {
        "name": {
            "type": "string",
            "help": "Allowed origin for CORS.",
            "default": "",
            "max_length": 79,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_AUTH_TYPE = [
    "http",
    "https",
    "ftp",
    "telnet",
]
VALID_BODY_AUTH_SECURE_HTTP = [
    "enable",
    "disable",
]
VALID_BODY_AUTH_HTTP_BASIC = [
    "enable",
    "disable",
]
VALID_BODY_AUTH_SSL_ALLOW_RENEGOTIATION = [
    "enable",
    "disable",
]
VALID_BODY_AUTH_SRC_MAC = [
    "enable",
    "disable",
]
VALID_BODY_AUTH_ON_DEMAND = [
    "always",
    "implicitly",
]
VALID_BODY_AUTH_TIMEOUT_TYPE = [
    "idle-timeout",
    "hard-timeout",
    "new-session",
]
VALID_BODY_RADIUS_SES_TIMEOUT_ACT = [
    "hard-timeout",
    "ignore-timeout",
]
VALID_BODY_PER_POLICY_DISCLAIMER = [
    "enable",
    "disable",
]
VALID_BODY_AUTH_SSL_MIN_PROTO_VERSION = [
    "default",
    "SSLv3",
    "TLSv1",
    "TLSv1-1",
    "TLSv1-2",
    "TLSv1-3",
]
VALID_BODY_AUTH_SSL_MAX_PROTO_VERSION = [
    "sslv3",
    "tlsv1",
    "tlsv1-1",
    "tlsv1-2",
    "tlsv1-3",
]
VALID_BODY_AUTH_SSL_SIGALGS = [
    "no-rsa-pss",
    "all",
]
VALID_BODY_CORS = [
    "disable",
    "enable",
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_user_setting_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters for user/setting.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_user_setting_get()
        >>> assert is_valid == True
        
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_user_setting_get(
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
    Validate required fields for user/setting.

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


def validate_user_setting_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new user/setting object.

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
        >>> is_valid, error = validate_user_setting_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "auth-type": "http",  # Valid enum value
        ... }
        >>> is_valid, error = validate_user_setting_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["auth-type"] = "invalid-value"
        >>> is_valid, error = validate_user_setting_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_user_setting_post(payload)
        >>> assert is_valid == False
        >>> assert "Missing required field" in error
    """
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "auth-type" in payload:
        value = payload["auth-type"]
        if value not in VALID_BODY_AUTH_TYPE:
            desc = FIELD_DESCRIPTIONS.get("auth-type", "")
            error_msg = f"Invalid value for 'auth-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTH_TYPE)}"
            error_msg += f"\n  → Example: auth-type='{{ VALID_BODY_AUTH_TYPE[0] }}'"
            return (False, error_msg)
    if "auth-secure-http" in payload:
        value = payload["auth-secure-http"]
        if value not in VALID_BODY_AUTH_SECURE_HTTP:
            desc = FIELD_DESCRIPTIONS.get("auth-secure-http", "")
            error_msg = f"Invalid value for 'auth-secure-http': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTH_SECURE_HTTP)}"
            error_msg += f"\n  → Example: auth-secure-http='{{ VALID_BODY_AUTH_SECURE_HTTP[0] }}'"
            return (False, error_msg)
    if "auth-http-basic" in payload:
        value = payload["auth-http-basic"]
        if value not in VALID_BODY_AUTH_HTTP_BASIC:
            desc = FIELD_DESCRIPTIONS.get("auth-http-basic", "")
            error_msg = f"Invalid value for 'auth-http-basic': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTH_HTTP_BASIC)}"
            error_msg += f"\n  → Example: auth-http-basic='{{ VALID_BODY_AUTH_HTTP_BASIC[0] }}'"
            return (False, error_msg)
    if "auth-ssl-allow-renegotiation" in payload:
        value = payload["auth-ssl-allow-renegotiation"]
        if value not in VALID_BODY_AUTH_SSL_ALLOW_RENEGOTIATION:
            desc = FIELD_DESCRIPTIONS.get("auth-ssl-allow-renegotiation", "")
            error_msg = f"Invalid value for 'auth-ssl-allow-renegotiation': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTH_SSL_ALLOW_RENEGOTIATION)}"
            error_msg += f"\n  → Example: auth-ssl-allow-renegotiation='{{ VALID_BODY_AUTH_SSL_ALLOW_RENEGOTIATION[0] }}'"
            return (False, error_msg)
    if "auth-src-mac" in payload:
        value = payload["auth-src-mac"]
        if value not in VALID_BODY_AUTH_SRC_MAC:
            desc = FIELD_DESCRIPTIONS.get("auth-src-mac", "")
            error_msg = f"Invalid value for 'auth-src-mac': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTH_SRC_MAC)}"
            error_msg += f"\n  → Example: auth-src-mac='{{ VALID_BODY_AUTH_SRC_MAC[0] }}'"
            return (False, error_msg)
    if "auth-on-demand" in payload:
        value = payload["auth-on-demand"]
        if value not in VALID_BODY_AUTH_ON_DEMAND:
            desc = FIELD_DESCRIPTIONS.get("auth-on-demand", "")
            error_msg = f"Invalid value for 'auth-on-demand': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTH_ON_DEMAND)}"
            error_msg += f"\n  → Example: auth-on-demand='{{ VALID_BODY_AUTH_ON_DEMAND[0] }}'"
            return (False, error_msg)
    if "auth-timeout-type" in payload:
        value = payload["auth-timeout-type"]
        if value not in VALID_BODY_AUTH_TIMEOUT_TYPE:
            desc = FIELD_DESCRIPTIONS.get("auth-timeout-type", "")
            error_msg = f"Invalid value for 'auth-timeout-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTH_TIMEOUT_TYPE)}"
            error_msg += f"\n  → Example: auth-timeout-type='{{ VALID_BODY_AUTH_TIMEOUT_TYPE[0] }}'"
            return (False, error_msg)
    if "radius-ses-timeout-act" in payload:
        value = payload["radius-ses-timeout-act"]
        if value not in VALID_BODY_RADIUS_SES_TIMEOUT_ACT:
            desc = FIELD_DESCRIPTIONS.get("radius-ses-timeout-act", "")
            error_msg = f"Invalid value for 'radius-ses-timeout-act': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_RADIUS_SES_TIMEOUT_ACT)}"
            error_msg += f"\n  → Example: radius-ses-timeout-act='{{ VALID_BODY_RADIUS_SES_TIMEOUT_ACT[0] }}'"
            return (False, error_msg)
    if "per-policy-disclaimer" in payload:
        value = payload["per-policy-disclaimer"]
        if value not in VALID_BODY_PER_POLICY_DISCLAIMER:
            desc = FIELD_DESCRIPTIONS.get("per-policy-disclaimer", "")
            error_msg = f"Invalid value for 'per-policy-disclaimer': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PER_POLICY_DISCLAIMER)}"
            error_msg += f"\n  → Example: per-policy-disclaimer='{{ VALID_BODY_PER_POLICY_DISCLAIMER[0] }}'"
            return (False, error_msg)
    if "auth-ssl-min-proto-version" in payload:
        value = payload["auth-ssl-min-proto-version"]
        if value not in VALID_BODY_AUTH_SSL_MIN_PROTO_VERSION:
            desc = FIELD_DESCRIPTIONS.get("auth-ssl-min-proto-version", "")
            error_msg = f"Invalid value for 'auth-ssl-min-proto-version': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTH_SSL_MIN_PROTO_VERSION)}"
            error_msg += f"\n  → Example: auth-ssl-min-proto-version='{{ VALID_BODY_AUTH_SSL_MIN_PROTO_VERSION[0] }}'"
            return (False, error_msg)
    if "auth-ssl-max-proto-version" in payload:
        value = payload["auth-ssl-max-proto-version"]
        if value not in VALID_BODY_AUTH_SSL_MAX_PROTO_VERSION:
            desc = FIELD_DESCRIPTIONS.get("auth-ssl-max-proto-version", "")
            error_msg = f"Invalid value for 'auth-ssl-max-proto-version': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTH_SSL_MAX_PROTO_VERSION)}"
            error_msg += f"\n  → Example: auth-ssl-max-proto-version='{{ VALID_BODY_AUTH_SSL_MAX_PROTO_VERSION[0] }}'"
            return (False, error_msg)
    if "auth-ssl-sigalgs" in payload:
        value = payload["auth-ssl-sigalgs"]
        if value not in VALID_BODY_AUTH_SSL_SIGALGS:
            desc = FIELD_DESCRIPTIONS.get("auth-ssl-sigalgs", "")
            error_msg = f"Invalid value for 'auth-ssl-sigalgs': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTH_SSL_SIGALGS)}"
            error_msg += f"\n  → Example: auth-ssl-sigalgs='{{ VALID_BODY_AUTH_SSL_SIGALGS[0] }}'"
            return (False, error_msg)
    if "cors" in payload:
        value = payload["cors"]
        if value not in VALID_BODY_CORS:
            desc = FIELD_DESCRIPTIONS.get("cors", "")
            error_msg = f"Invalid value for 'cors': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CORS)}"
            error_msg += f"\n  → Example: cors='{{ VALID_BODY_CORS[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_user_setting_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update user/setting.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_user_setting_put(payload)
    """
    # Step 1: Validate enum values
    if "auth-type" in payload:
        value = payload["auth-type"]
        if value not in VALID_BODY_AUTH_TYPE:
            return (
                False,
                f"Invalid value for 'auth-type'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_TYPE)}",
            )
    if "auth-secure-http" in payload:
        value = payload["auth-secure-http"]
        if value not in VALID_BODY_AUTH_SECURE_HTTP:
            return (
                False,
                f"Invalid value for 'auth-secure-http'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_SECURE_HTTP)}",
            )
    if "auth-http-basic" in payload:
        value = payload["auth-http-basic"]
        if value not in VALID_BODY_AUTH_HTTP_BASIC:
            return (
                False,
                f"Invalid value for 'auth-http-basic'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_HTTP_BASIC)}",
            )
    if "auth-ssl-allow-renegotiation" in payload:
        value = payload["auth-ssl-allow-renegotiation"]
        if value not in VALID_BODY_AUTH_SSL_ALLOW_RENEGOTIATION:
            return (
                False,
                f"Invalid value for 'auth-ssl-allow-renegotiation'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_SSL_ALLOW_RENEGOTIATION)}",
            )
    if "auth-src-mac" in payload:
        value = payload["auth-src-mac"]
        if value not in VALID_BODY_AUTH_SRC_MAC:
            return (
                False,
                f"Invalid value for 'auth-src-mac'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_SRC_MAC)}",
            )
    if "auth-on-demand" in payload:
        value = payload["auth-on-demand"]
        if value not in VALID_BODY_AUTH_ON_DEMAND:
            return (
                False,
                f"Invalid value for 'auth-on-demand'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_ON_DEMAND)}",
            )
    if "auth-timeout-type" in payload:
        value = payload["auth-timeout-type"]
        if value not in VALID_BODY_AUTH_TIMEOUT_TYPE:
            return (
                False,
                f"Invalid value for 'auth-timeout-type'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_TIMEOUT_TYPE)}",
            )
    if "radius-ses-timeout-act" in payload:
        value = payload["radius-ses-timeout-act"]
        if value not in VALID_BODY_RADIUS_SES_TIMEOUT_ACT:
            return (
                False,
                f"Invalid value for 'radius-ses-timeout-act'='{value}'. Must be one of: {', '.join(VALID_BODY_RADIUS_SES_TIMEOUT_ACT)}",
            )
    if "per-policy-disclaimer" in payload:
        value = payload["per-policy-disclaimer"]
        if value not in VALID_BODY_PER_POLICY_DISCLAIMER:
            return (
                False,
                f"Invalid value for 'per-policy-disclaimer'='{value}'. Must be one of: {', '.join(VALID_BODY_PER_POLICY_DISCLAIMER)}",
            )
    if "auth-ssl-min-proto-version" in payload:
        value = payload["auth-ssl-min-proto-version"]
        if value not in VALID_BODY_AUTH_SSL_MIN_PROTO_VERSION:
            return (
                False,
                f"Invalid value for 'auth-ssl-min-proto-version'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_SSL_MIN_PROTO_VERSION)}",
            )
    if "auth-ssl-max-proto-version" in payload:
        value = payload["auth-ssl-max-proto-version"]
        if value not in VALID_BODY_AUTH_SSL_MAX_PROTO_VERSION:
            return (
                False,
                f"Invalid value for 'auth-ssl-max-proto-version'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_SSL_MAX_PROTO_VERSION)}",
            )
    if "auth-ssl-sigalgs" in payload:
        value = payload["auth-ssl-sigalgs"]
        if value not in VALID_BODY_AUTH_SSL_SIGALGS:
            return (
                False,
                f"Invalid value for 'auth-ssl-sigalgs'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_SSL_SIGALGS)}",
            )
    if "cors" in payload:
        value = payload["cors"]
        if value not in VALID_BODY_CORS:
            return (
                False,
                f"Invalid value for 'cors'='{value}'. Must be one of: {', '.join(VALID_BODY_CORS)}",
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
    "endpoint": "user/setting",
    "category": "cmdb",
    "api_path": "user/setting",
    "help": "Configure user authentication setting.",
    "total_fields": 24,
    "required_fields_count": 0,
    "fields_with_defaults_count": 22,
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
