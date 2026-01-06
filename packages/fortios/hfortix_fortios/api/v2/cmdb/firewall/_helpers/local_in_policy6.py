"""Validation helpers for firewall/local_in_policy6 - Auto-generated"""

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
    "intf",  # Incoming interface name from available options.
    "srcaddr",  # Source address object from available options.
    "dstaddr",  # Destination address object from available options.
    "service",  # Service object from available options. Separate names with a space.
    "schedule",  # Schedule object from available options.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "policyid": 0,
    "uuid": "00000000-0000-0000-0000-000000000000",
    "srcaddr-negate": "disable",
    "internet-service6-src": "disable",
    "dstaddr-negate": "disable",
    "action": "deny",
    "service-negate": "disable",
    "internet-service6-src-negate": "disable",
    "schedule": "",
    "status": "enable",
    "virtual-patch": "disable",
    "logtraffic": "disable",
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
    "policyid": "integer",  # User defined local in policy ID.
    "uuid": "uuid",  # Universally Unique Identifier (UUID; automatically assigned 
    "intf": "string",  # Incoming interface name from available options.
    "srcaddr": "string",  # Source address object from available options.
    "srcaddr-negate": "option",  # When enabled srcaddr specifies what the source address must 
    "dstaddr": "string",  # Destination address object from available options.
    "internet-service6-src": "option",  # Enable/disable use of IPv6 Internet Services in source for t
    "internet-service6-src-name": "string",  # IPv6 Internet Service source name.
    "internet-service6-src-group": "string",  # Internet Service6 source group name.
    "internet-service6-src-custom": "string",  # Custom IPv6 Internet Service source name.
    "internet-service6-src-custom-group": "string",  # Custom Internet Service6 source group name.
    "internet-service6-src-fortiguard": "string",  # FortiGuard IPv6 Internet Service source name.
    "dstaddr-negate": "option",  # When enabled dstaddr specifies what the destination address 
    "action": "option",  # Action performed on traffic matching the policy (default = d
    "service": "string",  # Service object from available options. Separate names with a
    "service-negate": "option",  # When enabled service specifies what the service must NOT be.
    "internet-service6-src-negate": "option",  # When enabled internet-service6-src specifies what the servic
    "schedule": "string",  # Schedule object from available options.
    "status": "option",  # Enable/disable this local-in policy.
    "virtual-patch": "option",  # Enable/disable the virtual patching feature.
    "logtraffic": "option",  # Enable/disable local-in traffic logging.
    "comments": "var-string",  # Comment.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "policyid": "User defined local in policy ID.",
    "uuid": "Universally Unique Identifier (UUID; automatically assigned but can be manually reset).",
    "intf": "Incoming interface name from available options.",
    "srcaddr": "Source address object from available options.",
    "srcaddr-negate": "When enabled srcaddr specifies what the source address must NOT be.",
    "dstaddr": "Destination address object from available options.",
    "internet-service6-src": "Enable/disable use of IPv6 Internet Services in source for this local-in policy.If enabled, source address is not used.",
    "internet-service6-src-name": "IPv6 Internet Service source name.",
    "internet-service6-src-group": "Internet Service6 source group name.",
    "internet-service6-src-custom": "Custom IPv6 Internet Service source name.",
    "internet-service6-src-custom-group": "Custom Internet Service6 source group name.",
    "internet-service6-src-fortiguard": "FortiGuard IPv6 Internet Service source name.",
    "dstaddr-negate": "When enabled dstaddr specifies what the destination address must NOT be.",
    "action": "Action performed on traffic matching the policy (default = deny).",
    "service": "Service object from available options. Separate names with a space.",
    "service-negate": "When enabled service specifies what the service must NOT be.",
    "internet-service6-src-negate": "When enabled internet-service6-src specifies what the service must NOT be.",
    "schedule": "Schedule object from available options.",
    "status": "Enable/disable this local-in policy.",
    "virtual-patch": "Enable/disable the virtual patching feature.",
    "logtraffic": "Enable/disable local-in traffic logging.",
    "comments": "Comment.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "policyid": {"type": "integer", "min": 0, "max": 4294967295},
    "schedule": {"type": "string", "max_length": 35},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "intf": {
        "name": {
            "type": "string",
            "help": "Address name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "srcaddr": {
        "name": {
            "type": "string",
            "help": "Address name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "dstaddr": {
        "name": {
            "type": "string",
            "help": "Address name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "internet-service6-src-name": {
        "name": {
            "type": "string",
            "help": "Internet Service name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "internet-service6-src-group": {
        "name": {
            "type": "string",
            "help": "Internet Service group name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "internet-service6-src-custom": {
        "name": {
            "type": "string",
            "help": "Custom Internet Service name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "internet-service6-src-custom-group": {
        "name": {
            "type": "string",
            "help": "Custom Internet Service6 group name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "internet-service6-src-fortiguard": {
        "name": {
            "type": "string",
            "help": "FortiGuard Internet Service name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "service": {
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
VALID_BODY_SRCADDR_NEGATE = [
    "enable",  # Enable source address negate.
    "disable",  # Disable source address negate.
]
VALID_BODY_INTERNET_SERVICE6_SRC = [
    "enable",  # Enable use of IPv6 Internet Services source in local-in policy.
    "disable",  # Disable use of IPv6 Internet Services source in local-in policy.
]
VALID_BODY_DSTADDR_NEGATE = [
    "enable",  # Enable destination address negate.
    "disable",  # Disable destination address negate.
]
VALID_BODY_ACTION = [
    "accept",  # Allow local-in traffic matching this policy.
    "deny",  # Deny or block local-in traffic matching this policy.
]
VALID_BODY_SERVICE_NEGATE = [
    "enable",  # Enable negated service match.
    "disable",  # Disable negated service match.
]
VALID_BODY_INTERNET_SERVICE6_SRC_NEGATE = [
    "enable",  # Enable negated IPv6 Internet Service source match.
    "disable",  # Disable negated IPv6 Internet Service source match.
]
VALID_BODY_STATUS = [
    "enable",  # Enable this local-in policy.
    "disable",  # Disable this local-in policy.
]
VALID_BODY_VIRTUAL_PATCH = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_LOGTRAFFIC = [
    "enable",  # Enable local-in traffic logging.
    "disable",  # Disable local-in traffic logging.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_firewall_local_in_policy6_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for firewall/local_in_policy6."""
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
    """Validate required fields for firewall/local_in_policy6."""
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


def validate_firewall_local_in_policy6_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new firewall/local_in_policy6 object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "srcaddr-negate" in payload:
        value = payload["srcaddr-negate"]
        if value not in VALID_BODY_SRCADDR_NEGATE:
            desc = FIELD_DESCRIPTIONS.get("srcaddr-negate", "")
            error_msg = f"Invalid value for 'srcaddr-negate': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SRCADDR_NEGATE)}"
            error_msg += f"\n  → Example: srcaddr-negate='{{ VALID_BODY_SRCADDR_NEGATE[0] }}'"
            return (False, error_msg)
    if "internet-service6-src" in payload:
        value = payload["internet-service6-src"]
        if value not in VALID_BODY_INTERNET_SERVICE6_SRC:
            desc = FIELD_DESCRIPTIONS.get("internet-service6-src", "")
            error_msg = f"Invalid value for 'internet-service6-src': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_INTERNET_SERVICE6_SRC)}"
            error_msg += f"\n  → Example: internet-service6-src='{{ VALID_BODY_INTERNET_SERVICE6_SRC[0] }}'"
            return (False, error_msg)
    if "dstaddr-negate" in payload:
        value = payload["dstaddr-negate"]
        if value not in VALID_BODY_DSTADDR_NEGATE:
            desc = FIELD_DESCRIPTIONS.get("dstaddr-negate", "")
            error_msg = f"Invalid value for 'dstaddr-negate': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DSTADDR_NEGATE)}"
            error_msg += f"\n  → Example: dstaddr-negate='{{ VALID_BODY_DSTADDR_NEGATE[0] }}'"
            return (False, error_msg)
    if "action" in payload:
        value = payload["action"]
        if value not in VALID_BODY_ACTION:
            desc = FIELD_DESCRIPTIONS.get("action", "")
            error_msg = f"Invalid value for 'action': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ACTION)}"
            error_msg += f"\n  → Example: action='{{ VALID_BODY_ACTION[0] }}'"
            return (False, error_msg)
    if "service-negate" in payload:
        value = payload["service-negate"]
        if value not in VALID_BODY_SERVICE_NEGATE:
            desc = FIELD_DESCRIPTIONS.get("service-negate", "")
            error_msg = f"Invalid value for 'service-negate': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SERVICE_NEGATE)}"
            error_msg += f"\n  → Example: service-negate='{{ VALID_BODY_SERVICE_NEGATE[0] }}'"
            return (False, error_msg)
    if "internet-service6-src-negate" in payload:
        value = payload["internet-service6-src-negate"]
        if value not in VALID_BODY_INTERNET_SERVICE6_SRC_NEGATE:
            desc = FIELD_DESCRIPTIONS.get("internet-service6-src-negate", "")
            error_msg = f"Invalid value for 'internet-service6-src-negate': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_INTERNET_SERVICE6_SRC_NEGATE)}"
            error_msg += f"\n  → Example: internet-service6-src-negate='{{ VALID_BODY_INTERNET_SERVICE6_SRC_NEGATE[0] }}'"
            return (False, error_msg)
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
    if "virtual-patch" in payload:
        value = payload["virtual-patch"]
        if value not in VALID_BODY_VIRTUAL_PATCH:
            desc = FIELD_DESCRIPTIONS.get("virtual-patch", "")
            error_msg = f"Invalid value for 'virtual-patch': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_VIRTUAL_PATCH)}"
            error_msg += f"\n  → Example: virtual-patch='{{ VALID_BODY_VIRTUAL_PATCH[0] }}'"
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

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_firewall_local_in_policy6_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update firewall/local_in_policy6."""
    # Step 1: Validate enum values
    if "srcaddr-negate" in payload:
        value = payload["srcaddr-negate"]
        if value not in VALID_BODY_SRCADDR_NEGATE:
            return (
                False,
                f"Invalid value for 'srcaddr-negate'='{value}'. Must be one of: {', '.join(VALID_BODY_SRCADDR_NEGATE)}",
            )
    if "internet-service6-src" in payload:
        value = payload["internet-service6-src"]
        if value not in VALID_BODY_INTERNET_SERVICE6_SRC:
            return (
                False,
                f"Invalid value for 'internet-service6-src'='{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE6_SRC)}",
            )
    if "dstaddr-negate" in payload:
        value = payload["dstaddr-negate"]
        if value not in VALID_BODY_DSTADDR_NEGATE:
            return (
                False,
                f"Invalid value for 'dstaddr-negate'='{value}'. Must be one of: {', '.join(VALID_BODY_DSTADDR_NEGATE)}",
            )
    if "action" in payload:
        value = payload["action"]
        if value not in VALID_BODY_ACTION:
            return (
                False,
                f"Invalid value for 'action'='{value}'. Must be one of: {', '.join(VALID_BODY_ACTION)}",
            )
    if "service-negate" in payload:
        value = payload["service-negate"]
        if value not in VALID_BODY_SERVICE_NEGATE:
            return (
                False,
                f"Invalid value for 'service-negate'='{value}'. Must be one of: {', '.join(VALID_BODY_SERVICE_NEGATE)}",
            )
    if "internet-service6-src-negate" in payload:
        value = payload["internet-service6-src-negate"]
        if value not in VALID_BODY_INTERNET_SERVICE6_SRC_NEGATE:
            return (
                False,
                f"Invalid value for 'internet-service6-src-negate'='{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE6_SRC_NEGATE)}",
            )
    if "status" in payload:
        value = payload["status"]
        if value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid value for 'status'='{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )
    if "virtual-patch" in payload:
        value = payload["virtual-patch"]
        if value not in VALID_BODY_VIRTUAL_PATCH:
            return (
                False,
                f"Invalid value for 'virtual-patch'='{value}'. Must be one of: {', '.join(VALID_BODY_VIRTUAL_PATCH)}",
            )
    if "logtraffic" in payload:
        value = payload["logtraffic"]
        if value not in VALID_BODY_LOGTRAFFIC:
            return (
                False,
                f"Invalid value for 'logtraffic'='{value}'. Must be one of: {', '.join(VALID_BODY_LOGTRAFFIC)}",
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
    "endpoint": "firewall/local_in_policy6",
    "category": "cmdb",
    "api_path": "firewall/local-in-policy6",
    "mkey": "policyid",
    "mkey_type": "integer",
    "help": "Configure user defined IPv6 local-in policies.",
    "total_fields": 22,
    "required_fields_count": 5,
    "fields_with_defaults_count": 12,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
