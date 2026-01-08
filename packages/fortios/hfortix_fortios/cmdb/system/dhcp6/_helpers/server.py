"""Validation helpers for system/dhcp6/server - Auto-generated"""

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

# Import central validation functions (avoid duplication across 1,062 files)
from hfortix_fortios._helpers.validation import (
    validate_required_fields as _validate_required_fields,
    validate_enum_field as _validate_enum_field,
    validate_query_parameter as _validate_query_parameter,
)

# ============================================================================
# Required Fields Validation
# Auto-generated from schema
# ============================================================================

# ⚠️  IMPORTANT: FortiOS schemas have known issues with required field marking:

# Do NOT use this list for strict validation - test with the actual FortiOS API!

# Fields marked as required (after filtering false positives)
REQUIRED_FIELDS = [
    "interface",  # DHCP server can assign IP configurations to clients connected to this interface.
    "upstream-interface",  # Interface name from where delegated information is provided.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "id": 0,
    "status": "enable",
    "rapid-commit": "disable",
    "lease-time": 604800,
    "dns-service": "specify",
    "dns-search-list": "specify",
    "dns-server1": "::",
    "dns-server2": "::",
    "dns-server3": "::",
    "dns-server4": "::",
    "domain": "",
    "subnet": "::/0",
    "interface": "",
    "delegated-prefix-route": "disable",
    "upstream-interface": "",
    "delegated-prefix-iaid": 0,
    "ip-mode": "range",
    "prefix-mode": "dhcp6",
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
    "id": "integer",  # ID.
    "status": "option",  # Enable/disable this DHCPv6 configuration.
    "rapid-commit": "option",  # Enable/disable allow/disallow rapid commit.
    "lease-time": "integer",  # Lease time in seconds, 0 means unlimited.
    "dns-service": "option",  # Options for assigning DNS servers to DHCPv6 clients.
    "dns-search-list": "option",  # DNS search list options.
    "dns-server1": "ipv6-address",  # DNS server 1.
    "dns-server2": "ipv6-address",  # DNS server 2.
    "dns-server3": "ipv6-address",  # DNS server 3.
    "dns-server4": "ipv6-address",  # DNS server 4.
    "domain": "string",  # Domain name suffix for the IP addresses that the DHCP server
    "subnet": "ipv6-prefix",  # Subnet or subnet-id if the IP mode is delegated.
    "interface": "string",  # DHCP server can assign IP configurations to clients connecte
    "delegated-prefix-route": "option",  # Enable/disable automatically adding of routing for delegated
    "options": "string",  # DHCPv6 options.
    "upstream-interface": "string",  # Interface name from where delegated information is provided.
    "delegated-prefix-iaid": "integer",  # IAID of obtained delegated-prefix from the upstream interfac
    "ip-mode": "option",  # Method used to assign client IP.
    "prefix-mode": "option",  # Assigning a prefix from a DHCPv6 client or RA.
    "prefix-range": "string",  # DHCP prefix configuration.
    "ip-range": "string",  # DHCP IP range configuration.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "id": "ID.",
    "status": "Enable/disable this DHCPv6 configuration.",
    "rapid-commit": "Enable/disable allow/disallow rapid commit.",
    "lease-time": "Lease time in seconds, 0 means unlimited.",
    "dns-service": "Options for assigning DNS servers to DHCPv6 clients.",
    "dns-search-list": "DNS search list options.",
    "dns-server1": "DNS server 1.",
    "dns-server2": "DNS server 2.",
    "dns-server3": "DNS server 3.",
    "dns-server4": "DNS server 4.",
    "domain": "Domain name suffix for the IP addresses that the DHCP server assigns to clients.",
    "subnet": "Subnet or subnet-id if the IP mode is delegated.",
    "interface": "DHCP server can assign IP configurations to clients connected to this interface.",
    "delegated-prefix-route": "Enable/disable automatically adding of routing for delegated prefix.",
    "options": "DHCPv6 options.",
    "upstream-interface": "Interface name from where delegated information is provided.",
    "delegated-prefix-iaid": "IAID of obtained delegated-prefix from the upstream interface.",
    "ip-mode": "Method used to assign client IP.",
    "prefix-mode": "Assigning a prefix from a DHCPv6 client or RA.",
    "prefix-range": "DHCP prefix configuration.",
    "ip-range": "DHCP IP range configuration.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "id": {"type": "integer", "min": 0, "max": 4294967295},
    "lease-time": {"type": "integer", "min": 300, "max": 8640000},
    "domain": {"type": "string", "max_length": 35},
    "interface": {"type": "string", "max_length": 15},
    "upstream-interface": {"type": "string", "max_length": 15},
    "delegated-prefix-iaid": {"type": "integer", "min": 0, "max": 4294967295},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "options": {
        "id": {
            "type": "integer",
            "help": "ID.",
            "required": True,
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "code": {
            "type": "integer",
            "help": "DHCPv6 option code.",
            "required": True,
            "default": 0,
            "min_value": 0,
            "max_value": 255,
        },
        "type": {
            "type": "option",
            "help": "DHCPv6 option type.",
            "default": "hex",
            "options": ["hex", "string", "ip6", "fqdn"],
        },
        "value": {
            "type": "string",
            "help": "DHCPv6 option value (hexadecimal value must be even).",
            "default": "",
            "max_length": 312,
        },
        "ip6": {
            "type": "user",
            "help": "DHCP option IP6s.",
            "default": "",
        },
        "vci-match": {
            "type": "option",
            "help": "Enable/disable vendor class option matching. When enabled only DHCP requests with a matching VCI are served with this option.",
            "default": "disable",
            "options": ["disable", "enable"],
        },
        "vci-string": {
            "type": "string",
            "help": "One or more VCI strings in quotes separated by spaces.",
        },
    },
    "prefix-range": {
        "id": {
            "type": "integer",
            "help": "ID.",
            "required": True,
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "start-prefix": {
            "type": "ipv6-address",
            "help": "Start of prefix range.",
            "required": True,
            "default": "::",
        },
        "end-prefix": {
            "type": "ipv6-address",
            "help": "End of prefix range.",
            "required": True,
            "default": "::",
        },
        "prefix-length": {
            "type": "integer",
            "help": "Prefix length.",
            "required": True,
            "default": 0,
            "min_value": 1,
            "max_value": 128,
        },
    },
    "ip-range": {
        "id": {
            "type": "integer",
            "help": "ID.",
            "required": True,
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "start-ip": {
            "type": "ipv6-address",
            "help": "Start of IP range.",
            "required": True,
            "default": "::",
        },
        "end-ip": {
            "type": "ipv6-address",
            "help": "End of IP range.",
            "required": True,
            "default": "::",
        },
        "vci-match": {
            "type": "option",
            "help": "Enable/disable vendor class option matching. When enabled only DHCP requests with a matching VC are served with this range.",
            "default": "disable",
            "options": ["disable", "enable"],
        },
        "vci-string": {
            "type": "string",
            "help": "One or more VCI strings in quotes separated by spaces.",
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_STATUS = [
    "disable",
    "enable",
]
VALID_BODY_RAPID_COMMIT = [
    "disable",
    "enable",
]
VALID_BODY_DNS_SERVICE = [
    "delegated",
    "default",
    "specify",
]
VALID_BODY_DNS_SEARCH_LIST = [
    "delegated",
    "specify",
]
VALID_BODY_DELEGATED_PREFIX_ROUTE = [
    "disable",
    "enable",
]
VALID_BODY_IP_MODE = [
    "range",
    "delegated",
]
VALID_BODY_PREFIX_MODE = [
    "dhcp6",
    "ra",
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_system_dhcp6_server_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for system/dhcp6/server."""
    # Validate query parameters using central function
    if "action" in params:
        is_valid, error = _validate_query_parameter(
            "action",
            params.get("action"),
            VALID_QUERY_ACTION
        )
        if not is_valid:
            return (False, error)

    return (True, None)


# ============================================================================
# POST Validation
# ============================================================================


def validate_system_dhcp6_server_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new system/dhcp6/server object."""
    # Step 1: Validate required fields using central function
    is_valid, error = _validate_required_fields(
        payload,
        REQUIRED_FIELDS,
        FIELD_DESCRIPTIONS
    )
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values using central function
    if "status" in payload:
        is_valid, error = _validate_enum_field(
            "status",
            payload["status"],
            VALID_BODY_STATUS,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "rapid-commit" in payload:
        is_valid, error = _validate_enum_field(
            "rapid-commit",
            payload["rapid-commit"],
            VALID_BODY_RAPID_COMMIT,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "dns-service" in payload:
        is_valid, error = _validate_enum_field(
            "dns-service",
            payload["dns-service"],
            VALID_BODY_DNS_SERVICE,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "dns-search-list" in payload:
        is_valid, error = _validate_enum_field(
            "dns-search-list",
            payload["dns-search-list"],
            VALID_BODY_DNS_SEARCH_LIST,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "delegated-prefix-route" in payload:
        is_valid, error = _validate_enum_field(
            "delegated-prefix-route",
            payload["delegated-prefix-route"],
            VALID_BODY_DELEGATED_PREFIX_ROUTE,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "ip-mode" in payload:
        is_valid, error = _validate_enum_field(
            "ip-mode",
            payload["ip-mode"],
            VALID_BODY_IP_MODE,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "prefix-mode" in payload:
        is_valid, error = _validate_enum_field(
            "prefix-mode",
            payload["prefix-mode"],
            VALID_BODY_PREFIX_MODE,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_system_dhcp6_server_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update system/dhcp6/server."""
    # Validate enum values using central function
    if "status" in payload:
        is_valid, error = _validate_enum_field(
            "status",
            payload["status"],
            VALID_BODY_STATUS,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "rapid-commit" in payload:
        is_valid, error = _validate_enum_field(
            "rapid-commit",
            payload["rapid-commit"],
            VALID_BODY_RAPID_COMMIT,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "dns-service" in payload:
        is_valid, error = _validate_enum_field(
            "dns-service",
            payload["dns-service"],
            VALID_BODY_DNS_SERVICE,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "dns-search-list" in payload:
        is_valid, error = _validate_enum_field(
            "dns-search-list",
            payload["dns-search-list"],
            VALID_BODY_DNS_SEARCH_LIST,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "delegated-prefix-route" in payload:
        is_valid, error = _validate_enum_field(
            "delegated-prefix-route",
            payload["delegated-prefix-route"],
            VALID_BODY_DELEGATED_PREFIX_ROUTE,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "ip-mode" in payload:
        is_valid, error = _validate_enum_field(
            "ip-mode",
            payload["ip-mode"],
            VALID_BODY_IP_MODE,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "prefix-mode" in payload:
        is_valid, error = _validate_enum_field(
            "prefix-mode",
            payload["prefix-mode"],
            VALID_BODY_PREFIX_MODE,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)

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
    "endpoint": "system/dhcp6/server",
    "category": "cmdb",
    "api_path": "system.dhcp6/server",
    "mkey": "id",
    "mkey_type": "integer",
    "help": "Configure DHCPv6 servers.",
    "total_fields": 21,
    "required_fields_count": 2,
    "fields_with_defaults_count": 18,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
