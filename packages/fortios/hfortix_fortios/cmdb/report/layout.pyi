from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class LayoutPayload(TypedDict, total=False):
    """
    Type hints for report/layout payload fields.
    
    Report layout configuration.
    
    **Usage:**
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


class LayoutObject(FortiObject[LayoutPayload]):
    """Typed FortiObject for report/layout with IDE autocomplete support."""
    
    # Report layout name.
    name: str
    # Report title.
    title: str
    # Report subtitle.
    subtitle: str
    # Description.
    description: str
    # Report style theme.
    style_theme: str
    # Report layout options.
    options: Literal["include-table-of-content", "auto-numbering-heading", "view-chart-as-heading", "show-html-navbar-before-heading", "dummy-option"]
    # Report format.
    format: Literal["pdf"]
    # Report schedule type.
    schedule_type: Literal["demand", "daily", "weekly"]
    # Schedule days of week to generate report.
    day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
    # Schedule time to generate report (format = hh:mm).
    time: str
    # Cutoff-option is either run-time or custom.
    cutoff_option: Literal["run-time", "custom"]
    # Custom cutoff time to generate report (format = hh:mm).
    cutoff_time: str
    # Enable/disable sending emails after reports are generated.
    email_send: Literal["enable", "disable"]
    # Email recipients for generated reports.
    email_recipients: str
    # Maximum number of PDF reports to keep at one time (oldest report is overwritten)
    max_pdf_report: int
    # Configure report page.
    page: str
    # Configure report body item.
    body_item: list[str]  # Auto-flattened from member_table
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> LayoutPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Layout:
    """
    Report layout configuration.
    
    Path: report/layout
    Category: cmdb
    Primary Key: name
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey provided)
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
        *,
        response_mode: Literal["object"],
        **kwargs: Any,
    ) -> LayoutObject: ...
    
    # List of objects (no mkey provided - most specific for list returns)
    # For singleton endpoints (no mkey), returns single object; for table endpoints, returns list
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
        response_mode: Literal["object"],
        **kwargs: Any,
    ) -> list[LayoutObject]: ...
    
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
        raw_json: Literal[True],
        *,
        response_mode: Literal["object"],
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Dict mode with mkey provided (single dict)
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
    ) -> dict[str, Any]: ...
    
    # Dict mode without mkey (returns dict with results array)
    @overload
    def get(
        self,
        name: None = None,
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
    ) -> dict[str, Any]: ...
    
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
    ) -> LayoutObject | list[LayoutObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: LayoutPayload | None = ...,
        name: str | None = ...,
        title: str | None = ...,
        subtitle: str | None = ...,
        description: str | None = ...,
        style_theme: str | None = ...,
        options: Literal["include-table-of-content", "auto-numbering-heading", "view-chart-as-heading", "show-html-navbar-before-heading", "dummy-option"] | list[str] | list[dict[str, Any]] | None = ...,
        format: Literal["pdf"] | list[str] | list[dict[str, Any]] | None = ...,
        schedule_type: Literal["demand", "daily", "weekly"] | None = ...,
        day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | None = ...,
        time: str | None = ...,
        cutoff_option: Literal["run-time", "custom"] | None = ...,
        cutoff_time: str | None = ...,
        email_send: Literal["enable", "disable"] | None = ...,
        email_recipients: str | None = ...,
        max_pdf_report: int | None = ...,
        page: str | None = ...,
        body_item: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> LayoutObject: ...
    
    @overload
    def post(
        self,
        payload_dict: LayoutPayload | None = ...,
        name: str | None = ...,
        title: str | None = ...,
        subtitle: str | None = ...,
        description: str | None = ...,
        style_theme: str | None = ...,
        options: Literal["include-table-of-content", "auto-numbering-heading", "view-chart-as-heading", "show-html-navbar-before-heading", "dummy-option"] | list[str] | list[dict[str, Any]] | None = ...,
        format: Literal["pdf"] | list[str] | list[dict[str, Any]] | None = ...,
        schedule_type: Literal["demand", "daily", "weekly"] | None = ...,
        day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | None = ...,
        time: str | None = ...,
        cutoff_option: Literal["run-time", "custom"] | None = ...,
        cutoff_time: str | None = ...,
        email_send: Literal["enable", "disable"] | None = ...,
        email_recipients: str | None = ...,
        max_pdf_report: int | None = ...,
        page: str | None = ...,
        body_item: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: LayoutPayload | None = ...,
        name: str | None = ...,
        title: str | None = ...,
        subtitle: str | None = ...,
        description: str | None = ...,
        style_theme: str | None = ...,
        options: Literal["include-table-of-content", "auto-numbering-heading", "view-chart-as-heading", "show-html-navbar-before-heading", "dummy-option"] | list[str] | list[dict[str, Any]] | None = ...,
        format: Literal["pdf"] | list[str] | list[dict[str, Any]] | None = ...,
        schedule_type: Literal["demand", "daily", "weekly"] | None = ...,
        day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | None = ...,
        time: str | None = ...,
        cutoff_option: Literal["run-time", "custom"] | None = ...,
        cutoff_time: str | None = ...,
        email_send: Literal["enable", "disable"] | None = ...,
        email_recipients: str | None = ...,
        max_pdf_report: int | None = ...,
        page: str | None = ...,
        body_item: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: LayoutPayload | None = ...,
        name: str | None = ...,
        title: str | None = ...,
        subtitle: str | None = ...,
        description: str | None = ...,
        style_theme: str | None = ...,
        options: Literal["include-table-of-content", "auto-numbering-heading", "view-chart-as-heading", "show-html-navbar-before-heading", "dummy-option"] | list[str] | list[dict[str, Any]] | None = ...,
        format: Literal["pdf"] | list[str] | list[dict[str, Any]] | None = ...,
        schedule_type: Literal["demand", "daily", "weekly"] | None = ...,
        day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | None = ...,
        time: str | None = ...,
        cutoff_option: Literal["run-time", "custom"] | None = ...,
        cutoff_time: str | None = ...,
        email_send: Literal["enable", "disable"] | None = ...,
        email_recipients: str | None = ...,
        max_pdf_report: int | None = ...,
        page: str | None = ...,
        body_item: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: LayoutPayload | None = ...,
        name: str | None = ...,
        title: str | None = ...,
        subtitle: str | None = ...,
        description: str | None = ...,
        style_theme: str | None = ...,
        options: Literal["include-table-of-content", "auto-numbering-heading", "view-chart-as-heading", "show-html-navbar-before-heading", "dummy-option"] | list[str] | list[dict[str, Any]] | None = ...,
        format: Literal["pdf"] | list[str] | list[dict[str, Any]] | None = ...,
        schedule_type: Literal["demand", "daily", "weekly"] | None = ...,
        day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | None = ...,
        time: str | None = ...,
        cutoff_option: Literal["run-time", "custom"] | None = ...,
        cutoff_time: str | None = ...,
        email_send: Literal["enable", "disable"] | None = ...,
        email_recipients: str | None = ...,
        max_pdf_report: int | None = ...,
        page: str | None = ...,
        body_item: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> LayoutObject: ...
    
    @overload
    def put(
        self,
        payload_dict: LayoutPayload | None = ...,
        name: str | None = ...,
        title: str | None = ...,
        subtitle: str | None = ...,
        description: str | None = ...,
        style_theme: str | None = ...,
        options: Literal["include-table-of-content", "auto-numbering-heading", "view-chart-as-heading", "show-html-navbar-before-heading", "dummy-option"] | list[str] | list[dict[str, Any]] | None = ...,
        format: Literal["pdf"] | list[str] | list[dict[str, Any]] | None = ...,
        schedule_type: Literal["demand", "daily", "weekly"] | None = ...,
        day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | None = ...,
        time: str | None = ...,
        cutoff_option: Literal["run-time", "custom"] | None = ...,
        cutoff_time: str | None = ...,
        email_send: Literal["enable", "disable"] | None = ...,
        email_recipients: str | None = ...,
        max_pdf_report: int | None = ...,
        page: str | None = ...,
        body_item: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: LayoutPayload | None = ...,
        name: str | None = ...,
        title: str | None = ...,
        subtitle: str | None = ...,
        description: str | None = ...,
        style_theme: str | None = ...,
        options: Literal["include-table-of-content", "auto-numbering-heading", "view-chart-as-heading", "show-html-navbar-before-heading", "dummy-option"] | list[str] | list[dict[str, Any]] | None = ...,
        format: Literal["pdf"] | list[str] | list[dict[str, Any]] | None = ...,
        schedule_type: Literal["demand", "daily", "weekly"] | None = ...,
        day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | None = ...,
        time: str | None = ...,
        cutoff_option: Literal["run-time", "custom"] | None = ...,
        cutoff_time: str | None = ...,
        email_send: Literal["enable", "disable"] | None = ...,
        email_recipients: str | None = ...,
        max_pdf_report: int | None = ...,
        page: str | None = ...,
        body_item: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: LayoutPayload | None = ...,
        name: str | None = ...,
        title: str | None = ...,
        subtitle: str | None = ...,
        description: str | None = ...,
        style_theme: str | None = ...,
        options: Literal["include-table-of-content", "auto-numbering-heading", "view-chart-as-heading", "show-html-navbar-before-heading", "dummy-option"] | list[str] | list[dict[str, Any]] | None = ...,
        format: Literal["pdf"] | list[str] | list[dict[str, Any]] | None = ...,
        schedule_type: Literal["demand", "daily", "weekly"] | None = ...,
        day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | None = ...,
        time: str | None = ...,
        cutoff_option: Literal["run-time", "custom"] | None = ...,
        cutoff_time: str | None = ...,
        email_send: Literal["enable", "disable"] | None = ...,
        email_recipients: str | None = ...,
        max_pdf_report: int | None = ...,
        page: str | None = ...,
        body_item: str | list[str] | list[dict[str, Any]] | None = ...,
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
    ) -> LayoutObject: ...
    
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
        payload_dict: LayoutPayload | None = ...,
        name: str | None = ...,
        title: str | None = ...,
        subtitle: str | None = ...,
        description: str | None = ...,
        style_theme: str | None = ...,
        options: Literal["include-table-of-content", "auto-numbering-heading", "view-chart-as-heading", "show-html-navbar-before-heading", "dummy-option"] | list[str] | list[dict[str, Any]] | None = ...,
        format: Literal["pdf"] | list[str] | list[dict[str, Any]] | None = ...,
        schedule_type: Literal["demand", "daily", "weekly"] | None = ...,
        day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | None = ...,
        time: str | None = ...,
        cutoff_option: Literal["run-time", "custom"] | None = ...,
        cutoff_time: str | None = ...,
        email_send: Literal["enable", "disable"] | None = ...,
        email_recipients: str | None = ...,
        max_pdf_report: int | None = ...,
        page: str | None = ...,
        body_item: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "Layout",
    "LayoutPayload",
    "LayoutObject",
]