"""
Validation helpers for web-proxy wisp endpoint.

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
    "name",  # Server name.
    "server-ip",  # WISP server IP address.
    "server-port",  # WISP server port (1 - 65535, default = 15868).
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "max-connections": 64,
    "outgoing-ip": "0.0.0.0",
    "server-ip": "0.0.0.0",
    "server-port": 15868,
    "timeout": 5,
}


# Valid enum values from API documentation
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_wisp_get(
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
    Validate required fields for web-proxy_wisp.

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


def validate_wisp_post(payload: dict[str, Any]) -> tuple[bool, str | None]:
    """
    Validate POST request payload.

    This validator performs two-stage validation:
    1. Required fields validation (schema-based)
    2. Field value validation (enums, ranges, formats)

    Required fields:
      - name: Server name.
      - server-ip: WISP server IP address.
      - server-port: WISP server port (1 - 65535, default = 15868).

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

    # Validate comment if present
    if "comment" in payload:
        value = payload.get("comment")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "comment cannot exceed 255 characters")

    # Validate server-port if present
    if "server-port" in payload:
        value = payload.get("server-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (False, "server-port must be between 1 and 65535")
            except (ValueError, TypeError):
                return (False, f"server-port must be numeric, got: {value}")

    # Validate max-connections if present
    if "max-connections" in payload:
        value = payload.get("max-connections")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 4 or int_val > 4096:
                    return (
                        False,
                        "max-connections must be between 4 and 4096",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"max-connections must be numeric, got: {value}",
                )

    # Validate timeout if present
    if "timeout" in payload:
        value = payload.get("timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 15:
                    return (False, "timeout must be between 1 and 15")
            except (ValueError, TypeError):
                return (False, f"timeout must be numeric, got: {value}")

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_wisp_put(
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

    # Validate comment if present
    if "comment" in payload:
        value = payload.get("comment")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "comment cannot exceed 255 characters")

    # Validate server-port if present
    if "server-port" in payload:
        value = payload.get("server-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (False, "server-port must be between 1 and 65535")
            except (ValueError, TypeError):
                return (False, f"server-port must be numeric, got: {value}")

    # Validate max-connections if present
    if "max-connections" in payload:
        value = payload.get("max-connections")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 4 or int_val > 4096:
                    return (
                        False,
                        "max-connections must be between 4 and 4096",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"max-connections must be numeric, got: {value}",
                )

    # Validate timeout if present
    if "timeout" in payload:
        value = payload.get("timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 15:
                    return (False, "timeout must be between 1 and 15")
            except (ValueError, TypeError):
                return (False, f"timeout must be numeric, got: {value}")

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_wisp_delete(name: str | None = None) -> tuple[bool, str | None]:
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
