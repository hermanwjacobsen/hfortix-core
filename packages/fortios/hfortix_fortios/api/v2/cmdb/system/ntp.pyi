from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class NtpPayload(TypedDict, total=False):
    """
    Type hints for system/ntp payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: NtpPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    ntpsync: NotRequired[Literal["enable", "disable"]]  # Enable/disable setting the FortiGate system time by synchron
    type: NotRequired[Literal["fortiguard", "custom"]]  # Use the FortiGuard NTP server or any other available NTP Ser
    syncinterval: NotRequired[int]  # NTP synchronization interval (1 - 1440 min).
    ntpserver: NotRequired[list[dict[str, Any]]]  # Configure the FortiGate to connect to any available third-pa
    source_ip: NotRequired[str]  # Source IP address for communication to the NTP server.
    source_ip6: NotRequired[str]  # Source IPv6 address for communication to the NTP server.
    server_mode: NotRequired[Literal["enable", "disable"]]  # Enable/disable FortiGate NTP Server Mode. Your FortiGate bec
    authentication: NotRequired[Literal["enable", "disable"]]  # Enable/disable authentication.
    key_type: NotRequired[Literal["MD5", "SHA1", "SHA256"]]  # Key type for authentication (MD5, SHA1, SHA256).
    key: str  # Key for authentication.
    key_id: int  # Key ID for authentication.
    interface: NotRequired[list[dict[str, Any]]]  # FortiGate interface(s) with NTP server mode enabled. Devices


class Ntp:
    """
    Configure system NTP information.
    
    Path: system/ntp
    Category: cmdb
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
        payload_dict: NtpPayload | None = ...,
        ntpsync: Literal["enable", "disable"] | None = ...,
        type: Literal["fortiguard", "custom"] | None = ...,
        syncinterval: int | None = ...,
        ntpserver: list[dict[str, Any]] | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        server_mode: Literal["enable", "disable"] | None = ...,
        authentication: Literal["enable", "disable"] | None = ...,
        key_type: Literal["MD5", "SHA1", "SHA256"] | None = ...,
        key: str | None = ...,
        key_id: int | None = ...,
        interface: list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: NtpPayload | None = ...,
        ntpsync: Literal["enable", "disable"] | None = ...,
        type: Literal["fortiguard", "custom"] | None = ...,
        syncinterval: int | None = ...,
        ntpserver: list[dict[str, Any]] | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        server_mode: Literal["enable", "disable"] | None = ...,
        authentication: Literal["enable", "disable"] | None = ...,
        key_type: Literal["MD5", "SHA1", "SHA256"] | None = ...,
        key: str | None = ...,
        key_id: int | None = ...,
        interface: list[dict[str, Any]] | None = ...,
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
        payload_dict: NtpPayload | None = ...,
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