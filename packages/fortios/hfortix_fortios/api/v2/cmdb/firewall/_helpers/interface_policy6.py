"""
Validation helpers for firewall interface_policy6 endpoint.

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
    "application-list",  # Application list name.
    "av-profile",  # Antivirus profile.
    "dstaddr6",  # IPv6 address object to limit traffic monitoring to network t
    "interface",  # Monitored interface name from available interfaces.
    "ips-sensor",  # IPS sensor name.
    "srcaddr6",  # IPv6 address object to limit traffic monitoring to network t
]

# Mutually exclusive groups (at least ONE from each group required)
MUTUALLY_EXCLUSIVE_GROUPS = {
    "dest_address": ["dstaddr6"],
    "source_address": ["srcaddr6"],
}

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "application-list-status": "disable",
    "av-profile-status": "disable",
    "casb-profile-status": "disable",
    "dlp-profile-status": "disable",
    "dsri": "disable",
    "emailfilter-profile-status": "disable",
    "ips-sensor-status": "disable",
    "logtraffic": "utm",
    "status": "enable",
    "uuid": "00000000-0000-0000-0000-000000000000",
    "webfilter-profile-status": "disable",
}

# Fields wrongly marked as required in schema (schema bugs)
# These are specialized features and should be OPTIONAL
SCHEMA_FALSE_POSITIVES = [
    "casb-profile",  # CASB profile.
    "dlp-profile",  # DLP profile name.
    "emailfilter-profile",  # Email filter profile.
    "webfilter-profile",  # Web filter profile.
]


# Valid enum values from API documentation
VALID_BODY_STATUS = ["enable", "disable"]
VALID_BODY_LOGTRAFFIC = ["all", "utm", "disable"]
VALID_BODY_APPLICATION_LIST_STATUS = ["enable", "disable"]
VALID_BODY_IPS_SENSOR_STATUS = ["enable", "disable"]
VALID_BODY_DSRI = ["enable", "disable"]
VALID_BODY_AV_PROFILE_STATUS = ["enable", "disable"]
VALID_BODY_WEBFILTER_PROFILE_STATUS = ["enable", "disable"]
VALID_BODY_CASB_PROFILE_STATUS = ["enable", "disable"]
VALID_BODY_EMAILFILTER_PROFILE_STATUS = ["enable", "disable"]
VALID_BODY_DLP_PROFILE_STATUS = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_interface_policy6_get(
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
    Validate required fields for firewall_interface-policy6.

    This validator checks:
    1. Always-required fields are present
    2. Mutually exclusive groups have at least one field

    Args:
        payload: The request payload to validate

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> is_valid, error = validate_required_fields({
        ...     "application-list": "value",
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

    # Check mutually exclusive groups
    if not ("dstaddr6" in payload):
        return (False, "Must provide at least one of: dstaddr6")
    if not ("srcaddr6" in payload):
        return (False, "Must provide at least one of: srcaddr6")

    return (True, None)


# ============================================================================
# Endpoint Validation (Enhanced with Required Fields)
# ============================================================================


def validate_interface_policy6_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload.

    This validator performs two-stage validation:
    1. Required fields validation (schema-based)
    2. Field value validation (enums, ranges, formats)

    Required fields:
      - application-list: Application list name.
      - av-profile: Antivirus profile.
      - dstaddr6: IPv6 address object to limit traffic monitoring to network t
      - interface: Monitored interface name from available interfaces.
      - ips-sensor: IPS sensor name.
      - srcaddr6: IPv6 address object to limit traffic monitoring to network t

    Mutually exclusive (at least ONE required):
      - dstaddr6
      - srcaddr6

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
    # Validate policyid if present
    if "policyid" in payload:
        value = payload.get("policyid")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "policyid must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"policyid must be numeric, got: {value}")

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )

    # Validate comments if present
    if "comments" in payload:
        value = payload.get("comments")
        if value and isinstance(value, str) and len(value) > 1023:
            return (False, "comments cannot exceed 1023 characters")

    # Validate logtraffic if present
    if "logtraffic" in payload:
        value = payload.get("logtraffic")
        if value and value not in VALID_BODY_LOGTRAFFIC:
            return (
                False,
                f"Invalid logtraffic '{value}'. Must be one of: {', '.join(VALID_BODY_LOGTRAFFIC)}",
            )

    # Validate interface if present
    if "interface" in payload:
        value = payload.get("interface")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "interface cannot exceed 35 characters")

    # Validate application-list-status if present
    if "application-list-status" in payload:
        value = payload.get("application-list-status")
        if value and value not in VALID_BODY_APPLICATION_LIST_STATUS:
            return (
                False,
                f"Invalid application-list-status '{value}'. Must be one of: {', '.join(VALID_BODY_APPLICATION_LIST_STATUS)}",
            )

    # Validate application-list if present
    if "application-list" in payload:
        value = payload.get("application-list")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "application-list cannot exceed 47 characters")

    # Validate ips-sensor-status if present
    if "ips-sensor-status" in payload:
        value = payload.get("ips-sensor-status")
        if value and value not in VALID_BODY_IPS_SENSOR_STATUS:
            return (
                False,
                f"Invalid ips-sensor-status '{value}'. Must be one of: {', '.join(VALID_BODY_IPS_SENSOR_STATUS)}",
            )

    # Validate ips-sensor if present
    if "ips-sensor" in payload:
        value = payload.get("ips-sensor")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "ips-sensor cannot exceed 47 characters")

    # Validate dsri if present
    if "dsri" in payload:
        value = payload.get("dsri")
        if value and value not in VALID_BODY_DSRI:
            return (
                False,
                f"Invalid dsri '{value}'. Must be one of: {', '.join(VALID_BODY_DSRI)}",
            )

    # Validate av-profile-status if present
    if "av-profile-status" in payload:
        value = payload.get("av-profile-status")
        if value and value not in VALID_BODY_AV_PROFILE_STATUS:
            return (
                False,
                f"Invalid av-profile-status '{value}'. Must be one of: {', '.join(VALID_BODY_AV_PROFILE_STATUS)}",
            )

    # Validate av-profile if present
    if "av-profile" in payload:
        value = payload.get("av-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "av-profile cannot exceed 47 characters")

    # Validate webfilter-profile-status if present
    if "webfilter-profile-status" in payload:
        value = payload.get("webfilter-profile-status")
        if value and value not in VALID_BODY_WEBFILTER_PROFILE_STATUS:
            return (
                False,
                f"Invalid webfilter-profile-status '{value}'. Must be one of: {', '.join(VALID_BODY_WEBFILTER_PROFILE_STATUS)}",
            )

    # Validate webfilter-profile if present
    if "webfilter-profile" in payload:
        value = payload.get("webfilter-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "webfilter-profile cannot exceed 47 characters")

    # Validate casb-profile-status if present
    if "casb-profile-status" in payload:
        value = payload.get("casb-profile-status")
        if value and value not in VALID_BODY_CASB_PROFILE_STATUS:
            return (
                False,
                f"Invalid casb-profile-status '{value}'. Must be one of: {', '.join(VALID_BODY_CASB_PROFILE_STATUS)}",
            )

    # Validate casb-profile if present
    if "casb-profile" in payload:
        value = payload.get("casb-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "casb-profile cannot exceed 47 characters")

    # Validate emailfilter-profile-status if present
    if "emailfilter-profile-status" in payload:
        value = payload.get("emailfilter-profile-status")
        if value and value not in VALID_BODY_EMAILFILTER_PROFILE_STATUS:
            return (
                False,
                f"Invalid emailfilter-profile-status '{value}'. Must be one of: {', '.join(VALID_BODY_EMAILFILTER_PROFILE_STATUS)}",
            )

    # Validate emailfilter-profile if present
    if "emailfilter-profile" in payload:
        value = payload.get("emailfilter-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "emailfilter-profile cannot exceed 47 characters")

    # Validate dlp-profile-status if present
    if "dlp-profile-status" in payload:
        value = payload.get("dlp-profile-status")
        if value and value not in VALID_BODY_DLP_PROFILE_STATUS:
            return (
                False,
                f"Invalid dlp-profile-status '{value}'. Must be one of: {', '.join(VALID_BODY_DLP_PROFILE_STATUS)}",
            )

    # Validate dlp-profile if present
    if "dlp-profile" in payload:
        value = payload.get("dlp-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "dlp-profile cannot exceed 47 characters")

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_interface_policy6_put(
    policyid: str | None = None, payload: dict[str, Any] | None = None
) -> tuple[bool, str | None]:
    """
    Validate PUT request payload for updating {endpoint_name}.

    Args:
        policyid: Object identifier (required)
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # policyid is required for updates
    if not policyid:
        return (False, "policyid is required for PUT operation")

    # If no payload provided, nothing to validate
    if not payload:
        return (True, None)

    # Validate policyid if present
    if "policyid" in payload:
        value = payload.get("policyid")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "policyid must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"policyid must be numeric, got: {value}")

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )

    # Validate comments if present
    if "comments" in payload:
        value = payload.get("comments")
        if value and isinstance(value, str) and len(value) > 1023:
            return (False, "comments cannot exceed 1023 characters")

    # Validate logtraffic if present
    if "logtraffic" in payload:
        value = payload.get("logtraffic")
        if value and value not in VALID_BODY_LOGTRAFFIC:
            return (
                False,
                f"Invalid logtraffic '{value}'. Must be one of: {', '.join(VALID_BODY_LOGTRAFFIC)}",
            )

    # Validate interface if present
    if "interface" in payload:
        value = payload.get("interface")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "interface cannot exceed 35 characters")

    # Validate application-list-status if present
    if "application-list-status" in payload:
        value = payload.get("application-list-status")
        if value and value not in VALID_BODY_APPLICATION_LIST_STATUS:
            return (
                False,
                f"Invalid application-list-status '{value}'. Must be one of: {', '.join(VALID_BODY_APPLICATION_LIST_STATUS)}",
            )

    # Validate application-list if present
    if "application-list" in payload:
        value = payload.get("application-list")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "application-list cannot exceed 47 characters")

    # Validate ips-sensor-status if present
    if "ips-sensor-status" in payload:
        value = payload.get("ips-sensor-status")
        if value and value not in VALID_BODY_IPS_SENSOR_STATUS:
            return (
                False,
                f"Invalid ips-sensor-status '{value}'. Must be one of: {', '.join(VALID_BODY_IPS_SENSOR_STATUS)}",
            )

    # Validate ips-sensor if present
    if "ips-sensor" in payload:
        value = payload.get("ips-sensor")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "ips-sensor cannot exceed 47 characters")

    # Validate dsri if present
    if "dsri" in payload:
        value = payload.get("dsri")
        if value and value not in VALID_BODY_DSRI:
            return (
                False,
                f"Invalid dsri '{value}'. Must be one of: {', '.join(VALID_BODY_DSRI)}",
            )

    # Validate av-profile-status if present
    if "av-profile-status" in payload:
        value = payload.get("av-profile-status")
        if value and value not in VALID_BODY_AV_PROFILE_STATUS:
            return (
                False,
                f"Invalid av-profile-status '{value}'. Must be one of: {', '.join(VALID_BODY_AV_PROFILE_STATUS)}",
            )

    # Validate av-profile if present
    if "av-profile" in payload:
        value = payload.get("av-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "av-profile cannot exceed 47 characters")

    # Validate webfilter-profile-status if present
    if "webfilter-profile-status" in payload:
        value = payload.get("webfilter-profile-status")
        if value and value not in VALID_BODY_WEBFILTER_PROFILE_STATUS:
            return (
                False,
                f"Invalid webfilter-profile-status '{value}'. Must be one of: {', '.join(VALID_BODY_WEBFILTER_PROFILE_STATUS)}",
            )

    # Validate webfilter-profile if present
    if "webfilter-profile" in payload:
        value = payload.get("webfilter-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "webfilter-profile cannot exceed 47 characters")

    # Validate casb-profile-status if present
    if "casb-profile-status" in payload:
        value = payload.get("casb-profile-status")
        if value and value not in VALID_BODY_CASB_PROFILE_STATUS:
            return (
                False,
                f"Invalid casb-profile-status '{value}'. Must be one of: {', '.join(VALID_BODY_CASB_PROFILE_STATUS)}",
            )

    # Validate casb-profile if present
    if "casb-profile" in payload:
        value = payload.get("casb-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "casb-profile cannot exceed 47 characters")

    # Validate emailfilter-profile-status if present
    if "emailfilter-profile-status" in payload:
        value = payload.get("emailfilter-profile-status")
        if value and value not in VALID_BODY_EMAILFILTER_PROFILE_STATUS:
            return (
                False,
                f"Invalid emailfilter-profile-status '{value}'. Must be one of: {', '.join(VALID_BODY_EMAILFILTER_PROFILE_STATUS)}",
            )

    # Validate emailfilter-profile if present
    if "emailfilter-profile" in payload:
        value = payload.get("emailfilter-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "emailfilter-profile cannot exceed 47 characters")

    # Validate dlp-profile-status if present
    if "dlp-profile-status" in payload:
        value = payload.get("dlp-profile-status")
        if value and value not in VALID_BODY_DLP_PROFILE_STATUS:
            return (
                False,
                f"Invalid dlp-profile-status '{value}'. Must be one of: {', '.join(VALID_BODY_DLP_PROFILE_STATUS)}",
            )

    # Validate dlp-profile if present
    if "dlp-profile" in payload:
        value = payload.get("dlp-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "dlp-profile cannot exceed 47 characters")

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_interface_policy6_delete(
    policyid: str | None = None,
) -> tuple[bool, str | None]:
    """
    Validate DELETE request parameters.

    Args:
        policyid: Object identifier (required)

    Returns:
        Tuple of (is_valid, error_message)
    """
    if not policyid:
        return (False, "policyid is required for DELETE operation")

    return (True, None)
