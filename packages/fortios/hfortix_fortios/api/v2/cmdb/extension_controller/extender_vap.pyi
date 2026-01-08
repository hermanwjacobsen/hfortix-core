from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class ExtenderVapPayload(TypedDict, total=False):
    """
    Type hints for extension_controller/extender_vap payload fields.
    
    FortiExtender wifi vap configuration.
    
    **Usage:**
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
    rts_threshold: NotRequired[int]  # Wi-Fi RTS Threshold (256 - 2347), default = 2347
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

# Nested classes for table field children


# Response TypedDict for GET returns (all fields present in API response)
class ExtenderVapResponse(TypedDict):
    """
    Type hints for extension_controller/extender_vap API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str
    type: Literal["local-vap", "lan-ext-vap"]
    ssid: str
    max_clients: int
    broadcast_ssid: Literal["disable", "enable"]
    security: Literal["OPEN", "WPA2-Personal", "WPA-WPA2-Personal", "WPA3-SAE", "WPA3-SAE-Transition", "WPA2-Enterprise", "WPA3-Enterprise-only", "WPA3-Enterprise-transition", "WPA3-Enterprise-192-bit"]
    dtim: int
    rts_threshold: int
    pmf: Literal["disabled", "optional", "required"]
    target_wake_time: Literal["disable", "enable"]
    bss_color_partial: Literal["disable", "enable"]
    mu_mimo: Literal["disable", "enable"]
    passphrase: str
    sae_password: str
    auth_server_address: str
    auth_server_port: int
    auth_server_secret: str
    ip_address: str
    start_ip: str
    end_ip: str
    allowaccess: Literal["ping", "telnet", "http", "https", "ssh", "snmp"]


@final
class ExtenderVapObject:
    """Typed FortiObject for extension_controller/extender_vap with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Wi-Fi VAP name.
    name: str
    # Wi-Fi VAP type local-vap / lan-extension-vap.
    type: Literal["local-vap", "lan-ext-vap"]
    # Wi-Fi SSID.
    ssid: str
    # Wi-Fi max clients (0 - 512), default = 0 (no limit)
    max_clients: int
    # Wi-Fi broadcast SSID enable / disable.
    broadcast_ssid: Literal["disable", "enable"]
    # Wi-Fi security.
    security: Literal["OPEN", "WPA2-Personal", "WPA-WPA2-Personal", "WPA3-SAE", "WPA3-SAE-Transition", "WPA2-Enterprise", "WPA3-Enterprise-only", "WPA3-Enterprise-transition", "WPA3-Enterprise-192-bit"]
    # Wi-Fi DTIM (1 - 255) default = 1.
    dtim: int
    # Wi-Fi RTS Threshold (256 - 2347), default = 2347 (RTS/CTS disabled).
    rts_threshold: int
    # Wi-Fi pmf enable/disable, default = disable.
    pmf: Literal["disabled", "optional", "required"]
    # Wi-Fi 802.11AX target wake time enable / disable, default = enable.
    target_wake_time: Literal["disable", "enable"]
    # Wi-Fi 802.11AX bss color partial enable / disable, default = enable.
    bss_color_partial: Literal["disable", "enable"]
    # Wi-Fi multi-user MIMO enable / disable, default = enable.
    mu_mimo: Literal["disable", "enable"]
    # Wi-Fi passphrase.
    passphrase: str
    # Wi-Fi SAE Password.
    sae_password: str
    # Wi-Fi Authentication Server Address (IPv4 format).
    auth_server_address: str
    # Wi-Fi Authentication Server Port.
    auth_server_port: int
    # Wi-Fi Authentication Server Secret.
    auth_server_secret: str
    # Extender ip address.
    ip_address: str
    # Start ip address.
    start_ip: str
    # End ip address.
    end_ip: str
    # Control management access to the managed extender. Separate entries with a space
    allowaccess: Literal["ping", "telnet", "http", "https", "ssh", "snmp"]
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> ExtenderVapPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class ExtenderVap:
    """
    FortiExtender wifi vap configuration.
    
    Path: extension_controller/extender_vap
    Category: cmdb
    Primary Key: name
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey/name provided as positional arg)
    @overload
    def get(
        self,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ExtenderVapObject: ...
    
    # Single object (mkey/name provided as keyword arg)
    @overload
    def get(
        self,
        *,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ExtenderVapObject: ...
    
    # List of objects (no mkey/name provided) - keyword-only signature
    @overload
    def get(
        self,
        *,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> list[ExtenderVapObject]: ...
    
    @overload
    def get(
        self,
        name: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Dict mode with mkey provided as positional arg (single dict)
    @overload
    def get(
        self,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] = ...,
        **kwargs: Any,
    ) -> ExtenderVapResponse: ...
    
    # Dict mode with mkey provided as keyword arg (single dict)
    @overload
    def get(
        self,
        *,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] = ...,
        **kwargs: Any,
    ) -> ExtenderVapResponse: ...
    
    # Dict mode - list of dicts (no mkey/name provided) - keyword-only signature
    @overload
    def get(
        self,
        *,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] = ...,
        **kwargs: Any,
    ) -> list[ExtenderVapResponse]: ...
    
    # Default overload for dict mode
    @overload
    def get(
        self,
        name: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], list[dict[str, Any]]]: ...
    
    def get(
        self,
        name: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: str | None = ...,
        **kwargs: Any,
    ) -> ExtenderVapObject | list[ExtenderVapObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
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
        allowaccess: Literal["ping", "telnet", "http", "https", "ssh", "snmp"] | list[str] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ExtenderVapObject: ...
    
    @overload
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
        allowaccess: Literal["ping", "telnet", "http", "https", "ssh", "snmp"] | list[str] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
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
        allowaccess: Literal["ping", "telnet", "http", "https", "ssh", "snmp"] | list[str] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
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
        allowaccess: Literal["ping", "telnet", "http", "https", "ssh", "snmp"] | list[str] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
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
        allowaccess: Literal["ping", "telnet", "http", "https", "ssh", "snmp"] | list[str] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ExtenderVapObject: ...
    
    @overload
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
        allowaccess: Literal["ping", "telnet", "http", "https", "ssh", "snmp"] | list[str] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
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
        allowaccess: Literal["ping", "telnet", "http", "https", "ssh", "snmp"] | list[str] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
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
        allowaccess: Literal["ping", "telnet", "http", "https", "ssh", "snmp"] | list[str] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ExtenderVapObject: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
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
        allowaccess: Literal["ping", "telnet", "http", "https", "ssh", "snmp"] | list[str] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
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
    "ExtenderVapObject",
]