"""
Validation helpers for webfilter override endpoint.

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
    "expires",  # Override expiration date and time, from 5 minutes to 365 fro
    "ip",  # IPv4 address which the override applies.
    "ip6",  # IPv6 address which the override applies.
    "new-profile",  # Name of the new web filter profile used by the override.
    "old-profile",  # Name of the web filter profile which the override applies.
    "user",  # Name of the user which the override applies.
    "user-group",  # Specify the user group for which the override applies.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "expires": "1970/01/01 00:00:00",
    "ip": "0.0.0.0",
    "ip6": "::",
    "scope": "user",
    "status": "disable",
}


# Valid enum values from API documentation
VALID_BODY_STATUS = ["enable", "disable"]
VALID_BODY_SCOPE = ["user", "user-group", "ip", "ip6"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_override_get(
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
    Validate required fields for webfilter_override.

    This validator checks:
    1. Always-required fields are present
    2. Mutually exclusive groups have at least one field

    Args:
        payload: The request payload to validate

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> is_valid, error = validate_required_fields({
        ...     "expires": "value",
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


def validate_override_post(payload: dict[str, Any]) -> tuple[bool, str | None]:
    """
    Validate POST request payload.

    This validator performs two-stage validation:
    1. Required fields validation (schema-based)
    2. Field value validation (enums, ranges, formats)

    Required fields:
      - expires: Override expiration date and time, from 5 minutes to 365 fro
      - ip: IPv4 address which the override applies.
      - ip6: IPv6 address which the override applies.
      - new-profile: Name of the new web filter profile used by the override.
      - old-profile: Name of the web filter profile which the override applies.
      - user: Name of the user which the override applies.
      - user-group: Specify the user group for which the override applies.

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
    # Validate id if present
    if "id" in payload:
        value = payload.get("id")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (False, "id must be between 0 and 4294967295")
            except (ValueError, TypeError):
                return (False, f"id must be numeric, got: {value}")

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )

    # Validate scope if present
    if "scope" in payload:
        value = payload.get("scope")
        if value and value not in VALID_BODY_SCOPE:
            return (
                False,
                f"Invalid scope '{value}'. Must be one of: {', '.join(VALID_BODY_SCOPE)}",
            )

    # Validate user if present
    if "user" in payload:
        value = payload.get("user")
        if value and isinstance(value, str) and len(value) > 64:
            return (False, "user cannot exceed 64 characters")

    # Validate user-group if present
    if "user-group" in payload:
        value = payload.get("user-group")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "user-group cannot exceed 63 characters")

    # Validate old-profile if present
    if "old-profile" in payload:
        value = payload.get("old-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "old-profile cannot exceed 47 characters")

    # Validate new-profile if present
    if "new-profile" in payload:
        value = payload.get("new-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "new-profile cannot exceed 47 characters")

    # Validate initiator if present
    if "initiator" in payload:
        value = payload.get("initiator")
        if value and isinstance(value, str) and len(value) > 64:
            return (False, "initiator cannot exceed 64 characters")

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_override_put(
    id: str | None = None, payload: dict[str, Any] | None = None
) -> tuple[bool, str | None]:
    """
    Validate PUT request payload for updating {endpoint_name}.

    Args:
        id: Object identifier (required)
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # id is required for updates
    if not id:
        return (False, "id is required for PUT operation")

    # If no payload provided, nothing to validate
    if not payload:
        return (True, None)

    # Validate id if present
    if "id" in payload:
        value = payload.get("id")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (False, "id must be between 0 and 4294967295")
            except (ValueError, TypeError):
                return (False, f"id must be numeric, got: {value}")

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )

    # Validate scope if present
    if "scope" in payload:
        value = payload.get("scope")
        if value and value not in VALID_BODY_SCOPE:
            return (
                False,
                f"Invalid scope '{value}'. Must be one of: {', '.join(VALID_BODY_SCOPE)}",
            )

    # Validate user if present
    if "user" in payload:
        value = payload.get("user")
        if value and isinstance(value, str) and len(value) > 64:
            return (False, "user cannot exceed 64 characters")

    # Validate user-group if present
    if "user-group" in payload:
        value = payload.get("user-group")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "user-group cannot exceed 63 characters")

    # Validate old-profile if present
    if "old-profile" in payload:
        value = payload.get("old-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "old-profile cannot exceed 47 characters")

    # Validate new-profile if present
    if "new-profile" in payload:
        value = payload.get("new-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "new-profile cannot exceed 47 characters")

    # Validate initiator if present
    if "initiator" in payload:
        value = payload.get("initiator")
        if value and isinstance(value, str) and len(value) > 64:
            return (False, "initiator cannot exceed 64 characters")

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_override_delete(id: str | None = None) -> tuple[bool, str | None]:
    """
    Validate DELETE request parameters.

    Args:
        id: Object identifier (required)

    Returns:
        Tuple of (is_valid, error_message)
    """
    if not id:
        return (False, "id is required for DELETE operation")

    return (True, None)
