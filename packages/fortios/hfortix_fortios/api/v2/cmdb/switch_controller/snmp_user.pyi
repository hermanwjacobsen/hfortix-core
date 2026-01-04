from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class SnmpUserPayload(TypedDict, total=False):
    """
    Type hints for switch_controller/snmp_user payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
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


class SnmpUser:
    """
    Configure FortiSwitch SNMP v3 users globally.
    
    Path: switch_controller/snmp_user
    Category: cmdb
    Primary Key: name
    """
    
    def get(
        self,
        name: str | None = ...,
        filter: str | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
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
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
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
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> Union[bool, Coroutine[Any, Any, bool]]: ...
    
    def set(
        self,
        payload_dict: SnmpUserPayload | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
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