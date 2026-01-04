"""
Validation helpers for user/radius endpoint.

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
    "server",  # Primary RADIUS server CN domain name or IP address.
    "secret",  # Pre-shared secret key used to access the primary RADIUS server.
    "interface",  # Specify outgoing interface to reach server.
    "rsso-secret",  # RADIUS secret used by the RADIUS accounting server.
    "rsso-endpoint-block-attribute",  # RADIUS attributes used to block a user.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "server": "",
    "secondary-server": "",
    "tertiary-server": "",
    "timeout": 5,
    "status-ttl": 300,
    "all-usergroup": "disable",
    "use-management-vdom": "disable",
    "switch-controller-nas-ip-dynamic": "disable",
    "nas-ip": "0.0.0.0",
    "nas-id-type": "legacy",
    "call-station-id-type": "legacy",
    "nas-id": "",
    "acct-interim-interval": 0,
    "radius-coa": "disable",
    "radius-port": 0,
    "h3c-compatibility": "disable",
    "auth-type": "auto",
    "source-ip": "",
    "source-ip-interface": "",
    "username-case-sensitive": "disable",
    "group-override-attr-type": "",
    "password-renewal": "enable",
    "require-message-authenticator": "enable",
    "password-encoding": "auto",
    "mac-username-delimiter": "hyphen",
    "mac-password-delimiter": "hyphen",
    "mac-case": "lowercase",
    "acct-all-servers": "disable",
    "switch-controller-acct-fast-framedip-detect": 2,
    "interface-select-method": "auto",
    "interface": "",
    "vrf-select": 0,
    "switch-controller-service-type": "",
    "transport-protocol": "udp",
    "tls-min-proto-version": "default",
    "ca-cert": "",
    "client-cert": "",
    "server-identity-check": "enable",
    "account-key-processing": "same",
    "account-key-cert-field": "othername",
    "rsso": "disable",
    "rsso-radius-server-port": 1813,
    "rsso-radius-response": "disable",
    "rsso-validate-request-secret": "disable",
    "rsso-endpoint-attribute": "Calling-Station-Id",
    "rsso-endpoint-block-attribute": "",
    "sso-attribute": "Class",
    "sso-attribute-key": "",
    "sso-attribute-value-override": "enable",
    "rsso-context-timeout": 28800,
    "rsso-log-period": 0,
    "rsso-log-flags": "protocol-error profile-missing accounting-stop-missed accounting-event endpoint-block radiusd-other",
    "rsso-flush-ip-session": "disable",
    "rsso-ep-one-ip-only": "disable",
    "delimiter": "plus",
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
    "name": "string",  # RADIUS server entry name.
    "server": "string",  # Primary RADIUS server CN domain name or IP address.
    "secret": "password",  # Pre-shared secret key used to access the primary RADIUS serv
    "secondary-server": "string",  # Secondary RADIUS CN domain name or IP address.
    "secondary-secret": "password",  # Secret key to access the secondary server.
    "tertiary-server": "string",  # Tertiary RADIUS CN domain name or IP address.
    "tertiary-secret": "password",  # Secret key to access the tertiary server.
    "timeout": "integer",  # Time in seconds to retry connecting server.
    "status-ttl": "integer",  # Time for which server reachability is cached so that when a 
    "all-usergroup": "option",  # Enable/disable automatically including this RADIUS server in
    "use-management-vdom": "option",  # Enable/disable using management VDOM to send requests.
    "switch-controller-nas-ip-dynamic": "option",  # Enable/Disable switch-controller nas-ip dynamic to dynamical
    "nas-ip": "ipv4-address",  # IP address used to communicate with the RADIUS server and us
    "nas-id-type": "option",  # NAS identifier type configuration (default = legacy).
    "call-station-id-type": "option",  # Calling & Called station identifier type configuration (defa
    "nas-id": "string",  # Custom NAS identifier.
    "acct-interim-interval": "integer",  # Time in seconds between each accounting interim update messa
    "radius-coa": "option",  # Enable to allow a mechanism to change the attributes of an a
    "radius-port": "integer",  # RADIUS service port number.
    "h3c-compatibility": "option",  # Enable/disable compatibility with the H3C, a mechanism that 
    "auth-type": "option",  # Authentication methods/protocols permitted for this RADIUS s
    "source-ip": "string",  # Source IP address for communications to the RADIUS server.
    "source-ip-interface": "string",  # Source interface for communication with the RADIUS server.
    "username-case-sensitive": "option",  # Enable/disable case sensitive user names.
    "group-override-attr-type": "option",  # RADIUS attribute type to override user group information.
    "class": "string",  # Class attribute name(s).
    "password-renewal": "option",  # Enable/disable password renewal.
    "require-message-authenticator": "option",  # Require message authenticator in authentication response.
    "password-encoding": "option",  # Password encoding.
    "mac-username-delimiter": "option",  # MAC authentication username delimiter (default = hyphen).
    "mac-password-delimiter": "option",  # MAC authentication password delimiter (default = hyphen).
    "mac-case": "option",  # MAC authentication case (default = lowercase).
    "acct-all-servers": "option",  # Enable/disable sending of accounting messages to all configu
    "switch-controller-acct-fast-framedip-detect": "integer",  # Switch controller accounting message Framed-IP detection fro
    "interface-select-method": "option",  # Specify how to select outgoing interface to reach server.
    "interface": "string",  # Specify outgoing interface to reach server.
    "vrf-select": "integer",  # VRF ID used for connection to server.
    "switch-controller-service-type": "option",  # RADIUS service type.
    "transport-protocol": "option",  # Transport protocol to be used (default = udp).
    "tls-min-proto-version": "option",  # Minimum supported protocol version for TLS connections (defa
    "ca-cert": "string",  # CA of server to trust under TLS.
    "client-cert": "string",  # Client certificate to use under TLS.
    "server-identity-check": "option",  # Enable/disable RADIUS server identity check (verify server d
    "account-key-processing": "option",  # Account key processing operation. The FortiGate will keep ei
    "account-key-cert-field": "option",  # Define subject identity field in certificate for user access
    "rsso": "option",  # Enable/disable RADIUS based single sign on feature.
    "rsso-radius-server-port": "integer",  # UDP port to listen on for RADIUS Start and Stop records.
    "rsso-radius-response": "option",  # Enable/disable sending RADIUS response packets after receivi
    "rsso-validate-request-secret": "option",  # Enable/disable validating the RADIUS request shared secret i
    "rsso-secret": "password",  # RADIUS secret used by the RADIUS accounting server.
    "rsso-endpoint-attribute": "option",  # RADIUS attributes used to extract the user end point identif
    "rsso-endpoint-block-attribute": "option",  # RADIUS attributes used to block a user.
    "sso-attribute": "option",  # RADIUS attribute that contains the profile group name to be 
    "sso-attribute-key": "string",  # Key prefix for SSO group value in the SSO attribute.
    "sso-attribute-value-override": "option",  # Enable/disable override old attribute value with new value f
    "rsso-context-timeout": "integer",  # Time in seconds before the logged out user is removed from t
    "rsso-log-period": "integer",  # Time interval in seconds that group event log messages will 
    "rsso-log-flags": "option",  # Events to log.
    "rsso-flush-ip-session": "option",  # Enable/disable flushing user IP sessions on RADIUS accountin
    "rsso-ep-one-ip-only": "option",  # Enable/disable the replacement of old IP addresses with new 
    "delimiter": "option",  # Configure delimiter to be used for separating profile group 
    "accounting-server": "string",  # Additional accounting servers.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "RADIUS server entry name.",
    "server": "Primary RADIUS server CN domain name or IP address.",
    "secret": "Pre-shared secret key used to access the primary RADIUS server.",
    "secondary-server": "Secondary RADIUS CN domain name or IP address.",
    "secondary-secret": "Secret key to access the secondary server.",
    "tertiary-server": "Tertiary RADIUS CN domain name or IP address.",
    "tertiary-secret": "Secret key to access the tertiary server.",
    "timeout": "Time in seconds to retry connecting server.",
    "status-ttl": "Time for which server reachability is cached so that when a server is unreachable, it will not be retried for at least this period of time (0 = cache disabled, default = 300).",
    "all-usergroup": "Enable/disable automatically including this RADIUS server in all user groups.",
    "use-management-vdom": "Enable/disable using management VDOM to send requests.",
    "switch-controller-nas-ip-dynamic": "Enable/Disable switch-controller nas-ip dynamic to dynamically set nas-ip.",
    "nas-ip": "IP address used to communicate with the RADIUS server and used as NAS-IP-Address and Called-Station-ID attributes.",
    "nas-id-type": "NAS identifier type configuration (default = legacy).",
    "call-station-id-type": "Calling & Called station identifier type configuration (default = legacy), this option is not available for 802.1x authentication. ",
    "nas-id": "Custom NAS identifier.",
    "acct-interim-interval": "Time in seconds between each accounting interim update message.",
    "radius-coa": "Enable to allow a mechanism to change the attributes of an authentication, authorization, and accounting session after it is authenticated.",
    "radius-port": "RADIUS service port number.",
    "h3c-compatibility": "Enable/disable compatibility with the H3C, a mechanism that performs security checking for authentication.",
    "auth-type": "Authentication methods/protocols permitted for this RADIUS server.",
    "source-ip": "Source IP address for communications to the RADIUS server.",
    "source-ip-interface": "Source interface for communication with the RADIUS server.",
    "username-case-sensitive": "Enable/disable case sensitive user names.",
    "group-override-attr-type": "RADIUS attribute type to override user group information.",
    "class": "Class attribute name(s).",
    "password-renewal": "Enable/disable password renewal.",
    "require-message-authenticator": "Require message authenticator in authentication response.",
    "password-encoding": "Password encoding.",
    "mac-username-delimiter": "MAC authentication username delimiter (default = hyphen).",
    "mac-password-delimiter": "MAC authentication password delimiter (default = hyphen).",
    "mac-case": "MAC authentication case (default = lowercase).",
    "acct-all-servers": "Enable/disable sending of accounting messages to all configured servers (default = disable).",
    "switch-controller-acct-fast-framedip-detect": "Switch controller accounting message Framed-IP detection from DHCP snooping (seconds, default=2).",
    "interface-select-method": "Specify how to select outgoing interface to reach server.",
    "interface": "Specify outgoing interface to reach server.",
    "vrf-select": "VRF ID used for connection to server.",
    "switch-controller-service-type": "RADIUS service type.",
    "transport-protocol": "Transport protocol to be used (default = udp).",
    "tls-min-proto-version": "Minimum supported protocol version for TLS connections (default is to follow system global setting).",
    "ca-cert": "CA of server to trust under TLS.",
    "client-cert": "Client certificate to use under TLS.",
    "server-identity-check": "Enable/disable RADIUS server identity check (verify server domain name/IP address against the server certificate).",
    "account-key-processing": "Account key processing operation. The FortiGate will keep either the whole domain or strip the domain from the subject identity.",
    "account-key-cert-field": "Define subject identity field in certificate for user access right checking.",
    "rsso": "Enable/disable RADIUS based single sign on feature.",
    "rsso-radius-server-port": "UDP port to listen on for RADIUS Start and Stop records.",
    "rsso-radius-response": "Enable/disable sending RADIUS response packets after receiving Start and Stop records.",
    "rsso-validate-request-secret": "Enable/disable validating the RADIUS request shared secret in the Start or End record.",
    "rsso-secret": "RADIUS secret used by the RADIUS accounting server.",
    "rsso-endpoint-attribute": "RADIUS attributes used to extract the user end point identifier from the RADIUS Start record.",
    "rsso-endpoint-block-attribute": "RADIUS attributes used to block a user.",
    "sso-attribute": "RADIUS attribute that contains the profile group name to be extracted from the RADIUS Start record.",
    "sso-attribute-key": "Key prefix for SSO group value in the SSO attribute.",
    "sso-attribute-value-override": "Enable/disable override old attribute value with new value for the same endpoint.",
    "rsso-context-timeout": "Time in seconds before the logged out user is removed from the \"user context list\" of logged on users.",
    "rsso-log-period": "Time interval in seconds that group event log messages will be generated for dynamic profile events.",
    "rsso-log-flags": "Events to log.",
    "rsso-flush-ip-session": "Enable/disable flushing user IP sessions on RADIUS accounting Stop messages.",
    "rsso-ep-one-ip-only": "Enable/disable the replacement of old IP addresses with new ones for the same endpoint on RADIUS accounting Start messages.",
    "delimiter": "Configure delimiter to be used for separating profile group names in the SSO attribute (default = plus character \"+\").",
    "accounting-server": "Additional accounting servers.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 35},
    "server": {"type": "string", "max_length": 63},
    "secondary-server": {"type": "string", "max_length": 63},
    "tertiary-server": {"type": "string", "max_length": 63},
    "timeout": {"type": "integer", "min": 1, "max": 300},
    "status-ttl": {"type": "integer", "min": 0, "max": 600},
    "nas-id": {"type": "string", "max_length": 255},
    "acct-interim-interval": {"type": "integer", "min": 60, "max": 86400},
    "radius-port": {"type": "integer", "min": 0, "max": 65535},
    "source-ip": {"type": "string", "max_length": 63},
    "source-ip-interface": {"type": "string", "max_length": 15},
    "switch-controller-acct-fast-framedip-detect": {"type": "integer", "min": 2, "max": 600},
    "interface": {"type": "string", "max_length": 15},
    "vrf-select": {"type": "integer", "min": 0, "max": 511},
    "ca-cert": {"type": "string", "max_length": 79},
    "client-cert": {"type": "string", "max_length": 35},
    "rsso-radius-server-port": {"type": "integer", "min": 0, "max": 65535},
    "sso-attribute-key": {"type": "string", "max_length": 35},
    "rsso-context-timeout": {"type": "integer", "min": 0, "max": 4294967295},
    "rsso-log-period": {"type": "integer", "min": 0, "max": 4294967295},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "class": {
        "name": {
            "type": "string",
            "help": "Class name.",
            "default": "",
            "max_length": 79,
        },
    },
    "accounting-server": {
        "id": {
            "type": "integer",
            "help": "ID (0 - 4294967295).",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "status": {
            "type": "option",
            "help": "Status.",
            "default": "disable",
            "options": ["enable", "disable"],
        },
        "server": {
            "type": "string",
            "help": "Server CN domain name or IP address.",
            "required": True,
            "default": "",
            "max_length": 63,
        },
        "secret": {
            "type": "password",
            "help": "Secret key.",
            "required": True,
            "max_length": 128,
        },
        "port": {
            "type": "integer",
            "help": "RADIUS accounting port number.",
            "default": 0,
            "min_value": 0,
            "max_value": 65535,
        },
        "source-ip": {
            "type": "string",
            "help": "Source IP address for communications to the RADIUS server.",
            "default": "",
            "max_length": 63,
        },
        "interface-select-method": {
            "type": "option",
            "help": "Specify how to select outgoing interface to reach server.",
            "default": "auto",
            "options": ["auto", "sdwan", "specify"],
        },
        "interface": {
            "type": "string",
            "help": "Specify outgoing interface to reach server.",
            "required": True,
            "default": "",
            "max_length": 15,
        },
        "vrf-select": {
            "type": "integer",
            "help": "VRF ID used for connection to server.",
            "default": 0,
            "min_value": 0,
            "max_value": 511,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_ALL_USERGROUP = [
    "disable",
    "enable",
]
VALID_BODY_USE_MANAGEMENT_VDOM = [
    "enable",
    "disable",
]
VALID_BODY_SWITCH_CONTROLLER_NAS_IP_DYNAMIC = [
    "enable",
    "disable",
]
VALID_BODY_NAS_ID_TYPE = [
    "legacy",
    "custom",
    "hostname",
]
VALID_BODY_CALL_STATION_ID_TYPE = [
    "legacy",
    "IP",
    "MAC",
]
VALID_BODY_RADIUS_COA = [
    "enable",
    "disable",
]
VALID_BODY_H3C_COMPATIBILITY = [
    "enable",
    "disable",
]
VALID_BODY_AUTH_TYPE = [
    "auto",
    "ms_chap_v2",
    "ms_chap",
    "chap",
    "pap",
]
VALID_BODY_USERNAME_CASE_SENSITIVE = [
    "enable",
    "disable",
]
VALID_BODY_GROUP_OVERRIDE_ATTR_TYPE = [
    "filter-Id",
    "class",
]
VALID_BODY_PASSWORD_RENEWAL = [
    "enable",
    "disable",
]
VALID_BODY_REQUIRE_MESSAGE_AUTHENTICATOR = [
    "enable",
    "disable",
]
VALID_BODY_PASSWORD_ENCODING = [
    "auto",
    "ISO-8859-1",
]
VALID_BODY_MAC_USERNAME_DELIMITER = [
    "hyphen",
    "single-hyphen",
    "colon",
    "none",
]
VALID_BODY_MAC_PASSWORD_DELIMITER = [
    "hyphen",
    "single-hyphen",
    "colon",
    "none",
]
VALID_BODY_MAC_CASE = [
    "uppercase",
    "lowercase",
]
VALID_BODY_ACCT_ALL_SERVERS = [
    "enable",
    "disable",
]
VALID_BODY_INTERFACE_SELECT_METHOD = [
    "auto",
    "sdwan",
    "specify",
]
VALID_BODY_SWITCH_CONTROLLER_SERVICE_TYPE = [
    "login",
    "framed",
    "callback-login",
    "callback-framed",
    "outbound",
    "administrative",
    "nas-prompt",
    "authenticate-only",
    "callback-nas-prompt",
    "call-check",
    "callback-administrative",
]
VALID_BODY_TRANSPORT_PROTOCOL = [
    "udp",
    "tcp",
    "tls",
]
VALID_BODY_TLS_MIN_PROTO_VERSION = [
    "default",
    "SSLv3",
    "TLSv1",
    "TLSv1-1",
    "TLSv1-2",
    "TLSv1-3",
]
VALID_BODY_SERVER_IDENTITY_CHECK = [
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
VALID_BODY_RSSO = [
    "enable",
    "disable",
]
VALID_BODY_RSSO_RADIUS_RESPONSE = [
    "enable",
    "disable",
]
VALID_BODY_RSSO_VALIDATE_REQUEST_SECRET = [
    "enable",
    "disable",
]
VALID_BODY_RSSO_ENDPOINT_ATTRIBUTE = [
    "User-Name",
    "NAS-IP-Address",
    "Framed-IP-Address",
    "Framed-IP-Netmask",
    "Filter-Id",
    "Login-IP-Host",
    "Reply-Message",
    "Callback-Number",
    "Callback-Id",
    "Framed-Route",
    "Framed-IPX-Network",
    "Class",
    "Called-Station-Id",
    "Calling-Station-Id",
    "NAS-Identifier",
    "Proxy-State",
    "Login-LAT-Service",
    "Login-LAT-Node",
    "Login-LAT-Group",
    "Framed-AppleTalk-Zone",
    "Acct-Session-Id",
    "Acct-Multi-Session-Id",
]
VALID_BODY_RSSO_ENDPOINT_BLOCK_ATTRIBUTE = [
    "User-Name",
    "NAS-IP-Address",
    "Framed-IP-Address",
    "Framed-IP-Netmask",
    "Filter-Id",
    "Login-IP-Host",
    "Reply-Message",
    "Callback-Number",
    "Callback-Id",
    "Framed-Route",
    "Framed-IPX-Network",
    "Class",
    "Called-Station-Id",
    "Calling-Station-Id",
    "NAS-Identifier",
    "Proxy-State",
    "Login-LAT-Service",
    "Login-LAT-Node",
    "Login-LAT-Group",
    "Framed-AppleTalk-Zone",
    "Acct-Session-Id",
    "Acct-Multi-Session-Id",
]
VALID_BODY_SSO_ATTRIBUTE = [
    "User-Name",
    "NAS-IP-Address",
    "Framed-IP-Address",
    "Framed-IP-Netmask",
    "Filter-Id",
    "Login-IP-Host",
    "Reply-Message",
    "Callback-Number",
    "Callback-Id",
    "Framed-Route",
    "Framed-IPX-Network",
    "Class",
    "Called-Station-Id",
    "Calling-Station-Id",
    "NAS-Identifier",
    "Proxy-State",
    "Login-LAT-Service",
    "Login-LAT-Node",
    "Login-LAT-Group",
    "Framed-AppleTalk-Zone",
    "Acct-Session-Id",
    "Acct-Multi-Session-Id",
]
VALID_BODY_SSO_ATTRIBUTE_VALUE_OVERRIDE = [
    "enable",
    "disable",
]
VALID_BODY_RSSO_LOG_FLAGS = [
    "protocol-error",
    "profile-missing",
    "accounting-stop-missed",
    "accounting-event",
    "endpoint-block",
    "radiusd-other",
    "none",
]
VALID_BODY_RSSO_FLUSH_IP_SESSION = [
    "enable",
    "disable",
]
VALID_BODY_RSSO_EP_ONE_IP_ONLY = [
    "enable",
    "disable",
]
VALID_BODY_DELIMITER = [
    "plus",
    "comma",
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_user_radius_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters for user/radius.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_user_radius_get()
        >>> assert is_valid == True
        
        >>> # Valid - Get specific item by name
        >>> is_valid, error = validate_user_radius_get(name="test-item")
        >>> assert is_valid == True
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_user_radius_get(
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
    Validate required fields for user/radius.

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


def validate_user_radius_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new user/radius object.

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
        ...     "server": True,  # Primary RADIUS server CN domain name or IP address
        ...     "secret": True,  # Pre-shared secret key used to access the primary R
        ... }
        >>> is_valid, error = validate_user_radius_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "server": True,
        ...     "all-usergroup": "disable",  # Valid enum value
        ... }
        >>> is_valid, error = validate_user_radius_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["all-usergroup"] = "invalid-value"
        >>> is_valid, error = validate_user_radius_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_user_radius_post(payload)
        >>> assert is_valid == False
        >>> assert "Missing required field" in error
    """
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "all-usergroup" in payload:
        value = payload["all-usergroup"]
        if value not in VALID_BODY_ALL_USERGROUP:
            desc = FIELD_DESCRIPTIONS.get("all-usergroup", "")
            error_msg = f"Invalid value for 'all-usergroup': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ALL_USERGROUP)}"
            error_msg += f"\n  → Example: all-usergroup='{{ VALID_BODY_ALL_USERGROUP[0] }}'"
            return (False, error_msg)
    if "use-management-vdom" in payload:
        value = payload["use-management-vdom"]
        if value not in VALID_BODY_USE_MANAGEMENT_VDOM:
            desc = FIELD_DESCRIPTIONS.get("use-management-vdom", "")
            error_msg = f"Invalid value for 'use-management-vdom': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_USE_MANAGEMENT_VDOM)}"
            error_msg += f"\n  → Example: use-management-vdom='{{ VALID_BODY_USE_MANAGEMENT_VDOM[0] }}'"
            return (False, error_msg)
    if "switch-controller-nas-ip-dynamic" in payload:
        value = payload["switch-controller-nas-ip-dynamic"]
        if value not in VALID_BODY_SWITCH_CONTROLLER_NAS_IP_DYNAMIC:
            desc = FIELD_DESCRIPTIONS.get("switch-controller-nas-ip-dynamic", "")
            error_msg = f"Invalid value for 'switch-controller-nas-ip-dynamic': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SWITCH_CONTROLLER_NAS_IP_DYNAMIC)}"
            error_msg += f"\n  → Example: switch-controller-nas-ip-dynamic='{{ VALID_BODY_SWITCH_CONTROLLER_NAS_IP_DYNAMIC[0] }}'"
            return (False, error_msg)
    if "nas-id-type" in payload:
        value = payload["nas-id-type"]
        if value not in VALID_BODY_NAS_ID_TYPE:
            desc = FIELD_DESCRIPTIONS.get("nas-id-type", "")
            error_msg = f"Invalid value for 'nas-id-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_NAS_ID_TYPE)}"
            error_msg += f"\n  → Example: nas-id-type='{{ VALID_BODY_NAS_ID_TYPE[0] }}'"
            return (False, error_msg)
    if "call-station-id-type" in payload:
        value = payload["call-station-id-type"]
        if value not in VALID_BODY_CALL_STATION_ID_TYPE:
            desc = FIELD_DESCRIPTIONS.get("call-station-id-type", "")
            error_msg = f"Invalid value for 'call-station-id-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CALL_STATION_ID_TYPE)}"
            error_msg += f"\n  → Example: call-station-id-type='{{ VALID_BODY_CALL_STATION_ID_TYPE[0] }}'"
            return (False, error_msg)
    if "radius-coa" in payload:
        value = payload["radius-coa"]
        if value not in VALID_BODY_RADIUS_COA:
            desc = FIELD_DESCRIPTIONS.get("radius-coa", "")
            error_msg = f"Invalid value for 'radius-coa': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_RADIUS_COA)}"
            error_msg += f"\n  → Example: radius-coa='{{ VALID_BODY_RADIUS_COA[0] }}'"
            return (False, error_msg)
    if "h3c-compatibility" in payload:
        value = payload["h3c-compatibility"]
        if value not in VALID_BODY_H3C_COMPATIBILITY:
            desc = FIELD_DESCRIPTIONS.get("h3c-compatibility", "")
            error_msg = f"Invalid value for 'h3c-compatibility': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_H3C_COMPATIBILITY)}"
            error_msg += f"\n  → Example: h3c-compatibility='{{ VALID_BODY_H3C_COMPATIBILITY[0] }}'"
            return (False, error_msg)
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
    if "username-case-sensitive" in payload:
        value = payload["username-case-sensitive"]
        if value not in VALID_BODY_USERNAME_CASE_SENSITIVE:
            desc = FIELD_DESCRIPTIONS.get("username-case-sensitive", "")
            error_msg = f"Invalid value for 'username-case-sensitive': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_USERNAME_CASE_SENSITIVE)}"
            error_msg += f"\n  → Example: username-case-sensitive='{{ VALID_BODY_USERNAME_CASE_SENSITIVE[0] }}'"
            return (False, error_msg)
    if "group-override-attr-type" in payload:
        value = payload["group-override-attr-type"]
        if value not in VALID_BODY_GROUP_OVERRIDE_ATTR_TYPE:
            desc = FIELD_DESCRIPTIONS.get("group-override-attr-type", "")
            error_msg = f"Invalid value for 'group-override-attr-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GROUP_OVERRIDE_ATTR_TYPE)}"
            error_msg += f"\n  → Example: group-override-attr-type='{{ VALID_BODY_GROUP_OVERRIDE_ATTR_TYPE[0] }}'"
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
    if "require-message-authenticator" in payload:
        value = payload["require-message-authenticator"]
        if value not in VALID_BODY_REQUIRE_MESSAGE_AUTHENTICATOR:
            desc = FIELD_DESCRIPTIONS.get("require-message-authenticator", "")
            error_msg = f"Invalid value for 'require-message-authenticator': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_REQUIRE_MESSAGE_AUTHENTICATOR)}"
            error_msg += f"\n  → Example: require-message-authenticator='{{ VALID_BODY_REQUIRE_MESSAGE_AUTHENTICATOR[0] }}'"
            return (False, error_msg)
    if "password-encoding" in payload:
        value = payload["password-encoding"]
        if value not in VALID_BODY_PASSWORD_ENCODING:
            desc = FIELD_DESCRIPTIONS.get("password-encoding", "")
            error_msg = f"Invalid value for 'password-encoding': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PASSWORD_ENCODING)}"
            error_msg += f"\n  → Example: password-encoding='{{ VALID_BODY_PASSWORD_ENCODING[0] }}'"
            return (False, error_msg)
    if "mac-username-delimiter" in payload:
        value = payload["mac-username-delimiter"]
        if value not in VALID_BODY_MAC_USERNAME_DELIMITER:
            desc = FIELD_DESCRIPTIONS.get("mac-username-delimiter", "")
            error_msg = f"Invalid value for 'mac-username-delimiter': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MAC_USERNAME_DELIMITER)}"
            error_msg += f"\n  → Example: mac-username-delimiter='{{ VALID_BODY_MAC_USERNAME_DELIMITER[0] }}'"
            return (False, error_msg)
    if "mac-password-delimiter" in payload:
        value = payload["mac-password-delimiter"]
        if value not in VALID_BODY_MAC_PASSWORD_DELIMITER:
            desc = FIELD_DESCRIPTIONS.get("mac-password-delimiter", "")
            error_msg = f"Invalid value for 'mac-password-delimiter': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MAC_PASSWORD_DELIMITER)}"
            error_msg += f"\n  → Example: mac-password-delimiter='{{ VALID_BODY_MAC_PASSWORD_DELIMITER[0] }}'"
            return (False, error_msg)
    if "mac-case" in payload:
        value = payload["mac-case"]
        if value not in VALID_BODY_MAC_CASE:
            desc = FIELD_DESCRIPTIONS.get("mac-case", "")
            error_msg = f"Invalid value for 'mac-case': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MAC_CASE)}"
            error_msg += f"\n  → Example: mac-case='{{ VALID_BODY_MAC_CASE[0] }}'"
            return (False, error_msg)
    if "acct-all-servers" in payload:
        value = payload["acct-all-servers"]
        if value not in VALID_BODY_ACCT_ALL_SERVERS:
            desc = FIELD_DESCRIPTIONS.get("acct-all-servers", "")
            error_msg = f"Invalid value for 'acct-all-servers': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ACCT_ALL_SERVERS)}"
            error_msg += f"\n  → Example: acct-all-servers='{{ VALID_BODY_ACCT_ALL_SERVERS[0] }}'"
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
    if "switch-controller-service-type" in payload:
        value = payload["switch-controller-service-type"]
        if value not in VALID_BODY_SWITCH_CONTROLLER_SERVICE_TYPE:
            desc = FIELD_DESCRIPTIONS.get("switch-controller-service-type", "")
            error_msg = f"Invalid value for 'switch-controller-service-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SWITCH_CONTROLLER_SERVICE_TYPE)}"
            error_msg += f"\n  → Example: switch-controller-service-type='{{ VALID_BODY_SWITCH_CONTROLLER_SERVICE_TYPE[0] }}'"
            return (False, error_msg)
    if "transport-protocol" in payload:
        value = payload["transport-protocol"]
        if value not in VALID_BODY_TRANSPORT_PROTOCOL:
            desc = FIELD_DESCRIPTIONS.get("transport-protocol", "")
            error_msg = f"Invalid value for 'transport-protocol': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_TRANSPORT_PROTOCOL)}"
            error_msg += f"\n  → Example: transport-protocol='{{ VALID_BODY_TRANSPORT_PROTOCOL[0] }}'"
            return (False, error_msg)
    if "tls-min-proto-version" in payload:
        value = payload["tls-min-proto-version"]
        if value not in VALID_BODY_TLS_MIN_PROTO_VERSION:
            desc = FIELD_DESCRIPTIONS.get("tls-min-proto-version", "")
            error_msg = f"Invalid value for 'tls-min-proto-version': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_TLS_MIN_PROTO_VERSION)}"
            error_msg += f"\n  → Example: tls-min-proto-version='{{ VALID_BODY_TLS_MIN_PROTO_VERSION[0] }}'"
            return (False, error_msg)
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
    if "rsso" in payload:
        value = payload["rsso"]
        if value not in VALID_BODY_RSSO:
            desc = FIELD_DESCRIPTIONS.get("rsso", "")
            error_msg = f"Invalid value for 'rsso': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_RSSO)}"
            error_msg += f"\n  → Example: rsso='{{ VALID_BODY_RSSO[0] }}'"
            return (False, error_msg)
    if "rsso-radius-response" in payload:
        value = payload["rsso-radius-response"]
        if value not in VALID_BODY_RSSO_RADIUS_RESPONSE:
            desc = FIELD_DESCRIPTIONS.get("rsso-radius-response", "")
            error_msg = f"Invalid value for 'rsso-radius-response': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_RSSO_RADIUS_RESPONSE)}"
            error_msg += f"\n  → Example: rsso-radius-response='{{ VALID_BODY_RSSO_RADIUS_RESPONSE[0] }}'"
            return (False, error_msg)
    if "rsso-validate-request-secret" in payload:
        value = payload["rsso-validate-request-secret"]
        if value not in VALID_BODY_RSSO_VALIDATE_REQUEST_SECRET:
            desc = FIELD_DESCRIPTIONS.get("rsso-validate-request-secret", "")
            error_msg = f"Invalid value for 'rsso-validate-request-secret': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_RSSO_VALIDATE_REQUEST_SECRET)}"
            error_msg += f"\n  → Example: rsso-validate-request-secret='{{ VALID_BODY_RSSO_VALIDATE_REQUEST_SECRET[0] }}'"
            return (False, error_msg)
    if "rsso-endpoint-attribute" in payload:
        value = payload["rsso-endpoint-attribute"]
        if value not in VALID_BODY_RSSO_ENDPOINT_ATTRIBUTE:
            desc = FIELD_DESCRIPTIONS.get("rsso-endpoint-attribute", "")
            error_msg = f"Invalid value for 'rsso-endpoint-attribute': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_RSSO_ENDPOINT_ATTRIBUTE)}"
            error_msg += f"\n  → Example: rsso-endpoint-attribute='{{ VALID_BODY_RSSO_ENDPOINT_ATTRIBUTE[0] }}'"
            return (False, error_msg)
    if "rsso-endpoint-block-attribute" in payload:
        value = payload["rsso-endpoint-block-attribute"]
        if value not in VALID_BODY_RSSO_ENDPOINT_BLOCK_ATTRIBUTE:
            desc = FIELD_DESCRIPTIONS.get("rsso-endpoint-block-attribute", "")
            error_msg = f"Invalid value for 'rsso-endpoint-block-attribute': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_RSSO_ENDPOINT_BLOCK_ATTRIBUTE)}"
            error_msg += f"\n  → Example: rsso-endpoint-block-attribute='{{ VALID_BODY_RSSO_ENDPOINT_BLOCK_ATTRIBUTE[0] }}'"
            return (False, error_msg)
    if "sso-attribute" in payload:
        value = payload["sso-attribute"]
        if value not in VALID_BODY_SSO_ATTRIBUTE:
            desc = FIELD_DESCRIPTIONS.get("sso-attribute", "")
            error_msg = f"Invalid value for 'sso-attribute': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SSO_ATTRIBUTE)}"
            error_msg += f"\n  → Example: sso-attribute='{{ VALID_BODY_SSO_ATTRIBUTE[0] }}'"
            return (False, error_msg)
    if "sso-attribute-value-override" in payload:
        value = payload["sso-attribute-value-override"]
        if value not in VALID_BODY_SSO_ATTRIBUTE_VALUE_OVERRIDE:
            desc = FIELD_DESCRIPTIONS.get("sso-attribute-value-override", "")
            error_msg = f"Invalid value for 'sso-attribute-value-override': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SSO_ATTRIBUTE_VALUE_OVERRIDE)}"
            error_msg += f"\n  → Example: sso-attribute-value-override='{{ VALID_BODY_SSO_ATTRIBUTE_VALUE_OVERRIDE[0] }}'"
            return (False, error_msg)
    if "rsso-log-flags" in payload:
        value = payload["rsso-log-flags"]
        if value not in VALID_BODY_RSSO_LOG_FLAGS:
            desc = FIELD_DESCRIPTIONS.get("rsso-log-flags", "")
            error_msg = f"Invalid value for 'rsso-log-flags': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_RSSO_LOG_FLAGS)}"
            error_msg += f"\n  → Example: rsso-log-flags='{{ VALID_BODY_RSSO_LOG_FLAGS[0] }}'"
            return (False, error_msg)
    if "rsso-flush-ip-session" in payload:
        value = payload["rsso-flush-ip-session"]
        if value not in VALID_BODY_RSSO_FLUSH_IP_SESSION:
            desc = FIELD_DESCRIPTIONS.get("rsso-flush-ip-session", "")
            error_msg = f"Invalid value for 'rsso-flush-ip-session': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_RSSO_FLUSH_IP_SESSION)}"
            error_msg += f"\n  → Example: rsso-flush-ip-session='{{ VALID_BODY_RSSO_FLUSH_IP_SESSION[0] }}'"
            return (False, error_msg)
    if "rsso-ep-one-ip-only" in payload:
        value = payload["rsso-ep-one-ip-only"]
        if value not in VALID_BODY_RSSO_EP_ONE_IP_ONLY:
            desc = FIELD_DESCRIPTIONS.get("rsso-ep-one-ip-only", "")
            error_msg = f"Invalid value for 'rsso-ep-one-ip-only': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_RSSO_EP_ONE_IP_ONLY)}"
            error_msg += f"\n  → Example: rsso-ep-one-ip-only='{{ VALID_BODY_RSSO_EP_ONE_IP_ONLY[0] }}'"
            return (False, error_msg)
    if "delimiter" in payload:
        value = payload["delimiter"]
        if value not in VALID_BODY_DELIMITER:
            desc = FIELD_DESCRIPTIONS.get("delimiter", "")
            error_msg = f"Invalid value for 'delimiter': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DELIMITER)}"
            error_msg += f"\n  → Example: delimiter='{{ VALID_BODY_DELIMITER[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_user_radius_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update user/radius.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_user_radius_put(payload)
    """
    # Step 1: Validate enum values
    if "all-usergroup" in payload:
        value = payload["all-usergroup"]
        if value not in VALID_BODY_ALL_USERGROUP:
            return (
                False,
                f"Invalid value for 'all-usergroup'='{value}'. Must be one of: {', '.join(VALID_BODY_ALL_USERGROUP)}",
            )
    if "use-management-vdom" in payload:
        value = payload["use-management-vdom"]
        if value not in VALID_BODY_USE_MANAGEMENT_VDOM:
            return (
                False,
                f"Invalid value for 'use-management-vdom'='{value}'. Must be one of: {', '.join(VALID_BODY_USE_MANAGEMENT_VDOM)}",
            )
    if "switch-controller-nas-ip-dynamic" in payload:
        value = payload["switch-controller-nas-ip-dynamic"]
        if value not in VALID_BODY_SWITCH_CONTROLLER_NAS_IP_DYNAMIC:
            return (
                False,
                f"Invalid value for 'switch-controller-nas-ip-dynamic'='{value}'. Must be one of: {', '.join(VALID_BODY_SWITCH_CONTROLLER_NAS_IP_DYNAMIC)}",
            )
    if "nas-id-type" in payload:
        value = payload["nas-id-type"]
        if value not in VALID_BODY_NAS_ID_TYPE:
            return (
                False,
                f"Invalid value for 'nas-id-type'='{value}'. Must be one of: {', '.join(VALID_BODY_NAS_ID_TYPE)}",
            )
    if "call-station-id-type" in payload:
        value = payload["call-station-id-type"]
        if value not in VALID_BODY_CALL_STATION_ID_TYPE:
            return (
                False,
                f"Invalid value for 'call-station-id-type'='{value}'. Must be one of: {', '.join(VALID_BODY_CALL_STATION_ID_TYPE)}",
            )
    if "radius-coa" in payload:
        value = payload["radius-coa"]
        if value not in VALID_BODY_RADIUS_COA:
            return (
                False,
                f"Invalid value for 'radius-coa'='{value}'. Must be one of: {', '.join(VALID_BODY_RADIUS_COA)}",
            )
    if "h3c-compatibility" in payload:
        value = payload["h3c-compatibility"]
        if value not in VALID_BODY_H3C_COMPATIBILITY:
            return (
                False,
                f"Invalid value for 'h3c-compatibility'='{value}'. Must be one of: {', '.join(VALID_BODY_H3C_COMPATIBILITY)}",
            )
    if "auth-type" in payload:
        value = payload["auth-type"]
        if value not in VALID_BODY_AUTH_TYPE:
            return (
                False,
                f"Invalid value for 'auth-type'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_TYPE)}",
            )
    if "username-case-sensitive" in payload:
        value = payload["username-case-sensitive"]
        if value not in VALID_BODY_USERNAME_CASE_SENSITIVE:
            return (
                False,
                f"Invalid value for 'username-case-sensitive'='{value}'. Must be one of: {', '.join(VALID_BODY_USERNAME_CASE_SENSITIVE)}",
            )
    if "group-override-attr-type" in payload:
        value = payload["group-override-attr-type"]
        if value not in VALID_BODY_GROUP_OVERRIDE_ATTR_TYPE:
            return (
                False,
                f"Invalid value for 'group-override-attr-type'='{value}'. Must be one of: {', '.join(VALID_BODY_GROUP_OVERRIDE_ATTR_TYPE)}",
            )
    if "password-renewal" in payload:
        value = payload["password-renewal"]
        if value not in VALID_BODY_PASSWORD_RENEWAL:
            return (
                False,
                f"Invalid value for 'password-renewal'='{value}'. Must be one of: {', '.join(VALID_BODY_PASSWORD_RENEWAL)}",
            )
    if "require-message-authenticator" in payload:
        value = payload["require-message-authenticator"]
        if value not in VALID_BODY_REQUIRE_MESSAGE_AUTHENTICATOR:
            return (
                False,
                f"Invalid value for 'require-message-authenticator'='{value}'. Must be one of: {', '.join(VALID_BODY_REQUIRE_MESSAGE_AUTHENTICATOR)}",
            )
    if "password-encoding" in payload:
        value = payload["password-encoding"]
        if value not in VALID_BODY_PASSWORD_ENCODING:
            return (
                False,
                f"Invalid value for 'password-encoding'='{value}'. Must be one of: {', '.join(VALID_BODY_PASSWORD_ENCODING)}",
            )
    if "mac-username-delimiter" in payload:
        value = payload["mac-username-delimiter"]
        if value not in VALID_BODY_MAC_USERNAME_DELIMITER:
            return (
                False,
                f"Invalid value for 'mac-username-delimiter'='{value}'. Must be one of: {', '.join(VALID_BODY_MAC_USERNAME_DELIMITER)}",
            )
    if "mac-password-delimiter" in payload:
        value = payload["mac-password-delimiter"]
        if value not in VALID_BODY_MAC_PASSWORD_DELIMITER:
            return (
                False,
                f"Invalid value for 'mac-password-delimiter'='{value}'. Must be one of: {', '.join(VALID_BODY_MAC_PASSWORD_DELIMITER)}",
            )
    if "mac-case" in payload:
        value = payload["mac-case"]
        if value not in VALID_BODY_MAC_CASE:
            return (
                False,
                f"Invalid value for 'mac-case'='{value}'. Must be one of: {', '.join(VALID_BODY_MAC_CASE)}",
            )
    if "acct-all-servers" in payload:
        value = payload["acct-all-servers"]
        if value not in VALID_BODY_ACCT_ALL_SERVERS:
            return (
                False,
                f"Invalid value for 'acct-all-servers'='{value}'. Must be one of: {', '.join(VALID_BODY_ACCT_ALL_SERVERS)}",
            )
    if "interface-select-method" in payload:
        value = payload["interface-select-method"]
        if value not in VALID_BODY_INTERFACE_SELECT_METHOD:
            return (
                False,
                f"Invalid value for 'interface-select-method'='{value}'. Must be one of: {', '.join(VALID_BODY_INTERFACE_SELECT_METHOD)}",
            )
    if "switch-controller-service-type" in payload:
        value = payload["switch-controller-service-type"]
        if value not in VALID_BODY_SWITCH_CONTROLLER_SERVICE_TYPE:
            return (
                False,
                f"Invalid value for 'switch-controller-service-type'='{value}'. Must be one of: {', '.join(VALID_BODY_SWITCH_CONTROLLER_SERVICE_TYPE)}",
            )
    if "transport-protocol" in payload:
        value = payload["transport-protocol"]
        if value not in VALID_BODY_TRANSPORT_PROTOCOL:
            return (
                False,
                f"Invalid value for 'transport-protocol'='{value}'. Must be one of: {', '.join(VALID_BODY_TRANSPORT_PROTOCOL)}",
            )
    if "tls-min-proto-version" in payload:
        value = payload["tls-min-proto-version"]
        if value not in VALID_BODY_TLS_MIN_PROTO_VERSION:
            return (
                False,
                f"Invalid value for 'tls-min-proto-version'='{value}'. Must be one of: {', '.join(VALID_BODY_TLS_MIN_PROTO_VERSION)}",
            )
    if "server-identity-check" in payload:
        value = payload["server-identity-check"]
        if value not in VALID_BODY_SERVER_IDENTITY_CHECK:
            return (
                False,
                f"Invalid value for 'server-identity-check'='{value}'. Must be one of: {', '.join(VALID_BODY_SERVER_IDENTITY_CHECK)}",
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
    if "rsso" in payload:
        value = payload["rsso"]
        if value not in VALID_BODY_RSSO:
            return (
                False,
                f"Invalid value for 'rsso'='{value}'. Must be one of: {', '.join(VALID_BODY_RSSO)}",
            )
    if "rsso-radius-response" in payload:
        value = payload["rsso-radius-response"]
        if value not in VALID_BODY_RSSO_RADIUS_RESPONSE:
            return (
                False,
                f"Invalid value for 'rsso-radius-response'='{value}'. Must be one of: {', '.join(VALID_BODY_RSSO_RADIUS_RESPONSE)}",
            )
    if "rsso-validate-request-secret" in payload:
        value = payload["rsso-validate-request-secret"]
        if value not in VALID_BODY_RSSO_VALIDATE_REQUEST_SECRET:
            return (
                False,
                f"Invalid value for 'rsso-validate-request-secret'='{value}'. Must be one of: {', '.join(VALID_BODY_RSSO_VALIDATE_REQUEST_SECRET)}",
            )
    if "rsso-endpoint-attribute" in payload:
        value = payload["rsso-endpoint-attribute"]
        if value not in VALID_BODY_RSSO_ENDPOINT_ATTRIBUTE:
            return (
                False,
                f"Invalid value for 'rsso-endpoint-attribute'='{value}'. Must be one of: {', '.join(VALID_BODY_RSSO_ENDPOINT_ATTRIBUTE)}",
            )
    if "rsso-endpoint-block-attribute" in payload:
        value = payload["rsso-endpoint-block-attribute"]
        if value not in VALID_BODY_RSSO_ENDPOINT_BLOCK_ATTRIBUTE:
            return (
                False,
                f"Invalid value for 'rsso-endpoint-block-attribute'='{value}'. Must be one of: {', '.join(VALID_BODY_RSSO_ENDPOINT_BLOCK_ATTRIBUTE)}",
            )
    if "sso-attribute" in payload:
        value = payload["sso-attribute"]
        if value not in VALID_BODY_SSO_ATTRIBUTE:
            return (
                False,
                f"Invalid value for 'sso-attribute'='{value}'. Must be one of: {', '.join(VALID_BODY_SSO_ATTRIBUTE)}",
            )
    if "sso-attribute-value-override" in payload:
        value = payload["sso-attribute-value-override"]
        if value not in VALID_BODY_SSO_ATTRIBUTE_VALUE_OVERRIDE:
            return (
                False,
                f"Invalid value for 'sso-attribute-value-override'='{value}'. Must be one of: {', '.join(VALID_BODY_SSO_ATTRIBUTE_VALUE_OVERRIDE)}",
            )
    if "rsso-log-flags" in payload:
        value = payload["rsso-log-flags"]
        if value not in VALID_BODY_RSSO_LOG_FLAGS:
            return (
                False,
                f"Invalid value for 'rsso-log-flags'='{value}'. Must be one of: {', '.join(VALID_BODY_RSSO_LOG_FLAGS)}",
            )
    if "rsso-flush-ip-session" in payload:
        value = payload["rsso-flush-ip-session"]
        if value not in VALID_BODY_RSSO_FLUSH_IP_SESSION:
            return (
                False,
                f"Invalid value for 'rsso-flush-ip-session'='{value}'. Must be one of: {', '.join(VALID_BODY_RSSO_FLUSH_IP_SESSION)}",
            )
    if "rsso-ep-one-ip-only" in payload:
        value = payload["rsso-ep-one-ip-only"]
        if value not in VALID_BODY_RSSO_EP_ONE_IP_ONLY:
            return (
                False,
                f"Invalid value for 'rsso-ep-one-ip-only'='{value}'. Must be one of: {', '.join(VALID_BODY_RSSO_EP_ONE_IP_ONLY)}",
            )
    if "delimiter" in payload:
        value = payload["delimiter"]
        if value not in VALID_BODY_DELIMITER:
            return (
                False,
                f"Invalid value for 'delimiter'='{value}'. Must be one of: {', '.join(VALID_BODY_DELIMITER)}",
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
    "endpoint": "user/radius",
    "category": "cmdb",
    "api_path": "user/radius",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure RADIUS server entries.",
    "total_fields": 62,
    "required_fields_count": 5,
    "fields_with_defaults_count": 56,
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
