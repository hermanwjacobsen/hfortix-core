"""
Validation helpers for webfilter urlfilter endpoint.

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
    "entries",  # URL filter entries.
    "id",  # ID.
    "name",  # Name of URL filter list.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "include-subdomains": "enable",
    "ip-addr-block": "disable",
    "ip4-mapped-ip6": "disable",
    "one-arm-ips-urlfilter": "disable",
}


# Valid enum values from API documentation
VALID_BODY_ONE_ARM_IPS_URLFILTER = ["enable", "disable"]
VALID_BODY_IP_ADDR_BLOCK = ["enable", "disable"]
VALID_BODY_IP4_MAPPED_IP6 = ["enable", "disable"]
VALID_BODY_INCLUDE_SUBDOMAINS = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_urlfilter_get(
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
    Validate required fields for webfilter_urlfilter.

    This validator checks:
    1. Always-required fields are present
    2. Mutually exclusive groups have at least one field

    Args:
        payload: The request payload to validate

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> is_valid, error = validate_required_fields({
        ...     "entries": "value",
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


def validate_urlfilter_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload.

    This validator performs two-stage validation:
    1. Required fields validation (schema-based)
    2. Field value validation (enums, ranges, formats)

    Required fields:
      - entries: URL filter entries.
      - id: ID.
      - name: Name of URL filter list.

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

    # Validate name if present
    if "name" in payload:
        value = payload.get("name")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "name cannot exceed 63 characters")

    # Validate comment if present
    if "comment" in payload:
        value = payload.get("comment")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "comment cannot exceed 255 characters")

    # Validate one-arm-ips-urlfilter if present
    if "one-arm-ips-urlfilter" in payload:
        value = payload.get("one-arm-ips-urlfilter")
        if value and value not in VALID_BODY_ONE_ARM_IPS_URLFILTER:
            return (
                False,
                f"Invalid one-arm-ips-urlfilter '{value}'. Must be one of: {', '.join(VALID_BODY_ONE_ARM_IPS_URLFILTER)}",
            )

    # Validate ip-addr-block if present
    if "ip-addr-block" in payload:
        value = payload.get("ip-addr-block")
        if value and value not in VALID_BODY_IP_ADDR_BLOCK:
            return (
                False,
                f"Invalid ip-addr-block '{value}'. Must be one of: {', '.join(VALID_BODY_IP_ADDR_BLOCK)}",
            )

    # Validate ip4-mapped-ip6 if present
    if "ip4-mapped-ip6" in payload:
        value = payload.get("ip4-mapped-ip6")
        if value and value not in VALID_BODY_IP4_MAPPED_IP6:
            return (
                False,
                f"Invalid ip4-mapped-ip6 '{value}'. Must be one of: {', '.join(VALID_BODY_IP4_MAPPED_IP6)}",
            )

    # Validate include-subdomains if present
    if "include-subdomains" in payload:
        value = payload.get("include-subdomains")
        if value and value not in VALID_BODY_INCLUDE_SUBDOMAINS:
            return (
                False,
                f"Invalid include-subdomains '{value}'. Must be one of: {', '.join(VALID_BODY_INCLUDE_SUBDOMAINS)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_urlfilter_put(
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

    # Validate name if present
    if "name" in payload:
        value = payload.get("name")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "name cannot exceed 63 characters")

    # Validate comment if present
    if "comment" in payload:
        value = payload.get("comment")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "comment cannot exceed 255 characters")

    # Validate one-arm-ips-urlfilter if present
    if "one-arm-ips-urlfilter" in payload:
        value = payload.get("one-arm-ips-urlfilter")
        if value and value not in VALID_BODY_ONE_ARM_IPS_URLFILTER:
            return (
                False,
                f"Invalid one-arm-ips-urlfilter '{value}'. Must be one of: {', '.join(VALID_BODY_ONE_ARM_IPS_URLFILTER)}",
            )

    # Validate ip-addr-block if present
    if "ip-addr-block" in payload:
        value = payload.get("ip-addr-block")
        if value and value not in VALID_BODY_IP_ADDR_BLOCK:
            return (
                False,
                f"Invalid ip-addr-block '{value}'. Must be one of: {', '.join(VALID_BODY_IP_ADDR_BLOCK)}",
            )

    # Validate ip4-mapped-ip6 if present
    if "ip4-mapped-ip6" in payload:
        value = payload.get("ip4-mapped-ip6")
        if value and value not in VALID_BODY_IP4_MAPPED_IP6:
            return (
                False,
                f"Invalid ip4-mapped-ip6 '{value}'. Must be one of: {', '.join(VALID_BODY_IP4_MAPPED_IP6)}",
            )

    # Validate include-subdomains if present
    if "include-subdomains" in payload:
        value = payload.get("include-subdomains")
        if value and value not in VALID_BODY_INCLUDE_SUBDOMAINS:
            return (
                False,
                f"Invalid include-subdomains '{value}'. Must be one of: {', '.join(VALID_BODY_INCLUDE_SUBDOMAINS)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_urlfilter_delete(
    id: str | None = None,
) -> tuple[bool, str | None]:
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
