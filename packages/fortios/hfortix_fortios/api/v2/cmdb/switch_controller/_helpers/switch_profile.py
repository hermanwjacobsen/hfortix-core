"""
Validation helpers for switch-controller switch_profile endpoint.

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
    "name",  # FortiSwitch Profile name.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "login": "enable",
    "login-passwd-override": "disable",
    "revision-backup-on-logout": "disable",
    "revision-backup-on-upgrade": "disable",
}


# Valid enum values from API documentation
VALID_BODY_LOGIN_PASSWD_OVERRIDE = ["enable", "disable"]
VALID_BODY_LOGIN = ["enable", "disable"]
VALID_BODY_REVISION_BACKUP_ON_LOGOUT = ["enable", "disable"]
VALID_BODY_REVISION_BACKUP_ON_UPGRADE = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_switch_profile_get(
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
    Validate required fields for switch-controller_switch-profile.

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


def validate_switch_profile_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload.

    This validator performs two-stage validation:
    1. Required fields validation (schema-based)
    2. Field value validation (enums, ranges, formats)

    Required fields:
      - name: FortiSwitch Profile name.

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
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "name cannot exceed 35 characters")

    # Validate login-passwd-override if present
    if "login-passwd-override" in payload:
        value = payload.get("login-passwd-override")
        if value and value not in VALID_BODY_LOGIN_PASSWD_OVERRIDE:
            return (
                False,
                f"Invalid login-passwd-override '{value}'. Must be one of: {', '.join(VALID_BODY_LOGIN_PASSWD_OVERRIDE)}",
            )

    # Validate login if present
    if "login" in payload:
        value = payload.get("login")
        if value and value not in VALID_BODY_LOGIN:
            return (
                False,
                f"Invalid login '{value}'. Must be one of: {', '.join(VALID_BODY_LOGIN)}",
            )

    # Validate revision-backup-on-logout if present
    if "revision-backup-on-logout" in payload:
        value = payload.get("revision-backup-on-logout")
        if value and value not in VALID_BODY_REVISION_BACKUP_ON_LOGOUT:
            return (
                False,
                f"Invalid revision-backup-on-logout '{value}'. Must be one of: {', '.join(VALID_BODY_REVISION_BACKUP_ON_LOGOUT)}",
            )

    # Validate revision-backup-on-upgrade if present
    if "revision-backup-on-upgrade" in payload:
        value = payload.get("revision-backup-on-upgrade")
        if value and value not in VALID_BODY_REVISION_BACKUP_ON_UPGRADE:
            return (
                False,
                f"Invalid revision-backup-on-upgrade '{value}'. Must be one of: {', '.join(VALID_BODY_REVISION_BACKUP_ON_UPGRADE)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_switch_profile_put(
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
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "name cannot exceed 35 characters")

    # Validate login-passwd-override if present
    if "login-passwd-override" in payload:
        value = payload.get("login-passwd-override")
        if value and value not in VALID_BODY_LOGIN_PASSWD_OVERRIDE:
            return (
                False,
                f"Invalid login-passwd-override '{value}'. Must be one of: {', '.join(VALID_BODY_LOGIN_PASSWD_OVERRIDE)}",
            )

    # Validate login if present
    if "login" in payload:
        value = payload.get("login")
        if value and value not in VALID_BODY_LOGIN:
            return (
                False,
                f"Invalid login '{value}'. Must be one of: {', '.join(VALID_BODY_LOGIN)}",
            )

    # Validate revision-backup-on-logout if present
    if "revision-backup-on-logout" in payload:
        value = payload.get("revision-backup-on-logout")
        if value and value not in VALID_BODY_REVISION_BACKUP_ON_LOGOUT:
            return (
                False,
                f"Invalid revision-backup-on-logout '{value}'. Must be one of: {', '.join(VALID_BODY_REVISION_BACKUP_ON_LOGOUT)}",
            )

    # Validate revision-backup-on-upgrade if present
    if "revision-backup-on-upgrade" in payload:
        value = payload.get("revision-backup-on-upgrade")
        if value and value not in VALID_BODY_REVISION_BACKUP_ON_UPGRADE:
            return (
                False,
                f"Invalid revision-backup-on-upgrade '{value}'. Must be one of: {', '.join(VALID_BODY_REVISION_BACKUP_ON_UPGRADE)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_switch_profile_delete(
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
