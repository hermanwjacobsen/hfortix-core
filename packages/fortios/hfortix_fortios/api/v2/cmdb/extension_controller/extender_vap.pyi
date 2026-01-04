from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class ExtenderVapPayload(TypedDict, total=False):
    """
    Type hints for extension_controller/extender_vap payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: ExtenderVapPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Wi-Fi VAP name.
    type: Literal["local-vap", "lan-ext-vap"]  # Wi-Fi VAP type local-vap / lan-extension-vap.
    ssid: str  # Wi-Fi SSID.
    max_clients: NotRequired[int]  # Wi-Fi max clients (0 - 512), default = 0 (no limit) 
    broadcast_ssid: NotRequired[Literal["disable", "enable"]]  # Wi-Fi broadcast SSID enable / disable.
    security: Literal["OPEN", "WPA2-Personal", "WPA-WPA2-Personal", "WPA3-SAE", "WPA3-SAE-Transition", "WPA2-Enterprise", "WPA3-Enterprise-only", "WPA3-Enterprise-transition", "WPA3-Enterprise-192-bit"]  # Wi-Fi security.
    dtim: NotRequired[int]  # Wi-Fi DTIM (1 - 255) default = 1.
    rts_threshold: NotRequired[int]  # Wi-Fi RTS Threshold (256 - 2347), default = 2347 (RTS/CTS di
    pmf: NotRequired[Literal["disabled", "optional", "required"]]  # Wi-Fi pmf enable/disable, default = disable.
    target_wake_time: NotRequired[Literal["disable", "enable"]]  # Wi-Fi 802.11AX target wake time enable / disable, default = 
    bss_color_partial: NotRequired[Literal["disable", "enable"]]  # Wi-Fi 802.11AX bss color partial enable / disable, default =
    mu_mimo: NotRequired[Literal["disable", "enable"]]  # Wi-Fi multi-user MIMO enable / disable, default = enable.
    passphrase: str  # Wi-Fi passphrase.
    sae_password: str  # Wi-Fi SAE Password.
    auth_server_address: str  # Wi-Fi Authentication Server Address (IPv4 format).
    auth_server_port: int  # Wi-Fi Authentication Server Port.
    auth_server_secret: str  # Wi-Fi Authentication Server Secret.
    ip_address: NotRequired[str]  # Extender ip address.
    start_ip: NotRequired[str]  # Start ip address.
    end_ip: NotRequired[str]  # End ip address.
    allowaccess: NotRequired[Literal["ping", "telnet", "http", "https", "ssh", "snmp"]]  # Control management access to the managed extender. Separate 


class ExtenderVap:
    """
    FortiExtender wifi vap configuration.
    
    Path: extension_controller/extender_vap
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
        payload_dict: ExtenderVapPayload | None = ...,
        name: str | None = ...,
        type: Literal["local-vap", "lan-ext-vap"] | None = ...,
        ssid: str | None = ...,
        max_clients: int | None = ...,
        broadcast_ssid: Literal["disable", "enable"] | None = ...,
        security: Literal["OPEN", "WPA2-Personal", "WPA-WPA2-Personal", "WPA3-SAE", "WPA3-SAE-Transition", "WPA2-Enterprise", "WPA3-Enterprise-only", "WPA3-Enterprise-transition", "WPA3-Enterprise-192-bit"] | None = ...,
        dtim: int | None = ...,
        rts_threshold: int | None = ...,
        pmf: Literal["disabled", "optional", "required"] | None = ...,
        target_wake_time: Literal["disable", "enable"] | None = ...,
        bss_color_partial: Literal["disable", "enable"] | None = ...,
        mu_mimo: Literal["disable", "enable"] | None = ...,
        passphrase: str | None = ...,
        sae_password: str | None = ...,
        auth_server_address: str | None = ...,
        auth_server_port: int | None = ...,
        auth_server_secret: str | None = ...,
        ip_address: str | None = ...,
        start_ip: str | None = ...,
        end_ip: str | None = ...,
        allowaccess: Literal["ping", "telnet", "http", "https", "ssh", "snmp"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: ExtenderVapPayload | None = ...,
        name: str | None = ...,
        type: Literal["local-vap", "lan-ext-vap"] | None = ...,
        ssid: str | None = ...,
        max_clients: int | None = ...,
        broadcast_ssid: Literal["disable", "enable"] | None = ...,
        security: Literal["OPEN", "WPA2-Personal", "WPA-WPA2-Personal", "WPA3-SAE", "WPA3-SAE-Transition", "WPA2-Enterprise", "WPA3-Enterprise-only", "WPA3-Enterprise-transition", "WPA3-Enterprise-192-bit"] | None = ...,
        dtim: int | None = ...,
        rts_threshold: int | None = ...,
        pmf: Literal["disabled", "optional", "required"] | None = ...,
        target_wake_time: Literal["disable", "enable"] | None = ...,
        bss_color_partial: Literal["disable", "enable"] | None = ...,
        mu_mimo: Literal["disable", "enable"] | None = ...,
        passphrase: str | None = ...,
        sae_password: str | None = ...,
        auth_server_address: str | None = ...,
        auth_server_port: int | None = ...,
        auth_server_secret: str | None = ...,
        ip_address: str | None = ...,
        start_ip: str | None = ...,
        end_ip: str | None = ...,
        allowaccess: Literal["ping", "telnet", "http", "https", "ssh", "snmp"] | None = ...,
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
        payload_dict: ExtenderVapPayload | None = ...,
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
    "ExtenderVap",
    "ExtenderVapPayload",
]