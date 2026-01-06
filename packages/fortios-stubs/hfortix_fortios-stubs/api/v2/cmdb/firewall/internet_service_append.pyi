from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class InternetServiceAppendPayload(TypedDict, total=False):
    """
    Type hints for firewall/internet_service_append payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: InternetServiceAppendPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    addr_mode: NotRequired[Literal[{"description": "IPv4 mode", "help": "IPv4 mode.", "label": "Ipv4", "name": "ipv4"}, {"description": "IPv6 mode", "help": "IPv6 mode.", "label": "Ipv6", "name": "ipv6"}, {"description": "Both IPv4 and IPv6 mode", "help": "Both IPv4 and IPv6 mode.", "label": "Both", "name": "both"}]]  # Address mode (IPv4 or IPv6).
    match_port: NotRequired[int]  # Matching TCP/UDP/SCTP destination port (0 to 65535, 0 means 
    append_port: NotRequired[int]  # Appending TCP/UDP/SCTP destination port (1 to 65535).


class InternetServiceAppend:
    """
    Configure additional port mappings for Internet Services.
    
    Path: firewall/internet_service_append
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
        payload_dict: InternetServiceAppendPayload | None = ...,
        addr_mode: Literal[{"description": "IPv4 mode", "help": "IPv4 mode.", "label": "Ipv4", "name": "ipv4"}, {"description": "IPv6 mode", "help": "IPv6 mode.", "label": "Ipv6", "name": "ipv6"}, {"description": "Both IPv4 and IPv6 mode", "help": "Both IPv4 and IPv6 mode.", "label": "Both", "name": "both"}] | None = ...,
        match_port: int | None = ...,
        append_port: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: InternetServiceAppendPayload | None = ...,
        addr_mode: Literal[{"description": "IPv4 mode", "help": "IPv4 mode.", "label": "Ipv4", "name": "ipv4"}, {"description": "IPv6 mode", "help": "IPv6 mode.", "label": "Ipv6", "name": "ipv6"}, {"description": "Both IPv4 and IPv6 mode", "help": "Both IPv4 and IPv6 mode.", "label": "Both", "name": "both"}] | None = ...,
        match_port: int | None = ...,
        append_port: int | None = ...,
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
        payload_dict: InternetServiceAppendPayload | None = ...,
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


__all__ = [
    "InternetServiceAppend",
    "InternetServiceAppendPayload",
]