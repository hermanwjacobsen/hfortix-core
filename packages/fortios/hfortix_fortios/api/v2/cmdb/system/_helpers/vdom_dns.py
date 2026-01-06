"""Validation helpers for system/vdom_dns - Auto-generated"""

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
    "interface",  # Specify outgoing interface to reach server.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "vdom-dns": "disable",
    "primary": "0.0.0.0",
    "secondary": "0.0.0.0",
    "protocol": "cleartext",
    "ssl-certificate": "",
    "ip6-primary": "::",
    "ip6-secondary": "::",
    "source-ip": "0.0.0.0",
    "source-ip-interface": "",
    "interface-select-method": "auto",
    "interface": "",
    "vrf-select": 0,
    "server-select-method": "least-rtt",
    "alt-primary": "0.0.0.0",
    "alt-secondary": "0.0.0.0",
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
    "vdom-dns": "option",  # Enable/disable configuring DNS servers for the current VDOM.
    "primary": "ipv4-address",  # Primary DNS server IP address for the VDOM.
    "secondary": "ipv4-address",  # Secondary DNS server IP address for the VDOM.
    "protocol": "option",  # DNS transport protocols.
    "ssl-certificate": "string",  # Name of local certificate for SSL connections.
    "server-hostname": "string",  # DNS server host name list.
    "ip6-primary": "ipv6-address",  # Primary IPv6 DNS server IP address for the VDOM.
    "ip6-secondary": "ipv6-address",  # Secondary IPv6 DNS server IP address for the VDOM.
    "source-ip": "ipv4-address",  # Source IP for communications with the DNS server.
    "source-ip-interface": "string",  # IP address of the specified interface as the source IP addre
    "interface-select-method": "option",  # Specify how to select outgoing interface to reach server.
    "interface": "string",  # Specify outgoing interface to reach server.
    "vrf-select": "integer",  # VRF ID used for connection to server.
    "server-select-method": "option",  # Specify how configured servers are prioritized.
    "alt-primary": "ipv4-address",  # Alternate primary DNS server. This is not used as a failover
    "alt-secondary": "ipv4-address",  # Alternate secondary DNS server. This is not used as a failov
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "vdom-dns": "Enable/disable configuring DNS servers for the current VDOM.",
    "primary": "Primary DNS server IP address for the VDOM.",
    "secondary": "Secondary DNS server IP address for the VDOM.",
    "protocol": "DNS transport protocols.",
    "ssl-certificate": "Name of local certificate for SSL connections.",
    "server-hostname": "DNS server host name list.",
    "ip6-primary": "Primary IPv6 DNS server IP address for the VDOM.",
    "ip6-secondary": "Secondary IPv6 DNS server IP address for the VDOM.",
    "source-ip": "Source IP for communications with the DNS server.",
    "source-ip-interface": "IP address of the specified interface as the source IP address.",
    "interface-select-method": "Specify how to select outgoing interface to reach server.",
    "interface": "Specify outgoing interface to reach server.",
    "vrf-select": "VRF ID used for connection to server.",
    "server-select-method": "Specify how configured servers are prioritized.",
    "alt-primary": "Alternate primary DNS server. This is not used as a failover DNS server.",
    "alt-secondary": "Alternate secondary DNS server. This is not used as a failover DNS server.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "ssl-certificate": {"type": "string", "max_length": 35},
    "source-ip-interface": {"type": "string", "max_length": 15},
    "interface": {"type": "string", "max_length": 15},
    "vrf-select": {"type": "integer", "min": 0, "max": 511},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "server-hostname": {
        "hostname": {
            "type": "string",
            "help": "DNS server host name list separated by space (maximum 4 domains).",
            "required": True,
            "default": "",
            "max_length": 127,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_VDOM_DNS = [
    "enable",  # Enable configuring DNS servers for the current VDOM.
    "disable",  # Disable configuring DNS servers for the current VDOM.
]
VALID_BODY_PROTOCOL = [
    "cleartext",  # DNS over UDP/53, DNS over TCP/53.
    "dot",  # DNS over TLS/853.
    "doh",  # DNS over HTTPS/443.
]
VALID_BODY_INTERFACE_SELECT_METHOD = [
    "auto",  # Set outgoing interface automatically.
    "sdwan",  # Set outgoing interface by SD-WAN or policy routing rules.
    "specify",  # Set outgoing interface manually.
]
VALID_BODY_SERVER_SELECT_METHOD = [
    "least-rtt",  # Select servers based on least round trip time.
    "failover",  # Select servers based on the order they are configured.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_system_vdom_dns_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for system/vdom_dns."""
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
    """Validate required fields for system/vdom_dns."""
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


def validate_system_vdom_dns_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new system/vdom_dns object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "vdom-dns" in payload:
        value = payload["vdom-dns"]
        if value not in VALID_BODY_VDOM_DNS:
            desc = FIELD_DESCRIPTIONS.get("vdom-dns", "")
            error_msg = f"Invalid value for 'vdom-dns': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_VDOM_DNS)}"
            error_msg += f"\n  → Example: vdom-dns='{{ VALID_BODY_VDOM_DNS[0] }}'"
            return (False, error_msg)
    if "protocol" in payload:
        value = payload["protocol"]
        if value not in VALID_BODY_PROTOCOL:
            desc = FIELD_DESCRIPTIONS.get("protocol", "")
            error_msg = f"Invalid value for 'protocol': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PROTOCOL)}"
            error_msg += f"\n  → Example: protocol='{{ VALID_BODY_PROTOCOL[0] }}'"
            return (False, error_msg)
    if "interface-select-method" in payload:
        value = payload["interface-select-method"]
        if value not in VALID_BODY_INTERFACE_SELECT_METHOD:
            desc = FIELD_DESCRIPTIONS.get("interface-select-method", "")
            error_msg = f"Invalid value for 'interface-select-method': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_INTERFACE_SELECT_METHOD)}"
            error_msg += f"\n  → Example: interface-select-method='{{ VALID_BODY_INTERFACE_SELECT_METHOD[0] }}'"
            return (False, error_msg)
    if "server-select-method" in payload:
        value = payload["server-select-method"]
        if value not in VALID_BODY_SERVER_SELECT_METHOD:
            desc = FIELD_DESCRIPTIONS.get("server-select-method", "")
            error_msg = f"Invalid value for 'server-select-method': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SERVER_SELECT_METHOD)}"
            error_msg += f"\n  → Example: server-select-method='{{ VALID_BODY_SERVER_SELECT_METHOD[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_system_vdom_dns_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update system/vdom_dns."""
    # Step 1: Validate enum values
    if "vdom-dns" in payload:
        value = payload["vdom-dns"]
        if value not in VALID_BODY_VDOM_DNS:
            return (
                False,
                f"Invalid value for 'vdom-dns'='{value}'. Must be one of: {', '.join(VALID_BODY_VDOM_DNS)}",
            )
    if "protocol" in payload:
        value = payload["protocol"]
        if value not in VALID_BODY_PROTOCOL:
            return (
                False,
                f"Invalid value for 'protocol'='{value}'. Must be one of: {', '.join(VALID_BODY_PROTOCOL)}",
            )
    if "interface-select-method" in payload:
        value = payload["interface-select-method"]
        if value not in VALID_BODY_INTERFACE_SELECT_METHOD:
            return (
                False,
                f"Invalid value for 'interface-select-method'='{value}'. Must be one of: {', '.join(VALID_BODY_INTERFACE_SELECT_METHOD)}",
            )
    if "server-select-method" in payload:
        value = payload["server-select-method"]
        if value not in VALID_BODY_SERVER_SELECT_METHOD:
            return (
                False,
                f"Invalid value for 'server-select-method'='{value}'. Must be one of: {', '.join(VALID_BODY_SERVER_SELECT_METHOD)}",
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
    "endpoint": "system/vdom_dns",
    "category": "cmdb",
    "api_path": "system/vdom-dns",
    "help": "Configure DNS servers for a non-management VDOM.",
    "total_fields": 16,
    "required_fields_count": 1,
    "fields_with_defaults_count": 15,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
