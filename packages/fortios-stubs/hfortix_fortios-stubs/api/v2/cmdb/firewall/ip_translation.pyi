from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class IpTranslationPayload(TypedDict, total=False):
    """
    Type hints for firewall/ip_translation payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: IpTranslationPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    transid: NotRequired[int]  # IP translation ID.
    type: NotRequired[Literal[{"description": "SCTP", "help": "SCTP", "label": "Sctp", "name": "SCTP"}]]  # IP translation type (option: SCTP).
    startip: str  # First IPv4 address (inclusive) in the range of the addresses
    endip: str  # Final IPv4 address (inclusive) in the range of the addresses
    map_startip: str  # Address to be used as the starting point for translation in 


class IpTranslation:
    """
    Configure firewall IP-translation.
    
    Path: firewall/ip_translation
    Category: cmdb
    Primary Key: transid
    """
    
    def get(
        self,
        transid: int | None = ...,
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
        payload_dict: IpTranslationPayload | None = ...,
        transid: int | None = ...,
        type: Literal[{"description": "SCTP", "help": "SCTP", "label": "Sctp", "name": "SCTP"}] | None = ...,
        startip: str | None = ...,
        endip: str | None = ...,
        map_startip: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: IpTranslationPayload | None = ...,
        transid: int | None = ...,
        type: Literal[{"description": "SCTP", "help": "SCTP", "label": "Sctp", "name": "SCTP"}] | None = ...,
        startip: str | None = ...,
        endip: str | None = ...,
        map_startip: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def delete(
        self,
        transid: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def exists(
        self,
        transid: int,
        vdom: str | bool | None = ...,
    ) -> Union[bool, Coroutine[Any, Any, bool]]: ...
    
    def set(
        self,
        payload_dict: IpTranslationPayload | None = ...,
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
    "IpTranslation",
    "IpTranslationPayload",
]