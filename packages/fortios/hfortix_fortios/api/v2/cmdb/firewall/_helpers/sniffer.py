"""Validation helpers for firewall/sniffer - Auto-generated"""

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
    "application-list",  # Name of an existing application list.
    "ips-sensor",  # Name of an existing IPS sensor.
    "av-profile",  # Name of an existing antivirus profile.
    "webfilter-profile",  # Name of an existing web filter profile.
    "emailfilter-profile",  # Name of an existing email filter profile.
    "dlp-profile",  # Name of an existing DLP profile.
    "file-filter-profile",  # Name of an existing file-filter profile.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "id": 0,
    "uuid": "00000000-0000-0000-0000-000000000000",
    "status": "enable",
    "logtraffic": "utm",
    "ipv6": "disable",
    "non-ip": "disable",
    "interface": "",
    "host": "",
    "port": "",
    "protocol": "",
    "vlan": "",
    "application-list-status": "disable",
    "application-list": "",
    "ips-sensor-status": "disable",
    "ips-sensor": "",
    "dsri": "disable",
    "av-profile-status": "disable",
    "av-profile": "",
    "webfilter-profile-status": "disable",
    "webfilter-profile": "",
    "emailfilter-profile-status": "disable",
    "emailfilter-profile": "",
    "dlp-profile-status": "disable",
    "dlp-profile": "",
    "ip-threatfeed-status": "disable",
    "file-filter-profile-status": "disable",
    "file-filter-profile": "",
    "ips-dos-status": "disable",
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
    "id": "integer",  # Sniffer ID (0 - 9999).
    "uuid": "uuid",  # Universally Unique Identifier (UUID; automatically assigned 
    "status": "option",  # Enable/disable the active status of the sniffer.
    "logtraffic": "option",  # Either log all sessions, only sessions that have a security 
    "ipv6": "option",  # Enable/disable sniffing IPv6 packets.
    "non-ip": "option",  # Enable/disable sniffing non-IP packets.
    "interface": "string",  # Interface name that traffic sniffing will take place on.
    "host": "string",  # Hosts to filter for in sniffer traffic (Format examples: 1.1
    "port": "string",  # Ports to sniff (Format examples: 10, :20, 30:40, 50-, 100-20
    "protocol": "string",  # Integer value for the protocol type as defined by IANA (0 - 
    "vlan": "string",  # List of VLANs to sniff.
    "application-list-status": "option",  # Enable/disable application control profile.
    "application-list": "string",  # Name of an existing application list.
    "ips-sensor-status": "option",  # Enable/disable IPS sensor.
    "ips-sensor": "string",  # Name of an existing IPS sensor.
    "dsri": "option",  # Enable/disable DSRI.
    "av-profile-status": "option",  # Enable/disable antivirus profile.
    "av-profile": "string",  # Name of an existing antivirus profile.
    "webfilter-profile-status": "option",  # Enable/disable web filter profile.
    "webfilter-profile": "string",  # Name of an existing web filter profile.
    "emailfilter-profile-status": "option",  # Enable/disable emailfilter.
    "emailfilter-profile": "string",  # Name of an existing email filter profile.
    "dlp-profile-status": "option",  # Enable/disable DLP profile.
    "dlp-profile": "string",  # Name of an existing DLP profile.
    "ip-threatfeed-status": "option",  # Enable/disable IP threat feed.
    "ip-threatfeed": "string",  # Name of an existing IP threat feed.
    "file-filter-profile-status": "option",  # Enable/disable file filter.
    "file-filter-profile": "string",  # Name of an existing file-filter profile.
    "ips-dos-status": "option",  # Enable/disable IPS DoS anomaly detection.
    "anomaly": "string",  # Configuration method to edit Denial of Service (DoS) anomaly
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "id": "Sniffer ID (0 - 9999).",
    "uuid": "Universally Unique Identifier (UUID; automatically assigned but can be manually reset).",
    "status": "Enable/disable the active status of the sniffer.",
    "logtraffic": "Either log all sessions, only sessions that have a security profile applied, or disable all logging for this policy.",
    "ipv6": "Enable/disable sniffing IPv6 packets.",
    "non-ip": "Enable/disable sniffing non-IP packets.",
    "interface": "Interface name that traffic sniffing will take place on.",
    "host": "Hosts to filter for in sniffer traffic (Format examples: 1.1.1.1, 2.2.2.0/24, 3.3.3.3/255.255.255.0, 4.4.4.0-4.4.4.240).",
    "port": "Ports to sniff (Format examples: 10, :20, 30:40, 50-, 100-200).",
    "protocol": "Integer value for the protocol type as defined by IANA (0 - 255).",
    "vlan": "List of VLANs to sniff.",
    "application-list-status": "Enable/disable application control profile.",
    "application-list": "Name of an existing application list.",
    "ips-sensor-status": "Enable/disable IPS sensor.",
    "ips-sensor": "Name of an existing IPS sensor.",
    "dsri": "Enable/disable DSRI.",
    "av-profile-status": "Enable/disable antivirus profile.",
    "av-profile": "Name of an existing antivirus profile.",
    "webfilter-profile-status": "Enable/disable web filter profile.",
    "webfilter-profile": "Name of an existing web filter profile.",
    "emailfilter-profile-status": "Enable/disable emailfilter.",
    "emailfilter-profile": "Name of an existing email filter profile.",
    "dlp-profile-status": "Enable/disable DLP profile.",
    "dlp-profile": "Name of an existing DLP profile.",
    "ip-threatfeed-status": "Enable/disable IP threat feed.",
    "ip-threatfeed": "Name of an existing IP threat feed.",
    "file-filter-profile-status": "Enable/disable file filter.",
    "file-filter-profile": "Name of an existing file-filter profile.",
    "ips-dos-status": "Enable/disable IPS DoS anomaly detection.",
    "anomaly": "Configuration method to edit Denial of Service (DoS) anomaly settings.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "id": {"type": "integer", "min": 0, "max": 9999},
    "interface": {"type": "string", "max_length": 35},
    "host": {"type": "string", "max_length": 63},
    "port": {"type": "string", "max_length": 63},
    "protocol": {"type": "string", "max_length": 63},
    "vlan": {"type": "string", "max_length": 63},
    "application-list": {"type": "string", "max_length": 47},
    "ips-sensor": {"type": "string", "max_length": 47},
    "av-profile": {"type": "string", "max_length": 47},
    "webfilter-profile": {"type": "string", "max_length": 47},
    "emailfilter-profile": {"type": "string", "max_length": 47},
    "dlp-profile": {"type": "string", "max_length": 47},
    "file-filter-profile": {"type": "string", "max_length": 47},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "ip-threatfeed": {
        "name": {
            "type": "string",
            "help": "Threat feed name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "anomaly": {
        "name": {
            "type": "string",
            "help": "Anomaly name.",
            "default": "",
            "max_length": 63,
        },
        "status": {
            "type": "option",
            "help": "Enable/disable this anomaly.",
            "default": "disable",
            "options": [{"help": "Disable this status.", "label": "Disable", "name": "disable"}, {"help": "Enable this status.", "label": "Enable", "name": "enable"}],
        },
        "log": {
            "type": "option",
            "help": "Enable/disable anomaly logging.",
            "default": "disable",
            "options": [{"help": "Enable anomaly logging.", "label": "Enable", "name": "enable"}, {"help": "Disable anomaly logging.", "label": "Disable", "name": "disable"}],
        },
        "action": {
            "type": "option",
            "help": "Action taken when the threshold is reached.",
            "default": "pass",
            "options": [{"help": "Allow traffic but record a log message if logging is enabled.", "label": "Pass", "name": "pass"}, {"help": "Block traffic if this anomaly is found.", "label": "Block", "name": "block"}],
        },
        "quarantine": {
            "type": "option",
            "help": "Quarantine method.",
            "default": "none",
            "options": [{"help": "Quarantine is disabled.", "label": "None", "name": "none"}, {"help": "Block all traffic sent from attacker\u0027s IP address. The attacker\u0027s IP address is also added to the banned user list. The target\u0027s address is not affected.", "label": "Attacker", "name": "attacker"}],
        },
        "quarantine-expiry": {
            "type": "user",
            "help": "Duration of quarantine. (Format ###d##h##m, minimum 1m, maximum 364d23h59m, default = 5m). Requires quarantine set to attacker.",
            "default": "5m",
        },
        "quarantine-log": {
            "type": "option",
            "help": "Enable/disable quarantine logging.",
            "default": "enable",
            "options": [{"help": "Disable quarantine logging.", "label": "Disable", "name": "disable"}, {"help": "Enable quarantine logging.", "label": "Enable", "name": "enable"}],
        },
        "threshold": {
            "type": "integer",
            "help": "Anomaly threshold. Number of detected instances (packets per second or concurrent session number) that triggers the anomaly action.",
            "default": 0,
            "min_value": 1,
            "max_value": 2147483647,
        },
        "threshold(default)": {
            "type": "integer",
            "help": "Number of detected instances (packets per second or concurrent session number) which triggers action (1 - 2147483647, default = 1000). Note that each anomaly has a different threshold value assigned to it.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_STATUS = [
    "enable",  # Enable sniffer status.
    "disable",  # Disable sniffer status.
]
VALID_BODY_LOGTRAFFIC = [
    "all",  # Log all sessions accepted or denied by this policy.
    "utm",  # Log traffic that has a security profile applied to it.
    "disable",  # Disable all logging for this policy.
]
VALID_BODY_IPV6 = [
    "enable",  # Enable sniffer for IPv6 packets.
    "disable",  # Disable sniffer for IPv6 packets.
]
VALID_BODY_NON_IP = [
    "enable",  # Enable sniffer for non-IP packets.
    "disable",  # Disable sniffer for non-IP packets.
]
VALID_BODY_APPLICATION_LIST_STATUS = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_IPS_SENSOR_STATUS = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_DSRI = [
    "enable",  # Enable DSRI.
    "disable",  # Disable DSRI.
]
VALID_BODY_AV_PROFILE_STATUS = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_WEBFILTER_PROFILE_STATUS = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_EMAILFILTER_PROFILE_STATUS = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_DLP_PROFILE_STATUS = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_IP_THREATFEED_STATUS = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_FILE_FILTER_PROFILE_STATUS = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_IPS_DOS_STATUS = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_firewall_sniffer_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for firewall/sniffer."""
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
    """Validate required fields for firewall/sniffer."""
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


def validate_firewall_sniffer_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new firewall/sniffer object."""
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
    if "logtraffic" in payload:
        value = payload["logtraffic"]
        if value not in VALID_BODY_LOGTRAFFIC:
            desc = FIELD_DESCRIPTIONS.get("logtraffic", "")
            error_msg = f"Invalid value for 'logtraffic': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LOGTRAFFIC)}"
            error_msg += f"\n  → Example: logtraffic='{{ VALID_BODY_LOGTRAFFIC[0] }}'"
            return (False, error_msg)
    if "ipv6" in payload:
        value = payload["ipv6"]
        if value not in VALID_BODY_IPV6:
            desc = FIELD_DESCRIPTIONS.get("ipv6", "")
            error_msg = f"Invalid value for 'ipv6': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_IPV6)}"
            error_msg += f"\n  → Example: ipv6='{{ VALID_BODY_IPV6[0] }}'"
            return (False, error_msg)
    if "non-ip" in payload:
        value = payload["non-ip"]
        if value not in VALID_BODY_NON_IP:
            desc = FIELD_DESCRIPTIONS.get("non-ip", "")
            error_msg = f"Invalid value for 'non-ip': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_NON_IP)}"
            error_msg += f"\n  → Example: non-ip='{{ VALID_BODY_NON_IP[0] }}'"
            return (False, error_msg)
    if "application-list-status" in payload:
        value = payload["application-list-status"]
        if value not in VALID_BODY_APPLICATION_LIST_STATUS:
            desc = FIELD_DESCRIPTIONS.get("application-list-status", "")
            error_msg = f"Invalid value for 'application-list-status': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_APPLICATION_LIST_STATUS)}"
            error_msg += f"\n  → Example: application-list-status='{{ VALID_BODY_APPLICATION_LIST_STATUS[0] }}'"
            return (False, error_msg)
    if "ips-sensor-status" in payload:
        value = payload["ips-sensor-status"]
        if value not in VALID_BODY_IPS_SENSOR_STATUS:
            desc = FIELD_DESCRIPTIONS.get("ips-sensor-status", "")
            error_msg = f"Invalid value for 'ips-sensor-status': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_IPS_SENSOR_STATUS)}"
            error_msg += f"\n  → Example: ips-sensor-status='{{ VALID_BODY_IPS_SENSOR_STATUS[0] }}'"
            return (False, error_msg)
    if "dsri" in payload:
        value = payload["dsri"]
        if value not in VALID_BODY_DSRI:
            desc = FIELD_DESCRIPTIONS.get("dsri", "")
            error_msg = f"Invalid value for 'dsri': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DSRI)}"
            error_msg += f"\n  → Example: dsri='{{ VALID_BODY_DSRI[0] }}'"
            return (False, error_msg)
    if "av-profile-status" in payload:
        value = payload["av-profile-status"]
        if value not in VALID_BODY_AV_PROFILE_STATUS:
            desc = FIELD_DESCRIPTIONS.get("av-profile-status", "")
            error_msg = f"Invalid value for 'av-profile-status': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AV_PROFILE_STATUS)}"
            error_msg += f"\n  → Example: av-profile-status='{{ VALID_BODY_AV_PROFILE_STATUS[0] }}'"
            return (False, error_msg)
    if "webfilter-profile-status" in payload:
        value = payload["webfilter-profile-status"]
        if value not in VALID_BODY_WEBFILTER_PROFILE_STATUS:
            desc = FIELD_DESCRIPTIONS.get("webfilter-profile-status", "")
            error_msg = f"Invalid value for 'webfilter-profile-status': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WEBFILTER_PROFILE_STATUS)}"
            error_msg += f"\n  → Example: webfilter-profile-status='{{ VALID_BODY_WEBFILTER_PROFILE_STATUS[0] }}'"
            return (False, error_msg)
    if "emailfilter-profile-status" in payload:
        value = payload["emailfilter-profile-status"]
        if value not in VALID_BODY_EMAILFILTER_PROFILE_STATUS:
            desc = FIELD_DESCRIPTIONS.get("emailfilter-profile-status", "")
            error_msg = f"Invalid value for 'emailfilter-profile-status': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_EMAILFILTER_PROFILE_STATUS)}"
            error_msg += f"\n  → Example: emailfilter-profile-status='{{ VALID_BODY_EMAILFILTER_PROFILE_STATUS[0] }}'"
            return (False, error_msg)
    if "dlp-profile-status" in payload:
        value = payload["dlp-profile-status"]
        if value not in VALID_BODY_DLP_PROFILE_STATUS:
            desc = FIELD_DESCRIPTIONS.get("dlp-profile-status", "")
            error_msg = f"Invalid value for 'dlp-profile-status': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DLP_PROFILE_STATUS)}"
            error_msg += f"\n  → Example: dlp-profile-status='{{ VALID_BODY_DLP_PROFILE_STATUS[0] }}'"
            return (False, error_msg)
    if "ip-threatfeed-status" in payload:
        value = payload["ip-threatfeed-status"]
        if value not in VALID_BODY_IP_THREATFEED_STATUS:
            desc = FIELD_DESCRIPTIONS.get("ip-threatfeed-status", "")
            error_msg = f"Invalid value for 'ip-threatfeed-status': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_IP_THREATFEED_STATUS)}"
            error_msg += f"\n  → Example: ip-threatfeed-status='{{ VALID_BODY_IP_THREATFEED_STATUS[0] }}'"
            return (False, error_msg)
    if "file-filter-profile-status" in payload:
        value = payload["file-filter-profile-status"]
        if value not in VALID_BODY_FILE_FILTER_PROFILE_STATUS:
            desc = FIELD_DESCRIPTIONS.get("file-filter-profile-status", "")
            error_msg = f"Invalid value for 'file-filter-profile-status': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FILE_FILTER_PROFILE_STATUS)}"
            error_msg += f"\n  → Example: file-filter-profile-status='{{ VALID_BODY_FILE_FILTER_PROFILE_STATUS[0] }}'"
            return (False, error_msg)
    if "ips-dos-status" in payload:
        value = payload["ips-dos-status"]
        if value not in VALID_BODY_IPS_DOS_STATUS:
            desc = FIELD_DESCRIPTIONS.get("ips-dos-status", "")
            error_msg = f"Invalid value for 'ips-dos-status': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_IPS_DOS_STATUS)}"
            error_msg += f"\n  → Example: ips-dos-status='{{ VALID_BODY_IPS_DOS_STATUS[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_firewall_sniffer_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update firewall/sniffer."""
    # Step 1: Validate enum values
    if "status" in payload:
        value = payload["status"]
        if value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid value for 'status'='{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )
    if "logtraffic" in payload:
        value = payload["logtraffic"]
        if value not in VALID_BODY_LOGTRAFFIC:
            return (
                False,
                f"Invalid value for 'logtraffic'='{value}'. Must be one of: {', '.join(VALID_BODY_LOGTRAFFIC)}",
            )
    if "ipv6" in payload:
        value = payload["ipv6"]
        if value not in VALID_BODY_IPV6:
            return (
                False,
                f"Invalid value for 'ipv6'='{value}'. Must be one of: {', '.join(VALID_BODY_IPV6)}",
            )
    if "non-ip" in payload:
        value = payload["non-ip"]
        if value not in VALID_BODY_NON_IP:
            return (
                False,
                f"Invalid value for 'non-ip'='{value}'. Must be one of: {', '.join(VALID_BODY_NON_IP)}",
            )
    if "application-list-status" in payload:
        value = payload["application-list-status"]
        if value not in VALID_BODY_APPLICATION_LIST_STATUS:
            return (
                False,
                f"Invalid value for 'application-list-status'='{value}'. Must be one of: {', '.join(VALID_BODY_APPLICATION_LIST_STATUS)}",
            )
    if "ips-sensor-status" in payload:
        value = payload["ips-sensor-status"]
        if value not in VALID_BODY_IPS_SENSOR_STATUS:
            return (
                False,
                f"Invalid value for 'ips-sensor-status'='{value}'. Must be one of: {', '.join(VALID_BODY_IPS_SENSOR_STATUS)}",
            )
    if "dsri" in payload:
        value = payload["dsri"]
        if value not in VALID_BODY_DSRI:
            return (
                False,
                f"Invalid value for 'dsri'='{value}'. Must be one of: {', '.join(VALID_BODY_DSRI)}",
            )
    if "av-profile-status" in payload:
        value = payload["av-profile-status"]
        if value not in VALID_BODY_AV_PROFILE_STATUS:
            return (
                False,
                f"Invalid value for 'av-profile-status'='{value}'. Must be one of: {', '.join(VALID_BODY_AV_PROFILE_STATUS)}",
            )
    if "webfilter-profile-status" in payload:
        value = payload["webfilter-profile-status"]
        if value not in VALID_BODY_WEBFILTER_PROFILE_STATUS:
            return (
                False,
                f"Invalid value for 'webfilter-profile-status'='{value}'. Must be one of: {', '.join(VALID_BODY_WEBFILTER_PROFILE_STATUS)}",
            )
    if "emailfilter-profile-status" in payload:
        value = payload["emailfilter-profile-status"]
        if value not in VALID_BODY_EMAILFILTER_PROFILE_STATUS:
            return (
                False,
                f"Invalid value for 'emailfilter-profile-status'='{value}'. Must be one of: {', '.join(VALID_BODY_EMAILFILTER_PROFILE_STATUS)}",
            )
    if "dlp-profile-status" in payload:
        value = payload["dlp-profile-status"]
        if value not in VALID_BODY_DLP_PROFILE_STATUS:
            return (
                False,
                f"Invalid value for 'dlp-profile-status'='{value}'. Must be one of: {', '.join(VALID_BODY_DLP_PROFILE_STATUS)}",
            )
    if "ip-threatfeed-status" in payload:
        value = payload["ip-threatfeed-status"]
        if value not in VALID_BODY_IP_THREATFEED_STATUS:
            return (
                False,
                f"Invalid value for 'ip-threatfeed-status'='{value}'. Must be one of: {', '.join(VALID_BODY_IP_THREATFEED_STATUS)}",
            )
    if "file-filter-profile-status" in payload:
        value = payload["file-filter-profile-status"]
        if value not in VALID_BODY_FILE_FILTER_PROFILE_STATUS:
            return (
                False,
                f"Invalid value for 'file-filter-profile-status'='{value}'. Must be one of: {', '.join(VALID_BODY_FILE_FILTER_PROFILE_STATUS)}",
            )
    if "ips-dos-status" in payload:
        value = payload["ips-dos-status"]
        if value not in VALID_BODY_IPS_DOS_STATUS:
            return (
                False,
                f"Invalid value for 'ips-dos-status'='{value}'. Must be one of: {', '.join(VALID_BODY_IPS_DOS_STATUS)}",
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
    "endpoint": "firewall/sniffer",
    "category": "cmdb",
    "api_path": "firewall/sniffer",
    "mkey": "id",
    "mkey_type": "integer",
    "help": "Configure sniffer.",
    "total_fields": 30,
    "required_fields_count": 7,
    "fields_with_defaults_count": 28,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
