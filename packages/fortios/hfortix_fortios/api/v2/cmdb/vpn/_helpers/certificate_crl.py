"""
Validation helpers for vpn certificate_crl endpoint.

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
    "name",  # Name.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "range": "vdom",
    "scep-cert": "Fortinet_CA_SSL",
    "source": "user",
    "source-ip": "0.0.0.0",
    "update-vdom": "root",
}


# Valid enum values from API documentation
VALID_BODY_RANGE = ["global", "vdom"]
VALID_BODY_SOURCE = ["factory", "user", "bundle"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_certificate_crl_get(
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
    Validate required fields for vpn_certificate_crl.

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


def validate_certificate_crl_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload.

    This validator performs two-stage validation:
    1. Required fields validation (schema-based)
    2. Field value validation (enums, ranges, formats)

    Required fields:
      - name: Name.

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

    # Validate range if present
    if "range" in payload:
        value = payload.get("range")
        if value and value not in VALID_BODY_RANGE:
            return (
                False,
                f"Invalid range '{value}'. Must be one of: {', '.join(VALID_BODY_RANGE)}",
            )

    # Validate source if present
    if "source" in payload:
        value = payload.get("source")
        if value and value not in VALID_BODY_SOURCE:
            return (
                False,
                f"Invalid source '{value}'. Must be one of: {', '.join(VALID_BODY_SOURCE)}",
            )

    # Validate update-vdom if present
    if "update-vdom" in payload:
        value = payload.get("update-vdom")
        if value and isinstance(value, str) and len(value) > 31:
            return (False, "update-vdom cannot exceed 31 characters")

    # Validate ldap-server if present
    if "ldap-server" in payload:
        value = payload.get("ldap-server")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "ldap-server cannot exceed 35 characters")

    # Validate ldap-username if present
    if "ldap-username" in payload:
        value = payload.get("ldap-username")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "ldap-username cannot exceed 63 characters")

    # Validate http-url if present
    if "http-url" in payload:
        value = payload.get("http-url")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "http-url cannot exceed 255 characters")

    # Validate scep-url if present
    if "scep-url" in payload:
        value = payload.get("scep-url")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "scep-url cannot exceed 255 characters")

    # Validate scep-cert if present
    if "scep-cert" in payload:
        value = payload.get("scep-cert")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "scep-cert cannot exceed 35 characters")

    # Validate update-interval if present
    if "update-interval" in payload:
        value = payload.get("update-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "update-interval must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"update-interval must be numeric, got: {value}",
                )

    return (True, None)
