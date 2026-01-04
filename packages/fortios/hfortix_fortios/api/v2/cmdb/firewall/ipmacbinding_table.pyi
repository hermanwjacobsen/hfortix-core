from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class IpmacbindingTablePayload(TypedDict, total=False):
    """
    Type hints for firewall/ipmacbinding_table payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: IpmacbindingTablePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    seq_num: NotRequired[int]  # Entry number.
    ip: str  # IPv4 address portion of the pair (format: xxx.xxx.xxx.xxx).
    mac: NotRequired[str]  # MAC address portion of the pair (format = xx:xx:xx:xx:xx:xx 
    name: NotRequired[str]  # Name of the pair (optional, default = no name).
    status: NotRequired[Literal["enable", "disable"]]  # Enable/disable this IP-mac binding pair.


class IpmacbindingTable:
    """
    Configure IP to MAC address pairs in the IP/MAC binding table.
    
    Path: firewall/ipmacbinding_table
    Category: cmdb
    Primary Key: seq-num
    """
    
    def get(
        self,
        seq_num: int | None = ...,
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
        payload_dict: IpmacbindingTablePayload | None = ...,
        seq_num: int | None = ...,
        ip: str | None = ...,
        mac: str | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: IpmacbindingTablePayload | None = ...,
        seq_num: int | None = ...,
        ip: str | None = ...,
        mac: str | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def delete(
        self,
        seq_num: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def exists(
        self,
        seq_num: int,
        vdom: str | bool | None = ...,
    ) -> Union[bool, Coroutine[Any, Any, bool]]: ...
    
    def set(
        self,
        payload_dict: IpmacbindingTablePayload | None = ...,
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