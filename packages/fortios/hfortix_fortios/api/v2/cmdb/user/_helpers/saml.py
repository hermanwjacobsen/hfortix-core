"""
Validation helpers for user saml endpoint.

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
    "entity-id",  # SP entity ID.
    "idp-cert",  # IDP Certificate name.
    "idp-entity-id",  # IDP entity ID.
    "idp-single-sign-on-url",  # IDP single sign-on URL.
    "name",  # SAML server entry name.
    "single-sign-on-url",  # SP single sign-on URL.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "adfs-claim": "disable",
    "clock-tolerance": 15,
    "digest-method": "sha1",
    "group-claim-type": "group",
    "limit-relaystate": "disable",
    "reauth": "disable",
    "scim-group-attr-type": "display-name",
    "scim-user-attr-type": "user-name",
    "user-claim-type": "upn",
}


# Valid enum values from API documentation
VALID_BODY_SCIM_USER_ATTR_TYPE = [
    "user-name",
    "display-name",
    "external-id",
    "email",
]
VALID_BODY_SCIM_GROUP_ATTR_TYPE = ["display-name", "external-id"]
VALID_BODY_DIGEST_METHOD = ["sha1", "sha256"]
VALID_BODY_REQUIRE_SIGNED_RESP_AND_ASRT = ["enable", "disable"]
VALID_BODY_LIMIT_RELAYSTATE = ["enable", "disable"]
VALID_BODY_ADFS_CLAIM = ["enable", "disable"]
VALID_BODY_USER_CLAIM_TYPE = [
    "email",
    "given-name",
    "name",
    "upn",
    "common-name",
    "email-adfs-1x",
    "group",
    "upn-adfs-1x",
    "role",
    "sur-name",
    "ppid",
    "name-identifier",
    "authentication-method",
    "deny-only-group-sid",
    "deny-only-primary-sid",
    "deny-only-primary-group-sid",
    "group-sid",
    "primary-group-sid",
    "primary-sid",
    "windows-account-name",
]
VALID_BODY_GROUP_CLAIM_TYPE = [
    "email",
    "given-name",
    "name",
    "upn",
    "common-name",
    "email-adfs-1x",
    "group",
    "upn-adfs-1x",
    "role",
    "sur-name",
    "ppid",
    "name-identifier",
    "authentication-method",
    "deny-only-group-sid",
    "deny-only-primary-sid",
    "deny-only-primary-group-sid",
    "group-sid",
    "primary-group-sid",
    "primary-sid",
    "windows-account-name",
]
VALID_BODY_REAUTH = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_saml_get(
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
    Validate required fields for user_saml.

    This validator checks:
    1. Always-required fields are present
    2. Mutually exclusive groups have at least one field

    Args:
        payload: The request payload to validate

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> is_valid, error = validate_required_fields({
        ...     "entity-id": "value",
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


def validate_saml_post(payload: dict[str, Any]) -> tuple[bool, str | None]:
    """
    Validate POST request payload.

    This validator performs two-stage validation:
    1. Required fields validation (schema-based)
    2. Field value validation (enums, ranges, formats)

    Required fields:
      - entity-id: SP entity ID.
      - idp-cert: IDP Certificate name.
      - idp-entity-id: IDP entity ID.
      - idp-single-sign-on-url: IDP single sign-on URL.
      - name: SAML server entry name.
      - single-sign-on-url: SP single sign-on URL.

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

    # Validate cert if present
    if "cert" in payload:
        value = payload.get("cert")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "cert cannot exceed 35 characters")

    # Validate entity-id if present
    if "entity-id" in payload:
        value = payload.get("entity-id")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "entity-id cannot exceed 255 characters")

    # Validate single-sign-on-url if present
    if "single-sign-on-url" in payload:
        value = payload.get("single-sign-on-url")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "single-sign-on-url cannot exceed 255 characters")

    # Validate single-logout-url if present
    if "single-logout-url" in payload:
        value = payload.get("single-logout-url")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "single-logout-url cannot exceed 255 characters")

    # Validate idp-entity-id if present
    if "idp-entity-id" in payload:
        value = payload.get("idp-entity-id")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "idp-entity-id cannot exceed 255 characters")

    # Validate idp-single-sign-on-url if present
    if "idp-single-sign-on-url" in payload:
        value = payload.get("idp-single-sign-on-url")
        if value and isinstance(value, str) and len(value) > 255:
            return (
                False,
                "idp-single-sign-on-url cannot exceed 255 characters",
            )

    # Validate idp-single-logout-url if present
    if "idp-single-logout-url" in payload:
        value = payload.get("idp-single-logout-url")
        if value and isinstance(value, str) and len(value) > 255:
            return (
                False,
                "idp-single-logout-url cannot exceed 255 characters",
            )

    # Validate idp-cert if present
    if "idp-cert" in payload:
        value = payload.get("idp-cert")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "idp-cert cannot exceed 35 characters")

    # Validate scim-client if present
    if "scim-client" in payload:
        value = payload.get("scim-client")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "scim-client cannot exceed 35 characters")

    # Validate scim-user-attr-type if present
    if "scim-user-attr-type" in payload:
        value = payload.get("scim-user-attr-type")
        if value and value not in VALID_BODY_SCIM_USER_ATTR_TYPE:
            return (
                False,
                f"Invalid scim-user-attr-type '{value}'. Must be one of: {', '.join(VALID_BODY_SCIM_USER_ATTR_TYPE)}",
            )

    # Validate scim-group-attr-type if present
    if "scim-group-attr-type" in payload:
        value = payload.get("scim-group-attr-type")
        if value and value not in VALID_BODY_SCIM_GROUP_ATTR_TYPE:
            return (
                False,
                f"Invalid scim-group-attr-type '{value}'. Must be one of: {', '.join(VALID_BODY_SCIM_GROUP_ATTR_TYPE)}",
            )

    # Validate user-name if present
    if "user-name" in payload:
        value = payload.get("user-name")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "user-name cannot exceed 255 characters")

    # Validate group-name if present
    if "group-name" in payload:
        value = payload.get("group-name")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "group-name cannot exceed 255 characters")

    # Validate digest-method if present
    if "digest-method" in payload:
        value = payload.get("digest-method")
        if value and value not in VALID_BODY_DIGEST_METHOD:
            return (
                False,
                f"Invalid digest-method '{value}'. Must be one of: {', '.join(VALID_BODY_DIGEST_METHOD)}",
            )

    # Validate require-signed-resp-and-asrt if present
    if "require-signed-resp-and-asrt" in payload:
        value = payload.get("require-signed-resp-and-asrt")
        if value and value not in VALID_BODY_REQUIRE_SIGNED_RESP_AND_ASRT:
            return (
                False,
                f"Invalid require-signed-resp-and-asrt '{value}'. Must be one of: {', '.join(VALID_BODY_REQUIRE_SIGNED_RESP_AND_ASRT)}",
            )

    # Validate limit-relaystate if present
    if "limit-relaystate" in payload:
        value = payload.get("limit-relaystate")
        if value and value not in VALID_BODY_LIMIT_RELAYSTATE:
            return (
                False,
                f"Invalid limit-relaystate '{value}'. Must be one of: {', '.join(VALID_BODY_LIMIT_RELAYSTATE)}",
            )

    # Validate clock-tolerance if present
    if "clock-tolerance" in payload:
        value = payload.get("clock-tolerance")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 300:
                    return (
                        False,
                        "clock-tolerance must be between 0 and 300",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"clock-tolerance must be numeric, got: {value}",
                )

    # Validate adfs-claim if present
    if "adfs-claim" in payload:
        value = payload.get("adfs-claim")
        if value and value not in VALID_BODY_ADFS_CLAIM:
            return (
                False,
                f"Invalid adfs-claim '{value}'. Must be one of: {', '.join(VALID_BODY_ADFS_CLAIM)}",
            )

    # Validate user-claim-type if present
    if "user-claim-type" in payload:
        value = payload.get("user-claim-type")
        if value and value not in VALID_BODY_USER_CLAIM_TYPE:
            return (
                False,
                f"Invalid user-claim-type '{value}'. Must be one of: {', '.join(VALID_BODY_USER_CLAIM_TYPE)}",
            )

    # Validate group-claim-type if present
    if "group-claim-type" in payload:
        value = payload.get("group-claim-type")
        if value and value not in VALID_BODY_GROUP_CLAIM_TYPE:
            return (
                False,
                f"Invalid group-claim-type '{value}'. Must be one of: {', '.join(VALID_BODY_GROUP_CLAIM_TYPE)}",
            )

    # Validate reauth if present
    if "reauth" in payload:
        value = payload.get("reauth")
        if value and value not in VALID_BODY_REAUTH:
            return (
                False,
                f"Invalid reauth '{value}'. Must be one of: {', '.join(VALID_BODY_REAUTH)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_saml_put(
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

    # Validate cert if present
    if "cert" in payload:
        value = payload.get("cert")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "cert cannot exceed 35 characters")

    # Validate entity-id if present
    if "entity-id" in payload:
        value = payload.get("entity-id")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "entity-id cannot exceed 255 characters")

    # Validate single-sign-on-url if present
    if "single-sign-on-url" in payload:
        value = payload.get("single-sign-on-url")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "single-sign-on-url cannot exceed 255 characters")

    # Validate single-logout-url if present
    if "single-logout-url" in payload:
        value = payload.get("single-logout-url")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "single-logout-url cannot exceed 255 characters")

    # Validate idp-entity-id if present
    if "idp-entity-id" in payload:
        value = payload.get("idp-entity-id")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "idp-entity-id cannot exceed 255 characters")

    # Validate idp-single-sign-on-url if present
    if "idp-single-sign-on-url" in payload:
        value = payload.get("idp-single-sign-on-url")
        if value and isinstance(value, str) and len(value) > 255:
            return (
                False,
                "idp-single-sign-on-url cannot exceed 255 characters",
            )

    # Validate idp-single-logout-url if present
    if "idp-single-logout-url" in payload:
        value = payload.get("idp-single-logout-url")
        if value and isinstance(value, str) and len(value) > 255:
            return (
                False,
                "idp-single-logout-url cannot exceed 255 characters",
            )

    # Validate idp-cert if present
    if "idp-cert" in payload:
        value = payload.get("idp-cert")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "idp-cert cannot exceed 35 characters")

    # Validate scim-client if present
    if "scim-client" in payload:
        value = payload.get("scim-client")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "scim-client cannot exceed 35 characters")

    # Validate scim-user-attr-type if present
    if "scim-user-attr-type" in payload:
        value = payload.get("scim-user-attr-type")
        if value and value not in VALID_BODY_SCIM_USER_ATTR_TYPE:
            return (
                False,
                f"Invalid scim-user-attr-type '{value}'. Must be one of: {', '.join(VALID_BODY_SCIM_USER_ATTR_TYPE)}",
            )

    # Validate scim-group-attr-type if present
    if "scim-group-attr-type" in payload:
        value = payload.get("scim-group-attr-type")
        if value and value not in VALID_BODY_SCIM_GROUP_ATTR_TYPE:
            return (
                False,
                f"Invalid scim-group-attr-type '{value}'. Must be one of: {', '.join(VALID_BODY_SCIM_GROUP_ATTR_TYPE)}",
            )

    # Validate user-name if present
    if "user-name" in payload:
        value = payload.get("user-name")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "user-name cannot exceed 255 characters")

    # Validate group-name if present
    if "group-name" in payload:
        value = payload.get("group-name")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "group-name cannot exceed 255 characters")

    # Validate digest-method if present
    if "digest-method" in payload:
        value = payload.get("digest-method")
        if value and value not in VALID_BODY_DIGEST_METHOD:
            return (
                False,
                f"Invalid digest-method '{value}'. Must be one of: {', '.join(VALID_BODY_DIGEST_METHOD)}",
            )

    # Validate require-signed-resp-and-asrt if present
    if "require-signed-resp-and-asrt" in payload:
        value = payload.get("require-signed-resp-and-asrt")
        if value and value not in VALID_BODY_REQUIRE_SIGNED_RESP_AND_ASRT:
            return (
                False,
                f"Invalid require-signed-resp-and-asrt '{value}'. Must be one of: {', '.join(VALID_BODY_REQUIRE_SIGNED_RESP_AND_ASRT)}",
            )

    # Validate limit-relaystate if present
    if "limit-relaystate" in payload:
        value = payload.get("limit-relaystate")
        if value and value not in VALID_BODY_LIMIT_RELAYSTATE:
            return (
                False,
                f"Invalid limit-relaystate '{value}'. Must be one of: {', '.join(VALID_BODY_LIMIT_RELAYSTATE)}",
            )

    # Validate clock-tolerance if present
    if "clock-tolerance" in payload:
        value = payload.get("clock-tolerance")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 300:
                    return (
                        False,
                        "clock-tolerance must be between 0 and 300",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"clock-tolerance must be numeric, got: {value}",
                )

    # Validate adfs-claim if present
    if "adfs-claim" in payload:
        value = payload.get("adfs-claim")
        if value and value not in VALID_BODY_ADFS_CLAIM:
            return (
                False,
                f"Invalid adfs-claim '{value}'. Must be one of: {', '.join(VALID_BODY_ADFS_CLAIM)}",
            )

    # Validate user-claim-type if present
    if "user-claim-type" in payload:
        value = payload.get("user-claim-type")
        if value and value not in VALID_BODY_USER_CLAIM_TYPE:
            return (
                False,
                f"Invalid user-claim-type '{value}'. Must be one of: {', '.join(VALID_BODY_USER_CLAIM_TYPE)}",
            )

    # Validate group-claim-type if present
    if "group-claim-type" in payload:
        value = payload.get("group-claim-type")
        if value and value not in VALID_BODY_GROUP_CLAIM_TYPE:
            return (
                False,
                f"Invalid group-claim-type '{value}'. Must be one of: {', '.join(VALID_BODY_GROUP_CLAIM_TYPE)}",
            )

    # Validate reauth if present
    if "reauth" in payload:
        value = payload.get("reauth")
        if value and value not in VALID_BODY_REAUTH:
            return (
                False,
                f"Invalid reauth '{value}'. Must be one of: {', '.join(VALID_BODY_REAUTH)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_saml_delete(name: str | None = None) -> tuple[bool, str | None]:
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
