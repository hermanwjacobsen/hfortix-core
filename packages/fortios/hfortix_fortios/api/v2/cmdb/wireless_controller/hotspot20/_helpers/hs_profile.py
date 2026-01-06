"""Validation helpers for wireless_controller/hotspot20/hs_profile - Auto-generated"""

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
    "release": 2,
    "access-network-type": "private-network",
    "access-network-internet": "disable",
    "access-network-asra": "disable",
    "access-network-esr": "disable",
    "access-network-uesa": "disable",
    "venue-group": "unspecified",
    "venue-type": "unspecified",
    "hessid": "00:00:00:00:00:00",
    "proxy-arp": "enable",
    "l2tif": "disable",
    "pame-bi": "enable",
    "anqp-domain-id": 0,
    "domain-name": "",
    "osu-ssid": "",
    "gas-comeback-delay": 500,
    "gas-fragmentation-limit": 1024,
    "dgaf": "disable",
    "deauth-request-timeout": 60,
    "wnm-sleep-mode": "disable",
    "bss-transition": "disable",
    "venue-name": "",
    "venue-url": "",
    "roaming-consortium": "",
    "nai-realm": "",
    "oper-friendly-name": "",
    "oper-icon": "",
    "advice-of-charge": "",
    "osu-provider-nai": "",
    "terms-and-conditions": "",
    "wan-metrics": "",
    "network-auth": "",
    "3gpp-plmn": "",
    "conn-cap": "",
    "qos-map": "",
    "ip-addr-type": "",
    "wba-open-roaming": "disable",
    "wba-financial-clearing-provider": "",
    "wba-data-clearing-provider": "",
    "wba-charging-currency": "",
    "wba-charging-rate": 0,
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
    "name": "string",  # Hotspot profile name.
    "release": "integer",  # Hotspot 2.0 Release number (1, 2, 3, default = 2).
    "access-network-type": "option",  # Access network type.
    "access-network-internet": "option",  # Enable/disable connectivity to the Internet.
    "access-network-asra": "option",  # Enable/disable additional step required for access (ASRA).
    "access-network-esr": "option",  # Enable/disable emergency services reachable (ESR).
    "access-network-uesa": "option",  # Enable/disable unauthenticated emergency service accessible 
    "venue-group": "option",  # Venue group.
    "venue-type": "option",  # Venue type.
    "hessid": "mac-address",  # Homogeneous extended service set identifier (HESSID).
    "proxy-arp": "option",  # Enable/disable Proxy ARP.
    "l2tif": "option",  # Enable/disable Layer 2 traffic inspection and filtering.
    "pame-bi": "option",  # Enable/disable Pre-Association Message Exchange BSSID Indepe
    "anqp-domain-id": "integer",  # ANQP Domain ID (0-65535).
    "domain-name": "string",  # Domain name.
    "osu-ssid": "string",  # Online sign up (OSU) SSID.
    "gas-comeback-delay": "integer",  # GAS comeback delay (0 or 100 - 10000 milliseconds, default =
    "gas-fragmentation-limit": "integer",  # GAS fragmentation limit (512 - 4096, default = 1024).
    "dgaf": "option",  # Enable/disable downstream group-addressed forwarding (DGAF).
    "deauth-request-timeout": "integer",  # Deauthentication request timeout (in seconds).
    "wnm-sleep-mode": "option",  # Enable/disable wireless network management (WNM) sleep mode.
    "bss-transition": "option",  # Enable/disable basic service set (BSS) transition Support.
    "venue-name": "string",  # Venue name.
    "venue-url": "string",  # Venue name.
    "roaming-consortium": "string",  # Roaming consortium list name.
    "nai-realm": "string",  # NAI realm list name.
    "oper-friendly-name": "string",  # Operator friendly name.
    "oper-icon": "string",  # Operator icon.
    "advice-of-charge": "string",  # Advice of charge.
    "osu-provider-nai": "string",  # OSU Provider NAI.
    "terms-and-conditions": "string",  # Terms and conditions.
    "osu-provider": "string",  # Manually selected list of OSU provider(s).
    "wan-metrics": "string",  # WAN metric name.
    "network-auth": "string",  # Network authentication name.
    "3gpp-plmn": "string",  # 3GPP PLMN name.
    "conn-cap": "string",  # Connection capability name.
    "qos-map": "string",  # QoS MAP set ID.
    "ip-addr-type": "string",  # IP address type name.
    "wba-open-roaming": "option",  # Enable/disable WBA open roaming support.
    "wba-financial-clearing-provider": "string",  # WBA ID of financial clearing provider.
    "wba-data-clearing-provider": "string",  # WBA ID of data clearing provider.
    "wba-charging-currency": "string",  # Three letter currency code.
    "wba-charging-rate": "integer",  # Number of currency units per kilobyte.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "Hotspot profile name.",
    "release": "Hotspot 2.0 Release number (1, 2, 3, default = 2).",
    "access-network-type": "Access network type.",
    "access-network-internet": "Enable/disable connectivity to the Internet.",
    "access-network-asra": "Enable/disable additional step required for access (ASRA).",
    "access-network-esr": "Enable/disable emergency services reachable (ESR).",
    "access-network-uesa": "Enable/disable unauthenticated emergency service accessible (UESA).",
    "venue-group": "Venue group.",
    "venue-type": "Venue type.",
    "hessid": "Homogeneous extended service set identifier (HESSID).",
    "proxy-arp": "Enable/disable Proxy ARP.",
    "l2tif": "Enable/disable Layer 2 traffic inspection and filtering.",
    "pame-bi": "Enable/disable Pre-Association Message Exchange BSSID Independent (PAME-BI).",
    "anqp-domain-id": "ANQP Domain ID (0-65535).",
    "domain-name": "Domain name.",
    "osu-ssid": "Online sign up (OSU) SSID.",
    "gas-comeback-delay": "GAS comeback delay (0 or 100 - 10000 milliseconds, default = 500).",
    "gas-fragmentation-limit": "GAS fragmentation limit (512 - 4096, default = 1024).",
    "dgaf": "Enable/disable downstream group-addressed forwarding (DGAF).",
    "deauth-request-timeout": "Deauthentication request timeout (in seconds).",
    "wnm-sleep-mode": "Enable/disable wireless network management (WNM) sleep mode.",
    "bss-transition": "Enable/disable basic service set (BSS) transition Support.",
    "venue-name": "Venue name.",
    "venue-url": "Venue name.",
    "roaming-consortium": "Roaming consortium list name.",
    "nai-realm": "NAI realm list name.",
    "oper-friendly-name": "Operator friendly name.",
    "oper-icon": "Operator icon.",
    "advice-of-charge": "Advice of charge.",
    "osu-provider-nai": "OSU Provider NAI.",
    "terms-and-conditions": "Terms and conditions.",
    "osu-provider": "Manually selected list of OSU provider(s).",
    "wan-metrics": "WAN metric name.",
    "network-auth": "Network authentication name.",
    "3gpp-plmn": "3GPP PLMN name.",
    "conn-cap": "Connection capability name.",
    "qos-map": "QoS MAP set ID.",
    "ip-addr-type": "IP address type name.",
    "wba-open-roaming": "Enable/disable WBA open roaming support.",
    "wba-financial-clearing-provider": "WBA ID of financial clearing provider.",
    "wba-data-clearing-provider": "WBA ID of data clearing provider.",
    "wba-charging-currency": "Three letter currency code.",
    "wba-charging-rate": "Number of currency units per kilobyte.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 35},
    "release": {"type": "integer", "min": 1, "max": 3},
    "anqp-domain-id": {"type": "integer", "min": 0, "max": 65535},
    "domain-name": {"type": "string", "max_length": 255},
    "osu-ssid": {"type": "string", "max_length": 255},
    "gas-comeback-delay": {"type": "integer", "min": 100, "max": 10000},
    "gas-fragmentation-limit": {"type": "integer", "min": 512, "max": 4096},
    "deauth-request-timeout": {"type": "integer", "min": 30, "max": 120},
    "venue-name": {"type": "string", "max_length": 35},
    "venue-url": {"type": "string", "max_length": 35},
    "roaming-consortium": {"type": "string", "max_length": 35},
    "nai-realm": {"type": "string", "max_length": 35},
    "oper-friendly-name": {"type": "string", "max_length": 35},
    "oper-icon": {"type": "string", "max_length": 35},
    "advice-of-charge": {"type": "string", "max_length": 35},
    "osu-provider-nai": {"type": "string", "max_length": 35},
    "terms-and-conditions": {"type": "string", "max_length": 35},
    "wan-metrics": {"type": "string", "max_length": 35},
    "network-auth": {"type": "string", "max_length": 35},
    "3gpp-plmn": {"type": "string", "max_length": 35},
    "conn-cap": {"type": "string", "max_length": 35},
    "qos-map": {"type": "string", "max_length": 35},
    "ip-addr-type": {"type": "string", "max_length": 35},
    "wba-financial-clearing-provider": {"type": "string", "max_length": 127},
    "wba-data-clearing-provider": {"type": "string", "max_length": 127},
    "wba-charging-currency": {"type": "string", "max_length": 3},
    "wba-charging-rate": {"type": "integer", "min": 0, "max": 4294967295},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "osu-provider": {
        "name": {
            "type": "string",
            "help": "OSU provider name.",
            "required": True,
            "default": "",
            "max_length": 35,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_ACCESS_NETWORK_TYPE = [
    "private-network",  # Private network.
    "private-network-with-guest-access",  # Private network with guest access.
    "chargeable-public-network",  # Chargeable public network.
    "free-public-network",  # Free public network.
    "personal-device-network",  # Personal devices network.
    "emergency-services-only-network",  # Emergency services only network.
    "test-or-experimental",  # Test or experimental.
    "wildcard",  # Wildcard.
]
VALID_BODY_ACCESS_NETWORK_INTERNET = [
    "enable",  # Enable connectivity to the Internet.
    "disable",  # Disable connectivity to the Internet.
]
VALID_BODY_ACCESS_NETWORK_ASRA = [
    "enable",  # Enable additional step required for access (ASRA).
    "disable",  # Disable additional step required for access (ASRA).
]
VALID_BODY_ACCESS_NETWORK_ESR = [
    "enable",  # Enable emergency services reachable (ESR).
    "disable",  # Disable emergency services reachable (ESR).
]
VALID_BODY_ACCESS_NETWORK_UESA = [
    "enable",  # Enable unauthenticated emergency service accessible (UESA).
    "disable",  # Disable unauthenticated emergency service accessible (UESA).
]
VALID_BODY_VENUE_GROUP = [
    "unspecified",  # Unspecified.
    "assembly",  # Assembly.
    "business",  # Business.
    "educational",  # Educational.
    "factory",  # Factory and industrial.
    "institutional",  # Institutional.
    "mercantile",  # Mercantile.
    "residential",  # Residential.
    "storage",  # Storage.
    "utility",  # Utility and miscellaneous.
    "vehicular",  # Vehicular.
    "outdoor",  # Outdoor.
]
VALID_BODY_VENUE_TYPE = [
    "unspecified",  # Unspecified.
    "arena",  # Arena.
    "stadium",  # Stadium.
    "passenger-terminal",  # Passenger terminal.
    "amphitheater",  # Amphitheater.
    "amusement-park",  # Amusement park.
    "place-of-worship",  # Place of worship.
    "convention-center",  # Convention center.
    "library",  # Library.
    "museum",  # Museum.
    "restaurant",  # Restaurant.
    "theater",  # Theater.
    "bar",  # Bar.
    "coffee-shop",  # Coffee shop.
    "zoo-or-aquarium",  # Zoo or aquarium.
    "emergency-center",  # Emergency coordination center.
    "doctor-office",  # Doctor or dentist office.
    "bank",  # Bank.
    "fire-station",  # Fire station.
    "police-station",  # Police station.
    "post-office",  # Post office.
    "professional-office",  # Professional office.
    "research-facility",  # Research and development facility.
    "attorney-office",  # Attorney office.
    "primary-school",  # Primary school.
    "secondary-school",  # Secondary school.
    "university-or-college",  # University or college.
    "factory",  # Factory.
    "hospital",  # Hospital.
    "long-term-care-facility",  # Long term care facility.
    "rehab-center",  # Alcohol and drug rehabilitation center.
    "group-home",  # Group home.
    "prison-or-jail",  # Prison or jail.
    "retail-store",  # Retail store.
    "grocery-market",  # Grocery market.
    "auto-service-station",  # Auto service station.
    "shopping-mall",  # Shopping mall.
    "gas-station",  # Gas station.
    "private",  # Private residence.
    "hotel-or-motel",  # Hotel or motel.
    "dormitory",  # Dormitory.
    "boarding-house",  # Boarding house.
    "automobile",  # Automobile or truck.
    "airplane",  # Airplane.
    "bus",  # Bus.
    "ferry",  # Ferry.
    "ship-or-boat",  # Ship or boat.
    "train",  # Train.
    "motor-bike",  # Motor bike.
    "muni-mesh-network",  # Muni mesh network.
    "city-park",  # City park.
    "rest-area",  # Rest area.
    "traffic-control",  # Traffic control.
    "bus-stop",  # Bus stop.
    "kiosk",  # Kiosk.
]
VALID_BODY_PROXY_ARP = [
    "enable",  # Enable Proxy ARP.
    "disable",  # Disable Proxy ARP.
]
VALID_BODY_L2TIF = [
    "enable",  # Enable Layer 2 traffic inspection and filtering.
    "disable",  # Disable Layer 2 traffic inspection and filtering.
]
VALID_BODY_PAME_BI = [
    "disable",  # Disable Pre-Association Message Exchange BSSID Independent (PAME-BI).
    "enable",  # Enable Pre-Association Message Exchange BSSID Independent (PAME-BI).
]
VALID_BODY_DGAF = [
    "enable",  # Enable downstream group-addressed forwarding (DGAF).
    "disable",  # Disable downstream group-addressed forwarding (DGAF).
]
VALID_BODY_WNM_SLEEP_MODE = [
    "enable",  # Enable wireless network management (WNM) sleep mode.
    "disable",  # Disable wireless network management (WNM) sleep mode.
]
VALID_BODY_BSS_TRANSITION = [
    "enable",  # Enable basic service set (BSS) transition support.
    "disable",  # Disable basic service set (BSS) transition support.
]
VALID_BODY_WBA_OPEN_ROAMING = [
    "disable",  # Disable WBA open roaming support.
    "enable",  # Enable WBA open roaming support.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_wireless_controller_hotspot20_hs_profile_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for wireless_controller/hotspot20/hs_profile."""
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
    """Validate required fields for wireless_controller/hotspot20/hs_profile."""
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


def validate_wireless_controller_hotspot20_hs_profile_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new wireless_controller/hotspot20/hs_profile object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "access-network-type" in payload:
        value = payload["access-network-type"]
        if value not in VALID_BODY_ACCESS_NETWORK_TYPE:
            desc = FIELD_DESCRIPTIONS.get("access-network-type", "")
            error_msg = f"Invalid value for 'access-network-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ACCESS_NETWORK_TYPE)}"
            error_msg += f"\n  → Example: access-network-type='{{ VALID_BODY_ACCESS_NETWORK_TYPE[0] }}'"
            return (False, error_msg)
    if "access-network-internet" in payload:
        value = payload["access-network-internet"]
        if value not in VALID_BODY_ACCESS_NETWORK_INTERNET:
            desc = FIELD_DESCRIPTIONS.get("access-network-internet", "")
            error_msg = f"Invalid value for 'access-network-internet': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ACCESS_NETWORK_INTERNET)}"
            error_msg += f"\n  → Example: access-network-internet='{{ VALID_BODY_ACCESS_NETWORK_INTERNET[0] }}'"
            return (False, error_msg)
    if "access-network-asra" in payload:
        value = payload["access-network-asra"]
        if value not in VALID_BODY_ACCESS_NETWORK_ASRA:
            desc = FIELD_DESCRIPTIONS.get("access-network-asra", "")
            error_msg = f"Invalid value for 'access-network-asra': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ACCESS_NETWORK_ASRA)}"
            error_msg += f"\n  → Example: access-network-asra='{{ VALID_BODY_ACCESS_NETWORK_ASRA[0] }}'"
            return (False, error_msg)
    if "access-network-esr" in payload:
        value = payload["access-network-esr"]
        if value not in VALID_BODY_ACCESS_NETWORK_ESR:
            desc = FIELD_DESCRIPTIONS.get("access-network-esr", "")
            error_msg = f"Invalid value for 'access-network-esr': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ACCESS_NETWORK_ESR)}"
            error_msg += f"\n  → Example: access-network-esr='{{ VALID_BODY_ACCESS_NETWORK_ESR[0] }}'"
            return (False, error_msg)
    if "access-network-uesa" in payload:
        value = payload["access-network-uesa"]
        if value not in VALID_BODY_ACCESS_NETWORK_UESA:
            desc = FIELD_DESCRIPTIONS.get("access-network-uesa", "")
            error_msg = f"Invalid value for 'access-network-uesa': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ACCESS_NETWORK_UESA)}"
            error_msg += f"\n  → Example: access-network-uesa='{{ VALID_BODY_ACCESS_NETWORK_UESA[0] }}'"
            return (False, error_msg)
    if "venue-group" in payload:
        value = payload["venue-group"]
        if value not in VALID_BODY_VENUE_GROUP:
            desc = FIELD_DESCRIPTIONS.get("venue-group", "")
            error_msg = f"Invalid value for 'venue-group': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_VENUE_GROUP)}"
            error_msg += f"\n  → Example: venue-group='{{ VALID_BODY_VENUE_GROUP[0] }}'"
            return (False, error_msg)
    if "venue-type" in payload:
        value = payload["venue-type"]
        if value not in VALID_BODY_VENUE_TYPE:
            desc = FIELD_DESCRIPTIONS.get("venue-type", "")
            error_msg = f"Invalid value for 'venue-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_VENUE_TYPE)}"
            error_msg += f"\n  → Example: venue-type='{{ VALID_BODY_VENUE_TYPE[0] }}'"
            return (False, error_msg)
    if "proxy-arp" in payload:
        value = payload["proxy-arp"]
        if value not in VALID_BODY_PROXY_ARP:
            desc = FIELD_DESCRIPTIONS.get("proxy-arp", "")
            error_msg = f"Invalid value for 'proxy-arp': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PROXY_ARP)}"
            error_msg += f"\n  → Example: proxy-arp='{{ VALID_BODY_PROXY_ARP[0] }}'"
            return (False, error_msg)
    if "l2tif" in payload:
        value = payload["l2tif"]
        if value not in VALID_BODY_L2TIF:
            desc = FIELD_DESCRIPTIONS.get("l2tif", "")
            error_msg = f"Invalid value for 'l2tif': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_L2TIF)}"
            error_msg += f"\n  → Example: l2tif='{{ VALID_BODY_L2TIF[0] }}'"
            return (False, error_msg)
    if "pame-bi" in payload:
        value = payload["pame-bi"]
        if value not in VALID_BODY_PAME_BI:
            desc = FIELD_DESCRIPTIONS.get("pame-bi", "")
            error_msg = f"Invalid value for 'pame-bi': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PAME_BI)}"
            error_msg += f"\n  → Example: pame-bi='{{ VALID_BODY_PAME_BI[0] }}'"
            return (False, error_msg)
    if "dgaf" in payload:
        value = payload["dgaf"]
        if value not in VALID_BODY_DGAF:
            desc = FIELD_DESCRIPTIONS.get("dgaf", "")
            error_msg = f"Invalid value for 'dgaf': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DGAF)}"
            error_msg += f"\n  → Example: dgaf='{{ VALID_BODY_DGAF[0] }}'"
            return (False, error_msg)
    if "wnm-sleep-mode" in payload:
        value = payload["wnm-sleep-mode"]
        if value not in VALID_BODY_WNM_SLEEP_MODE:
            desc = FIELD_DESCRIPTIONS.get("wnm-sleep-mode", "")
            error_msg = f"Invalid value for 'wnm-sleep-mode': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WNM_SLEEP_MODE)}"
            error_msg += f"\n  → Example: wnm-sleep-mode='{{ VALID_BODY_WNM_SLEEP_MODE[0] }}'"
            return (False, error_msg)
    if "bss-transition" in payload:
        value = payload["bss-transition"]
        if value not in VALID_BODY_BSS_TRANSITION:
            desc = FIELD_DESCRIPTIONS.get("bss-transition", "")
            error_msg = f"Invalid value for 'bss-transition': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_BSS_TRANSITION)}"
            error_msg += f"\n  → Example: bss-transition='{{ VALID_BODY_BSS_TRANSITION[0] }}'"
            return (False, error_msg)
    if "wba-open-roaming" in payload:
        value = payload["wba-open-roaming"]
        if value not in VALID_BODY_WBA_OPEN_ROAMING:
            desc = FIELD_DESCRIPTIONS.get("wba-open-roaming", "")
            error_msg = f"Invalid value for 'wba-open-roaming': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WBA_OPEN_ROAMING)}"
            error_msg += f"\n  → Example: wba-open-roaming='{{ VALID_BODY_WBA_OPEN_ROAMING[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_wireless_controller_hotspot20_hs_profile_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update wireless_controller/hotspot20/hs_profile."""
    # Step 1: Validate enum values
    if "access-network-type" in payload:
        value = payload["access-network-type"]
        if value not in VALID_BODY_ACCESS_NETWORK_TYPE:
            return (
                False,
                f"Invalid value for 'access-network-type'='{value}'. Must be one of: {', '.join(VALID_BODY_ACCESS_NETWORK_TYPE)}",
            )
    if "access-network-internet" in payload:
        value = payload["access-network-internet"]
        if value not in VALID_BODY_ACCESS_NETWORK_INTERNET:
            return (
                False,
                f"Invalid value for 'access-network-internet'='{value}'. Must be one of: {', '.join(VALID_BODY_ACCESS_NETWORK_INTERNET)}",
            )
    if "access-network-asra" in payload:
        value = payload["access-network-asra"]
        if value not in VALID_BODY_ACCESS_NETWORK_ASRA:
            return (
                False,
                f"Invalid value for 'access-network-asra'='{value}'. Must be one of: {', '.join(VALID_BODY_ACCESS_NETWORK_ASRA)}",
            )
    if "access-network-esr" in payload:
        value = payload["access-network-esr"]
        if value not in VALID_BODY_ACCESS_NETWORK_ESR:
            return (
                False,
                f"Invalid value for 'access-network-esr'='{value}'. Must be one of: {', '.join(VALID_BODY_ACCESS_NETWORK_ESR)}",
            )
    if "access-network-uesa" in payload:
        value = payload["access-network-uesa"]
        if value not in VALID_BODY_ACCESS_NETWORK_UESA:
            return (
                False,
                f"Invalid value for 'access-network-uesa'='{value}'. Must be one of: {', '.join(VALID_BODY_ACCESS_NETWORK_UESA)}",
            )
    if "venue-group" in payload:
        value = payload["venue-group"]
        if value not in VALID_BODY_VENUE_GROUP:
            return (
                False,
                f"Invalid value for 'venue-group'='{value}'. Must be one of: {', '.join(VALID_BODY_VENUE_GROUP)}",
            )
    if "venue-type" in payload:
        value = payload["venue-type"]
        if value not in VALID_BODY_VENUE_TYPE:
            return (
                False,
                f"Invalid value for 'venue-type'='{value}'. Must be one of: {', '.join(VALID_BODY_VENUE_TYPE)}",
            )
    if "proxy-arp" in payload:
        value = payload["proxy-arp"]
        if value not in VALID_BODY_PROXY_ARP:
            return (
                False,
                f"Invalid value for 'proxy-arp'='{value}'. Must be one of: {', '.join(VALID_BODY_PROXY_ARP)}",
            )
    if "l2tif" in payload:
        value = payload["l2tif"]
        if value not in VALID_BODY_L2TIF:
            return (
                False,
                f"Invalid value for 'l2tif'='{value}'. Must be one of: {', '.join(VALID_BODY_L2TIF)}",
            )
    if "pame-bi" in payload:
        value = payload["pame-bi"]
        if value not in VALID_BODY_PAME_BI:
            return (
                False,
                f"Invalid value for 'pame-bi'='{value}'. Must be one of: {', '.join(VALID_BODY_PAME_BI)}",
            )
    if "dgaf" in payload:
        value = payload["dgaf"]
        if value not in VALID_BODY_DGAF:
            return (
                False,
                f"Invalid value for 'dgaf'='{value}'. Must be one of: {', '.join(VALID_BODY_DGAF)}",
            )
    if "wnm-sleep-mode" in payload:
        value = payload["wnm-sleep-mode"]
        if value not in VALID_BODY_WNM_SLEEP_MODE:
            return (
                False,
                f"Invalid value for 'wnm-sleep-mode'='{value}'. Must be one of: {', '.join(VALID_BODY_WNM_SLEEP_MODE)}",
            )
    if "bss-transition" in payload:
        value = payload["bss-transition"]
        if value not in VALID_BODY_BSS_TRANSITION:
            return (
                False,
                f"Invalid value for 'bss-transition'='{value}'. Must be one of: {', '.join(VALID_BODY_BSS_TRANSITION)}",
            )
    if "wba-open-roaming" in payload:
        value = payload["wba-open-roaming"]
        if value not in VALID_BODY_WBA_OPEN_ROAMING:
            return (
                False,
                f"Invalid value for 'wba-open-roaming'='{value}'. Must be one of: {', '.join(VALID_BODY_WBA_OPEN_ROAMING)}",
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
    "endpoint": "wireless_controller/hotspot20/hs_profile",
    "category": "cmdb",
    "api_path": "wireless-controller.hotspot20/hs-profile",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure hotspot profile.",
    "total_fields": 43,
    "required_fields_count": 0,
    "fields_with_defaults_count": 42,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
