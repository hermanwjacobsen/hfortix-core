"""Validation helpers for extension_controller/extender_profile - Auto-generated"""

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
    "login-password",  # Set the managed extender's administrator password.
    "cellular",  # FortiExtender cellular configuration.
    "lan-extension",  # FortiExtender LAN extension configuration.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "id": 32,
    "model": "FX201E",
    "extension": "wan-extension",
    "allowaccess": "",
    "login-password-change": "no",
    "enforce-bandwidth": "disable",
    "bandwidth-limit": 1024,
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
    "name": "string",  # FortiExtender profile name.
    "id": "integer",  # ID.
    "model": "option",  # Model.
    "extension": "option",  # Extension option.
    "allowaccess": "option",  # Control management access to the managed extender. Separate 
    "login-password-change": "option",  # Change or reset the administrator password of a managed exte
    "login-password": "password",  # Set the managed extender's administrator password.
    "enforce-bandwidth": "option",  # Enable/disable enforcement of bandwidth on LAN extension int
    "bandwidth-limit": "integer",  # FortiExtender LAN extension bandwidth limit (Mbps).
    "cellular": "string",  # FortiExtender cellular configuration.
    "wifi": "string",  # FortiExtender Wi-Fi configuration.
    "lan-extension": "string",  # FortiExtender LAN extension configuration.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "FortiExtender profile name.",
    "id": "ID.",
    "model": "Model.",
    "extension": "Extension option.",
    "allowaccess": "Control management access to the managed extender. Separate entries with a space.",
    "login-password-change": "Change or reset the administrator password of a managed extender (yes, default, or no, default = no).",
    "login-password": "Set the managed extender's administrator password.",
    "enforce-bandwidth": "Enable/disable enforcement of bandwidth on LAN extension interface.",
    "bandwidth-limit": "FortiExtender LAN extension bandwidth limit (Mbps).",
    "cellular": "FortiExtender cellular configuration.",
    "wifi": "FortiExtender Wi-Fi configuration.",
    "lan-extension": "FortiExtender LAN extension configuration.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 31},
    "id": {"type": "integer", "min": 0, "max": 102400000},
    "bandwidth-limit": {"type": "integer", "min": 1, "max": 16776000},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "cellular": {
        "dataplan": {
            "type": "string",
            "help": "Dataplan names.",
        },
        "controller-report": {
            "type": "string",
            "help": "FortiExtender controller report configuration.",
        },
        "sms-notification": {
            "type": "string",
            "help": "FortiExtender cellular SMS notification configuration.",
        },
        "modem1": {
            "type": "string",
            "help": "Configuration options for modem 1.",
        },
        "modem2": {
            "type": "string",
            "help": "Configuration options for modem 2.",
        },
    },
    "wifi": {
        "country": {
            "type": "option",
            "help": "Country in which this FEX will operate (default = NA).",
            "default": "--",
            "options": [{"help": "NO_COUNTRY_SET", "label": "  ", "name": "--"}, {"help": "AFGHANISTAN", "label": "Af", "name": "AF"}, {"help": "ALBANIA", "label": "Al", "name": "AL"}, {"help": "ALGERIA", "label": "Dz", "name": "DZ"}, {"help": "AMERICAN SAMOA", "label": "As", "name": "AS"}, {"help": "ANGOLA", "label": "Ao", "name": "AO"}, {"help": "ARGENTINA", "label": "Ar", "name": "AR"}, {"help": "ARMENIA", "label": "Am", "name": "AM"}, {"help": "AUSTRALIA", "label": "Au", "name": "AU"}, {"help": "AUSTRIA", "label": "At", "name": "AT"}, {"help": "AZERBAIJAN", "label": "Az", "name": "AZ"}, {"help": "BAHAMAS", "label": "Bs", "name": "BS"}, {"help": "BAHRAIN", "label": "Bh", "name": "BH"}, {"help": "BANGLADESH", "label": "Bd", "name": "BD"}, {"help": "BARBADOS", "label": "Bb", "name": "BB"}, {"help": "BELARUS", "label": "By", "name": "BY"}, {"help": "BELGIUM", "label": "Be", "name": "BE"}, {"help": "BELIZE", "label": "Bz", "name": "BZ"}, {"help": "BENIN", "label": "Bj", "name": "BJ"}, {"help": "BERMUDA", "label": "Bm", "name": "BM"}, {"help": "BHUTAN", "label": "Bt", "name": "BT"}, {"help": "BOLIVIA", "label": "Bo", "name": "BO"}, {"help": "BOSNIA AND HERZEGOVINA", "label": "Ba", "name": "BA"}, {"help": "BOTSWANA", "label": "Bw", "name": "BW"}, {"help": "BRAZIL", "label": "Br", "name": "BR"}, {"help": "BRUNEI DARUSSALAM", "label": "Bn", "name": "BN"}, {"help": "BULGARIA", "label": "Bg", "name": "BG"}, {"help": "BURKINA-FASO", "label": "Bf", "name": "BF"}, {"help": "CAMBODIA", "label": "Kh", "name": "KH"}, {"help": "CAMEROON", "label": "Cm", "name": "CM"}, {"help": "CAYMAN ISLANDS", "label": "Ky", "name": "KY"}, {"help": "CENTRAL AFRICA REPUBLIC", "label": "Cf", "name": "CF"}, {"help": "CHAD  ", "label": "Td", "name": "TD"}, {"help": "CHILE", "label": "Cl", "name": "CL"}, {"help": "CHINA", "label": "Cn", "name": "CN"}, {"help": "CHRISTMAS ISLAND", "label": "Cx", "name": "CX"}, {"help": "COLOMBIA", "label": "Co", "name": "CO"}, {"help": "CONGO REPUBLIC", "label": "Cg", "name": "CG"}, {"help": "DEMOCRATIC REPUBLIC OF CONGO", "label": "Cd", "name": "CD"}, {"help": "COSTA RICA", "label": "Cr", "name": "CR"}, {"help": "CROATIA", "label": "Hr", "name": "HR"}, {"help": "CYPRUS", "label": "Cy", "name": "CY"}, {"help": "CZECH REPUBLIC", "label": "Cz", "name": "CZ"}, {"help": "DENMARK", "label": "Dk", "name": "DK"}, {"help": "DJIBOUTI", "label": "Dj", "name": "DJ"}, {"help": "DOMINICA", "label": "Dm", "name": "DM"}, {"help": "DOMINICAN REPUBLIC", "label": "Do", "name": "DO"}, {"help": "ECUADOR", "label": "Ec", "name": "EC"}, {"help": "EGYPT", "label": "Eg", "name": "EG"}, {"help": "EL SALVADOR", "label": "Sv", "name": "SV"}, {"help": "ETHIOPIA", "label": "Et", "name": "ET"}, {"help": "ESTONIA", "label": "Ee", "name": "EE"}, {"help": "FRENCH GUIANA", "label": "Gf", "name": "GF"}, {"help": "FRENCH POLYNESIA", "label": "Pf", "name": "PF"}, {"help": "FAEROE ISLANDS", "label": "Fo", "name": "FO"}, {"help": "FIJI", "label": "Fj", "name": "FJ"}, {"help": "FINLAND", "label": "Fi", "name": "FI"}, {"help": "FRANCE", "label": "Fr", "name": "FR"}, {"help": "GABON", "label": "Ga", "name": "GA"}, {"help": "GEORGIA", "label": "Ge", "name": "GE"}, {"help": "GAMBIA", "label": "Gm", "name": "GM"}, {"help": "GERMANY", "label": "De", "name": "DE"}, {"help": "GHANA", "label": "Gh", "name": "GH"}, {"help": "GIBRALTAR", "label": "Gi", "name": "GI"}, {"help": "GREECE", "label": "Gr", "name": "GR"}, {"help": "GREENLAND", "label": "Gl", "name": "GL"}, {"help": "GRENADA", "label": "Gd", "name": "GD"}, {"help": "GUADELOUPE", "label": "Gp", "name": "GP"}, {"help": "GUAM", "label": "Gu", "name": "GU"}, {"help": "GUATEMALA", "label": "Gt", "name": "GT"}, {"help": "GUYANA", "label": "Gy", "name": "GY"}, {"help": "HAITI", "label": "Ht", "name": "HT"}, {"help": "HONDURAS", "label": "Hn", "name": "HN"}, {"help": "HONG KONG", "label": "Hk", "name": "HK"}, {"help": "HUNGARY", "label": "Hu", "name": "HU"}, {"help": "ICELAND", "label": "Is", "name": "IS"}, {"help": "INDIA", "label": "In", "name": "IN"}, {"help": "INDONESIA", "label": "Id", "name": "ID"}, {"help": "IRAQ", "label": "Iq", "name": "IQ"}, {"help": "IRELAND", "label": "Ie", "name": "IE"}, {"help": "ISLE OF MAN", "label": "Im", "name": "IM"}, {"help": "ISRAEL", "label": "Il", "name": "IL"}, {"help": "ITALY", "label": "It", "name": "IT"}, {"help": "COTE_D_IVOIRE", "label": "Ci", "name": "CI"}, {"help": "JAMAICA", "label": "Jm", "name": "JM"}, {"help": "JORDAN", "label": "Jo", "name": "JO"}, {"help": "KAZAKHSTAN", "label": "Kz", "name": "KZ"}, {"help": "KENYA", "label": "Ke", "name": "KE"}, {"help": "KOREA REPUBLIC", "label": "Kr", "name": "KR"}, {"help": "KUWAIT", "label": "Kw", "name": "KW"}, {"help": "LAOS", "label": "La", "name": "LA"}, {"help": "LATVIA", "label": "Lv", "name": "LV"}, {"help": "LEBANON", "label": "Lb", "name": "LB"}, {"help": "LESOTHO", "label": "Ls", "name": "LS"}, {"help": "LIBERIA", "label": "Lr", "name": "LR"}, {"help": "LIBYA", "label": "Ly", "name": "LY"}, {"help": "LIECHTENSTEIN", "label": "Li", "name": "LI"}, {"help": "LITHUANIA", "label": "Lt", "name": "LT"}, {"help": "LUXEMBOURG", "label": "Lu", "name": "LU"}, {"help": "MACAU SAR", "label": "Mo", "name": "MO"}, {"help": "MACEDONIA, FYRO", "label": "Mk", "name": "MK"}, {"help": "MADAGASCAR", "label": "Mg", "name": "MG"}, {"help": "MALAWI", "label": "Mw", "name": "MW"}, {"help": "MALAYSIA", "label": "My", "name": "MY"}, {"help": "MALDIVES", "label": "Mv", "name": "MV"}, {"help": "MALI", "label": "Ml", "name": "ML"}, {"help": "MALTA", "label": "Mt", "name": "MT"}, {"help": "MARSHALL ISLANDS", "label": "Mh", "name": "MH"}, {"help": "MARTINIQUE", "label": "Mq", "name": "MQ"}, {"help": "MAURITANIA", "label": "Mr", "name": "MR"}, {"help": "MAURITIUS", "label": "Mu", "name": "MU"}, {"help": "MAYOTTE", "label": "Yt", "name": "YT"}, {"help": "MEXICO", "label": "Mx", "name": "MX"}, {"help": "MICRONESIA", "label": "Fm", "name": "FM"}, {"help": "REPUBLIC OF MOLDOVA", "label": "Md", "name": "MD"}, {"help": "MONACO", "label": "Mc", "name": "MC"}, {"help": "MONGOLIA", "label": "Mn", "name": "MN"}, {"help": "MOROCCO", "label": "Ma", "name": "MA"}, {"help": "MOZAMBIQUE", "label": "Mz", "name": "MZ"}, {"help": "MYANMAR", "label": "Mm", "name": "MM"}, {"help": "NAMIBIA", "label": "Na", "name": "NA"}, {"help": "NEPAL", "label": "Np", "name": "NP"}, {"help": "NETHERLANDS", "label": "Nl", "name": "NL"}, {"help": "NETHERLANDS ANTILLES", "label": "An", "name": "AN"}, {"help": "ARUBA", "label": "Aw", "name": "AW"}, {"help": "NEW ZEALAND", "label": "Nz", "name": "NZ"}, {"help": "NICARAGUA", "label": "Ni", "name": "NI"}, {"help": "NIGER", "label": "Ne", "name": "NE"}, {"help": "NIGERIA", "label": "Ng", "name": "NG"}, {"help": "NORWAY", "label": "No", "name": "NO"}, {"help": "NORTHERN MARIANA ISLANDS", "label": "Mp", "name": "MP"}, {"help": "OMAN", "label": "Om", "name": "OM"}, {"help": "PAKISTAN", "label": "Pk", "name": "PK"}, {"help": "PALAU", "label": "Pw", "name": "PW"}, {"help": "PANAMA", "label": "Pa", "name": "PA"}, {"help": "PAPUA NEW GUINEA", "label": "Pg", "name": "PG"}, {"help": "PARAGUAY", "label": "Py", "name": "PY"}, {"help": "PERU", "label": "Pe", "name": "PE"}, {"help": "PHILIPPINES", "label": "Ph", "name": "PH"}, {"help": "POLAND", "label": "Pl", "name": "PL"}, {"help": "PORTUGAL", "label": "Pt", "name": "PT"}, {"help": "PUERTO RICO", "label": "Pr", "name": "PR"}, {"help": "QATAR", "label": "Qa", "name": "QA"}, {"help": "REUNION", "label": "Re", "name": "RE"}, {"help": "ROMANIA", "label": "Ro", "name": "RO"}, {"help": "RUSSIA", "label": "Ru", "name": "RU"}, {"help": "RWANDA", "label": "Rw", "name": "RW"}, {"help": "SAINT BARTHELEMY", "label": "Bl", "name": "BL"}, {"help": "SAINT KITTS AND NEVIS", "label": "Kn", "name": "KN"}, {"help": "SAINT LUCIA", "label": "Lc", "name": "LC"}, {"help": "SAINT MARTIN", "label": "Mf", "name": "MF"}, {"help": "SAINT PIERRE AND MIQUELON", "label": "Pm", "name": "PM"}, {"help": "SAINT VINCENT AND GRENADIENS", "label": "Vc", "name": "VC"}, {"help": "SAUDI ARABIA", "label": "Sa", "name": "SA"}, {"help": "SENEGAL", "label": "Sn", "name": "SN"}, {"help": "REPUBLIC OF SERBIA", "label": "Rs", "name": "RS"}, {"help": "MONTENEGRO", "label": "Me", "name": "ME"}, {"help": "SIERRA LEONE", "label": "Sl", "name": "SL"}, {"help": "SINGAPORE", "label": "Sg", "name": "SG"}, {"help": "SLOVAKIA", "label": "Sk", "name": "SK"}, {"help": "SLOVENIA", "label": "Si", "name": "SI"}, {"help": "SOMALIA", "label": "So", "name": "SO"}, {"help": "SOUTH AFRICA", "label": "Za", "name": "ZA"}, {"help": "SPAIN", "label": "Es", "name": "ES"}, {"help": "SRI LANKA", "label": "Lk", "name": "LK"}, {"help": "SURINAME", "label": "Sr", "name": "SR"}, {"help": "SWAZILAND", "label": "Sz", "name": "SZ"}, {"help": "SWEDEN", "label": "Se", "name": "SE"}, {"help": "SWITZERLAND", "label": "Ch", "name": "CH"}, {"help": "TAIWAN", "label": "Tw", "name": "TW"}, {"help": "TANZANIA", "label": "Tz", "name": "TZ"}, {"help": "THAILAND", "label": "Th", "name": "TH"}, {"help": "TIMOR-LESTE", "label": "Tl", "name": "TL"}, {"help": "TOGO", "label": "Tg", "name": "TG"}, {"help": "TRINIDAD AND TOBAGO", "label": "Tt", "name": "TT"}, {"help": "TUNISIA", "label": "Tn", "name": "TN"}, {"help": "TURKEY", "label": "Tr", "name": "TR"}, {"help": "TURKMENISTAN", "label": "Tm", "name": "TM"}, {"help": "UNITED ARAB EMIRATES", "label": "Ae", "name": "AE"}, {"help": "TURKS AND CAICOS", "label": "Tc", "name": "TC"}, {"help": "UGANDA", "label": "Ug", "name": "UG"}, {"help": "UKRAINE", "label": "Ua", "name": "UA"}, {"help": "UNITED KINGDOM", "label": "Gb", "name": "GB"}, {"help": "UNITED STATES2", "label": "Us", "name": "US"}, {"help": "UNITED STATES (PUBLIC SAFETY)", "label": "Ps", "name": "PS"}, {"help": "URUGUAY", "label": "Uy", "name": "UY"}, {"help": "UZBEKISTAN", "label": "Uz", "name": "UZ"}, {"help": "VANUATU", "label": "Vu", "name": "VU"}, {"help": "VENEZUELA", "label": "Ve", "name": "VE"}, {"help": "VIET NAM", "label": "Vn", "name": "VN"}, {"help": "VIRGIN ISLANDS", "label": "Vi", "name": "VI"}, {"help": "WALLIS AND FUTUNA", "label": "Wf", "name": "WF"}, {"help": "YEMEN", "label": "Ye", "name": "YE"}, {"help": "ZAMBIA", "label": "Zm", "name": "ZM"}, {"help": "ZIMBABWE", "label": "Zw", "name": "ZW"}, {"help": "JAPAN14", "label": "Jp", "name": "JP"}, {"help": "CANADA2", "label": "Ca", "name": "CA"}],
        },
        "radio-1": {
            "type": "string",
            "help": "Radio-1 config for Wi-Fi 2.4GHz",
        },
        "radio-2": {
            "type": "string",
            "help": "Radio-2 config for Wi-Fi 5GHz",
        },
    },
    "lan-extension": {
        "link-loadbalance": {
            "type": "option",
            "help": "LAN extension link load balance strategy.",
            "required": True,
            "default": "activebackup",
            "options": [{"help": "FortiExtender LAN extension active-backup.", "label": "Activebackup", "name": "activebackup"}, {"help": "FortiExtender LAN extension load-balance.", "label": "Loadbalance", "name": "loadbalance"}],
        },
        "ipsec-tunnel": {
            "type": "string",
            "help": "IPsec tunnel name.",
            "default": "",
            "max_length": 15,
        },
        "backhaul-interface": {
            "type": "string",
            "help": "IPsec phase1 interface.",
            "default": "",
            "max_length": 15,
        },
        "backhaul-ip": {
            "type": "string",
            "help": "IPsec phase1 IPv4/FQDN. Used to specify the external IP/FQDN when the FortiGate unit is behind a NAT device.",
            "default": "",
            "max_length": 63,
        },
        "backhaul": {
            "type": "string",
            "help": "LAN extension backhaul tunnel configuration.",
        },
        "downlinks": {
            "type": "string",
            "help": "Config FortiExtender downlink interface for LAN extension.",
        },
        "traffic-split-services": {
            "type": "string",
            "help": "Config FortiExtender traffic split interface for LAN extension.",
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_MODEL = [
    "FX201E",  # FEX-201E model.
    "FX211E",  # FEX-211E model.
    "FX200F",  # FEX-200F model.
    "FXA11F",  # FEX-101F-AM model.
    "FXE11F",  # FEX-101F-EA model.
    "FXA21F",  # FEX-201F-AM model.
    "FXE21F",  # FEX-201F-EA model.
    "FXA22F",  # FEX-202F-AM model.
    "FXE22F",  # FEX-202F-EA model.
    "FX212F",  # FEX-212F model.
    "FX311F",  # FEX-311F model.
    "FX312F",  # FEX-312F model.
    "FX511F",  # FEX-511F model.
    "FXR51G",  # FER-511G model.
    "FXN51G",  # FEX-511G model.
    "FXW51G",  # FEX-511G-Wifi model.
    "FVG21F",  # FEV-211F model.
    "FVA21F",  # FEV-211F-AM model.
    "FVG22F",  # FEV-212F model.
    "FVA22F",  # FEV-212F-AM model.
    "FX04DA",  # FX40D-AMEU model.
    "FG",  # FG-CONNECTOR model.
    "BS10FW",  # FBS-10FW model.
    "BS20GW",  # FBS-20GW model.
    "BS20GN",  # FBS-20G model.
    "FVG51G",  # FEV-511G model.
    "FXE11G",  # FEX-101G model.
    "FX211G",  # FEX-211G model.
]
VALID_BODY_EXTENSION = [
    "wan-extension",  # WAN extension.
    "lan-extension",  # LAN extension.
]
VALID_BODY_ALLOWACCESS = [
    "ping",  # PING access.
    "telnet",  # TELNET access.
    "http",  # HTTP access.
    "https",  # HTTPS access.
    "ssh",  # SSH access.
    "snmp",  # SNMP access.
]
VALID_BODY_LOGIN_PASSWORD_CHANGE = [
    "yes",  # Change the managed extender's administrator password. Use the login-password option to set the password.
    "default",  # Keep the managed extender's administrator password set to the factory default.
    "no",  # Do not change the managed extender's administrator password.
]
VALID_BODY_ENFORCE_BANDWIDTH = [
    "enable",  # Enable to enforce bandwidth limit on LAN extension interface.
    "disable",  # Disable to enforce bandwidth limit on LAN extension interface.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_extension_controller_extender_profile_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for extension_controller/extender_profile."""
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
    """Validate required fields for extension_controller/extender_profile."""
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


def validate_extension_controller_extender_profile_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new extension_controller/extender_profile object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "model" in payload:
        value = payload["model"]
        if value not in VALID_BODY_MODEL:
            desc = FIELD_DESCRIPTIONS.get("model", "")
            error_msg = f"Invalid value for 'model': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MODEL)}"
            error_msg += f"\n  → Example: model='{{ VALID_BODY_MODEL[0] }}'"
            return (False, error_msg)
    if "extension" in payload:
        value = payload["extension"]
        if value not in VALID_BODY_EXTENSION:
            desc = FIELD_DESCRIPTIONS.get("extension", "")
            error_msg = f"Invalid value for 'extension': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_EXTENSION)}"
            error_msg += f"\n  → Example: extension='{{ VALID_BODY_EXTENSION[0] }}'"
            return (False, error_msg)
    if "allowaccess" in payload:
        value = payload["allowaccess"]
        if value not in VALID_BODY_ALLOWACCESS:
            desc = FIELD_DESCRIPTIONS.get("allowaccess", "")
            error_msg = f"Invalid value for 'allowaccess': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ALLOWACCESS)}"
            error_msg += f"\n  → Example: allowaccess='{{ VALID_BODY_ALLOWACCESS[0] }}'"
            return (False, error_msg)
    if "login-password-change" in payload:
        value = payload["login-password-change"]
        if value not in VALID_BODY_LOGIN_PASSWORD_CHANGE:
            desc = FIELD_DESCRIPTIONS.get("login-password-change", "")
            error_msg = f"Invalid value for 'login-password-change': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LOGIN_PASSWORD_CHANGE)}"
            error_msg += f"\n  → Example: login-password-change='{{ VALID_BODY_LOGIN_PASSWORD_CHANGE[0] }}'"
            return (False, error_msg)
    if "enforce-bandwidth" in payload:
        value = payload["enforce-bandwidth"]
        if value not in VALID_BODY_ENFORCE_BANDWIDTH:
            desc = FIELD_DESCRIPTIONS.get("enforce-bandwidth", "")
            error_msg = f"Invalid value for 'enforce-bandwidth': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ENFORCE_BANDWIDTH)}"
            error_msg += f"\n  → Example: enforce-bandwidth='{{ VALID_BODY_ENFORCE_BANDWIDTH[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_extension_controller_extender_profile_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update extension_controller/extender_profile."""
    # Step 1: Validate enum values
    if "model" in payload:
        value = payload["model"]
        if value not in VALID_BODY_MODEL:
            return (
                False,
                f"Invalid value for 'model'='{value}'. Must be one of: {', '.join(VALID_BODY_MODEL)}",
            )
    if "extension" in payload:
        value = payload["extension"]
        if value not in VALID_BODY_EXTENSION:
            return (
                False,
                f"Invalid value for 'extension'='{value}'. Must be one of: {', '.join(VALID_BODY_EXTENSION)}",
            )
    if "allowaccess" in payload:
        value = payload["allowaccess"]
        if value not in VALID_BODY_ALLOWACCESS:
            return (
                False,
                f"Invalid value for 'allowaccess'='{value}'. Must be one of: {', '.join(VALID_BODY_ALLOWACCESS)}",
            )
    if "login-password-change" in payload:
        value = payload["login-password-change"]
        if value not in VALID_BODY_LOGIN_PASSWORD_CHANGE:
            return (
                False,
                f"Invalid value for 'login-password-change'='{value}'. Must be one of: {', '.join(VALID_BODY_LOGIN_PASSWORD_CHANGE)}",
            )
    if "enforce-bandwidth" in payload:
        value = payload["enforce-bandwidth"]
        if value not in VALID_BODY_ENFORCE_BANDWIDTH:
            return (
                False,
                f"Invalid value for 'enforce-bandwidth'='{value}'. Must be one of: {', '.join(VALID_BODY_ENFORCE_BANDWIDTH)}",
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
    "endpoint": "extension_controller/extender_profile",
    "category": "cmdb",
    "api_path": "extension-controller/extender-profile",
    "mkey": "name",
    "mkey_type": "string",
    "help": "FortiExtender extender profile configuration.",
    "total_fields": 12,
    "required_fields_count": 3,
    "fields_with_defaults_count": 8,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
