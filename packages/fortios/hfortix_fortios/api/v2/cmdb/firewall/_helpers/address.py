"""Validation helpers for firewall/address - Auto-generated"""

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
    "interface",  # Name of interface whose IP address is to be used.
    "filter",  # Match criteria filter.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "uuid": "00000000-0000-0000-0000-000000000000",
    "subnet": "0.0.0.0 0.0.0.0",
    "type": "ipmask",
    "route-tag": 0,
    "sub-type": "sdn",
    "clearpass-spt": "unknown",
    "start-ip": "0.0.0.0",
    "end-ip": "0.0.0.0",
    "fqdn": "",
    "country": "",
    "wildcard-fqdn": "",
    "cache-ttl": 0,
    "wildcard": "0.0.0.0 0.0.0.0",
    "sdn": "",
    "interface": "",
    "tenant": "",
    "organization": "",
    "epg-name": "",
    "subnet-name": "",
    "sdn-tag": "",
    "policy-group": "",
    "obj-tag": "",
    "obj-type": "ip",
    "tag-detection-level": "",
    "tag-type": "",
    "hw-vendor": "",
    "hw-model": "",
    "os": "",
    "sw-version": "",
    "associated-interface": "",
    "color": 0,
    "sdn-addr-type": "private",
    "node-ip-only": "disable",
    "allow-routing": "disable",
    "passive-fqdn-learning": "enable",
    "fabric-object": "disable",
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
    "name": "string",  # Address name.
    "uuid": "uuid",  # Universally Unique Identifier (UUID; automatically assigned 
    "subnet": "ipv4-classnet-any",  # IP address and subnet mask of address.
    "type": "option",  # Type of address.
    "route-tag": "integer",  # route-tag address.
    "sub-type": "option",  # Sub-type of address.
    "clearpass-spt": "option",  # SPT (System Posture Token) value.
    "macaddr": "string",  # Multiple MAC address ranges.
    "start-ip": "ipv4-address-any",  # First IP address (inclusive) in the range for the address.
    "end-ip": "ipv4-address-any",  # Final IP address (inclusive) in the range for the address.
    "fqdn": "string",  # Fully Qualified Domain Name address.
    "country": "string",  # IP addresses associated to a specific country.
    "wildcard-fqdn": "string",  # Fully Qualified Domain Name with wildcard characters.
    "cache-ttl": "integer",  # Defines the minimal TTL of individual IP addresses in FQDN c
    "wildcard": "ipv4-classnet-any",  # IP address and wildcard netmask.
    "sdn": "string",  # SDN.
    "fsso-group": "string",  # FSSO group(s).
    "sso-attribute-value": "string",  # RADIUS attributes value.
    "interface": "string",  # Name of interface whose IP address is to be used.
    "tenant": "string",  # Tenant.
    "organization": "string",  # Organization domain name (Syntax: organization/domain).
    "epg-name": "string",  # Endpoint group name.
    "subnet-name": "string",  # Subnet name.
    "sdn-tag": "string",  # SDN Tag.
    "policy-group": "string",  # Policy group name.
    "obj-tag": "string",  # Tag of dynamic address object.
    "obj-type": "option",  # Object type.
    "tag-detection-level": "string",  # Tag detection level of dynamic address object.
    "tag-type": "string",  # Tag type of dynamic address object.
    "hw-vendor": "string",  # Dynamic address matching hardware vendor.
    "hw-model": "string",  # Dynamic address matching hardware model.
    "os": "string",  # Dynamic address matching operating system.
    "sw-version": "string",  # Dynamic address matching software version.
    "comment": "var-string",  # Comment.
    "associated-interface": "string",  # Network interface associated with address.
    "color": "integer",  # Color of icon on the GUI.
    "filter": "var-string",  # Match criteria filter.
    "sdn-addr-type": "option",  # Type of addresses to collect.
    "node-ip-only": "option",  # Enable/disable collection of node addresses only in Kubernet
    "obj-id": "var-string",  # Object ID for NSX.
    "list": "string",  # IP address list.
    "tagging": "string",  # Config object tagging.
    "allow-routing": "option",  # Enable/disable use of this address in routing configurations
    "passive-fqdn-learning": "option",  # Enable/disable passive learning of FQDNs.  When enabled, the
    "fabric-object": "option",  # Security Fabric global object setting.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "Address name.",
    "uuid": "Universally Unique Identifier (UUID; automatically assigned but can be manually reset).",
    "subnet": "IP address and subnet mask of address.",
    "type": "Type of address.",
    "route-tag": "route-tag address.",
    "sub-type": "Sub-type of address.",
    "clearpass-spt": "SPT (System Posture Token) value.",
    "macaddr": "Multiple MAC address ranges.",
    "start-ip": "First IP address (inclusive) in the range for the address.",
    "end-ip": "Final IP address (inclusive) in the range for the address.",
    "fqdn": "Fully Qualified Domain Name address.",
    "country": "IP addresses associated to a specific country.",
    "wildcard-fqdn": "Fully Qualified Domain Name with wildcard characters.",
    "cache-ttl": "Defines the minimal TTL of individual IP addresses in FQDN cache measured in seconds.",
    "wildcard": "IP address and wildcard netmask.",
    "sdn": "SDN.",
    "fsso-group": "FSSO group(s).",
    "sso-attribute-value": "RADIUS attributes value.",
    "interface": "Name of interface whose IP address is to be used.",
    "tenant": "Tenant.",
    "organization": "Organization domain name (Syntax: organization/domain).",
    "epg-name": "Endpoint group name.",
    "subnet-name": "Subnet name.",
    "sdn-tag": "SDN Tag.",
    "policy-group": "Policy group name.",
    "obj-tag": "Tag of dynamic address object.",
    "obj-type": "Object type.",
    "tag-detection-level": "Tag detection level of dynamic address object.",
    "tag-type": "Tag type of dynamic address object.",
    "hw-vendor": "Dynamic address matching hardware vendor.",
    "hw-model": "Dynamic address matching hardware model.",
    "os": "Dynamic address matching operating system.",
    "sw-version": "Dynamic address matching software version.",
    "comment": "Comment.",
    "associated-interface": "Network interface associated with address.",
    "color": "Color of icon on the GUI.",
    "filter": "Match criteria filter.",
    "sdn-addr-type": "Type of addresses to collect.",
    "node-ip-only": "Enable/disable collection of node addresses only in Kubernetes.",
    "obj-id": "Object ID for NSX.",
    "list": "IP address list.",
    "tagging": "Config object tagging.",
    "allow-routing": "Enable/disable use of this address in routing configurations.",
    "passive-fqdn-learning": "Enable/disable passive learning of FQDNs.  When enabled, the FortiGate learns, trusts, and saves FQDNs from endpoint DNS queries (default = enable).",
    "fabric-object": "Security Fabric global object setting.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 79},
    "route-tag": {"type": "integer", "min": 1, "max": 4294967295},
    "fqdn": {"type": "string", "max_length": 255},
    "country": {"type": "string", "max_length": 2},
    "wildcard-fqdn": {"type": "string", "max_length": 255},
    "cache-ttl": {"type": "integer", "min": 0, "max": 86400},
    "sdn": {"type": "string", "max_length": 35},
    "interface": {"type": "string", "max_length": 35},
    "tenant": {"type": "string", "max_length": 35},
    "organization": {"type": "string", "max_length": 35},
    "epg-name": {"type": "string", "max_length": 255},
    "subnet-name": {"type": "string", "max_length": 255},
    "sdn-tag": {"type": "string", "max_length": 15},
    "policy-group": {"type": "string", "max_length": 15},
    "obj-tag": {"type": "string", "max_length": 255},
    "tag-detection-level": {"type": "string", "max_length": 15},
    "tag-type": {"type": "string", "max_length": 63},
    "hw-vendor": {"type": "string", "max_length": 35},
    "hw-model": {"type": "string", "max_length": 35},
    "os": {"type": "string", "max_length": 35},
    "sw-version": {"type": "string", "max_length": 35},
    "associated-interface": {"type": "string", "max_length": 35},
    "color": {"type": "integer", "min": 0, "max": 32},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "macaddr": {
        "macaddr": {
            "type": "string",
            "help": "MAC address ranges <start>[-<end>] separated by space.",
            "required": True,
            "default": "",
            "max_length": 127,
        },
    },
    "fsso-group": {
        "name": {
            "type": "string",
            "help": "FSSO group name.",
            "default": "",
            "max_length": 511,
        },
    },
    "sso-attribute-value": {
        "name": {
            "type": "string",
            "help": "RADIUS attribute value.",
            "default": "",
            "max_length": 511,
        },
    },
    "list": {
        "ip": {
            "type": "string",
            "help": "IP.",
            "required": True,
            "default": "",
            "max_length": 35,
        },
    },
    "tagging": {
        "name": {
            "type": "string",
            "help": "Tagging entry name.",
            "default": "",
            "max_length": 63,
        },
        "category": {
            "type": "string",
            "help": "Tag category.",
            "default": "",
            "max_length": 63,
        },
        "tags": {
            "type": "string",
            "help": "Tags.",
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_TYPE = [
    "ipmask",  # Standard IPv4 address with subnet mask.
    "iprange",  # Range of IPv4 addresses between two specified addresses (inclusive).
    "fqdn",  # Fully Qualified Domain Name address.
    "geography",  # IP addresses from a specified country.
    "wildcard",  # Standard IPv4 using a wildcard subnet mask.
    "dynamic",  # Dynamic address object.
    "interface-subnet",  # IP and subnet of interface.
    "mac",  # Range of MAC addresses.
    "route-tag",  # route-tag addresses.
]
VALID_BODY_SUB_TYPE = [
    "sdn",  # SDN address.
    "clearpass-spt",  # ClearPass SPT (System Posture Token) address.
    "fsso",  # FSSO address.
    "rsso",  # RSSO address.
    "ems-tag",  # FortiClient EMS tag.
    "fortivoice-tag",  # FortiVoice tag.
    "fortinac-tag",  # FortiNAC tag.
    "swc-tag",  # Switch Controller NAC policy tag.
    "device-identification",  # Device address.
    "external-resource",  # External resource.
    "obsolete",  # Tag from EOL product.
]
VALID_BODY_CLEARPASS_SPT = [
    "unknown",  # UNKNOWN.
    "healthy",  # HEALTHY.
    "quarantine",  # QUARANTINE.
    "checkup",  # CHECKUP.
    "transient",  # TRANSIENT.
    "infected",  # INFECTED.
]
VALID_BODY_OBJ_TYPE = [
    "ip",  # IP address.
    "mac",  # MAC address
]
VALID_BODY_SDN_ADDR_TYPE = [
    "private",  # Collect private addresses only.
    "public",  # Collect public addresses only.
    "all",  # Collect both public and private addresses.
]
VALID_BODY_NODE_IP_ONLY = [
    "enable",  # Enable collection of node addresses only in Kubernetes.
    "disable",  # Disable collection of node addresses only in Kubernetes.
]
VALID_BODY_ALLOW_ROUTING = [
    "enable",  # Enable use of this address in routing configurations.
    "disable",  # Disable use of this address in routing configurations.
]
VALID_BODY_PASSIVE_FQDN_LEARNING = [
    "disable",  # Disable passive learning of FQDNs.
    "enable",  # Enable passive learning of FQDNs.
]
VALID_BODY_FABRIC_OBJECT = [
    "enable",  # Object is set as a security fabric-wide global object.
    "disable",  # Object is local to this security fabric member.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_firewall_address_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for firewall/address."""
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
    """Validate required fields for firewall/address."""
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


def validate_firewall_address_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new firewall/address object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
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
    if "sub-type" in payload:
        value = payload["sub-type"]
        if value not in VALID_BODY_SUB_TYPE:
            desc = FIELD_DESCRIPTIONS.get("sub-type", "")
            error_msg = f"Invalid value for 'sub-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SUB_TYPE)}"
            error_msg += f"\n  → Example: sub-type='{{ VALID_BODY_SUB_TYPE[0] }}'"
            return (False, error_msg)
    if "clearpass-spt" in payload:
        value = payload["clearpass-spt"]
        if value not in VALID_BODY_CLEARPASS_SPT:
            desc = FIELD_DESCRIPTIONS.get("clearpass-spt", "")
            error_msg = f"Invalid value for 'clearpass-spt': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CLEARPASS_SPT)}"
            error_msg += f"\n  → Example: clearpass-spt='{{ VALID_BODY_CLEARPASS_SPT[0] }}'"
            return (False, error_msg)
    if "obj-type" in payload:
        value = payload["obj-type"]
        if value not in VALID_BODY_OBJ_TYPE:
            desc = FIELD_DESCRIPTIONS.get("obj-type", "")
            error_msg = f"Invalid value for 'obj-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_OBJ_TYPE)}"
            error_msg += f"\n  → Example: obj-type='{{ VALID_BODY_OBJ_TYPE[0] }}'"
            return (False, error_msg)
    if "sdn-addr-type" in payload:
        value = payload["sdn-addr-type"]
        if value not in VALID_BODY_SDN_ADDR_TYPE:
            desc = FIELD_DESCRIPTIONS.get("sdn-addr-type", "")
            error_msg = f"Invalid value for 'sdn-addr-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SDN_ADDR_TYPE)}"
            error_msg += f"\n  → Example: sdn-addr-type='{{ VALID_BODY_SDN_ADDR_TYPE[0] }}'"
            return (False, error_msg)
    if "node-ip-only" in payload:
        value = payload["node-ip-only"]
        if value not in VALID_BODY_NODE_IP_ONLY:
            desc = FIELD_DESCRIPTIONS.get("node-ip-only", "")
            error_msg = f"Invalid value for 'node-ip-only': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_NODE_IP_ONLY)}"
            error_msg += f"\n  → Example: node-ip-only='{{ VALID_BODY_NODE_IP_ONLY[0] }}'"
            return (False, error_msg)
    if "allow-routing" in payload:
        value = payload["allow-routing"]
        if value not in VALID_BODY_ALLOW_ROUTING:
            desc = FIELD_DESCRIPTIONS.get("allow-routing", "")
            error_msg = f"Invalid value for 'allow-routing': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ALLOW_ROUTING)}"
            error_msg += f"\n  → Example: allow-routing='{{ VALID_BODY_ALLOW_ROUTING[0] }}'"
            return (False, error_msg)
    if "passive-fqdn-learning" in payload:
        value = payload["passive-fqdn-learning"]
        if value not in VALID_BODY_PASSIVE_FQDN_LEARNING:
            desc = FIELD_DESCRIPTIONS.get("passive-fqdn-learning", "")
            error_msg = f"Invalid value for 'passive-fqdn-learning': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PASSIVE_FQDN_LEARNING)}"
            error_msg += f"\n  → Example: passive-fqdn-learning='{{ VALID_BODY_PASSIVE_FQDN_LEARNING[0] }}'"
            return (False, error_msg)
    if "fabric-object" in payload:
        value = payload["fabric-object"]
        if value not in VALID_BODY_FABRIC_OBJECT:
            desc = FIELD_DESCRIPTIONS.get("fabric-object", "")
            error_msg = f"Invalid value for 'fabric-object': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FABRIC_OBJECT)}"
            error_msg += f"\n  → Example: fabric-object='{{ VALID_BODY_FABRIC_OBJECT[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_firewall_address_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update firewall/address."""
    # Step 1: Validate enum values
    if "type" in payload:
        value = payload["type"]
        if value not in VALID_BODY_TYPE:
            return (
                False,
                f"Invalid value for 'type'='{value}'. Must be one of: {', '.join(VALID_BODY_TYPE)}",
            )
    if "sub-type" in payload:
        value = payload["sub-type"]
        if value not in VALID_BODY_SUB_TYPE:
            return (
                False,
                f"Invalid value for 'sub-type'='{value}'. Must be one of: {', '.join(VALID_BODY_SUB_TYPE)}",
            )
    if "clearpass-spt" in payload:
        value = payload["clearpass-spt"]
        if value not in VALID_BODY_CLEARPASS_SPT:
            return (
                False,
                f"Invalid value for 'clearpass-spt'='{value}'. Must be one of: {', '.join(VALID_BODY_CLEARPASS_SPT)}",
            )
    if "obj-type" in payload:
        value = payload["obj-type"]
        if value not in VALID_BODY_OBJ_TYPE:
            return (
                False,
                f"Invalid value for 'obj-type'='{value}'. Must be one of: {', '.join(VALID_BODY_OBJ_TYPE)}",
            )
    if "sdn-addr-type" in payload:
        value = payload["sdn-addr-type"]
        if value not in VALID_BODY_SDN_ADDR_TYPE:
            return (
                False,
                f"Invalid value for 'sdn-addr-type'='{value}'. Must be one of: {', '.join(VALID_BODY_SDN_ADDR_TYPE)}",
            )
    if "node-ip-only" in payload:
        value = payload["node-ip-only"]
        if value not in VALID_BODY_NODE_IP_ONLY:
            return (
                False,
                f"Invalid value for 'node-ip-only'='{value}'. Must be one of: {', '.join(VALID_BODY_NODE_IP_ONLY)}",
            )
    if "allow-routing" in payload:
        value = payload["allow-routing"]
        if value not in VALID_BODY_ALLOW_ROUTING:
            return (
                False,
                f"Invalid value for 'allow-routing'='{value}'. Must be one of: {', '.join(VALID_BODY_ALLOW_ROUTING)}",
            )
    if "passive-fqdn-learning" in payload:
        value = payload["passive-fqdn-learning"]
        if value not in VALID_BODY_PASSIVE_FQDN_LEARNING:
            return (
                False,
                f"Invalid value for 'passive-fqdn-learning'='{value}'. Must be one of: {', '.join(VALID_BODY_PASSIVE_FQDN_LEARNING)}",
            )
    if "fabric-object" in payload:
        value = payload["fabric-object"]
        if value not in VALID_BODY_FABRIC_OBJECT:
            return (
                False,
                f"Invalid value for 'fabric-object'='{value}'. Must be one of: {', '.join(VALID_BODY_FABRIC_OBJECT)}",
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
    "endpoint": "firewall/address",
    "category": "cmdb",
    "api_path": "firewall/address",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure IPv4 addresses.",
    "total_fields": 45,
    "required_fields_count": 2,
    "fields_with_defaults_count": 37,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
