"""Validation helpers for wireless_controller/setting - Auto-generated"""

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
    "account-id": "",
    "country": "US",
    "duplicate-ssid": "disable",
    "fapc-compatibility": "disable",
    "wfa-compatibility": "disable",
    "phishing-ssid-detect": "enable",
    "fake-ssid-action": "log",
    "device-weight": 1,
    "device-holdoff": 5,
    "device-idle": 1440,
    "firmware-provision-on-authorization": "disable",
    "rolling-wtp-upgrade": "disable",
    "darrp-optimize": 86400,
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
    "account-id": "string",  # FortiCloud customer account ID.
    "country": "option",  # Country or region in which the FortiGate is located. The cou
    "duplicate-ssid": "option",  # Enable/disable allowing Virtual Access Points (VAPs) to use 
    "fapc-compatibility": "option",  # Enable/disable FAP-C series compatibility.
    "wfa-compatibility": "option",  # Enable/disable WFA compatibility.
    "phishing-ssid-detect": "option",  # Enable/disable phishing SSID detection.
    "fake-ssid-action": "option",  # Actions taken for detected fake SSID.
    "offending-ssid": "string",  # Configure offending SSID.
    "device-weight": "integer",  # Upper limit of confidence of device for identification (0 - 
    "device-holdoff": "integer",  # Lower limit of creation time of device for identification in
    "device-idle": "integer",  # Upper limit of idle time of device for identification in min
    "firmware-provision-on-authorization": "option",  # Enable/disable automatic provisioning of latest firmware on 
    "rolling-wtp-upgrade": "option",  # Enable/disable rolling WTP upgrade (default = disable).
    "darrp-optimize": "integer",  # Time for running Distributed Automatic Radio Resource Provis
    "darrp-optimize-schedules": "string",  # Firewall schedules for DARRP running time. DARRP will run pe
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "account-id": "FortiCloud customer account ID.",
    "country": "Country or region in which the FortiGate is located. The country determines the 802.11 bands and channels that are available.",
    "duplicate-ssid": "Enable/disable allowing Virtual Access Points (VAPs) to use the same SSID name in the same VDOM.",
    "fapc-compatibility": "Enable/disable FAP-C series compatibility.",
    "wfa-compatibility": "Enable/disable WFA compatibility.",
    "phishing-ssid-detect": "Enable/disable phishing SSID detection.",
    "fake-ssid-action": "Actions taken for detected fake SSID.",
    "offending-ssid": "Configure offending SSID.",
    "device-weight": "Upper limit of confidence of device for identification (0 - 255, default = 1, 0 = disable).",
    "device-holdoff": "Lower limit of creation time of device for identification in minutes (0 - 60, default = 5).",
    "device-idle": "Upper limit of idle time of device for identification in minutes (0 - 14400, default = 1440).",
    "firmware-provision-on-authorization": "Enable/disable automatic provisioning of latest firmware on authorization.",
    "rolling-wtp-upgrade": "Enable/disable rolling WTP upgrade (default = disable).",
    "darrp-optimize": "Time for running Distributed Automatic Radio Resource Provisioning (DARRP) optimizations (0 - 86400 sec, default = 86400, 0 = disable).",
    "darrp-optimize-schedules": "Firewall schedules for DARRP running time. DARRP will run periodically based on darrp-optimize within the schedules. Separate multiple schedule names with a space.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "account-id": {"type": "string", "max_length": 63},
    "device-weight": {"type": "integer", "min": 0, "max": 255},
    "device-holdoff": {"type": "integer", "min": 0, "max": 60},
    "device-idle": {"type": "integer", "min": 0, "max": 14400},
    "darrp-optimize": {"type": "integer", "min": 0, "max": 86400},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "offending-ssid": {
        "id": {
            "type": "integer",
            "help": "ID.",
            "default": 0,
            "min_value": 0,
            "max_value": 65535,
        },
        "ssid-pattern": {
            "type": "string",
            "help": "Define offending SSID pattern (case insensitive). For example, word, word*, *word, wo*rd.",
            "required": True,
            "default": "",
            "max_length": 33,
        },
        "action": {
            "type": "option",
            "help": "Actions taken for detected offending SSID.",
            "default": "log",
            "options": [{"help": "Generate logs for detected offending SSID.", "label": "Log", "name": "log"}, {"help": "Suppress detected offending SSID.", "label": "Suppress", "name": "suppress"}],
        },
    },
    "darrp-optimize-schedules": {
        "name": {
            "type": "string",
            "help": "Schedule name.",
            "required": True,
            "default": "",
            "max_length": 35,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_COUNTRY = [
    "--",  # NO_COUNTRY_SET
    "AF",  # AFGHANISTAN
    "AL",  # ALBANIA
    "DZ",  # ALGERIA
    "AS",  # AMERICAN SAMOA
    "AO",  # ANGOLA
    "AR",  # ARGENTINA
    "AM",  # ARMENIA
    "AU",  # AUSTRALIA
    "AT",  # AUSTRIA
    "AZ",  # AZERBAIJAN
    "BS",  # BAHAMAS
    "BH",  # BAHRAIN
    "BD",  # BANGLADESH
    "BB",  # BARBADOS
    "BY",  # BELARUS
    "BE",  # BELGIUM
    "BZ",  # BELIZE
    "BJ",  # BENIN
    "BM",  # BERMUDA
    "BT",  # BHUTAN
    "BO",  # BOLIVIA
    "BA",  # BOSNIA AND HERZEGOVINA
    "BW",  # BOTSWANA
    "BR",  # BRAZIL
    "BN",  # BRUNEI DARUSSALAM
    "BG",  # BULGARIA
    "BF",  # BURKINA-FASO
    "KH",  # CAMBODIA
    "CM",  # CAMEROON
    "KY",  # CAYMAN ISLANDS
    "CF",  # CENTRAL AFRICA REPUBLIC
    "TD",  # CHAD  
    "CL",  # CHILE
    "CN",  # CHINA
    "CX",  # CHRISTMAS ISLAND
    "CO",  # COLOMBIA
    "CG",  # CONGO REPUBLIC
    "CD",  # DEMOCRATIC REPUBLIC OF CONGO
    "CR",  # COSTA RICA
    "HR",  # CROATIA
    "CY",  # CYPRUS
    "CZ",  # CZECH REPUBLIC
    "DK",  # DENMARK
    "DJ",  # DJIBOUTI
    "DM",  # DOMINICA
    "DO",  # DOMINICAN REPUBLIC
    "EC",  # ECUADOR
    "EG",  # EGYPT
    "SV",  # EL SALVADOR
    "ET",  # ETHIOPIA
    "EE",  # ESTONIA
    "GF",  # FRENCH GUIANA
    "PF",  # FRENCH POLYNESIA
    "FO",  # FAEROE ISLANDS
    "FJ",  # FIJI
    "FI",  # FINLAND
    "FR",  # FRANCE
    "GA",  # GABON
    "GE",  # GEORGIA
    "GM",  # GAMBIA
    "DE",  # GERMANY
    "GH",  # GHANA
    "GI",  # GIBRALTAR
    "GR",  # GREECE
    "GL",  # GREENLAND
    "GD",  # GRENADA
    "GP",  # GUADELOUPE
    "GU",  # GUAM
    "GT",  # GUATEMALA
    "GY",  # GUYANA
    "HT",  # HAITI
    "HN",  # HONDURAS
    "HK",  # HONG KONG
    "HU",  # HUNGARY
    "IS",  # ICELAND
    "IN",  # INDIA
    "ID",  # INDONESIA
    "IQ",  # IRAQ
    "IE",  # IRELAND
    "IM",  # ISLE OF MAN
    "IL",  # ISRAEL
    "IT",  # ITALY
    "CI",  # COTE_D_IVOIRE
    "JM",  # JAMAICA
    "JO",  # JORDAN
    "KZ",  # KAZAKHSTAN
    "KE",  # KENYA
    "KR",  # KOREA REPUBLIC
    "KW",  # KUWAIT
    "LA",  # LAOS
    "LV",  # LATVIA
    "LB",  # LEBANON
    "LS",  # LESOTHO
    "LR",  # LIBERIA
    "LY",  # LIBYA
    "LI",  # LIECHTENSTEIN
    "LT",  # LITHUANIA
    "LU",  # LUXEMBOURG
    "MO",  # MACAU SAR
    "MK",  # MACEDONIA, FYRO
    "MG",  # MADAGASCAR
    "MW",  # MALAWI
    "MY",  # MALAYSIA
    "MV",  # MALDIVES
    "ML",  # MALI
    "MT",  # MALTA
    "MH",  # MARSHALL ISLANDS
    "MQ",  # MARTINIQUE
    "MR",  # MAURITANIA
    "MU",  # MAURITIUS
    "YT",  # MAYOTTE
    "MX",  # MEXICO
    "FM",  # MICRONESIA
    "MD",  # REPUBLIC OF MOLDOVA
    "MC",  # MONACO
    "MN",  # MONGOLIA
    "MA",  # MOROCCO
    "MZ",  # MOZAMBIQUE
    "MM",  # MYANMAR
    "NA",  # NAMIBIA
    "NP",  # NEPAL
    "NL",  # NETHERLANDS
    "AN",  # NETHERLANDS ANTILLES
    "AW",  # ARUBA
    "NZ",  # NEW ZEALAND
    "NI",  # NICARAGUA
    "NE",  # NIGER
    "NG",  # NIGERIA
    "NO",  # NORWAY
    "MP",  # NORTHERN MARIANA ISLANDS
    "OM",  # OMAN
    "PK",  # PAKISTAN
    "PW",  # PALAU
    "PA",  # PANAMA
    "PG",  # PAPUA NEW GUINEA
    "PY",  # PARAGUAY
    "PE",  # PERU
    "PH",  # PHILIPPINES
    "PL",  # POLAND
    "PT",  # PORTUGAL
    "PR",  # PUERTO RICO
    "QA",  # QATAR
    "RE",  # REUNION
    "RO",  # ROMANIA
    "RU",  # RUSSIA
    "RW",  # RWANDA
    "BL",  # SAINT BARTHELEMY
    "KN",  # SAINT KITTS AND NEVIS
    "LC",  # SAINT LUCIA
    "MF",  # SAINT MARTIN
    "PM",  # SAINT PIERRE AND MIQUELON
    "VC",  # SAINT VINCENT AND GRENADIENS
    "SA",  # SAUDI ARABIA
    "SN",  # SENEGAL
    "RS",  # REPUBLIC OF SERBIA
    "ME",  # MONTENEGRO
    "SL",  # SIERRA LEONE
    "SG",  # SINGAPORE
    "SK",  # SLOVAKIA
    "SI",  # SLOVENIA
    "SO",  # SOMALIA
    "ZA",  # SOUTH AFRICA
    "ES",  # SPAIN
    "LK",  # SRI LANKA
    "SR",  # SURINAME
    "SZ",  # SWAZILAND
    "SE",  # SWEDEN
    "CH",  # SWITZERLAND
    "TW",  # TAIWAN
    "TZ",  # TANZANIA
    "TH",  # THAILAND
    "TL",  # TIMOR-LESTE
    "TG",  # TOGO
    "TT",  # TRINIDAD AND TOBAGO
    "TN",  # TUNISIA
    "TR",  # TURKEY
    "TM",  # TURKMENISTAN
    "AE",  # UNITED ARAB EMIRATES
    "TC",  # TURKS AND CAICOS
    "UG",  # UGANDA
    "UA",  # UKRAINE
    "GB",  # UNITED KINGDOM
    "US",  # UNITED STATES2
    "PS",  # UNITED STATES (PUBLIC SAFETY)
    "UY",  # URUGUAY
    "UZ",  # UZBEKISTAN
    "VU",  # VANUATU
    "VE",  # VENEZUELA
    "VN",  # VIET NAM
    "VI",  # VIRGIN ISLANDS
    "WF",  # WALLIS AND FUTUNA
    "YE",  # YEMEN
    "ZM",  # ZAMBIA
    "ZW",  # ZIMBABWE
    "JP",  # JAPAN14
    "CA",  # CANADA2
]
VALID_BODY_DUPLICATE_SSID = [
    "enable",  # Allow VAPs to use the same SSID name in the same VDOM.
    "disable",  # Do not allow VAPs to use the same SSID name in the same VDOM.
]
VALID_BODY_FAPC_COMPATIBILITY = [
    "enable",  # Enable FAP-C series compatibility.
    "disable",  # Disable FAP-C series compatibility.
]
VALID_BODY_WFA_COMPATIBILITY = [
    "enable",  # Enable Wi-Fi Alliance Certification compatibility.
    "disable",  # Disable Wi-Fi Alliance Certification compatibility.
]
VALID_BODY_PHISHING_SSID_DETECT = [
    "enable",  # Enable phishing SSID detection.
    "disable",  # Disable phishing SSID detection.
]
VALID_BODY_FAKE_SSID_ACTION = [
    "log",  # Write logs for detected fake SSID.
    "suppress",  # Suppress detected fake SSID.
]
VALID_BODY_FIRMWARE_PROVISION_ON_AUTHORIZATION = [
    "enable",  # Enable firmware provision on authorization.
    "disable",  # Disable firmware provision on authorization.
]
VALID_BODY_ROLLING_WTP_UPGRADE = [
    "enable",  # Enable rolling WTP upgrade.
    "disable",  # Disable rolling WTP upgrade.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_wireless_controller_setting_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for wireless_controller/setting."""
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
    """Validate required fields for wireless_controller/setting."""
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


def validate_wireless_controller_setting_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new wireless_controller/setting object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "country" in payload:
        value = payload["country"]
        if value not in VALID_BODY_COUNTRY:
            desc = FIELD_DESCRIPTIONS.get("country", "")
            error_msg = f"Invalid value for 'country': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_COUNTRY)}"
            error_msg += f"\n  → Example: country='{{ VALID_BODY_COUNTRY[0] }}'"
            return (False, error_msg)
    if "duplicate-ssid" in payload:
        value = payload["duplicate-ssid"]
        if value not in VALID_BODY_DUPLICATE_SSID:
            desc = FIELD_DESCRIPTIONS.get("duplicate-ssid", "")
            error_msg = f"Invalid value for 'duplicate-ssid': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DUPLICATE_SSID)}"
            error_msg += f"\n  → Example: duplicate-ssid='{{ VALID_BODY_DUPLICATE_SSID[0] }}'"
            return (False, error_msg)
    if "fapc-compatibility" in payload:
        value = payload["fapc-compatibility"]
        if value not in VALID_BODY_FAPC_COMPATIBILITY:
            desc = FIELD_DESCRIPTIONS.get("fapc-compatibility", "")
            error_msg = f"Invalid value for 'fapc-compatibility': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FAPC_COMPATIBILITY)}"
            error_msg += f"\n  → Example: fapc-compatibility='{{ VALID_BODY_FAPC_COMPATIBILITY[0] }}'"
            return (False, error_msg)
    if "wfa-compatibility" in payload:
        value = payload["wfa-compatibility"]
        if value not in VALID_BODY_WFA_COMPATIBILITY:
            desc = FIELD_DESCRIPTIONS.get("wfa-compatibility", "")
            error_msg = f"Invalid value for 'wfa-compatibility': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WFA_COMPATIBILITY)}"
            error_msg += f"\n  → Example: wfa-compatibility='{{ VALID_BODY_WFA_COMPATIBILITY[0] }}'"
            return (False, error_msg)
    if "phishing-ssid-detect" in payload:
        value = payload["phishing-ssid-detect"]
        if value not in VALID_BODY_PHISHING_SSID_DETECT:
            desc = FIELD_DESCRIPTIONS.get("phishing-ssid-detect", "")
            error_msg = f"Invalid value for 'phishing-ssid-detect': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PHISHING_SSID_DETECT)}"
            error_msg += f"\n  → Example: phishing-ssid-detect='{{ VALID_BODY_PHISHING_SSID_DETECT[0] }}'"
            return (False, error_msg)
    if "fake-ssid-action" in payload:
        value = payload["fake-ssid-action"]
        if value not in VALID_BODY_FAKE_SSID_ACTION:
            desc = FIELD_DESCRIPTIONS.get("fake-ssid-action", "")
            error_msg = f"Invalid value for 'fake-ssid-action': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FAKE_SSID_ACTION)}"
            error_msg += f"\n  → Example: fake-ssid-action='{{ VALID_BODY_FAKE_SSID_ACTION[0] }}'"
            return (False, error_msg)
    if "firmware-provision-on-authorization" in payload:
        value = payload["firmware-provision-on-authorization"]
        if value not in VALID_BODY_FIRMWARE_PROVISION_ON_AUTHORIZATION:
            desc = FIELD_DESCRIPTIONS.get("firmware-provision-on-authorization", "")
            error_msg = f"Invalid value for 'firmware-provision-on-authorization': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FIRMWARE_PROVISION_ON_AUTHORIZATION)}"
            error_msg += f"\n  → Example: firmware-provision-on-authorization='{{ VALID_BODY_FIRMWARE_PROVISION_ON_AUTHORIZATION[0] }}'"
            return (False, error_msg)
    if "rolling-wtp-upgrade" in payload:
        value = payload["rolling-wtp-upgrade"]
        if value not in VALID_BODY_ROLLING_WTP_UPGRADE:
            desc = FIELD_DESCRIPTIONS.get("rolling-wtp-upgrade", "")
            error_msg = f"Invalid value for 'rolling-wtp-upgrade': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ROLLING_WTP_UPGRADE)}"
            error_msg += f"\n  → Example: rolling-wtp-upgrade='{{ VALID_BODY_ROLLING_WTP_UPGRADE[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_wireless_controller_setting_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update wireless_controller/setting."""
    # Step 1: Validate enum values
    if "country" in payload:
        value = payload["country"]
        if value not in VALID_BODY_COUNTRY:
            return (
                False,
                f"Invalid value for 'country'='{value}'. Must be one of: {', '.join(VALID_BODY_COUNTRY)}",
            )
    if "duplicate-ssid" in payload:
        value = payload["duplicate-ssid"]
        if value not in VALID_BODY_DUPLICATE_SSID:
            return (
                False,
                f"Invalid value for 'duplicate-ssid'='{value}'. Must be one of: {', '.join(VALID_BODY_DUPLICATE_SSID)}",
            )
    if "fapc-compatibility" in payload:
        value = payload["fapc-compatibility"]
        if value not in VALID_BODY_FAPC_COMPATIBILITY:
            return (
                False,
                f"Invalid value for 'fapc-compatibility'='{value}'. Must be one of: {', '.join(VALID_BODY_FAPC_COMPATIBILITY)}",
            )
    if "wfa-compatibility" in payload:
        value = payload["wfa-compatibility"]
        if value not in VALID_BODY_WFA_COMPATIBILITY:
            return (
                False,
                f"Invalid value for 'wfa-compatibility'='{value}'. Must be one of: {', '.join(VALID_BODY_WFA_COMPATIBILITY)}",
            )
    if "phishing-ssid-detect" in payload:
        value = payload["phishing-ssid-detect"]
        if value not in VALID_BODY_PHISHING_SSID_DETECT:
            return (
                False,
                f"Invalid value for 'phishing-ssid-detect'='{value}'. Must be one of: {', '.join(VALID_BODY_PHISHING_SSID_DETECT)}",
            )
    if "fake-ssid-action" in payload:
        value = payload["fake-ssid-action"]
        if value not in VALID_BODY_FAKE_SSID_ACTION:
            return (
                False,
                f"Invalid value for 'fake-ssid-action'='{value}'. Must be one of: {', '.join(VALID_BODY_FAKE_SSID_ACTION)}",
            )
    if "firmware-provision-on-authorization" in payload:
        value = payload["firmware-provision-on-authorization"]
        if value not in VALID_BODY_FIRMWARE_PROVISION_ON_AUTHORIZATION:
            return (
                False,
                f"Invalid value for 'firmware-provision-on-authorization'='{value}'. Must be one of: {', '.join(VALID_BODY_FIRMWARE_PROVISION_ON_AUTHORIZATION)}",
            )
    if "rolling-wtp-upgrade" in payload:
        value = payload["rolling-wtp-upgrade"]
        if value not in VALID_BODY_ROLLING_WTP_UPGRADE:
            return (
                False,
                f"Invalid value for 'rolling-wtp-upgrade'='{value}'. Must be one of: {', '.join(VALID_BODY_ROLLING_WTP_UPGRADE)}",
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
    "endpoint": "wireless_controller/setting",
    "category": "cmdb",
    "api_path": "wireless-controller/setting",
    "help": "VDOM wireless controller configuration.",
    "total_fields": 15,
    "required_fields_count": 0,
    "fields_with_defaults_count": 13,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
