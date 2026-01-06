"""Validation helpers for firewall/multicast_policy - Auto-generated"""

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
    "srcintf",  # Source interface name.
    "dstintf",  # Destination interface name.
    "srcaddr",  # Source address objects.
    "dstaddr",  # Destination address objects.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "id": 0,
    "uuid": "00000000-0000-0000-0000-000000000000",
    "name": "",
    "status": "enable",
    "srcintf": "",
    "dstintf": "",
    "snat": "disable",
    "snat-ip": "0.0.0.0",
    "dnat": "0.0.0.0",
    "action": "accept",
    "protocol": 0,
    "start-port": 1,
    "end-port": 65535,
    "utm-status": "disable",
    "ips-sensor": "",
    "logtraffic": "utm",
    "auto-asic-offload": "enable",
    "traffic-shaper": "",
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
    "id": "integer",  # Policy ID ((0 - 4294967294).
    "uuid": "uuid",  # Universally Unique Identifier (UUID; automatically assigned 
    "name": "string",  # Policy name.
    "comments": "var-string",  # Comment.
    "status": "option",  # Enable/disable this policy.
    "srcintf": "string",  # Source interface name.
    "dstintf": "string",  # Destination interface name.
    "srcaddr": "string",  # Source address objects.
    "dstaddr": "string",  # Destination address objects.
    "snat": "option",  # Enable/disable substitution of the outgoing interface IP add
    "snat-ip": "ipv4-address",  # IPv4 address to be used as the source address for NATed traf
    "dnat": "ipv4-address-any",  # IPv4 DNAT address used for multicast destination addresses.
    "action": "option",  # Accept or deny traffic matching the policy.
    "protocol": "integer",  # Integer value for the protocol type as defined by IANA (0 - 
    "start-port": "integer",  # Integer value for starting TCP/UDP/SCTP destination port in 
    "end-port": "integer",  # Integer value for ending TCP/UDP/SCTP destination port in ra
    "utm-status": "option",  # Enable to add an IPS security profile to the policy.
    "ips-sensor": "string",  # Name of an existing IPS sensor.
    "logtraffic": "option",  # Enable or disable logging. Log all sessions or security prof
    "auto-asic-offload": "option",  # Enable/disable offloading policy traffic for hardware accele
    "traffic-shaper": "string",  # Traffic shaper to apply to traffic forwarded by the multicas
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "id": "Policy ID ((0 - 4294967294).",
    "uuid": "Universally Unique Identifier (UUID; automatically assigned but can be manually reset).",
    "name": "Policy name.",
    "comments": "Comment.",
    "status": "Enable/disable this policy.",
    "srcintf": "Source interface name.",
    "dstintf": "Destination interface name.",
    "srcaddr": "Source address objects.",
    "dstaddr": "Destination address objects.",
    "snat": "Enable/disable substitution of the outgoing interface IP address for the original source IP address (called source NAT or SNAT).",
    "snat-ip": "IPv4 address to be used as the source address for NATed traffic.",
    "dnat": "IPv4 DNAT address used for multicast destination addresses.",
    "action": "Accept or deny traffic matching the policy.",
    "protocol": "Integer value for the protocol type as defined by IANA (0 - 255, default = 0).",
    "start-port": "Integer value for starting TCP/UDP/SCTP destination port in range (1 - 65535, default = 1).",
    "end-port": "Integer value for ending TCP/UDP/SCTP destination port in range (1 - 65535, default = 1).",
    "utm-status": "Enable to add an IPS security profile to the policy.",
    "ips-sensor": "Name of an existing IPS sensor.",
    "logtraffic": "Enable or disable logging. Log all sessions or security profile sessions.",
    "auto-asic-offload": "Enable/disable offloading policy traffic for hardware acceleration.",
    "traffic-shaper": "Traffic shaper to apply to traffic forwarded by the multicast policy.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "id": {"type": "integer", "min": 0, "max": 4294967294},
    "name": {"type": "string", "max_length": 35},
    "srcintf": {"type": "string", "max_length": 35},
    "dstintf": {"type": "string", "max_length": 35},
    "protocol": {"type": "integer", "min": 0, "max": 255},
    "start-port": {"type": "integer", "min": 0, "max": 65535},
    "end-port": {"type": "integer", "min": 0, "max": 65535},
    "ips-sensor": {"type": "string", "max_length": 47},
    "traffic-shaper": {"type": "string", "max_length": 35},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "srcaddr": {
        "name": {
            "type": "string",
            "help": "Source address objects.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "dstaddr": {
        "name": {
            "type": "string",
            "help": "Destination address objects.",
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
VALID_BODY_SNAT = [
    "enable",  # Enable source NAT.
    "disable",  # Disable source NAT.
]
VALID_BODY_ACTION = [
    "accept",  # Accept traffic matching the policy.
    "deny",  # Deny or block traffic matching the policy.
]
VALID_BODY_UTM_STATUS = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_LOGTRAFFIC = [
    "all",  # Enable logging traffic accepted by this policy.
    "utm",  # Log traffic that has a security profile applied to it.
    "disable",  # Disable all logging for this policy.
]
VALID_BODY_AUTO_ASIC_OFFLOAD = [
    "enable",  # Enable hardware acceleration offloading.
    "disable",  # Disable offloading for hardware acceleration.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_firewall_multicast_policy_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for firewall/multicast_policy."""
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
    """Validate required fields for firewall/multicast_policy."""
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


def validate_firewall_multicast_policy_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new firewall/multicast_policy object."""
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
    if "snat" in payload:
        value = payload["snat"]
        if value not in VALID_BODY_SNAT:
            desc = FIELD_DESCRIPTIONS.get("snat", "")
            error_msg = f"Invalid value for 'snat': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SNAT)}"
            error_msg += f"\n  → Example: snat='{{ VALID_BODY_SNAT[0] }}'"
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
    if "utm-status" in payload:
        value = payload["utm-status"]
        if value not in VALID_BODY_UTM_STATUS:
            desc = FIELD_DESCRIPTIONS.get("utm-status", "")
            error_msg = f"Invalid value for 'utm-status': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_UTM_STATUS)}"
            error_msg += f"\n  → Example: utm-status='{{ VALID_BODY_UTM_STATUS[0] }}'"
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
    if "auto-asic-offload" in payload:
        value = payload["auto-asic-offload"]
        if value not in VALID_BODY_AUTO_ASIC_OFFLOAD:
            desc = FIELD_DESCRIPTIONS.get("auto-asic-offload", "")
            error_msg = f"Invalid value for 'auto-asic-offload': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTO_ASIC_OFFLOAD)}"
            error_msg += f"\n  → Example: auto-asic-offload='{{ VALID_BODY_AUTO_ASIC_OFFLOAD[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_firewall_multicast_policy_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update firewall/multicast_policy."""
    # Step 1: Validate enum values
    if "status" in payload:
        value = payload["status"]
        if value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid value for 'status'='{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )
    if "snat" in payload:
        value = payload["snat"]
        if value not in VALID_BODY_SNAT:
            return (
                False,
                f"Invalid value for 'snat'='{value}'. Must be one of: {', '.join(VALID_BODY_SNAT)}",
            )
    if "action" in payload:
        value = payload["action"]
        if value not in VALID_BODY_ACTION:
            return (
                False,
                f"Invalid value for 'action'='{value}'. Must be one of: {', '.join(VALID_BODY_ACTION)}",
            )
    if "utm-status" in payload:
        value = payload["utm-status"]
        if value not in VALID_BODY_UTM_STATUS:
            return (
                False,
                f"Invalid value for 'utm-status'='{value}'. Must be one of: {', '.join(VALID_BODY_UTM_STATUS)}",
            )
    if "logtraffic" in payload:
        value = payload["logtraffic"]
        if value not in VALID_BODY_LOGTRAFFIC:
            return (
                False,
                f"Invalid value for 'logtraffic'='{value}'. Must be one of: {', '.join(VALID_BODY_LOGTRAFFIC)}",
            )
    if "auto-asic-offload" in payload:
        value = payload["auto-asic-offload"]
        if value not in VALID_BODY_AUTO_ASIC_OFFLOAD:
            return (
                False,
                f"Invalid value for 'auto-asic-offload'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTO_ASIC_OFFLOAD)}",
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
    "endpoint": "firewall/multicast_policy",
    "category": "cmdb",
    "api_path": "firewall/multicast-policy",
    "mkey": "id",
    "mkey_type": "integer",
    "help": "Configure multicast NAT policies.",
    "total_fields": 21,
    "required_fields_count": 4,
    "fields_with_defaults_count": 18,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
