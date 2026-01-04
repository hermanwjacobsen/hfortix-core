from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class L2tpPayload(TypedDict, total=False):
    """
    Type hints for vpn/l2tp payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: L2tpPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    status: Literal["enable", "disable"]  # Enable/disable FortiGate as a L2TP gateway.
    eip: str  # End IP.
    sip: str  # Start IP.
    usrgrp: str  # User group.
    enforce_ipsec: Literal["enable", "disable"]  # Enable/disable IPsec enforcement.
    lcp_echo_interval: NotRequired[int]  # Time in seconds between PPPoE Link Control Protocol (LCP) ec
    lcp_max_echo_fails: NotRequired[int]  # Maximum number of missed LCP echo messages before disconnect
    hello_interval: NotRequired[int]  # L2TP hello message interval in seconds (0 - 3600 sec, defaul
    compress: Literal["enable", "disable"]  # Enable/disable data compression.


class L2tp:
    """
    Configure L2TP.
    
    Path: vpn/l2tp
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
        payload_dict: L2tpPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        eip: str | None = ...,
        sip: str | None = ...,
        usrgrp: str | None = ...,
        enforce_ipsec: Literal["enable", "disable"] | None = ...,
        lcp_echo_interval: int | None = ...,
        lcp_max_echo_fails: int | None = ...,
        hello_interval: int | None = ...,
        compress: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: L2tpPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        eip: str | None = ...,
        sip: str | None = ...,
        usrgrp: str | None = ...,
        enforce_ipsec: Literal["enable", "disable"] | None = ...,
        lcp_echo_interval: int | None = ...,
        lcp_max_echo_fails: int | None = ...,
        hello_interval: int | None = ...,
        compress: Literal["enable", "disable"] | None = ...,
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
        payload_dict: L2tpPayload | None = ...,
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