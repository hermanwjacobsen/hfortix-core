"""
Validation helpers for wireless-controller hotspot20_h2qp_conn_capability
endpoint.

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
    "name",  # Connection capability name.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "esp-port": "unknown",
    "ftp-port": "unknown",
    "http-port": "unknown",
    "icmp-port": "unknown",
    "ikev2-port": "unknown",
    "ikev2-xx-port": "unknown",
    "pptp-vpn-port": "unknown",
    "ssh-port": "unknown",
    "tls-port": "unknown",
    "voip-tcp-port": "unknown",
    "voip-udp-port": "unknown",
}


# Valid enum values from API documentation
VALID_BODY_ICMP_PORT = ["closed", "open", "unknown"]
VALID_BODY_FTP_PORT = ["closed", "open", "unknown"]
VALID_BODY_SSH_PORT = ["closed", "open", "unknown"]
VALID_BODY_HTTP_PORT = ["closed", "open", "unknown"]
VALID_BODY_TLS_PORT = ["closed", "open", "unknown"]
VALID_BODY_PPTP_VPN_PORT = ["closed", "open", "unknown"]
VALID_BODY_VOIP_TCP_PORT = ["closed", "open", "unknown"]
VALID_BODY_VOIP_UDP_PORT = ["closed", "open", "unknown"]
VALID_BODY_IKEV2_PORT = ["closed", "open", "unknown"]
VALID_BODY_IKEV2_XX_PORT = ["closed", "open", "unknown"]
VALID_BODY_ESP_PORT = ["closed", "open", "unknown"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_hotspot20_h2qp_conn_capability_get(
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
    Validate required fields for wireless-controller_hotspot20_h2qp-conn-capability.

    This validator checks:
    1. Always-required fields are present
    2. Mutually exclusive groups have at least one field

    Args:
        payload: The request payload to validate

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> is_valid, error = validate_required_fields({
        ...     "name": "value",
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


def validate_hotspot20_h2qp_conn_capability_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload.

    This validator performs two-stage validation:
    1. Required fields validation (schema-based)
    2. Field value validation (enums, ranges, formats)

    Required fields:
      - name: Connection capability name.

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

    # Validate icmp-port if present
    if "icmp-port" in payload:
        value = payload.get("icmp-port")
        if value and value not in VALID_BODY_ICMP_PORT:
            return (
                False,
                f"Invalid icmp-port '{value}'. Must be one of: {', '.join(VALID_BODY_ICMP_PORT)}",
            )

    # Validate ftp-port if present
    if "ftp-port" in payload:
        value = payload.get("ftp-port")
        if value and value not in VALID_BODY_FTP_PORT:
            return (
                False,
                f"Invalid ftp-port '{value}'. Must be one of: {', '.join(VALID_BODY_FTP_PORT)}",
            )

    # Validate ssh-port if present
    if "ssh-port" in payload:
        value = payload.get("ssh-port")
        if value and value not in VALID_BODY_SSH_PORT:
            return (
                False,
                f"Invalid ssh-port '{value}'. Must be one of: {', '.join(VALID_BODY_SSH_PORT)}",
            )

    # Validate http-port if present
    if "http-port" in payload:
        value = payload.get("http-port")
        if value and value not in VALID_BODY_HTTP_PORT:
            return (
                False,
                f"Invalid http-port '{value}'. Must be one of: {', '.join(VALID_BODY_HTTP_PORT)}",
            )

    # Validate tls-port if present
    if "tls-port" in payload:
        value = payload.get("tls-port")
        if value and value not in VALID_BODY_TLS_PORT:
            return (
                False,
                f"Invalid tls-port '{value}'. Must be one of: {', '.join(VALID_BODY_TLS_PORT)}",
            )

    # Validate pptp-vpn-port if present
    if "pptp-vpn-port" in payload:
        value = payload.get("pptp-vpn-port")
        if value and value not in VALID_BODY_PPTP_VPN_PORT:
            return (
                False,
                f"Invalid pptp-vpn-port '{value}'. Must be one of: {', '.join(VALID_BODY_PPTP_VPN_PORT)}",
            )

    # Validate voip-tcp-port if present
    if "voip-tcp-port" in payload:
        value = payload.get("voip-tcp-port")
        if value and value not in VALID_BODY_VOIP_TCP_PORT:
            return (
                False,
                f"Invalid voip-tcp-port '{value}'. Must be one of: {', '.join(VALID_BODY_VOIP_TCP_PORT)}",
            )

    # Validate voip-udp-port if present
    if "voip-udp-port" in payload:
        value = payload.get("voip-udp-port")
        if value and value not in VALID_BODY_VOIP_UDP_PORT:
            return (
                False,
                f"Invalid voip-udp-port '{value}'. Must be one of: {', '.join(VALID_BODY_VOIP_UDP_PORT)}",
            )

    # Validate ikev2-port if present
    if "ikev2-port" in payload:
        value = payload.get("ikev2-port")
        if value and value not in VALID_BODY_IKEV2_PORT:
            return (
                False,
                f"Invalid ikev2-port '{value}'. Must be one of: {', '.join(VALID_BODY_IKEV2_PORT)}",
            )

    # Validate ikev2-xx-port if present
    if "ikev2-xx-port" in payload:
        value = payload.get("ikev2-xx-port")
        if value and value not in VALID_BODY_IKEV2_XX_PORT:
            return (
                False,
                f"Invalid ikev2-xx-port '{value}'. Must be one of: {', '.join(VALID_BODY_IKEV2_XX_PORT)}",
            )

    # Validate esp-port if present
    if "esp-port" in payload:
        value = payload.get("esp-port")
        if value and value not in VALID_BODY_ESP_PORT:
            return (
                False,
                f"Invalid esp-port '{value}'. Must be one of: {', '.join(VALID_BODY_ESP_PORT)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_hotspot20_h2qp_conn_capability_put(
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

    # Validate icmp-port if present
    if "icmp-port" in payload:
        value = payload.get("icmp-port")
        if value and value not in VALID_BODY_ICMP_PORT:
            return (
                False,
                f"Invalid icmp-port '{value}'. Must be one of: {', '.join(VALID_BODY_ICMP_PORT)}",
            )

    # Validate ftp-port if present
    if "ftp-port" in payload:
        value = payload.get("ftp-port")
        if value and value not in VALID_BODY_FTP_PORT:
            return (
                False,
                f"Invalid ftp-port '{value}'. Must be one of: {', '.join(VALID_BODY_FTP_PORT)}",
            )

    # Validate ssh-port if present
    if "ssh-port" in payload:
        value = payload.get("ssh-port")
        if value and value not in VALID_BODY_SSH_PORT:
            return (
                False,
                f"Invalid ssh-port '{value}'. Must be one of: {', '.join(VALID_BODY_SSH_PORT)}",
            )

    # Validate http-port if present
    if "http-port" in payload:
        value = payload.get("http-port")
        if value and value not in VALID_BODY_HTTP_PORT:
            return (
                False,
                f"Invalid http-port '{value}'. Must be one of: {', '.join(VALID_BODY_HTTP_PORT)}",
            )

    # Validate tls-port if present
    if "tls-port" in payload:
        value = payload.get("tls-port")
        if value and value not in VALID_BODY_TLS_PORT:
            return (
                False,
                f"Invalid tls-port '{value}'. Must be one of: {', '.join(VALID_BODY_TLS_PORT)}",
            )

    # Validate pptp-vpn-port if present
    if "pptp-vpn-port" in payload:
        value = payload.get("pptp-vpn-port")
        if value and value not in VALID_BODY_PPTP_VPN_PORT:
            return (
                False,
                f"Invalid pptp-vpn-port '{value}'. Must be one of: {', '.join(VALID_BODY_PPTP_VPN_PORT)}",
            )

    # Validate voip-tcp-port if present
    if "voip-tcp-port" in payload:
        value = payload.get("voip-tcp-port")
        if value and value not in VALID_BODY_VOIP_TCP_PORT:
            return (
                False,
                f"Invalid voip-tcp-port '{value}'. Must be one of: {', '.join(VALID_BODY_VOIP_TCP_PORT)}",
            )

    # Validate voip-udp-port if present
    if "voip-udp-port" in payload:
        value = payload.get("voip-udp-port")
        if value and value not in VALID_BODY_VOIP_UDP_PORT:
            return (
                False,
                f"Invalid voip-udp-port '{value}'. Must be one of: {', '.join(VALID_BODY_VOIP_UDP_PORT)}",
            )

    # Validate ikev2-port if present
    if "ikev2-port" in payload:
        value = payload.get("ikev2-port")
        if value and value not in VALID_BODY_IKEV2_PORT:
            return (
                False,
                f"Invalid ikev2-port '{value}'. Must be one of: {', '.join(VALID_BODY_IKEV2_PORT)}",
            )

    # Validate ikev2-xx-port if present
    if "ikev2-xx-port" in payload:
        value = payload.get("ikev2-xx-port")
        if value and value not in VALID_BODY_IKEV2_XX_PORT:
            return (
                False,
                f"Invalid ikev2-xx-port '{value}'. Must be one of: {', '.join(VALID_BODY_IKEV2_XX_PORT)}",
            )

    # Validate esp-port if present
    if "esp-port" in payload:
        value = payload.get("esp-port")
        if value and value not in VALID_BODY_ESP_PORT:
            return (
                False,
                f"Invalid esp-port '{value}'. Must be one of: {', '.join(VALID_BODY_ESP_PORT)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_hotspot20_h2qp_conn_capability_delete(
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
