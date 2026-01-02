"""
Validation helpers for firewall ssl_server endpoint.

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
    "ip",  # IPv4 address of the SSL server.
    "mapped-port",  # Mapped server service port (1 - 65535, default = 80).
    "name",  # Server name.
    "port",  # Server service port (1 - 65535, default = 443).
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "add-header-x-forwarded-proto": "enable",
    "ip": "0.0.0.0",
    "mapped-port": 80,
    "port": 443,
    "ssl-algorithm": "high",
    "ssl-client-renegotiation": "allow",
    "ssl-dh-bits": "2048",
    "ssl-max-version": "tls-1.3",
    "ssl-min-version": "tls-1.1",
    "ssl-mode": "full",
    "ssl-send-empty-frags": "enable",
    "url-rewrite": "disable",
}


# Valid enum values from API documentation
VALID_BODY_SSL_MODE = ["hal", "full"]
VALID_BODY_ADD_HEADER_X_FORWARDED_PROTO = ["enable", "disable"]
VALID_BODY_SSL_DH_BITS = ["768", "1024", "1536", "2048"]
VALID_BODY_SSL_ALGORITHM = ["high", "medium", "low"]
VALID_BODY_SSL_CLIENT_RENEGOTIATION = ["allow", "deny", "secure"]
VALID_BODY_SSL_MIN_VERSION = ["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"]
VALID_BODY_SSL_MAX_VERSION = ["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"]
VALID_BODY_SSL_SEND_EMPTY_FRAGS = ["enable", "disable"]
VALID_BODY_URL_REWRITE = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_ssl_server_get(
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
    Validate required fields for firewall_ssl-server.

    This validator checks:
    1. Always-required fields are present
    2. Mutually exclusive groups have at least one field

    Args:
        payload: The request payload to validate

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> is_valid, error = validate_required_fields({
        ...     "ip": "value",
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


def validate_ssl_server_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload.

    This validator performs two-stage validation:
    1. Required fields validation (schema-based)
    2. Field value validation (enums, ranges, formats)

    Required fields:
      - ip: IPv4 address of the SSL server.
      - mapped-port: Mapped server service port (1 - 65535, default = 80).
      - name: Server name.
      - port: Server service port (1 - 65535, default = 443).

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

    # Validate port if present
    if "port" in payload:
        value = payload.get("port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (False, "port must be between 1 and 65535")
            except (ValueError, TypeError):
                return (False, f"port must be numeric, got: {value}")

    # Validate ssl-mode if present
    if "ssl-mode" in payload:
        value = payload.get("ssl-mode")
        if value and value not in VALID_BODY_SSL_MODE:
            return (
                False,
                f"Invalid ssl-mode '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_MODE)}",
            )

    # Validate add-header-x-forwarded-proto if present
    if "add-header-x-forwarded-proto" in payload:
        value = payload.get("add-header-x-forwarded-proto")
        if value and value not in VALID_BODY_ADD_HEADER_X_FORWARDED_PROTO:
            return (
                False,
                f"Invalid add-header-x-forwarded-proto '{value}'. Must be one of: {', '.join(VALID_BODY_ADD_HEADER_X_FORWARDED_PROTO)}",
            )

    # Validate mapped-port if present
    if "mapped-port" in payload:
        value = payload.get("mapped-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (False, "mapped-port must be between 1 and 65535")
            except (ValueError, TypeError):
                return (False, f"mapped-port must be numeric, got: {value}")

    # Validate ssl-dh-bits if present
    if "ssl-dh-bits" in payload:
        value = payload.get("ssl-dh-bits")
        if value and value not in VALID_BODY_SSL_DH_BITS:
            return (
                False,
                f"Invalid ssl-dh-bits '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_DH_BITS)}",
            )

    # Validate ssl-algorithm if present
    if "ssl-algorithm" in payload:
        value = payload.get("ssl-algorithm")
        if value and value not in VALID_BODY_SSL_ALGORITHM:
            return (
                False,
                f"Invalid ssl-algorithm '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_ALGORITHM)}",
            )

    # Validate ssl-client-renegotiation if present
    if "ssl-client-renegotiation" in payload:
        value = payload.get("ssl-client-renegotiation")
        if value and value not in VALID_BODY_SSL_CLIENT_RENEGOTIATION:
            return (
                False,
                f"Invalid ssl-client-renegotiation '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_CLIENT_RENEGOTIATION)}",
            )

    # Validate ssl-min-version if present
    if "ssl-min-version" in payload:
        value = payload.get("ssl-min-version")
        if value and value not in VALID_BODY_SSL_MIN_VERSION:
            return (
                False,
                f"Invalid ssl-min-version '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_MIN_VERSION)}",
            )

    # Validate ssl-max-version if present
    if "ssl-max-version" in payload:
        value = payload.get("ssl-max-version")
        if value and value not in VALID_BODY_SSL_MAX_VERSION:
            return (
                False,
                f"Invalid ssl-max-version '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_MAX_VERSION)}",
            )

    # Validate ssl-send-empty-frags if present
    if "ssl-send-empty-frags" in payload:
        value = payload.get("ssl-send-empty-frags")
        if value and value not in VALID_BODY_SSL_SEND_EMPTY_FRAGS:
            return (
                False,
                f"Invalid ssl-send-empty-frags '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_SEND_EMPTY_FRAGS)}",
            )

    # Validate url-rewrite if present
    if "url-rewrite" in payload:
        value = payload.get("url-rewrite")
        if value and value not in VALID_BODY_URL_REWRITE:
            return (
                False,
                f"Invalid url-rewrite '{value}'. Must be one of: {', '.join(VALID_BODY_URL_REWRITE)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_ssl_server_put(
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

    # Validate port if present
    if "port" in payload:
        value = payload.get("port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (False, "port must be between 1 and 65535")
            except (ValueError, TypeError):
                return (False, f"port must be numeric, got: {value}")

    # Validate ssl-mode if present
    if "ssl-mode" in payload:
        value = payload.get("ssl-mode")
        if value and value not in VALID_BODY_SSL_MODE:
            return (
                False,
                f"Invalid ssl-mode '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_MODE)}",
            )

    # Validate add-header-x-forwarded-proto if present
    if "add-header-x-forwarded-proto" in payload:
        value = payload.get("add-header-x-forwarded-proto")
        if value and value not in VALID_BODY_ADD_HEADER_X_FORWARDED_PROTO:
            return (
                False,
                f"Invalid add-header-x-forwarded-proto '{value}'. Must be one of: {', '.join(VALID_BODY_ADD_HEADER_X_FORWARDED_PROTO)}",
            )

    # Validate mapped-port if present
    if "mapped-port" in payload:
        value = payload.get("mapped-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (False, "mapped-port must be between 1 and 65535")
            except (ValueError, TypeError):
                return (False, f"mapped-port must be numeric, got: {value}")

    # Validate ssl-dh-bits if present
    if "ssl-dh-bits" in payload:
        value = payload.get("ssl-dh-bits")
        if value and value not in VALID_BODY_SSL_DH_BITS:
            return (
                False,
                f"Invalid ssl-dh-bits '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_DH_BITS)}",
            )

    # Validate ssl-algorithm if present
    if "ssl-algorithm" in payload:
        value = payload.get("ssl-algorithm")
        if value and value not in VALID_BODY_SSL_ALGORITHM:
            return (
                False,
                f"Invalid ssl-algorithm '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_ALGORITHM)}",
            )

    # Validate ssl-client-renegotiation if present
    if "ssl-client-renegotiation" in payload:
        value = payload.get("ssl-client-renegotiation")
        if value and value not in VALID_BODY_SSL_CLIENT_RENEGOTIATION:
            return (
                False,
                f"Invalid ssl-client-renegotiation '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_CLIENT_RENEGOTIATION)}",
            )

    # Validate ssl-min-version if present
    if "ssl-min-version" in payload:
        value = payload.get("ssl-min-version")
        if value and value not in VALID_BODY_SSL_MIN_VERSION:
            return (
                False,
                f"Invalid ssl-min-version '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_MIN_VERSION)}",
            )

    # Validate ssl-max-version if present
    if "ssl-max-version" in payload:
        value = payload.get("ssl-max-version")
        if value and value not in VALID_BODY_SSL_MAX_VERSION:
            return (
                False,
                f"Invalid ssl-max-version '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_MAX_VERSION)}",
            )

    # Validate ssl-send-empty-frags if present
    if "ssl-send-empty-frags" in payload:
        value = payload.get("ssl-send-empty-frags")
        if value and value not in VALID_BODY_SSL_SEND_EMPTY_FRAGS:
            return (
                False,
                f"Invalid ssl-send-empty-frags '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_SEND_EMPTY_FRAGS)}",
            )

    # Validate url-rewrite if present
    if "url-rewrite" in payload:
        value = payload.get("url-rewrite")
        if value and value not in VALID_BODY_URL_REWRITE:
            return (
                False,
                f"Invalid url-rewrite '{value}'. Must be one of: {', '.join(VALID_BODY_URL_REWRITE)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_ssl_server_delete(
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
