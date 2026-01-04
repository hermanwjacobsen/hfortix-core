"""
Validation helpers for switch_controller/802_1X_settings endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Import common validators from central _helpers module
from hfortix_fortios._helpers import (
    validate_enable_disable,
    validate_integer_range,
    validate_string_length,
    validate_port_number,
    validate_ip_address,
    validate_ipv6_address,
    validate_mac_address,
)

# ============================================================================
# Required Fields Validation
# Auto-generated from schema
# ============================================================================

# NOTE: The FortiOS schema has known bugs where some specialized optional
# features are incorrectly marked as required. See SCHEMA_FALSE_POSITIVES
# for fields that should be OPTIONAL despite being marked required in
# the schema. The REQUIRED_FIELDS list below reflects the ACTUAL
# requirements based on API testing and schema analysis.

# Always required fields (no alternatives)
REQUIRED_FIELDS = [
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "link-down-auth": "set-unauth",
    "reauth-period": 60,
    "max-reauth-attempt": 3,
    "tx-period": 30,
    "mab-reauth": "disable",
    "mac-username-delimiter": "hyphen",
    "mac-password-delimiter": "hyphen",
    "mac-calling-station-delimiter": "hyphen",
    "mac-called-station-delimiter": "hyphen",
    "mac-case": "lowercase",
}


# Valid enum values from API documentation
VALID_BODY_LINK_DOWN_AUTH = [
    "set-unauth",
    "no-action",
]
VALID_BODY_MAB_REAUTH = [
    "disable",
    "enable",
]
VALID_BODY_MAC_USERNAME_DELIMITER = [
    "colon",
    "hyphen",
    "none",
    "single-hyphen",
]
VALID_BODY_MAC_PASSWORD_DELIMITER = [
    "colon",
    "hyphen",
    "none",
    "single-hyphen",
]
VALID_BODY_MAC_CALLING_STATION_DELIMITER = [
    "colon",
    "hyphen",
    "none",
    "single-hyphen",
]
VALID_BODY_MAC_CALLED_STATION_DELIMITER = [
    "colon",
    "hyphen",
    "none",
    "single-hyphen",
]
VALID_BODY_MAC_CASE = [
    "lowercase",
    "uppercase",
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_switch_controller_802_1X_settings_get(
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
        >>> is_valid, error = validate_switch_controller_802_1X_settings_get()
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
    Validate required fields for switch_controller/802_1X_settings.

    This validator checks:
    1. Always-required fields are present
    2. Mutually exclusive groups have at least one field

    Args:
        payload: The request payload to validate

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "test"}
        >>> is_valid, error = validate_required_fields(payload)
    """
    # Check always-required fields
    for field in REQUIRED_FIELDS:
        if field not in payload:
            return (False, f"Missing required field: {field}")

    return (True, None)


def validate_switch_controller_802_1X_settings_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create switch_controller/802_1X_settings.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {
        ...     "name": "new_item",
        ... }
        >>> is_valid, error = validate_switch_controller_802_1X_settings_post(payload)
    """
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "link-down-auth" in payload:
        value = payload["link-down-auth"]
        if value not in VALID_BODY_LINK_DOWN_AUTH:
            return (
                False,
                f"Invalid value for 'link-down-auth'='{value}'. Must be one of: {', '.join(VALID_BODY_LINK_DOWN_AUTH)}",
            )
    if "mab-reauth" in payload:
        value = payload["mab-reauth"]
        if value not in VALID_BODY_MAB_REAUTH:
            return (
                False,
                f"Invalid value for 'mab-reauth'='{value}'. Must be one of: {', '.join(VALID_BODY_MAB_REAUTH)}",
            )
    if "mac-username-delimiter" in payload:
        value = payload["mac-username-delimiter"]
        if value not in VALID_BODY_MAC_USERNAME_DELIMITER:
            return (
                False,
                f"Invalid value for 'mac-username-delimiter'='{value}'. Must be one of: {', '.join(VALID_BODY_MAC_USERNAME_DELIMITER)}",
            )
    if "mac-password-delimiter" in payload:
        value = payload["mac-password-delimiter"]
        if value not in VALID_BODY_MAC_PASSWORD_DELIMITER:
            return (
                False,
                f"Invalid value for 'mac-password-delimiter'='{value}'. Must be one of: {', '.join(VALID_BODY_MAC_PASSWORD_DELIMITER)}",
            )
    if "mac-calling-station-delimiter" in payload:
        value = payload["mac-calling-station-delimiter"]
        if value not in VALID_BODY_MAC_CALLING_STATION_DELIMITER:
            return (
                False,
                f"Invalid value for 'mac-calling-station-delimiter'='{value}'. Must be one of: {', '.join(VALID_BODY_MAC_CALLING_STATION_DELIMITER)}",
            )
    if "mac-called-station-delimiter" in payload:
        value = payload["mac-called-station-delimiter"]
        if value not in VALID_BODY_MAC_CALLED_STATION_DELIMITER:
            return (
                False,
                f"Invalid value for 'mac-called-station-delimiter'='{value}'. Must be one of: {', '.join(VALID_BODY_MAC_CALLED_STATION_DELIMITER)}",
            )
    if "mac-case" in payload:
        value = payload["mac-case"]
        if value not in VALID_BODY_MAC_CASE:
            return (
                False,
                f"Invalid value for 'mac-case'='{value}'. Must be one of: {', '.join(VALID_BODY_MAC_CASE)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_switch_controller_802_1X_settings_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update switch_controller/802_1X_settings.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_switch_controller_802_1X_settings_put(payload)
    """
    # Step 1: Validate enum values
    if "link-down-auth" in payload:
        value = payload["link-down-auth"]
        if value not in VALID_BODY_LINK_DOWN_AUTH:
            return (
                False,
                f"Invalid value for 'link-down-auth'='{value}'. Must be one of: {', '.join(VALID_BODY_LINK_DOWN_AUTH)}",
            )
    if "mab-reauth" in payload:
        value = payload["mab-reauth"]
        if value not in VALID_BODY_MAB_REAUTH:
            return (
                False,
                f"Invalid value for 'mab-reauth'='{value}'. Must be one of: {', '.join(VALID_BODY_MAB_REAUTH)}",
            )
    if "mac-username-delimiter" in payload:
        value = payload["mac-username-delimiter"]
        if value not in VALID_BODY_MAC_USERNAME_DELIMITER:
            return (
                False,
                f"Invalid value for 'mac-username-delimiter'='{value}'. Must be one of: {', '.join(VALID_BODY_MAC_USERNAME_DELIMITER)}",
            )
    if "mac-password-delimiter" in payload:
        value = payload["mac-password-delimiter"]
        if value not in VALID_BODY_MAC_PASSWORD_DELIMITER:
            return (
                False,
                f"Invalid value for 'mac-password-delimiter'='{value}'. Must be one of: {', '.join(VALID_BODY_MAC_PASSWORD_DELIMITER)}",
            )
    if "mac-calling-station-delimiter" in payload:
        value = payload["mac-calling-station-delimiter"]
        if value not in VALID_BODY_MAC_CALLING_STATION_DELIMITER:
            return (
                False,
                f"Invalid value for 'mac-calling-station-delimiter'='{value}'. Must be one of: {', '.join(VALID_BODY_MAC_CALLING_STATION_DELIMITER)}",
            )
    if "mac-called-station-delimiter" in payload:
        value = payload["mac-called-station-delimiter"]
        if value not in VALID_BODY_MAC_CALLED_STATION_DELIMITER:
            return (
                False,
                f"Invalid value for 'mac-called-station-delimiter'='{value}'. Must be one of: {', '.join(VALID_BODY_MAC_CALLED_STATION_DELIMITER)}",
            )
    if "mac-case" in payload:
        value = payload["mac-case"]
        if value not in VALID_BODY_MAC_CASE:
            return (
                False,
                f"Invalid value for 'mac-case'='{value}'. Must be one of: {', '.join(VALID_BODY_MAC_CASE)}",
            )

    return (True, None)


# ============================================================================
# Field Help Documentation
# ============================================================================

HELP_TEXT = {
}


def get_field_help(field_name: str) -> str | None:
    """
    Get help text for a specific field.

    Args:
        field_name: Name of the field

    Returns:
        Help text or None if field doesn't exist
    """
    return HELP_TEXT.get(field_name)