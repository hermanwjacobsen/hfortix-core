from typing import Any, Literal

# Enum type aliases for validation
VALID_BODY_HTTPS_IMAGE_PUSH: Literal["enable", "disable"]
VALID_BODY_VLAN_ALL_MODE: Literal["all", "defined"]
VALID_BODY_VLAN_OPTIMIZATION: Literal["prune", "configured", "none"]
VALID_BODY_VLAN_IDENTITY: Literal["description", "name"]
VALID_BODY_DHCP_SERVER_ACCESS_LIST: Literal["enable", "disable"]
VALID_BODY_DHCP_OPTION82_FORMAT: Literal["ascii", "legacy"]
VALID_BODY_DHCP_OPTION82_CIRCUIT_ID: Literal["intfname", "vlan", "hostname", "mode", "description"]
VALID_BODY_DHCP_OPTION82_REMOTE_ID: Literal["mac", "hostname", "ip"]
VALID_BODY_DHCP_SNOOP_CLIENT_REQ: Literal["drop-untrusted", "forward-untrusted"]
VALID_BODY_LOG_MAC_LIMIT_VIOLATIONS: Literal["enable", "disable"]
VALID_BODY_SN_DNS_RESOLUTION: Literal["enable", "disable"]
VALID_BODY_MAC_EVENT_LOGGING: Literal["enable", "disable"]
VALID_BODY_BOUNCE_QUARANTINED_LINK: Literal["disable", "enable"]
VALID_BODY_QUARANTINE_MODE: Literal["by-vlan", "by-redirect"]
VALID_BODY_UPDATE_USER_DEVICE: Literal["mac-cache", "lldp", "dhcp-snooping", "l2-db", "l3-db"]
VALID_BODY_FIPS_ENFORCE: Literal["disable", "enable"]
VALID_BODY_FIRMWARE_PROVISION_ON_AUTHORIZATION: Literal["enable", "disable"]
VALID_BODY_SWITCH_ON_DEAUTH: Literal["no-op", "factory-reset"]

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