from typing import Any, Literal

# Enum type aliases for validation
VALID_BODY_SCOPE: Literal["vdom", "global"]
VALID_BODY_SECFABGRP: Literal["none", "read", "read-write"]
VALID_BODY_FTVIEWGRP: Literal["none", "read", "read-write"]
VALID_BODY_AUTHGRP: Literal["none", "read", "read-write"]
VALID_BODY_SYSGRP: Literal["none", "read", "read-write", "custom"]
VALID_BODY_NETGRP: Literal["none", "read", "read-write", "custom"]
VALID_BODY_LOGGRP: Literal["none", "read", "read-write", "custom"]
VALID_BODY_FWGRP: Literal["none", "read", "read-write", "custom"]
VALID_BODY_VPNGRP: Literal["none", "read", "read-write"]
VALID_BODY_UTMGRP: Literal["none", "read", "read-write", "custom"]
VALID_BODY_WANOPTGRP: Literal["none", "read", "read-write"]
VALID_BODY_WIFI: Literal["none", "read", "read-write"]
VALID_BODY_ADMINTIMEOUT_OVERRIDE: Literal["enable", "disable"]
VALID_BODY_CLI_DIAGNOSE: Literal["enable", "disable"]
VALID_BODY_CLI_GET: Literal["enable", "disable"]
VALID_BODY_CLI_SHOW: Literal["enable", "disable"]
VALID_BODY_CLI_EXEC: Literal["enable", "disable"]
VALID_BODY_CLI_CONFIG: Literal["enable", "disable"]
VALID_BODY_SYSTEM_EXECUTE_SSH: Literal["enable", "disable"]
VALID_BODY_SYSTEM_EXECUTE_TELNET: Literal["enable", "disable"]

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