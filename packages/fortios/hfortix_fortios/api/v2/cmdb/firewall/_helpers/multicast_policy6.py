"""
Validation helpers for firewall multicast_policy6 endpoint.

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
    "dstaddr",  # IPv6 destination address name.
    "dstintf",  # IPv6 destination interface name.
    "name",  # Policy name.
    "srcaddr",  # IPv6 source address name.
    "srcintf",  # IPv6 source interface name.
]

# Mutually exclusive groups (at least ONE from each group required)
MUTUALLY_EXCLUSIVE_GROUPS = {
    "dest_address": ["dstaddr"],
    "source_address": ["srcaddr"],
}

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "action": "accept",
    "auto-asic-offload": "enable",
    "end-port": 65535,
    "logtraffic": "utm",
    "start-port": 1,
    "status": "enable",
    "utm-status": "disable",
    "uuid": "00000000-0000-0000-0000-000000000000",
}


# Valid enum values from API documentation
VALID_BODY_STATUS = ["enable", "disable"]
VALID_BODY_ACTION = ["accept", "deny"]
VALID_BODY_UTM_STATUS = ["enable", "disable"]
VALID_BODY_LOGTRAFFIC = ["all", "utm", "disable"]
VALID_BODY_AUTO_ASIC_OFFLOAD = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_multicast_policy6_get(
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
    Validate required fields for firewall_multicast-policy6.

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
    if not ("dstaddr" in payload):
        return (False, "Must provide at least one of: dstaddr")
    if not ("srcaddr" in payload):
        return (False, "Must provide at least one of: srcaddr")

    return (True, None)


# ============================================================================
# Endpoint Validation (Enhanced with Required Fields)
# ============================================================================


def validate_multicast_policy6_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload.

    This validator performs two-stage validation:
    1. Required fields validation (schema-based)
    2. Field value validation (enums, ranges, formats)

    Required fields:
      - dstaddr: IPv6 destination address name.
      - dstintf: IPv6 destination interface name.
      - name: Policy name.
      - srcaddr: IPv6 source address name.
      - srcintf: IPv6 source interface name.

    Mutually exclusive (at least ONE required):
      - dstaddr
      - srcaddr

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
                if int_val < 0 or int_val > 4294967294:
                    return (False, "id must be between 0 and 4294967294")
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

    # Validate name if present
    if "name" in payload:
        value = payload.get("name")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "name cannot exceed 35 characters")

    # Validate srcintf if present
    if "srcint" in payload:
        value = payload.get("srcint")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "srcintf cannot exceed 35 characters")

    # Validate dstintf if present
    if "dstint" in payload:
        value = payload.get("dstint")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "dstintf cannot exceed 35 characters")

    # Validate action if present
    if "action" in payload:
        value = payload.get("action")
        if value and value not in VALID_BODY_ACTION:
            return (
                False,
                f"Invalid action '{value}'. Must be one of: {', '.join(VALID_BODY_ACTION)}",
            )

    # Validate protocol if present
    if "protocol" in payload:
        value = payload.get("protocol")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 255:
                    return (False, "protocol must be between 0 and 255")
            except (ValueError, TypeError):
                return (False, f"protocol must be numeric, got: {value}")

    # Validate start-port if present
    if "start-port" in payload:
        value = payload.get("start-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (False, "start-port must be between 0 and 65535")
            except (ValueError, TypeError):
                return (False, f"start-port must be numeric, got: {value}")

    # Validate end-port if present
    if "end-port" in payload:
        value = payload.get("end-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (False, "end-port must be between 0 and 65535")
            except (ValueError, TypeError):
                return (False, f"end-port must be numeric, got: {value}")

    # Validate utm-status if present
    if "utm-status" in payload:
        value = payload.get("utm-status")
        if value and value not in VALID_BODY_UTM_STATUS:
            return (
                False,
                f"Invalid utm-status '{value}'. Must be one of: {', '.join(VALID_BODY_UTM_STATUS)}",
            )

    # Validate ips-sensor if present
    if "ips-sensor" in payload:
        value = payload.get("ips-sensor")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "ips-sensor cannot exceed 47 characters")

    # Validate logtraffic if present
    if "logtraffic" in payload:
        value = payload.get("logtraffic")
        if value and value not in VALID_BODY_LOGTRAFFIC:
            return (
                False,
                f"Invalid logtraffic '{value}'. Must be one of: {', '.join(VALID_BODY_LOGTRAFFIC)}",
            )

    # Validate auto-asic-offload if present
    if "auto-asic-offload" in payload:
        value = payload.get("auto-asic-offload")
        if value and value not in VALID_BODY_AUTO_ASIC_OFFLOAD:
            return (
                False,
                f"Invalid auto-asic-offload '{value}'. Must be one of: {', '.join(VALID_BODY_AUTO_ASIC_OFFLOAD)}",
            )

    # Validate comments if present
    if "comments" in payload:
        value = payload.get("comments")
        if value and isinstance(value, str) and len(value) > 1023:
            return (False, "comments cannot exceed 1023 characters")

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_multicast_policy6_put(
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
                if int_val < 0 or int_val > 4294967294:
                    return (False, "id must be between 0 and 4294967294")
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

    # Validate name if present
    if "name" in payload:
        value = payload.get("name")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "name cannot exceed 35 characters")

    # Validate srcintf if present
    if "srcint" in payload:
        value = payload.get("srcint")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "srcintf cannot exceed 35 characters")

    # Validate dstintf if present
    if "dstint" in payload:
        value = payload.get("dstint")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "dstintf cannot exceed 35 characters")

    # Validate action if present
    if "action" in payload:
        value = payload.get("action")
        if value and value not in VALID_BODY_ACTION:
            return (
                False,
                f"Invalid action '{value}'. Must be one of: {', '.join(VALID_BODY_ACTION)}",
            )

    # Validate protocol if present
    if "protocol" in payload:
        value = payload.get("protocol")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 255:
                    return (False, "protocol must be between 0 and 255")
            except (ValueError, TypeError):
                return (False, f"protocol must be numeric, got: {value}")

    # Validate start-port if present
    if "start-port" in payload:
        value = payload.get("start-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (False, "start-port must be between 0 and 65535")
            except (ValueError, TypeError):
                return (False, f"start-port must be numeric, got: {value}")

    # Validate end-port if present
    if "end-port" in payload:
        value = payload.get("end-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (False, "end-port must be between 0 and 65535")
            except (ValueError, TypeError):
                return (False, f"end-port must be numeric, got: {value}")

    # Validate utm-status if present
    if "utm-status" in payload:
        value = payload.get("utm-status")
        if value and value not in VALID_BODY_UTM_STATUS:
            return (
                False,
                f"Invalid utm-status '{value}'. Must be one of: {', '.join(VALID_BODY_UTM_STATUS)}",
            )

    # Validate ips-sensor if present
    if "ips-sensor" in payload:
        value = payload.get("ips-sensor")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "ips-sensor cannot exceed 47 characters")

    # Validate logtraffic if present
    if "logtraffic" in payload:
        value = payload.get("logtraffic")
        if value and value not in VALID_BODY_LOGTRAFFIC:
            return (
                False,
                f"Invalid logtraffic '{value}'. Must be one of: {', '.join(VALID_BODY_LOGTRAFFIC)}",
            )

    # Validate auto-asic-offload if present
    if "auto-asic-offload" in payload:
        value = payload.get("auto-asic-offload")
        if value and value not in VALID_BODY_AUTO_ASIC_OFFLOAD:
            return (
                False,
                f"Invalid auto-asic-offload '{value}'. Must be one of: {', '.join(VALID_BODY_AUTO_ASIC_OFFLOAD)}",
            )

    # Validate comments if present
    if "comments" in payload:
        value = payload.get("comments")
        if value and isinstance(value, str) and len(value) > 1023:
            return (False, "comments cannot exceed 1023 characters")

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_multicast_policy6_delete(
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
