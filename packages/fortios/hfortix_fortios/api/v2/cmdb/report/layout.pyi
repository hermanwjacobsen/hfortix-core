from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class LayoutPayload(TypedDict, total=False):
    """
    Type hints for report/layout payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: LayoutPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Report layout name.
    title: NotRequired[str]  # Report title.
    subtitle: NotRequired[str]  # Report subtitle.
    description: NotRequired[str]  # Description.
    style_theme: str  # Report style theme.
    options: NotRequired[Literal["include-table-of-content", "auto-numbering-heading", "view-chart-as-heading", "show-html-navbar-before-heading", "dummy-option"]]  # Report layout options.
    format: NotRequired[Literal["pdf"]]  # Report format.
    schedule_type: NotRequired[Literal["demand", "daily", "weekly"]]  # Report schedule type.
    day: NotRequired[Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]]  # Schedule days of week to generate report.
    time: NotRequired[str]  # Schedule time to generate report (format = hh:mm).
    cutoff_option: NotRequired[Literal["run-time", "custom"]]  # Cutoff-option is either run-time or custom.
    cutoff_time: NotRequired[str]  # Custom cutoff time to generate report (format = hh:mm).
    email_send: NotRequired[Literal["enable", "disable"]]  # Enable/disable sending emails after reports are generated.
    email_recipients: NotRequired[str]  # Email recipients for generated reports.
    max_pdf_report: NotRequired[int]  # Maximum number of PDF reports to keep at one time (oldest re
    page: NotRequired[str]  # Configure report page.
    body_item: NotRequired[list[dict[str, Any]]]  # Configure report body item.


class Layout:
    """
    Report layout configuration.
    
    Path: report/layout
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
        payload_dict: LayoutPayload | None = ...,
        name: str | None = ...,
        title: str | None = ...,
        subtitle: str | None = ...,
        description: str | None = ...,
        style_theme: str | None = ...,
        options: Literal["include-table-of-content", "auto-numbering-heading", "view-chart-as-heading", "show-html-navbar-before-heading", "dummy-option"] | None = ...,
        format: Literal["pdf"] | None = ...,
        schedule_type: Literal["demand", "daily", "weekly"] | None = ...,
        day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | None = ...,
        time: str | None = ...,
        cutoff_option: Literal["run-time", "custom"] | None = ...,
        cutoff_time: str | None = ...,
        email_send: Literal["enable", "disable"] | None = ...,
        email_recipients: str | None = ...,
        max_pdf_report: int | None = ...,
        page: str | None = ...,
        body_item: list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: LayoutPayload | None = ...,
        name: str | None = ...,
        title: str | None = ...,
        subtitle: str | None = ...,
        description: str | None = ...,
        style_theme: str | None = ...,
        options: Literal["include-table-of-content", "auto-numbering-heading", "view-chart-as-heading", "show-html-navbar-before-heading", "dummy-option"] | None = ...,
        format: Literal["pdf"] | None = ...,
        schedule_type: Literal["demand", "daily", "weekly"] | None = ...,
        day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | None = ...,
        time: str | None = ...,
        cutoff_option: Literal["run-time", "custom"] | None = ...,
        cutoff_time: str | None = ...,
        email_send: Literal["enable", "disable"] | None = ...,
        email_recipients: str | None = ...,
        max_pdf_report: int | None = ...,
        page: str | None = ...,
        body_item: list[dict[str, Any]] | None = ...,
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
        payload_dict: LayoutPayload | None = ...,
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