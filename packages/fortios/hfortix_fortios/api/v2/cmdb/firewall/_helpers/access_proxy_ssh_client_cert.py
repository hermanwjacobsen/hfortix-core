"""
Validation helpers for firewall access_proxy_ssh_client_cert endpoint.

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
    "auth-ca",  # Name of the SSH server public key authentication CA.
    "name",  # SSH client certificate name.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "permit-agent-forwarding": "enable",
    "permit-port-forwarding": "enable",
    "permit-pty": "enable",
    "permit-user-rc": "enable",
    "permit-x11-forwarding": "enable",
    "source-address": "disable",
}


# Valid enum values from API documentation
VALID_BODY_SOURCE_ADDRESS = ["enable", "disable"]
VALID_BODY_PERMIT_X11_FORWARDING = ["enable", "disable"]
VALID_BODY_PERMIT_AGENT_FORWARDING = ["enable", "disable"]
VALID_BODY_PERMIT_PORT_FORWARDING = ["enable", "disable"]
VALID_BODY_PERMIT_PTY = ["enable", "disable"]
VALID_BODY_PERMIT_USER_RC = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_access_proxy_ssh_client_cert_get(
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
    Validate required fields for firewall_access-proxy-ssh-client-cert.

    This validator checks:
    1. Always-required fields are present
    2. Mutually exclusive groups have at least one field

    Args:
        payload: The request payload to validate

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> is_valid, error = validate_required_fields({
        ...     "auth-ca": "value",
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


def validate_access_proxy_ssh_client_cert_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload.

    This validator performs two-stage validation:
    1. Required fields validation (schema-based)
    2. Field value validation (enums, ranges, formats)

    Required fields:
      - auth-ca: Name of the SSH server public key authentication CA.
      - name: SSH client certificate name.

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
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "name cannot exceed 79 characters")

    # Validate source-address if present
    if "source-address" in payload:
        value = payload.get("source-address")
        if value and value not in VALID_BODY_SOURCE_ADDRESS:
            return (
                False,
                f"Invalid source-address '{value}'. Must be one of: {', '.join(VALID_BODY_SOURCE_ADDRESS)}",
            )

    # Validate permit-x11-forwarding if present
    if "permit-x11-forwarding" in payload:
        value = payload.get("permit-x11-forwarding")
        if value and value not in VALID_BODY_PERMIT_X11_FORWARDING:
            return (
                False,
                f"Invalid permit-x11-forwarding '{value}'. Must be one of: {', '.join(VALID_BODY_PERMIT_X11_FORWARDING)}",
            )

    # Validate permit-agent-forwarding if present
    if "permit-agent-forwarding" in payload:
        value = payload.get("permit-agent-forwarding")
        if value and value not in VALID_BODY_PERMIT_AGENT_FORWARDING:
            return (
                False,
                f"Invalid permit-agent-forwarding '{value}'. Must be one of: {', '.join(VALID_BODY_PERMIT_AGENT_FORWARDING)}",
            )

    # Validate permit-port-forwarding if present
    if "permit-port-forwarding" in payload:
        value = payload.get("permit-port-forwarding")
        if value and value not in VALID_BODY_PERMIT_PORT_FORWARDING:
            return (
                False,
                f"Invalid permit-port-forwarding '{value}'. Must be one of: {', '.join(VALID_BODY_PERMIT_PORT_FORWARDING)}",
            )

    # Validate permit-pty if present
    if "permit-pty" in payload:
        value = payload.get("permit-pty")
        if value and value not in VALID_BODY_PERMIT_PTY:
            return (
                False,
                f"Invalid permit-pty '{value}'. Must be one of: {', '.join(VALID_BODY_PERMIT_PTY)}",
            )

    # Validate permit-user-rc if present
    if "permit-user-rc" in payload:
        value = payload.get("permit-user-rc")
        if value and value not in VALID_BODY_PERMIT_USER_RC:
            return (
                False,
                f"Invalid permit-user-rc '{value}'. Must be one of: {', '.join(VALID_BODY_PERMIT_USER_RC)}",
            )

    # Validate auth-ca if present
    if "auth-ca" in payload:
        value = payload.get("auth-ca")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "auth-ca cannot exceed 79 characters")

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_access_proxy_ssh_client_cert_put(
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
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "name cannot exceed 79 characters")

    # Validate source-address if present
    if "source-address" in payload:
        value = payload.get("source-address")
        if value and value not in VALID_BODY_SOURCE_ADDRESS:
            return (
                False,
                f"Invalid source-address '{value}'. Must be one of: {', '.join(VALID_BODY_SOURCE_ADDRESS)}",
            )

    # Validate permit-x11-forwarding if present
    if "permit-x11-forwarding" in payload:
        value = payload.get("permit-x11-forwarding")
        if value and value not in VALID_BODY_PERMIT_X11_FORWARDING:
            return (
                False,
                f"Invalid permit-x11-forwarding '{value}'. Must be one of: {', '.join(VALID_BODY_PERMIT_X11_FORWARDING)}",
            )

    # Validate permit-agent-forwarding if present
    if "permit-agent-forwarding" in payload:
        value = payload.get("permit-agent-forwarding")
        if value and value not in VALID_BODY_PERMIT_AGENT_FORWARDING:
            return (
                False,
                f"Invalid permit-agent-forwarding '{value}'. Must be one of: {', '.join(VALID_BODY_PERMIT_AGENT_FORWARDING)}",
            )

    # Validate permit-port-forwarding if present
    if "permit-port-forwarding" in payload:
        value = payload.get("permit-port-forwarding")
        if value and value not in VALID_BODY_PERMIT_PORT_FORWARDING:
            return (
                False,
                f"Invalid permit-port-forwarding '{value}'. Must be one of: {', '.join(VALID_BODY_PERMIT_PORT_FORWARDING)}",
            )

    # Validate permit-pty if present
    if "permit-pty" in payload:
        value = payload.get("permit-pty")
        if value and value not in VALID_BODY_PERMIT_PTY:
            return (
                False,
                f"Invalid permit-pty '{value}'. Must be one of: {', '.join(VALID_BODY_PERMIT_PTY)}",
            )

    # Validate permit-user-rc if present
    if "permit-user-rc" in payload:
        value = payload.get("permit-user-rc")
        if value and value not in VALID_BODY_PERMIT_USER_RC:
            return (
                False,
                f"Invalid permit-user-rc '{value}'. Must be one of: {', '.join(VALID_BODY_PERMIT_USER_RC)}",
            )

    # Validate auth-ca if present
    if "auth-ca" in payload:
        value = payload.get("auth-ca")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "auth-ca cannot exceed 79 characters")

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_access_proxy_ssh_client_cert_delete(
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
