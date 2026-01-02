"""
Validation helpers for dnsfilter profile endpoint.

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
    "name",  # Profile name.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "block-action": "redirect",
    "block-botnet": "disable",
    "log-all-domain": "disable",
    "redirect-portal": "0.0.0.0",
    "redirect-portal6": "::",
    "safe-search": "disable",
    "sdns-domain-log": "enable",
    "sdns-ftgd-err-log": "enable",
    "strip-ech": "enable",
    "youtube-restrict": "strict",
}


# Valid enum values from API documentation
VALID_BODY_LOG_ALL_DOMAIN = ["enable", "disable"]
VALID_BODY_SDNS_FTGD_ERR_LOG = ["enable", "disable"]
VALID_BODY_SDNS_DOMAIN_LOG = ["enable", "disable"]
VALID_BODY_BLOCK_ACTION = ["block", "redirect", "block-sevrfail"]
VALID_BODY_BLOCK_BOTNET = ["disable", "enable"]
VALID_BODY_SAFE_SEARCH = ["disable", "enable"]
VALID_BODY_YOUTUBE_RESTRICT = ["strict", "moderate", "none"]
VALID_BODY_STRIP_ECH = ["disable", "enable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_profile_get(
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
    Validate required fields for dnsfilter_profile.

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


def validate_profile_post(payload: dict[str, Any]) -> tuple[bool, str | None]:
    """
    Validate POST request payload.

    This validator performs two-stage validation:
    1. Required fields validation (schema-based)
    2. Field value validation (enums, ranges, formats)

    Required fields:
      - name: Profile name.

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
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "name cannot exceed 47 characters")

    # Validate comment if present
    if "comment" in payload:
        value = payload.get("comment")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "comment cannot exceed 255 characters")

    # Validate log-all-domain if present
    if "log-all-domain" in payload:
        value = payload.get("log-all-domain")
        if value and value not in VALID_BODY_LOG_ALL_DOMAIN:
            return (
                False,
                f"Invalid log-all-domain '{value}'. Must be one of: {', '.join(VALID_BODY_LOG_ALL_DOMAIN)}",
            )

    # Validate sdns-ftgd-err-log if present
    if "sdns-ftgd-err-log" in payload:
        value = payload.get("sdns-ftgd-err-log")
        if value and value not in VALID_BODY_SDNS_FTGD_ERR_LOG:
            return (
                False,
                f"Invalid sdns-ftgd-err-log '{value}'. Must be one of: {', '.join(VALID_BODY_SDNS_FTGD_ERR_LOG)}",
            )

    # Validate sdns-domain-log if present
    if "sdns-domain-log" in payload:
        value = payload.get("sdns-domain-log")
        if value and value not in VALID_BODY_SDNS_DOMAIN_LOG:
            return (
                False,
                f"Invalid sdns-domain-log '{value}'. Must be one of: {', '.join(VALID_BODY_SDNS_DOMAIN_LOG)}",
            )

    # Validate block-action if present
    if "block-action" in payload:
        value = payload.get("block-action")
        if value and value not in VALID_BODY_BLOCK_ACTION:
            return (
                False,
                f"Invalid block-action '{value}'. Must be one of: {', '.join(VALID_BODY_BLOCK_ACTION)}",
            )

    # Validate block-botnet if present
    if "block-botnet" in payload:
        value = payload.get("block-botnet")
        if value and value not in VALID_BODY_BLOCK_BOTNET:
            return (
                False,
                f"Invalid block-botnet '{value}'. Must be one of: {', '.join(VALID_BODY_BLOCK_BOTNET)}",
            )

    # Validate safe-search if present
    if "safe-search" in payload:
        value = payload.get("safe-search")
        if value and value not in VALID_BODY_SAFE_SEARCH:
            return (
                False,
                f"Invalid safe-search '{value}'. Must be one of: {', '.join(VALID_BODY_SAFE_SEARCH)}",
            )

    # Validate youtube-restrict if present
    if "youtube-restrict" in payload:
        value = payload.get("youtube-restrict")
        if value and value not in VALID_BODY_YOUTUBE_RESTRICT:
            return (
                False,
                f"Invalid youtube-restrict '{value}'. Must be one of: {', '.join(VALID_BODY_YOUTUBE_RESTRICT)}",
            )

    # Validate strip-ech if present
    if "strip-ech" in payload:
        value = payload.get("strip-ech")
        if value and value not in VALID_BODY_STRIP_ECH:
            return (
                False,
                f"Invalid strip-ech '{value}'. Must be one of: {', '.join(VALID_BODY_STRIP_ECH)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_profile_put(
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

    # Validate comment if present
    if "comment" in payload:
        value = payload.get("comment")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "comment cannot exceed 255 characters")

    # Validate log-all-domain if present
    if "log-all-domain" in payload:
        value = payload.get("log-all-domain")
        if value and value not in VALID_BODY_LOG_ALL_DOMAIN:
            return (
                False,
                f"Invalid log-all-domain '{value}'. Must be one of: {', '.join(VALID_BODY_LOG_ALL_DOMAIN)}",
            )

    # Validate sdns-ftgd-err-log if present
    if "sdns-ftgd-err-log" in payload:
        value = payload.get("sdns-ftgd-err-log")
        if value and value not in VALID_BODY_SDNS_FTGD_ERR_LOG:
            return (
                False,
                f"Invalid sdns-ftgd-err-log '{value}'. Must be one of: {', '.join(VALID_BODY_SDNS_FTGD_ERR_LOG)}",
            )

    # Validate sdns-domain-log if present
    if "sdns-domain-log" in payload:
        value = payload.get("sdns-domain-log")
        if value and value not in VALID_BODY_SDNS_DOMAIN_LOG:
            return (
                False,
                f"Invalid sdns-domain-log '{value}'. Must be one of: {', '.join(VALID_BODY_SDNS_DOMAIN_LOG)}",
            )

    # Validate block-action if present
    if "block-action" in payload:
        value = payload.get("block-action")
        if value and value not in VALID_BODY_BLOCK_ACTION:
            return (
                False,
                f"Invalid block-action '{value}'. Must be one of: {', '.join(VALID_BODY_BLOCK_ACTION)}",
            )

    # Validate block-botnet if present
    if "block-botnet" in payload:
        value = payload.get("block-botnet")
        if value and value not in VALID_BODY_BLOCK_BOTNET:
            return (
                False,
                f"Invalid block-botnet '{value}'. Must be one of: {', '.join(VALID_BODY_BLOCK_BOTNET)}",
            )

    # Validate safe-search if present
    if "safe-search" in payload:
        value = payload.get("safe-search")
        if value and value not in VALID_BODY_SAFE_SEARCH:
            return (
                False,
                f"Invalid safe-search '{value}'. Must be one of: {', '.join(VALID_BODY_SAFE_SEARCH)}",
            )

    # Validate youtube-restrict if present
    if "youtube-restrict" in payload:
        value = payload.get("youtube-restrict")
        if value and value not in VALID_BODY_YOUTUBE_RESTRICT:
            return (
                False,
                f"Invalid youtube-restrict '{value}'. Must be one of: {', '.join(VALID_BODY_YOUTUBE_RESTRICT)}",
            )

    # Validate strip-ech if present
    if "strip-ech" in payload:
        value = payload.get("strip-ech")
        if value and value not in VALID_BODY_STRIP_ECH:
            return (
                False,
                f"Invalid strip-ech '{value}'. Must be one of: {', '.join(VALID_BODY_STRIP_ECH)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_profile_delete(
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
