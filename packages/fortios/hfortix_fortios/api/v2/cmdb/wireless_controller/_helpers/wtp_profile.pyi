from typing import Any, Literal

# Enum type aliases for validation
VALID_BODY_CONTROL_MESSAGE_OFFLOAD: Literal["ebp-frame", "aeroscout-tag", "ap-list", "sta-list", "sta-cap-list", "stats", "aeroscout-mu", "sta-health", "spectral-analysis"]
VALID_BODY_APCFG_MESH: Literal["enable", "disable"]
VALID_BODY_APCFG_MESH_AP_TYPE: Literal["ethernet", "mesh", "auto"]
VALID_BODY_APCFG_MESH_ETH_BRIDGE: Literal["enable", "disable"]
VALID_BODY_WAN_PORT_MODE: Literal["wan-lan", "wan-only"]
VALID_BODY_ENERGY_EFFICIENT_ETHERNET: Literal["enable", "disable"]
VALID_BODY_LED_STATE: Literal["enable", "disable"]
VALID_BODY_DTLS_POLICY: Literal["clear-text", "dtls-enabled", "ipsec-vpn", "ipsec-sn-vpn"]
VALID_BODY_DTLS_IN_KERNEL: Literal["enable", "disable"]
VALID_BODY_HANDOFF_ROAMING: Literal["enable", "disable"]
VALID_BODY_AP_COUNTRY: Literal["--", "AF", "AL", "DZ", "AS", "AO", "AR", "AM", "AU", "AT", "AZ", "BS", "BH", "BD", "BB", "BY", "BE", "BZ", "BJ", "BM", "BT", "BO", "BA", "BW", "BR", "BN", "BG", "BF", "KH", "CM", "KY", "CF", "TD", "CL", "CN", "CX", "CO", "CG", "CD", "CR", "HR", "CY", "CZ", "DK", "DJ", "DM", "DO", "EC", "EG", "SV", "ET", "EE", "GF", "PF", "FO", "FJ", "FI", "FR", "GA", "GE", "GM", "DE", "GH", "GI", "GR", "GL", "GD", "GP", "GU", "GT", "GY", "HT", "HN", "HK", "HU", "IS", "IN", "ID", "IQ", "IE", "IM", "IL", "IT", "CI", "JM", "JO", "KZ", "KE", "KR", "KW", "LA", "LV", "LB", "LS", "LR", "LY", "LI", "LT", "LU", "MO", "MK", "MG", "MW", "MY", "MV", "ML", "MT", "MH", "MQ", "MR", "MU", "YT", "MX", "FM", "MD", "MC", "MN", "MA", "MZ", "MM", "NA", "NP", "NL", "AN", "AW", "NZ", "NI", "NE", "NG", "NO", "MP", "OM", "PK", "PW", "PA", "PG", "PY", "PE", "PH", "PL", "PT", "PR", "QA", "RE", "RO", "RU", "RW", "BL", "KN", "LC", "MF", "PM", "VC", "SA", "SN", "RS", "ME", "SL", "SG", "SK", "SI", "SO", "ZA", "ES", "LK", "SR", "SZ", "SE", "CH", "TW", "TZ", "TH", "TL", "TG", "TT", "TN", "TR", "TM", "AE", "TC", "UG", "UA", "GB", "US", "PS", "UY", "UZ", "VU", "VE", "VN", "VI", "WF", "YE", "ZM", "ZW", "JP", "CA"]
VALID_BODY_IP_FRAGMENT_PREVENTING: Literal["tcp-mss-adjust", "icmp-unreachable"]
VALID_BODY_SPLIT_TUNNELING_ACL_PATH: Literal["tunnel", "local"]
VALID_BODY_SPLIT_TUNNELING_ACL_LOCAL_AP_SUBNET: Literal["enable", "disable"]
VALID_BODY_ALLOWACCESS: Literal["https", "ssh", "snmp"]
VALID_BODY_LOGIN_PASSWD_CHANGE: Literal["yes", "default", "no"]
VALID_BODY_LLDP: Literal["enable", "disable"]
VALID_BODY_POE_MODE: Literal["auto", "8023af", "8023at", "power-adapter", "full", "high", "low"]
VALID_BODY_USB_PORT: Literal["enable", "disable"]
VALID_BODY_FREQUENCY_HANDOFF: Literal["enable", "disable"]
VALID_BODY_AP_HANDOFF: Literal["enable", "disable"]
VALID_BODY_DEFAULT_MESH_ROOT: Literal["enable", "disable"]
VALID_BODY_EXT_INFO_ENABLE: Literal["enable", "disable"]
VALID_BODY_INDOOR_OUTDOOR_DEPLOYMENT: Literal["platform-determined", "outdoor", "indoor"]
VALID_BODY_CONSOLE_LOGIN: Literal["enable", "disable"]
VALID_BODY_WAN_PORT_AUTH: Literal["none", "802.1x"]
VALID_BODY_WAN_PORT_AUTH_METHODS: Literal["all", "EAP-FAST", "EAP-TLS", "EAP-PEAP"]
VALID_BODY_WAN_PORT_AUTH_MACSEC: Literal["enable", "disable"]
VALID_BODY_UNII_4_5GHZ_BAND: Literal["enable", "disable"]
VALID_BODY_ADMIN_RESTRICT_LOCAL: Literal["enable", "disable"]

# Metadata dictionaries
FIELD_TYPES: dict[str, str]
FIELD_DESCRIPTIONS: dict[str, str]
FIELD_CONSTRAINTS: dict[str, dict[str, Any]]
NESTED_SCHEMAS: dict[str, dict[str, Any]]
FIELDS_WITH_DEFAULTS: dict[str, Any]

# Helper functions
def get_field_type(field_name: str) -> str | None: ...
def get_field_description(field_name: str) -> str | None: ...
def get_field_default(field_name: str) -> Any: ...
def get_field_constraints(field_name: str) -> dict[str, Any]: ...
def get_nested_schema(field_name: str) -> dict[str, Any] | None: ...
def get_field_metadata(field_name: str) -> dict[str, Any]: ...
def validate_field_value(field_name: str, value: Any) -> bool: ...
def get_all_fields() -> list[str]: ...
def get_required_fields() -> list[str]: ...
def get_schema_info() -> dict[str, Any]: ...