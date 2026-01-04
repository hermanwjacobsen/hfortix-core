"""
Validation helpers for user/ldap endpoint.

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
    "server",  # LDAP server CN domain name or IP.
    "dn",  # Distinguished name used to look up entries on the LDAP server.
    "username",  # Username (full DN) for initial binding.
    "interface",  # Specify outgoing interface to reach server.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "server": "",
    "secondary-server": "",
    "tertiary-server": "",
    "status-ttl": 300,
    "server-identity-check": "enable",
    "source-ip": "",
    "source-ip-interface": "",
    "source-port": 0,
    "cnid": "cn",
    "dn": "",
    "type": "simple",
    "two-factor": "disable",
    "two-factor-authentication": "",
    "two-factor-notification": "",
    "two-factor-filter": "",
    "username": "",
    "group-member-check": "user-attr",
    "group-search-base": "",
    "group-object-filter": "(\u0026(objectcategory=group)(member=*))",
    "group-filter": "",
    "secure": "disable",
    "ssl-min-proto-version": "default",
    "ca-cert": "",
    "port": 389,
    "password-expiry-warning": "disable",
    "password-renewal": "disable",
    "member-attr": "memberOf",
    "account-key-processing": "same",
    "account-key-cert-field": "othername",
    "account-key-filter": "(\u0026(userPrincipalName=%s)(!(UserAccountControl:1.2.840.113556.1.4.803:=2)))",
    "search-type": "",
    "client-cert-auth": "disable",
    "client-cert": "",
    "obtain-user-info": "enable",
    "user-info-exchange-server": "",
    "interface-select-method": "auto",
    "interface": "",
    "vrf-select": 0,
    "antiphish": "disable",
    "password-attr": "userPassword",
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
    "name": "string",  # LDAP server entry name.
    "server": "string",  # LDAP server CN domain name or IP.
    "secondary-server": "string",  # Secondary LDAP server CN domain name or IP.
    "tertiary-server": "string",  # Tertiary LDAP server CN domain name or IP.
    "status-ttl": "integer",  # Time for which server reachability is cached so that when a 
    "server-identity-check": "option",  # Enable/disable LDAP server identity check (verify server dom
    "source-ip": "string",  # FortiGate IP address to be used for communication with the L
    "source-ip-interface": "string",  # Source interface for communication with the LDAP server.
    "source-port": "integer",  # Source port to be used for communication with the LDAP serve
    "cnid": "string",  # Common name identifier for the LDAP server. The common name 
    "dn": "string",  # Distinguished name used to look up entries on the LDAP serve
    "type": "option",  # Authentication type for LDAP searches.
    "two-factor": "option",  # Enable/disable two-factor authentication.
    "two-factor-authentication": "option",  # Authentication method by FortiToken Cloud.
    "two-factor-notification": "option",  # Notification method for user activation by FortiToken Cloud.
    "two-factor-filter": "string",  # Filter used to synchronize users to FortiToken Cloud.
    "username": "string",  # Username (full DN) for initial binding.
    "password": "password",  # Password for initial binding.
    "group-member-check": "option",  # Group member checking methods.
    "group-search-base": "string",  # Search base used for group searching.
    "group-object-filter": "string",  # Filter used for group searching.
    "group-filter": "string",  # Filter used for group matching.
    "secure": "option",  # Port to be used for authentication.
    "ssl-min-proto-version": "option",  # Minimum supported protocol version for SSL/TLS connections (
    "ca-cert": "string",  # CA certificate name.
    "port": "integer",  # Port to be used for communication with the LDAP server (defa
    "password-expiry-warning": "option",  # Enable/disable password expiry warnings.
    "password-renewal": "option",  # Enable/disable online password renewal.
    "member-attr": "string",  # Name of attribute from which to get group membership.
    "account-key-processing": "option",  # Account key processing operation. The FortiGate will keep ei
    "account-key-cert-field": "option",  # Define subject identity field in certificate for user access
    "account-key-filter": "string",  # Account key filter, using the UPN as the search filter.
    "search-type": "option",  # Search type.
    "client-cert-auth": "option",  # Enable/disable using client certificate for TLS authenticati
    "client-cert": "string",  # Client certificate name.
    "obtain-user-info": "option",  # Enable/disable obtaining of user information.
    "user-info-exchange-server": "string",  # MS Exchange server from which to fetch user information.
    "interface-select-method": "option",  # Specify how to select outgoing interface to reach server.
    "interface": "string",  # Specify outgoing interface to reach server.
    "vrf-select": "integer",  # VRF ID used for connection to server.
    "antiphish": "option",  # Enable/disable AntiPhishing credential backend.
    "password-attr": "string",  # Name of attribute to get password hash.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "LDAP server entry name.",
    "server": "LDAP server CN domain name or IP.",
    "secondary-server": "Secondary LDAP server CN domain name or IP.",
    "tertiary-server": "Tertiary LDAP server CN domain name or IP.",
    "status-ttl": "Time for which server reachability is cached so that when a server is unreachable, it will not be retried for at least this period of time (0 = cache disabled, default = 300).",
    "server-identity-check": "Enable/disable LDAP server identity check (verify server domain name/IP address against the server certificate).",
    "source-ip": "FortiGate IP address to be used for communication with the LDAP server.",
    "source-ip-interface": "Source interface for communication with the LDAP server.",
    "source-port": "Source port to be used for communication with the LDAP server.",
    "cnid": "Common name identifier for the LDAP server. The common name identifier for most LDAP servers is \"cn\".",
    "dn": "Distinguished name used to look up entries on the LDAP server.",
    "type": "Authentication type for LDAP searches.",
    "two-factor": "Enable/disable two-factor authentication.",
    "two-factor-authentication": "Authentication method by FortiToken Cloud.",
    "two-factor-notification": "Notification method for user activation by FortiToken Cloud.",
    "two-factor-filter": "Filter used to synchronize users to FortiToken Cloud.",
    "username": "Username (full DN) for initial binding.",
    "password": "Password for initial binding.",
    "group-member-check": "Group member checking methods.",
    "group-search-base": "Search base used for group searching.",
    "group-object-filter": "Filter used for group searching.",
    "group-filter": "Filter used for group matching.",
    "secure": "Port to be used for authentication.",
    "ssl-min-proto-version": "Minimum supported protocol version for SSL/TLS connections (default is to follow system global setting).",
    "ca-cert": "CA certificate name.",
    "port": "Port to be used for communication with the LDAP server (default = 389).",
    "password-expiry-warning": "Enable/disable password expiry warnings.",
    "password-renewal": "Enable/disable online password renewal.",
    "member-attr": "Name of attribute from which to get group membership.",
    "account-key-processing": "Account key processing operation. The FortiGate will keep either the whole domain or strip the domain from the subject identity.",
    "account-key-cert-field": "Define subject identity field in certificate for user access right checking.",
    "account-key-filter": "Account key filter, using the UPN as the search filter.",
    "search-type": "Search type.",
    "client-cert-auth": "Enable/disable using client certificate for TLS authentication.",
    "client-cert": "Client certificate name.",
    "obtain-user-info": "Enable/disable obtaining of user information.",
    "user-info-exchange-server": "MS Exchange server from which to fetch user information.",
    "interface-select-method": "Specify how to select outgoing interface to reach server.",
    "interface": "Specify outgoing interface to reach server.",
    "vrf-select": "VRF ID used for connection to server.",
    "antiphish": "Enable/disable AntiPhishing credential backend.",
    "password-attr": "Name of attribute to get password hash.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 35},
    "server": {"type": "string", "max_length": 63},
    "secondary-server": {"type": "string", "max_length": 63},
    "tertiary-server": {"type": "string", "max_length": 63},
    "status-ttl": {"type": "integer", "min": 0, "max": 600},
    "source-ip": {"type": "string", "max_length": 63},
    "source-ip-interface": {"type": "string", "max_length": 15},
    "source-port": {"type": "integer", "min": 0, "max": 65535},
    "cnid": {"type": "string", "max_length": 20},
    "dn": {"type": "string", "max_length": 511},
    "two-factor-filter": {"type": "string", "max_length": 2047},
    "username": {"type": "string", "max_length": 511},
    "group-search-base": {"type": "string", "max_length": 511},
    "group-object-filter": {"type": "string", "max_length": 2047},
    "group-filter": {"type": "string", "max_length": 2047},
    "ca-cert": {"type": "string", "max_length": 79},
    "port": {"type": "integer", "min": 1, "max": 65535},
    "member-attr": {"type": "string", "max_length": 63},
    "account-key-filter": {"type": "string", "max_length": 2047},
    "client-cert": {"type": "string", "max_length": 79},
    "user-info-exchange-server": {"type": "string", "max_length": 35},
    "interface": {"type": "string", "max_length": 15},
    "vrf-select": {"type": "integer", "min": 0, "max": 511},
    "password-attr": {"type": "string", "max_length": 35},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
}


# Valid enum values from API documentation
VALID_BODY_SERVER_IDENTITY_CHECK = [
    "enable",
    "disable",
]
VALID_BODY_TYPE = [
    "simple",
    "anonymous",
    "regular",
]
VALID_BODY_TWO_FACTOR = [
    "disable",
    "fortitoken-cloud",
]
VALID_BODY_TWO_FACTOR_AUTHENTICATION = [
    "fortitoken",
    "email",
    "sms",
]
VALID_BODY_TWO_FACTOR_NOTIFICATION = [
    "email",
    "sms",
]
VALID_BODY_GROUP_MEMBER_CHECK = [
    "user-attr",
    "group-object",
    "posix-group-object",
]
VALID_BODY_SECURE = [
    "disable",
    "starttls",
    "ldaps",
]
VALID_BODY_SSL_MIN_PROTO_VERSION = [
    "default",
    "SSLv3",
    "TLSv1",
    "TLSv1-1",
    "TLSv1-2",
    "TLSv1-3",
]
VALID_BODY_PASSWORD_EXPIRY_WARNING = [
    "enable",
    "disable",
]
VALID_BODY_PASSWORD_RENEWAL = [
    "enable",
    "disable",
]
VALID_BODY_ACCOUNT_KEY_PROCESSING = [
    "same",
    "strip",
]
VALID_BODY_ACCOUNT_KEY_CERT_FIELD = [
    "othername",
    "rfc822name",
    "dnsname",
    "cn",
]
VALID_BODY_SEARCH_TYPE = [
    "recursive",
]
VALID_BODY_CLIENT_CERT_AUTH = [
    "enable",
    "disable",
]
VALID_BODY_OBTAIN_USER_INFO = [
    "enable",
    "disable",
]
VALID_BODY_INTERFACE_SELECT_METHOD = [
    "auto",
    "sdwan",
    "specify",
]
VALID_BODY_ANTIPHISH = [
    "enable",
    "disable",
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_user_ldap_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters for user/ldap.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_user_ldap_get()
        >>> assert is_valid == True
        
        >>> # Valid - Get specific item by name
        >>> is_valid, error = validate_user_ldap_get(name="test-item")
        >>> assert is_valid == True
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_user_ldap_get(
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
    Validate required fields for user/ldap.

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


def validate_user_ldap_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new user/ldap object.

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
        ...     "server": True,  # LDAP server CN domain name or IP.
        ...     "dn": True,  # Distinguished name used to look up entries on the 
        ... }
        >>> is_valid, error = validate_user_ldap_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "server": True,
        ...     "server-identity-check": "enable",  # Valid enum value
        ... }
        >>> is_valid, error = validate_user_ldap_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["server-identity-check"] = "invalid-value"
        >>> is_valid, error = validate_user_ldap_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_user_ldap_post(payload)
        >>> assert is_valid == False
        >>> assert "Missing required field" in error
    """
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "server-identity-check" in payload:
        value = payload["server-identity-check"]
        if value not in VALID_BODY_SERVER_IDENTITY_CHECK:
            desc = FIELD_DESCRIPTIONS.get("server-identity-check", "")
            error_msg = f"Invalid value for 'server-identity-check': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SERVER_IDENTITY_CHECK)}"
            error_msg += f"\n  → Example: server-identity-check='{{ VALID_BODY_SERVER_IDENTITY_CHECK[0] }}'"
            return (False, error_msg)
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
    if "two-factor" in payload:
        value = payload["two-factor"]
        if value not in VALID_BODY_TWO_FACTOR:
            desc = FIELD_DESCRIPTIONS.get("two-factor", "")
            error_msg = f"Invalid value for 'two-factor': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_TWO_FACTOR)}"
            error_msg += f"\n  → Example: two-factor='{{ VALID_BODY_TWO_FACTOR[0] }}'"
            return (False, error_msg)
    if "two-factor-authentication" in payload:
        value = payload["two-factor-authentication"]
        if value not in VALID_BODY_TWO_FACTOR_AUTHENTICATION:
            desc = FIELD_DESCRIPTIONS.get("two-factor-authentication", "")
            error_msg = f"Invalid value for 'two-factor-authentication': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_TWO_FACTOR_AUTHENTICATION)}"
            error_msg += f"\n  → Example: two-factor-authentication='{{ VALID_BODY_TWO_FACTOR_AUTHENTICATION[0] }}'"
            return (False, error_msg)
    if "two-factor-notification" in payload:
        value = payload["two-factor-notification"]
        if value not in VALID_BODY_TWO_FACTOR_NOTIFICATION:
            desc = FIELD_DESCRIPTIONS.get("two-factor-notification", "")
            error_msg = f"Invalid value for 'two-factor-notification': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_TWO_FACTOR_NOTIFICATION)}"
            error_msg += f"\n  → Example: two-factor-notification='{{ VALID_BODY_TWO_FACTOR_NOTIFICATION[0] }}'"
            return (False, error_msg)
    if "group-member-check" in payload:
        value = payload["group-member-check"]
        if value not in VALID_BODY_GROUP_MEMBER_CHECK:
            desc = FIELD_DESCRIPTIONS.get("group-member-check", "")
            error_msg = f"Invalid value for 'group-member-check': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GROUP_MEMBER_CHECK)}"
            error_msg += f"\n  → Example: group-member-check='{{ VALID_BODY_GROUP_MEMBER_CHECK[0] }}'"
            return (False, error_msg)
    if "secure" in payload:
        value = payload["secure"]
        if value not in VALID_BODY_SECURE:
            desc = FIELD_DESCRIPTIONS.get("secure", "")
            error_msg = f"Invalid value for 'secure': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SECURE)}"
            error_msg += f"\n  → Example: secure='{{ VALID_BODY_SECURE[0] }}'"
            return (False, error_msg)
    if "ssl-min-proto-version" in payload:
        value = payload["ssl-min-proto-version"]
        if value not in VALID_BODY_SSL_MIN_PROTO_VERSION:
            desc = FIELD_DESCRIPTIONS.get("ssl-min-proto-version", "")
            error_msg = f"Invalid value for 'ssl-min-proto-version': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SSL_MIN_PROTO_VERSION)}"
            error_msg += f"\n  → Example: ssl-min-proto-version='{{ VALID_BODY_SSL_MIN_PROTO_VERSION[0] }}'"
            return (False, error_msg)
    if "password-expiry-warning" in payload:
        value = payload["password-expiry-warning"]
        if value not in VALID_BODY_PASSWORD_EXPIRY_WARNING:
            desc = FIELD_DESCRIPTIONS.get("password-expiry-warning", "")
            error_msg = f"Invalid value for 'password-expiry-warning': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PASSWORD_EXPIRY_WARNING)}"
            error_msg += f"\n  → Example: password-expiry-warning='{{ VALID_BODY_PASSWORD_EXPIRY_WARNING[0] }}'"
            return (False, error_msg)
    if "password-renewal" in payload:
        value = payload["password-renewal"]
        if value not in VALID_BODY_PASSWORD_RENEWAL:
            desc = FIELD_DESCRIPTIONS.get("password-renewal", "")
            error_msg = f"Invalid value for 'password-renewal': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PASSWORD_RENEWAL)}"
            error_msg += f"\n  → Example: password-renewal='{{ VALID_BODY_PASSWORD_RENEWAL[0] }}'"
            return (False, error_msg)
    if "account-key-processing" in payload:
        value = payload["account-key-processing"]
        if value not in VALID_BODY_ACCOUNT_KEY_PROCESSING:
            desc = FIELD_DESCRIPTIONS.get("account-key-processing", "")
            error_msg = f"Invalid value for 'account-key-processing': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ACCOUNT_KEY_PROCESSING)}"
            error_msg += f"\n  → Example: account-key-processing='{{ VALID_BODY_ACCOUNT_KEY_PROCESSING[0] }}'"
            return (False, error_msg)
    if "account-key-cert-field" in payload:
        value = payload["account-key-cert-field"]
        if value not in VALID_BODY_ACCOUNT_KEY_CERT_FIELD:
            desc = FIELD_DESCRIPTIONS.get("account-key-cert-field", "")
            error_msg = f"Invalid value for 'account-key-cert-field': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ACCOUNT_KEY_CERT_FIELD)}"
            error_msg += f"\n  → Example: account-key-cert-field='{{ VALID_BODY_ACCOUNT_KEY_CERT_FIELD[0] }}'"
            return (False, error_msg)
    if "search-type" in payload:
        value = payload["search-type"]
        if value not in VALID_BODY_SEARCH_TYPE:
            desc = FIELD_DESCRIPTIONS.get("search-type", "")
            error_msg = f"Invalid value for 'search-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SEARCH_TYPE)}"
            error_msg += f"\n  → Example: search-type='{{ VALID_BODY_SEARCH_TYPE[0] }}'"
            return (False, error_msg)
    if "client-cert-auth" in payload:
        value = payload["client-cert-auth"]
        if value not in VALID_BODY_CLIENT_CERT_AUTH:
            desc = FIELD_DESCRIPTIONS.get("client-cert-auth", "")
            error_msg = f"Invalid value for 'client-cert-auth': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CLIENT_CERT_AUTH)}"
            error_msg += f"\n  → Example: client-cert-auth='{{ VALID_BODY_CLIENT_CERT_AUTH[0] }}'"
            return (False, error_msg)
    if "obtain-user-info" in payload:
        value = payload["obtain-user-info"]
        if value not in VALID_BODY_OBTAIN_USER_INFO:
            desc = FIELD_DESCRIPTIONS.get("obtain-user-info", "")
            error_msg = f"Invalid value for 'obtain-user-info': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_OBTAIN_USER_INFO)}"
            error_msg += f"\n  → Example: obtain-user-info='{{ VALID_BODY_OBTAIN_USER_INFO[0] }}'"
            return (False, error_msg)
    if "interface-select-method" in payload:
        value = payload["interface-select-method"]
        if value not in VALID_BODY_INTERFACE_SELECT_METHOD:
            desc = FIELD_DESCRIPTIONS.get("interface-select-method", "")
            error_msg = f"Invalid value for 'interface-select-method': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_INTERFACE_SELECT_METHOD)}"
            error_msg += f"\n  → Example: interface-select-method='{{ VALID_BODY_INTERFACE_SELECT_METHOD[0] }}'"
            return (False, error_msg)
    if "antiphish" in payload:
        value = payload["antiphish"]
        if value not in VALID_BODY_ANTIPHISH:
            desc = FIELD_DESCRIPTIONS.get("antiphish", "")
            error_msg = f"Invalid value for 'antiphish': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ANTIPHISH)}"
            error_msg += f"\n  → Example: antiphish='{{ VALID_BODY_ANTIPHISH[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_user_ldap_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update user/ldap.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_user_ldap_put(payload)
    """
    # Step 1: Validate enum values
    if "server-identity-check" in payload:
        value = payload["server-identity-check"]
        if value not in VALID_BODY_SERVER_IDENTITY_CHECK:
            return (
                False,
                f"Invalid value for 'server-identity-check'='{value}'. Must be one of: {', '.join(VALID_BODY_SERVER_IDENTITY_CHECK)}",
            )
    if "type" in payload:
        value = payload["type"]
        if value not in VALID_BODY_TYPE:
            return (
                False,
                f"Invalid value for 'type'='{value}'. Must be one of: {', '.join(VALID_BODY_TYPE)}",
            )
    if "two-factor" in payload:
        value = payload["two-factor"]
        if value not in VALID_BODY_TWO_FACTOR:
            return (
                False,
                f"Invalid value for 'two-factor'='{value}'. Must be one of: {', '.join(VALID_BODY_TWO_FACTOR)}",
            )
    if "two-factor-authentication" in payload:
        value = payload["two-factor-authentication"]
        if value not in VALID_BODY_TWO_FACTOR_AUTHENTICATION:
            return (
                False,
                f"Invalid value for 'two-factor-authentication'='{value}'. Must be one of: {', '.join(VALID_BODY_TWO_FACTOR_AUTHENTICATION)}",
            )
    if "two-factor-notification" in payload:
        value = payload["two-factor-notification"]
        if value not in VALID_BODY_TWO_FACTOR_NOTIFICATION:
            return (
                False,
                f"Invalid value for 'two-factor-notification'='{value}'. Must be one of: {', '.join(VALID_BODY_TWO_FACTOR_NOTIFICATION)}",
            )
    if "group-member-check" in payload:
        value = payload["group-member-check"]
        if value not in VALID_BODY_GROUP_MEMBER_CHECK:
            return (
                False,
                f"Invalid value for 'group-member-check'='{value}'. Must be one of: {', '.join(VALID_BODY_GROUP_MEMBER_CHECK)}",
            )
    if "secure" in payload:
        value = payload["secure"]
        if value not in VALID_BODY_SECURE:
            return (
                False,
                f"Invalid value for 'secure'='{value}'. Must be one of: {', '.join(VALID_BODY_SECURE)}",
            )
    if "ssl-min-proto-version" in payload:
        value = payload["ssl-min-proto-version"]
        if value not in VALID_BODY_SSL_MIN_PROTO_VERSION:
            return (
                False,
                f"Invalid value for 'ssl-min-proto-version'='{value}'. Must be one of: {', '.join(VALID_BODY_SSL_MIN_PROTO_VERSION)}",
            )
    if "password-expiry-warning" in payload:
        value = payload["password-expiry-warning"]
        if value not in VALID_BODY_PASSWORD_EXPIRY_WARNING:
            return (
                False,
                f"Invalid value for 'password-expiry-warning'='{value}'. Must be one of: {', '.join(VALID_BODY_PASSWORD_EXPIRY_WARNING)}",
            )
    if "password-renewal" in payload:
        value = payload["password-renewal"]
        if value not in VALID_BODY_PASSWORD_RENEWAL:
            return (
                False,
                f"Invalid value for 'password-renewal'='{value}'. Must be one of: {', '.join(VALID_BODY_PASSWORD_RENEWAL)}",
            )
    if "account-key-processing" in payload:
        value = payload["account-key-processing"]
        if value not in VALID_BODY_ACCOUNT_KEY_PROCESSING:
            return (
                False,
                f"Invalid value for 'account-key-processing'='{value}'. Must be one of: {', '.join(VALID_BODY_ACCOUNT_KEY_PROCESSING)}",
            )
    if "account-key-cert-field" in payload:
        value = payload["account-key-cert-field"]
        if value not in VALID_BODY_ACCOUNT_KEY_CERT_FIELD:
            return (
                False,
                f"Invalid value for 'account-key-cert-field'='{value}'. Must be one of: {', '.join(VALID_BODY_ACCOUNT_KEY_CERT_FIELD)}",
            )
    if "search-type" in payload:
        value = payload["search-type"]
        if value not in VALID_BODY_SEARCH_TYPE:
            return (
                False,
                f"Invalid value for 'search-type'='{value}'. Must be one of: {', '.join(VALID_BODY_SEARCH_TYPE)}",
            )
    if "client-cert-auth" in payload:
        value = payload["client-cert-auth"]
        if value not in VALID_BODY_CLIENT_CERT_AUTH:
            return (
                False,
                f"Invalid value for 'client-cert-auth'='{value}'. Must be one of: {', '.join(VALID_BODY_CLIENT_CERT_AUTH)}",
            )
    if "obtain-user-info" in payload:
        value = payload["obtain-user-info"]
        if value not in VALID_BODY_OBTAIN_USER_INFO:
            return (
                False,
                f"Invalid value for 'obtain-user-info'='{value}'. Must be one of: {', '.join(VALID_BODY_OBTAIN_USER_INFO)}",
            )
    if "interface-select-method" in payload:
        value = payload["interface-select-method"]
        if value not in VALID_BODY_INTERFACE_SELECT_METHOD:
            return (
                False,
                f"Invalid value for 'interface-select-method'='{value}'. Must be one of: {', '.join(VALID_BODY_INTERFACE_SELECT_METHOD)}",
            )
    if "antiphish" in payload:
        value = payload["antiphish"]
        if value not in VALID_BODY_ANTIPHISH:
            return (
                False,
                f"Invalid value for 'antiphish'='{value}'. Must be one of: {', '.join(VALID_BODY_ANTIPHISH)}",
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
    "endpoint": "user/ldap",
    "category": "cmdb",
    "api_path": "user/ldap",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure LDAP server entries.",
    "total_fields": 42,
    "required_fields_count": 4,
    "fields_with_defaults_count": 41,
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
