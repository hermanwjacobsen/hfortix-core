from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class PptpPayload(TypedDict, total=False):
    """
    Type hints for vpn/pptp payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: PptpPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    status: Literal[{"description": "Enable setting", "help": "Enable setting.", "label": "Enable", "name": "enable"}, {"description": "Disable setting", "help": "Disable setting.", "label": "Disable", "name": "disable"}]  # Enable/disable FortiGate as a PPTP gateway.
    ip_mode: Literal[{"description": "PPTP client IP from manual config (range from sip to eip)", "help": "PPTP client IP from manual config (range from sip to eip).", "label": "Range", "name": "range"}, {"description": "PPTP client IP from user-group defined server", "help": "PPTP client IP from user-group defined server.", "label": "Usrgrp", "name": "usrgrp"}]  # IP assignment mode for PPTP client.
    eip: str  # End IP.
    sip: str  # Start IP.
    local_ip: str  # Local IP to be used for peer's remote IP.
    usrgrp: str  # User group.


class Pptp:
    """
    Configure PPTP.
    
    Path: vpn/pptp
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
        payload_dict: PptpPayload | None = ...,
        status: Literal[{"description": "Enable setting", "help": "Enable setting.", "label": "Enable", "name": "enable"}, {"description": "Disable setting", "help": "Disable setting.", "label": "Disable", "name": "disable"}] | None = ...,
        ip_mode: Literal[{"description": "PPTP client IP from manual config (range from sip to eip)", "help": "PPTP client IP from manual config (range from sip to eip).", "label": "Range", "name": "range"}, {"description": "PPTP client IP from user-group defined server", "help": "PPTP client IP from user-group defined server.", "label": "Usrgrp", "name": "usrgrp"}] | None = ...,
        eip: str | None = ...,
        sip: str | None = ...,
        local_ip: str | None = ...,
        usrgrp: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: PptpPayload | None = ...,
        status: Literal[{"description": "Enable setting", "help": "Enable setting.", "label": "Enable", "name": "enable"}, {"description": "Disable setting", "help": "Disable setting.", "label": "Disable", "name": "disable"}] | None = ...,
        ip_mode: Literal[{"description": "PPTP client IP from manual config (range from sip to eip)", "help": "PPTP client IP from manual config (range from sip to eip).", "label": "Range", "name": "range"}, {"description": "PPTP client IP from user-group defined server", "help": "PPTP client IP from user-group defined server.", "label": "Usrgrp", "name": "usrgrp"}] | None = ...,
        eip: str | None = ...,
        sip: str | None = ...,
        local_ip: str | None = ...,
        usrgrp: str | None = ...,
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
        payload_dict: PptpPayload | None = ...,
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
    "Pptp",
    "PptpPayload",
]