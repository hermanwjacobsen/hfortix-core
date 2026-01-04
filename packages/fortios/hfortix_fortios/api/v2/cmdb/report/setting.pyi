from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class SettingPayload(TypedDict, total=False):
    """
    Type hints for report/setting payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: SettingPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    pdf_report: NotRequired[Literal["enable", "disable"]]  # Enable/disable PDF report.
    fortiview: NotRequired[Literal["enable", "disable"]]  # Enable/disable historical FortiView.
    report_source: NotRequired[Literal["forward-traffic", "sniffer-traffic", "local-deny-traffic"]]  # Report log source.
    web_browsing_threshold: NotRequired[int]  # Web browsing time calculation threshold (3 - 15 min).
    top_n: NotRequired[int]  # Number of items to populate (1000 - 20000).


class Setting:
    """
    Report setting configuration.
    
    Path: report/setting
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
        payload_dict: SettingPayload | None = ...,
        pdf_report: Literal["enable", "disable"] | None = ...,
        fortiview: Literal["enable", "disable"] | None = ...,
        report_source: Literal["forward-traffic", "sniffer-traffic", "local-deny-traffic"] | None = ...,
        web_browsing_threshold: int | None = ...,
        top_n: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: SettingPayload | None = ...,
        pdf_report: Literal["enable", "disable"] | None = ...,
        fortiview: Literal["enable", "disable"] | None = ...,
        report_source: Literal["forward-traffic", "sniffer-traffic", "local-deny-traffic"] | None = ...,
        web_browsing_threshold: int | None = ...,
        top_n: int | None = ...,
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
        payload_dict: SettingPayload | None = ...,
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