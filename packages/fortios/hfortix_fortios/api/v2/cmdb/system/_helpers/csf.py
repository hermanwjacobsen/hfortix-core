"""Validation helpers for system/csf - Auto-generated"""

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
    "upstream-interface",  # Specify outgoing interface to reach server.
    "downstream-accprofile",  # Default access profile for requests from downstream devices.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "status": "disable",
    "uid": "",
    "upstream": "",
    "source-ip": "0.0.0.0",
    "upstream-interface-select-method": "auto",
    "upstream-interface": "",
    "upstream-port": 8013,
    "group-name": "",
    "accept-auth-by-cert": "enable",
    "log-unification": "enable",
    "authorization-request-type": "serial",
    "certificate": "",
    "fabric-workers": 2,
    "downstream-access": "disable",
    "legacy-authentication": "disable",
    "downstream-accprofile": "",
    "configuration-sync": "default",
    "fabric-object-unification": "default",
    "saml-configuration-sync": "default",
    "forticloud-account-enforcement": "enable",
    "file-mgmt": "enable",
    "file-quota": 0,
    "file-quota-warning": 90,
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
    "status": "option",  # Enable/disable Security Fabric.
    "uid": "string",  # Unique ID of the current CSF node
    "upstream": "string",  # IP/FQDN of the FortiGate upstream from this FortiGate in the
    "source-ip": "ipv4-address",  # Source IP address for communication with the upstream FortiG
    "upstream-interface-select-method": "option",  # Specify how to select outgoing interface to reach server.
    "upstream-interface": "string",  # Specify outgoing interface to reach server.
    "upstream-port": "integer",  # The port number to use to communicate with the FortiGate ups
    "group-name": "string",  # Security Fabric group name. All FortiGates in a Security Fab
    "group-password": "password",  # Security Fabric group password. For legacy authentication, f
    "accept-auth-by-cert": "option",  # Accept connections with unknown certificates and ask admin f
    "log-unification": "option",  # Enable/disable broadcast of discovery messages for log unifi
    "authorization-request-type": "option",  # Authorization request type.
    "certificate": "string",  # Certificate.
    "fabric-workers": "integer",  # Number of worker processes for Security Fabric daemon.
    "downstream-access": "option",  # Enable/disable downstream device access to this device's con
    "legacy-authentication": "option",  # Enable/disable legacy authentication.
    "downstream-accprofile": "string",  # Default access profile for requests from downstream devices.
    "configuration-sync": "option",  # Configuration sync mode.
    "fabric-object-unification": "option",  # Fabric CMDB Object Unification.
    "saml-configuration-sync": "option",  # SAML setting configuration synchronization.
    "trusted-list": "string",  # Pre-authorized and blocked security fabric nodes.
    "fabric-connector": "string",  # Fabric connector configuration.
    "forticloud-account-enforcement": "option",  # Fabric FortiCloud account unification.
    "file-mgmt": "option",  # Enable/disable Security Fabric daemon file management.
    "file-quota": "integer",  # Maximum amount of memory that can be used by the daemon file
    "file-quota-warning": "integer",  # Warn when the set percentage of quota has been used.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "status": "Enable/disable Security Fabric.",
    "uid": "Unique ID of the current CSF node",
    "upstream": "IP/FQDN of the FortiGate upstream from this FortiGate in the Security Fabric.",
    "source-ip": "Source IP address for communication with the upstream FortiGate.",
    "upstream-interface-select-method": "Specify how to select outgoing interface to reach server.",
    "upstream-interface": "Specify outgoing interface to reach server.",
    "upstream-port": "The port number to use to communicate with the FortiGate upstream from this FortiGate in the Security Fabric (default = 8013).",
    "group-name": "Security Fabric group name. All FortiGates in a Security Fabric must have the same group name.",
    "group-password": "Security Fabric group password. For legacy authentication, fabric members must have the same group password.",
    "accept-auth-by-cert": "Accept connections with unknown certificates and ask admin for approval.",
    "log-unification": "Enable/disable broadcast of discovery messages for log unification.",
    "authorization-request-type": "Authorization request type.",
    "certificate": "Certificate.",
    "fabric-workers": "Number of worker processes for Security Fabric daemon.",
    "downstream-access": "Enable/disable downstream device access to this device's configuration and data.",
    "legacy-authentication": "Enable/disable legacy authentication.",
    "downstream-accprofile": "Default access profile for requests from downstream devices.",
    "configuration-sync": "Configuration sync mode.",
    "fabric-object-unification": "Fabric CMDB Object Unification.",
    "saml-configuration-sync": "SAML setting configuration synchronization.",
    "trusted-list": "Pre-authorized and blocked security fabric nodes.",
    "fabric-connector": "Fabric connector configuration.",
    "forticloud-account-enforcement": "Fabric FortiCloud account unification.",
    "file-mgmt": "Enable/disable Security Fabric daemon file management.",
    "file-quota": "Maximum amount of memory that can be used by the daemon files (in bytes).",
    "file-quota-warning": "Warn when the set percentage of quota has been used.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "uid": {"type": "string", "max_length": 35},
    "upstream": {"type": "string", "max_length": 255},
    "upstream-interface": {"type": "string", "max_length": 15},
    "upstream-port": {"type": "integer", "min": 1, "max": 65535},
    "group-name": {"type": "string", "max_length": 35},
    "certificate": {"type": "string", "max_length": 35},
    "fabric-workers": {"type": "integer", "min": 1, "max": 4},
    "downstream-accprofile": {"type": "string", "max_length": 35},
    "file-quota": {"type": "integer", "min": 0, "max": 4294967295},
    "file-quota-warning": {"type": "integer", "min": 1, "max": 99},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "trusted-list": {
        "name": {
            "type": "string",
            "help": "Name.",
            "default": "",
            "max_length": 35,
        },
        "authorization-type": {
            "type": "option",
            "help": "Authorization type.",
            "default": "serial",
            "options": [{"help": "Verify downstream by serial number.", "label": "Serial", "name": "serial"}, {"help": "Verify downstream by certificate.", "label": "Certificate", "name": "certificate"}],
        },
        "serial": {
            "type": "string",
            "help": "Serial.",
            "default": "",
            "max_length": 19,
        },
        "certificate": {
            "type": "var-string",
            "help": "Certificate.",
            "max_length": 32767,
        },
        "action": {
            "type": "option",
            "help": "Security fabric authorization action.",
            "default": "accept",
            "options": [{"help": "Accept authorization request.", "label": "Accept", "name": "accept"}, {"help": "Deny authorization request.", "label": "Deny", "name": "deny"}],
        },
        "ha-members": {
            "type": "string",
            "help": "HA members.",
            "default": "",
            "max_length": 19,
        },
        "downstream-authorization": {
            "type": "option",
            "help": "Trust authorizations by this node's administrator.",
            "default": "disable",
            "options": [{"help": "Enable downstream authorization.", "label": "Enable", "name": "enable"}, {"help": "Disable downstream authorization.", "label": "Disable", "name": "disable"}],
        },
        "index": {
            "type": "integer",
            "help": "Index of the downstream in tree.",
            "default": 0,
            "min_value": 1,
            "max_value": 1024,
        },
    },
    "fabric-connector": {
        "serial": {
            "type": "string",
            "help": "Serial.",
            "default": "",
            "max_length": 19,
        },
        "accprofile": {
            "type": "string",
            "help": "Override access profile.",
            "default": "",
            "max_length": 35,
        },
        "configuration-write-access": {
            "type": "option",
            "help": "Enable/disable downstream device write access to configuration.",
            "default": "disable",
            "options": [{"help": "Enable downstream device write access to configuration.", "label": "Enable", "name": "enable"}, {"help": "Disable downstream device write access to configuration.", "label": "Disable", "name": "disable"}],
        },
        "vdom": {
            "type": "string",
            "help": "Virtual domains that the connector has access to. If none are set, the connector will only have access to the VDOM that it joins the Security Fabric through.",
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_STATUS = [
    "enable",  # Enable Security Fabric.
    "disable",  # Disable Security Fabric.
]
VALID_BODY_UPSTREAM_INTERFACE_SELECT_METHOD = [
    "auto",  # Set outgoing interface automatically.
    "sdwan",  # Set outgoing interface by SD-WAN or policy routing rules.
    "specify",  # Set outgoing interface manually.
]
VALID_BODY_ACCEPT_AUTH_BY_CERT = [
    "disable",  # Do not accept SSL connections with unknown certificates.
    "enable",  # Accept SSL connections without automatic certificate verification.
]
VALID_BODY_LOG_UNIFICATION = [
    "disable",  # Disable broadcast of discovery messages for log unification.
    "enable",  # Enable broadcast of discovery messages for log unification.
]
VALID_BODY_AUTHORIZATION_REQUEST_TYPE = [
    "serial",  # Request verification by serial number.
    "certificate",  # Request verification by certificate.
]
VALID_BODY_DOWNSTREAM_ACCESS = [
    "enable",  # Enable downstream device access to this device's configuration and data.
    "disable",  # Disable downstream device access to this device's configuration and data.
]
VALID_BODY_LEGACY_AUTHENTICATION = [
    "disable",  # Do not accept legacy authentication requests.
    "enable",  # Accept legacy authentication requests.
]
VALID_BODY_CONFIGURATION_SYNC = [
    "default",  # Synchronize configuration for IPAM, FortiAnalyzer, FortiSandbox, and Central Management to root node.
    "local",  # Do not synchronize configuration with root node.
]
VALID_BODY_FABRIC_OBJECT_UNIFICATION = [
    "default",  # Global CMDB objects will be synchronized in Security Fabric.
    "local",  # Global CMDB objects will not be synchronized to and from this device.
]
VALID_BODY_SAML_CONFIGURATION_SYNC = [
    "default",  # SAML setting for fabric members is created by fabric root.
    "local",  # Do not apply SAML configuration generated by root.
]
VALID_BODY_FORTICLOUD_ACCOUNT_ENFORCEMENT = [
    "enable",  # Enable FortiCloud account ID matching for Security Fabric.
    "disable",  # Disable FortiCloud accound ID matching for Security Fabric.
]
VALID_BODY_FILE_MGMT = [
    "enable",  # Enable daemon file management.
    "disable",  # Disable daemon file management.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_system_csf_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for system/csf."""
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
    """Validate required fields for system/csf."""
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


def validate_system_csf_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new system/csf object."""
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
    if "upstream-interface-select-method" in payload:
        value = payload["upstream-interface-select-method"]
        if value not in VALID_BODY_UPSTREAM_INTERFACE_SELECT_METHOD:
            desc = FIELD_DESCRIPTIONS.get("upstream-interface-select-method", "")
            error_msg = f"Invalid value for 'upstream-interface-select-method': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_UPSTREAM_INTERFACE_SELECT_METHOD)}"
            error_msg += f"\n  → Example: upstream-interface-select-method='{{ VALID_BODY_UPSTREAM_INTERFACE_SELECT_METHOD[0] }}'"
            return (False, error_msg)
    if "accept-auth-by-cert" in payload:
        value = payload["accept-auth-by-cert"]
        if value not in VALID_BODY_ACCEPT_AUTH_BY_CERT:
            desc = FIELD_DESCRIPTIONS.get("accept-auth-by-cert", "")
            error_msg = f"Invalid value for 'accept-auth-by-cert': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ACCEPT_AUTH_BY_CERT)}"
            error_msg += f"\n  → Example: accept-auth-by-cert='{{ VALID_BODY_ACCEPT_AUTH_BY_CERT[0] }}'"
            return (False, error_msg)
    if "log-unification" in payload:
        value = payload["log-unification"]
        if value not in VALID_BODY_LOG_UNIFICATION:
            desc = FIELD_DESCRIPTIONS.get("log-unification", "")
            error_msg = f"Invalid value for 'log-unification': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LOG_UNIFICATION)}"
            error_msg += f"\n  → Example: log-unification='{{ VALID_BODY_LOG_UNIFICATION[0] }}'"
            return (False, error_msg)
    if "authorization-request-type" in payload:
        value = payload["authorization-request-type"]
        if value not in VALID_BODY_AUTHORIZATION_REQUEST_TYPE:
            desc = FIELD_DESCRIPTIONS.get("authorization-request-type", "")
            error_msg = f"Invalid value for 'authorization-request-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTHORIZATION_REQUEST_TYPE)}"
            error_msg += f"\n  → Example: authorization-request-type='{{ VALID_BODY_AUTHORIZATION_REQUEST_TYPE[0] }}'"
            return (False, error_msg)
    if "downstream-access" in payload:
        value = payload["downstream-access"]
        if value not in VALID_BODY_DOWNSTREAM_ACCESS:
            desc = FIELD_DESCRIPTIONS.get("downstream-access", "")
            error_msg = f"Invalid value for 'downstream-access': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DOWNSTREAM_ACCESS)}"
            error_msg += f"\n  → Example: downstream-access='{{ VALID_BODY_DOWNSTREAM_ACCESS[0] }}'"
            return (False, error_msg)
    if "legacy-authentication" in payload:
        value = payload["legacy-authentication"]
        if value not in VALID_BODY_LEGACY_AUTHENTICATION:
            desc = FIELD_DESCRIPTIONS.get("legacy-authentication", "")
            error_msg = f"Invalid value for 'legacy-authentication': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LEGACY_AUTHENTICATION)}"
            error_msg += f"\n  → Example: legacy-authentication='{{ VALID_BODY_LEGACY_AUTHENTICATION[0] }}'"
            return (False, error_msg)
    if "configuration-sync" in payload:
        value = payload["configuration-sync"]
        if value not in VALID_BODY_CONFIGURATION_SYNC:
            desc = FIELD_DESCRIPTIONS.get("configuration-sync", "")
            error_msg = f"Invalid value for 'configuration-sync': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CONFIGURATION_SYNC)}"
            error_msg += f"\n  → Example: configuration-sync='{{ VALID_BODY_CONFIGURATION_SYNC[0] }}'"
            return (False, error_msg)
    if "fabric-object-unification" in payload:
        value = payload["fabric-object-unification"]
        if value not in VALID_BODY_FABRIC_OBJECT_UNIFICATION:
            desc = FIELD_DESCRIPTIONS.get("fabric-object-unification", "")
            error_msg = f"Invalid value for 'fabric-object-unification': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FABRIC_OBJECT_UNIFICATION)}"
            error_msg += f"\n  → Example: fabric-object-unification='{{ VALID_BODY_FABRIC_OBJECT_UNIFICATION[0] }}'"
            return (False, error_msg)
    if "saml-configuration-sync" in payload:
        value = payload["saml-configuration-sync"]
        if value not in VALID_BODY_SAML_CONFIGURATION_SYNC:
            desc = FIELD_DESCRIPTIONS.get("saml-configuration-sync", "")
            error_msg = f"Invalid value for 'saml-configuration-sync': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SAML_CONFIGURATION_SYNC)}"
            error_msg += f"\n  → Example: saml-configuration-sync='{{ VALID_BODY_SAML_CONFIGURATION_SYNC[0] }}'"
            return (False, error_msg)
    if "forticloud-account-enforcement" in payload:
        value = payload["forticloud-account-enforcement"]
        if value not in VALID_BODY_FORTICLOUD_ACCOUNT_ENFORCEMENT:
            desc = FIELD_DESCRIPTIONS.get("forticloud-account-enforcement", "")
            error_msg = f"Invalid value for 'forticloud-account-enforcement': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FORTICLOUD_ACCOUNT_ENFORCEMENT)}"
            error_msg += f"\n  → Example: forticloud-account-enforcement='{{ VALID_BODY_FORTICLOUD_ACCOUNT_ENFORCEMENT[0] }}'"
            return (False, error_msg)
    if "file-mgmt" in payload:
        value = payload["file-mgmt"]
        if value not in VALID_BODY_FILE_MGMT:
            desc = FIELD_DESCRIPTIONS.get("file-mgmt", "")
            error_msg = f"Invalid value for 'file-mgmt': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FILE_MGMT)}"
            error_msg += f"\n  → Example: file-mgmt='{{ VALID_BODY_FILE_MGMT[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_system_csf_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update system/csf."""
    # Step 1: Validate enum values
    if "status" in payload:
        value = payload["status"]
        if value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid value for 'status'='{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )
    if "upstream-interface-select-method" in payload:
        value = payload["upstream-interface-select-method"]
        if value not in VALID_BODY_UPSTREAM_INTERFACE_SELECT_METHOD:
            return (
                False,
                f"Invalid value for 'upstream-interface-select-method'='{value}'. Must be one of: {', '.join(VALID_BODY_UPSTREAM_INTERFACE_SELECT_METHOD)}",
            )
    if "accept-auth-by-cert" in payload:
        value = payload["accept-auth-by-cert"]
        if value not in VALID_BODY_ACCEPT_AUTH_BY_CERT:
            return (
                False,
                f"Invalid value for 'accept-auth-by-cert'='{value}'. Must be one of: {', '.join(VALID_BODY_ACCEPT_AUTH_BY_CERT)}",
            )
    if "log-unification" in payload:
        value = payload["log-unification"]
        if value not in VALID_BODY_LOG_UNIFICATION:
            return (
                False,
                f"Invalid value for 'log-unification'='{value}'. Must be one of: {', '.join(VALID_BODY_LOG_UNIFICATION)}",
            )
    if "authorization-request-type" in payload:
        value = payload["authorization-request-type"]
        if value not in VALID_BODY_AUTHORIZATION_REQUEST_TYPE:
            return (
                False,
                f"Invalid value for 'authorization-request-type'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTHORIZATION_REQUEST_TYPE)}",
            )
    if "downstream-access" in payload:
        value = payload["downstream-access"]
        if value not in VALID_BODY_DOWNSTREAM_ACCESS:
            return (
                False,
                f"Invalid value for 'downstream-access'='{value}'. Must be one of: {', '.join(VALID_BODY_DOWNSTREAM_ACCESS)}",
            )
    if "legacy-authentication" in payload:
        value = payload["legacy-authentication"]
        if value not in VALID_BODY_LEGACY_AUTHENTICATION:
            return (
                False,
                f"Invalid value for 'legacy-authentication'='{value}'. Must be one of: {', '.join(VALID_BODY_LEGACY_AUTHENTICATION)}",
            )
    if "configuration-sync" in payload:
        value = payload["configuration-sync"]
        if value not in VALID_BODY_CONFIGURATION_SYNC:
            return (
                False,
                f"Invalid value for 'configuration-sync'='{value}'. Must be one of: {', '.join(VALID_BODY_CONFIGURATION_SYNC)}",
            )
    if "fabric-object-unification" in payload:
        value = payload["fabric-object-unification"]
        if value not in VALID_BODY_FABRIC_OBJECT_UNIFICATION:
            return (
                False,
                f"Invalid value for 'fabric-object-unification'='{value}'. Must be one of: {', '.join(VALID_BODY_FABRIC_OBJECT_UNIFICATION)}",
            )
    if "saml-configuration-sync" in payload:
        value = payload["saml-configuration-sync"]
        if value not in VALID_BODY_SAML_CONFIGURATION_SYNC:
            return (
                False,
                f"Invalid value for 'saml-configuration-sync'='{value}'. Must be one of: {', '.join(VALID_BODY_SAML_CONFIGURATION_SYNC)}",
            )
    if "forticloud-account-enforcement" in payload:
        value = payload["forticloud-account-enforcement"]
        if value not in VALID_BODY_FORTICLOUD_ACCOUNT_ENFORCEMENT:
            return (
                False,
                f"Invalid value for 'forticloud-account-enforcement'='{value}'. Must be one of: {', '.join(VALID_BODY_FORTICLOUD_ACCOUNT_ENFORCEMENT)}",
            )
    if "file-mgmt" in payload:
        value = payload["file-mgmt"]
        if value not in VALID_BODY_FILE_MGMT:
            return (
                False,
                f"Invalid value for 'file-mgmt'='{value}'. Must be one of: {', '.join(VALID_BODY_FILE_MGMT)}",
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
    "endpoint": "system/csf",
    "category": "cmdb",
    "api_path": "system/csf",
    "help": "Add this FortiGate to a Security Fabric or set up a new Security Fabric on this FortiGate.",
    "total_fields": 26,
    "required_fields_count": 2,
    "fields_with_defaults_count": 23,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
