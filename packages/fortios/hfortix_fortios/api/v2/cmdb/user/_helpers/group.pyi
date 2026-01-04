from typing import Any, Literal

# Enum type aliases for validation
VALID_BODY_GROUP_TYPE: Literal["firewall", "fsso-service", "rsso", "guest"]
VALID_BODY_AUTH_CONCURRENT_OVERRIDE: Literal["enable", "disable"]
VALID_BODY_USER_ID: Literal["email", "auto-generate", "specify"]
VALID_BODY_PASSWORD: Literal["auto-generate", "specify", "disable"]
VALID_BODY_USER_NAME: Literal["disable", "enable"]
VALID_BODY_SPONSOR: Literal["optional", "mandatory", "disabled"]
VALID_BODY_COMPANY: Literal["optional", "mandatory", "disabled"]
VALID_BODY_EMAIL: Literal["disable", "enable"]
VALID_BODY_MOBILE_PHONE: Literal["disable", "enable"]
VALID_BODY_SMS_SERVER: Literal["fortiguard", "custom"]
VALID_BODY_EXPIRE_TYPE: Literal["immediately", "first-successful-login"]
VALID_BODY_MULTIPLE_GUEST_ADD: Literal["disable", "enable"]

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