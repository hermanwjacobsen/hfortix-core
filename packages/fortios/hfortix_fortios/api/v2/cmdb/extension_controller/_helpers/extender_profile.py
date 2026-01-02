"""
Validation helpers for extension-controller extender_profile endpoint.

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
    "bandwidth-limit",  # FortiExtender LAN extension bandwidth limit (Mbps).
    "cellular",  # FortiExtender cellular configuration.
    "extension",  # Extension option.
    "lan-extension",  # FortiExtender LAN extension configuration.
    "login-password",  # Set the managed extender's administrator password.
    "model",  # Model.
    "name",  # FortiExtender profile name.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "allowaccess": "ping",
    "bandwidth-limit": 1024,
    "enforce-bandwidth": "disable",
    "extension": "wan-extension",
    "id": 32,
    "login-password-change": "no",
    "model": "FX201E",
}


# Valid enum values from API documentation
VALID_BODY_MODEL = [
    "FX201E",
    "FX211E",
    "FX200F",
    "FXA11F",
    "FXE11F",
    "FXA21F",
    "FXE21F",
    "FXA22F",
    "FXE22F",
    "FX212F",
    "FX311F",
    "FX312F",
    "FX511F",
    "FXR51G",
    "FXN51G",
    "FXW51G",
    "FVG21F",
    "FVA21F",
    "FVG22F",
    "FVA22F",
    "FX04DA",
    "FG",
    "BS10FW",
    "BS20GW",
    "BS20GN",
    "FVG51G",
    "FXE11G",
    "FX211G",
]
VALID_BODY_EXTENSION = ["wan-extension", "lan-extension"]
VALID_BODY_ALLOWACCESS = ["ping", "telnet", "http", "https", "ssh", "snmp"]
VALID_BODY_LOGIN_PASSWORD_CHANGE = ["yes", "default", "no"]
VALID_BODY_ENFORCE_BANDWIDTH = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_extender_profile_get(
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
    Validate required fields for extension-controller_extender-profile.

    This validator checks:
    1. Always-required fields are present
    2. Mutually exclusive groups have at least one field

    Args:
        payload: The request payload to validate

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> is_valid, error = validate_required_fields({
        ...     "bandwidth-limit": "value",
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


def validate_extender_profile_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload.

    This validator performs two-stage validation:
    1. Required fields validation (schema-based)
    2. Field value validation (enums, ranges, formats)

    Required fields:
      - bandwidth-limit: FortiExtender LAN extension bandwidth limit (Mbps).
      - cellular: FortiExtender cellular configuration.
      - extension: Extension option.
      - lan-extension: FortiExtender LAN extension configuration.
      - login-password: Set the managed extender's administrator password.
      - model: Model.
      - name: FortiExtender profile name.

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
        if value and isinstance(value, str) and len(value) > 31:
            return (False, "name cannot exceed 31 characters")

    # Validate id if present
    if "id" in payload:
        value = payload.get("id")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 102400000:
                    return (False, "id must be between 0 and 102400000")
            except (ValueError, TypeError):
                return (False, f"id must be numeric, got: {value}")

    # Validate model if present
    if "model" in payload:
        value = payload.get("model")
        if value and value not in VALID_BODY_MODEL:
            return (
                False,
                f"Invalid model '{value}'. Must be one of: {', '.join(VALID_BODY_MODEL)}",
            )

    # Validate extension if present
    if "extension" in payload:
        value = payload.get("extension")
        if value and value not in VALID_BODY_EXTENSION:
            return (
                False,
                f"Invalid extension '{value}'. Must be one of: {', '.join(VALID_BODY_EXTENSION)}",
            )

    # Validate allowaccess if present
    if "allowaccess" in payload:
        value = payload.get("allowaccess")
        if value and value not in VALID_BODY_ALLOWACCESS:
            return (
                False,
                f"Invalid allowaccess '{value}'. Must be one of: {', '.join(VALID_BODY_ALLOWACCESS)}",
            )

    # Validate login-password-change if present
    if "login-password-change" in payload:
        value = payload.get("login-password-change")
        if value and value not in VALID_BODY_LOGIN_PASSWORD_CHANGE:
            return (
                False,
                f"Invalid login-password-change '{value}'. Must be one of: {', '.join(VALID_BODY_LOGIN_PASSWORD_CHANGE)}",
            )

    # Validate enforce-bandwidth if present
    if "enforce-bandwidth" in payload:
        value = payload.get("enforce-bandwidth")
        if value and value not in VALID_BODY_ENFORCE_BANDWIDTH:
            return (
                False,
                f"Invalid enforce-bandwidth '{value}'. Must be one of: {', '.join(VALID_BODY_ENFORCE_BANDWIDTH)}",
            )

    # Validate bandwidth-limit if present
    if "bandwidth-limit" in payload:
        value = payload.get("bandwidth-limit")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 16776000:
                    return (
                        False,
                        "bandwidth-limit must be between 1 and 16776000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"bandwidth-limit must be numeric, got: {value}",
                )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_extender_profile_put(
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
        if value and isinstance(value, str) and len(value) > 31:
            return (False, "name cannot exceed 31 characters")

    # Validate id if present
    if "id" in payload:
        value = payload.get("id")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 102400000:
                    return (False, "id must be between 0 and 102400000")
            except (ValueError, TypeError):
                return (False, f"id must be numeric, got: {value}")

    # Validate model if present
    if "model" in payload:
        value = payload.get("model")
        if value and value not in VALID_BODY_MODEL:
            return (
                False,
                f"Invalid model '{value}'. Must be one of: {', '.join(VALID_BODY_MODEL)}",
            )

    # Validate extension if present
    if "extension" in payload:
        value = payload.get("extension")
        if value and value not in VALID_BODY_EXTENSION:
            return (
                False,
                f"Invalid extension '{value}'. Must be one of: {', '.join(VALID_BODY_EXTENSION)}",
            )

    # Validate allowaccess if present
    if "allowaccess" in payload:
        value = payload.get("allowaccess")
        if value and value not in VALID_BODY_ALLOWACCESS:
            return (
                False,
                f"Invalid allowaccess '{value}'. Must be one of: {', '.join(VALID_BODY_ALLOWACCESS)}",
            )

    # Validate login-password-change if present
    if "login-password-change" in payload:
        value = payload.get("login-password-change")
        if value and value not in VALID_BODY_LOGIN_PASSWORD_CHANGE:
            return (
                False,
                f"Invalid login-password-change '{value}'. Must be one of: {', '.join(VALID_BODY_LOGIN_PASSWORD_CHANGE)}",
            )

    # Validate enforce-bandwidth if present
    if "enforce-bandwidth" in payload:
        value = payload.get("enforce-bandwidth")
        if value and value not in VALID_BODY_ENFORCE_BANDWIDTH:
            return (
                False,
                f"Invalid enforce-bandwidth '{value}'. Must be one of: {', '.join(VALID_BODY_ENFORCE_BANDWIDTH)}",
            )

    # Validate bandwidth-limit if present
    if "bandwidth-limit" in payload:
        value = payload.get("bandwidth-limit")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 16776000:
                    return (
                        False,
                        "bandwidth-limit must be between 1 and 16776000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"bandwidth-limit must be numeric, got: {value}",
                )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_extender_profile_delete(
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
