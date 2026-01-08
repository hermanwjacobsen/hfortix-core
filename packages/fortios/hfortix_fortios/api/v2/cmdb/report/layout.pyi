from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
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
    max_pdf_report: NotRequired[int]  # Maximum number of PDF reports to keep at one time
    page: NotRequired[str]  # Configure report page.
    body_item: NotRequired[list[dict[str, Any]]]  # Configure report body item.

# Nested classes for table field children

@final
class LayoutBodyitemObject:
    """Typed object for body-item table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Report item ID.
    id: int
    # Description.
    description: str
    # Report item type.
    type: Literal["text", "image", "chart", "misc"]
    # Report item style.
    style: str
    # Value of top.
    top_n: int
    # Parameters.
    parameters: str
    # Report item text component.
    text_component: Literal["text", "heading1", "heading2", "heading3"]
    # Report item text content.
    content: str
    # Report item image file name.
    img_src: str
    # Report item chart name.
    chart: str
    # Report chart options.
    chart_options: Literal["include-no-data", "hide-title", "show-caption"]
    # Report item miscellaneous component.
    misc_component: Literal["hline", "page-break", "column-break", "section-start"]
    # Report section title.
    title: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...



# Response TypedDict for GET returns (all fields present in API response)
class LayoutResponse(TypedDict):
    """
    Type hints for report/layout API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str
    title: str
    subtitle: str
    description: str
    style_theme: str
    options: Literal["include-table-of-content", "auto-numbering-heading", "view-chart-as-heading", "show-html-navbar-before-heading", "dummy-option"]
    format: Literal["pdf"]
    schedule_type: Literal["demand", "daily", "weekly"]
    day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
    time: str
    cutoff_option: Literal["run-time", "custom"]
    cutoff_time: str
    email_send: Literal["enable", "disable"]
    email_recipients: str
    max_pdf_report: int
    page: str
    body_item: list[dict[str, Any]]


@final
class LayoutObject:
    """Typed FortiObject for report/layout with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
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
    body_item: list[LayoutBodyitemObject]  # Table field - list of typed objects
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> LayoutPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class Layout:
    """
    Report layout configuration.
    
    Path: report/layout
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
    ) -> LayoutObject: ...
    
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
    ) -> LayoutObject: ...
    
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
    ) -> LayoutResponse: ...
    
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
    ) -> LayoutResponse: ...
    
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
    ) -> list[LayoutResponse]: ...
    
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
        options: Literal["include-table-of-content", "auto-numbering-heading", "view-chart-as-heading", "show-html-navbar-before-heading", "dummy-option"] | list[str] | None = ...,
        format: Literal["pdf"] | list[str] | None = ...,
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
        options: Literal["include-table-of-content", "auto-numbering-heading", "view-chart-as-heading", "show-html-navbar-before-heading", "dummy-option"] | list[str] | None = ...,
        format: Literal["pdf"] | list[str] | None = ...,
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
        options: Literal["include-table-of-content", "auto-numbering-heading", "view-chart-as-heading", "show-html-navbar-before-heading", "dummy-option"] | list[str] | None = ...,
        format: Literal["pdf"] | list[str] | None = ...,
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
        options: Literal["include-table-of-content", "auto-numbering-heading", "view-chart-as-heading", "show-html-navbar-before-heading", "dummy-option"] | list[str] | None = ...,
        format: Literal["pdf"] | list[str] | None = ...,
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
        options: Literal["include-table-of-content", "auto-numbering-heading", "view-chart-as-heading", "show-html-navbar-before-heading", "dummy-option"] | list[str] | None = ...,
        format: Literal["pdf"] | list[str] | None = ...,
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
        options: Literal["include-table-of-content", "auto-numbering-heading", "view-chart-as-heading", "show-html-navbar-before-heading", "dummy-option"] | list[str] | None = ...,
        format: Literal["pdf"] | list[str] | None = ...,
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
        options: Literal["include-table-of-content", "auto-numbering-heading", "view-chart-as-heading", "show-html-navbar-before-heading", "dummy-option"] | list[str] | None = ...,
        format: Literal["pdf"] | list[str] | None = ...,
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
        options: Literal["include-table-of-content", "auto-numbering-heading", "view-chart-as-heading", "show-html-navbar-before-heading", "dummy-option"] | list[str] | None = ...,
        format: Literal["pdf"] | list[str] | None = ...,
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
        options: Literal["include-table-of-content", "auto-numbering-heading", "view-chart-as-heading", "show-html-navbar-before-heading", "dummy-option"] | list[str] | None = ...,
        format: Literal["pdf"] | list[str] | None = ...,
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