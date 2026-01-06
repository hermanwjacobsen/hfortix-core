"""Validation helpers for firewall/shaping_policy - Auto-generated"""

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
    "srcaddr",  # IPv4 source address and address group names.
    "dstaddr",  # IPv4 destination address and address group names.
    "srcaddr6",  # IPv6 source address and address group names.
    "dstaddr6",  # IPv6 destination address and address group names.
    "service",  # Service and service group names.
    "dstintf",  # One or more outgoing (egress) interfaces.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "id": 0,
    "uuid": "00000000-0000-0000-0000-000000000000",
    "name": "",
    "status": "enable",
    "ip-version": "4",
    "traffic-type": "forwarding",
    "internet-service": "disable",
    "internet-service-src": "disable",
    "schedule": "",
    "tos-mask": "",
    "tos": "",
    "tos-negate": "disable",
    "traffic-shaper": "",
    "traffic-shaper-reverse": "",
    "per-ip-shaper": "",
    "class-id": 0,
    "diffserv-forward": "disable",
    "diffserv-reverse": "disable",
    "diffservcode-forward": "",
    "diffservcode-rev": "",
    "cos-mask": "",
    "cos": "",
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
    "id": "integer",  # Shaping policy ID (0 - 4294967295).
    "uuid": "uuid",  # Universally Unique Identifier (UUID; automatically assigned 
    "name": "string",  # Shaping policy name.
    "comment": "var-string",  # Comments.
    "status": "option",  # Enable/disable this traffic shaping policy.
    "ip-version": "option",  # Apply this traffic shaping policy to IPv4 or IPv6 traffic.
    "traffic-type": "option",  # Traffic type.
    "srcaddr": "string",  # IPv4 source address and address group names.
    "dstaddr": "string",  # IPv4 destination address and address group names.
    "srcaddr6": "string",  # IPv6 source address and address group names.
    "dstaddr6": "string",  # IPv6 destination address and address group names.
    "internet-service": "option",  # Enable/disable use of Internet Services for this policy. If 
    "internet-service-name": "string",  # Internet Service ID.
    "internet-service-group": "string",  # Internet Service group name.
    "internet-service-custom": "string",  # Custom Internet Service name.
    "internet-service-custom-group": "string",  # Custom Internet Service group name.
    "internet-service-fortiguard": "string",  # FortiGuard Internet Service name.
    "internet-service-src": "option",  # Enable/disable use of Internet Services in source for this p
    "internet-service-src-name": "string",  # Internet Service source name.
    "internet-service-src-group": "string",  # Internet Service source group name.
    "internet-service-src-custom": "string",  # Custom Internet Service source name.
    "internet-service-src-custom-group": "string",  # Custom Internet Service source group name.
    "internet-service-src-fortiguard": "string",  # FortiGuard Internet Service source name.
    "service": "string",  # Service and service group names.
    "schedule": "string",  # Schedule name.
    "users": "string",  # Apply this traffic shaping policy to individual users that h
    "groups": "string",  # Apply this traffic shaping policy to user groups that have a
    "application": "string",  # IDs of one or more applications that this shaper applies app
    "app-category": "string",  # IDs of one or more application categories that this shaper a
    "app-group": "string",  # One or more application group names.
    "url-category": "string",  # IDs of one or more FortiGuard Web Filtering categories that 
    "srcintf": "string",  # One or more incoming (ingress) interfaces.
    "dstintf": "string",  # One or more outgoing (egress) interfaces.
    "tos-mask": "user",  # Non-zero bit positions are used for comparison while zero bi
    "tos": "user",  # ToS (Type of Service) value used for comparison.
    "tos-negate": "option",  # Enable negated TOS match.
    "traffic-shaper": "string",  # Traffic shaper to apply to traffic forwarded by the firewall
    "traffic-shaper-reverse": "string",  # Traffic shaper to apply to response traffic received by the 
    "per-ip-shaper": "string",  # Per-IP traffic shaper to apply with this policy.
    "class-id": "integer",  # Traffic class ID.
    "diffserv-forward": "option",  # Enable to change packet's DiffServ values to the specified d
    "diffserv-reverse": "option",  # Enable to change packet's reverse (reply) DiffServ values to
    "diffservcode-forward": "user",  # Change packet's DiffServ to this value.
    "diffservcode-rev": "user",  # Change packet's reverse (reply) DiffServ to this value.
    "cos-mask": "user",  # VLAN CoS evaluated bits.
    "cos": "user",  # VLAN CoS bit pattern.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "id": "Shaping policy ID (0 - 4294967295).",
    "uuid": "Universally Unique Identifier (UUID; automatically assigned but can be manually reset).",
    "name": "Shaping policy name.",
    "comment": "Comments.",
    "status": "Enable/disable this traffic shaping policy.",
    "ip-version": "Apply this traffic shaping policy to IPv4 or IPv6 traffic.",
    "traffic-type": "Traffic type.",
    "srcaddr": "IPv4 source address and address group names.",
    "dstaddr": "IPv4 destination address and address group names.",
    "srcaddr6": "IPv6 source address and address group names.",
    "dstaddr6": "IPv6 destination address and address group names.",
    "internet-service": "Enable/disable use of Internet Services for this policy. If enabled, destination address and service are not used.",
    "internet-service-name": "Internet Service ID.",
    "internet-service-group": "Internet Service group name.",
    "internet-service-custom": "Custom Internet Service name.",
    "internet-service-custom-group": "Custom Internet Service group name.",
    "internet-service-fortiguard": "FortiGuard Internet Service name.",
    "internet-service-src": "Enable/disable use of Internet Services in source for this policy. If enabled, source address is not used.",
    "internet-service-src-name": "Internet Service source name.",
    "internet-service-src-group": "Internet Service source group name.",
    "internet-service-src-custom": "Custom Internet Service source name.",
    "internet-service-src-custom-group": "Custom Internet Service source group name.",
    "internet-service-src-fortiguard": "FortiGuard Internet Service source name.",
    "service": "Service and service group names.",
    "schedule": "Schedule name.",
    "users": "Apply this traffic shaping policy to individual users that have authenticated with the FortiGate.",
    "groups": "Apply this traffic shaping policy to user groups that have authenticated with the FortiGate.",
    "application": "IDs of one or more applications that this shaper applies application control traffic shaping to.",
    "app-category": "IDs of one or more application categories that this shaper applies application control traffic shaping to.",
    "app-group": "One or more application group names.",
    "url-category": "IDs of one or more FortiGuard Web Filtering categories that this shaper applies traffic shaping to.",
    "srcintf": "One or more incoming (ingress) interfaces.",
    "dstintf": "One or more outgoing (egress) interfaces.",
    "tos-mask": "Non-zero bit positions are used for comparison while zero bit positions are ignored.",
    "tos": "ToS (Type of Service) value used for comparison.",
    "tos-negate": "Enable negated TOS match.",
    "traffic-shaper": "Traffic shaper to apply to traffic forwarded by the firewall policy.",
    "traffic-shaper-reverse": "Traffic shaper to apply to response traffic received by the firewall policy.",
    "per-ip-shaper": "Per-IP traffic shaper to apply with this policy.",
    "class-id": "Traffic class ID.",
    "diffserv-forward": "Enable to change packet's DiffServ values to the specified diffservcode-forward value.",
    "diffserv-reverse": "Enable to change packet's reverse (reply) DiffServ values to the specified diffservcode-rev value.",
    "diffservcode-forward": "Change packet's DiffServ to this value.",
    "diffservcode-rev": "Change packet's reverse (reply) DiffServ to this value.",
    "cos-mask": "VLAN CoS evaluated bits.",
    "cos": "VLAN CoS bit pattern.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "id": {"type": "integer", "min": 0, "max": 4294967295},
    "name": {"type": "string", "max_length": 35},
    "schedule": {"type": "string", "max_length": 35},
    "traffic-shaper": {"type": "string", "max_length": 35},
    "traffic-shaper-reverse": {"type": "string", "max_length": 35},
    "per-ip-shaper": {"type": "string", "max_length": 35},
    "class-id": {"type": "integer", "min": 0, "max": 4294967295},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
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
    "internet-service-name": {
        "name": {
            "type": "string",
            "help": "Internet Service name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "internet-service-group": {
        "name": {
            "type": "string",
            "help": "Internet Service group name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "internet-service-custom": {
        "name": {
            "type": "string",
            "help": "Custom Internet Service name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "internet-service-custom-group": {
        "name": {
            "type": "string",
            "help": "Custom Internet Service group name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "internet-service-fortiguard": {
        "name": {
            "type": "string",
            "help": "FortiGuard Internet Service name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "internet-service-src-name": {
        "name": {
            "type": "string",
            "help": "Internet Service name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "internet-service-src-group": {
        "name": {
            "type": "string",
            "help": "Internet Service group name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "internet-service-src-custom": {
        "name": {
            "type": "string",
            "help": "Custom Internet Service name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "internet-service-src-custom-group": {
        "name": {
            "type": "string",
            "help": "Custom Internet Service group name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "internet-service-src-fortiguard": {
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
    "users": {
        "name": {
            "type": "string",
            "help": "User name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "groups": {
        "name": {
            "type": "string",
            "help": "Group name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "application": {
        "id": {
            "type": "integer",
            "help": "Application IDs.",
            "required": True,
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
    },
    "app-category": {
        "id": {
            "type": "integer",
            "help": "Category IDs.",
            "required": True,
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
    },
    "app-group": {
        "name": {
            "type": "string",
            "help": "Application group name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "url-category": {
        "id": {
            "type": "integer",
            "help": "URL category ID.",
            "required": True,
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
    },
    "srcintf": {
        "name": {
            "type": "string",
            "help": "Interface name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "dstintf": {
        "name": {
            "type": "string",
            "help": "Interface name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_STATUS = [
    "enable",  # Enable traffic shaping policy.
    "disable",  # Disable traffic shaping policy.
]
VALID_BODY_IP_VERSION = [
    "4",  # Use IPv4 addressing for Configuration Method.
    "6",  # Use IPv6 addressing for Configuration Method.
]
VALID_BODY_TRAFFIC_TYPE = [
    "forwarding",  # Forwarding traffic.
    "local-in",  # Local-in traffic.
    "local-out",  # Local-out traffic.
]
VALID_BODY_INTERNET_SERVICE = [
    "enable",  # Enable use of Internet Service in shaping-policy.
    "disable",  # Disable use of Internet Service in shaping-policy.
]
VALID_BODY_INTERNET_SERVICE_SRC = [
    "enable",  # Enable use of Internet Service source in shaping-policy.
    "disable",  # Disable use of Internet Service source in shaping-policy.
]
VALID_BODY_TOS_NEGATE = [
    "enable",  # Enable TOS match negate.
    "disable",  # Disable TOS match negate.
]
VALID_BODY_DIFFSERV_FORWARD = [
    "enable",  # Enable setting forward (original) traffic DiffServ.
    "disable",  # Disable setting forward (original) traffic DiffServ.
]
VALID_BODY_DIFFSERV_REVERSE = [
    "enable",  # Enable setting reverse (reply) traffic DiffServ.
    "disable",  # Disable setting reverse (reply) traffic DiffServ.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_firewall_shaping_policy_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for firewall/shaping_policy."""
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
    """Validate required fields for firewall/shaping_policy."""
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


def validate_firewall_shaping_policy_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new firewall/shaping_policy object."""
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
    if "ip-version" in payload:
        value = payload["ip-version"]
        if value not in VALID_BODY_IP_VERSION:
            desc = FIELD_DESCRIPTIONS.get("ip-version", "")
            error_msg = f"Invalid value for 'ip-version': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_IP_VERSION)}"
            error_msg += f"\n  → Example: ip-version='{{ VALID_BODY_IP_VERSION[0] }}'"
            return (False, error_msg)
    if "traffic-type" in payload:
        value = payload["traffic-type"]
        if value not in VALID_BODY_TRAFFIC_TYPE:
            desc = FIELD_DESCRIPTIONS.get("traffic-type", "")
            error_msg = f"Invalid value for 'traffic-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_TRAFFIC_TYPE)}"
            error_msg += f"\n  → Example: traffic-type='{{ VALID_BODY_TRAFFIC_TYPE[0] }}'"
            return (False, error_msg)
    if "internet-service" in payload:
        value = payload["internet-service"]
        if value not in VALID_BODY_INTERNET_SERVICE:
            desc = FIELD_DESCRIPTIONS.get("internet-service", "")
            error_msg = f"Invalid value for 'internet-service': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_INTERNET_SERVICE)}"
            error_msg += f"\n  → Example: internet-service='{{ VALID_BODY_INTERNET_SERVICE[0] }}'"
            return (False, error_msg)
    if "internet-service-src" in payload:
        value = payload["internet-service-src"]
        if value not in VALID_BODY_INTERNET_SERVICE_SRC:
            desc = FIELD_DESCRIPTIONS.get("internet-service-src", "")
            error_msg = f"Invalid value for 'internet-service-src': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_INTERNET_SERVICE_SRC)}"
            error_msg += f"\n  → Example: internet-service-src='{{ VALID_BODY_INTERNET_SERVICE_SRC[0] }}'"
            return (False, error_msg)
    if "tos-negate" in payload:
        value = payload["tos-negate"]
        if value not in VALID_BODY_TOS_NEGATE:
            desc = FIELD_DESCRIPTIONS.get("tos-negate", "")
            error_msg = f"Invalid value for 'tos-negate': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_TOS_NEGATE)}"
            error_msg += f"\n  → Example: tos-negate='{{ VALID_BODY_TOS_NEGATE[0] }}'"
            return (False, error_msg)
    if "diffserv-forward" in payload:
        value = payload["diffserv-forward"]
        if value not in VALID_BODY_DIFFSERV_FORWARD:
            desc = FIELD_DESCRIPTIONS.get("diffserv-forward", "")
            error_msg = f"Invalid value for 'diffserv-forward': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DIFFSERV_FORWARD)}"
            error_msg += f"\n  → Example: diffserv-forward='{{ VALID_BODY_DIFFSERV_FORWARD[0] }}'"
            return (False, error_msg)
    if "diffserv-reverse" in payload:
        value = payload["diffserv-reverse"]
        if value not in VALID_BODY_DIFFSERV_REVERSE:
            desc = FIELD_DESCRIPTIONS.get("diffserv-reverse", "")
            error_msg = f"Invalid value for 'diffserv-reverse': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DIFFSERV_REVERSE)}"
            error_msg += f"\n  → Example: diffserv-reverse='{{ VALID_BODY_DIFFSERV_REVERSE[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_firewall_shaping_policy_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update firewall/shaping_policy."""
    # Step 1: Validate enum values
    if "status" in payload:
        value = payload["status"]
        if value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid value for 'status'='{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )
    if "ip-version" in payload:
        value = payload["ip-version"]
        if value not in VALID_BODY_IP_VERSION:
            return (
                False,
                f"Invalid value for 'ip-version'='{value}'. Must be one of: {', '.join(VALID_BODY_IP_VERSION)}",
            )
    if "traffic-type" in payload:
        value = payload["traffic-type"]
        if value not in VALID_BODY_TRAFFIC_TYPE:
            return (
                False,
                f"Invalid value for 'traffic-type'='{value}'. Must be one of: {', '.join(VALID_BODY_TRAFFIC_TYPE)}",
            )
    if "internet-service" in payload:
        value = payload["internet-service"]
        if value not in VALID_BODY_INTERNET_SERVICE:
            return (
                False,
                f"Invalid value for 'internet-service'='{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE)}",
            )
    if "internet-service-src" in payload:
        value = payload["internet-service-src"]
        if value not in VALID_BODY_INTERNET_SERVICE_SRC:
            return (
                False,
                f"Invalid value for 'internet-service-src'='{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE_SRC)}",
            )
    if "tos-negate" in payload:
        value = payload["tos-negate"]
        if value not in VALID_BODY_TOS_NEGATE:
            return (
                False,
                f"Invalid value for 'tos-negate'='{value}'. Must be one of: {', '.join(VALID_BODY_TOS_NEGATE)}",
            )
    if "diffserv-forward" in payload:
        value = payload["diffserv-forward"]
        if value not in VALID_BODY_DIFFSERV_FORWARD:
            return (
                False,
                f"Invalid value for 'diffserv-forward'='{value}'. Must be one of: {', '.join(VALID_BODY_DIFFSERV_FORWARD)}",
            )
    if "diffserv-reverse" in payload:
        value = payload["diffserv-reverse"]
        if value not in VALID_BODY_DIFFSERV_REVERSE:
            return (
                False,
                f"Invalid value for 'diffserv-reverse'='{value}'. Must be one of: {', '.join(VALID_BODY_DIFFSERV_REVERSE)}",
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
    "endpoint": "firewall/shaping_policy",
    "category": "cmdb",
    "api_path": "firewall/shaping-policy",
    "mkey": "id",
    "mkey_type": "integer",
    "help": "Configure shaping policies.",
    "total_fields": 46,
    "required_fields_count": 6,
    "fields_with_defaults_count": 22,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
