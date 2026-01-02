"""
Validation helpers for switch-controller ptp_profile endpoint.

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
    "domain": 254,
    "mode": "transparent-e2e",
    "pdelay-req-interval": "1sec",
    "ptp-profile": "C37.238-2017",
    "transport": "l2-mcast",
}


# Valid enum values from API documentation
VALID_BODY_MODE = ["transparent-e2e", "transparent-p2p"]
VALID_BODY_PTP_PROFILE = ["C37.238-2017"]
VALID_BODY_TRANSPORT = ["l2-mcast"]
VALID_BODY_PDELAY_REQ_INTERVAL = [
    "1sec",
    "2sec",
    "4sec",
    "8sec",
    "16sec",
    "32sec",
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_ptp_profile_get(
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
    Validate required fields for switch-controller_ptp_profile.

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


def validate_ptp_profile_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
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
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "name cannot exceed 63 characters")

    # Validate description if present
    if "description" in payload:
        value = payload.get("description")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "description cannot exceed 63 characters")

    # Validate mode if present
    if "mode" in payload:
        value = payload.get("mode")
        if value and value not in VALID_BODY_MODE:
            return (
                False,
                f"Invalid mode '{value}'. Must be one of: {', '.join(VALID_BODY_MODE)}",
            )

    # Validate ptp-profile if present
    if "ptp-profile" in payload:
        value = payload.get("ptp-profile")
        if value and value not in VALID_BODY_PTP_PROFILE:
            return (
                False,
                f"Invalid ptp-profile '{value}'. Must be one of: {', '.join(VALID_BODY_PTP_PROFILE)}",
            )

    # Validate transport if present
    if "transport" in payload:
        value = payload.get("transport")
        if value and value not in VALID_BODY_TRANSPORT:
            return (
                False,
                f"Invalid transport '{value}'. Must be one of: {', '.join(VALID_BODY_TRANSPORT)}",
            )

    # Validate domain if present
    if "domain" in payload:
        value = payload.get("domain")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 255:
                    return (False, "domain must be between 0 and 255")
            except (ValueError, TypeError):
                return (False, f"domain must be numeric, got: {value}")

    # Validate pdelay-req-interval if present
    if "pdelay-req-interval" in payload:
        value = payload.get("pdelay-req-interval")
        if value and value not in VALID_BODY_PDELAY_REQ_INTERVAL:
            return (
                False,
                f"Invalid pdelay-req-interval '{value}'. Must be one of: {', '.join(VALID_BODY_PDELAY_REQ_INTERVAL)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_ptp_profile_put(
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
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "name cannot exceed 63 characters")

    # Validate description if present
    if "description" in payload:
        value = payload.get("description")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "description cannot exceed 63 characters")

    # Validate mode if present
    if "mode" in payload:
        value = payload.get("mode")
        if value and value not in VALID_BODY_MODE:
            return (
                False,
                f"Invalid mode '{value}'. Must be one of: {', '.join(VALID_BODY_MODE)}",
            )

    # Validate ptp-profile if present
    if "ptp-profile" in payload:
        value = payload.get("ptp-profile")
        if value and value not in VALID_BODY_PTP_PROFILE:
            return (
                False,
                f"Invalid ptp-profile '{value}'. Must be one of: {', '.join(VALID_BODY_PTP_PROFILE)}",
            )

    # Validate transport if present
    if "transport" in payload:
        value = payload.get("transport")
        if value and value not in VALID_BODY_TRANSPORT:
            return (
                False,
                f"Invalid transport '{value}'. Must be one of: {', '.join(VALID_BODY_TRANSPORT)}",
            )

    # Validate domain if present
    if "domain" in payload:
        value = payload.get("domain")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 255:
                    return (False, "domain must be between 0 and 255")
            except (ValueError, TypeError):
                return (False, f"domain must be numeric, got: {value}")

    # Validate pdelay-req-interval if present
    if "pdelay-req-interval" in payload:
        value = payload.get("pdelay-req-interval")
        if value and value not in VALID_BODY_PDELAY_REQ_INTERVAL:
            return (
                False,
                f"Invalid pdelay-req-interval '{value}'. Must be one of: {', '.join(VALID_BODY_PDELAY_REQ_INTERVAL)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_ptp_profile_delete(
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
