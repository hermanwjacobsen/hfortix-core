"""
Validation helpers for system affinity_packet_redistribution endpoint.

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
    "id",  # ID of the packet redistribution setting.
    "interface",  # Physical interface name on which to perform packet redistrib
    "round-robin",  # Enable/disable round-robin redistribution to multiple CPUs.
    "rxqid",  # ID of the receive queue (when the interface has multiple que
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "round-robin": "enable",
    "rxqid": 255,
}


# Valid enum values from API documentation
VALID_BODY_ROUND_ROBIN = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_affinity_packet_redistribution_get(
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
    Validate required fields for system_affinity-packet-redistribution.

    This validator checks:
    1. Always-required fields are present
    2. Mutually exclusive groups have at least one field

    Args:
        payload: The request payload to validate

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> is_valid, error = validate_required_fields({
        ...     "id": "value",
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


def validate_affinity_packet_redistribution_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload.

    This validator performs two-stage validation:
    1. Required fields validation (schema-based)
    2. Field value validation (enums, ranges, formats)

    Required fields:
      - id: ID of the packet redistribution setting.
      - interface: Physical interface name on which to perform packet redistrib
      - round-robin: Enable/disable round-robin redistribution to multiple CPUs.
      - rxqid: ID of the receive queue (when the interface has multiple que

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

    # Validate interface if present
    if "interface" in payload:
        value = payload.get("interface")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "interface cannot exceed 15 characters")

    # Validate rxqid if present
    if "rxqid" in payload:
        value = payload.get("rxqid")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 255:
                    return (False, "rxqid must be between 0 and 255")
            except (ValueError, TypeError):
                return (False, f"rxqid must be numeric, got: {value}")

    # Validate round-robin if present
    if "round-robin" in payload:
        value = payload.get("round-robin")
        if value and value not in VALID_BODY_ROUND_ROBIN:
            return (
                False,
                f"Invalid round-robin '{value}'. Must be one of: {', '.join(VALID_BODY_ROUND_ROBIN)}",
            )

    # Validate affinity-cpumask if present
    if "affinity-cpumask" in payload:
        value = payload.get("affinity-cpumask")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "affinity-cpumask cannot exceed 127 characters")

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_affinity_packet_redistribution_put(
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

    # Validate interface if present
    if "interface" in payload:
        value = payload.get("interface")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "interface cannot exceed 15 characters")

    # Validate rxqid if present
    if "rxqid" in payload:
        value = payload.get("rxqid")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 255:
                    return (False, "rxqid must be between 0 and 255")
            except (ValueError, TypeError):
                return (False, f"rxqid must be numeric, got: {value}")

    # Validate round-robin if present
    if "round-robin" in payload:
        value = payload.get("round-robin")
        if value and value not in VALID_BODY_ROUND_ROBIN:
            return (
                False,
                f"Invalid round-robin '{value}'. Must be one of: {', '.join(VALID_BODY_ROUND_ROBIN)}",
            )

    # Validate affinity-cpumask if present
    if "affinity-cpumask" in payload:
        value = payload.get("affinity-cpumask")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "affinity-cpumask cannot exceed 127 characters")

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_affinity_packet_redistribution_delete(
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
