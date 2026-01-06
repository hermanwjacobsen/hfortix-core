"""Validation helpers for system/dns_database - Auto-generated"""

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
    "name",  # Zone name.
    "domain",  # Domain name.
    "dns-entry",  # DNS entry.
    "interface",  # Specify outgoing interface to reach server.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "status": "enable",
    "domain": "",
    "allow-transfer": "",
    "type": "primary",
    "view": "shadow",
    "ip-primary": "0.0.0.0",
    "primary-name": "dns",
    "contact": "host",
    "ttl": 86400,
    "authoritative": "enable",
    "forwarder": "",
    "forwarder6": "::",
    "source-ip": "0.0.0.0",
    "source-ip6": "::",
    "source-ip-interface": "",
    "rr-max": 16384,
    "interface-select-method": "auto",
    "interface": "",
    "vrf-select": 0,
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
    "name": "string",  # Zone name.
    "status": "option",  # Enable/disable this DNS zone.
    "domain": "string",  # Domain name.
    "allow-transfer": "user",  # DNS zone transfer IP address list.
    "type": "option",  # Zone type (primary to manage entries directly, secondary to 
    "view": "option",  # Zone view (public to serve public clients, shadow to serve i
    "ip-primary": "ipv4-address-any",  # IP address of primary DNS server. Entries in this primary DN
    "primary-name": "string",  # Domain name of the default DNS server for this zone.
    "contact": "string",  # Email address of the administrator for this zone. You can sp
    "ttl": "integer",  # Default time-to-live value for the entries of this DNS zone 
    "authoritative": "option",  # Enable/disable authoritative zone.
    "forwarder": "user",  # DNS zone forwarder IP address list.
    "forwarder6": "ipv6-address",  # Forwarder IPv6 address.
    "source-ip": "ipv4-address",  # Source IP for forwarding to DNS server.
    "source-ip6": "ipv6-address",  # IPv6 source IP address for forwarding to DNS server.
    "source-ip-interface": "string",  # IP address of the specified interface as the source IP addre
    "rr-max": "integer",  # Maximum number of resource records (10 - 65536, 0 means infi
    "dns-entry": "string",  # DNS entry.
    "interface-select-method": "option",  # Specify how to select outgoing interface to reach server.
    "interface": "string",  # Specify outgoing interface to reach server.
    "vrf-select": "integer",  # VRF ID used for connection to server.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "Zone name.",
    "status": "Enable/disable this DNS zone.",
    "domain": "Domain name.",
    "allow-transfer": "DNS zone transfer IP address list.",
    "type": "Zone type (primary to manage entries directly, secondary to import entries from other zones).",
    "view": "Zone view (public to serve public clients, shadow to serve internal clients).",
    "ip-primary": "IP address of primary DNS server. Entries in this primary DNS server and imported into the DNS zone.",
    "primary-name": "Domain name of the default DNS server for this zone.",
    "contact": "Email address of the administrator for this zone. You can specify only the username, such as admin or the full email address, such as admin@test.com When using only a username, the domain of the email will be this zone.",
    "ttl": "Default time-to-live value for the entries of this DNS zone (0 - 2147483647 sec, default = 86400).",
    "authoritative": "Enable/disable authoritative zone.",
    "forwarder": "DNS zone forwarder IP address list.",
    "forwarder6": "Forwarder IPv6 address.",
    "source-ip": "Source IP for forwarding to DNS server.",
    "source-ip6": "IPv6 source IP address for forwarding to DNS server.",
    "source-ip-interface": "IP address of the specified interface as the source IP address.",
    "rr-max": "Maximum number of resource records (10 - 65536, 0 means infinite).",
    "dns-entry": "DNS entry.",
    "interface-select-method": "Specify how to select outgoing interface to reach server.",
    "interface": "Specify outgoing interface to reach server.",
    "vrf-select": "VRF ID used for connection to server.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 35},
    "domain": {"type": "string", "max_length": 255},
    "primary-name": {"type": "string", "max_length": 255},
    "contact": {"type": "string", "max_length": 255},
    "ttl": {"type": "integer", "min": 0, "max": 2147483647},
    "source-ip-interface": {"type": "string", "max_length": 15},
    "rr-max": {"type": "integer", "min": 10, "max": 65536},
    "interface": {"type": "string", "max_length": 15},
    "vrf-select": {"type": "integer", "min": 0, "max": 511},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "dns-entry": {
        "id": {
            "type": "integer",
            "help": "DNS entry ID.",
            "required": True,
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "status": {
            "type": "option",
            "help": "Enable/disable resource record status.",
            "default": "enable",
            "options": [{"help": "Enable resource record status.", "label": "Enable", "name": "enable"}, {"help": "Disable resource record status.", "label": "Disable", "name": "disable"}],
        },
        "type": {
            "type": "option",
            "help": "Resource record type.",
            "required": True,
            "default": "A",
            "options": [{"help": "Host type.", "label": "A", "name": "A"}, {"help": "Name server type.", "label": "Ns", "name": "NS"}, {"help": "Canonical name type.", "label": "Cname", "name": "CNAME"}, {"help": "Mail exchange type.", "label": "Mx", "name": "MX"}, {"help": "IPv6 host type.", "label": "Aaaa", "name": "AAAA"}, {"help": "Pointer type.", "label": "Ptr", "name": "PTR"}, {"help": "IPv6 pointer type.", "label": "Ptr V6", "name": "PTR_V6"}],
        },
        "ttl": {
            "type": "integer",
            "help": "Time-to-live for this entry (0 to 2147483647 sec, default = 0).",
            "default": 0,
            "min_value": 0,
            "max_value": 2147483647,
        },
        "preference": {
            "type": "integer",
            "help": "DNS entry preference (0 - 65535, highest preference = 0, default = 10).",
            "default": 10,
            "min_value": 0,
            "max_value": 65535,
        },
        "ip": {
            "type": "ipv4-address-any",
            "help": "IPv4 address of the host.",
            "default": "0.0.0.0",
        },
        "ipv6": {
            "type": "ipv6-address",
            "help": "IPv6 address of the host.",
            "default": "::",
        },
        "hostname": {
            "type": "string",
            "help": "Name of the host.",
            "required": True,
            "default": "",
            "max_length": 255,
        },
        "canonical-name": {
            "type": "string",
            "help": "Canonical name of the host.",
            "default": "",
            "max_length": 255,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_STATUS = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_TYPE = [
    "primary",  # Primary DNS zone, to manage entries directly.
    "secondary",  # Secondary DNS zone, to import entries from other DNS zones.
]
VALID_BODY_VIEW = [
    "shadow",  # Shadow DNS zone to serve internal clients.
    "public",  # Public DNS zone to serve public clients.
    "shadow-ztna",  # implicit DNS zone for ztna dox tunnel.
    "proxy",  # Shadow DNS zone for internal proxy.
]
VALID_BODY_AUTHORITATIVE = [
    "enable",  # Enable authoritative zone.
    "disable",  # Disable authoritative zone.
]
VALID_BODY_INTERFACE_SELECT_METHOD = [
    "auto",  # Set outgoing interface automatically.
    "sdwan",  # Set outgoing interface by SD-WAN or policy routing rules.
    "specify",  # Set outgoing interface manually.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_system_dns_database_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for system/dns_database."""
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
    """Validate required fields for system/dns_database."""
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


def validate_system_dns_database_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new system/dns_database object."""
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
    if "type" in payload:
        value = payload["type"]
        if value not in VALID_BODY_TYPE:
            desc = FIELD_DESCRIPTIONS.get("type", "")
            error_msg = f"Invalid value for 'type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_TYPE)}"
            error_msg += f"\n  → Example: type='{{ VALID_BODY_TYPE[0] }}'"
            return (False, error_msg)
    if "view" in payload:
        value = payload["view"]
        if value not in VALID_BODY_VIEW:
            desc = FIELD_DESCRIPTIONS.get("view", "")
            error_msg = f"Invalid value for 'view': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_VIEW)}"
            error_msg += f"\n  → Example: view='{{ VALID_BODY_VIEW[0] }}'"
            return (False, error_msg)
    if "authoritative" in payload:
        value = payload["authoritative"]
        if value not in VALID_BODY_AUTHORITATIVE:
            desc = FIELD_DESCRIPTIONS.get("authoritative", "")
            error_msg = f"Invalid value for 'authoritative': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTHORITATIVE)}"
            error_msg += f"\n  → Example: authoritative='{{ VALID_BODY_AUTHORITATIVE[0] }}'"
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

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_system_dns_database_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update system/dns_database."""
    # Step 1: Validate enum values
    if "status" in payload:
        value = payload["status"]
        if value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid value for 'status'='{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )
    if "type" in payload:
        value = payload["type"]
        if value not in VALID_BODY_TYPE:
            return (
                False,
                f"Invalid value for 'type'='{value}'. Must be one of: {', '.join(VALID_BODY_TYPE)}",
            )
    if "view" in payload:
        value = payload["view"]
        if value not in VALID_BODY_VIEW:
            return (
                False,
                f"Invalid value for 'view'='{value}'. Must be one of: {', '.join(VALID_BODY_VIEW)}",
            )
    if "authoritative" in payload:
        value = payload["authoritative"]
        if value not in VALID_BODY_AUTHORITATIVE:
            return (
                False,
                f"Invalid value for 'authoritative'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTHORITATIVE)}",
            )
    if "interface-select-method" in payload:
        value = payload["interface-select-method"]
        if value not in VALID_BODY_INTERFACE_SELECT_METHOD:
            return (
                False,
                f"Invalid value for 'interface-select-method'='{value}'. Must be one of: {', '.join(VALID_BODY_INTERFACE_SELECT_METHOD)}",
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
    "endpoint": "system/dns_database",
    "category": "cmdb",
    "api_path": "system/dns-database",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure DNS databases.",
    "total_fields": 21,
    "required_fields_count": 4,
    "fields_with_defaults_count": 20,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
