from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class TacacsPlusPayload(TypedDict, total=False):
    """
    Type hints for user/tacacs_plus payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: TacacsPlusPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # TACACS+ server entry name.
    server: str  # Primary TACACS+ server CN domain name or IP address.
    secondary_server: NotRequired[str]  # Secondary TACACS+ server CN domain name or IP address.
    tertiary_server: NotRequired[str]  # Tertiary TACACS+ server CN domain name or IP address.
    port: NotRequired[int]  # Port number of the TACACS+ server.
    key: NotRequired[str]  # Key to access the primary server.
    secondary_key: NotRequired[str]  # Key to access the secondary server.
    tertiary_key: NotRequired[str]  # Key to access the tertiary server.
    status_ttl: NotRequired[int]  # Time for which server reachability is cached so that when a 
    authen_type: NotRequired[Literal["mschap", "chap", "pap", "ascii", "auto"]]  # Allowed authentication protocols/methods.
    authorization: NotRequired[Literal["enable", "disable"]]  # Enable/disable TACACS+ authorization.
    source_ip: NotRequired[str]  # Source IP address for communications to TACACS+ server.
    interface_select_method: NotRequired[Literal["auto", "sdwan", "specify"]]  # Specify how to select outgoing interface to reach server.
    interface: str  # Specify outgoing interface to reach server.
    vrf_select: NotRequired[int]  # VRF ID used for connection to server.


class TacacsPlus:
    """
    Configure TACACS+ server entries.
    
    Path: user/tacacs_plus
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
        payload_dict: TacacsPlusPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        secondary_server: str | None = ...,
        tertiary_server: str | None = ...,
        port: int | None = ...,
        key: str | None = ...,
        secondary_key: str | None = ...,
        tertiary_key: str | None = ...,
        status_ttl: int | None = ...,
        authen_type: Literal["mschap", "chap", "pap", "ascii", "auto"] | None = ...,
        authorization: Literal["enable", "disable"] | None = ...,
        source_ip: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: TacacsPlusPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        secondary_server: str | None = ...,
        tertiary_server: str | None = ...,
        port: int | None = ...,
        key: str | None = ...,
        secondary_key: str | None = ...,
        tertiary_key: str | None = ...,
        status_ttl: int | None = ...,
        authen_type: Literal["mschap", "chap", "pap", "ascii", "auto"] | None = ...,
        authorization: Literal["enable", "disable"] | None = ...,
        source_ip: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
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
        payload_dict: TacacsPlusPayload | None = ...,
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