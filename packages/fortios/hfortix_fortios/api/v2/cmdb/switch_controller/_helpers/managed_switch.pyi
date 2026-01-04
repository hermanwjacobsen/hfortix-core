from typing import Any, Literal

# Enum type aliases for validation
VALID_BODY_PURDUE_LEVEL: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"]
VALID_BODY_FSW_WAN1_ADMIN: Literal["discovered", "disable", "enable"]
VALID_BODY_POE_PRE_STANDARD_DETECTION: Literal["enable", "disable"]
VALID_BODY_DHCP_SERVER_ACCESS_LIST: Literal["global", "enable", "disable"]
VALID_BODY_MCLAG_IGMP_SNOOPING_AWARE: Literal["enable", "disable"]
VALID_BODY_PTP_STATUS: Literal["disable", "enable"]
VALID_BODY_RADIUS_NAS_IP_OVERRIDE: Literal["disable", "enable"]
VALID_BODY_ROUTE_OFFLOAD: Literal["disable", "enable"]
VALID_BODY_ROUTE_OFFLOAD_MCLAG: Literal["disable", "enable"]
VALID_BODY_TYPE: Literal["virtual", "physical"]
VALID_BODY_FIRMWARE_PROVISION: Literal["enable", "disable"]
VALID_BODY_FIRMWARE_PROVISION_LATEST: Literal["disable", "once"]
VALID_BODY_OVERRIDE_SNMP_SYSINFO: Literal["disable", "enable"]
VALID_BODY_OVERRIDE_SNMP_TRAP_THRESHOLD: Literal["enable", "disable"]
VALID_BODY_OVERRIDE_SNMP_COMMUNITY: Literal["enable", "disable"]
VALID_BODY_OVERRIDE_SNMP_USER: Literal["enable", "disable"]
VALID_BODY_QOS_DROP_POLICY: Literal["taildrop", "random-early-detection"]

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