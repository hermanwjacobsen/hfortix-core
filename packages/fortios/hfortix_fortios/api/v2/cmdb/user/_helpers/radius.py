"""
Validation helpers for user radius endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# ============================================================================
# Required Fields Validation
# Auto-generated from schema using required_fields_analyzer.py
# ============================================================================

# NOTE: The FortiOS schema has known bugs where some specialized optional
# features are incorrectly marked as required. See SCHEMA_FALSE_POSITIVES
# for fields that should be OPTIONAL despite being marked required in
# the schema. The REQUIRED_FIELDS list below reflects the ACTUAL
# requirements based on API testing and schema analysis.

# Always required fields (no alternatives)
REQUIRED_FIELDS = [
    "interface",  # Specify outgoing interface to reach server.
    "name",  # RADIUS server entry name.
    "secret",  # Pre-shared secret key used to access the primary RADIUS serv
    "server",  # Primary RADIUS server CN domain name or IP address.
    "sso-attribute",  # RADIUS attribute that contains the profile group name to be
    "sso-attribute-value-override",  # Enable/disable override old attribute value with new value f
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "account-key-cert-field": "othername",
    "account-key-processing": "same",
    "acct-all-servers": "disable",
    "all-usergroup": "disable",
    "auth-type": "auto",
    "call-station-id-type": "legacy",
    "delimiter": "plus",
    "group-override-attr-type": "filter-Id",
    "h3c-compatibility": "disable",
    "interface-select-method": "auto",
    "mac-case": "lowercase",
    "mac-password-delimiter": "hyphen",
    "mac-username-delimiter": "hyphen",
    "nas-id-type": "legacy",
    "nas-ip": "0.0.0.0",
    "password-encoding": "auto",
    "password-renewal": "enable",
    "radius-coa": "disable",
    "require-message-authenticator": "enable",
    "rsso": "disable",
    "rsso-context-timeout": 28800,
    "rsso-endpoint-attribute": "Calling-Station-Id",
    "rsso-endpoint-block-attribute": "User-Name",
    "rsso-ep-one-ip-only": "disable",
    "rsso-flush-ip-session": "disable",
    "rsso-log-flags": "protocol-error profile-missing accounting-stop-missed accounting-event endpoint-block radiusd-other",
    "rsso-radius-response": "disable",
    "rsso-radius-server-port": 1813,
    "rsso-validate-request-secret": "disable",
    "server-identity-check": "enable",
    "sso-attribute": "Class",
    "sso-attribute-value-override": "enable",
    "status-ttl": 300,
    "switch-controller-acct-fast-framedip-detect": 2,
    "switch-controller-nas-ip-dynamic": "disable",
    "switch-controller-service-type": "login",
    "timeout": 5,
    "tls-min-proto-version": "default",
    "transport-protocol": "udp",
    "use-management-vdom": "disable",
    "username-case-sensitive": "disable",
}

# Fields wrongly marked as required in schema (schema bugs)
# These are specialized features and should be OPTIONAL
SCHEMA_FALSE_POSITIVES = [
    "rsso",  # Enable/disable RADIUS based single sign on feature
    "rsso-context-timeout",  # Time in seconds before the logged out user is remo
    "rsso-endpoint-attribute",  # RADIUS attributes used to extract the user end poi
    "rsso-endpoint-block-attribute",  # RADIUS attributes used to block a user.
    "rsso-log-period",  # Time interval in seconds that group event log mess
    "rsso-radius-response",  # Enable/disable sending RADIUS response packets aft
    "rsso-radius-server-port",  # UDP port to listen on for RADIUS Start and Stop re
    "rsso-secret",  # RADIUS secret used by the RADIUS accounting server
    "rsso-validate-request-secret",  # Enable/disable validating the RADIUS request share
]


# Valid enum values from API documentation
VALID_BODY_ALL_USERGROUP = ["disable", "enable"]
VALID_BODY_USE_MANAGEMENT_VDOM = ["enable", "disable"]
VALID_BODY_SWITCH_CONTROLLER_NAS_IP_DYNAMIC = ["enable", "disable"]
VALID_BODY_NAS_ID_TYPE = ["legacy", "custom", "hostname"]
VALID_BODY_CALL_STATION_ID_TYPE = ["legacy", "IP", "MAC"]
VALID_BODY_RADIUS_COA = ["enable", "disable"]
VALID_BODY_H3C_COMPATIBILITY = ["enable", "disable"]
VALID_BODY_AUTH_TYPE = ["auto", "ms_chap_v2", "ms_chap", "chap", "pap"]
VALID_BODY_USERNAME_CASE_SENSITIVE = ["enable", "disable"]
VALID_BODY_GROUP_OVERRIDE_ATTR_TYPE = ["filter-Id", "class"]
VALID_BODY_PASSWORD_RENEWAL = ["enable", "disable"]
VALID_BODY_REQUIRE_MESSAGE_AUTHENTICATOR = ["enable", "disable"]
VALID_BODY_PASSWORD_ENCODING = ["auto", "ISO-8859-1"]
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
VALID_BODY_MAC_CASE = ["uppercase", "lowercase"]
VALID_BODY_ACCT_ALL_SERVERS = ["enable", "disable"]
VALID_BODY_INTERFACE_SELECT_METHOD = ["auto", "sdwan", "specify"]
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
VALID_BODY_TRANSPORT_PROTOCOL = ["udp", "tcp", "tls"]
VALID_BODY_TLS_MIN_PROTO_VERSION = [
    "default",
    "SSLv3",
    "TLSv1",
    "TLSv1-1",
    "TLSv1-2",
    "TLSv1-3",
]
VALID_BODY_SERVER_IDENTITY_CHECK = ["enable", "disable"]
VALID_BODY_ACCOUNT_KEY_PROCESSING = ["same", "strip"]
VALID_BODY_ACCOUNT_KEY_CERT_FIELD = [
    "othername",
    "rfc822name",
    "dnsname",
    "cn",
]
VALID_BODY_RSSO = ["enable", "disable"]
VALID_BODY_RSSO_RADIUS_RESPONSE = ["enable", "disable"]
VALID_BODY_RSSO_VALIDATE_REQUEST_SECRET = ["enable", "disable"]
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
VALID_BODY_SSO_ATTRIBUTE_VALUE_OVERRIDE = ["enable", "disable"]
VALID_BODY_RSSO_LOG_FLAGS = [
    "protocol-error",
    "profile-missing",
    "accounting-stop-missed",
    "accounting-event",
    "endpoint-block",
    "radiusd-other",
    "none",
]
VALID_BODY_RSSO_FLUSH_IP_SESSION = ["enable", "disable"]
VALID_BODY_RSSO_EP_ONE_IP_ONLY = ["enable", "disable"]
VALID_BODY_DELIMITER = ["plus", "comma"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_radius_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> # List all objects
        >>> is_valid, error = {func_name}()
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
    Validate required fields for user_radius.

    This validator checks:
    1. Always-required fields are present
    2. Mutually exclusive groups have at least one field

    Args:
        payload: The request payload to validate

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> is_valid, error = validate_required_fields({
        ...     "interface": "value",
        ...     # ... other fields
        ... })
    """
    # Check always-required fields
    missing = []
    for field in REQUIRED_FIELDS:
        # Skip fields with defaults
        if field in FIELDS_WITH_DEFAULTS:
            continue
        if field not in payload or payload.get(field) is None:
            missing.append(field)

    if missing:
        return (False, f"Missing required fields: {', '.join(missing)}")

    return (True, None)


# ============================================================================
# Endpoint Validation (Enhanced with Required Fields)
# ============================================================================


def validate_radius_post(payload: dict[str, Any]) -> tuple[bool, str | None]:
    """
    Validate POST request payload.

    This validator performs two-stage validation:
    1. Required fields validation (schema-based)
    2. Field value validation (enums, ranges, formats)

    Required fields:
      - interface: Specify outgoing interface to reach server.
      - name: RADIUS server entry name.
      - secret: Pre-shared secret key used to access the primary RADIUS serv
      - server: Primary RADIUS server CN domain name or IP address.
      - sso-attribute: RADIUS attribute that contains the profile group name to be
      - sso-attribute-value-override: Enable/disable override old attribute value with new value f

    Args:
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Validate payload exists
    if not payload:
        payload = {}

    # Validate payload exists
    if not payload:
        payload = {}

    # Validate payload exists
    if not payload:
        payload = {}

    # Validate payload exists
    if not payload:
        payload = {}

    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate field values (enums, ranges, etc.)
    # Validate name if present
    if "name" in payload:
        value = payload.get("name")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "name cannot exceed 35 characters")

    # Validate server if present
    if "server" in payload:
        value = payload.get("server")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "server cannot exceed 63 characters")

    # Validate secondary-server if present
    if "secondary-server" in payload:
        value = payload.get("secondary-server")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "secondary-server cannot exceed 63 characters")

    # Validate tertiary-server if present
    if "tertiary-server" in payload:
        value = payload.get("tertiary-server")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "tertiary-server cannot exceed 63 characters")

    # Validate timeout if present
    if "timeout" in payload:
        value = payload.get("timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 300:
                    return (False, "timeout must be between 1 and 300")
            except (ValueError, TypeError):
                return (False, f"timeout must be numeric, got: {value}")

    # Validate status-ttl if present
    if "status-ttl" in payload:
        value = payload.get("status-ttl")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 600:
                    return (False, "status-ttl must be between 0 and 600")
            except (ValueError, TypeError):
                return (False, f"status-ttl must be numeric, got: {value}")

    # Validate all-usergroup if present
    if "all-usergroup" in payload:
        value = payload.get("all-usergroup")
        if value and value not in VALID_BODY_ALL_USERGROUP:
            return (
                False,
                f"Invalid all-usergroup '{value}'. Must be one of: {', '.join(VALID_BODY_ALL_USERGROUP)}",
            )

    # Validate use-management-vdom if present
    if "use-management-vdom" in payload:
        value = payload.get("use-management-vdom")
        if value and value not in VALID_BODY_USE_MANAGEMENT_VDOM:
            return (
                False,
                f"Invalid use-management-vdom '{value}'. Must be one of: {', '.join(VALID_BODY_USE_MANAGEMENT_VDOM)}",
            )

    # Validate switch-controller-nas-ip-dynamic if present
    if "switch-controller-nas-ip-dynamic" in payload:
        value = payload.get("switch-controller-nas-ip-dynamic")
        if value and value not in VALID_BODY_SWITCH_CONTROLLER_NAS_IP_DYNAMIC:
            return (
                False,
                f"Invalid switch-controller-nas-ip-dynamic '{value}'. Must be one of: {', '.join(VALID_BODY_SWITCH_CONTROLLER_NAS_IP_DYNAMIC)}",
            )

    # Validate nas-id-type if present
    if "nas-id-type" in payload:
        value = payload.get("nas-id-type")
        if value and value not in VALID_BODY_NAS_ID_TYPE:
            return (
                False,
                f"Invalid nas-id-type '{value}'. Must be one of: {', '.join(VALID_BODY_NAS_ID_TYPE)}",
            )

    # Validate call-station-id-type if present
    if "call-station-id-type" in payload:
        value = payload.get("call-station-id-type")
        if value and value not in VALID_BODY_CALL_STATION_ID_TYPE:
            return (
                False,
                f"Invalid call-station-id-type '{value}'. Must be one of: {', '.join(VALID_BODY_CALL_STATION_ID_TYPE)}",
            )

    # Validate nas-id if present
    if "nas-id" in payload:
        value = payload.get("nas-id")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "nas-id cannot exceed 255 characters")

    # Validate acct-interim-interval if present
    if "acct-interim-interval" in payload:
        value = payload.get("acct-interim-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 60 or int_val > 86400:
                    return (
                        False,
                        "acct-interim-interval must be between 60 and 86400",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"acct-interim-interval must be numeric, got: {value}",
                )

    # Validate radius-coa if present
    if "radius-coa" in payload:
        value = payload.get("radius-coa")
        if value and value not in VALID_BODY_RADIUS_COA:
            return (
                False,
                f"Invalid radius-coa '{value}'. Must be one of: {', '.join(VALID_BODY_RADIUS_COA)}",
            )

    # Validate radius-port if present
    if "radius-port" in payload:
        value = payload.get("radius-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (False, "radius-port must be between 0 and 65535")
            except (ValueError, TypeError):
                return (False, f"radius-port must be numeric, got: {value}")

    # Validate h3c-compatibility if present
    if "h3c-compatibility" in payload:
        value = payload.get("h3c-compatibility")
        if value and value not in VALID_BODY_H3C_COMPATIBILITY:
            return (
                False,
                f"Invalid h3c-compatibility '{value}'. Must be one of: {', '.join(VALID_BODY_H3C_COMPATIBILITY)}",
            )

    # Validate auth-type if present
    if "auth-type" in payload:
        value = payload.get("auth-type")
        if value and value not in VALID_BODY_AUTH_TYPE:
            return (
                False,
                f"Invalid auth-type '{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_TYPE)}",
            )

    # Validate source-ip if present
    if "source-ip" in payload:
        value = payload.get("source-ip")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "source-ip cannot exceed 63 characters")

    # Validate source-ip-interface if present
    if "source-ip-interface" in payload:
        value = payload.get("source-ip-interface")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "source-ip-interface cannot exceed 15 characters")

    # Validate username-case-sensitive if present
    if "username-case-sensitive" in payload:
        value = payload.get("username-case-sensitive")
        if value and value not in VALID_BODY_USERNAME_CASE_SENSITIVE:
            return (
                False,
                f"Invalid username-case-sensitive '{value}'. Must be one of: {', '.join(VALID_BODY_USERNAME_CASE_SENSITIVE)}",
            )

    # Validate group-override-attr-type if present
    if "group-override-attr-type" in payload:
        value = payload.get("group-override-attr-type")
        if value and value not in VALID_BODY_GROUP_OVERRIDE_ATTR_TYPE:
            return (
                False,
                f"Invalid group-override-attr-type '{value}'. Must be one of: {', '.join(VALID_BODY_GROUP_OVERRIDE_ATTR_TYPE)}",
            )

    # Validate password-renewal if present
    if "password-renewal" in payload:
        value = payload.get("password-renewal")
        if value and value not in VALID_BODY_PASSWORD_RENEWAL:
            return (
                False,
                f"Invalid password-renewal '{value}'. Must be one of: {', '.join(VALID_BODY_PASSWORD_RENEWAL)}",
            )

    # Validate require-message-authenticator if present
    if "require-message-authenticator" in payload:
        value = payload.get("require-message-authenticator")
        if value and value not in VALID_BODY_REQUIRE_MESSAGE_AUTHENTICATOR:
            return (
                False,
                f"Invalid require-message-authenticator '{value}'. Must be one of: {', '.join(VALID_BODY_REQUIRE_MESSAGE_AUTHENTICATOR)}",
            )

    # Validate password-encoding if present
    if "password-encoding" in payload:
        value = payload.get("password-encoding")
        if value and value not in VALID_BODY_PASSWORD_ENCODING:
            return (
                False,
                f"Invalid password-encoding '{value}'. Must be one of: {', '.join(VALID_BODY_PASSWORD_ENCODING)}",
            )

    # Validate mac-username-delimiter if present
    if "mac-username-delimiter" in payload:
        value = payload.get("mac-username-delimiter")
        if value and value not in VALID_BODY_MAC_USERNAME_DELIMITER:
            return (
                False,
                f"Invalid mac-username-delimiter '{value}'. Must be one of: {', '.join(VALID_BODY_MAC_USERNAME_DELIMITER)}",
            )

    # Validate mac-password-delimiter if present
    if "mac-password-delimiter" in payload:
        value = payload.get("mac-password-delimiter")
        if value and value not in VALID_BODY_MAC_PASSWORD_DELIMITER:
            return (
                False,
                f"Invalid mac-password-delimiter '{value}'. Must be one of: {', '.join(VALID_BODY_MAC_PASSWORD_DELIMITER)}",
            )

    # Validate mac-case if present
    if "mac-case" in payload:
        value = payload.get("mac-case")
        if value and value not in VALID_BODY_MAC_CASE:
            return (
                False,
                f"Invalid mac-case '{value}'. Must be one of: {', '.join(VALID_BODY_MAC_CASE)}",
            )

    # Validate acct-all-servers if present
    if "acct-all-servers" in payload:
        value = payload.get("acct-all-servers")
        if value and value not in VALID_BODY_ACCT_ALL_SERVERS:
            return (
                False,
                f"Invalid acct-all-servers '{value}'. Must be one of: {', '.join(VALID_BODY_ACCT_ALL_SERVERS)}",
            )

    # Validate switch-controller-acct-fast-framedip-detect if present
    if "switch-controller-acct-fast-framedip-detect" in payload:
        value = payload.get("switch-controller-acct-fast-framedip-detect")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 2 or int_val > 600:
                    return (
                        False,
                        "switch-controller-acct-fast-framedip-detect must be between 2 and 600",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"switch-controller-acct-fast-framedip-detect must be numeric, got: {value}",
                )

    # Validate interface-select-method if present
    if "interface-select-method" in payload:
        value = payload.get("interface-select-method")
        if value and value not in VALID_BODY_INTERFACE_SELECT_METHOD:
            return (
                False,
                f"Invalid interface-select-method '{value}'. Must be one of: {', '.join(VALID_BODY_INTERFACE_SELECT_METHOD)}",
            )

    # Validate interface if present
    if "interface" in payload:
        value = payload.get("interface")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "interface cannot exceed 15 characters")

    # Validate vrf-select if present
    if "vrf-select" in payload:
        value = payload.get("vrf-select")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 511:
                    return (False, "vrf-select must be between 0 and 511")
            except (ValueError, TypeError):
                return (False, f"vrf-select must be numeric, got: {value}")

    # Validate switch-controller-service-type if present
    if "switch-controller-service-type" in payload:
        value = payload.get("switch-controller-service-type")
        if value and value not in VALID_BODY_SWITCH_CONTROLLER_SERVICE_TYPE:
            return (
                False,
                f"Invalid switch-controller-service-type '{value}'. Must be one of: {', '.join(VALID_BODY_SWITCH_CONTROLLER_SERVICE_TYPE)}",
            )

    # Validate transport-protocol if present
    if "transport-protocol" in payload:
        value = payload.get("transport-protocol")
        if value and value not in VALID_BODY_TRANSPORT_PROTOCOL:
            return (
                False,
                f"Invalid transport-protocol '{value}'. Must be one of: {', '.join(VALID_BODY_TRANSPORT_PROTOCOL)}",
            )

    # Validate tls-min-proto-version if present
    if "tls-min-proto-version" in payload:
        value = payload.get("tls-min-proto-version")
        if value and value not in VALID_BODY_TLS_MIN_PROTO_VERSION:
            return (
                False,
                f"Invalid tls-min-proto-version '{value}'. Must be one of: {', '.join(VALID_BODY_TLS_MIN_PROTO_VERSION)}",
            )

    # Validate ca-cert if present
    if "ca-cert" in payload:
        value = payload.get("ca-cert")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "ca-cert cannot exceed 79 characters")

    # Validate client-cert if present
    if "client-cert" in payload:
        value = payload.get("client-cert")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "client-cert cannot exceed 35 characters")

    # Validate server-identity-check if present
    if "server-identity-check" in payload:
        value = payload.get("server-identity-check")
        if value and value not in VALID_BODY_SERVER_IDENTITY_CHECK:
            return (
                False,
                f"Invalid server-identity-check '{value}'. Must be one of: {', '.join(VALID_BODY_SERVER_IDENTITY_CHECK)}",
            )

    # Validate account-key-processing if present
    if "account-key-processing" in payload:
        value = payload.get("account-key-processing")
        if value and value not in VALID_BODY_ACCOUNT_KEY_PROCESSING:
            return (
                False,
                f"Invalid account-key-processing '{value}'. Must be one of: {', '.join(VALID_BODY_ACCOUNT_KEY_PROCESSING)}",
            )

    # Validate account-key-cert-field if present
    if "account-key-cert-field" in payload:
        value = payload.get("account-key-cert-field")
        if value and value not in VALID_BODY_ACCOUNT_KEY_CERT_FIELD:
            return (
                False,
                f"Invalid account-key-cert-field '{value}'. Must be one of: {', '.join(VALID_BODY_ACCOUNT_KEY_CERT_FIELD)}",
            )

    # Validate rsso if present
    if "rsso" in payload:
        value = payload.get("rsso")
        if value and value not in VALID_BODY_RSSO:
            return (
                False,
                f"Invalid rsso '{value}'. Must be one of: {', '.join(VALID_BODY_RSSO)}",
            )

    # Validate rsso-radius-server-port if present
    if "rsso-radius-server-port" in payload:
        value = payload.get("rsso-radius-server-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (
                        False,
                        "rsso-radius-server-port must be between 0 and 65535",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"rsso-radius-server-port must be numeric, got: {value}",
                )

    # Validate rsso-radius-response if present
    if "rsso-radius-response" in payload:
        value = payload.get("rsso-radius-response")
        if value and value not in VALID_BODY_RSSO_RADIUS_RESPONSE:
            return (
                False,
                f"Invalid rsso-radius-response '{value}'. Must be one of: {', '.join(VALID_BODY_RSSO_RADIUS_RESPONSE)}",
            )

    # Validate rsso-validate-request-secret if present
    if "rsso-validate-request-secret" in payload:
        value = payload.get("rsso-validate-request-secret")
        if value and value not in VALID_BODY_RSSO_VALIDATE_REQUEST_SECRET:
            return (
                False,
                f"Invalid rsso-validate-request-secret '{value}'. Must be one of: {', '.join(VALID_BODY_RSSO_VALIDATE_REQUEST_SECRET)}",
            )

    # Validate rsso-endpoint-attribute if present
    if "rsso-endpoint-attribute" in payload:
        value = payload.get("rsso-endpoint-attribute")
        if value and value not in VALID_BODY_RSSO_ENDPOINT_ATTRIBUTE:
            return (
                False,
                f"Invalid rsso-endpoint-attribute '{value}'. Must be one of: {', '.join(VALID_BODY_RSSO_ENDPOINT_ATTRIBUTE)}",
            )

    # Validate rsso-endpoint-block-attribute if present
    if "rsso-endpoint-block-attribute" in payload:
        value = payload.get("rsso-endpoint-block-attribute")
        if value and value not in VALID_BODY_RSSO_ENDPOINT_BLOCK_ATTRIBUTE:
            return (
                False,
                f"Invalid rsso-endpoint-block-attribute '{value}'. Must be one of: {', '.join(VALID_BODY_RSSO_ENDPOINT_BLOCK_ATTRIBUTE)}",
            )

    # Validate sso-attribute if present
    if "sso-attribute" in payload:
        value = payload.get("sso-attribute")
        if value and value not in VALID_BODY_SSO_ATTRIBUTE:
            return (
                False,
                f"Invalid sso-attribute '{value}'. Must be one of: {', '.join(VALID_BODY_SSO_ATTRIBUTE)}",
            )

    # Validate sso-attribute-key if present
    if "sso-attribute-key" in payload:
        value = payload.get("sso-attribute-key")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "sso-attribute-key cannot exceed 35 characters")

    # Validate sso-attribute-value-override if present
    if "sso-attribute-value-override" in payload:
        value = payload.get("sso-attribute-value-override")
        if value and value not in VALID_BODY_SSO_ATTRIBUTE_VALUE_OVERRIDE:
            return (
                False,
                f"Invalid sso-attribute-value-override '{value}'. Must be one of: {', '.join(VALID_BODY_SSO_ATTRIBUTE_VALUE_OVERRIDE)}",
            )

    # Validate rsso-context-timeout if present
    if "rsso-context-timeout" in payload:
        value = payload.get("rsso-context-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "rsso-context-timeout must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"rsso-context-timeout must be numeric, got: {value}",
                )

    # Validate rsso-log-period if present
    if "rsso-log-period" in payload:
        value = payload.get("rsso-log-period")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "rsso-log-period must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"rsso-log-period must be numeric, got: {value}",
                )

    # Validate rsso-log-flags if present
    if "rsso-log-flags" in payload:
        value = payload.get("rsso-log-flags")
        if value and value not in VALID_BODY_RSSO_LOG_FLAGS:
            return (
                False,
                f"Invalid rsso-log-flags '{value}'. Must be one of: {', '.join(VALID_BODY_RSSO_LOG_FLAGS)}",
            )

    # Validate rsso-flush-ip-session if present
    if "rsso-flush-ip-session" in payload:
        value = payload.get("rsso-flush-ip-session")
        if value and value not in VALID_BODY_RSSO_FLUSH_IP_SESSION:
            return (
                False,
                f"Invalid rsso-flush-ip-session '{value}'. Must be one of: {', '.join(VALID_BODY_RSSO_FLUSH_IP_SESSION)}",
            )

    # Validate rsso-ep-one-ip-only if present
    if "rsso-ep-one-ip-only" in payload:
        value = payload.get("rsso-ep-one-ip-only")
        if value and value not in VALID_BODY_RSSO_EP_ONE_IP_ONLY:
            return (
                False,
                f"Invalid rsso-ep-one-ip-only '{value}'. Must be one of: {', '.join(VALID_BODY_RSSO_EP_ONE_IP_ONLY)}",
            )

    # Validate delimiter if present
    if "delimiter" in payload:
        value = payload.get("delimiter")
        if value and value not in VALID_BODY_DELIMITER:
            return (
                False,
                f"Invalid delimiter '{value}'. Must be one of: {', '.join(VALID_BODY_DELIMITER)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_radius_put(
    name: str | None = None, payload: dict[str, Any] | None = None
) -> tuple[bool, str | None]:
    """
    Validate PUT request payload for updating {endpoint_name}.

    Args:
        name: Object identifier (required)
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # name is required for updates
    if not name:
        return (False, "name is required for PUT operation")

    # If no payload provided, nothing to validate
    if not payload:
        return (True, None)

    # Validate name if present
    if "name" in payload:
        value = payload.get("name")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "name cannot exceed 35 characters")

    # Validate server if present
    if "server" in payload:
        value = payload.get("server")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "server cannot exceed 63 characters")

    # Validate secondary-server if present
    if "secondary-server" in payload:
        value = payload.get("secondary-server")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "secondary-server cannot exceed 63 characters")

    # Validate tertiary-server if present
    if "tertiary-server" in payload:
        value = payload.get("tertiary-server")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "tertiary-server cannot exceed 63 characters")

    # Validate timeout if present
    if "timeout" in payload:
        value = payload.get("timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 300:
                    return (False, "timeout must be between 1 and 300")
            except (ValueError, TypeError):
                return (False, f"timeout must be numeric, got: {value}")

    # Validate status-ttl if present
    if "status-ttl" in payload:
        value = payload.get("status-ttl")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 600:
                    return (False, "status-ttl must be between 0 and 600")
            except (ValueError, TypeError):
                return (False, f"status-ttl must be numeric, got: {value}")

    # Validate all-usergroup if present
    if "all-usergroup" in payload:
        value = payload.get("all-usergroup")
        if value and value not in VALID_BODY_ALL_USERGROUP:
            return (
                False,
                f"Invalid all-usergroup '{value}'. Must be one of: {', '.join(VALID_BODY_ALL_USERGROUP)}",
            )

    # Validate use-management-vdom if present
    if "use-management-vdom" in payload:
        value = payload.get("use-management-vdom")
        if value and value not in VALID_BODY_USE_MANAGEMENT_VDOM:
            return (
                False,
                f"Invalid use-management-vdom '{value}'. Must be one of: {', '.join(VALID_BODY_USE_MANAGEMENT_VDOM)}",
            )

    # Validate switch-controller-nas-ip-dynamic if present
    if "switch-controller-nas-ip-dynamic" in payload:
        value = payload.get("switch-controller-nas-ip-dynamic")
        if value and value not in VALID_BODY_SWITCH_CONTROLLER_NAS_IP_DYNAMIC:
            return (
                False,
                f"Invalid switch-controller-nas-ip-dynamic '{value}'. Must be one of: {', '.join(VALID_BODY_SWITCH_CONTROLLER_NAS_IP_DYNAMIC)}",
            )

    # Validate nas-id-type if present
    if "nas-id-type" in payload:
        value = payload.get("nas-id-type")
        if value and value not in VALID_BODY_NAS_ID_TYPE:
            return (
                False,
                f"Invalid nas-id-type '{value}'. Must be one of: {', '.join(VALID_BODY_NAS_ID_TYPE)}",
            )

    # Validate call-station-id-type if present
    if "call-station-id-type" in payload:
        value = payload.get("call-station-id-type")
        if value and value not in VALID_BODY_CALL_STATION_ID_TYPE:
            return (
                False,
                f"Invalid call-station-id-type '{value}'. Must be one of: {', '.join(VALID_BODY_CALL_STATION_ID_TYPE)}",
            )

    # Validate nas-id if present
    if "nas-id" in payload:
        value = payload.get("nas-id")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "nas-id cannot exceed 255 characters")

    # Validate acct-interim-interval if present
    if "acct-interim-interval" in payload:
        value = payload.get("acct-interim-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 60 or int_val > 86400:
                    return (
                        False,
                        "acct-interim-interval must be between 60 and 86400",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"acct-interim-interval must be numeric, got: {value}",
                )

    # Validate radius-coa if present
    if "radius-coa" in payload:
        value = payload.get("radius-coa")
        if value and value not in VALID_BODY_RADIUS_COA:
            return (
                False,
                f"Invalid radius-coa '{value}'. Must be one of: {', '.join(VALID_BODY_RADIUS_COA)}",
            )

    # Validate radius-port if present
    if "radius-port" in payload:
        value = payload.get("radius-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (False, "radius-port must be between 0 and 65535")
            except (ValueError, TypeError):
                return (False, f"radius-port must be numeric, got: {value}")

    # Validate h3c-compatibility if present
    if "h3c-compatibility" in payload:
        value = payload.get("h3c-compatibility")
        if value and value not in VALID_BODY_H3C_COMPATIBILITY:
            return (
                False,
                f"Invalid h3c-compatibility '{value}'. Must be one of: {', '.join(VALID_BODY_H3C_COMPATIBILITY)}",
            )

    # Validate auth-type if present
    if "auth-type" in payload:
        value = payload.get("auth-type")
        if value and value not in VALID_BODY_AUTH_TYPE:
            return (
                False,
                f"Invalid auth-type '{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_TYPE)}",
            )

    # Validate source-ip if present
    if "source-ip" in payload:
        value = payload.get("source-ip")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "source-ip cannot exceed 63 characters")

    # Validate source-ip-interface if present
    if "source-ip-interface" in payload:
        value = payload.get("source-ip-interface")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "source-ip-interface cannot exceed 15 characters")

    # Validate username-case-sensitive if present
    if "username-case-sensitive" in payload:
        value = payload.get("username-case-sensitive")
        if value and value not in VALID_BODY_USERNAME_CASE_SENSITIVE:
            return (
                False,
                f"Invalid username-case-sensitive '{value}'. Must be one of: {', '.join(VALID_BODY_USERNAME_CASE_SENSITIVE)}",
            )

    # Validate group-override-attr-type if present
    if "group-override-attr-type" in payload:
        value = payload.get("group-override-attr-type")
        if value and value not in VALID_BODY_GROUP_OVERRIDE_ATTR_TYPE:
            return (
                False,
                f"Invalid group-override-attr-type '{value}'. Must be one of: {', '.join(VALID_BODY_GROUP_OVERRIDE_ATTR_TYPE)}",
            )

    # Validate password-renewal if present
    if "password-renewal" in payload:
        value = payload.get("password-renewal")
        if value and value not in VALID_BODY_PASSWORD_RENEWAL:
            return (
                False,
                f"Invalid password-renewal '{value}'. Must be one of: {', '.join(VALID_BODY_PASSWORD_RENEWAL)}",
            )

    # Validate require-message-authenticator if present
    if "require-message-authenticator" in payload:
        value = payload.get("require-message-authenticator")
        if value and value not in VALID_BODY_REQUIRE_MESSAGE_AUTHENTICATOR:
            return (
                False,
                f"Invalid require-message-authenticator '{value}'. Must be one of: {', '.join(VALID_BODY_REQUIRE_MESSAGE_AUTHENTICATOR)}",
            )

    # Validate password-encoding if present
    if "password-encoding" in payload:
        value = payload.get("password-encoding")
        if value and value not in VALID_BODY_PASSWORD_ENCODING:
            return (
                False,
                f"Invalid password-encoding '{value}'. Must be one of: {', '.join(VALID_BODY_PASSWORD_ENCODING)}",
            )

    # Validate mac-username-delimiter if present
    if "mac-username-delimiter" in payload:
        value = payload.get("mac-username-delimiter")
        if value and value not in VALID_BODY_MAC_USERNAME_DELIMITER:
            return (
                False,
                f"Invalid mac-username-delimiter '{value}'. Must be one of: {', '.join(VALID_BODY_MAC_USERNAME_DELIMITER)}",
            )

    # Validate mac-password-delimiter if present
    if "mac-password-delimiter" in payload:
        value = payload.get("mac-password-delimiter")
        if value and value not in VALID_BODY_MAC_PASSWORD_DELIMITER:
            return (
                False,
                f"Invalid mac-password-delimiter '{value}'. Must be one of: {', '.join(VALID_BODY_MAC_PASSWORD_DELIMITER)}",
            )

    # Validate mac-case if present
    if "mac-case" in payload:
        value = payload.get("mac-case")
        if value and value not in VALID_BODY_MAC_CASE:
            return (
                False,
                f"Invalid mac-case '{value}'. Must be one of: {', '.join(VALID_BODY_MAC_CASE)}",
            )

    # Validate acct-all-servers if present
    if "acct-all-servers" in payload:
        value = payload.get("acct-all-servers")
        if value and value not in VALID_BODY_ACCT_ALL_SERVERS:
            return (
                False,
                f"Invalid acct-all-servers '{value}'. Must be one of: {', '.join(VALID_BODY_ACCT_ALL_SERVERS)}",
            )

    # Validate switch-controller-acct-fast-framedip-detect if present
    if "switch-controller-acct-fast-framedip-detect" in payload:
        value = payload.get("switch-controller-acct-fast-framedip-detect")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 2 or int_val > 600:
                    return (
                        False,
                        "switch-controller-acct-fast-framedip-detect must be between 2 and 600",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"switch-controller-acct-fast-framedip-detect must be numeric, got: {value}",
                )

    # Validate interface-select-method if present
    if "interface-select-method" in payload:
        value = payload.get("interface-select-method")
        if value and value not in VALID_BODY_INTERFACE_SELECT_METHOD:
            return (
                False,
                f"Invalid interface-select-method '{value}'. Must be one of: {', '.join(VALID_BODY_INTERFACE_SELECT_METHOD)}",
            )

    # Validate interface if present
    if "interface" in payload:
        value = payload.get("interface")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "interface cannot exceed 15 characters")

    # Validate vrf-select if present
    if "vrf-select" in payload:
        value = payload.get("vrf-select")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 511:
                    return (False, "vrf-select must be between 0 and 511")
            except (ValueError, TypeError):
                return (False, f"vrf-select must be numeric, got: {value}")

    # Validate switch-controller-service-type if present
    if "switch-controller-service-type" in payload:
        value = payload.get("switch-controller-service-type")
        if value and value not in VALID_BODY_SWITCH_CONTROLLER_SERVICE_TYPE:
            return (
                False,
                f"Invalid switch-controller-service-type '{value}'. Must be one of: {', '.join(VALID_BODY_SWITCH_CONTROLLER_SERVICE_TYPE)}",
            )

    # Validate transport-protocol if present
    if "transport-protocol" in payload:
        value = payload.get("transport-protocol")
        if value and value not in VALID_BODY_TRANSPORT_PROTOCOL:
            return (
                False,
                f"Invalid transport-protocol '{value}'. Must be one of: {', '.join(VALID_BODY_TRANSPORT_PROTOCOL)}",
            )

    # Validate tls-min-proto-version if present
    if "tls-min-proto-version" in payload:
        value = payload.get("tls-min-proto-version")
        if value and value not in VALID_BODY_TLS_MIN_PROTO_VERSION:
            return (
                False,
                f"Invalid tls-min-proto-version '{value}'. Must be one of: {', '.join(VALID_BODY_TLS_MIN_PROTO_VERSION)}",
            )

    # Validate ca-cert if present
    if "ca-cert" in payload:
        value = payload.get("ca-cert")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "ca-cert cannot exceed 79 characters")

    # Validate client-cert if present
    if "client-cert" in payload:
        value = payload.get("client-cert")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "client-cert cannot exceed 35 characters")

    # Validate server-identity-check if present
    if "server-identity-check" in payload:
        value = payload.get("server-identity-check")
        if value and value not in VALID_BODY_SERVER_IDENTITY_CHECK:
            return (
                False,
                f"Invalid server-identity-check '{value}'. Must be one of: {', '.join(VALID_BODY_SERVER_IDENTITY_CHECK)}",
            )

    # Validate account-key-processing if present
    if "account-key-processing" in payload:
        value = payload.get("account-key-processing")
        if value and value not in VALID_BODY_ACCOUNT_KEY_PROCESSING:
            return (
                False,
                f"Invalid account-key-processing '{value}'. Must be one of: {', '.join(VALID_BODY_ACCOUNT_KEY_PROCESSING)}",
            )

    # Validate account-key-cert-field if present
    if "account-key-cert-field" in payload:
        value = payload.get("account-key-cert-field")
        if value and value not in VALID_BODY_ACCOUNT_KEY_CERT_FIELD:
            return (
                False,
                f"Invalid account-key-cert-field '{value}'. Must be one of: {', '.join(VALID_BODY_ACCOUNT_KEY_CERT_FIELD)}",
            )

    # Validate rsso if present
    if "rsso" in payload:
        value = payload.get("rsso")
        if value and value not in VALID_BODY_RSSO:
            return (
                False,
                f"Invalid rsso '{value}'. Must be one of: {', '.join(VALID_BODY_RSSO)}",
            )

    # Validate rsso-radius-server-port if present
    if "rsso-radius-server-port" in payload:
        value = payload.get("rsso-radius-server-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (
                        False,
                        "rsso-radius-server-port must be between 0 and 65535",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"rsso-radius-server-port must be numeric, got: {value}",
                )

    # Validate rsso-radius-response if present
    if "rsso-radius-response" in payload:
        value = payload.get("rsso-radius-response")
        if value and value not in VALID_BODY_RSSO_RADIUS_RESPONSE:
            return (
                False,
                f"Invalid rsso-radius-response '{value}'. Must be one of: {', '.join(VALID_BODY_RSSO_RADIUS_RESPONSE)}",
            )

    # Validate rsso-validate-request-secret if present
    if "rsso-validate-request-secret" in payload:
        value = payload.get("rsso-validate-request-secret")
        if value and value not in VALID_BODY_RSSO_VALIDATE_REQUEST_SECRET:
            return (
                False,
                f"Invalid rsso-validate-request-secret '{value}'. Must be one of: {', '.join(VALID_BODY_RSSO_VALIDATE_REQUEST_SECRET)}",
            )

    # Validate rsso-endpoint-attribute if present
    if "rsso-endpoint-attribute" in payload:
        value = payload.get("rsso-endpoint-attribute")
        if value and value not in VALID_BODY_RSSO_ENDPOINT_ATTRIBUTE:
            return (
                False,
                f"Invalid rsso-endpoint-attribute '{value}'. Must be one of: {', '.join(VALID_BODY_RSSO_ENDPOINT_ATTRIBUTE)}",
            )

    # Validate rsso-endpoint-block-attribute if present
    if "rsso-endpoint-block-attribute" in payload:
        value = payload.get("rsso-endpoint-block-attribute")
        if value and value not in VALID_BODY_RSSO_ENDPOINT_BLOCK_ATTRIBUTE:
            return (
                False,
                f"Invalid rsso-endpoint-block-attribute '{value}'. Must be one of: {', '.join(VALID_BODY_RSSO_ENDPOINT_BLOCK_ATTRIBUTE)}",
            )

    # Validate sso-attribute if present
    if "sso-attribute" in payload:
        value = payload.get("sso-attribute")
        if value and value not in VALID_BODY_SSO_ATTRIBUTE:
            return (
                False,
                f"Invalid sso-attribute '{value}'. Must be one of: {', '.join(VALID_BODY_SSO_ATTRIBUTE)}",
            )

    # Validate sso-attribute-key if present
    if "sso-attribute-key" in payload:
        value = payload.get("sso-attribute-key")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "sso-attribute-key cannot exceed 35 characters")

    # Validate sso-attribute-value-override if present
    if "sso-attribute-value-override" in payload:
        value = payload.get("sso-attribute-value-override")
        if value and value not in VALID_BODY_SSO_ATTRIBUTE_VALUE_OVERRIDE:
            return (
                False,
                f"Invalid sso-attribute-value-override '{value}'. Must be one of: {', '.join(VALID_BODY_SSO_ATTRIBUTE_VALUE_OVERRIDE)}",
            )

    # Validate rsso-context-timeout if present
    if "rsso-context-timeout" in payload:
        value = payload.get("rsso-context-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "rsso-context-timeout must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"rsso-context-timeout must be numeric, got: {value}",
                )

    # Validate rsso-log-period if present
    if "rsso-log-period" in payload:
        value = payload.get("rsso-log-period")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "rsso-log-period must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"rsso-log-period must be numeric, got: {value}",
                )

    # Validate rsso-log-flags if present
    if "rsso-log-flags" in payload:
        value = payload.get("rsso-log-flags")
        if value and value not in VALID_BODY_RSSO_LOG_FLAGS:
            return (
                False,
                f"Invalid rsso-log-flags '{value}'. Must be one of: {', '.join(VALID_BODY_RSSO_LOG_FLAGS)}",
            )

    # Validate rsso-flush-ip-session if present
    if "rsso-flush-ip-session" in payload:
        value = payload.get("rsso-flush-ip-session")
        if value and value not in VALID_BODY_RSSO_FLUSH_IP_SESSION:
            return (
                False,
                f"Invalid rsso-flush-ip-session '{value}'. Must be one of: {', '.join(VALID_BODY_RSSO_FLUSH_IP_SESSION)}",
            )

    # Validate rsso-ep-one-ip-only if present
    if "rsso-ep-one-ip-only" in payload:
        value = payload.get("rsso-ep-one-ip-only")
        if value and value not in VALID_BODY_RSSO_EP_ONE_IP_ONLY:
            return (
                False,
                f"Invalid rsso-ep-one-ip-only '{value}'. Must be one of: {', '.join(VALID_BODY_RSSO_EP_ONE_IP_ONLY)}",
            )

    # Validate delimiter if present
    if "delimiter" in payload:
        value = payload.get("delimiter")
        if value and value not in VALID_BODY_DELIMITER:
            return (
                False,
                f"Invalid delimiter '{value}'. Must be one of: {', '.join(VALID_BODY_DELIMITER)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_radius_delete(name: str | None = None) -> tuple[bool, str | None]:
    """
    Validate DELETE request parameters.

    Args:
        name: Object identifier (required)

    Returns:
        Tuple of (is_valid, error_message)
    """
    if not name:
        return (False, "name is required for DELETE operation")

    return (True, None)
