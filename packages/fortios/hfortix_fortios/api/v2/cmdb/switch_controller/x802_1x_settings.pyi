from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class X8021xSettingsPayload(TypedDict, total=False):
    """
    Type hints for switch_controller/x802_1x_settings payload fields.
    
    Configure global 802.1X settings.
    
    **Usage:**
        payload: X8021xSettingsPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    link_down_auth: NotRequired[Literal["set-unauth", "no-action"]]  # Interface-reauthentication state to set if a link is down.
    reauth_period: NotRequired[int]  # Period of time to allow for reauthentication
    max_reauth_attempt: NotRequired[int]  # Maximum number of authentication attempts
    tx_period: NotRequired[int]  # 802.1X Tx period (seconds, default=30).
    mab_reauth: NotRequired[Literal["disable", "enable"]]  # Enable/disable MAB re-authentication.
    mac_username_delimiter: NotRequired[Literal["colon", "hyphen", "none", "single-hyphen"]]  # MAC authentication username delimiter (default = hyphen).
    mac_password_delimiter: NotRequired[Literal["colon", "hyphen", "none", "single-hyphen"]]  # MAC authentication password delimiter (default = hyphen).
    mac_calling_station_delimiter: NotRequired[Literal["colon", "hyphen", "none", "single-hyphen"]]  # MAC calling station delimiter (default = hyphen).
    mac_called_station_delimiter: NotRequired[Literal["colon", "hyphen", "none", "single-hyphen"]]  # MAC called station delimiter (default = hyphen).
    mac_case: NotRequired[Literal["lowercase", "uppercase"]]  # MAC case (default = lowercase).

# Nested classes for table field children


# Response TypedDict for GET returns (all fields present in API response)
class X8021xSettingsResponse(TypedDict):
    """
    Type hints for switch_controller/x802_1x_settings API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    link_down_auth: Literal["set-unauth", "no-action"]
    reauth_period: int
    max_reauth_attempt: int
    tx_period: int
    mab_reauth: Literal["disable", "enable"]
    mac_username_delimiter: Literal["colon", "hyphen", "none", "single-hyphen"]
    mac_password_delimiter: Literal["colon", "hyphen", "none", "single-hyphen"]
    mac_calling_station_delimiter: Literal["colon", "hyphen", "none", "single-hyphen"]
    mac_called_station_delimiter: Literal["colon", "hyphen", "none", "single-hyphen"]
    mac_case: Literal["lowercase", "uppercase"]


@final
class X8021xSettingsObject:
    """Typed FortiObject for switch_controller/x802_1x_settings with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Interface-reauthentication state to set if a link is down.
    link_down_auth: Literal["set-unauth", "no-action"]
    # Period of time to allow for reauthentication
    reauth_period: int
    # Maximum number of authentication attempts (0 - 15, default = 3).
    max_reauth_attempt: int
    # 802.1X Tx period (seconds, default=30).
    tx_period: int
    # Enable/disable MAB re-authentication.
    mab_reauth: Literal["disable", "enable"]
    # MAC authentication username delimiter (default = hyphen).
    mac_username_delimiter: Literal["colon", "hyphen", "none", "single-hyphen"]
    # MAC authentication password delimiter (default = hyphen).
    mac_password_delimiter: Literal["colon", "hyphen", "none", "single-hyphen"]
    # MAC calling station delimiter (default = hyphen).
    mac_calling_station_delimiter: Literal["colon", "hyphen", "none", "single-hyphen"]
    # MAC called station delimiter (default = hyphen).
    mac_called_station_delimiter: Literal["colon", "hyphen", "none", "single-hyphen"]
    # MAC case (default = lowercase).
    mac_case: Literal["lowercase", "uppercase"]
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> X8021xSettingsPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class X8021xSettings:
    """
    Configure global 802.1X settings.
    
    Path: switch_controller/x802_1x_settings
    Category: cmdb
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
    ) -> X8021xSettingsObject: ...
    
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
    ) -> X8021xSettingsObject: ...
    
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
    ) -> X8021xSettingsObject: ...
    
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
    ) -> X8021xSettingsResponse: ...
    
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
    ) -> X8021xSettingsResponse: ...
    
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
    ) -> X8021xSettingsResponse: ...
    
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
    ) -> dict[str, Any]: ...
    
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
    ) -> X8021xSettingsObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: X8021xSettingsPayload | None = ...,
        link_down_auth: Literal["set-unauth", "no-action"] | None = ...,
        reauth_period: int | None = ...,
        max_reauth_attempt: int | None = ...,
        tx_period: int | None = ...,
        mab_reauth: Literal["disable", "enable"] | None = ...,
        mac_username_delimiter: Literal["colon", "hyphen", "none", "single-hyphen"] | None = ...,
        mac_password_delimiter: Literal["colon", "hyphen", "none", "single-hyphen"] | None = ...,
        mac_calling_station_delimiter: Literal["colon", "hyphen", "none", "single-hyphen"] | None = ...,
        mac_called_station_delimiter: Literal["colon", "hyphen", "none", "single-hyphen"] | None = ...,
        mac_case: Literal["lowercase", "uppercase"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> X8021xSettingsObject: ...
    
    @overload
    def put(
        self,
        payload_dict: X8021xSettingsPayload | None = ...,
        link_down_auth: Literal["set-unauth", "no-action"] | None = ...,
        reauth_period: int | None = ...,
        max_reauth_attempt: int | None = ...,
        tx_period: int | None = ...,
        mab_reauth: Literal["disable", "enable"] | None = ...,
        mac_username_delimiter: Literal["colon", "hyphen", "none", "single-hyphen"] | None = ...,
        mac_password_delimiter: Literal["colon", "hyphen", "none", "single-hyphen"] | None = ...,
        mac_calling_station_delimiter: Literal["colon", "hyphen", "none", "single-hyphen"] | None = ...,
        mac_called_station_delimiter: Literal["colon", "hyphen", "none", "single-hyphen"] | None = ...,
        mac_case: Literal["lowercase", "uppercase"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: X8021xSettingsPayload | None = ...,
        link_down_auth: Literal["set-unauth", "no-action"] | None = ...,
        reauth_period: int | None = ...,
        max_reauth_attempt: int | None = ...,
        tx_period: int | None = ...,
        mab_reauth: Literal["disable", "enable"] | None = ...,
        mac_username_delimiter: Literal["colon", "hyphen", "none", "single-hyphen"] | None = ...,
        mac_password_delimiter: Literal["colon", "hyphen", "none", "single-hyphen"] | None = ...,
        mac_calling_station_delimiter: Literal["colon", "hyphen", "none", "single-hyphen"] | None = ...,
        mac_called_station_delimiter: Literal["colon", "hyphen", "none", "single-hyphen"] | None = ...,
        mac_case: Literal["lowercase", "uppercase"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: X8021xSettingsPayload | None = ...,
        link_down_auth: Literal["set-unauth", "no-action"] | None = ...,
        reauth_period: int | None = ...,
        max_reauth_attempt: int | None = ...,
        tx_period: int | None = ...,
        mab_reauth: Literal["disable", "enable"] | None = ...,
        mac_username_delimiter: Literal["colon", "hyphen", "none", "single-hyphen"] | None = ...,
        mac_password_delimiter: Literal["colon", "hyphen", "none", "single-hyphen"] | None = ...,
        mac_calling_station_delimiter: Literal["colon", "hyphen", "none", "single-hyphen"] | None = ...,
        mac_called_station_delimiter: Literal["colon", "hyphen", "none", "single-hyphen"] | None = ...,
        mac_case: Literal["lowercase", "uppercase"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: X8021xSettingsPayload | None = ...,
        link_down_auth: Literal["set-unauth", "no-action"] | None = ...,
        reauth_period: int | None = ...,
        max_reauth_attempt: int | None = ...,
        tx_period: int | None = ...,
        mab_reauth: Literal["disable", "enable"] | None = ...,
        mac_username_delimiter: Literal["colon", "hyphen", "none", "single-hyphen"] | None = ...,
        mac_password_delimiter: Literal["colon", "hyphen", "none", "single-hyphen"] | None = ...,
        mac_calling_station_delimiter: Literal["colon", "hyphen", "none", "single-hyphen"] | None = ...,
        mac_called_station_delimiter: Literal["colon", "hyphen", "none", "single-hyphen"] | None = ...,
        mac_case: Literal["lowercase", "uppercase"] | None = ...,
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
    "X8021xSettings",
    "X8021xSettingsPayload",
    "X8021xSettingsObject",
]