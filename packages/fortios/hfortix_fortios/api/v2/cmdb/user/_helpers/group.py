"""
Validation helpers for user group endpoint.

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
    "name",  # Group name.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "auth-concurrent-override": "disable",
    "company": "optional",
    "email": "enable",
    "expire": 14400,
    "expire-type": "immediately",
    "group-type": "firewall",
    "mobile-phone": "disable",
    "multiple-guest-add": "disable",
    "password": "auto-generate",
    "sms-server": "fortiguard",
    "sponsor": "optional",
    "user-id": "email",
    "user-name": "disable",
}


# Valid enum values from API documentation
VALID_BODY_GROUP_TYPE = ["firewall", "fsso-service", "rsso", "guest"]
VALID_BODY_AUTH_CONCURRENT_OVERRIDE = ["enable", "disable"]
VALID_BODY_USER_ID = ["email", "auto-generate", "specify"]
VALID_BODY_PASSWORD = ["auto-generate", "specify", "disable"]
VALID_BODY_USER_NAME = ["disable", "enable"]
VALID_BODY_SPONSOR = ["optional", "mandatory", "disabled"]
VALID_BODY_COMPANY = ["optional", "mandatory", "disabled"]
VALID_BODY_EMAIL = ["disable", "enable"]
VALID_BODY_MOBILE_PHONE = ["disable", "enable"]
VALID_BODY_SMS_SERVER = ["fortiguard", "custom"]
VALID_BODY_EXPIRE_TYPE = ["immediately", "first-successful-login"]
VALID_BODY_MULTIPLE_GUEST_ADD = ["disable", "enable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_group_get(
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
    Validate required fields for user_group.

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


def validate_group_post(payload: dict[str, Any]) -> tuple[bool, str | None]:
    """
    Validate POST request payload.

    This validator performs two-stage validation:
    1. Required fields validation (schema-based)
    2. Field value validation (enums, ranges, formats)

    Required fields:
      - name: Group name.

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

    # Validate group-type if present
    if "group-type" in payload:
        value = payload.get("group-type")
        if value and value not in VALID_BODY_GROUP_TYPE:
            return (
                False,
                f"Invalid group-type '{value}'. Must be one of: {', '.join(VALID_BODY_GROUP_TYPE)}",
            )

    # Validate authtimeout if present
    if "authtimeout" in payload:
        value = payload.get("authtimeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 43200:
                    return (False, "authtimeout must be between 0 and 43200")
            except (ValueError, TypeError):
                return (False, f"authtimeout must be numeric, got: {value}")

    # Validate auth-concurrent-override if present
    if "auth-concurrent-override" in payload:
        value = payload.get("auth-concurrent-override")
        if value and value not in VALID_BODY_AUTH_CONCURRENT_OVERRIDE:
            return (
                False,
                f"Invalid auth-concurrent-override '{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_CONCURRENT_OVERRIDE)}",
            )

    # Validate auth-concurrent-value if present
    if "auth-concurrent-value" in payload:
        value = payload.get("auth-concurrent-value")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 100:
                    return (
                        False,
                        "auth-concurrent-value must be between 0 and 100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"auth-concurrent-value must be numeric, got: {value}",
                )

    # Validate http-digest-realm if present
    if "http-digest-realm" in payload:
        value = payload.get("http-digest-realm")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "http-digest-realm cannot exceed 35 characters")

    # Validate sso-attribute-value if present
    if "sso-attribute-value" in payload:
        value = payload.get("sso-attribute-value")
        if value and isinstance(value, str) and len(value) > 511:
            return (False, "sso-attribute-value cannot exceed 511 characters")

    # Validate user-id if present
    if "user-id" in payload:
        value = payload.get("user-id")
        if value and value not in VALID_BODY_USER_ID:
            return (
                False,
                f"Invalid user-id '{value}'. Must be one of: {', '.join(VALID_BODY_USER_ID)}",
            )

    # Validate password if present
    if "password" in payload:
        value = payload.get("password")
        if value and value not in VALID_BODY_PASSWORD:
            return (
                False,
                f"Invalid password '{value}'. Must be one of: {', '.join(VALID_BODY_PASSWORD)}",
            )

    # Validate user-name if present
    if "user-name" in payload:
        value = payload.get("user-name")
        if value and value not in VALID_BODY_USER_NAME:
            return (
                False,
                f"Invalid user-name '{value}'. Must be one of: {', '.join(VALID_BODY_USER_NAME)}",
            )

    # Validate sponsor if present
    if "sponsor" in payload:
        value = payload.get("sponsor")
        if value and value not in VALID_BODY_SPONSOR:
            return (
                False,
                f"Invalid sponsor '{value}'. Must be one of: {', '.join(VALID_BODY_SPONSOR)}",
            )

    # Validate company if present
    if "company" in payload:
        value = payload.get("company")
        if value and value not in VALID_BODY_COMPANY:
            return (
                False,
                f"Invalid company '{value}'. Must be one of: {', '.join(VALID_BODY_COMPANY)}",
            )

    # Validate email if present
    if "email" in payload:
        value = payload.get("email")
        if value and value not in VALID_BODY_EMAIL:
            return (
                False,
                f"Invalid email '{value}'. Must be one of: {', '.join(VALID_BODY_EMAIL)}",
            )

    # Validate mobile-phone if present
    if "mobile-phone" in payload:
        value = payload.get("mobile-phone")
        if value and value not in VALID_BODY_MOBILE_PHONE:
            return (
                False,
                f"Invalid mobile-phone '{value}'. Must be one of: {', '.join(VALID_BODY_MOBILE_PHONE)}",
            )

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

    # Validate expire-type if present
    if "expire-type" in payload:
        value = payload.get("expire-type")
        if value and value not in VALID_BODY_EXPIRE_TYPE:
            return (
                False,
                f"Invalid expire-type '{value}'. Must be one of: {', '.join(VALID_BODY_EXPIRE_TYPE)}",
            )

    # Validate expire if present
    if "expire" in payload:
        value = payload.get("expire")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 31536000:
                    return (False, "expire must be between 1 and 31536000")
            except (ValueError, TypeError):
                return (False, f"expire must be numeric, got: {value}")

    # Validate max-accounts if present
    if "max-accounts" in payload:
        value = payload.get("max-accounts")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 500:
                    return (False, "max-accounts must be between 0 and 500")
            except (ValueError, TypeError):
                return (False, f"max-accounts must be numeric, got: {value}")

    # Validate multiple-guest-add if present
    if "multiple-guest-add" in payload:
        value = payload.get("multiple-guest-add")
        if value and value not in VALID_BODY_MULTIPLE_GUEST_ADD:
            return (
                False,
                f"Invalid multiple-guest-add '{value}'. Must be one of: {', '.join(VALID_BODY_MULTIPLE_GUEST_ADD)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_group_put(
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

    # Validate group-type if present
    if "group-type" in payload:
        value = payload.get("group-type")
        if value and value not in VALID_BODY_GROUP_TYPE:
            return (
                False,
                f"Invalid group-type '{value}'. Must be one of: {', '.join(VALID_BODY_GROUP_TYPE)}",
            )

    # Validate authtimeout if present
    if "authtimeout" in payload:
        value = payload.get("authtimeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 43200:
                    return (False, "authtimeout must be between 0 and 43200")
            except (ValueError, TypeError):
                return (False, f"authtimeout must be numeric, got: {value}")

    # Validate auth-concurrent-override if present
    if "auth-concurrent-override" in payload:
        value = payload.get("auth-concurrent-override")
        if value and value not in VALID_BODY_AUTH_CONCURRENT_OVERRIDE:
            return (
                False,
                f"Invalid auth-concurrent-override '{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_CONCURRENT_OVERRIDE)}",
            )

    # Validate auth-concurrent-value if present
    if "auth-concurrent-value" in payload:
        value = payload.get("auth-concurrent-value")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 100:
                    return (
                        False,
                        "auth-concurrent-value must be between 0 and 100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"auth-concurrent-value must be numeric, got: {value}",
                )

    # Validate http-digest-realm if present
    if "http-digest-realm" in payload:
        value = payload.get("http-digest-realm")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "http-digest-realm cannot exceed 35 characters")

    # Validate sso-attribute-value if present
    if "sso-attribute-value" in payload:
        value = payload.get("sso-attribute-value")
        if value and isinstance(value, str) and len(value) > 511:
            return (False, "sso-attribute-value cannot exceed 511 characters")

    # Validate user-id if present
    if "user-id" in payload:
        value = payload.get("user-id")
        if value and value not in VALID_BODY_USER_ID:
            return (
                False,
                f"Invalid user-id '{value}'. Must be one of: {', '.join(VALID_BODY_USER_ID)}",
            )

    # Validate password if present
    if "password" in payload:
        value = payload.get("password")
        if value and value not in VALID_BODY_PASSWORD:
            return (
                False,
                f"Invalid password '{value}'. Must be one of: {', '.join(VALID_BODY_PASSWORD)}",
            )

    # Validate user-name if present
    if "user-name" in payload:
        value = payload.get("user-name")
        if value and value not in VALID_BODY_USER_NAME:
            return (
                False,
                f"Invalid user-name '{value}'. Must be one of: {', '.join(VALID_BODY_USER_NAME)}",
            )

    # Validate sponsor if present
    if "sponsor" in payload:
        value = payload.get("sponsor")
        if value and value not in VALID_BODY_SPONSOR:
            return (
                False,
                f"Invalid sponsor '{value}'. Must be one of: {', '.join(VALID_BODY_SPONSOR)}",
            )

    # Validate company if present
    if "company" in payload:
        value = payload.get("company")
        if value and value not in VALID_BODY_COMPANY:
            return (
                False,
                f"Invalid company '{value}'. Must be one of: {', '.join(VALID_BODY_COMPANY)}",
            )

    # Validate email if present
    if "email" in payload:
        value = payload.get("email")
        if value and value not in VALID_BODY_EMAIL:
            return (
                False,
                f"Invalid email '{value}'. Must be one of: {', '.join(VALID_BODY_EMAIL)}",
            )

    # Validate mobile-phone if present
    if "mobile-phone" in payload:
        value = payload.get("mobile-phone")
        if value and value not in VALID_BODY_MOBILE_PHONE:
            return (
                False,
                f"Invalid mobile-phone '{value}'. Must be one of: {', '.join(VALID_BODY_MOBILE_PHONE)}",
            )

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

    # Validate expire-type if present
    if "expire-type" in payload:
        value = payload.get("expire-type")
        if value and value not in VALID_BODY_EXPIRE_TYPE:
            return (
                False,
                f"Invalid expire-type '{value}'. Must be one of: {', '.join(VALID_BODY_EXPIRE_TYPE)}",
            )

    # Validate expire if present
    if "expire" in payload:
        value = payload.get("expire")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 31536000:
                    return (False, "expire must be between 1 and 31536000")
            except (ValueError, TypeError):
                return (False, f"expire must be numeric, got: {value}")

    # Validate max-accounts if present
    if "max-accounts" in payload:
        value = payload.get("max-accounts")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 500:
                    return (False, "max-accounts must be between 0 and 500")
            except (ValueError, TypeError):
                return (False, f"max-accounts must be numeric, got: {value}")

    # Validate multiple-guest-add if present
    if "multiple-guest-add" in payload:
        value = payload.get("multiple-guest-add")
        if value and value not in VALID_BODY_MULTIPLE_GUEST_ADD:
            return (
                False,
                f"Invalid multiple-guest-add '{value}'. Must be one of: {', '.join(VALID_BODY_MULTIPLE_GUEST_ADD)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_group_delete(name: str | None = None) -> tuple[bool, str | None]:
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
