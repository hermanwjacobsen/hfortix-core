"""
Validation helpers for file-filter profile endpoint.

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
    "name",  # Profile name.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "feature-set": "voipd",
}


# Valid enum values from API documentation
VALID_BODY_FEATURE_SET = ["flow", "proxy"]
VALID_BODY_LOG = ["disable", "enable"]
VALID_BODY_EXTENDED_LOG = ["disable", "enable"]
VALID_BODY_SCAN_ARCHIVE_CONTENTS = ["disable", "enable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_profile_get(
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
    Validate required fields for voip_profile.

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


def validate_profile_post(payload: dict[str, Any]) -> tuple[bool, str | None]:
    """
    Validate POST request payload.

    This validator performs two-stage validation:
    1. Required fields validation (schema-based)
    2. Field value validation (enums, ranges, formats)

    Required fields:
      - name: Profile name.

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
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "name cannot exceed 47 characters")

    # Validate comment if present
    if "comment" in payload:
        value = payload.get("comment")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "comment cannot exceed 255 characters")

    # Validate feature-set if present
    if "feature-set" in payload:
        value = payload.get("feature-set")
        if value and value not in VALID_BODY_FEATURE_SET:
            return (
                False,
                f"Invalid feature-set '{value}'. Must be one of: {', '.join(VALID_BODY_FEATURE_SET)}",
            )

    # Validate replacemsg-group if present
    if "replacemsg-group" in payload:
        value = payload.get("replacemsg-group")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "replacemsg-group cannot exceed 35 characters")

    # Validate log if present
    if "log" in payload:
        value = payload.get("log")
        if value and value not in VALID_BODY_LOG:
            return (
                False,
                f"Invalid log '{value}'. Must be one of: {', '.join(VALID_BODY_LOG)}",
            )

    # Validate extended-log if present
    if "extended-log" in payload:
        value = payload.get("extended-log")
        if value and value not in VALID_BODY_EXTENDED_LOG:
            return (
                False,
                f"Invalid extended-log '{value}'. Must be one of: {', '.join(VALID_BODY_EXTENDED_LOG)}",
            )

    # Validate scan-archive-contents if present
    if "scan-archive-contents" in payload:
        value = payload.get("scan-archive-contents")
        if value and value not in VALID_BODY_SCAN_ARCHIVE_CONTENTS:
            return (
                False,
                f"Invalid scan-archive-contents '{value}'. Must be one of: {', '.join(VALID_BODY_SCAN_ARCHIVE_CONTENTS)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_profile_put(
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
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "name cannot exceed 47 characters")

    # Validate comment if present
    if "comment" in payload:
        value = payload.get("comment")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "comment cannot exceed 255 characters")

    # Validate feature-set if present
    if "feature-set" in payload:
        value = payload.get("feature-set")
        if value and value not in VALID_BODY_FEATURE_SET:
            return (
                False,
                f"Invalid feature-set '{value}'. Must be one of: {', '.join(VALID_BODY_FEATURE_SET)}",
            )

    # Validate replacemsg-group if present
    if "replacemsg-group" in payload:
        value = payload.get("replacemsg-group")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "replacemsg-group cannot exceed 35 characters")

    # Validate log if present
    if "log" in payload:
        value = payload.get("log")
        if value and value not in VALID_BODY_LOG:
            return (
                False,
                f"Invalid log '{value}'. Must be one of: {', '.join(VALID_BODY_LOG)}",
            )

    # Validate extended-log if present
    if "extended-log" in payload:
        value = payload.get("extended-log")
        if value and value not in VALID_BODY_EXTENDED_LOG:
            return (
                False,
                f"Invalid extended-log '{value}'. Must be one of: {', '.join(VALID_BODY_EXTENDED_LOG)}",
            )

    # Validate scan-archive-contents if present
    if "scan-archive-contents" in payload:
        value = payload.get("scan-archive-contents")
        if value and value not in VALID_BODY_SCAN_ARCHIVE_CONTENTS:
            return (
                False,
                f"Invalid scan-archive-contents '{value}'. Must be one of: {', '.join(VALID_BODY_SCAN_ARCHIVE_CONTENTS)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_profile_delete(
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
