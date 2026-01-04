"""
Validation helpers for endpoint_control/fctems_override endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification
Customize as needed for endpoint-specific business logic.
"""

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
#
# 1. FALSE POSITIVES: Some fields marked "required" have default values,
#    meaning they're optional (filtered out by generator)
#
# 2. CONDITIONAL REQUIREMENTS: Many endpoints require EITHER field A OR field B:
#    - firewall.policy: requires (srcaddr + dstaddr) OR (srcaddr6 + dstaddr6)
#    - These conditional requirements cannot be expressed in a simple list
#
# 3. SPECIALIZED FEATURES: Fields for WAN optimization, VPN, NAT64, etc.
#    are marked "required" but only apply when using those features
#
# The REQUIRED_FIELDS list below is INFORMATIONAL ONLY and shows fields that:
# - Are marked required in the schema
# - Don't have non-empty default values
# - Aren't specialized feature fields
#
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
    "enable",
    "disable",
]
VALID_BODY_DIRTY_REASON = [
    "none",
    "mismatched-ems-sn",
]
VALID_BODY_FORTINETONE_CLOUD_AUTHENTICATION = [
    "enable",
    "disable",
]
VALID_BODY_PULL_SYSINFO = [
    "enable",
    "disable",
]
VALID_BODY_PULL_VULNERABILITIES = [
    "enable",
    "disable",
]
VALID_BODY_PULL_TAGS = [
    "enable",
    "disable",
]
VALID_BODY_PULL_MALWARE_HASH = [
    "enable",
    "disable",
]
VALID_BODY_CAPABILITIES = [
    "fabric-auth",
    "silent-approval",
    "websocket",
    "websocket-malware",
    "push-ca-certs",
    "common-tags-api",
    "tenant-id",
    "client-avatars",
    "single-vdom-connector",
    "fgt-sysinfo-api",
    "ztna-server-info",
    "used-tags",
]
VALID_BODY_SEND_TAGS_TO_ALL_VDOMS = [
    "enable",
    "disable",
]
VALID_BODY_WEBSOCKET_OVERRIDE = [
    "enable",
    "disable",
]
VALID_BODY_INTERFACE_SELECT_METHOD = [
    "auto",
    "sdwan",
    "specify",
]
VALID_BODY_TRUST_CA_CN = [
    "enable",
    "disable",
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_endpoint_control_fctems_override_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters for endpoint_control/fctems_override.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_endpoint_control_fctems_override_get()
        >>> assert is_valid == True
        
        >>> # Valid - Get specific item by ems-id
        >>> is_valid, error = validate_endpoint_control_fctems_override_get(ems_id="test-item")
        >>> assert is_valid == True
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_endpoint_control_fctems_override_get(
        ...     filters={"format": "name|type"}
        ... )
        >>> assert is_valid == True
    """
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
    """
    Validate required fields for endpoint_control/fctems_override.

    This validator checks:
    1. Always-required fields are present
    2. Mutually exclusive groups have at least one field

    Args:
        payload: The request payload to validate

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "test"}
        >>> is_valid, error = validate_required_fields(payload)
    """
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


def validate_endpoint_control_fctems_override_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new endpoint_control/fctems_override object.

    This validator performs two-stage validation:
    1. Required fields check (schema-based)
    2. Field value validation (enums, ranges, formats)

    Args:
        payload: Request body data with configuration
        **params: Query parameters (vdom, etc.)

    Returns:
        Tuple of (is_valid, error_message)
        - is_valid: True if payload is valid, False otherwise
        - error_message: None if valid, detailed error string if invalid

    Examples:
        >>> # ✅ Valid - Minimal required fields
        >>> payload = {
        ...     "interface": True,  # Specify outgoing interface to reach server.
        ... }
        >>> is_valid, error = validate_endpoint_control_fctems_override_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "interface": True,
        ...     "status": "enable",  # Valid enum value
        ... }
        >>> is_valid, error = validate_endpoint_control_fctems_override_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["status"] = "invalid-value"
        >>> is_valid, error = validate_endpoint_control_fctems_override_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_endpoint_control_fctems_override_post(payload)
        >>> assert is_valid == False
        >>> assert "Missing required field" in error
    """
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


def validate_endpoint_control_fctems_override_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update endpoint_control/fctems_override.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_endpoint_control_fctems_override_put(payload)
    """
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
# Provide programmatic access to field metadata for IDE autocomplete,
# documentation generation, and dynamic validation
# ============================================================================


def get_field_description(field_name: str) -> str | None:
    """
    Get description/help text for a field.

    Args:
        field_name: Name of the field

    Returns:
        Description text or None if field doesn't exist

    Example:
        >>> desc = get_field_description("name")
        >>> print(desc)
    """
    return FIELD_DESCRIPTIONS.get(field_name)


def get_field_type(field_name: str) -> str | None:
    """
    Get the type of a field.

    Args:
        field_name: Name of the field

    Returns:
        Field type (e.g., "string", "integer", "option") or None

    Example:
        >>> field_type = get_field_type("status")
        >>> print(field_type)  # "option"
    """
    return FIELD_TYPES.get(field_name)


def get_field_constraints(field_name: str) -> dict[str, Any] | None:
    """
    Get constraints for a field (min/max values, string length).

    Args:
        field_name: Name of the field

    Returns:
        Constraint dict or None

    Example:
        >>> constraints = get_field_constraints("port")
        >>> print(constraints)  # {"type": "integer", "min": 1, "max": 65535}
    """
    return FIELD_CONSTRAINTS.get(field_name)


def get_field_default(field_name: str) -> Any | None:
    """
    Get default value for a field.

    Args:
        field_name: Name of the field

    Returns:
        Default value or None if no default

    Example:
        >>> default = get_field_default("status")
        >>> print(default)  # "enable"
    """
    return FIELDS_WITH_DEFAULTS.get(field_name)


def get_field_options(field_name: str) -> list[str] | None:
    """
    Get valid enum options for a field.

    Args:
        field_name: Name of the field

    Returns:
        List of valid values or None if not an enum field

    Example:
        >>> options = get_field_options("status")
        >>> print(options)  # ["enable", "disable"]
    """
    # Construct the constant name from field name
    # Replace all non-alphanumeric characters with underscores for valid Python identifiers
    import re
    safe_name = re.sub(r'[^a-zA-Z0-9]', '_', field_name)
    constant_name = f"VALID_BODY_{safe_name.upper()}"
    return globals().get(constant_name)


def get_nested_schema(field_name: str) -> dict[str, Any] | None:
    """
    Get schema for nested table/list fields.

    Args:
        field_name: Name of the parent field

    Returns:
        Dict mapping child field names to their metadata

    Example:
        >>> nested = get_nested_schema("members")
        >>> if nested:
        ...     for child_field, child_meta in nested.items():
        ...         print(f"{child_field}: {child_meta['type']}")
    """
    return NESTED_SCHEMAS.get(field_name)


def get_all_fields() -> list[str]:
    """
    Get list of all field names.

    Returns:
        List of all field names in the schema

    Example:
        >>> fields = get_all_fields()
        >>> print(len(fields))
    """
    return list(FIELD_TYPES.keys())


def get_field_metadata(field_name: str) -> dict[str, Any] | None:
    """
    Get complete metadata for a field (type, description, constraints, defaults, options).

    Args:
        field_name: Name of the field

    Returns:
        Dict with all available metadata or None if field doesn't exist

    Example:
        >>> meta = get_field_metadata("status")
        >>> print(meta)
        >>> # {
        >>> #   "type": "option",
        >>> #   "description": "Enable/disable this feature",
        >>> #   "default": "enable",
        >>> #   "options": ["enable", "disable"]
        >>> # }
    """
    if field_name not in FIELD_TYPES:
        return None

    metadata = {
        "name": field_name,
        "type": FIELD_TYPES[field_name],
    }

    # Add description if available
    if field_name in FIELD_DESCRIPTIONS:
        metadata["description"] = FIELD_DESCRIPTIONS[field_name]

    # Add constraints if available
    if field_name in FIELD_CONSTRAINTS:
        metadata["constraints"] = FIELD_CONSTRAINTS[field_name]

    # Add default if available
    if field_name in FIELDS_WITH_DEFAULTS:
        metadata["default"] = FIELDS_WITH_DEFAULTS[field_name]

    # Add required flag
    metadata["required"] = field_name in REQUIRED_FIELDS

    # Add options if available
    options = get_field_options(field_name)
    if options:
        metadata["options"] = options

    # Add nested schema if available
    nested = get_nested_schema(field_name)
    if nested:
        metadata["nested_schema"] = nested

    return metadata


def validate_field_value(field_name: str, value: Any) -> tuple[bool, str | None]:
    """
    Validate a single field value against its constraints.

    Args:
        field_name: Name of the field
        value: Value to validate

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> is_valid, error = validate_field_value("status", "enable")
        >>> if not is_valid:
        ...     print(error)
    """
    # Get field metadata
    field_type = get_field_type(field_name)
    if field_type is None:
        return (False, f"Unknown field: '{field_name}' (not defined in schema)")

    # Get field description for better error context
    description = get_field_description(field_name)

    # Validate enum values
    options = get_field_options(field_name)
    if options and value not in options:
        error_msg = f"Invalid value for '{field_name}': {repr(value)}"
        if description:
            error_msg += f"\n  → Description: {description}"
        error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in options)}"
        if options:
            error_msg += f"\n  → Example: {field_name}={repr(options[0])}"
        return (False, error_msg)

    # Validate constraints
    constraints = get_field_constraints(field_name)
    if constraints:
        constraint_type = constraints.get("type")

        if constraint_type == "integer":
            if not isinstance(value, int):
                error_msg = f"Field '{field_name}' must be an integer"
                if description:
                    error_msg += f"\n  → Description: {description}"
                error_msg += f"\n  → You provided: {type(value).__name__} = {repr(value)}"
                return (False, error_msg)

            min_val = constraints.get("min")
            max_val = constraints.get("max")

            if min_val is not None and value < min_val:
                error_msg = f"Field '{field_name}' value {value} is below minimum {min_val}"
                if description:
                    error_msg += f"\n  → Description: {description}"
                if max_val is not None:
                    error_msg += f"\n  → Valid range: {min_val} to {max_val}"
                return (False, error_msg)

            if max_val is not None and value > max_val:
                error_msg = f"Field '{field_name}' value {value} exceeds maximum {max_val}"
                if description:
                    error_msg += f"\n  → Description: {description}"
                if min_val is not None:
                    error_msg += f"\n  → Valid range: {min_val} to {max_val}"
                return (False, error_msg)

        elif constraint_type == "string":
            if not isinstance(value, str):
                error_msg = f"Field '{field_name}' must be a string"
                if description:
                    error_msg += f"\n  → Description: {description}"
                error_msg += f"\n  → You provided: {type(value).__name__} = {repr(value)}"
                return (False, error_msg)

            max_length = constraints.get("max_length")
            if max_length and len(value) > max_length:
                error_msg = f"Field '{field_name}' length {len(value)} exceeds maximum {max_length}"
                if description:
                    error_msg += f"\n  → Description: {description}"
                error_msg += f"\n  → Your value: {repr(value[:50])}{'...' if len(value) > 50 else ''}"
                return (False, error_msg)

    return (True, None)


# ============================================================================
# Schema Information
# Metadata about this endpoint schema
# ============================================================================

SCHEMA_INFO = {
    "endpoint": "endpoint_control/fctems_override",
    "category": "cmdb",
    "api_path": "endpoint-control/fctems-override",
    "mkey": "ems-id",
    "mkey_type": "integer",
    "help": "Configure FortiClient Enterprise Management Server (EMS) entries.",
    "total_fields": 24,
    "required_fields_count": 1,
    "fields_with_defaults_count": 23,
}


def get_schema_info() -> dict[str, Any]:
    """
    Get information about this endpoint schema.

    Returns:
        Dict with schema metadata

    Example:
        >>> info = get_schema_info()
        >>> print(f"Endpoint: {info['endpoint']}")
        >>> print(f"Total fields: {info['total_fields']}")
    """
    return SCHEMA_INFO.copy()
