"""
Validation helpers for vpn certificate_ca endpoint.

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
    "ca",  # CA certificate as a PEM file.
    "name",  # Name.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "fabric-ca": "disable",
    "obsolete": "disable",
    "range": "vdom",
    "source": "user",
    "source-ip": "0.0.0.0",
    "ssl-inspection-trusted": "enable",
}


# Valid enum values from API documentation
VALID_BODY_RANGE = ["global", "vdom"]
VALID_BODY_SOURCE = ["factory", "user", "bundle"]
VALID_BODY_SSL_INSPECTION_TRUSTED = ["enable", "disable"]
VALID_BODY_OBSOLETE = ["disable", "enable"]
VALID_BODY_FABRIC_CA = ["disable", "enable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_certificate_ca_get(
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
    Validate required fields for vpn_certificate_ca.

    This validator checks:
    1. Always-required fields are present
    2. Mutually exclusive groups have at least one field

    Args:
        payload: The request payload to validate

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> is_valid, error = validate_required_fields({
        ...     "ca": "value",
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


def validate_certificate_ca_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload.

    This validator performs two-stage validation:
    1. Required fields validation (schema-based)
    2. Field value validation (enums, ranges, formats)

    Required fields:
      - ca: CA certificate as a PEM file.
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
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "name cannot exceed 79 characters")

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

    # Validate ssl-inspection-trusted if present
    if "ssl-inspection-trusted" in payload:
        value = payload.get("ssl-inspection-trusted")
        if value and value not in VALID_BODY_SSL_INSPECTION_TRUSTED:
            return (
                False,
                f"Invalid ssl-inspection-trusted '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_INSPECTION_TRUSTED)}",
            )

    # Validate scep-url if present
    if "scep-url" in payload:
        value = payload.get("scep-url")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "scep-url cannot exceed 255 characters")

    # Validate est-url if present
    if "est-url" in payload:
        value = payload.get("est-url")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "est-url cannot exceed 255 characters")

    # Validate auto-update-days if present
    if "auto-update-days" in payload:
        value = payload.get("auto-update-days")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "auto-update-days must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"auto-update-days must be numeric, got: {value}",
                )

    # Validate auto-update-days-warning if present
    if "auto-update-days-warning" in payload:
        value = payload.get("auto-update-days-warning")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "auto-update-days-warning must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"auto-update-days-warning must be numeric, got: {value}",
                )

    # Validate ca-identifier if present
    if "ca-identifier" in payload:
        value = payload.get("ca-identifier")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "ca-identifier cannot exceed 255 characters")

    # Validate obsolete if present
    if "obsolete" in payload:
        value = payload.get("obsolete")
        if value and value not in VALID_BODY_OBSOLETE:
            return (
                False,
                f"Invalid obsolete '{value}'. Must be one of: {', '.join(VALID_BODY_OBSOLETE)}",
            )

    # Validate fabric-ca if present
    if "fabric-ca" in payload:
        value = payload.get("fabric-ca")
        if value and value not in VALID_BODY_FABRIC_CA:
            return (
                False,
                f"Invalid fabric-ca '{value}'. Must be one of: {', '.join(VALID_BODY_FABRIC_CA)}",
            )

    return (True, None)
