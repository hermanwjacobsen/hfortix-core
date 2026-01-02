"""
Validation helpers for system vxlan endpoint.

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
    "interface",  # Outgoing interface for VXLAN encapsulated traffic.
    "ip-version",  # IP version to use for the VXLAN interface and so for communi
    "multicast-ttl",  # VXLAN multicast TTL (1-255, default = 0).
    "name",  # VXLAN device or interface name. Must be a unique interface n
    "remote-ip6",  # IPv6 IP address of the VXLAN interface on the device at the
    "vni",  # VXLAN network ID.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "dstport": 4789,
    "ip-version": "ipv4-unicast",
    "learn-from-traffic": "disable",
    "local-ip": "0.0.0.0",
    "local-ip6": "::",
}


# Valid enum values from API documentation
VALID_BODY_IP_VERSION = [
    "ipv4-unicast",
    "ipv6-unicast",
    "ipv4-multicast",
    "ipv6-multicast",
]
VALID_BODY_LEARN_FROM_TRAFFIC = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_vxlan_get(
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
    Validate required fields for system_vxlan.

    This validator checks:
    1. Always-required fields are present
    2. Mutually exclusive groups have at least one field

    Args:
        payload: The request payload to validate

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> is_valid, error = validate_required_fields({
        ...     "interface": "value",
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


def validate_vxlan_post(payload: dict[str, Any]) -> tuple[bool, str | None]:
    """
    Validate POST request payload.

    This validator performs two-stage validation:
    1. Required fields validation (schema-based)
    2. Field value validation (enums, ranges, formats)

    Required fields:
      - interface: Outgoing interface for VXLAN encapsulated traffic.
      - ip-version: IP version to use for the VXLAN interface and so for communi
      - multicast-ttl: VXLAN multicast TTL (1-255, default = 0).
      - name: VXLAN device or interface name. Must be a unique interface n
      - remote-ip6: IPv6 IP address of the VXLAN interface on the device at the
      - vni: VXLAN network ID.

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
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "name cannot exceed 15 characters")

    # Validate interface if present
    if "interface" in payload:
        value = payload.get("interface")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "interface cannot exceed 15 characters")

    # Validate vni if present
    if "vni" in payload:
        value = payload.get("vni")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 16777215:
                    return (False, "vni must be between 1 and 16777215")
            except (ValueError, TypeError):
                return (False, f"vni must be numeric, got: {value}")

    # Validate ip-version if present
    if "ip-version" in payload:
        value = payload.get("ip-version")
        if value and value not in VALID_BODY_IP_VERSION:
            return (
                False,
                f"Invalid ip-version '{value}'. Must be one of: {', '.join(VALID_BODY_IP_VERSION)}",
            )

    # Validate dstport if present
    if "dstport" in payload:
        value = payload.get("dstport")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (False, "dstport must be between 1 and 65535")
            except (ValueError, TypeError):
                return (False, f"dstport must be numeric, got: {value}")

    # Validate multicast-ttl if present
    if "multicast-ttl" in payload:
        value = payload.get("multicast-ttl")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 255:
                    return (False, "multicast-ttl must be between 1 and 255")
            except (ValueError, TypeError):
                return (False, f"multicast-ttl must be numeric, got: {value}")

    # Validate evpn-id if present
    if "evpn-id" in payload:
        value = payload.get("evpn-id")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (False, "evpn-id must be between 1 and 65535")
            except (ValueError, TypeError):
                return (False, f"evpn-id must be numeric, got: {value}")

    # Validate learn-from-traffic if present
    if "learn-from-traffic" in payload:
        value = payload.get("learn-from-traffic")
        if value and value not in VALID_BODY_LEARN_FROM_TRAFFIC:
            return (
                False,
                f"Invalid learn-from-traffic '{value}'. Must be one of: {', '.join(VALID_BODY_LEARN_FROM_TRAFFIC)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_vxlan_put(
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
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "name cannot exceed 15 characters")

    # Validate interface if present
    if "interface" in payload:
        value = payload.get("interface")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "interface cannot exceed 15 characters")

    # Validate vni if present
    if "vni" in payload:
        value = payload.get("vni")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 16777215:
                    return (False, "vni must be between 1 and 16777215")
            except (ValueError, TypeError):
                return (False, f"vni must be numeric, got: {value}")

    # Validate ip-version if present
    if "ip-version" in payload:
        value = payload.get("ip-version")
        if value and value not in VALID_BODY_IP_VERSION:
            return (
                False,
                f"Invalid ip-version '{value}'. Must be one of: {', '.join(VALID_BODY_IP_VERSION)}",
            )

    # Validate dstport if present
    if "dstport" in payload:
        value = payload.get("dstport")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (False, "dstport must be between 1 and 65535")
            except (ValueError, TypeError):
                return (False, f"dstport must be numeric, got: {value}")

    # Validate multicast-ttl if present
    if "multicast-ttl" in payload:
        value = payload.get("multicast-ttl")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 255:
                    return (False, "multicast-ttl must be between 1 and 255")
            except (ValueError, TypeError):
                return (False, f"multicast-ttl must be numeric, got: {value}")

    # Validate evpn-id if present
    if "evpn-id" in payload:
        value = payload.get("evpn-id")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (False, "evpn-id must be between 1 and 65535")
            except (ValueError, TypeError):
                return (False, f"evpn-id must be numeric, got: {value}")

    # Validate learn-from-traffic if present
    if "learn-from-traffic" in payload:
        value = payload.get("learn-from-traffic")
        if value and value not in VALID_BODY_LEARN_FROM_TRAFFIC:
            return (
                False,
                f"Invalid learn-from-traffic '{value}'. Must be one of: {', '.join(VALID_BODY_LEARN_FROM_TRAFFIC)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_vxlan_delete(name: str | None = None) -> tuple[bool, str | None]:
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
