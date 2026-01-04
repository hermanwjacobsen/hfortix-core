from typing import Any, Literal

# Enum type aliases for validation
VALID_BODY_PROXY: Literal["explicit-web", "transparent-web", "ftp", "ssh", "ssh-tunnel", "access-proxy", "ztna-proxy", "wanopt"]
VALID_BODY_ZTNA_TAGS_MATCH_LOGIC: Literal["or", "and"]
VALID_BODY_DEVICE_OWNERSHIP: Literal["enable", "disable"]
VALID_BODY_INTERNET_SERVICE: Literal["enable", "disable"]
VALID_BODY_INTERNET_SERVICE_NEGATE: Literal["enable", "disable"]
VALID_BODY_INTERNET_SERVICE6: Literal["enable", "disable"]
VALID_BODY_INTERNET_SERVICE6_NEGATE: Literal["enable", "disable"]
VALID_BODY_SRCADDR_NEGATE: Literal["enable", "disable"]
VALID_BODY_DSTADDR_NEGATE: Literal["enable", "disable"]
VALID_BODY_ZTNA_EMS_TAG_NEGATE: Literal["enable", "disable"]
VALID_BODY_SERVICE_NEGATE: Literal["enable", "disable"]
VALID_BODY_ACTION: Literal["accept", "deny", "redirect", "isolate"]
VALID_BODY_STATUS: Literal["enable", "disable"]
VALID_BODY_LOGTRAFFIC: Literal["all", "utm", "disable"]
VALID_BODY_HTTP_TUNNEL_AUTH: Literal["enable", "disable"]
VALID_BODY_SSH_POLICY_REDIRECT: Literal["enable", "disable"]
VALID_BODY_TRANSPARENT: Literal["enable", "disable"]
VALID_BODY_WEBCACHE: Literal["enable", "disable"]
VALID_BODY_WEBCACHE_HTTPS: Literal["disable", "enable"]
VALID_BODY_DISCLAIMER: Literal["disable", "domain", "policy", "user"]
VALID_BODY_UTM_STATUS: Literal["enable", "disable"]
VALID_BODY_PROFILE_TYPE: Literal["single", "group"]
VALID_BODY_LOGTRAFFIC_START: Literal["enable", "disable"]
VALID_BODY_LOG_HTTP_TRANSACTION: Literal["enable", "disable"]
VALID_BODY_BLOCK_NOTIFICATION: Literal["enable", "disable"]
VALID_BODY_HTTPS_SUB_CATEGORY: Literal["enable", "disable"]
VALID_BODY_DETECT_HTTPS_IN_HTTP_REQUEST: Literal["enable", "disable"]

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