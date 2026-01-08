from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class SnmpUserPayload(TypedDict, total=False):
    """
    Type hints for switch_controller/snmp_user payload fields.
    
    Configure FortiSwitch SNMP v3 users globally.
    
    **Usage:**
        payload: SnmpUserPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # SNMP user name.
    queries: NotRequired[Literal["disable", "enable"]]  # Enable/disable SNMP queries for this user.
    query_port: NotRequired[int]  # SNMPv3 query port (default = 161).
    security_level: NotRequired[Literal["no-auth-no-priv", "auth-no-priv", "auth-priv"]]  # Security level for message authentication and encryption.
    auth_proto: NotRequired[Literal["md5", "sha1", "sha224", "sha256", "sha384", "sha512"]]  # Authentication protocol.
    auth_pwd: str  # Password for authentication protocol.
    priv_proto: NotRequired[Literal["aes128", "aes192", "aes192c", "aes256", "aes256c", "des"]]  # Privacy (encryption) protocol.
    priv_pwd: str  # Password for privacy (encryption) protocol.


class SnmpUserObject(FortiObject[SnmpUserPayload]):
    """Typed FortiObject for switch_controller/snmp_user with IDE autocomplete support."""
    
    # SNMP user name.
    name: str
    # Enable/disable SNMP queries for this user.
    queries: Literal["disable", "enable"]
    # SNMPv3 query port (default = 161).
    query_port: int
    # Security level for message authentication and encryption.
    security_level: Literal["no-auth-no-priv", "auth-no-priv", "auth-priv"]
    # Authentication protocol.
    auth_proto: Literal["md5", "sha1", "sha224", "sha256", "sha384", "sha512"]
    # Password for authentication protocol.
    auth_pwd: str
    # Privacy (encryption) protocol.
    priv_proto: Literal["aes128", "aes192", "aes192c", "aes256", "aes256c", "des"]
    # Password for privacy (encryption) protocol.
    priv_pwd: str
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> SnmpUserPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class SnmpUser:
    """
    Configure FortiSwitch SNMP v3 users globally.
    
    Path: switch_controller/snmp_user
    Category: cmdb
    Primary Key: name
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey provided)
    @overload
    def get(
        self,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        *,
        response_mode: Literal["object"],
        **kwargs: Any,
    ) -> SnmpUserObject: ...
    
    # List of objects (no mkey provided - most specific for list returns)
    # For singleton endpoints (no mkey), returns single object; for table endpoints, returns list
    @overload
    def get(
        self,
        *,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"],
        **kwargs: Any,
    ) -> list[SnmpUserObject]: ...
    
    @overload
    def get(
        self,
        name: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True],
        *,
        response_mode: Literal["object"],
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Dict mode with mkey provided (single dict)
    @overload
    def get(
        self,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Dict mode without mkey (returns dict with results array)
    @overload
    def get(
        self,
        name: None = None,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Default overload for dict mode
    @overload
    def get(
        self,
        name: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], list[dict[str, Any]]]: ...
    
    def get(
        self,
        name: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: str | None = ...,
        **kwargs: Any,
    ) -> SnmpUserObject | list[SnmpUserObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: SnmpUserPayload | None = ...,
        name: str | None = ...,
        queries: Literal["disable", "enable"] | None = ...,
        query_port: int | None = ...,
        security_level: Literal["no-auth-no-priv", "auth-no-priv", "auth-priv"] | None = ...,
        auth_proto: Literal["md5", "sha1", "sha224", "sha256", "sha384", "sha512"] | None = ...,
        auth_pwd: str | None = ...,
        priv_proto: Literal["aes128", "aes192", "aes192c", "aes256", "aes256c", "des"] | None = ...,
        priv_pwd: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> SnmpUserObject: ...
    
    @overload
    def post(
        self,
        payload_dict: SnmpUserPayload | None = ...,
        name: str | None = ...,
        queries: Literal["disable", "enable"] | None = ...,
        query_port: int | None = ...,
        security_level: Literal["no-auth-no-priv", "auth-no-priv", "auth-priv"] | None = ...,
        auth_proto: Literal["md5", "sha1", "sha224", "sha256", "sha384", "sha512"] | None = ...,
        auth_pwd: str | None = ...,
        priv_proto: Literal["aes128", "aes192", "aes192c", "aes256", "aes256c", "des"] | None = ...,
        priv_pwd: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: SnmpUserPayload | None = ...,
        name: str | None = ...,
        queries: Literal["disable", "enable"] | None = ...,
        query_port: int | None = ...,
        security_level: Literal["no-auth-no-priv", "auth-no-priv", "auth-priv"] | None = ...,
        auth_proto: Literal["md5", "sha1", "sha224", "sha256", "sha384", "sha512"] | None = ...,
        auth_pwd: str | None = ...,
        priv_proto: Literal["aes128", "aes192", "aes192c", "aes256", "aes256c", "des"] | None = ...,
        priv_pwd: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: SnmpUserPayload | None = ...,
        name: str | None = ...,
        queries: Literal["disable", "enable"] | None = ...,
        query_port: int | None = ...,
        security_level: Literal["no-auth-no-priv", "auth-no-priv", "auth-priv"] | None = ...,
        auth_proto: Literal["md5", "sha1", "sha224", "sha256", "sha384", "sha512"] | None = ...,
        auth_pwd: str | None = ...,
        priv_proto: Literal["aes128", "aes192", "aes192c", "aes256", "aes256c", "des"] | None = ...,
        priv_pwd: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: SnmpUserPayload | None = ...,
        name: str | None = ...,
        queries: Literal["disable", "enable"] | None = ...,
        query_port: int | None = ...,
        security_level: Literal["no-auth-no-priv", "auth-no-priv", "auth-priv"] | None = ...,
        auth_proto: Literal["md5", "sha1", "sha224", "sha256", "sha384", "sha512"] | None = ...,
        auth_pwd: str | None = ...,
        priv_proto: Literal["aes128", "aes192", "aes192c", "aes256", "aes256c", "des"] | None = ...,
        priv_pwd: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> SnmpUserObject: ...
    
    @overload
    def put(
        self,
        payload_dict: SnmpUserPayload | None = ...,
        name: str | None = ...,
        queries: Literal["disable", "enable"] | None = ...,
        query_port: int | None = ...,
        security_level: Literal["no-auth-no-priv", "auth-no-priv", "auth-priv"] | None = ...,
        auth_proto: Literal["md5", "sha1", "sha224", "sha256", "sha384", "sha512"] | None = ...,
        auth_pwd: str | None = ...,
        priv_proto: Literal["aes128", "aes192", "aes192c", "aes256", "aes256c", "des"] | None = ...,
        priv_pwd: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: SnmpUserPayload | None = ...,
        name: str | None = ...,
        queries: Literal["disable", "enable"] | None = ...,
        query_port: int | None = ...,
        security_level: Literal["no-auth-no-priv", "auth-no-priv", "auth-priv"] | None = ...,
        auth_proto: Literal["md5", "sha1", "sha224", "sha256", "sha384", "sha512"] | None = ...,
        auth_pwd: str | None = ...,
        priv_proto: Literal["aes128", "aes192", "aes192c", "aes256", "aes256c", "des"] | None = ...,
        priv_pwd: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: SnmpUserPayload | None = ...,
        name: str | None = ...,
        queries: Literal["disable", "enable"] | None = ...,
        query_port: int | None = ...,
        security_level: Literal["no-auth-no-priv", "auth-no-priv", "auth-priv"] | None = ...,
        auth_proto: Literal["md5", "sha1", "sha224", "sha256", "sha384", "sha512"] | None = ...,
        auth_pwd: str | None = ...,
        priv_proto: Literal["aes128", "aes192", "aes192c", "aes256", "aes256c", "des"] | None = ...,
        priv_pwd: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> SnmpUserObject: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: SnmpUserPayload | None = ...,
        name: str | None = ...,
        queries: Literal["disable", "enable"] | None = ...,
        query_port: int | None = ...,
        security_level: Literal["no-auth-no-priv", "auth-no-priv", "auth-priv"] | None = ...,
        auth_proto: Literal["md5", "sha1", "sha224", "sha256", "sha384", "sha512"] | None = ...,
        auth_pwd: str | None = ...,
        priv_proto: Literal["aes128", "aes192", "aes192c", "aes256", "aes256c", "des"] | None = ...,
        priv_pwd: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Helper methods
    @staticmethod
    def help(field_name: str | None = ...) -> str: ...
    
    @staticmethod
    def fields(detailed: bool = ...) -> Union[list[str], list[dict[str, Any]]]: ...
    
    @staticmethod
    def field_info(field_name: str) -> dict[str, Any]: ...
    
    @staticmethod
    def validate_field(name: str, value: Any) -> bool: ...
    
    @staticmethod
    def required_fields() -> list[str]: ...
    
    @staticmethod
    def defaults() -> dict[str, Any]: ...
    
    @staticmethod
    def schema() -> dict[str, Any]: ...


__all__ = [
    "SnmpUser",
    "SnmpUserPayload",
    "SnmpUserObject",
]