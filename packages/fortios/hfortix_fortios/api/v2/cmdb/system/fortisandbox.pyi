from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class FortisandboxPayload(TypedDict, total=False):
    """
    Type hints for system/fortisandbox payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: FortisandboxPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    status: NotRequired[Literal["enable", "disable"]]  # Enable/disable FortiSandbox.
    forticloud: NotRequired[Literal["enable", "disable"]]  # Enable/disable FortiSandbox Cloud.
    inline_scan: NotRequired[Literal["enable", "disable"]]  # Enable/disable FortiSandbox inline scan.
    server: str  # Server IP address or FQDN of the remote FortiSandbox.
    source_ip: NotRequired[str]  # Source IP address for communications to FortiSandbox.
    interface_select_method: NotRequired[Literal["auto", "sdwan", "specify"]]  # Specify how to select outgoing interface to reach server.
    interface: str  # Specify outgoing interface to reach server.
    vrf_select: NotRequired[int]  # VRF ID used for connection to server.
    enc_algorithm: NotRequired[Literal["default", "high", "low"]]  # Configure the level of SSL protection for secure communicati
    ssl_min_proto_version: NotRequired[Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"]]  # Minimum supported protocol version for SSL/TLS connections (
    email: NotRequired[str]  # Notifier email address.
    ca: NotRequired[str]  # The CA that signs remote FortiSandbox certificate, empty for
    cn: NotRequired[str]  # The CN of remote server certificate, case sensitive, empty f
    certificate_verification: NotRequired[Literal["enable", "disable"]]  # Enable/disable identity verification of FortiSandbox by use 


class Fortisandbox:
    """
    Configure FortiSandbox.
    
    Path: system/fortisandbox
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
        payload_dict: FortisandboxPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        forticloud: Literal["enable", "disable"] | None = ...,
        inline_scan: Literal["enable", "disable"] | None = ...,
        server: str | None = ...,
        source_ip: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        enc_algorithm: Literal["default", "high", "low"] | None = ...,
        ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        email: str | None = ...,
        ca: str | None = ...,
        cn: str | None = ...,
        certificate_verification: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: FortisandboxPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        forticloud: Literal["enable", "disable"] | None = ...,
        inline_scan: Literal["enable", "disable"] | None = ...,
        server: str | None = ...,
        source_ip: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        enc_algorithm: Literal["default", "high", "low"] | None = ...,
        ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        email: str | None = ...,
        ca: str | None = ...,
        cn: str | None = ...,
        certificate_verification: Literal["enable", "disable"] | None = ...,
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
        payload_dict: FortisandboxPayload | None = ...,
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