"""Validation helpers for log/eventfilter - Auto-generated"""

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
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "event": "enable",
    "system": "enable",
    "vpn": "enable",
    "user": "enable",
    "router": "enable",
    "wireless-activity": "enable",
    "wan-opt": "enable",
    "endpoint": "enable",
    "ha": "enable",
    "security-rating": "enable",
    "fortiextender": "enable",
    "connector": "enable",
    "sdwan": "enable",
    "cifs": "enable",
    "switch-controller": "enable",
    "rest-api": "enable",
    "web-svc": "enable",
    "webproxy": "enable",
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
    "event": "option",  # Enable/disable event logging.
    "system": "option",  # Enable/disable system event logging.
    "vpn": "option",  # Enable/disable VPN event logging.
    "user": "option",  # Enable/disable user authentication event logging.
    "router": "option",  # Enable/disable router event logging.
    "wireless-activity": "option",  # Enable/disable wireless event logging.
    "wan-opt": "option",  # Enable/disable WAN optimization event logging.
    "endpoint": "option",  # Enable/disable endpoint event logging.
    "ha": "option",  # Enable/disable ha event logging.
    "security-rating": "option",  # Enable/disable Security Rating result logging.
    "fortiextender": "option",  # Enable/disable FortiExtender logging.
    "connector": "option",  # Enable/disable SDN connector logging.
    "sdwan": "option",  # Enable/disable SD-WAN logging.
    "cifs": "option",  # Enable/disable CIFS logging.
    "switch-controller": "option",  # Enable/disable Switch-Controller logging.
    "rest-api": "option",  # Enable/disable REST API logging.
    "web-svc": "option",  # Enable/disable web-svc performance logging.
    "webproxy": "option",  # Enable/disable web proxy event logging.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "event": "Enable/disable event logging.",
    "system": "Enable/disable system event logging.",
    "vpn": "Enable/disable VPN event logging.",
    "user": "Enable/disable user authentication event logging.",
    "router": "Enable/disable router event logging.",
    "wireless-activity": "Enable/disable wireless event logging.",
    "wan-opt": "Enable/disable WAN optimization event logging.",
    "endpoint": "Enable/disable endpoint event logging.",
    "ha": "Enable/disable ha event logging.",
    "security-rating": "Enable/disable Security Rating result logging.",
    "fortiextender": "Enable/disable FortiExtender logging.",
    "connector": "Enable/disable SDN connector logging.",
    "sdwan": "Enable/disable SD-WAN logging.",
    "cifs": "Enable/disable CIFS logging.",
    "switch-controller": "Enable/disable Switch-Controller logging.",
    "rest-api": "Enable/disable REST API logging.",
    "web-svc": "Enable/disable web-svc performance logging.",
    "webproxy": "Enable/disable web proxy event logging.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
}


# Valid enum values from API documentation
VALID_BODY_EVENT = [
    "enable",  # Enable event logging.
    "disable",  # Disable event logging.
]
VALID_BODY_SYSTEM = [
    "enable",  # Enable system event logging.
    "disable",  # Disable system event logging.
]
VALID_BODY_VPN = [
    "enable",  # Enable VPN event logging.
    "disable",  # Disable VPN event logging.
]
VALID_BODY_USER = [
    "enable",  # Enable user authentication event logging.
    "disable",  # Disable user authentication event logging.
]
VALID_BODY_ROUTER = [
    "enable",  # Enable router event logging.
    "disable",  # Disable router event logging.
]
VALID_BODY_WIRELESS_ACTIVITY = [
    "enable",  # Enable wireless event logging.
    "disable",  # Disable wireless event logging.
]
VALID_BODY_WAN_OPT = [
    "enable",  # Enable WAN optimization event logging.
    "disable",  # Disable WAN optimization event logging.
]
VALID_BODY_ENDPOINT = [
    "enable",  # Enable endpoint event logging.
    "disable",  # Disable endpoint event logging.
]
VALID_BODY_HA = [
    "enable",  # Enable ha event logging.
    "disable",  # Disable ha event logging.
]
VALID_BODY_SECURITY_RATING = [
    "enable",  # Enable Security Fabric audit result logging.
    "disable",  # Disable Security Fabric audit result logging.
]
VALID_BODY_FORTIEXTENDER = [
    "enable",  # Enable Forti-Extender logging.
    "disable",  # Disable Forti-Extender logging.
]
VALID_BODY_CONNECTOR = [
    "enable",  # Enable SDN connector logging.
    "disable",  # Disable SDN connector logging.
]
VALID_BODY_SDWAN = [
    "enable",  # Enable SD-WAN logging.
    "disable",  # Disable SD-WAN logging.
]
VALID_BODY_CIFS = [
    "enable",  # Enable CIFS logging.
    "disable",  # Disable CIFS logging.
]
VALID_BODY_SWITCH_CONTROLLER = [
    "enable",  # Enable Switch-Controller logging.
    "disable",  # Disable Switch-Controller logging.
]
VALID_BODY_REST_API = [
    "enable",  # Enable REST API logging.
    "disable",  # Disable REST API logging.
]
VALID_BODY_WEB_SVC = [
    "enable",  # Enable web-svc daemon logging.
    "disable",  # Disable web-svc daemon logging.
]
VALID_BODY_WEBPROXY = [
    "enable",  # Enable Web Proxy event logging.
    "disable",  # Disable Web Proxy event logging.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_log_eventfilter_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for log/eventfilter."""
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
    """Validate required fields for log/eventfilter."""
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


def validate_log_eventfilter_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new log/eventfilter object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "event" in payload:
        value = payload["event"]
        if value not in VALID_BODY_EVENT:
            desc = FIELD_DESCRIPTIONS.get("event", "")
            error_msg = f"Invalid value for 'event': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_EVENT)}"
            error_msg += f"\n  → Example: event='{{ VALID_BODY_EVENT[0] }}'"
            return (False, error_msg)
    if "system" in payload:
        value = payload["system"]
        if value not in VALID_BODY_SYSTEM:
            desc = FIELD_DESCRIPTIONS.get("system", "")
            error_msg = f"Invalid value for 'system': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SYSTEM)}"
            error_msg += f"\n  → Example: system='{{ VALID_BODY_SYSTEM[0] }}'"
            return (False, error_msg)
    if "vpn" in payload:
        value = payload["vpn"]
        if value not in VALID_BODY_VPN:
            desc = FIELD_DESCRIPTIONS.get("vpn", "")
            error_msg = f"Invalid value for 'vpn': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_VPN)}"
            error_msg += f"\n  → Example: vpn='{{ VALID_BODY_VPN[0] }}'"
            return (False, error_msg)
    if "user" in payload:
        value = payload["user"]
        if value not in VALID_BODY_USER:
            desc = FIELD_DESCRIPTIONS.get("user", "")
            error_msg = f"Invalid value for 'user': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_USER)}"
            error_msg += f"\n  → Example: user='{{ VALID_BODY_USER[0] }}'"
            return (False, error_msg)
    if "router" in payload:
        value = payload["router"]
        if value not in VALID_BODY_ROUTER:
            desc = FIELD_DESCRIPTIONS.get("router", "")
            error_msg = f"Invalid value for 'router': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ROUTER)}"
            error_msg += f"\n  → Example: router='{{ VALID_BODY_ROUTER[0] }}'"
            return (False, error_msg)
    if "wireless-activity" in payload:
        value = payload["wireless-activity"]
        if value not in VALID_BODY_WIRELESS_ACTIVITY:
            desc = FIELD_DESCRIPTIONS.get("wireless-activity", "")
            error_msg = f"Invalid value for 'wireless-activity': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WIRELESS_ACTIVITY)}"
            error_msg += f"\n  → Example: wireless-activity='{{ VALID_BODY_WIRELESS_ACTIVITY[0] }}'"
            return (False, error_msg)
    if "wan-opt" in payload:
        value = payload["wan-opt"]
        if value not in VALID_BODY_WAN_OPT:
            desc = FIELD_DESCRIPTIONS.get("wan-opt", "")
            error_msg = f"Invalid value for 'wan-opt': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WAN_OPT)}"
            error_msg += f"\n  → Example: wan-opt='{{ VALID_BODY_WAN_OPT[0] }}'"
            return (False, error_msg)
    if "endpoint" in payload:
        value = payload["endpoint"]
        if value not in VALID_BODY_ENDPOINT:
            desc = FIELD_DESCRIPTIONS.get("endpoint", "")
            error_msg = f"Invalid value for 'endpoint': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ENDPOINT)}"
            error_msg += f"\n  → Example: endpoint='{{ VALID_BODY_ENDPOINT[0] }}'"
            return (False, error_msg)
    if "ha" in payload:
        value = payload["ha"]
        if value not in VALID_BODY_HA:
            desc = FIELD_DESCRIPTIONS.get("ha", "")
            error_msg = f"Invalid value for 'ha': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_HA)}"
            error_msg += f"\n  → Example: ha='{{ VALID_BODY_HA[0] }}'"
            return (False, error_msg)
    if "security-rating" in payload:
        value = payload["security-rating"]
        if value not in VALID_BODY_SECURITY_RATING:
            desc = FIELD_DESCRIPTIONS.get("security-rating", "")
            error_msg = f"Invalid value for 'security-rating': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SECURITY_RATING)}"
            error_msg += f"\n  → Example: security-rating='{{ VALID_BODY_SECURITY_RATING[0] }}'"
            return (False, error_msg)
    if "fortiextender" in payload:
        value = payload["fortiextender"]
        if value not in VALID_BODY_FORTIEXTENDER:
            desc = FIELD_DESCRIPTIONS.get("fortiextender", "")
            error_msg = f"Invalid value for 'fortiextender': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FORTIEXTENDER)}"
            error_msg += f"\n  → Example: fortiextender='{{ VALID_BODY_FORTIEXTENDER[0] }}'"
            return (False, error_msg)
    if "connector" in payload:
        value = payload["connector"]
        if value not in VALID_BODY_CONNECTOR:
            desc = FIELD_DESCRIPTIONS.get("connector", "")
            error_msg = f"Invalid value for 'connector': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CONNECTOR)}"
            error_msg += f"\n  → Example: connector='{{ VALID_BODY_CONNECTOR[0] }}'"
            return (False, error_msg)
    if "sdwan" in payload:
        value = payload["sdwan"]
        if value not in VALID_BODY_SDWAN:
            desc = FIELD_DESCRIPTIONS.get("sdwan", "")
            error_msg = f"Invalid value for 'sdwan': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SDWAN)}"
            error_msg += f"\n  → Example: sdwan='{{ VALID_BODY_SDWAN[0] }}'"
            return (False, error_msg)
    if "cifs" in payload:
        value = payload["cifs"]
        if value not in VALID_BODY_CIFS:
            desc = FIELD_DESCRIPTIONS.get("cifs", "")
            error_msg = f"Invalid value for 'cifs': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CIFS)}"
            error_msg += f"\n  → Example: cifs='{{ VALID_BODY_CIFS[0] }}'"
            return (False, error_msg)
    if "switch-controller" in payload:
        value = payload["switch-controller"]
        if value not in VALID_BODY_SWITCH_CONTROLLER:
            desc = FIELD_DESCRIPTIONS.get("switch-controller", "")
            error_msg = f"Invalid value for 'switch-controller': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SWITCH_CONTROLLER)}"
            error_msg += f"\n  → Example: switch-controller='{{ VALID_BODY_SWITCH_CONTROLLER[0] }}'"
            return (False, error_msg)
    if "rest-api" in payload:
        value = payload["rest-api"]
        if value not in VALID_BODY_REST_API:
            desc = FIELD_DESCRIPTIONS.get("rest-api", "")
            error_msg = f"Invalid value for 'rest-api': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_REST_API)}"
            error_msg += f"\n  → Example: rest-api='{{ VALID_BODY_REST_API[0] }}'"
            return (False, error_msg)
    if "web-svc" in payload:
        value = payload["web-svc"]
        if value not in VALID_BODY_WEB_SVC:
            desc = FIELD_DESCRIPTIONS.get("web-svc", "")
            error_msg = f"Invalid value for 'web-svc': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WEB_SVC)}"
            error_msg += f"\n  → Example: web-svc='{{ VALID_BODY_WEB_SVC[0] }}'"
            return (False, error_msg)
    if "webproxy" in payload:
        value = payload["webproxy"]
        if value not in VALID_BODY_WEBPROXY:
            desc = FIELD_DESCRIPTIONS.get("webproxy", "")
            error_msg = f"Invalid value for 'webproxy': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WEBPROXY)}"
            error_msg += f"\n  → Example: webproxy='{{ VALID_BODY_WEBPROXY[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_log_eventfilter_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update log/eventfilter."""
    # Step 1: Validate enum values
    if "event" in payload:
        value = payload["event"]
        if value not in VALID_BODY_EVENT:
            return (
                False,
                f"Invalid value for 'event'='{value}'. Must be one of: {', '.join(VALID_BODY_EVENT)}",
            )
    if "system" in payload:
        value = payload["system"]
        if value not in VALID_BODY_SYSTEM:
            return (
                False,
                f"Invalid value for 'system'='{value}'. Must be one of: {', '.join(VALID_BODY_SYSTEM)}",
            )
    if "vpn" in payload:
        value = payload["vpn"]
        if value not in VALID_BODY_VPN:
            return (
                False,
                f"Invalid value for 'vpn'='{value}'. Must be one of: {', '.join(VALID_BODY_VPN)}",
            )
    if "user" in payload:
        value = payload["user"]
        if value not in VALID_BODY_USER:
            return (
                False,
                f"Invalid value for 'user'='{value}'. Must be one of: {', '.join(VALID_BODY_USER)}",
            )
    if "router" in payload:
        value = payload["router"]
        if value not in VALID_BODY_ROUTER:
            return (
                False,
                f"Invalid value for 'router'='{value}'. Must be one of: {', '.join(VALID_BODY_ROUTER)}",
            )
    if "wireless-activity" in payload:
        value = payload["wireless-activity"]
        if value not in VALID_BODY_WIRELESS_ACTIVITY:
            return (
                False,
                f"Invalid value for 'wireless-activity'='{value}'. Must be one of: {', '.join(VALID_BODY_WIRELESS_ACTIVITY)}",
            )
    if "wan-opt" in payload:
        value = payload["wan-opt"]
        if value not in VALID_BODY_WAN_OPT:
            return (
                False,
                f"Invalid value for 'wan-opt'='{value}'. Must be one of: {', '.join(VALID_BODY_WAN_OPT)}",
            )
    if "endpoint" in payload:
        value = payload["endpoint"]
        if value not in VALID_BODY_ENDPOINT:
            return (
                False,
                f"Invalid value for 'endpoint'='{value}'. Must be one of: {', '.join(VALID_BODY_ENDPOINT)}",
            )
    if "ha" in payload:
        value = payload["ha"]
        if value not in VALID_BODY_HA:
            return (
                False,
                f"Invalid value for 'ha'='{value}'. Must be one of: {', '.join(VALID_BODY_HA)}",
            )
    if "security-rating" in payload:
        value = payload["security-rating"]
        if value not in VALID_BODY_SECURITY_RATING:
            return (
                False,
                f"Invalid value for 'security-rating'='{value}'. Must be one of: {', '.join(VALID_BODY_SECURITY_RATING)}",
            )
    if "fortiextender" in payload:
        value = payload["fortiextender"]
        if value not in VALID_BODY_FORTIEXTENDER:
            return (
                False,
                f"Invalid value for 'fortiextender'='{value}'. Must be one of: {', '.join(VALID_BODY_FORTIEXTENDER)}",
            )
    if "connector" in payload:
        value = payload["connector"]
        if value not in VALID_BODY_CONNECTOR:
            return (
                False,
                f"Invalid value for 'connector'='{value}'. Must be one of: {', '.join(VALID_BODY_CONNECTOR)}",
            )
    if "sdwan" in payload:
        value = payload["sdwan"]
        if value not in VALID_BODY_SDWAN:
            return (
                False,
                f"Invalid value for 'sdwan'='{value}'. Must be one of: {', '.join(VALID_BODY_SDWAN)}",
            )
    if "cifs" in payload:
        value = payload["cifs"]
        if value not in VALID_BODY_CIFS:
            return (
                False,
                f"Invalid value for 'cifs'='{value}'. Must be one of: {', '.join(VALID_BODY_CIFS)}",
            )
    if "switch-controller" in payload:
        value = payload["switch-controller"]
        if value not in VALID_BODY_SWITCH_CONTROLLER:
            return (
                False,
                f"Invalid value for 'switch-controller'='{value}'. Must be one of: {', '.join(VALID_BODY_SWITCH_CONTROLLER)}",
            )
    if "rest-api" in payload:
        value = payload["rest-api"]
        if value not in VALID_BODY_REST_API:
            return (
                False,
                f"Invalid value for 'rest-api'='{value}'. Must be one of: {', '.join(VALID_BODY_REST_API)}",
            )
    if "web-svc" in payload:
        value = payload["web-svc"]
        if value not in VALID_BODY_WEB_SVC:
            return (
                False,
                f"Invalid value for 'web-svc'='{value}'. Must be one of: {', '.join(VALID_BODY_WEB_SVC)}",
            )
    if "webproxy" in payload:
        value = payload["webproxy"]
        if value not in VALID_BODY_WEBPROXY:
            return (
                False,
                f"Invalid value for 'webproxy'='{value}'. Must be one of: {', '.join(VALID_BODY_WEBPROXY)}",
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
    "endpoint": "log/eventfilter",
    "category": "cmdb",
    "api_path": "log/eventfilter",
    "help": "Configure log event filters.",
    "total_fields": 18,
    "required_fields_count": 0,
    "fields_with_defaults_count": 18,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
