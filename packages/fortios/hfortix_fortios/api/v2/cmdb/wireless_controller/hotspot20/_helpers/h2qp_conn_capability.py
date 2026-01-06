"""Validation helpers for wireless_controller/hotspot20/h2qp_conn_capability - Auto-generated"""

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
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "icmp-port": "unknown",
    "ftp-port": "unknown",
    "ssh-port": "unknown",
    "http-port": "unknown",
    "tls-port": "unknown",
    "pptp-vpn-port": "unknown",
    "voip-tcp-port": "unknown",
    "voip-udp-port": "unknown",
    "ikev2-port": "unknown",
    "ikev2-xx-port": "unknown",
    "esp-port": "unknown",
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
    "name": "string",  # Connection capability name.
    "icmp-port": "option",  # Set ICMP port service status.
    "ftp-port": "option",  # Set FTP port service status.
    "ssh-port": "option",  # Set SSH port service status.
    "http-port": "option",  # Set HTTP port service status.
    "tls-port": "option",  # Set TLS VPN (HTTPS) port service status.
    "pptp-vpn-port": "option",  # Set Point to Point Tunneling Protocol (PPTP) VPN port servic
    "voip-tcp-port": "option",  # Set VoIP TCP port service status.
    "voip-udp-port": "option",  # Set VoIP UDP port service status.
    "ikev2-port": "option",  # Set IKEv2 port service for IPsec VPN status.
    "ikev2-xx-port": "option",  # Set UDP port 4500 (which may be used by IKEv2 for IPsec VPN)
    "esp-port": "option",  # Set ESP port service (used by IPsec VPNs) status.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "Connection capability name.",
    "icmp-port": "Set ICMP port service status.",
    "ftp-port": "Set FTP port service status.",
    "ssh-port": "Set SSH port service status.",
    "http-port": "Set HTTP port service status.",
    "tls-port": "Set TLS VPN (HTTPS) port service status.",
    "pptp-vpn-port": "Set Point to Point Tunneling Protocol (PPTP) VPN port service status.",
    "voip-tcp-port": "Set VoIP TCP port service status.",
    "voip-udp-port": "Set VoIP UDP port service status.",
    "ikev2-port": "Set IKEv2 port service for IPsec VPN status.",
    "ikev2-xx-port": "Set UDP port 4500 (which may be used by IKEv2 for IPsec VPN) service status.",
    "esp-port": "Set ESP port service (used by IPsec VPNs) status.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 35},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
}


# Valid enum values from API documentation
VALID_BODY_ICMP_PORT = [
    "closed",  # The port is not open for communication.
    "open",  # The port is open for communication.
    "unknown",  # The port may or may not be open for communication.
]
VALID_BODY_FTP_PORT = [
    "closed",  # The port is not open for communication.
    "open",  # The port is open for communication.
    "unknown",  # The port may or may not be open for communication.
]
VALID_BODY_SSH_PORT = [
    "closed",  # The port is not open for communication.
    "open",  # The port is open for communication.
    "unknown",  # The port may or may not be open for communication.
]
VALID_BODY_HTTP_PORT = [
    "closed",  # The port is not open for communication.
    "open",  # The port is open for communication.
    "unknown",  # The port may or may not be open for communication.
]
VALID_BODY_TLS_PORT = [
    "closed",  # The port is not open for communication.
    "open",  # The port is open for communication.
    "unknown",  # The port may or may not be open for communication.
]
VALID_BODY_PPTP_VPN_PORT = [
    "closed",  # The port is not open for communication.
    "open",  # The port is open for communication.
    "unknown",  # The port may or may not be open for communication.
]
VALID_BODY_VOIP_TCP_PORT = [
    "closed",  # The port is not open for communication.
    "open",  # The port is open for communication.
    "unknown",  # The port may or may not be open for communication.
]
VALID_BODY_VOIP_UDP_PORT = [
    "closed",  # The port is not open for communication.
    "open",  # The port is open for communication.
    "unknown",  # The port may or may not be open for communication.
]
VALID_BODY_IKEV2_PORT = [
    "closed",  # The port is not open for communication.
    "open",  # The port is open for communication.
    "unknown",  # The port may or may not be open for communication.
]
VALID_BODY_IKEV2_XX_PORT = [
    "closed",  # The port is not open for communication.
    "open",  # The port is open for communication.
    "unknown",  # The port may or may not be open for communication.
]
VALID_BODY_ESP_PORT = [
    "closed",  # The port is not open for communication.
    "open",  # The port is open for communication.
    "unknown",  # The port may or may not be open for communication.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_wireless_controller_hotspot20_h2qp_conn_capability_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for wireless_controller/hotspot20/h2qp_conn_capability."""
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
    """Validate required fields for wireless_controller/hotspot20/h2qp_conn_capability."""
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


def validate_wireless_controller_hotspot20_h2qp_conn_capability_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new wireless_controller/hotspot20/h2qp_conn_capability object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "icmp-port" in payload:
        value = payload["icmp-port"]
        if value not in VALID_BODY_ICMP_PORT:
            desc = FIELD_DESCRIPTIONS.get("icmp-port", "")
            error_msg = f"Invalid value for 'icmp-port': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ICMP_PORT)}"
            error_msg += f"\n  → Example: icmp-port='{{ VALID_BODY_ICMP_PORT[0] }}'"
            return (False, error_msg)
    if "ftp-port" in payload:
        value = payload["ftp-port"]
        if value not in VALID_BODY_FTP_PORT:
            desc = FIELD_DESCRIPTIONS.get("ftp-port", "")
            error_msg = f"Invalid value for 'ftp-port': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FTP_PORT)}"
            error_msg += f"\n  → Example: ftp-port='{{ VALID_BODY_FTP_PORT[0] }}'"
            return (False, error_msg)
    if "ssh-port" in payload:
        value = payload["ssh-port"]
        if value not in VALID_BODY_SSH_PORT:
            desc = FIELD_DESCRIPTIONS.get("ssh-port", "")
            error_msg = f"Invalid value for 'ssh-port': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SSH_PORT)}"
            error_msg += f"\n  → Example: ssh-port='{{ VALID_BODY_SSH_PORT[0] }}'"
            return (False, error_msg)
    if "http-port" in payload:
        value = payload["http-port"]
        if value not in VALID_BODY_HTTP_PORT:
            desc = FIELD_DESCRIPTIONS.get("http-port", "")
            error_msg = f"Invalid value for 'http-port': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_HTTP_PORT)}"
            error_msg += f"\n  → Example: http-port='{{ VALID_BODY_HTTP_PORT[0] }}'"
            return (False, error_msg)
    if "tls-port" in payload:
        value = payload["tls-port"]
        if value not in VALID_BODY_TLS_PORT:
            desc = FIELD_DESCRIPTIONS.get("tls-port", "")
            error_msg = f"Invalid value for 'tls-port': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_TLS_PORT)}"
            error_msg += f"\n  → Example: tls-port='{{ VALID_BODY_TLS_PORT[0] }}'"
            return (False, error_msg)
    if "pptp-vpn-port" in payload:
        value = payload["pptp-vpn-port"]
        if value not in VALID_BODY_PPTP_VPN_PORT:
            desc = FIELD_DESCRIPTIONS.get("pptp-vpn-port", "")
            error_msg = f"Invalid value for 'pptp-vpn-port': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PPTP_VPN_PORT)}"
            error_msg += f"\n  → Example: pptp-vpn-port='{{ VALID_BODY_PPTP_VPN_PORT[0] }}'"
            return (False, error_msg)
    if "voip-tcp-port" in payload:
        value = payload["voip-tcp-port"]
        if value not in VALID_BODY_VOIP_TCP_PORT:
            desc = FIELD_DESCRIPTIONS.get("voip-tcp-port", "")
            error_msg = f"Invalid value for 'voip-tcp-port': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_VOIP_TCP_PORT)}"
            error_msg += f"\n  → Example: voip-tcp-port='{{ VALID_BODY_VOIP_TCP_PORT[0] }}'"
            return (False, error_msg)
    if "voip-udp-port" in payload:
        value = payload["voip-udp-port"]
        if value not in VALID_BODY_VOIP_UDP_PORT:
            desc = FIELD_DESCRIPTIONS.get("voip-udp-port", "")
            error_msg = f"Invalid value for 'voip-udp-port': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_VOIP_UDP_PORT)}"
            error_msg += f"\n  → Example: voip-udp-port='{{ VALID_BODY_VOIP_UDP_PORT[0] }}'"
            return (False, error_msg)
    if "ikev2-port" in payload:
        value = payload["ikev2-port"]
        if value not in VALID_BODY_IKEV2_PORT:
            desc = FIELD_DESCRIPTIONS.get("ikev2-port", "")
            error_msg = f"Invalid value for 'ikev2-port': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_IKEV2_PORT)}"
            error_msg += f"\n  → Example: ikev2-port='{{ VALID_BODY_IKEV2_PORT[0] }}'"
            return (False, error_msg)
    if "ikev2-xx-port" in payload:
        value = payload["ikev2-xx-port"]
        if value not in VALID_BODY_IKEV2_XX_PORT:
            desc = FIELD_DESCRIPTIONS.get("ikev2-xx-port", "")
            error_msg = f"Invalid value for 'ikev2-xx-port': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_IKEV2_XX_PORT)}"
            error_msg += f"\n  → Example: ikev2-xx-port='{{ VALID_BODY_IKEV2_XX_PORT[0] }}'"
            return (False, error_msg)
    if "esp-port" in payload:
        value = payload["esp-port"]
        if value not in VALID_BODY_ESP_PORT:
            desc = FIELD_DESCRIPTIONS.get("esp-port", "")
            error_msg = f"Invalid value for 'esp-port': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ESP_PORT)}"
            error_msg += f"\n  → Example: esp-port='{{ VALID_BODY_ESP_PORT[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_wireless_controller_hotspot20_h2qp_conn_capability_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update wireless_controller/hotspot20/h2qp_conn_capability."""
    # Step 1: Validate enum values
    if "icmp-port" in payload:
        value = payload["icmp-port"]
        if value not in VALID_BODY_ICMP_PORT:
            return (
                False,
                f"Invalid value for 'icmp-port'='{value}'. Must be one of: {', '.join(VALID_BODY_ICMP_PORT)}",
            )
    if "ftp-port" in payload:
        value = payload["ftp-port"]
        if value not in VALID_BODY_FTP_PORT:
            return (
                False,
                f"Invalid value for 'ftp-port'='{value}'. Must be one of: {', '.join(VALID_BODY_FTP_PORT)}",
            )
    if "ssh-port" in payload:
        value = payload["ssh-port"]
        if value not in VALID_BODY_SSH_PORT:
            return (
                False,
                f"Invalid value for 'ssh-port'='{value}'. Must be one of: {', '.join(VALID_BODY_SSH_PORT)}",
            )
    if "http-port" in payload:
        value = payload["http-port"]
        if value not in VALID_BODY_HTTP_PORT:
            return (
                False,
                f"Invalid value for 'http-port'='{value}'. Must be one of: {', '.join(VALID_BODY_HTTP_PORT)}",
            )
    if "tls-port" in payload:
        value = payload["tls-port"]
        if value not in VALID_BODY_TLS_PORT:
            return (
                False,
                f"Invalid value for 'tls-port'='{value}'. Must be one of: {', '.join(VALID_BODY_TLS_PORT)}",
            )
    if "pptp-vpn-port" in payload:
        value = payload["pptp-vpn-port"]
        if value not in VALID_BODY_PPTP_VPN_PORT:
            return (
                False,
                f"Invalid value for 'pptp-vpn-port'='{value}'. Must be one of: {', '.join(VALID_BODY_PPTP_VPN_PORT)}",
            )
    if "voip-tcp-port" in payload:
        value = payload["voip-tcp-port"]
        if value not in VALID_BODY_VOIP_TCP_PORT:
            return (
                False,
                f"Invalid value for 'voip-tcp-port'='{value}'. Must be one of: {', '.join(VALID_BODY_VOIP_TCP_PORT)}",
            )
    if "voip-udp-port" in payload:
        value = payload["voip-udp-port"]
        if value not in VALID_BODY_VOIP_UDP_PORT:
            return (
                False,
                f"Invalid value for 'voip-udp-port'='{value}'. Must be one of: {', '.join(VALID_BODY_VOIP_UDP_PORT)}",
            )
    if "ikev2-port" in payload:
        value = payload["ikev2-port"]
        if value not in VALID_BODY_IKEV2_PORT:
            return (
                False,
                f"Invalid value for 'ikev2-port'='{value}'. Must be one of: {', '.join(VALID_BODY_IKEV2_PORT)}",
            )
    if "ikev2-xx-port" in payload:
        value = payload["ikev2-xx-port"]
        if value not in VALID_BODY_IKEV2_XX_PORT:
            return (
                False,
                f"Invalid value for 'ikev2-xx-port'='{value}'. Must be one of: {', '.join(VALID_BODY_IKEV2_XX_PORT)}",
            )
    if "esp-port" in payload:
        value = payload["esp-port"]
        if value not in VALID_BODY_ESP_PORT:
            return (
                False,
                f"Invalid value for 'esp-port'='{value}'. Must be one of: {', '.join(VALID_BODY_ESP_PORT)}",
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
    "endpoint": "wireless_controller/hotspot20/h2qp_conn_capability",
    "category": "cmdb",
    "api_path": "wireless-controller.hotspot20/h2qp-conn-capability",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure connection capability.",
    "total_fields": 12,
    "required_fields_count": 0,
    "fields_with_defaults_count": 12,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
