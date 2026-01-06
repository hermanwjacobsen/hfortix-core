"""Validation helpers for firewall/interface_policy6 - Auto-generated"""

from typing import Any, TypedDict, NotRequired, Literal

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

# ⚠️  IMPORTANT: FortiOS schemas have known issues with required field marking:

# Do NOT use this list for strict validation - test with the actual FortiOS API!

# Fields marked as required (after filtering false positives)
REQUIRED_FIELDS = [
    "interface",  # Monitored interface name from available interfaces.
    "srcaddr6",  # IPv6 address object to limit traffic monitoring to network traffic sent from the specified address or range.
    "dstaddr6",  # IPv6 address object to limit traffic monitoring to network traffic sent to the specified address or range.
    "application-list",  # Application list name.
    "ips-sensor",  # IPS sensor name.
    "av-profile",  # Antivirus profile.
    "webfilter-profile",  # Web filter profile.
    "casb-profile",  # CASB profile.
    "emailfilter-profile",  # Email filter profile.
    "dlp-profile",  # DLP profile name.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "policyid": 0,
    "uuid": "00000000-0000-0000-0000-000000000000",
    "status": "enable",
    "logtraffic": "utm",
    "interface": "",
    "application-list-status": "disable",
    "application-list": "",
    "ips-sensor-status": "disable",
    "ips-sensor": "",
    "dsri": "disable",
    "av-profile-status": "disable",
    "av-profile": "",
    "webfilter-profile-status": "disable",
    "webfilter-profile": "",
    "casb-profile-status": "disable",
    "casb-profile": "",
    "emailfilter-profile-status": "disable",
    "emailfilter-profile": "",
    "dlp-profile-status": "disable",
    "dlp-profile": "",
}

# ============================================================================
# Deprecated Fields
# Auto-generated from schema - warns users about deprecated fields
# ============================================================================

# Deprecated fields with migration guidance
DEPRECATED_FIELDS = {
}

# ============================================================================
# Field Metadata (Type Information & Descriptions)
# Auto-generated from schema - use for IDE autocomplete and documentation
# ============================================================================

# Field types mapping
FIELD_TYPES = {
    "policyid": "integer",  # Policy ID (0 - 4294967295).
    "uuid": "uuid",  # Universally Unique Identifier (UUID; automatically assigned 
    "status": "option",  # Enable/disable this policy.
    "comments": "var-string",  # Comments.
    "logtraffic": "option",  # Logging type to be used in this policy (Options: all | utm |
    "interface": "string",  # Monitored interface name from available interfaces.
    "srcaddr6": "string",  # IPv6 address object to limit traffic monitoring to network t
    "dstaddr6": "string",  # IPv6 address object to limit traffic monitoring to network t
    "service6": "string",  # Service name.
    "application-list-status": "option",  # Enable/disable application control.
    "application-list": "string",  # Application list name.
    "ips-sensor-status": "option",  # Enable/disable IPS.
    "ips-sensor": "string",  # IPS sensor name.
    "dsri": "option",  # Enable/disable DSRI.
    "av-profile-status": "option",  # Enable/disable antivirus.
    "av-profile": "string",  # Antivirus profile.
    "webfilter-profile-status": "option",  # Enable/disable web filtering.
    "webfilter-profile": "string",  # Web filter profile.
    "casb-profile-status": "option",  # Enable/disable CASB.
    "casb-profile": "string",  # CASB profile.
    "emailfilter-profile-status": "option",  # Enable/disable email filter.
    "emailfilter-profile": "string",  # Email filter profile.
    "dlp-profile-status": "option",  # Enable/disable DLP.
    "dlp-profile": "string",  # DLP profile name.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "policyid": "Policy ID (0 - 4294967295).",
    "uuid": "Universally Unique Identifier (UUID; automatically assigned but can be manually reset).",
    "status": "Enable/disable this policy.",
    "comments": "Comments.",
    "logtraffic": "Logging type to be used in this policy (Options: all | utm | disable, Default: utm).",
    "interface": "Monitored interface name from available interfaces.",
    "srcaddr6": "IPv6 address object to limit traffic monitoring to network traffic sent from the specified address or range.",
    "dstaddr6": "IPv6 address object to limit traffic monitoring to network traffic sent to the specified address or range.",
    "service6": "Service name.",
    "application-list-status": "Enable/disable application control.",
    "application-list": "Application list name.",
    "ips-sensor-status": "Enable/disable IPS.",
    "ips-sensor": "IPS sensor name.",
    "dsri": "Enable/disable DSRI.",
    "av-profile-status": "Enable/disable antivirus.",
    "av-profile": "Antivirus profile.",
    "webfilter-profile-status": "Enable/disable web filtering.",
    "webfilter-profile": "Web filter profile.",
    "casb-profile-status": "Enable/disable CASB.",
    "casb-profile": "CASB profile.",
    "emailfilter-profile-status": "Enable/disable email filter.",
    "emailfilter-profile": "Email filter profile.",
    "dlp-profile-status": "Enable/disable DLP.",
    "dlp-profile": "DLP profile name.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "policyid": {"type": "integer", "min": 0, "max": 4294967295},
    "interface": {"type": "string", "max_length": 35},
    "application-list": {"type": "string", "max_length": 47},
    "ips-sensor": {"type": "string", "max_length": 47},
    "av-profile": {"type": "string", "max_length": 47},
    "webfilter-profile": {"type": "string", "max_length": 47},
    "casb-profile": {"type": "string", "max_length": 47},
    "emailfilter-profile": {"type": "string", "max_length": 47},
    "dlp-profile": {"type": "string", "max_length": 47},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "srcaddr6": {
        "name": {
            "type": "string",
            "help": "Address name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "dstaddr6": {
        "name": {
            "type": "string",
            "help": "Address name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "service6": {
        "name": {
            "type": "string",
            "help": "Service name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_STATUS = [
    "enable",  # Enable this policy.
    "disable",  # Disable this policy.
]
VALID_BODY_LOGTRAFFIC = [
    "all",  # Log all sessions accepted or denied by this policy.
    "utm",  # Log traffic that has a security profile applied to it.
    "disable",  # Disable all logging for this policy.
]
VALID_BODY_APPLICATION_LIST_STATUS = [
    "enable",  # Enable application control
    "disable",  # Disable application control
]
VALID_BODY_IPS_SENSOR_STATUS = [
    "enable",  # Enable IPS.
    "disable",  # Disable IPS.
]
VALID_BODY_DSRI = [
    "enable",  # Enable DSRI.
    "disable",  # Disable DSRI.
]
VALID_BODY_AV_PROFILE_STATUS = [
    "enable",  # Enable antivirus
    "disable",  # Disable antivirus
]
VALID_BODY_WEBFILTER_PROFILE_STATUS = [
    "enable",  # Enable web filtering.
    "disable",  # Disable web filtering.
]
VALID_BODY_CASB_PROFILE_STATUS = [
    "enable",  # Enable CASB.
    "disable",  # Disable CASB.
]
VALID_BODY_EMAILFILTER_PROFILE_STATUS = [
    "enable",  # Enable Email filter.
    "disable",  # Disable Email filter.
]
VALID_BODY_DLP_PROFILE_STATUS = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_firewall_interface_policy6_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for firewall/interface_policy6."""
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
    """Validate required fields for firewall/interface_policy6."""
    # Check always-required fields
    missing_fields = []
    for field in REQUIRED_FIELDS:
        if field not in payload:
            missing_fields.append(field)
    
    if missing_fields:
        # Build enhanced error message
        error_parts = [f"Missing required field(s): {', '.join(missing_fields)}"]
        
        # Add descriptions for first few missing fields
        for field in missing_fields[:3]:
            desc = FIELD_DESCRIPTIONS.get(field)
            if desc:
                error_parts.append(f"  • {field}: {desc}")
        
        if len(missing_fields) > 3:
            error_parts.append(f"  ... and {len(missing_fields) - 3} more")
        
        return (False, "\n".join(error_parts))

    return (True, None)


def validate_firewall_interface_policy6_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new firewall/interface_policy6 object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "status" in payload:
        value = payload["status"]
        if value not in VALID_BODY_STATUS:
            desc = FIELD_DESCRIPTIONS.get("status", "")
            error_msg = f"Invalid value for 'status': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_STATUS)}"
            error_msg += f"\n  → Example: status='{{ VALID_BODY_STATUS[0] }}'"
            return (False, error_msg)
    if "logtraffic" in payload:
        value = payload["logtraffic"]
        if value not in VALID_BODY_LOGTRAFFIC:
            desc = FIELD_DESCRIPTIONS.get("logtraffic", "")
            error_msg = f"Invalid value for 'logtraffic': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LOGTRAFFIC)}"
            error_msg += f"\n  → Example: logtraffic='{{ VALID_BODY_LOGTRAFFIC[0] }}'"
            return (False, error_msg)
    if "application-list-status" in payload:
        value = payload["application-list-status"]
        if value not in VALID_BODY_APPLICATION_LIST_STATUS:
            desc = FIELD_DESCRIPTIONS.get("application-list-status", "")
            error_msg = f"Invalid value for 'application-list-status': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_APPLICATION_LIST_STATUS)}"
            error_msg += f"\n  → Example: application-list-status='{{ VALID_BODY_APPLICATION_LIST_STATUS[0] }}'"
            return (False, error_msg)
    if "ips-sensor-status" in payload:
        value = payload["ips-sensor-status"]
        if value not in VALID_BODY_IPS_SENSOR_STATUS:
            desc = FIELD_DESCRIPTIONS.get("ips-sensor-status", "")
            error_msg = f"Invalid value for 'ips-sensor-status': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_IPS_SENSOR_STATUS)}"
            error_msg += f"\n  → Example: ips-sensor-status='{{ VALID_BODY_IPS_SENSOR_STATUS[0] }}'"
            return (False, error_msg)
    if "dsri" in payload:
        value = payload["dsri"]
        if value not in VALID_BODY_DSRI:
            desc = FIELD_DESCRIPTIONS.get("dsri", "")
            error_msg = f"Invalid value for 'dsri': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DSRI)}"
            error_msg += f"\n  → Example: dsri='{{ VALID_BODY_DSRI[0] }}'"
            return (False, error_msg)
    if "av-profile-status" in payload:
        value = payload["av-profile-status"]
        if value not in VALID_BODY_AV_PROFILE_STATUS:
            desc = FIELD_DESCRIPTIONS.get("av-profile-status", "")
            error_msg = f"Invalid value for 'av-profile-status': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AV_PROFILE_STATUS)}"
            error_msg += f"\n  → Example: av-profile-status='{{ VALID_BODY_AV_PROFILE_STATUS[0] }}'"
            return (False, error_msg)
    if "webfilter-profile-status" in payload:
        value = payload["webfilter-profile-status"]
        if value not in VALID_BODY_WEBFILTER_PROFILE_STATUS:
            desc = FIELD_DESCRIPTIONS.get("webfilter-profile-status", "")
            error_msg = f"Invalid value for 'webfilter-profile-status': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WEBFILTER_PROFILE_STATUS)}"
            error_msg += f"\n  → Example: webfilter-profile-status='{{ VALID_BODY_WEBFILTER_PROFILE_STATUS[0] }}'"
            return (False, error_msg)
    if "casb-profile-status" in payload:
        value = payload["casb-profile-status"]
        if value not in VALID_BODY_CASB_PROFILE_STATUS:
            desc = FIELD_DESCRIPTIONS.get("casb-profile-status", "")
            error_msg = f"Invalid value for 'casb-profile-status': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CASB_PROFILE_STATUS)}"
            error_msg += f"\n  → Example: casb-profile-status='{{ VALID_BODY_CASB_PROFILE_STATUS[0] }}'"
            return (False, error_msg)
    if "emailfilter-profile-status" in payload:
        value = payload["emailfilter-profile-status"]
        if value not in VALID_BODY_EMAILFILTER_PROFILE_STATUS:
            desc = FIELD_DESCRIPTIONS.get("emailfilter-profile-status", "")
            error_msg = f"Invalid value for 'emailfilter-profile-status': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_EMAILFILTER_PROFILE_STATUS)}"
            error_msg += f"\n  → Example: emailfilter-profile-status='{{ VALID_BODY_EMAILFILTER_PROFILE_STATUS[0] }}'"
            return (False, error_msg)
    if "dlp-profile-status" in payload:
        value = payload["dlp-profile-status"]
        if value not in VALID_BODY_DLP_PROFILE_STATUS:
            desc = FIELD_DESCRIPTIONS.get("dlp-profile-status", "")
            error_msg = f"Invalid value for 'dlp-profile-status': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DLP_PROFILE_STATUS)}"
            error_msg += f"\n  → Example: dlp-profile-status='{{ VALID_BODY_DLP_PROFILE_STATUS[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_firewall_interface_policy6_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update firewall/interface_policy6."""
    # Step 1: Validate enum values
    if "status" in payload:
        value = payload["status"]
        if value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid value for 'status'='{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )
    if "logtraffic" in payload:
        value = payload["logtraffic"]
        if value not in VALID_BODY_LOGTRAFFIC:
            return (
                False,
                f"Invalid value for 'logtraffic'='{value}'. Must be one of: {', '.join(VALID_BODY_LOGTRAFFIC)}",
            )
    if "application-list-status" in payload:
        value = payload["application-list-status"]
        if value not in VALID_BODY_APPLICATION_LIST_STATUS:
            return (
                False,
                f"Invalid value for 'application-list-status'='{value}'. Must be one of: {', '.join(VALID_BODY_APPLICATION_LIST_STATUS)}",
            )
    if "ips-sensor-status" in payload:
        value = payload["ips-sensor-status"]
        if value not in VALID_BODY_IPS_SENSOR_STATUS:
            return (
                False,
                f"Invalid value for 'ips-sensor-status'='{value}'. Must be one of: {', '.join(VALID_BODY_IPS_SENSOR_STATUS)}",
            )
    if "dsri" in payload:
        value = payload["dsri"]
        if value not in VALID_BODY_DSRI:
            return (
                False,
                f"Invalid value for 'dsri'='{value}'. Must be one of: {', '.join(VALID_BODY_DSRI)}",
            )
    if "av-profile-status" in payload:
        value = payload["av-profile-status"]
        if value not in VALID_BODY_AV_PROFILE_STATUS:
            return (
                False,
                f"Invalid value for 'av-profile-status'='{value}'. Must be one of: {', '.join(VALID_BODY_AV_PROFILE_STATUS)}",
            )
    if "webfilter-profile-status" in payload:
        value = payload["webfilter-profile-status"]
        if value not in VALID_BODY_WEBFILTER_PROFILE_STATUS:
            return (
                False,
                f"Invalid value for 'webfilter-profile-status'='{value}'. Must be one of: {', '.join(VALID_BODY_WEBFILTER_PROFILE_STATUS)}",
            )
    if "casb-profile-status" in payload:
        value = payload["casb-profile-status"]
        if value not in VALID_BODY_CASB_PROFILE_STATUS:
            return (
                False,
                f"Invalid value for 'casb-profile-status'='{value}'. Must be one of: {', '.join(VALID_BODY_CASB_PROFILE_STATUS)}",
            )
    if "emailfilter-profile-status" in payload:
        value = payload["emailfilter-profile-status"]
        if value not in VALID_BODY_EMAILFILTER_PROFILE_STATUS:
            return (
                False,
                f"Invalid value for 'emailfilter-profile-status'='{value}'. Must be one of: {', '.join(VALID_BODY_EMAILFILTER_PROFILE_STATUS)}",
            )
    if "dlp-profile-status" in payload:
        value = payload["dlp-profile-status"]
        if value not in VALID_BODY_DLP_PROFILE_STATUS:
            return (
                False,
                f"Invalid value for 'dlp-profile-status'='{value}'. Must be one of: {', '.join(VALID_BODY_DLP_PROFILE_STATUS)}",
            )

    return (True, None)


# ============================================================================
# Metadata Access Functions
# Imported from central module to avoid duplication across 1,062 files
# ============================================================================

from hfortix_fortios._helpers.metadata import (
    get_field_description as _get_field_description,
    get_field_type as _get_field_type,
    get_field_constraints as _get_field_constraints,
    get_field_default as _get_field_default,
    get_field_options as _get_field_options,
    get_nested_schema as _get_nested_schema,
    get_all_fields as _get_all_fields,
    get_field_metadata as _get_field_metadata,
    validate_field_value as _validate_field_value,
)

# Wrapper functions that bind module-specific data to central functions
def get_field_description(field_name: str) -> str | None:
    """Get description/help text for a field."""
    return _get_field_description(FIELD_DESCRIPTIONS, field_name)

def get_field_type(field_name: str) -> str | None:
    """Get the type of a field."""
    return _get_field_type(FIELD_TYPES, field_name)

def get_field_constraints(field_name: str) -> dict[str, Any] | None:
    """Get constraints for a field (min/max values, string length)."""
    return _get_field_constraints(FIELD_CONSTRAINTS, field_name)

def get_field_default(field_name: str) -> Any | None:
    """Get default value for a field."""
    return _get_field_default(FIELDS_WITH_DEFAULTS, field_name)

def get_field_options(field_name: str) -> list[str] | None:
    """Get valid enum options for a field."""
    return _get_field_options(globals(), field_name)

def get_nested_schema(field_name: str) -> dict[str, Any] | None:
    """Get schema for nested table/list fields."""
    return _get_nested_schema(NESTED_SCHEMAS, field_name)

def get_all_fields() -> list[str]:
    """Get list of all field names."""
    return _get_all_fields(FIELD_TYPES)

def get_field_metadata(field_name: str) -> dict[str, Any] | None:
    """Get complete metadata for a field (type, description, constraints, defaults, options)."""
    return _get_field_metadata(
        FIELD_TYPES, FIELD_DESCRIPTIONS, FIELD_CONSTRAINTS,
        FIELDS_WITH_DEFAULTS, REQUIRED_FIELDS, NESTED_SCHEMAS,
        globals(), field_name
    )

def validate_field_value(field_name: str, value: Any) -> tuple[bool, str | None]:
    """Validate a single field value against its constraints."""
    return _validate_field_value(
        FIELD_TYPES, FIELD_DESCRIPTIONS, FIELD_CONSTRAINTS,
        globals(), field_name, value
    )


# ============================================================================
# Schema Information
# Metadata about this endpoint schema
# ============================================================================

SCHEMA_INFO = {
    "endpoint": "firewall/interface_policy6",
    "category": "cmdb",
    "api_path": "firewall/interface-policy6",
    "mkey": "policyid",
    "mkey_type": "integer",
    "help": "Configure IPv6 interface policies.",
    "total_fields": 24,
    "required_fields_count": 10,
    "fields_with_defaults_count": 20,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
