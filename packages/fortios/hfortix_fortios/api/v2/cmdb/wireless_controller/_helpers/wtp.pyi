from typing import Any, Literal

# Enum type aliases for validation
VALID_BODY_ADMIN: Literal["discovered", "disable", "enable"]
VALID_BODY_FIRMWARE_PROVISION_LATEST: Literal["disable", "once"]
VALID_BODY_OVERRIDE_LED_STATE: Literal["enable", "disable"]
VALID_BODY_LED_STATE: Literal["enable", "disable"]
VALID_BODY_OVERRIDE_WAN_PORT_MODE: Literal["enable", "disable"]
VALID_BODY_WAN_PORT_MODE: Literal["wan-lan", "wan-only"]
VALID_BODY_OVERRIDE_IP_FRAGMENT: Literal["enable", "disable"]
VALID_BODY_IP_FRAGMENT_PREVENTING: Literal["tcp-mss-adjust", "icmp-unreachable"]
VALID_BODY_OVERRIDE_SPLIT_TUNNEL: Literal["enable", "disable"]
VALID_BODY_SPLIT_TUNNELING_ACL_PATH: Literal["tunnel", "local"]
VALID_BODY_SPLIT_TUNNELING_ACL_LOCAL_AP_SUBNET: Literal["enable", "disable"]
VALID_BODY_OVERRIDE_LAN: Literal["enable", "disable"]
VALID_BODY_OVERRIDE_ALLOWACCESS: Literal["enable", "disable"]
VALID_BODY_ALLOWACCESS: Literal["https", "ssh", "snmp"]
VALID_BODY_OVERRIDE_LOGIN_PASSWD_CHANGE: Literal["enable", "disable"]
VALID_BODY_LOGIN_PASSWD_CHANGE: Literal["yes", "default", "no"]
VALID_BODY_OVERRIDE_DEFAULT_MESH_ROOT: Literal["enable", "disable"]
VALID_BODY_DEFAULT_MESH_ROOT: Literal["enable", "disable"]
VALID_BODY_IMAGE_DOWNLOAD: Literal["enable", "disable"]
VALID_BODY_MESH_BRIDGE_ENABLE: Literal["default", "enable", "disable"]
VALID_BODY_PURDUE_LEVEL: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"]

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