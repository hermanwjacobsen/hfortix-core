"""
Validation helpers for switch-controller snmp_user endpoint.

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
    "auth-pwd",  # Password for authentication protocol.
    "interface",  # Specify outgoing interface to reach server.
    "name",  # SNMP user name.
    "priv-pwd",  # Password for privacy (encryption) protocol.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "auth-proto": "sha",
    "events": "cpu-high mem-low log-full intf-ip vpn-tun-up vpn-tun-down ha-switch ha-hb-failure ips-signature ips-anomaly av-virus av-oversize av-pattern av-fragmented fm-if-change bgp-established bgp-backward-transition ha-member-up ha-member-down ent-conf-change av-conserve av-bypass av-oversize-passed av-oversize-blocked ips-pkg-update ips-fail-open faz-disconnect faz wc-ap-up wc-ap-down fswctl-session-up fswctl-session-down load-balance-real-server-down per-cpu-high dhcp pool-usage ippool interface ospf-nbr-state-change ospf-virtnbr-state-change",
    "ha-direct": "disable",
    "interface-select-method": "auto",
    "priv-proto": "aes",
    "queries": "enable",
    "query-port": 161,
    "security-level": "no-auth-no-priv",
    "source-ip": "0.0.0.0",
    "source-ipv6": "::",
    "status": "enable",
    "trap-lport": 162,
    "trap-rport": 162,
    "trap-status": "enable",
}


# Valid enum values from API documentation
VALID_BODY_QUERIES = ["disable", "enable"]
VALID_BODY_SECURITY_LEVEL = ["no-auth-no-priv", "auth-no-priv", "auth-priv"]
VALID_BODY_AUTH_PROTO = ["md5", "sha1", "sha224", "sha256", "sha384", "sha512"]
VALID_BODY_PRIV_PROTO = [
    "aes128",
    "aes192",
    "aes192c",
    "aes256",
    "aes256c",
    "des",
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_snmp_user_get(
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
    Validate required fields for system_snmp_user.

    This validator checks:
    1. Always-required fields are present
    2. Mutually exclusive groups have at least one field

    Args:
        payload: The request payload to validate

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> is_valid, error = validate_required_fields({
        ...     "auth-pwd": "value",
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


def validate_snmp_user_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload.

    This validator performs two-stage validation:
    1. Required fields validation (schema-based)
    2. Field value validation (enums, ranges, formats)

    Required fields:
      - auth-pwd: Password for authentication protocol.
      - interface: Specify outgoing interface to reach server.
      - name: SNMP user name.
      - priv-pwd: Password for privacy (encryption) protocol.

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
        if value and isinstance(value, str) and len(value) > 32:
            return (False, "name cannot exceed 32 characters")

    # Validate queries if present
    if "queries" in payload:
        value = payload.get("queries")
        if value and value not in VALID_BODY_QUERIES:
            return (
                False,
                f"Invalid queries '{value}'. Must be one of: {', '.join(VALID_BODY_QUERIES)}",
            )

    # Validate query-port if present
    if "query-port" in payload:
        value = payload.get("query-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (False, "query-port must be between 0 and 65535")
            except (ValueError, TypeError):
                return (False, f"query-port must be numeric, got: {value}")

    # Validate security-level if present
    if "security-level" in payload:
        value = payload.get("security-level")
        if value and value not in VALID_BODY_SECURITY_LEVEL:
            return (
                False,
                f"Invalid security-level '{value}'. Must be one of: {', '.join(VALID_BODY_SECURITY_LEVEL)}",
            )

    # Validate auth-proto if present
    if "auth-proto" in payload:
        value = payload.get("auth-proto")
        if value and value not in VALID_BODY_AUTH_PROTO:
            return (
                False,
                f"Invalid auth-proto '{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_PROTO)}",
            )

    # Validate priv-proto if present
    if "priv-proto" in payload:
        value = payload.get("priv-proto")
        if value and value not in VALID_BODY_PRIV_PROTO:
            return (
                False,
                f"Invalid priv-proto '{value}'. Must be one of: {', '.join(VALID_BODY_PRIV_PROTO)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_snmp_user_put(
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
        if value and isinstance(value, str) and len(value) > 32:
            return (False, "name cannot exceed 32 characters")

    # Validate queries if present
    if "queries" in payload:
        value = payload.get("queries")
        if value and value not in VALID_BODY_QUERIES:
            return (
                False,
                f"Invalid queries '{value}'. Must be one of: {', '.join(VALID_BODY_QUERIES)}",
            )

    # Validate query-port if present
    if "query-port" in payload:
        value = payload.get("query-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (False, "query-port must be between 0 and 65535")
            except (ValueError, TypeError):
                return (False, f"query-port must be numeric, got: {value}")

    # Validate security-level if present
    if "security-level" in payload:
        value = payload.get("security-level")
        if value and value not in VALID_BODY_SECURITY_LEVEL:
            return (
                False,
                f"Invalid security-level '{value}'. Must be one of: {', '.join(VALID_BODY_SECURITY_LEVEL)}",
            )

    # Validate auth-proto if present
    if "auth-proto" in payload:
        value = payload.get("auth-proto")
        if value and value not in VALID_BODY_AUTH_PROTO:
            return (
                False,
                f"Invalid auth-proto '{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_PROTO)}",
            )

    # Validate priv-proto if present
    if "priv-proto" in payload:
        value = payload.get("priv-proto")
        if value and value not in VALID_BODY_PRIV_PROTO:
            return (
                False,
                f"Invalid priv-proto '{value}'. Must be one of: {', '.join(VALID_BODY_PRIV_PROTO)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_snmp_user_delete(
    name: str | None = None,
) -> tuple[bool, str | None]:
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
