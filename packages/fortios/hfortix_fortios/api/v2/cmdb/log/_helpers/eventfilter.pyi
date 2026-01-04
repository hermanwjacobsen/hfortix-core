from typing import Any, Literal

# Enum type aliases for validation
VALID_BODY_EVENT: Literal["enable", "disable"]
VALID_BODY_SYSTEM: Literal["enable", "disable"]
VALID_BODY_VPN: Literal["enable", "disable"]
VALID_BODY_USER: Literal["enable", "disable"]
VALID_BODY_ROUTER: Literal["enable", "disable"]
VALID_BODY_WIRELESS_ACTIVITY: Literal["enable", "disable"]
VALID_BODY_WAN_OPT: Literal["enable", "disable"]
VALID_BODY_ENDPOINT: Literal["enable", "disable"]
VALID_BODY_HA: Literal["enable", "disable"]
VALID_BODY_SECURITY_RATING: Literal["enable", "disable"]
VALID_BODY_FORTIEXTENDER: Literal["enable", "disable"]
VALID_BODY_CONNECTOR: Literal["enable", "disable"]
VALID_BODY_SDWAN: Literal["enable", "disable"]
VALID_BODY_CIFS: Literal["enable", "disable"]
VALID_BODY_SWITCH_CONTROLLER: Literal["enable", "disable"]
VALID_BODY_REST_API: Literal["enable", "disable"]
VALID_BODY_WEBPROXY: Literal["enable", "disable"]

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