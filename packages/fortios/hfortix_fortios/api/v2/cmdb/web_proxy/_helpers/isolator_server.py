"""
Validation helpers for web-proxy isolator_server endpoint.

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
    "interface",  # Specify outgoing interface to reach server.
    "name",  # Server name.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "addr-type": "ip",
    "interface-select-method": "sdwan",
    "ip": "0.0.0.0",
    "ipv6": "::",
    "masquerade": "enable",
    "port": 3128,
    "vrf-select": -1,
}


# Valid enum values from API documentation
VALID_BODY_ADDR_TYPE = ["ip", "ipv6", "fqdn"]
VALID_BODY_INTERFACE_SELECT_METHOD = ["sdwan", "specify"]
VALID_BODY_MASQUERADE = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_isolator_server_get(
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
    Validate required fields for web-proxy_isolator-server.

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


def validate_isolator_server_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload.

    This validator performs two-stage validation:
    1. Required fields validation (schema-based)
    2. Field value validation (enums, ranges, formats)

    Required fields:
      - interface: Specify outgoing interface to reach server.
      - name: Server name.

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

    # Validate addr-type if present
    if "addr-type" in payload:
        value = payload.get("addr-type")
        if value and value not in VALID_BODY_ADDR_TYPE:
            return (
                False,
                f"Invalid addr-type '{value}'. Must be one of: {', '.join(VALID_BODY_ADDR_TYPE)}",
            )

    # Validate fqdn if present
    if "fqdn" in payload:
        value = payload.get("fqdn")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "fqdn cannot exceed 255 characters")

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

    # Validate interface-select-method if present
    if "interface-select-method" in payload:
        value = payload.get("interface-select-method")
        if value and value not in VALID_BODY_INTERFACE_SELECT_METHOD:
            return (
                False,
                f"Invalid interface-select-method '{value}'. Must be one of: {', '.join(VALID_BODY_INTERFACE_SELECT_METHOD)}",
            )

    # Validate interface if present
    if "interface" in payload:
        value = payload.get("interface")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "interface cannot exceed 15 characters")

    # Validate vrf-select if present
    if "vrf-select" in payload:
        value = payload.get("vrf-select")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 511:
                    return (False, "vrf-select must be between 0 and 511")
            except (ValueError, TypeError):
                return (False, f"vrf-select must be numeric, got: {value}")

    # Validate comment if present
    if "comment" in payload:
        value = payload.get("comment")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "comment cannot exceed 63 characters")

    # Validate masquerade if present
    if "masquerade" in payload:
        value = payload.get("masquerade")
        if value and value not in VALID_BODY_MASQUERADE:
            return (
                False,
                f"Invalid masquerade '{value}'. Must be one of: {', '.join(VALID_BODY_MASQUERADE)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_isolator_server_put(
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

    # Validate addr-type if present
    if "addr-type" in payload:
        value = payload.get("addr-type")
        if value and value not in VALID_BODY_ADDR_TYPE:
            return (
                False,
                f"Invalid addr-type '{value}'. Must be one of: {', '.join(VALID_BODY_ADDR_TYPE)}",
            )

    # Validate fqdn if present
    if "fqdn" in payload:
        value = payload.get("fqdn")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "fqdn cannot exceed 255 characters")

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

    # Validate interface-select-method if present
    if "interface-select-method" in payload:
        value = payload.get("interface-select-method")
        if value and value not in VALID_BODY_INTERFACE_SELECT_METHOD:
            return (
                False,
                f"Invalid interface-select-method '{value}'. Must be one of: {', '.join(VALID_BODY_INTERFACE_SELECT_METHOD)}",
            )

    # Validate interface if present
    if "interface" in payload:
        value = payload.get("interface")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "interface cannot exceed 15 characters")

    # Validate vrf-select if present
    if "vrf-select" in payload:
        value = payload.get("vrf-select")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 511:
                    return (False, "vrf-select must be between 0 and 511")
            except (ValueError, TypeError):
                return (False, f"vrf-select must be numeric, got: {value}")

    # Validate comment if present
    if "comment" in payload:
        value = payload.get("comment")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "comment cannot exceed 63 characters")

    # Validate masquerade if present
    if "masquerade" in payload:
        value = payload.get("masquerade")
        if value and value not in VALID_BODY_MASQUERADE:
            return (
                False,
                f"Invalid masquerade '{value}'. Must be one of: {', '.join(VALID_BODY_MASQUERADE)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_isolator_server_delete(
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
