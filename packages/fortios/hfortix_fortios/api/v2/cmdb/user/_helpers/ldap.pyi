from typing import Any, Literal

# Enum type aliases for validation
VALID_BODY_SERVER_IDENTITY_CHECK: Literal["enable", "disable"]
VALID_BODY_TYPE: Literal["simple", "anonymous", "regular"]
VALID_BODY_TWO_FACTOR: Literal["disable", "fortitoken-cloud"]
VALID_BODY_TWO_FACTOR_AUTHENTICATION: Literal["fortitoken", "email", "sms"]
VALID_BODY_TWO_FACTOR_NOTIFICATION: Literal["email", "sms"]
VALID_BODY_GROUP_MEMBER_CHECK: Literal["user-attr", "group-object", "posix-group-object"]
VALID_BODY_SECURE: Literal["disable", "starttls", "ldaps"]
VALID_BODY_SSL_MIN_PROTO_VERSION: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"]
VALID_BODY_PASSWORD_EXPIRY_WARNING: Literal["enable", "disable"]
VALID_BODY_PASSWORD_RENEWAL: Literal["enable", "disable"]
VALID_BODY_ACCOUNT_KEY_PROCESSING: Literal["same", "strip"]
VALID_BODY_ACCOUNT_KEY_CERT_FIELD: Literal["othername", "rfc822name", "dnsname", "cn"]
VALID_BODY_SEARCH_TYPE: Literal["recursive"]
VALID_BODY_CLIENT_CERT_AUTH: Literal["enable", "disable"]
VALID_BODY_OBTAIN_USER_INFO: Literal["enable", "disable"]
VALID_BODY_INTERFACE_SELECT_METHOD: Literal["auto", "sdwan", "specify"]
VALID_BODY_ANTIPHISH: Literal["enable", "disable"]

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