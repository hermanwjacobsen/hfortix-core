from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class X8021xSettingsPayload(TypedDict, total=False):
    """
    Type hints for switch_controller/x802_1X_settings payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: X8021xSettingsPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    link_down_auth: NotRequired[Literal["set-unauth", "no-action"]]  # Interface-reauthentication state to set if a link is down.
    reauth_period: NotRequired[int]  # Period of time to allow for reauthentication (1 - 1440 sec, 
    max_reauth_attempt: NotRequired[int]  # Maximum number of authentication attempts (0 - 15, default =
    tx_period: NotRequired[int]  # 802.1X Tx period (seconds, default=30).
    mab_reauth: NotRequired[Literal["disable", "enable"]]  # Enable/disable MAB re-authentication.
    mac_username_delimiter: NotRequired[Literal["colon", "hyphen", "none", "single-hyphen"]]  # MAC authentication username delimiter (default = hyphen).
    mac_password_delimiter: NotRequired[Literal["colon", "hyphen", "none", "single-hyphen"]]  # MAC authentication password delimiter (default = hyphen).
    mac_calling_station_delimiter: NotRequired[Literal["colon", "hyphen", "none", "single-hyphen"]]  # MAC calling station delimiter (default = hyphen).
    mac_called_station_delimiter: NotRequired[Literal["colon", "hyphen", "none", "single-hyphen"]]  # MAC called station delimiter (default = hyphen).
    mac_case: NotRequired[Literal["lowercase", "uppercase"]]  # MAC case (default = lowercase).


class X8021xSettings:
    """
    Configure global 802.1X settings.
    
    Path: switch_controller/x802_1X_settings
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
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
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
        payload_dict: X8021xSettingsPayload | None = ...,
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