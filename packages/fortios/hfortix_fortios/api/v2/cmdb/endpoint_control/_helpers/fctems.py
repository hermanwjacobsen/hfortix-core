"""Validation helpers for endpoint_control/fctems - Auto-generated"""

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
    "ems-id": 0,
    "status": "disable",
    "name": "",
    "dirty-reason": "none",
    "fortinetone-cloud-authentication": "disable",
    "server": "",
    "https-port": 443,
    "serial-number": "",
    "tenant-id": "",
    "source-ip": "0.0.0.0",
    "pull-sysinfo": "enable",
    "pull-vulnerabilities": "enable",
    "pull-tags": "enable",
    "pull-malware-hash": "enable",
    "capabilities": "",
    "call-timeout": 30,
    "out-of-sync-threshold": 180,
    "send-tags-to-all-vdoms": "disable",
    "websocket-override": "disable",
    "interface-select-method": "auto",
    "interface": "",
    "trust-ca-cn": "enable",
    "verifying-ca": "",
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
    "ems-id": "integer",  # EMS ID in order (1 - 7).
    "status": "option",  # Enable or disable this EMS configuration.
    "name": "string",  # FortiClient Enterprise Management Server (EMS) name.
    "dirty-reason": "option",  # Dirty Reason for FortiClient EMS.
    "fortinetone-cloud-authentication": "option",  # Enable/disable authentication of FortiClient EMS Cloud throu
    "cloud-authentication-access-key": "password",  # FortiClient EMS Cloud multitenancy access key
    "server": "string",  # FortiClient EMS FQDN or IPv4 address.
    "https-port": "integer",  # FortiClient EMS HTTPS access port number. (1 - 65535, defaul
    "serial-number": "string",  # EMS Serial Number.
    "tenant-id": "string",  # EMS Tenant ID.
    "source-ip": "ipv4-address-any",  # REST API call source IP.
    "pull-sysinfo": "option",  # Enable/disable pulling SysInfo from EMS.
    "pull-vulnerabilities": "option",  # Enable/disable pulling vulnerabilities from EMS.
    "pull-tags": "option",  # Enable/disable pulling FortiClient user tags from EMS.
    "pull-malware-hash": "option",  # Enable/disable pulling FortiClient malware hash from EMS.
    "capabilities": "option",  # List of EMS capabilities.
    "call-timeout": "integer",  # FortiClient EMS call timeout in seconds (1 - 180 seconds, de
    "out-of-sync-threshold": "integer",  # Outdated resource threshold in seconds (10 - 3600, default =
    "send-tags-to-all-vdoms": "option",  # Relax restrictions on tags to send all EMS tags to all VDOMs
    "websocket-override": "option",  # Enable/disable override behavior for how this FortiGate unit
    "interface-select-method": "option",  # Specify how to select outgoing interface to reach server.
    "interface": "string",  # Specify outgoing interface to reach server.
    "trust-ca-cn": "option",  # Enable/disable trust of the EMS certificate issuer(CA) and c
    "verifying-ca": "string",  # Lowest CA cert on Fortigate in verified EMS cert chain.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "ems-id": "EMS ID in order (1 - 7).",
    "status": "Enable or disable this EMS configuration.",
    "name": "FortiClient Enterprise Management Server (EMS) name.",
    "dirty-reason": "Dirty Reason for FortiClient EMS.",
    "fortinetone-cloud-authentication": "Enable/disable authentication of FortiClient EMS Cloud through FortiCloud account.",
    "cloud-authentication-access-key": "FortiClient EMS Cloud multitenancy access key",
    "server": "FortiClient EMS FQDN or IPv4 address.",
    "https-port": "FortiClient EMS HTTPS access port number. (1 - 65535, default: 443).",
    "serial-number": "EMS Serial Number.",
    "tenant-id": "EMS Tenant ID.",
    "source-ip": "REST API call source IP.",
    "pull-sysinfo": "Enable/disable pulling SysInfo from EMS.",
    "pull-vulnerabilities": "Enable/disable pulling vulnerabilities from EMS.",
    "pull-tags": "Enable/disable pulling FortiClient user tags from EMS.",
    "pull-malware-hash": "Enable/disable pulling FortiClient malware hash from EMS.",
    "capabilities": "List of EMS capabilities.",
    "call-timeout": "FortiClient EMS call timeout in seconds (1 - 180 seconds, default = 30).",
    "out-of-sync-threshold": "Outdated resource threshold in seconds (10 - 3600, default = 180).",
    "send-tags-to-all-vdoms": "Relax restrictions on tags to send all EMS tags to all VDOMs",
    "websocket-override": "Enable/disable override behavior for how this FortiGate unit connects to EMS using a WebSocket connection.",
    "interface-select-method": "Specify how to select outgoing interface to reach server.",
    "interface": "Specify outgoing interface to reach server.",
    "trust-ca-cn": "Enable/disable trust of the EMS certificate issuer(CA) and common name(CN) for certificate auto-renewal.",
    "verifying-ca": "Lowest CA cert on Fortigate in verified EMS cert chain.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "ems-id": {"type": "integer", "min": 1, "max": 7},
    "name": {"type": "string", "max_length": 35},
    "server": {"type": "string", "max_length": 255},
    "https-port": {"type": "integer", "min": 1, "max": 65535},
    "serial-number": {"type": "string", "max_length": 16},
    "tenant-id": {"type": "string", "max_length": 32},
    "call-timeout": {"type": "integer", "min": 1, "max": 180},
    "out-of-sync-threshold": {"type": "integer", "min": 10, "max": 3600},
    "interface": {"type": "string", "max_length": 15},
    "verifying-ca": {"type": "string", "max_length": 79},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
}


# Valid enum values from API documentation
VALID_BODY_STATUS = [
    "enable",  # Enable EMS configuration and operation.
    "disable",  # Disable EMS configuration and operation.
]
VALID_BODY_DIRTY_REASON = [
    "none",  # FortiClient EMS entry not dirty.
    "mismatched-ems-sn",  # FortiClient EMS entry dirty because EMS SN is mismatched with configured SN.
]
VALID_BODY_FORTINETONE_CLOUD_AUTHENTICATION = [
    "enable",  # Enable authentication of FortiClient EMS Cloud through FortiCloud account.
    "disable",  # Disable authentication of FortiClient EMS Cloud through FortiCloud account.
]
VALID_BODY_PULL_SYSINFO = [
    "enable",  # Enable pulling FortiClient user SysInfo from EMS.
    "disable",  # Disable pulling FortiClient user SysInfo from EMS.
]
VALID_BODY_PULL_VULNERABILITIES = [
    "enable",  # Enable pulling client vulnerabilities from EMS.
    "disable",  # Disable pulling client vulnerabilities from EMS.
]
VALID_BODY_PULL_TAGS = [
    "enable",  # Enable pulling FortiClient user tags from EMS.
    "disable",  # Disable pulling FortiClient user tags from EMS.
]
VALID_BODY_PULL_MALWARE_HASH = [
    "enable",  # Enable pulling FortiClient malware hash from EMS.
    "disable",  # Disable pulling FortiClient malware hash from EMS.
]
VALID_BODY_CAPABILITIES = [
    "fabric-auth",  # Allow this FortiGate unit to load the authentication page provided by EMS to authenticate itself with EMS.
    "silent-approval",  # Allow silent approval of non-root or FortiGate HA clusters on EMS in the Security Fabric.
    "websocket",  # Enable/disable websockets for this FortiGate unit. Override behavior using websocket-override.
    "websocket-malware",  # Allow this FortiGate unit to request malware hash notifications over websocket.
    "push-ca-certs",  # Enable/disable syncing deep inspection certificates with EMS.
    "common-tags-api",  # Can recieve tag information from New Common Tags API from EMS.
    "tenant-id",  # Allow this FortiGate to retrieve Tenant-ID from EMS.
    "client-avatars",  # Allow this FortiGate to retrieve avatars from EMS by fingerprint.
    "single-vdom-connector",  # Allow this FortiGate to create a vdom connector to EMS.
    "fgt-sysinfo-api",  # Allow this FortiGate to send additional info to EMS.
    "ztna-server-info",  # Allow this FortiGate to send vdom's ZTNA server information to EMS.
    "used-tags",  # Allow this FortiGate to send used tags information to EMS.
]
VALID_BODY_SEND_TAGS_TO_ALL_VDOMS = [
    "enable",  # Enable sending tags to all vdoms.
    "disable",  # Disable sending tags to all vdoms.
]
VALID_BODY_WEBSOCKET_OVERRIDE = [
    "enable",  # Do not override the WebSocket connection. Connect to WebSocket of this EMS server if it is capable (default).
    "disable",  # Override the WebSocket connection. Do not connect to WebSocket even if EMS is capable of a WebSocket connection.
]
VALID_BODY_INTERFACE_SELECT_METHOD = [
    "auto",  # Set outgoing interface automatically.
    "sdwan",  # Set outgoing interface by SD-WAN or policy routing rules.
    "specify",  # Set outgoing interface manually.
]
VALID_BODY_TRUST_CA_CN = [
    "enable",  # Trust EMS certificate CA & CN to automatically renew certificate.
    "disable",  # Do not trust EMS certificate CA & CN to automatically renew certificate.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_endpoint_control_fctems_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for endpoint_control/fctems."""
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
    """Validate required fields for endpoint_control/fctems."""
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


def validate_endpoint_control_fctems_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new endpoint_control/fctems object."""
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
    if "dirty-reason" in payload:
        value = payload["dirty-reason"]
        if value not in VALID_BODY_DIRTY_REASON:
            desc = FIELD_DESCRIPTIONS.get("dirty-reason", "")
            error_msg = f"Invalid value for 'dirty-reason': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DIRTY_REASON)}"
            error_msg += f"\n  → Example: dirty-reason='{{ VALID_BODY_DIRTY_REASON[0] }}'"
            return (False, error_msg)
    if "fortinetone-cloud-authentication" in payload:
        value = payload["fortinetone-cloud-authentication"]
        if value not in VALID_BODY_FORTINETONE_CLOUD_AUTHENTICATION:
            desc = FIELD_DESCRIPTIONS.get("fortinetone-cloud-authentication", "")
            error_msg = f"Invalid value for 'fortinetone-cloud-authentication': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FORTINETONE_CLOUD_AUTHENTICATION)}"
            error_msg += f"\n  → Example: fortinetone-cloud-authentication='{{ VALID_BODY_FORTINETONE_CLOUD_AUTHENTICATION[0] }}'"
            return (False, error_msg)
    if "pull-sysinfo" in payload:
        value = payload["pull-sysinfo"]
        if value not in VALID_BODY_PULL_SYSINFO:
            desc = FIELD_DESCRIPTIONS.get("pull-sysinfo", "")
            error_msg = f"Invalid value for 'pull-sysinfo': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PULL_SYSINFO)}"
            error_msg += f"\n  → Example: pull-sysinfo='{{ VALID_BODY_PULL_SYSINFO[0] }}'"
            return (False, error_msg)
    if "pull-vulnerabilities" in payload:
        value = payload["pull-vulnerabilities"]
        if value not in VALID_BODY_PULL_VULNERABILITIES:
            desc = FIELD_DESCRIPTIONS.get("pull-vulnerabilities", "")
            error_msg = f"Invalid value for 'pull-vulnerabilities': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PULL_VULNERABILITIES)}"
            error_msg += f"\n  → Example: pull-vulnerabilities='{{ VALID_BODY_PULL_VULNERABILITIES[0] }}'"
            return (False, error_msg)
    if "pull-tags" in payload:
        value = payload["pull-tags"]
        if value not in VALID_BODY_PULL_TAGS:
            desc = FIELD_DESCRIPTIONS.get("pull-tags", "")
            error_msg = f"Invalid value for 'pull-tags': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PULL_TAGS)}"
            error_msg += f"\n  → Example: pull-tags='{{ VALID_BODY_PULL_TAGS[0] }}'"
            return (False, error_msg)
    if "pull-malware-hash" in payload:
        value = payload["pull-malware-hash"]
        if value not in VALID_BODY_PULL_MALWARE_HASH:
            desc = FIELD_DESCRIPTIONS.get("pull-malware-hash", "")
            error_msg = f"Invalid value for 'pull-malware-hash': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PULL_MALWARE_HASH)}"
            error_msg += f"\n  → Example: pull-malware-hash='{{ VALID_BODY_PULL_MALWARE_HASH[0] }}'"
            return (False, error_msg)
    if "capabilities" in payload:
        value = payload["capabilities"]
        if value not in VALID_BODY_CAPABILITIES:
            desc = FIELD_DESCRIPTIONS.get("capabilities", "")
            error_msg = f"Invalid value for 'capabilities': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CAPABILITIES)}"
            error_msg += f"\n  → Example: capabilities='{{ VALID_BODY_CAPABILITIES[0] }}'"
            return (False, error_msg)
    if "send-tags-to-all-vdoms" in payload:
        value = payload["send-tags-to-all-vdoms"]
        if value not in VALID_BODY_SEND_TAGS_TO_ALL_VDOMS:
            desc = FIELD_DESCRIPTIONS.get("send-tags-to-all-vdoms", "")
            error_msg = f"Invalid value for 'send-tags-to-all-vdoms': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SEND_TAGS_TO_ALL_VDOMS)}"
            error_msg += f"\n  → Example: send-tags-to-all-vdoms='{{ VALID_BODY_SEND_TAGS_TO_ALL_VDOMS[0] }}'"
            return (False, error_msg)
    if "websocket-override" in payload:
        value = payload["websocket-override"]
        if value not in VALID_BODY_WEBSOCKET_OVERRIDE:
            desc = FIELD_DESCRIPTIONS.get("websocket-override", "")
            error_msg = f"Invalid value for 'websocket-override': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WEBSOCKET_OVERRIDE)}"
            error_msg += f"\n  → Example: websocket-override='{{ VALID_BODY_WEBSOCKET_OVERRIDE[0] }}'"
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
    if "trust-ca-cn" in payload:
        value = payload["trust-ca-cn"]
        if value not in VALID_BODY_TRUST_CA_CN:
            desc = FIELD_DESCRIPTIONS.get("trust-ca-cn", "")
            error_msg = f"Invalid value for 'trust-ca-cn': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_TRUST_CA_CN)}"
            error_msg += f"\n  → Example: trust-ca-cn='{{ VALID_BODY_TRUST_CA_CN[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_endpoint_control_fctems_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update endpoint_control/fctems."""
    # Step 1: Validate enum values
    if "status" in payload:
        value = payload["status"]
        if value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid value for 'status'='{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )
    if "dirty-reason" in payload:
        value = payload["dirty-reason"]
        if value not in VALID_BODY_DIRTY_REASON:
            return (
                False,
                f"Invalid value for 'dirty-reason'='{value}'. Must be one of: {', '.join(VALID_BODY_DIRTY_REASON)}",
            )
    if "fortinetone-cloud-authentication" in payload:
        value = payload["fortinetone-cloud-authentication"]
        if value not in VALID_BODY_FORTINETONE_CLOUD_AUTHENTICATION:
            return (
                False,
                f"Invalid value for 'fortinetone-cloud-authentication'='{value}'. Must be one of: {', '.join(VALID_BODY_FORTINETONE_CLOUD_AUTHENTICATION)}",
            )
    if "pull-sysinfo" in payload:
        value = payload["pull-sysinfo"]
        if value not in VALID_BODY_PULL_SYSINFO:
            return (
                False,
                f"Invalid value for 'pull-sysinfo'='{value}'. Must be one of: {', '.join(VALID_BODY_PULL_SYSINFO)}",
            )
    if "pull-vulnerabilities" in payload:
        value = payload["pull-vulnerabilities"]
        if value not in VALID_BODY_PULL_VULNERABILITIES:
            return (
                False,
                f"Invalid value for 'pull-vulnerabilities'='{value}'. Must be one of: {', '.join(VALID_BODY_PULL_VULNERABILITIES)}",
            )
    if "pull-tags" in payload:
        value = payload["pull-tags"]
        if value not in VALID_BODY_PULL_TAGS:
            return (
                False,
                f"Invalid value for 'pull-tags'='{value}'. Must be one of: {', '.join(VALID_BODY_PULL_TAGS)}",
            )
    if "pull-malware-hash" in payload:
        value = payload["pull-malware-hash"]
        if value not in VALID_BODY_PULL_MALWARE_HASH:
            return (
                False,
                f"Invalid value for 'pull-malware-hash'='{value}'. Must be one of: {', '.join(VALID_BODY_PULL_MALWARE_HASH)}",
            )
    if "capabilities" in payload:
        value = payload["capabilities"]
        if value not in VALID_BODY_CAPABILITIES:
            return (
                False,
                f"Invalid value for 'capabilities'='{value}'. Must be one of: {', '.join(VALID_BODY_CAPABILITIES)}",
            )
    if "send-tags-to-all-vdoms" in payload:
        value = payload["send-tags-to-all-vdoms"]
        if value not in VALID_BODY_SEND_TAGS_TO_ALL_VDOMS:
            return (
                False,
                f"Invalid value for 'send-tags-to-all-vdoms'='{value}'. Must be one of: {', '.join(VALID_BODY_SEND_TAGS_TO_ALL_VDOMS)}",
            )
    if "websocket-override" in payload:
        value = payload["websocket-override"]
        if value not in VALID_BODY_WEBSOCKET_OVERRIDE:
            return (
                False,
                f"Invalid value for 'websocket-override'='{value}'. Must be one of: {', '.join(VALID_BODY_WEBSOCKET_OVERRIDE)}",
            )
    if "interface-select-method" in payload:
        value = payload["interface-select-method"]
        if value not in VALID_BODY_INTERFACE_SELECT_METHOD:
            return (
                False,
                f"Invalid value for 'interface-select-method'='{value}'. Must be one of: {', '.join(VALID_BODY_INTERFACE_SELECT_METHOD)}",
            )
    if "trust-ca-cn" in payload:
        value = payload["trust-ca-cn"]
        if value not in VALID_BODY_TRUST_CA_CN:
            return (
                False,
                f"Invalid value for 'trust-ca-cn'='{value}'. Must be one of: {', '.join(VALID_BODY_TRUST_CA_CN)}",
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
    "endpoint": "endpoint_control/fctems",
    "category": "cmdb",
    "api_path": "endpoint-control/fctems",
    "mkey": "ems-id",
    "mkey_type": "integer",
    "help": "Configure FortiClient Enterprise Management Server (EMS) entries.",
    "total_fields": 24,
    "required_fields_count": 1,
    "fields_with_defaults_count": 23,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
