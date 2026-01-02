"""
Validation helpers for firewall shaping_policy endpoint.

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
    "dstaddr",  # IPv4 destination address and address group names.
    "dstaddr6",  # IPv6 destination address and address group names.
    "dstintf",  # One or more outgoing (egress) interfaces.
    "name",  # Shaping policy name.
    "service",  # Service and service group names.
    "srcaddr",  # IPv4 source address and address group names.
    "srcaddr6",  # IPv6 source address and address group names.
    "srcintf",  # One or more incoming (ingress) interfaces.
]

# Mutually exclusive groups (at least ONE from each group required)
MUTUALLY_EXCLUSIVE_GROUPS = {
    "dest_address": ["dstaddr", "dstaddr6"],
    "source_address": ["srcaddr", "srcaddr6"],
}

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "diffserv-forward": "disable",
    "diffserv-reverse": "disable",
    "internet-service": "disable",
    "internet-service-src": "disable",
    "ip-version": "4",
    "schedule": "always",
    "status": "enable",
    "tos-negate": "disable",
    "traffic-type": "forwarding",
    "uuid": "00000000-0000-0000-0000-000000000000",
}


# Valid enum values from API documentation
VALID_BODY_STATUS = ["enable", "disable"]
VALID_BODY_IP_VERSION = ["4", "6"]
VALID_BODY_TRAFFIC_TYPE = ["forwarding", "local-in", "local-out"]
VALID_BODY_INTERNET_SERVICE = ["enable", "disable"]
VALID_BODY_INTERNET_SERVICE_SRC = ["enable", "disable"]
VALID_BODY_TOS_NEGATE = ["enable", "disable"]
VALID_BODY_DIFFSERV_FORWARD = ["enable", "disable"]
VALID_BODY_DIFFSERV_REVERSE = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_shaping_policy_get(
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
    Validate required fields for firewall_shaping-policy.

    This validator checks:
    1. Always-required fields are present
    2. Mutually exclusive groups have at least one field

    Args:
        payload: The request payload to validate

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> is_valid, error = validate_required_fields({
        ...     "dstaddr": "value",
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

    # Check mutually exclusive groups
    if not ("dstaddr" in payload or "dstaddr6" in payload):
        return (False, "Must provide at least one of: dstaddr, dstaddr6")
    if not ("srcaddr" in payload or "srcaddr6" in payload):
        return (False, "Must provide at least one of: srcaddr, srcaddr6")

    return (True, None)


# ============================================================================
# Endpoint Validation (Enhanced with Required Fields)
# ============================================================================


def validate_shaping_policy_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload.

    This validator performs two-stage validation:
    1. Required fields validation (schema-based)
    2. Field value validation (enums, ranges, formats)

    Required fields:
      - dstaddr: IPv4 destination address and address group names.
      - dstaddr6: IPv6 destination address and address group names.
      - dstintf: One or more outgoing (egress) interfaces.
      - name: Shaping policy name.
      - service: Service and service group names.
      - srcaddr: IPv4 source address and address group names.
      - srcaddr6: IPv6 source address and address group names.
      - srcintf: One or more incoming (ingress) interfaces.

    Mutually exclusive (at least ONE required):
      - dstaddr OR dstaddr6
      - srcaddr OR srcaddr6

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
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "name cannot exceed 35 characters")

    # Validate comment if present
    if "comment" in payload:
        value = payload.get("comment")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "comment cannot exceed 255 characters")

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )

    # Validate ip-version if present
    if "ip-version" in payload:
        value = payload.get("ip-version")
        if value and value not in VALID_BODY_IP_VERSION:
            return (
                False,
                f"Invalid ip-version '{value}'. Must be one of: {', '.join(VALID_BODY_IP_VERSION)}",
            )

    # Validate traffic-type if present
    if "traffic-type" in payload:
        value = payload.get("traffic-type")
        if value and value not in VALID_BODY_TRAFFIC_TYPE:
            return (
                False,
                f"Invalid traffic-type '{value}'. Must be one of: {', '.join(VALID_BODY_TRAFFIC_TYPE)}",
            )

    # Validate internet-service if present
    if "internet-service" in payload:
        value = payload.get("internet-service")
        if value and value not in VALID_BODY_INTERNET_SERVICE:
            return (
                False,
                f"Invalid internet-service '{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE)}",
            )

    # Validate internet-service-src if present
    if "internet-service-src" in payload:
        value = payload.get("internet-service-src")
        if value and value not in VALID_BODY_INTERNET_SERVICE_SRC:
            return (
                False,
                f"Invalid internet-service-src '{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE_SRC)}",
            )

    # Validate schedule if present
    if "schedule" in payload:
        value = payload.get("schedule")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "schedule cannot exceed 35 characters")

    # Validate tos-negate if present
    if "tos-negate" in payload:
        value = payload.get("tos-negate")
        if value and value not in VALID_BODY_TOS_NEGATE:
            return (
                False,
                f"Invalid tos-negate '{value}'. Must be one of: {', '.join(VALID_BODY_TOS_NEGATE)}",
            )

    # Validate traffic-shaper if present
    if "traffic-shaper" in payload:
        value = payload.get("traffic-shaper")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "traffic-shaper cannot exceed 35 characters")

    # Validate traffic-shaper-reverse if present
    if "traffic-shaper-reverse" in payload:
        value = payload.get("traffic-shaper-reverse")
        if value and isinstance(value, str) and len(value) > 35:
            return (
                False,
                "traffic-shaper-reverse cannot exceed 35 characters",
            )

    # Validate per-ip-shaper if present
    if "per-ip-shaper" in payload:
        value = payload.get("per-ip-shaper")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "per-ip-shaper cannot exceed 35 characters")

    # Validate class-id if present
    if "class-id" in payload:
        value = payload.get("class-id")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "class-id must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"class-id must be numeric, got: {value}")

    # Validate diffserv-forward if present
    if "diffserv-forward" in payload:
        value = payload.get("diffserv-forward")
        if value and value not in VALID_BODY_DIFFSERV_FORWARD:
            return (
                False,
                f"Invalid diffserv-forward '{value}'. Must be one of: {', '.join(VALID_BODY_DIFFSERV_FORWARD)}",
            )

    # Validate diffserv-reverse if present
    if "diffserv-reverse" in payload:
        value = payload.get("diffserv-reverse")
        if value and value not in VALID_BODY_DIFFSERV_REVERSE:
            return (
                False,
                f"Invalid diffserv-reverse '{value}'. Must be one of: {', '.join(VALID_BODY_DIFFSERV_REVERSE)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_shaping_policy_put(
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
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "name cannot exceed 35 characters")

    # Validate comment if present
    if "comment" in payload:
        value = payload.get("comment")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "comment cannot exceed 255 characters")

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )

    # Validate ip-version if present
    if "ip-version" in payload:
        value = payload.get("ip-version")
        if value and value not in VALID_BODY_IP_VERSION:
            return (
                False,
                f"Invalid ip-version '{value}'. Must be one of: {', '.join(VALID_BODY_IP_VERSION)}",
            )

    # Validate traffic-type if present
    if "traffic-type" in payload:
        value = payload.get("traffic-type")
        if value and value not in VALID_BODY_TRAFFIC_TYPE:
            return (
                False,
                f"Invalid traffic-type '{value}'. Must be one of: {', '.join(VALID_BODY_TRAFFIC_TYPE)}",
            )

    # Validate internet-service if present
    if "internet-service" in payload:
        value = payload.get("internet-service")
        if value and value not in VALID_BODY_INTERNET_SERVICE:
            return (
                False,
                f"Invalid internet-service '{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE)}",
            )

    # Validate internet-service-src if present
    if "internet-service-src" in payload:
        value = payload.get("internet-service-src")
        if value and value not in VALID_BODY_INTERNET_SERVICE_SRC:
            return (
                False,
                f"Invalid internet-service-src '{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE_SRC)}",
            )

    # Validate schedule if present
    if "schedule" in payload:
        value = payload.get("schedule")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "schedule cannot exceed 35 characters")

    # Validate tos-negate if present
    if "tos-negate" in payload:
        value = payload.get("tos-negate")
        if value and value not in VALID_BODY_TOS_NEGATE:
            return (
                False,
                f"Invalid tos-negate '{value}'. Must be one of: {', '.join(VALID_BODY_TOS_NEGATE)}",
            )

    # Validate traffic-shaper if present
    if "traffic-shaper" in payload:
        value = payload.get("traffic-shaper")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "traffic-shaper cannot exceed 35 characters")

    # Validate traffic-shaper-reverse if present
    if "traffic-shaper-reverse" in payload:
        value = payload.get("traffic-shaper-reverse")
        if value and isinstance(value, str) and len(value) > 35:
            return (
                False,
                "traffic-shaper-reverse cannot exceed 35 characters",
            )

    # Validate per-ip-shaper if present
    if "per-ip-shaper" in payload:
        value = payload.get("per-ip-shaper")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "per-ip-shaper cannot exceed 35 characters")

    # Validate class-id if present
    if "class-id" in payload:
        value = payload.get("class-id")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "class-id must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"class-id must be numeric, got: {value}")

    # Validate diffserv-forward if present
    if "diffserv-forward" in payload:
        value = payload.get("diffserv-forward")
        if value and value not in VALID_BODY_DIFFSERV_FORWARD:
            return (
                False,
                f"Invalid diffserv-forward '{value}'. Must be one of: {', '.join(VALID_BODY_DIFFSERV_FORWARD)}",
            )

    # Validate diffserv-reverse if present
    if "diffserv-reverse" in payload:
        value = payload.get("diffserv-reverse")
        if value and value not in VALID_BODY_DIFFSERV_REVERSE:
            return (
                False,
                f"Invalid diffserv-reverse '{value}'. Must be one of: {', '.join(VALID_BODY_DIFFSERV_REVERSE)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_shaping_policy_delete(
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
