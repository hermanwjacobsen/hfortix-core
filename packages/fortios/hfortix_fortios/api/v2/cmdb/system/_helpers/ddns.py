"""
Validation helpers for system ddns endpoint.

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
    "ddns-server",  # Select a DDNS service provider.
    "monitor-interface",  # Monitored interface.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "addr-type": "ipv4",
    "clear-text": "disable",
    "ddns-auth": "disable",
    "ddns-server": "dyndns.org",
    "ddns-ttl": 300,
    "server-type": "ipv4",
    "ssl-certificate": "Fortinet_Factory",
    "use-public-ip": "disable",
}


# Valid enum values from API documentation
VALID_BODY_DDNS_SERVER = [
    "dyndns.org",
    "dyns.net",
    "tzo.com",
    "vavic.com",
    "dipdns.net",
    "now.net.cn",
    "dhs.org",
    "easydns.com",
    "genericDDNS",
    "FortiGuardDDNS",
    "noip.com",
]
VALID_BODY_ADDR_TYPE = ["ipv4", "ipv6"]
VALID_BODY_SERVER_TYPE = ["ipv4", "ipv6"]
VALID_BODY_DDNS_AUTH = ["disable", "tsig"]
VALID_BODY_USE_PUBLIC_IP = ["disable", "enable"]
VALID_BODY_CLEAR_TEXT = ["disable", "enable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_ddns_get(
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
    Validate required fields for system_ddns.

    This validator checks:
    1. Always-required fields are present
    2. Mutually exclusive groups have at least one field

    Args:
        payload: The request payload to validate

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> is_valid, error = validate_required_fields({
        ...     "ddns-server": "value",
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


def validate_ddns_post(payload: dict[str, Any]) -> tuple[bool, str | None]:
    """
    Validate POST request payload.

    This validator performs two-stage validation:
    1. Required fields validation (schema-based)
    2. Field value validation (enums, ranges, formats)

    Required fields:
      - ddns-server: Select a DDNS service provider.
      - monitor-interface: Monitored interface.

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
    # Validate ddnsid if present
    if "ddnsid" in payload:
        value = payload.get("ddnsid")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (False, "ddnsid must be between 0 and 4294967295")
            except (ValueError, TypeError):
                return (False, f"ddnsid must be numeric, got: {value}")

    # Validate ddns-server if present
    if "ddns-server" in payload:
        value = payload.get("ddns-server")
        if value and value not in VALID_BODY_DDNS_SERVER:
            return (
                False,
                f"Invalid ddns-server '{value}'. Must be one of: {', '.join(VALID_BODY_DDNS_SERVER)}",
            )

    # Validate addr-type if present
    if "addr-type" in payload:
        value = payload.get("addr-type")
        if value and value not in VALID_BODY_ADDR_TYPE:
            return (
                False,
                f"Invalid addr-type '{value}'. Must be one of: {', '.join(VALID_BODY_ADDR_TYPE)}",
            )

    # Validate server-type if present
    if "server-type" in payload:
        value = payload.get("server-type")
        if value and value not in VALID_BODY_SERVER_TYPE:
            return (
                False,
                f"Invalid server-type '{value}'. Must be one of: {', '.join(VALID_BODY_SERVER_TYPE)}",
            )

    # Validate ddns-zone if present
    if "ddns-zone" in payload:
        value = payload.get("ddns-zone")
        if value and isinstance(value, str) and len(value) > 64:
            return (False, "ddns-zone cannot exceed 64 characters")

    # Validate ddns-ttl if present
    if "ddns-ttl" in payload:
        value = payload.get("ddns-ttl")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 60 or int_val > 86400:
                    return (False, "ddns-ttl must be between 60 and 86400")
            except (ValueError, TypeError):
                return (False, f"ddns-ttl must be numeric, got: {value}")

    # Validate ddns-auth if present
    if "ddns-auth" in payload:
        value = payload.get("ddns-auth")
        if value and value not in VALID_BODY_DDNS_AUTH:
            return (
                False,
                f"Invalid ddns-auth '{value}'. Must be one of: {', '.join(VALID_BODY_DDNS_AUTH)}",
            )

    # Validate ddns-keyname if present
    if "ddns-keyname" in payload:
        value = payload.get("ddns-keyname")
        if value and isinstance(value, str) and len(value) > 64:
            return (False, "ddns-keyname cannot exceed 64 characters")

    # Validate ddns-domain if present
    if "ddns-domain" in payload:
        value = payload.get("ddns-domain")
        if value and isinstance(value, str) and len(value) > 64:
            return (False, "ddns-domain cannot exceed 64 characters")

    # Validate ddns-username if present
    if "ddns-username" in payload:
        value = payload.get("ddns-username")
        if value and isinstance(value, str) and len(value) > 64:
            return (False, "ddns-username cannot exceed 64 characters")

    # Validate ddns-sn if present
    if "ddns-sn" in payload:
        value = payload.get("ddns-sn")
        if value and isinstance(value, str) and len(value) > 64:
            return (False, "ddns-sn cannot exceed 64 characters")

    # Validate use-public-ip if present
    if "use-public-ip" in payload:
        value = payload.get("use-public-ip")
        if value and value not in VALID_BODY_USE_PUBLIC_IP:
            return (
                False,
                f"Invalid use-public-ip '{value}'. Must be one of: {', '.join(VALID_BODY_USE_PUBLIC_IP)}",
            )

    # Validate update-interval if present
    if "update-interval" in payload:
        value = payload.get("update-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 60 or int_val > 2592000:
                    return (
                        False,
                        "update-interval must be between 60 and 2592000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"update-interval must be numeric, got: {value}",
                )

    # Validate clear-text if present
    if "clear-text" in payload:
        value = payload.get("clear-text")
        if value and value not in VALID_BODY_CLEAR_TEXT:
            return (
                False,
                f"Invalid clear-text '{value}'. Must be one of: {', '.join(VALID_BODY_CLEAR_TEXT)}",
            )

    # Validate ssl-certificate if present
    if "ssl-certificate" in payload:
        value = payload.get("ssl-certificate")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "ssl-certificate cannot exceed 35 characters")

    # Validate bound-ip if present
    if "bound-ip" in payload:
        value = payload.get("bound-ip")
        if value and isinstance(value, str) and len(value) > 46:
            return (False, "bound-ip cannot exceed 46 characters")

    return (True, None)
