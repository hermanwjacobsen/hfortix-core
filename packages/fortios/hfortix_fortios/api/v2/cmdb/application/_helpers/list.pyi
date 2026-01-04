from typing import Any, Literal

# Enum type aliases for validation
VALID_BODY_EXTENDED_LOG: Literal["enable", "disable"]
VALID_BODY_OTHER_APPLICATION_ACTION: Literal["pass", "block"]
VALID_BODY_APP_REPLACEMSG: Literal["disable", "enable"]
VALID_BODY_OTHER_APPLICATION_LOG: Literal["disable", "enable"]
VALID_BODY_ENFORCE_DEFAULT_APP_PORT: Literal["disable", "enable"]
VALID_BODY_FORCE_INCLUSION_SSL_DI_SIGS: Literal["disable", "enable"]
VALID_BODY_UNKNOWN_APPLICATION_ACTION: Literal["pass", "block"]
VALID_BODY_UNKNOWN_APPLICATION_LOG: Literal["disable", "enable"]
VALID_BODY_P2P_BLOCK_LIST: Literal["skype", "edonkey", "bittorrent"]
VALID_BODY_DEEP_APP_INSPECTION: Literal["disable", "enable"]
VALID_BODY_OPTIONS: Literal["allow-dns", "allow-icmp", "allow-http", "allow-ssl"]
VALID_BODY_CONTROL_DEFAULT_NETWORK_SERVICES: Literal["disable", "enable"]

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