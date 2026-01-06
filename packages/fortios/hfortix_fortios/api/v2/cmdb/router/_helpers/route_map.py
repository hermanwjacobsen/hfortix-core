"""Validation helpers for router/route_map - Auto-generated"""

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
    "name",  # Name.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "comments": "",
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
    "name": "string",  # Name.
    "comments": "string",  # Optional comments.
    "rule": "string",  # Rule.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "Name.",
    "comments": "Optional comments.",
    "rule": "Rule.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 35},
    "comments": {"type": "string", "max_length": 127},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "rule": {
        "id": {
            "type": "integer",
            "help": "Rule ID.",
            "required": True,
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "action": {
            "type": "option",
            "help": "Action.",
            "default": "permit",
            "options": [{"help": "Permit.", "label": "Permit", "name": "permit"}, {"help": "Deny.", "label": "Deny", "name": "deny"}],
        },
        "match-as-path": {
            "type": "string",
            "help": "Match BGP AS path list.",
            "default": "",
            "max_length": 35,
        },
        "match-community": {
            "type": "string",
            "help": "Match BGP community list.",
            "default": "",
            "max_length": 35,
        },
        "match-extcommunity": {
            "type": "string",
            "help": "Match BGP extended community list.",
            "default": "",
            "max_length": 35,
        },
        "match-community-exact": {
            "type": "option",
            "help": "Enable/disable exact matching of communities.",
            "default": "disable",
            "options": [{"help": "Enable exact matching of communities.", "label": "Enable", "name": "enable"}, {"help": "Disable exact matching of communities.", "label": "Disable", "name": "disable"}],
        },
        "match-extcommunity-exact": {
            "type": "option",
            "help": "Enable/disable exact matching of extended communities.",
            "default": "disable",
            "options": [{"help": "Enable exact matching of extended communities.", "label": "Enable", "name": "enable"}, {"help": "Disable exact matching of extended communities.", "label": "Disable", "name": "disable"}],
        },
        "match-origin": {
            "type": "option",
            "help": "Match BGP origin code.",
            "default": "none",
            "options": [{"help": "None.", "label": "None", "name": "none"}, {"help": "Remote EGP.", "label": "Egp", "name": "egp"}, {"help": "Local IGP.", "label": "Igp", "name": "igp"}, {"help": "Unknown heritage.", "label": "Incomplete", "name": "incomplete"}],
        },
        "match-interface": {
            "type": "string",
            "help": "Match interface configuration.",
            "default": "",
            "max_length": 15,
        },
        "match-ip-address": {
            "type": "string",
            "help": "Match IP address permitted by access-list or prefix-list.",
            "default": "",
            "max_length": 35,
        },
        "match-ip6-address": {
            "type": "string",
            "help": "Match IPv6 address permitted by access-list6 or prefix-list6.",
            "default": "",
            "max_length": 35,
        },
        "match-ip-nexthop": {
            "type": "string",
            "help": "Match next hop IP address passed by access-list or prefix-list.",
            "default": "",
            "max_length": 35,
        },
        "match-ip6-nexthop": {
            "type": "string",
            "help": "Match next hop IPv6 address passed by access-list6 or prefix-list6.",
            "default": "",
            "max_length": 35,
        },
        "match-metric": {
            "type": "integer",
            "help": "Match metric for redistribute routes.",
            "default": "",
            "min_value": 0,
            "max_value": 4294967295,
        },
        "match-route-type": {
            "type": "option",
            "help": "Match route type.",
            "default": "",
            "options": [{"help": "External type 1.", "label": "External Type1", "name": "external-type1"}, {"help": "External type 2.", "label": "External Type2", "name": "external-type2"}, {"help": "No type specified.", "label": "None", "name": "none"}],
        },
        "match-tag": {
            "type": "integer",
            "help": "Match tag.",
            "default": "",
            "min_value": 0,
            "max_value": 4294967295,
        },
        "match-vrf": {
            "type": "integer",
            "help": "Match VRF ID.",
            "default": "",
            "min_value": 0,
            "max_value": 511,
        },
        "match-suppress": {
            "type": "option",
            "help": "Enable/disable matching of suppressed original neighbor.",
            "default": "disable",
            "options": [{"help": "Enable matching of suppressed original neighbor.", "label": "Enable", "name": "enable"}, {"help": "Disable matching of suppressed original neighbor.", "label": "Disable", "name": "disable"}],
        },
        "set-aggregator-as": {
            "type": "integer",
            "help": "BGP aggregator AS.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "set-aggregator-ip": {
            "type": "ipv4-address-any",
            "help": "BGP aggregator IP.",
            "required": True,
            "default": "0.0.0.0",
        },
        "set-aspath-action": {
            "type": "option",
            "help": "Specify preferred action of set-aspath.",
            "default": "prepend",
            "options": [{"help": "Prepend.", "label": "Prepend", "name": "prepend"}, {"help": "Replace.", "label": "Replace", "name": "replace"}],
        },
        "set-aspath": {
            "type": "string",
            "help": "Prepend BGP AS path attribute.",
        },
        "set-atomic-aggregate": {
            "type": "option",
            "help": "Enable/disable BGP atomic aggregate attribute.",
            "default": "disable",
            "options": [{"help": "Enable BGP atomic aggregate attribute.", "label": "Enable", "name": "enable"}, {"help": "Disable BGP atomic aggregate attribute.", "label": "Disable", "name": "disable"}],
        },
        "set-community-delete": {
            "type": "string",
            "help": "Delete communities matching community list.",
            "default": "",
            "max_length": 35,
        },
        "set-community": {
            "type": "string",
            "help": "BGP community attribute.",
        },
        "set-community-additive": {
            "type": "option",
            "help": "Enable/disable adding set-community to existing community.",
            "default": "disable",
            "options": [{"help": "Enable adding set-community to existing community.", "label": "Enable", "name": "enable"}, {"help": "Disable adding set-community to existing community.", "label": "Disable", "name": "disable"}],
        },
        "set-dampening-reachability-half-life": {
            "type": "integer",
            "help": "Reachability half-life time for the penalty (1 - 45 min, 0 = unset).",
            "default": 0,
            "min_value": 0,
            "max_value": 45,
        },
        "set-dampening-reuse": {
            "type": "integer",
            "help": "Value to start reusing a route (1 - 20000, 0 = unset).",
            "default": 0,
            "min_value": 0,
            "max_value": 20000,
        },
        "set-dampening-suppress": {
            "type": "integer",
            "help": "Value to start suppressing a route (1 - 20000, 0 = unset).",
            "default": 0,
            "min_value": 0,
            "max_value": 20000,
        },
        "set-dampening-max-suppress": {
            "type": "integer",
            "help": "Maximum duration to suppress a route (1 - 255 min, 0 = unset).",
            "default": 0,
            "min_value": 0,
            "max_value": 255,
        },
        "set-dampening-unreachability-half-life": {
            "type": "integer",
            "help": "Unreachability Half-life time for the penalty (1 - 45 min, 0 = unset).",
            "default": 0,
            "min_value": 0,
            "max_value": 45,
        },
        "set-extcommunity-rt": {
            "type": "string",
            "help": "Route Target extended community.",
        },
        "set-extcommunity-soo": {
            "type": "string",
            "help": "Site-of-Origin extended community.",
        },
        "set-ip-nexthop": {
            "type": "ipv4-address",
            "help": "IP address of next hop.",
            "default": "",
        },
        "set-ip-prefsrc": {
            "type": "ipv4-address",
            "help": "IP address of preferred source.",
            "default": "",
        },
        "set-vpnv4-nexthop": {
            "type": "ipv4-address",
            "help": "IP address of VPNv4 next-hop.",
            "default": "",
        },
        "set-ip6-nexthop": {
            "type": "ipv6-address",
            "help": "IPv6 global address of next hop.",
            "default": "",
        },
        "set-ip6-nexthop-local": {
            "type": "ipv6-address",
            "help": "IPv6 local address of next hop.",
            "default": "",
        },
        "set-vpnv6-nexthop": {
            "type": "ipv6-address",
            "help": "IPv6 global address of VPNv6 next-hop.",
            "default": "",
        },
        "set-vpnv6-nexthop-local": {
            "type": "ipv6-address",
            "help": "IPv6 link-local address of VPNv6 next-hop.",
            "default": "",
        },
        "set-local-preference": {
            "type": "integer",
            "help": "BGP local preference path attribute.",
            "default": "",
            "min_value": 0,
            "max_value": 4294967295,
        },
        "set-metric": {
            "type": "integer",
            "help": "Metric value.",
            "default": "",
            "min_value": 0,
            "max_value": 4294967295,
        },
        "set-metric-type": {
            "type": "option",
            "help": "Metric type.",
            "default": "",
            "options": [{"help": "External type 1.", "label": "External Type1", "name": "external-type1"}, {"help": "External type 2.", "label": "External Type2", "name": "external-type2"}, {"help": "No type specified.", "label": "None", "name": "none"}],
        },
        "set-originator-id": {
            "type": "ipv4-address-any",
            "help": "BGP originator ID attribute.",
            "default": "",
        },
        "set-origin": {
            "type": "option",
            "help": "BGP origin code.",
            "default": "none",
            "options": [{"help": "None.", "label": "None", "name": "none"}, {"help": "Remote EGP.", "label": "Egp", "name": "egp"}, {"help": "Local IGP.", "label": "Igp", "name": "igp"}, {"help": "Unknown heritage.", "label": "Incomplete", "name": "incomplete"}],
        },
        "set-tag": {
            "type": "integer",
            "help": "Tag value.",
            "default": "",
            "min_value": 0,
            "max_value": 4294967295,
        },
        "set-weight": {
            "type": "integer",
            "help": "BGP weight for routing table.",
            "default": "",
            "min_value": 0,
            "max_value": 4294967295,
        },
        "set-route-tag": {
            "type": "integer",
            "help": "Route tag for routing table.",
            "default": "",
            "min_value": 0,
            "max_value": 4294967295,
        },
        "set-priority": {
            "type": "integer",
            "help": "Priority for routing table.",
            "default": "",
            "min_value": 1,
            "max_value": 65535,
        },
    },
}


# Valid enum values from API documentation
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_router_route_map_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for router/route_map."""
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
    """Validate required fields for router/route_map."""
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


def validate_router_route_map_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new router/route_map object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_router_route_map_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update router/route_map."""
    # Step 1: Validate enum values

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
    "endpoint": "router/route_map",
    "category": "cmdb",
    "api_path": "router/route-map",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure route maps.",
    "total_fields": 3,
    "required_fields_count": 1,
    "fields_with_defaults_count": 2,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
