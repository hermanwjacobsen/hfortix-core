from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class UtmProfilePayload(TypedDict, total=False):
    """
    Type hints for wireless_controller/utm_profile payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: UtmProfilePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # UTM profile name.
    comment: NotRequired[str]  # Comment.
    utm_log: NotRequired[Literal["enable", "disable"]]  # Enable/disable UTM logging.
    ips_sensor: NotRequired[str]  # IPS sensor name.
    application_list: NotRequired[str]  # Application control list name.
    antivirus_profile: NotRequired[str]  # AntiVirus profile name.
    webfilter_profile: NotRequired[str]  # WebFilter profile name.
    scan_botnet_connections: NotRequired[Literal["disable", "monitor", "block"]]  # Block or monitor connections to Botnet servers or disable Bo


class UtmProfile:
    """
    Configure UTM (Unified Threat Management) profile.
    
    Path: wireless_controller/utm_profile
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
        payload_dict: UtmProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        utm_log: Literal["enable", "disable"] | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        antivirus_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        scan_botnet_connections: Literal["disable", "monitor", "block"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: UtmProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        utm_log: Literal["enable", "disable"] | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        antivirus_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        scan_botnet_connections: Literal["disable", "monitor", "block"] | None = ...,
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
        payload_dict: UtmProfilePayload | None = ...,
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