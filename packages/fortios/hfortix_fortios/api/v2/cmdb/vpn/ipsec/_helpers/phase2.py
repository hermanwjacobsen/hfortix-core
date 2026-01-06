"""Validation helpers for vpn/ipsec/phase2 - Auto-generated"""

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
    "phase1name",  # Phase 1 determines the options required for phase 2.
    "proposal",  # Phase2 proposal.
    "src-name",  # Local proxy ID name.
    "src-name6",  # Local proxy ID name.
    "dst-name",  # Remote proxy ID name.
    "dst-name6",  # Remote proxy ID name.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "phase1name": "",
    "dhcp-ipsec": "disable",
    "use-natip": "enable",
    "selector-match": "auto",
    "proposal": "",
    "pfs": "enable",
    "dhgrp": "20",
    "addke1": "",
    "addke2": "",
    "addke3": "",
    "addke4": "",
    "addke5": "",
    "addke6": "",
    "addke7": "",
    "replay": "enable",
    "keepalive": "disable",
    "auto-negotiate": "disable",
    "add-route": "phase1",
    "inbound-dscp-copy": "phase1",
    "keylifeseconds": 43200,
    "keylifekbs": 5120,
    "keylife-type": "seconds",
    "single-source": "disable",
    "route-overlap": "use-new",
    "encapsulation": "tunnel-mode",
    "l2tp": "disable",
    "initiator-ts-narrow": "disable",
    "diffserv": "disable",
    "diffservcode": "",
    "protocol": 0,
    "src-name": "",
    "src-name6": "",
    "src-addr-type": "subnet",
    "src-start-ip": "0.0.0.0",
    "src-start-ip6": "::",
    "src-end-ip": "0.0.0.0",
    "src-end-ip6": "::",
    "src-subnet": "0.0.0.0 0.0.0.0",
    "src-subnet6": "::/0",
    "src-port": 0,
    "dst-name": "",
    "dst-name6": "",
    "dst-addr-type": "subnet",
    "dst-start-ip": "0.0.0.0",
    "dst-start-ip6": "::",
    "dst-end-ip": "0.0.0.0",
    "dst-end-ip6": "::",
    "dst-subnet": "0.0.0.0 0.0.0.0",
    "dst-subnet6": "::/0",
    "dst-port": 0,
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
    "name": "string",  # IPsec tunnel name.
    "phase1name": "string",  # Phase 1 determines the options required for phase 2.
    "dhcp-ipsec": "option",  # Enable/disable DHCP-IPsec.
    "use-natip": "option",  # Enable to use the FortiGate public IP as the source selector
    "selector-match": "option",  # Match type to use when comparing selectors.
    "proposal": "option",  # Phase2 proposal.
    "pfs": "option",  # Enable/disable PFS feature.
    "dhgrp": "option",  # Phase2 DH group.
    "addke1": "option",  # phase2 ADDKE1 group.
    "addke2": "option",  # phase2 ADDKE2 group.
    "addke3": "option",  # phase2 ADDKE3 group.
    "addke4": "option",  # phase2 ADDKE4 group.
    "addke5": "option",  # phase2 ADDKE5 group.
    "addke6": "option",  # phase2 ADDKE6 group.
    "addke7": "option",  # phase2 ADDKE7 group.
    "replay": "option",  # Enable/disable replay detection.
    "keepalive": "option",  # Enable/disable keep alive.
    "auto-negotiate": "option",  # Enable/disable IPsec SA auto-negotiation.
    "add-route": "option",  # Enable/disable automatic route addition.
    "inbound-dscp-copy": "option",  # Enable/disable copying of the DSCP in the ESP header to the 
    "keylifeseconds": "integer",  # Phase2 key life in time in seconds (120 - 172800).
    "keylifekbs": "integer",  # Phase2 key life in number of kilobytes of traffic (5120 - 42
    "keylife-type": "option",  # Keylife type.
    "single-source": "option",  # Enable/disable single source IP restriction.
    "route-overlap": "option",  # Action for overlapping routes.
    "encapsulation": "option",  # ESP encapsulation mode.
    "l2tp": "option",  # Enable/disable L2TP over IPsec.
    "comments": "var-string",  # Comment.
    "initiator-ts-narrow": "option",  # Enable/disable traffic selector narrowing for IKEv2 initiato
    "diffserv": "option",  # Enable/disable applying DSCP value to the IPsec tunnel outer
    "diffservcode": "user",  # DSCP value to be applied to the IPsec tunnel outer IP header
    "protocol": "integer",  # Quick mode protocol selector (1 - 255 or 0 for all).
    "src-name": "string",  # Local proxy ID name.
    "src-name6": "string",  # Local proxy ID name.
    "src-addr-type": "option",  # Local proxy ID type.
    "src-start-ip": "ipv4-address-any",  # Local proxy ID start.
    "src-start-ip6": "ipv6-address",  # Local proxy ID IPv6 start.
    "src-end-ip": "ipv4-address-any",  # Local proxy ID end.
    "src-end-ip6": "ipv6-address",  # Local proxy ID IPv6 end.
    "src-subnet": "ipv4-classnet-any",  # Local proxy ID subnet.
    "src-subnet6": "ipv6-prefix",  # Local proxy ID IPv6 subnet.
    "src-port": "integer",  # Quick mode source port (1 - 65535 or 0 for all).
    "dst-name": "string",  # Remote proxy ID name.
    "dst-name6": "string",  # Remote proxy ID name.
    "dst-addr-type": "option",  # Remote proxy ID type.
    "dst-start-ip": "ipv4-address-any",  # Remote proxy ID IPv4 start.
    "dst-start-ip6": "ipv6-address",  # Remote proxy ID IPv6 start.
    "dst-end-ip": "ipv4-address-any",  # Remote proxy ID IPv4 end.
    "dst-end-ip6": "ipv6-address",  # Remote proxy ID IPv6 end.
    "dst-subnet": "ipv4-classnet-any",  # Remote proxy ID IPv4 subnet.
    "dst-subnet6": "ipv6-prefix",  # Remote proxy ID IPv6 subnet.
    "dst-port": "integer",  # Quick mode destination port (1 - 65535 or 0 for all).
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "IPsec tunnel name.",
    "phase1name": "Phase 1 determines the options required for phase 2.",
    "dhcp-ipsec": "Enable/disable DHCP-IPsec.",
    "use-natip": "Enable to use the FortiGate public IP as the source selector when outbound NAT is used.",
    "selector-match": "Match type to use when comparing selectors.",
    "proposal": "Phase2 proposal.",
    "pfs": "Enable/disable PFS feature.",
    "dhgrp": "Phase2 DH group.",
    "addke1": "phase2 ADDKE1 group.",
    "addke2": "phase2 ADDKE2 group.",
    "addke3": "phase2 ADDKE3 group.",
    "addke4": "phase2 ADDKE4 group.",
    "addke5": "phase2 ADDKE5 group.",
    "addke6": "phase2 ADDKE6 group.",
    "addke7": "phase2 ADDKE7 group.",
    "replay": "Enable/disable replay detection.",
    "keepalive": "Enable/disable keep alive.",
    "auto-negotiate": "Enable/disable IPsec SA auto-negotiation.",
    "add-route": "Enable/disable automatic route addition.",
    "inbound-dscp-copy": "Enable/disable copying of the DSCP in the ESP header to the inner IP header.",
    "keylifeseconds": "Phase2 key life in time in seconds (120 - 172800).",
    "keylifekbs": "Phase2 key life in number of kilobytes of traffic (5120 - 4294967295).",
    "keylife-type": "Keylife type.",
    "single-source": "Enable/disable single source IP restriction.",
    "route-overlap": "Action for overlapping routes.",
    "encapsulation": "ESP encapsulation mode.",
    "l2tp": "Enable/disable L2TP over IPsec.",
    "comments": "Comment.",
    "initiator-ts-narrow": "Enable/disable traffic selector narrowing for IKEv2 initiator.",
    "diffserv": "Enable/disable applying DSCP value to the IPsec tunnel outer IP header.",
    "diffservcode": "DSCP value to be applied to the IPsec tunnel outer IP header.",
    "protocol": "Quick mode protocol selector (1 - 255 or 0 for all).",
    "src-name": "Local proxy ID name.",
    "src-name6": "Local proxy ID name.",
    "src-addr-type": "Local proxy ID type.",
    "src-start-ip": "Local proxy ID start.",
    "src-start-ip6": "Local proxy ID IPv6 start.",
    "src-end-ip": "Local proxy ID end.",
    "src-end-ip6": "Local proxy ID IPv6 end.",
    "src-subnet": "Local proxy ID subnet.",
    "src-subnet6": "Local proxy ID IPv6 subnet.",
    "src-port": "Quick mode source port (1 - 65535 or 0 for all).",
    "dst-name": "Remote proxy ID name.",
    "dst-name6": "Remote proxy ID name.",
    "dst-addr-type": "Remote proxy ID type.",
    "dst-start-ip": "Remote proxy ID IPv4 start.",
    "dst-start-ip6": "Remote proxy ID IPv6 start.",
    "dst-end-ip": "Remote proxy ID IPv4 end.",
    "dst-end-ip6": "Remote proxy ID IPv6 end.",
    "dst-subnet": "Remote proxy ID IPv4 subnet.",
    "dst-subnet6": "Remote proxy ID IPv6 subnet.",
    "dst-port": "Quick mode destination port (1 - 65535 or 0 for all).",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 35},
    "phase1name": {"type": "string", "max_length": 35},
    "keylifeseconds": {"type": "integer", "min": 120, "max": 172800},
    "keylifekbs": {"type": "integer", "min": 5120, "max": 4294967295},
    "protocol": {"type": "integer", "min": 0, "max": 255},
    "src-name": {"type": "string", "max_length": 79},
    "src-name6": {"type": "string", "max_length": 79},
    "src-port": {"type": "integer", "min": 0, "max": 65535},
    "dst-name": {"type": "string", "max_length": 79},
    "dst-name6": {"type": "string", "max_length": 79},
    "dst-port": {"type": "integer", "min": 0, "max": 65535},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
}


# Valid enum values from API documentation
VALID_BODY_DHCP_IPSEC = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_USE_NATIP = [
    "enable",  # Replace source selector with interface IP when using outbound NAT.
    "disable",  # Do not modify source selector when using outbound NAT.
]
VALID_BODY_SELECTOR_MATCH = [
    "exact",  # Match selectors exactly.
    "subset",  # Match selectors by subset.
    "auto",  # Use subset or exact match depending on selector address type.
]
VALID_BODY_PROPOSAL = [
    "null-md5",  # null-md5
    "null-sha1",  # null-sha1
    "null-sha256",  # null-sha256
    "null-sha384",  # null-sha384
    "null-sha512",  # null-sha512
    "des-null",  # des-null
    "des-md5",  # des-md5
    "des-sha1",  # des-sha1
    "des-sha256",  # des-sha256
    "des-sha384",  # des-sha384
    "des-sha512",  # des-sha512
    "3des-null",  # 3des-null
    "3des-md5",  # 3des-md5
    "3des-sha1",  # 3des-sha1
    "3des-sha256",  # 3des-sha256
    "3des-sha384",  # 3des-sha384
    "3des-sha512",  # 3des-sha512
    "aes128-null",  # aes128-null
    "aes128-md5",  # aes128-md5
    "aes128-sha1",  # aes128-sha1
    "aes128-sha256",  # aes128-sha256
    "aes128-sha384",  # aes128-sha384
    "aes128-sha512",  # aes128-sha512
    "aes128gcm",  # aes128gcm
    "aes192-null",  # aes192-null
    "aes192-md5",  # aes192-md5
    "aes192-sha1",  # aes192-sha1
    "aes192-sha256",  # aes192-sha256
    "aes192-sha384",  # aes192-sha384
    "aes192-sha512",  # aes192-sha512
    "aes256-null",  # aes256-null
    "aes256-md5",  # aes256-md5
    "aes256-sha1",  # aes256-sha1
    "aes256-sha256",  # aes256-sha256
    "aes256-sha384",  # aes256-sha384
    "aes256-sha512",  # aes256-sha512
    "aes256gcm",  # aes256gcm
    "chacha20poly1305",  # chacha20poly1305
    "aria128-null",  # aria128-null
    "aria128-md5",  # aria128-md5
    "aria128-sha1",  # aria128-sha1
    "aria128-sha256",  # aria128-sha256
    "aria128-sha384",  # aria128-sha384
    "aria128-sha512",  # aria128-sha512
    "aria192-null",  # aria192-null
    "aria192-md5",  # aria192-md5
    "aria192-sha1",  # aria192-sha1
    "aria192-sha256",  # aria192-sha256
    "aria192-sha384",  # aria192-sha384
    "aria192-sha512",  # aria192-sha512
    "aria256-null",  # aria256-null
    "aria256-md5",  # aria256-md5
    "aria256-sha1",  # aria256-sha1
    "aria256-sha256",  # aria256-sha256
    "aria256-sha384",  # aria256-sha384
    "aria256-sha512",  # aria256-sha512
    "seed-null",  # seed-null
    "seed-md5",  # seed-md5
    "seed-sha1",  # seed-sha1
    "seed-sha256",  # seed-sha256
    "seed-sha384",  # seed-sha384
    "seed-sha512",  # seed-sha512
]
VALID_BODY_PFS = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_DHGRP = [
    "1",  # DH Group 1.
    "2",  # DH Group 2.
    "5",  # DH Group 5.
    "14",  # DH Group 14.
    "15",  # DH Group 15.
    "16",  # DH Group 16.
    "17",  # DH Group 17.
    "18",  # DH Group 18.
    "19",  # DH Group 19.
    "20",  # DH Group 20.
    "21",  # DH Group 21.
    "27",  # DH Group 27.
    "28",  # DH Group 28.
    "29",  # DH Group 29.
    "30",  # DH Group 30.
    "31",  # DH Group 31.
    "32",  # DH Group 32.
]
VALID_BODY_ADDKE1 = [
    "0",  # NONE.
    "35",  # ML-KEM-512.
    "36",  # ML-KEM-768.
    "37",  # ML-KEM-1024.
    "1080",  # KYBER512.
    "1081",  # KYBER768.
    "1082",  # KYBER1024.
    "1083",  # FRODO L1.
    "1084",  # FRODO L3.
    "1085",  # FRODO L5.
    "1089",  # BIKE L1.
    "1090",  # BIKE L3.
    "1091",  # BIKE L5.
    "1092",  # HQC128.
    "1093",  # HQC192.
    "1094",  # HQC256.
]
VALID_BODY_ADDKE2 = [
    "0",  # NONE.
    "35",  # ML-KEM-512.
    "36",  # ML-KEM-768.
    "37",  # ML-KEM-1024.
    "1080",  # KYBER512.
    "1081",  # KYBER768.
    "1082",  # KYBER1024.
    "1083",  # FRODO L1.
    "1084",  # FRODO L3.
    "1085",  # FRODO L5.
    "1089",  # BIKE L1.
    "1090",  # BIKE L3.
    "1091",  # BIKE L5.
    "1092",  # HQC128.
    "1093",  # HQC192.
    "1094",  # HQC256.
]
VALID_BODY_ADDKE3 = [
    "0",  # NONE.
    "35",  # ML-KEM-512.
    "36",  # ML-KEM-768.
    "37",  # ML-KEM-1024.
    "1080",  # KYBER512.
    "1081",  # KYBER768.
    "1082",  # KYBER1024.
    "1083",  # FRODO L1.
    "1084",  # FRODO L3.
    "1085",  # FRODO L5.
    "1089",  # BIKE L1.
    "1090",  # BIKE L3.
    "1091",  # BIKE L5.
    "1092",  # HQC128.
    "1093",  # HQC192.
    "1094",  # HQC256.
]
VALID_BODY_ADDKE4 = [
    "0",  # NONE.
    "35",  # ML-KEM-512.
    "36",  # ML-KEM-768.
    "37",  # ML-KEM-1024.
    "1080",  # KYBER512.
    "1081",  # KYBER768.
    "1082",  # KYBER1024.
    "1083",  # FRODO L1.
    "1084",  # FRODO L3.
    "1085",  # FRODO L5.
    "1089",  # BIKE L1.
    "1090",  # BIKE L3.
    "1091",  # BIKE L5.
    "1092",  # HQC128.
    "1093",  # HQC192.
    "1094",  # HQC256.
]
VALID_BODY_ADDKE5 = [
    "0",  # NONE.
    "35",  # ML-KEM-512.
    "36",  # ML-KEM-768.
    "37",  # ML-KEM-1024.
    "1080",  # KYBER512.
    "1081",  # KYBER768.
    "1082",  # KYBER1024.
    "1083",  # FRODO L1.
    "1084",  # FRODO L3.
    "1085",  # FRODO L5.
    "1089",  # BIKE L1.
    "1090",  # BIKE L3.
    "1091",  # BIKE L5.
    "1092",  # HQC128.
    "1093",  # HQC192.
    "1094",  # HQC256.
]
VALID_BODY_ADDKE6 = [
    "0",  # NONE.
    "35",  # ML-KEM-512.
    "36",  # ML-KEM-768.
    "37",  # ML-KEM-1024.
    "1080",  # KYBER512.
    "1081",  # KYBER768.
    "1082",  # KYBER1024.
    "1083",  # FRODO L1.
    "1084",  # FRODO L3.
    "1085",  # FRODO L5.
    "1089",  # BIKE L1.
    "1090",  # BIKE L3.
    "1091",  # BIKE L5.
    "1092",  # HQC128.
    "1093",  # HQC192.
    "1094",  # HQC256.
]
VALID_BODY_ADDKE7 = [
    "0",  # NONE.
    "35",  # ML-KEM-512.
    "36",  # ML-KEM-768.
    "37",  # ML-KEM-1024.
    "1080",  # KYBER512.
    "1081",  # KYBER768.
    "1082",  # KYBER1024.
    "1083",  # FRODO L1.
    "1084",  # FRODO L3.
    "1085",  # FRODO L5.
    "1089",  # BIKE L1.
    "1090",  # BIKE L3.
    "1091",  # BIKE L5.
    "1092",  # HQC128.
    "1093",  # HQC192.
    "1094",  # HQC256.
]
VALID_BODY_REPLAY = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_KEEPALIVE = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_AUTO_NEGOTIATE = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_ADD_ROUTE = [
    "phase1",  # Add route according to phase1 add-route setting.
    "enable",  # Add route for remote proxy ID.
    "disable",  # Do not add route for remote proxy ID.
]
VALID_BODY_INBOUND_DSCP_COPY = [
    "phase1",  # copy the DCSP in the ESP header to the inner IP Header according to the phase1 inbound_dscp_copy setting.
    "enable",  # Enable copying of the DSCP in the ESP header to the inner IP header.
    "disable",  # Disable copying of the DSCP in the ESP header to the inner IP header.
]
VALID_BODY_KEYLIFE_TYPE = [
    "seconds",  # Key life in seconds.
    "kbs",  # Key life in kilobytes.
    "both",  # Key life both.
]
VALID_BODY_SINGLE_SOURCE = [
    "enable",  # Only single source IP will be accepted.
    "disable",  # Source IP range will be accepted.
]
VALID_BODY_ROUTE_OVERLAP = [
    "use-old",  # Use the old route and do not add the new route.
    "use-new",  # Delete the old route and add the new route.
    "allow",  # Allow overlapping routes.
]
VALID_BODY_ENCAPSULATION = [
    "tunnel-mode",  # Use tunnel mode encapsulation.
    "transport-mode",  # Use transport mode encapsulation.
]
VALID_BODY_L2TP = [
    "enable",  # Enable L2TP over IPsec.
    "disable",  # Disable L2TP over IPsec.
]
VALID_BODY_INITIATOR_TS_NARROW = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_DIFFSERV = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_SRC_ADDR_TYPE = [
    "subnet",  # IPv4 subnet.
    "range",  # IPv4 range.
    "ip",  # IPv4 IP.
    "name",  # IPv4 firewall address or group name.
]
VALID_BODY_DST_ADDR_TYPE = [
    "subnet",  # IPv4 subnet.
    "range",  # IPv4 range.
    "ip",  # IPv4 IP.
    "name",  # IPv4 firewall address or group name.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_vpn_ipsec_phase2_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for vpn/ipsec/phase2."""
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
    """Validate required fields for vpn/ipsec/phase2."""
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


def validate_vpn_ipsec_phase2_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new vpn/ipsec/phase2 object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "dhcp-ipsec" in payload:
        value = payload["dhcp-ipsec"]
        if value not in VALID_BODY_DHCP_IPSEC:
            desc = FIELD_DESCRIPTIONS.get("dhcp-ipsec", "")
            error_msg = f"Invalid value for 'dhcp-ipsec': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DHCP_IPSEC)}"
            error_msg += f"\n  → Example: dhcp-ipsec='{{ VALID_BODY_DHCP_IPSEC[0] }}'"
            return (False, error_msg)
    if "use-natip" in payload:
        value = payload["use-natip"]
        if value not in VALID_BODY_USE_NATIP:
            desc = FIELD_DESCRIPTIONS.get("use-natip", "")
            error_msg = f"Invalid value for 'use-natip': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_USE_NATIP)}"
            error_msg += f"\n  → Example: use-natip='{{ VALID_BODY_USE_NATIP[0] }}'"
            return (False, error_msg)
    if "selector-match" in payload:
        value = payload["selector-match"]
        if value not in VALID_BODY_SELECTOR_MATCH:
            desc = FIELD_DESCRIPTIONS.get("selector-match", "")
            error_msg = f"Invalid value for 'selector-match': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SELECTOR_MATCH)}"
            error_msg += f"\n  → Example: selector-match='{{ VALID_BODY_SELECTOR_MATCH[0] }}'"
            return (False, error_msg)
    if "proposal" in payload:
        value = payload["proposal"]
        if value not in VALID_BODY_PROPOSAL:
            desc = FIELD_DESCRIPTIONS.get("proposal", "")
            error_msg = f"Invalid value for 'proposal': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PROPOSAL)}"
            error_msg += f"\n  → Example: proposal='{{ VALID_BODY_PROPOSAL[0] }}'"
            return (False, error_msg)
    if "pfs" in payload:
        value = payload["pfs"]
        if value not in VALID_BODY_PFS:
            desc = FIELD_DESCRIPTIONS.get("pfs", "")
            error_msg = f"Invalid value for 'pfs': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PFS)}"
            error_msg += f"\n  → Example: pfs='{{ VALID_BODY_PFS[0] }}'"
            return (False, error_msg)
    if "dhgrp" in payload:
        value = payload["dhgrp"]
        if value not in VALID_BODY_DHGRP:
            desc = FIELD_DESCRIPTIONS.get("dhgrp", "")
            error_msg = f"Invalid value for 'dhgrp': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DHGRP)}"
            error_msg += f"\n  → Example: dhgrp='{{ VALID_BODY_DHGRP[0] }}'"
            return (False, error_msg)
    if "addke1" in payload:
        value = payload["addke1"]
        if value not in VALID_BODY_ADDKE1:
            desc = FIELD_DESCRIPTIONS.get("addke1", "")
            error_msg = f"Invalid value for 'addke1': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ADDKE1)}"
            error_msg += f"\n  → Example: addke1='{{ VALID_BODY_ADDKE1[0] }}'"
            return (False, error_msg)
    if "addke2" in payload:
        value = payload["addke2"]
        if value not in VALID_BODY_ADDKE2:
            desc = FIELD_DESCRIPTIONS.get("addke2", "")
            error_msg = f"Invalid value for 'addke2': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ADDKE2)}"
            error_msg += f"\n  → Example: addke2='{{ VALID_BODY_ADDKE2[0] }}'"
            return (False, error_msg)
    if "addke3" in payload:
        value = payload["addke3"]
        if value not in VALID_BODY_ADDKE3:
            desc = FIELD_DESCRIPTIONS.get("addke3", "")
            error_msg = f"Invalid value for 'addke3': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ADDKE3)}"
            error_msg += f"\n  → Example: addke3='{{ VALID_BODY_ADDKE3[0] }}'"
            return (False, error_msg)
    if "addke4" in payload:
        value = payload["addke4"]
        if value not in VALID_BODY_ADDKE4:
            desc = FIELD_DESCRIPTIONS.get("addke4", "")
            error_msg = f"Invalid value for 'addke4': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ADDKE4)}"
            error_msg += f"\n  → Example: addke4='{{ VALID_BODY_ADDKE4[0] }}'"
            return (False, error_msg)
    if "addke5" in payload:
        value = payload["addke5"]
        if value not in VALID_BODY_ADDKE5:
            desc = FIELD_DESCRIPTIONS.get("addke5", "")
            error_msg = f"Invalid value for 'addke5': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ADDKE5)}"
            error_msg += f"\n  → Example: addke5='{{ VALID_BODY_ADDKE5[0] }}'"
            return (False, error_msg)
    if "addke6" in payload:
        value = payload["addke6"]
        if value not in VALID_BODY_ADDKE6:
            desc = FIELD_DESCRIPTIONS.get("addke6", "")
            error_msg = f"Invalid value for 'addke6': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ADDKE6)}"
            error_msg += f"\n  → Example: addke6='{{ VALID_BODY_ADDKE6[0] }}'"
            return (False, error_msg)
    if "addke7" in payload:
        value = payload["addke7"]
        if value not in VALID_BODY_ADDKE7:
            desc = FIELD_DESCRIPTIONS.get("addke7", "")
            error_msg = f"Invalid value for 'addke7': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ADDKE7)}"
            error_msg += f"\n  → Example: addke7='{{ VALID_BODY_ADDKE7[0] }}'"
            return (False, error_msg)
    if "replay" in payload:
        value = payload["replay"]
        if value not in VALID_BODY_REPLAY:
            desc = FIELD_DESCRIPTIONS.get("replay", "")
            error_msg = f"Invalid value for 'replay': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_REPLAY)}"
            error_msg += f"\n  → Example: replay='{{ VALID_BODY_REPLAY[0] }}'"
            return (False, error_msg)
    if "keepalive" in payload:
        value = payload["keepalive"]
        if value not in VALID_BODY_KEEPALIVE:
            desc = FIELD_DESCRIPTIONS.get("keepalive", "")
            error_msg = f"Invalid value for 'keepalive': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_KEEPALIVE)}"
            error_msg += f"\n  → Example: keepalive='{{ VALID_BODY_KEEPALIVE[0] }}'"
            return (False, error_msg)
    if "auto-negotiate" in payload:
        value = payload["auto-negotiate"]
        if value not in VALID_BODY_AUTO_NEGOTIATE:
            desc = FIELD_DESCRIPTIONS.get("auto-negotiate", "")
            error_msg = f"Invalid value for 'auto-negotiate': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTO_NEGOTIATE)}"
            error_msg += f"\n  → Example: auto-negotiate='{{ VALID_BODY_AUTO_NEGOTIATE[0] }}'"
            return (False, error_msg)
    if "add-route" in payload:
        value = payload["add-route"]
        if value not in VALID_BODY_ADD_ROUTE:
            desc = FIELD_DESCRIPTIONS.get("add-route", "")
            error_msg = f"Invalid value for 'add-route': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ADD_ROUTE)}"
            error_msg += f"\n  → Example: add-route='{{ VALID_BODY_ADD_ROUTE[0] }}'"
            return (False, error_msg)
    if "inbound-dscp-copy" in payload:
        value = payload["inbound-dscp-copy"]
        if value not in VALID_BODY_INBOUND_DSCP_COPY:
            desc = FIELD_DESCRIPTIONS.get("inbound-dscp-copy", "")
            error_msg = f"Invalid value for 'inbound-dscp-copy': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_INBOUND_DSCP_COPY)}"
            error_msg += f"\n  → Example: inbound-dscp-copy='{{ VALID_BODY_INBOUND_DSCP_COPY[0] }}'"
            return (False, error_msg)
    if "keylife-type" in payload:
        value = payload["keylife-type"]
        if value not in VALID_BODY_KEYLIFE_TYPE:
            desc = FIELD_DESCRIPTIONS.get("keylife-type", "")
            error_msg = f"Invalid value for 'keylife-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_KEYLIFE_TYPE)}"
            error_msg += f"\n  → Example: keylife-type='{{ VALID_BODY_KEYLIFE_TYPE[0] }}'"
            return (False, error_msg)
    if "single-source" in payload:
        value = payload["single-source"]
        if value not in VALID_BODY_SINGLE_SOURCE:
            desc = FIELD_DESCRIPTIONS.get("single-source", "")
            error_msg = f"Invalid value for 'single-source': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SINGLE_SOURCE)}"
            error_msg += f"\n  → Example: single-source='{{ VALID_BODY_SINGLE_SOURCE[0] }}'"
            return (False, error_msg)
    if "route-overlap" in payload:
        value = payload["route-overlap"]
        if value not in VALID_BODY_ROUTE_OVERLAP:
            desc = FIELD_DESCRIPTIONS.get("route-overlap", "")
            error_msg = f"Invalid value for 'route-overlap': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ROUTE_OVERLAP)}"
            error_msg += f"\n  → Example: route-overlap='{{ VALID_BODY_ROUTE_OVERLAP[0] }}'"
            return (False, error_msg)
    if "encapsulation" in payload:
        value = payload["encapsulation"]
        if value not in VALID_BODY_ENCAPSULATION:
            desc = FIELD_DESCRIPTIONS.get("encapsulation", "")
            error_msg = f"Invalid value for 'encapsulation': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ENCAPSULATION)}"
            error_msg += f"\n  → Example: encapsulation='{{ VALID_BODY_ENCAPSULATION[0] }}'"
            return (False, error_msg)
    if "l2tp" in payload:
        value = payload["l2tp"]
        if value not in VALID_BODY_L2TP:
            desc = FIELD_DESCRIPTIONS.get("l2tp", "")
            error_msg = f"Invalid value for 'l2tp': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_L2TP)}"
            error_msg += f"\n  → Example: l2tp='{{ VALID_BODY_L2TP[0] }}'"
            return (False, error_msg)
    if "initiator-ts-narrow" in payload:
        value = payload["initiator-ts-narrow"]
        if value not in VALID_BODY_INITIATOR_TS_NARROW:
            desc = FIELD_DESCRIPTIONS.get("initiator-ts-narrow", "")
            error_msg = f"Invalid value for 'initiator-ts-narrow': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_INITIATOR_TS_NARROW)}"
            error_msg += f"\n  → Example: initiator-ts-narrow='{{ VALID_BODY_INITIATOR_TS_NARROW[0] }}'"
            return (False, error_msg)
    if "diffserv" in payload:
        value = payload["diffserv"]
        if value not in VALID_BODY_DIFFSERV:
            desc = FIELD_DESCRIPTIONS.get("diffserv", "")
            error_msg = f"Invalid value for 'diffserv': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DIFFSERV)}"
            error_msg += f"\n  → Example: diffserv='{{ VALID_BODY_DIFFSERV[0] }}'"
            return (False, error_msg)
    if "src-addr-type" in payload:
        value = payload["src-addr-type"]
        if value not in VALID_BODY_SRC_ADDR_TYPE:
            desc = FIELD_DESCRIPTIONS.get("src-addr-type", "")
            error_msg = f"Invalid value for 'src-addr-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SRC_ADDR_TYPE)}"
            error_msg += f"\n  → Example: src-addr-type='{{ VALID_BODY_SRC_ADDR_TYPE[0] }}'"
            return (False, error_msg)
    if "dst-addr-type" in payload:
        value = payload["dst-addr-type"]
        if value not in VALID_BODY_DST_ADDR_TYPE:
            desc = FIELD_DESCRIPTIONS.get("dst-addr-type", "")
            error_msg = f"Invalid value for 'dst-addr-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DST_ADDR_TYPE)}"
            error_msg += f"\n  → Example: dst-addr-type='{{ VALID_BODY_DST_ADDR_TYPE[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_vpn_ipsec_phase2_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update vpn/ipsec/phase2."""
    # Step 1: Validate enum values
    if "dhcp-ipsec" in payload:
        value = payload["dhcp-ipsec"]
        if value not in VALID_BODY_DHCP_IPSEC:
            return (
                False,
                f"Invalid value for 'dhcp-ipsec'='{value}'. Must be one of: {', '.join(VALID_BODY_DHCP_IPSEC)}",
            )
    if "use-natip" in payload:
        value = payload["use-natip"]
        if value not in VALID_BODY_USE_NATIP:
            return (
                False,
                f"Invalid value for 'use-natip'='{value}'. Must be one of: {', '.join(VALID_BODY_USE_NATIP)}",
            )
    if "selector-match" in payload:
        value = payload["selector-match"]
        if value not in VALID_BODY_SELECTOR_MATCH:
            return (
                False,
                f"Invalid value for 'selector-match'='{value}'. Must be one of: {', '.join(VALID_BODY_SELECTOR_MATCH)}",
            )
    if "proposal" in payload:
        value = payload["proposal"]
        if value not in VALID_BODY_PROPOSAL:
            return (
                False,
                f"Invalid value for 'proposal'='{value}'. Must be one of: {', '.join(VALID_BODY_PROPOSAL)}",
            )
    if "pfs" in payload:
        value = payload["pfs"]
        if value not in VALID_BODY_PFS:
            return (
                False,
                f"Invalid value for 'pfs'='{value}'. Must be one of: {', '.join(VALID_BODY_PFS)}",
            )
    if "dhgrp" in payload:
        value = payload["dhgrp"]
        if value not in VALID_BODY_DHGRP:
            return (
                False,
                f"Invalid value for 'dhgrp'='{value}'. Must be one of: {', '.join(VALID_BODY_DHGRP)}",
            )
    if "addke1" in payload:
        value = payload["addke1"]
        if value not in VALID_BODY_ADDKE1:
            return (
                False,
                f"Invalid value for 'addke1'='{value}'. Must be one of: {', '.join(VALID_BODY_ADDKE1)}",
            )
    if "addke2" in payload:
        value = payload["addke2"]
        if value not in VALID_BODY_ADDKE2:
            return (
                False,
                f"Invalid value for 'addke2'='{value}'. Must be one of: {', '.join(VALID_BODY_ADDKE2)}",
            )
    if "addke3" in payload:
        value = payload["addke3"]
        if value not in VALID_BODY_ADDKE3:
            return (
                False,
                f"Invalid value for 'addke3'='{value}'. Must be one of: {', '.join(VALID_BODY_ADDKE3)}",
            )
    if "addke4" in payload:
        value = payload["addke4"]
        if value not in VALID_BODY_ADDKE4:
            return (
                False,
                f"Invalid value for 'addke4'='{value}'. Must be one of: {', '.join(VALID_BODY_ADDKE4)}",
            )
    if "addke5" in payload:
        value = payload["addke5"]
        if value not in VALID_BODY_ADDKE5:
            return (
                False,
                f"Invalid value for 'addke5'='{value}'. Must be one of: {', '.join(VALID_BODY_ADDKE5)}",
            )
    if "addke6" in payload:
        value = payload["addke6"]
        if value not in VALID_BODY_ADDKE6:
            return (
                False,
                f"Invalid value for 'addke6'='{value}'. Must be one of: {', '.join(VALID_BODY_ADDKE6)}",
            )
    if "addke7" in payload:
        value = payload["addke7"]
        if value not in VALID_BODY_ADDKE7:
            return (
                False,
                f"Invalid value for 'addke7'='{value}'. Must be one of: {', '.join(VALID_BODY_ADDKE7)}",
            )
    if "replay" in payload:
        value = payload["replay"]
        if value not in VALID_BODY_REPLAY:
            return (
                False,
                f"Invalid value for 'replay'='{value}'. Must be one of: {', '.join(VALID_BODY_REPLAY)}",
            )
    if "keepalive" in payload:
        value = payload["keepalive"]
        if value not in VALID_BODY_KEEPALIVE:
            return (
                False,
                f"Invalid value for 'keepalive'='{value}'. Must be one of: {', '.join(VALID_BODY_KEEPALIVE)}",
            )
    if "auto-negotiate" in payload:
        value = payload["auto-negotiate"]
        if value not in VALID_BODY_AUTO_NEGOTIATE:
            return (
                False,
                f"Invalid value for 'auto-negotiate'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTO_NEGOTIATE)}",
            )
    if "add-route" in payload:
        value = payload["add-route"]
        if value not in VALID_BODY_ADD_ROUTE:
            return (
                False,
                f"Invalid value for 'add-route'='{value}'. Must be one of: {', '.join(VALID_BODY_ADD_ROUTE)}",
            )
    if "inbound-dscp-copy" in payload:
        value = payload["inbound-dscp-copy"]
        if value not in VALID_BODY_INBOUND_DSCP_COPY:
            return (
                False,
                f"Invalid value for 'inbound-dscp-copy'='{value}'. Must be one of: {', '.join(VALID_BODY_INBOUND_DSCP_COPY)}",
            )
    if "keylife-type" in payload:
        value = payload["keylife-type"]
        if value not in VALID_BODY_KEYLIFE_TYPE:
            return (
                False,
                f"Invalid value for 'keylife-type'='{value}'. Must be one of: {', '.join(VALID_BODY_KEYLIFE_TYPE)}",
            )
    if "single-source" in payload:
        value = payload["single-source"]
        if value not in VALID_BODY_SINGLE_SOURCE:
            return (
                False,
                f"Invalid value for 'single-source'='{value}'. Must be one of: {', '.join(VALID_BODY_SINGLE_SOURCE)}",
            )
    if "route-overlap" in payload:
        value = payload["route-overlap"]
        if value not in VALID_BODY_ROUTE_OVERLAP:
            return (
                False,
                f"Invalid value for 'route-overlap'='{value}'. Must be one of: {', '.join(VALID_BODY_ROUTE_OVERLAP)}",
            )
    if "encapsulation" in payload:
        value = payload["encapsulation"]
        if value not in VALID_BODY_ENCAPSULATION:
            return (
                False,
                f"Invalid value for 'encapsulation'='{value}'. Must be one of: {', '.join(VALID_BODY_ENCAPSULATION)}",
            )
    if "l2tp" in payload:
        value = payload["l2tp"]
        if value not in VALID_BODY_L2TP:
            return (
                False,
                f"Invalid value for 'l2tp'='{value}'. Must be one of: {', '.join(VALID_BODY_L2TP)}",
            )
    if "initiator-ts-narrow" in payload:
        value = payload["initiator-ts-narrow"]
        if value not in VALID_BODY_INITIATOR_TS_NARROW:
            return (
                False,
                f"Invalid value for 'initiator-ts-narrow'='{value}'. Must be one of: {', '.join(VALID_BODY_INITIATOR_TS_NARROW)}",
            )
    if "diffserv" in payload:
        value = payload["diffserv"]
        if value not in VALID_BODY_DIFFSERV:
            return (
                False,
                f"Invalid value for 'diffserv'='{value}'. Must be one of: {', '.join(VALID_BODY_DIFFSERV)}",
            )
    if "src-addr-type" in payload:
        value = payload["src-addr-type"]
        if value not in VALID_BODY_SRC_ADDR_TYPE:
            return (
                False,
                f"Invalid value for 'src-addr-type'='{value}'. Must be one of: {', '.join(VALID_BODY_SRC_ADDR_TYPE)}",
            )
    if "dst-addr-type" in payload:
        value = payload["dst-addr-type"]
        if value not in VALID_BODY_DST_ADDR_TYPE:
            return (
                False,
                f"Invalid value for 'dst-addr-type'='{value}'. Must be one of: {', '.join(VALID_BODY_DST_ADDR_TYPE)}",
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
    "endpoint": "vpn/ipsec/phase2",
    "category": "cmdb",
    "api_path": "vpn.ipsec/phase2",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure VPN autokey tunnel.",
    "total_fields": 52,
    "required_fields_count": 6,
    "fields_with_defaults_count": 51,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
