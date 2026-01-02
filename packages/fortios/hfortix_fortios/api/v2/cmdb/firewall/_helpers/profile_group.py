"""
Validation helpers for firewall profile_group endpoint.

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
    "name",  # Profile group name.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "profile-protocol-options": "default",
    "ssl-ssh-profile": "certificate-inspection",
}


# Valid enum values from API documentation
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_profile_group_get(
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
    Validate required fields for firewall_profile-group.

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


def validate_profile_group_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload.

    This validator performs two-stage validation:
    1. Required fields validation (schema-based)
    2. Field value validation (enums, ranges, formats)

    Required fields:
      - name: Profile group name.

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

    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate field values (enums, ranges, etc.)
    # Validate name if present
    if "name" in payload:
        value = payload.get("name")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "name cannot exceed 47 characters")

    # Validate profile-protocol-options if present
    if "profile-protocol-options" in payload:
        value = payload.get("profile-protocol-options")
        if value and isinstance(value, str) and len(value) > 47:
            return (
                False,
                "profile-protocol-options cannot exceed 47 characters",
            )

    # Validate ssl-ssh-profile if present
    if "ssl-ssh-profile" in payload:
        value = payload.get("ssl-ssh-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "ssl-ssh-profile cannot exceed 47 characters")

    # Validate av-profile if present
    if "av-profile" in payload:
        value = payload.get("av-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "av-profile cannot exceed 47 characters")

    # Validate webfilter-profile if present
    if "webfilter-profile" in payload:
        value = payload.get("webfilter-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "webfilter-profile cannot exceed 47 characters")

    # Validate dnsfilter-profile if present
    if "dnsfilter-profile" in payload:
        value = payload.get("dnsfilter-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "dnsfilter-profile cannot exceed 47 characters")

    # Validate emailfilter-profile if present
    if "emailfilter-profile" in payload:
        value = payload.get("emailfilter-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "emailfilter-profile cannot exceed 47 characters")

    # Validate dlp-profile if present
    if "dlp-profile" in payload:
        value = payload.get("dlp-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "dlp-profile cannot exceed 47 characters")

    # Validate file-filter-profile if present
    if "file-filter-profile" in payload:
        value = payload.get("file-filter-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "file-filter-profile cannot exceed 47 characters")

    # Validate ips-sensor if present
    if "ips-sensor" in payload:
        value = payload.get("ips-sensor")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "ips-sensor cannot exceed 47 characters")

    # Validate application-list if present
    if "application-list" in payload:
        value = payload.get("application-list")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "application-list cannot exceed 47 characters")

    # Validate voip-profile if present
    if "voip-profile" in payload:
        value = payload.get("voip-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "voip-profile cannot exceed 47 characters")

    # Validate ips-voip-filter if present
    if "ips-voip-filter" in payload:
        value = payload.get("ips-voip-filter")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "ips-voip-filter cannot exceed 47 characters")

    # Validate sctp-filter-profile if present
    if "sctp-filter-profile" in payload:
        value = payload.get("sctp-filter-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "sctp-filter-profile cannot exceed 47 characters")

    # Validate diameter-filter-profile if present
    if "diameter-filter-profile" in payload:
        value = payload.get("diameter-filter-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (
                False,
                "diameter-filter-profile cannot exceed 47 characters",
            )

    # Validate virtual-patch-profile if present
    if "virtual-patch-profile" in payload:
        value = payload.get("virtual-patch-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (
                False,
                "virtual-patch-profile cannot exceed 47 characters",
            )

    # Validate icap-profile if present
    if "icap-profile" in payload:
        value = payload.get("icap-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "icap-profile cannot exceed 47 characters")

    # Validate videofilter-profile if present
    if "videofilter-profile" in payload:
        value = payload.get("videofilter-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "videofilter-profile cannot exceed 47 characters")

    # Validate waf-profile if present
    if "waf-profile" in payload:
        value = payload.get("waf-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "waf-profile cannot exceed 47 characters")

    # Validate ssh-filter-profile if present
    if "ssh-filter-profile" in payload:
        value = payload.get("ssh-filter-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "ssh-filter-profile cannot exceed 47 characters")

    # Validate casb-profile if present
    if "casb-profile" in payload:
        value = payload.get("casb-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "casb-profile cannot exceed 47 characters")

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_profile_group_put(
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
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "name cannot exceed 47 characters")

    # Validate profile-protocol-options if present
    if "profile-protocol-options" in payload:
        value = payload.get("profile-protocol-options")
        if value and isinstance(value, str) and len(value) > 47:
            return (
                False,
                "profile-protocol-options cannot exceed 47 characters",
            )

    # Validate ssl-ssh-profile if present
    if "ssl-ssh-profile" in payload:
        value = payload.get("ssl-ssh-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "ssl-ssh-profile cannot exceed 47 characters")

    # Validate av-profile if present
    if "av-profile" in payload:
        value = payload.get("av-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "av-profile cannot exceed 47 characters")

    # Validate webfilter-profile if present
    if "webfilter-profile" in payload:
        value = payload.get("webfilter-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "webfilter-profile cannot exceed 47 characters")

    # Validate dnsfilter-profile if present
    if "dnsfilter-profile" in payload:
        value = payload.get("dnsfilter-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "dnsfilter-profile cannot exceed 47 characters")

    # Validate emailfilter-profile if present
    if "emailfilter-profile" in payload:
        value = payload.get("emailfilter-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "emailfilter-profile cannot exceed 47 characters")

    # Validate dlp-profile if present
    if "dlp-profile" in payload:
        value = payload.get("dlp-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "dlp-profile cannot exceed 47 characters")

    # Validate file-filter-profile if present
    if "file-filter-profile" in payload:
        value = payload.get("file-filter-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "file-filter-profile cannot exceed 47 characters")

    # Validate ips-sensor if present
    if "ips-sensor" in payload:
        value = payload.get("ips-sensor")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "ips-sensor cannot exceed 47 characters")

    # Validate application-list if present
    if "application-list" in payload:
        value = payload.get("application-list")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "application-list cannot exceed 47 characters")

    # Validate voip-profile if present
    if "voip-profile" in payload:
        value = payload.get("voip-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "voip-profile cannot exceed 47 characters")

    # Validate ips-voip-filter if present
    if "ips-voip-filter" in payload:
        value = payload.get("ips-voip-filter")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "ips-voip-filter cannot exceed 47 characters")

    # Validate sctp-filter-profile if present
    if "sctp-filter-profile" in payload:
        value = payload.get("sctp-filter-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "sctp-filter-profile cannot exceed 47 characters")

    # Validate diameter-filter-profile if present
    if "diameter-filter-profile" in payload:
        value = payload.get("diameter-filter-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (
                False,
                "diameter-filter-profile cannot exceed 47 characters",
            )

    # Validate virtual-patch-profile if present
    if "virtual-patch-profile" in payload:
        value = payload.get("virtual-patch-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (
                False,
                "virtual-patch-profile cannot exceed 47 characters",
            )

    # Validate icap-profile if present
    if "icap-profile" in payload:
        value = payload.get("icap-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "icap-profile cannot exceed 47 characters")

    # Validate videofilter-profile if present
    if "videofilter-profile" in payload:
        value = payload.get("videofilter-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "videofilter-profile cannot exceed 47 characters")

    # Validate waf-profile if present
    if "waf-profile" in payload:
        value = payload.get("waf-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "waf-profile cannot exceed 47 characters")

    # Validate ssh-filter-profile if present
    if "ssh-filter-profile" in payload:
        value = payload.get("ssh-filter-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "ssh-filter-profile cannot exceed 47 characters")

    # Validate casb-profile if present
    if "casb-profile" in payload:
        value = payload.get("casb-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "casb-profile cannot exceed 47 characters")

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_profile_group_delete(
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
