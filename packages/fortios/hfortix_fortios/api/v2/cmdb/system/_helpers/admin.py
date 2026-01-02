"""
Validation helpers for system admin endpoint.

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
    "name",  # User name.
    "password",  # Admin user password.
    "peer-group",  # Name of peer group defined under config user group which has
    "remote-group",  # User group name used for remote auth.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "accprofile-override": "disable",
    "allow-remove-admin-session": "enable",
    "force-password-change": "disable",
    "guest-auth": "disable",
    "ip6-trusthost1": "::/0",
    "ip6-trusthost10": "::/0",
    "ip6-trusthost2": "::/0",
    "ip6-trusthost3": "::/0",
    "ip6-trusthost4": "::/0",
    "ip6-trusthost5": "::/0",
    "ip6-trusthost6": "::/0",
    "ip6-trusthost7": "::/0",
    "ip6-trusthost8": "::/0",
    "ip6-trusthost9": "::/0",
    "password-expire": "0000-00-00 00:00:00",
    "peer-auth": "disable",
    "remote-auth": "disable",
    "schedule": "always",
    "sms-server": "fortiguard",
    "status": "enable",
    "trusthost1": "0.0.0.0 0.0.0.0",
    "trusthost10": "0.0.0.0 0.0.0.0",
    "trusthost2": "0.0.0.0 0.0.0.0",
    "trusthost3": "0.0.0.0 0.0.0.0",
    "trusthost4": "0.0.0.0 0.0.0.0",
    "trusthost5": "0.0.0.0 0.0.0.0",
    "trusthost6": "0.0.0.0 0.0.0.0",
    "trusthost7": "0.0.0.0 0.0.0.0",
    "trusthost8": "0.0.0.0 0.0.0.0",
    "trusthost9": "0.0.0.0 0.0.0.0",
    "two-factor": "disable",
    "two-factor-authentication": "fortitoken",
    "two-factor-notification": "email",
    "vdom-override": "disable",
    "wildcard": "disable",
}


# Valid enum values from API documentation
VALID_BODY_REMOTE_AUTH = ["enable", "disable"]
VALID_BODY_WILDCARD = ["enable", "disable"]
VALID_BODY_PEER_AUTH = ["enable", "disable"]
VALID_BODY_ALLOW_REMOVE_ADMIN_SESSION = ["enable", "disable"]
VALID_BODY_ACCPROFILE_OVERRIDE = ["enable", "disable"]
VALID_BODY_VDOM_OVERRIDE = ["enable", "disable"]
VALID_BODY_FORCE_PASSWORD_CHANGE = ["enable", "disable"]
VALID_BODY_TWO_FACTOR = [
    "disable",
    "fortitoken",
    "fortitoken-cloud",
    "email",
    "sms",
]
VALID_BODY_TWO_FACTOR_AUTHENTICATION = ["fortitoken", "email", "sms"]
VALID_BODY_TWO_FACTOR_NOTIFICATION = ["email", "sms"]
VALID_BODY_SMS_SERVER = ["fortiguard", "custom"]
VALID_BODY_GUEST_AUTH = ["disable", "enable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_admin_get(
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
    Validate required fields for system_admin.

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


def validate_admin_post(payload: dict[str, Any]) -> tuple[bool, str | None]:
    """
    Validate POST request payload.

    This validator performs two-stage validation:
    1. Required fields validation (schema-based)
    2. Field value validation (enums, ranges, formats)

    Required fields:
      - name: User name.
      - password: Admin user password.
      - peer-group: Name of peer group defined under config user group which has
      - remote-group: User group name used for remote auth.

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
        if value and isinstance(value, str) and len(value) > 64:
            return (False, "name cannot exceed 64 characters")

    # Validate remote-auth if present
    if "remote-auth" in payload:
        value = payload.get("remote-auth")
        if value and value not in VALID_BODY_REMOTE_AUTH:
            return (
                False,
                f"Invalid remote-auth '{value}'. Must be one of: {', '.join(VALID_BODY_REMOTE_AUTH)}",
            )

    # Validate remote-group if present
    if "remote-group" in payload:
        value = payload.get("remote-group")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "remote-group cannot exceed 35 characters")

    # Validate wildcard if present
    if "wildcard" in payload:
        value = payload.get("wildcard")
        if value and value not in VALID_BODY_WILDCARD:
            return (
                False,
                f"Invalid wildcard '{value}'. Must be one of: {', '.join(VALID_BODY_WILDCARD)}",
            )

    # Validate peer-auth if present
    if "peer-auth" in payload:
        value = payload.get("peer-auth")
        if value and value not in VALID_BODY_PEER_AUTH:
            return (
                False,
                f"Invalid peer-auth '{value}'. Must be one of: {', '.join(VALID_BODY_PEER_AUTH)}",
            )

    # Validate peer-group if present
    if "peer-group" in payload:
        value = payload.get("peer-group")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "peer-group cannot exceed 35 characters")

    # Validate accprofile if present
    if "accprofile" in payload:
        value = payload.get("accprofile")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "accprofile cannot exceed 35 characters")

    # Validate allow-remove-admin-session if present
    if "allow-remove-admin-session" in payload:
        value = payload.get("allow-remove-admin-session")
        if value and value not in VALID_BODY_ALLOW_REMOVE_ADMIN_SESSION:
            return (
                False,
                f"Invalid allow-remove-admin-session '{value}'. Must be one of: {', '.join(VALID_BODY_ALLOW_REMOVE_ADMIN_SESSION)}",
            )

    # Validate comments if present
    if "comments" in payload:
        value = payload.get("comments")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "comments cannot exceed 255 characters")

    # Validate ssh-certificate if present
    if "ssh-certificate" in payload:
        value = payload.get("ssh-certificate")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "ssh-certificate cannot exceed 35 characters")

    # Validate schedule if present
    if "schedule" in payload:
        value = payload.get("schedule")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "schedule cannot exceed 35 characters")

    # Validate accprofile-override if present
    if "accprofile-override" in payload:
        value = payload.get("accprofile-override")
        if value and value not in VALID_BODY_ACCPROFILE_OVERRIDE:
            return (
                False,
                f"Invalid accprofile-override '{value}'. Must be one of: {', '.join(VALID_BODY_ACCPROFILE_OVERRIDE)}",
            )

    # Validate vdom-override if present
    if "vdom-override" in payload:
        value = payload.get("vdom-override")
        if value and value not in VALID_BODY_VDOM_OVERRIDE:
            return (
                False,
                f"Invalid vdom-override '{value}'. Must be one of: {', '.join(VALID_BODY_VDOM_OVERRIDE)}",
            )

    # Validate force-password-change if present
    if "force-password-change" in payload:
        value = payload.get("force-password-change")
        if value and value not in VALID_BODY_FORCE_PASSWORD_CHANGE:
            return (
                False,
                f"Invalid force-password-change '{value}'. Must be one of: {', '.join(VALID_BODY_FORCE_PASSWORD_CHANGE)}",
            )

    # Validate two-factor if present
    if "two-factor" in payload:
        value = payload.get("two-factor")
        if value and value not in VALID_BODY_TWO_FACTOR:
            return (
                False,
                f"Invalid two-factor '{value}'. Must be one of: {', '.join(VALID_BODY_TWO_FACTOR)}",
            )

    # Validate two-factor-authentication if present
    if "two-factor-authentication" in payload:
        value = payload.get("two-factor-authentication")
        if value and value not in VALID_BODY_TWO_FACTOR_AUTHENTICATION:
            return (
                False,
                f"Invalid two-factor-authentication '{value}'. Must be one of: {', '.join(VALID_BODY_TWO_FACTOR_AUTHENTICATION)}",
            )

    # Validate two-factor-notification if present
    if "two-factor-notification" in payload:
        value = payload.get("two-factor-notification")
        if value and value not in VALID_BODY_TWO_FACTOR_NOTIFICATION:
            return (
                False,
                f"Invalid two-factor-notification '{value}'. Must be one of: {', '.join(VALID_BODY_TWO_FACTOR_NOTIFICATION)}",
            )

    # Validate fortitoken if present
    if "fortitoken" in payload:
        value = payload.get("fortitoken")
        if value and isinstance(value, str) and len(value) > 16:
            return (False, "fortitoken cannot exceed 16 characters")

    # Validate email-to if present
    if "email-to" in payload:
        value = payload.get("email-to")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "email-to cannot exceed 63 characters")

    # Validate sms-server if present
    if "sms-server" in payload:
        value = payload.get("sms-server")
        if value and value not in VALID_BODY_SMS_SERVER:
            return (
                False,
                f"Invalid sms-server '{value}'. Must be one of: {', '.join(VALID_BODY_SMS_SERVER)}",
            )

    # Validate sms-custom-server if present
    if "sms-custom-server" in payload:
        value = payload.get("sms-custom-server")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "sms-custom-server cannot exceed 35 characters")

    # Validate sms-phone if present
    if "sms-phone" in payload:
        value = payload.get("sms-phone")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "sms-phone cannot exceed 15 characters")

    # Validate guest-auth if present
    if "guest-auth" in payload:
        value = payload.get("guest-auth")
        if value and value not in VALID_BODY_GUEST_AUTH:
            return (
                False,
                f"Invalid guest-auth '{value}'. Must be one of: {', '.join(VALID_BODY_GUEST_AUTH)}",
            )

    # Validate guest-lang if present
    if "guest-lang" in payload:
        value = payload.get("guest-lang")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "guest-lang cannot exceed 35 characters")

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_admin_put(
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
        if value and isinstance(value, str) and len(value) > 64:
            return (False, "name cannot exceed 64 characters")

    # Validate remote-auth if present
    if "remote-auth" in payload:
        value = payload.get("remote-auth")
        if value and value not in VALID_BODY_REMOTE_AUTH:
            return (
                False,
                f"Invalid remote-auth '{value}'. Must be one of: {', '.join(VALID_BODY_REMOTE_AUTH)}",
            )

    # Validate remote-group if present
    if "remote-group" in payload:
        value = payload.get("remote-group")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "remote-group cannot exceed 35 characters")

    # Validate wildcard if present
    if "wildcard" in payload:
        value = payload.get("wildcard")
        if value and value not in VALID_BODY_WILDCARD:
            return (
                False,
                f"Invalid wildcard '{value}'. Must be one of: {', '.join(VALID_BODY_WILDCARD)}",
            )

    # Validate peer-auth if present
    if "peer-auth" in payload:
        value = payload.get("peer-auth")
        if value and value not in VALID_BODY_PEER_AUTH:
            return (
                False,
                f"Invalid peer-auth '{value}'. Must be one of: {', '.join(VALID_BODY_PEER_AUTH)}",
            )

    # Validate peer-group if present
    if "peer-group" in payload:
        value = payload.get("peer-group")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "peer-group cannot exceed 35 characters")

    # Validate accprofile if present
    if "accprofile" in payload:
        value = payload.get("accprofile")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "accprofile cannot exceed 35 characters")

    # Validate allow-remove-admin-session if present
    if "allow-remove-admin-session" in payload:
        value = payload.get("allow-remove-admin-session")
        if value and value not in VALID_BODY_ALLOW_REMOVE_ADMIN_SESSION:
            return (
                False,
                f"Invalid allow-remove-admin-session '{value}'. Must be one of: {', '.join(VALID_BODY_ALLOW_REMOVE_ADMIN_SESSION)}",
            )

    # Validate comments if present
    if "comments" in payload:
        value = payload.get("comments")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "comments cannot exceed 255 characters")

    # Validate ssh-certificate if present
    if "ssh-certificate" in payload:
        value = payload.get("ssh-certificate")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "ssh-certificate cannot exceed 35 characters")

    # Validate schedule if present
    if "schedule" in payload:
        value = payload.get("schedule")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "schedule cannot exceed 35 characters")

    # Validate accprofile-override if present
    if "accprofile-override" in payload:
        value = payload.get("accprofile-override")
        if value and value not in VALID_BODY_ACCPROFILE_OVERRIDE:
            return (
                False,
                f"Invalid accprofile-override '{value}'. Must be one of: {', '.join(VALID_BODY_ACCPROFILE_OVERRIDE)}",
            )

    # Validate vdom-override if present
    if "vdom-override" in payload:
        value = payload.get("vdom-override")
        if value and value not in VALID_BODY_VDOM_OVERRIDE:
            return (
                False,
                f"Invalid vdom-override '{value}'. Must be one of: {', '.join(VALID_BODY_VDOM_OVERRIDE)}",
            )

    # Validate force-password-change if present
    if "force-password-change" in payload:
        value = payload.get("force-password-change")
        if value and value not in VALID_BODY_FORCE_PASSWORD_CHANGE:
            return (
                False,
                f"Invalid force-password-change '{value}'. Must be one of: {', '.join(VALID_BODY_FORCE_PASSWORD_CHANGE)}",
            )

    # Validate two-factor if present
    if "two-factor" in payload:
        value = payload.get("two-factor")
        if value and value not in VALID_BODY_TWO_FACTOR:
            return (
                False,
                f"Invalid two-factor '{value}'. Must be one of: {', '.join(VALID_BODY_TWO_FACTOR)}",
            )

    # Validate two-factor-authentication if present
    if "two-factor-authentication" in payload:
        value = payload.get("two-factor-authentication")
        if value and value not in VALID_BODY_TWO_FACTOR_AUTHENTICATION:
            return (
                False,
                f"Invalid two-factor-authentication '{value}'. Must be one of: {', '.join(VALID_BODY_TWO_FACTOR_AUTHENTICATION)}",
            )

    # Validate two-factor-notification if present
    if "two-factor-notification" in payload:
        value = payload.get("two-factor-notification")
        if value and value not in VALID_BODY_TWO_FACTOR_NOTIFICATION:
            return (
                False,
                f"Invalid two-factor-notification '{value}'. Must be one of: {', '.join(VALID_BODY_TWO_FACTOR_NOTIFICATION)}",
            )

    # Validate fortitoken if present
    if "fortitoken" in payload:
        value = payload.get("fortitoken")
        if value and isinstance(value, str) and len(value) > 16:
            return (False, "fortitoken cannot exceed 16 characters")

    # Validate email-to if present
    if "email-to" in payload:
        value = payload.get("email-to")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "email-to cannot exceed 63 characters")

    # Validate sms-server if present
    if "sms-server" in payload:
        value = payload.get("sms-server")
        if value and value not in VALID_BODY_SMS_SERVER:
            return (
                False,
                f"Invalid sms-server '{value}'. Must be one of: {', '.join(VALID_BODY_SMS_SERVER)}",
            )

    # Validate sms-custom-server if present
    if "sms-custom-server" in payload:
        value = payload.get("sms-custom-server")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "sms-custom-server cannot exceed 35 characters")

    # Validate sms-phone if present
    if "sms-phone" in payload:
        value = payload.get("sms-phone")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "sms-phone cannot exceed 15 characters")

    # Validate guest-auth if present
    if "guest-auth" in payload:
        value = payload.get("guest-auth")
        if value and value not in VALID_BODY_GUEST_AUTH:
            return (
                False,
                f"Invalid guest-auth '{value}'. Must be one of: {', '.join(VALID_BODY_GUEST_AUTH)}",
            )

    # Validate guest-lang if present
    if "guest-lang" in payload:
        value = payload.get("guest-lang")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "guest-lang cannot exceed 35 characters")

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_admin_delete(name: str | None = None) -> tuple[bool, str | None]:
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
