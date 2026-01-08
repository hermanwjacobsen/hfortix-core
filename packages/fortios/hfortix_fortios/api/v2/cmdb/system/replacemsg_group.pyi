from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class ReplacemsgGroupPayload(TypedDict, total=False):
    """
    Type hints for system/replacemsg_group payload fields.
    
    Configure replacement message groups.
    
    **Usage:**
        payload: ReplacemsgGroupPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Group name.
    comment: NotRequired[str]  # Comment.
    group_type: Literal["default", "utm", "auth"]  # Group type.
    mail: NotRequired[list[dict[str, Any]]]  # Replacement message table entries.
    http: NotRequired[list[dict[str, Any]]]  # Replacement message table entries.
    webproxy: NotRequired[list[dict[str, Any]]]  # Replacement message table entries.
    ftp: NotRequired[list[dict[str, Any]]]  # Replacement message table entries.
    fortiguard_wf: NotRequired[list[dict[str, Any]]]  # Replacement message table entries.
    spam: NotRequired[list[dict[str, Any]]]  # Replacement message table entries.
    alertmail: NotRequired[list[dict[str, Any]]]  # Replacement message table entries.
    admin: NotRequired[list[dict[str, Any]]]  # Replacement message table entries.
    auth: NotRequired[list[dict[str, Any]]]  # Replacement message table entries.
    sslvpn: NotRequired[list[dict[str, Any]]]  # Replacement message table entries.
    nac_quar: NotRequired[list[dict[str, Any]]]  # Replacement message table entries.
    traffic_quota: NotRequired[list[dict[str, Any]]]  # Replacement message table entries.
    utm: NotRequired[list[dict[str, Any]]]  # Replacement message table entries.
    custom_message: NotRequired[list[dict[str, Any]]]  # Replacement message table entries.
    icap: NotRequired[list[dict[str, Any]]]  # Replacement message table entries.
    automation: NotRequired[list[dict[str, Any]]]  # Replacement message table entries.

# Nested classes for table field children

@final
class ReplacemsgGroupMailObject:
    """Typed object for mail table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Message type.
    msg_type: str
    # Message string.
    buffer: str
    # Header flag.
    header: Literal["none", "http", "8bit"]
    # Format flag.
    format: Literal["none", "text", "html"]
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class ReplacemsgGroupHttpObject:
    """Typed object for http table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Message type.
    msg_type: str
    # Message string.
    buffer: str
    # Header flag.
    header: Literal["none", "http", "8bit"]
    # Format flag.
    format: Literal["none", "text", "html"]
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class ReplacemsgGroupWebproxyObject:
    """Typed object for webproxy table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Message type.
    msg_type: str
    # Message string.
    buffer: str
    # Header flag.
    header: Literal["none", "http", "8bit"]
    # Format flag.
    format: Literal["none", "text", "html"]
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class ReplacemsgGroupFtpObject:
    """Typed object for ftp table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Message type.
    msg_type: str
    # Message string.
    buffer: str
    # Header flag.
    header: Literal["none", "http", "8bit"]
    # Format flag.
    format: Literal["none", "text", "html"]
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class ReplacemsgGroupFortiguardwfObject:
    """Typed object for fortiguard-wf table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Message type.
    msg_type: str
    # Message string.
    buffer: str
    # Header flag.
    header: Literal["none", "http", "8bit"]
    # Format flag.
    format: Literal["none", "text", "html"]
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class ReplacemsgGroupSpamObject:
    """Typed object for spam table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Message type.
    msg_type: str
    # Message string.
    buffer: str
    # Header flag.
    header: Literal["none", "http", "8bit"]
    # Format flag.
    format: Literal["none", "text", "html"]
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class ReplacemsgGroupAlertmailObject:
    """Typed object for alertmail table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Message type.
    msg_type: str
    # Message string.
    buffer: str
    # Header flag.
    header: Literal["none", "http", "8bit"]
    # Format flag.
    format: Literal["none", "text", "html"]
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class ReplacemsgGroupAdminObject:
    """Typed object for admin table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Message type.
    msg_type: str
    # Message string.
    buffer: str
    # Header flag.
    header: Literal["none", "http", "8bit"]
    # Format flag.
    format: Literal["none", "text", "html"]
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class ReplacemsgGroupAuthObject:
    """Typed object for auth table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Message type.
    msg_type: str
    # Message string.
    buffer: str
    # Header flag.
    header: Literal["none", "http", "8bit"]
    # Format flag.
    format: Literal["none", "text", "html"]
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class ReplacemsgGroupSslvpnObject:
    """Typed object for sslvpn table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Message type.
    msg_type: str
    # Message string.
    buffer: str
    # Header flag.
    header: Literal["none", "http", "8bit"]
    # Format flag.
    format: Literal["none", "text", "html"]
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class ReplacemsgGroupNacquarObject:
    """Typed object for nac-quar table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Message type.
    msg_type: str
    # Message string.
    buffer: str
    # Header flag.
    header: Literal["none", "http", "8bit"]
    # Format flag.
    format: Literal["none", "text", "html"]
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class ReplacemsgGroupTrafficquotaObject:
    """Typed object for traffic-quota table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Message type.
    msg_type: str
    # Message string.
    buffer: str
    # Header flag.
    header: Literal["none", "http", "8bit"]
    # Format flag.
    format: Literal["none", "text", "html"]
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class ReplacemsgGroupUtmObject:
    """Typed object for utm table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Message type.
    msg_type: str
    # Message string.
    buffer: str
    # Header flag.
    header: Literal["none", "http", "8bit"]
    # Format flag.
    format: Literal["none", "text", "html"]
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class ReplacemsgGroupCustommessageObject:
    """Typed object for custom-message table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Message type.
    msg_type: str
    # Message string.
    buffer: str
    # Header flag.
    header: Literal["none", "http", "8bit"]
    # Format flag.
    format: Literal["none", "text", "html"]
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class ReplacemsgGroupIcapObject:
    """Typed object for icap table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Message type.
    msg_type: str
    # Message string.
    buffer: str
    # Header flag.
    header: Literal["none", "http", "8bit"]
    # Format flag.
    format: Literal["none", "text", "html"]
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class ReplacemsgGroupAutomationObject:
    """Typed object for automation table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Message type.
    msg_type: str
    # Message string.
    buffer: str
    # Header flag.
    header: Literal["none", "http", "8bit"]
    # Format flag.
    format: Literal["none", "text", "html"]
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...



# Response TypedDict for GET returns (all fields present in API response)
class ReplacemsgGroupResponse(TypedDict):
    """
    Type hints for system/replacemsg_group API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str
    comment: str
    group_type: Literal["default", "utm", "auth"]
    mail: list[dict[str, Any]]
    http: list[dict[str, Any]]
    webproxy: list[dict[str, Any]]
    ftp: list[dict[str, Any]]
    fortiguard_wf: list[dict[str, Any]]
    spam: list[dict[str, Any]]
    alertmail: list[dict[str, Any]]
    admin: list[dict[str, Any]]
    auth: list[dict[str, Any]]
    sslvpn: list[dict[str, Any]]
    nac_quar: list[dict[str, Any]]
    traffic_quota: list[dict[str, Any]]
    utm: list[dict[str, Any]]
    custom_message: list[dict[str, Any]]
    icap: list[dict[str, Any]]
    automation: list[dict[str, Any]]


@final
class ReplacemsgGroupObject:
    """Typed FortiObject for system/replacemsg_group with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Group name.
    name: str
    # Comment.
    comment: str
    # Group type.
    group_type: Literal["default", "utm", "auth"]
    # Replacement message table entries.
    mail: list[ReplacemsgGroupMailObject]  # Table field - list of typed objects
    # Replacement message table entries.
    http: list[ReplacemsgGroupHttpObject]  # Table field - list of typed objects
    # Replacement message table entries.
    webproxy: list[ReplacemsgGroupWebproxyObject]  # Table field - list of typed objects
    # Replacement message table entries.
    ftp: list[ReplacemsgGroupFtpObject]  # Table field - list of typed objects
    # Replacement message table entries.
    fortiguard_wf: list[ReplacemsgGroupFortiguardwfObject]  # Table field - list of typed objects
    # Replacement message table entries.
    spam: list[ReplacemsgGroupSpamObject]  # Table field - list of typed objects
    # Replacement message table entries.
    alertmail: list[ReplacemsgGroupAlertmailObject]  # Table field - list of typed objects
    # Replacement message table entries.
    admin: list[ReplacemsgGroupAdminObject]  # Table field - list of typed objects
    # Replacement message table entries.
    auth: list[ReplacemsgGroupAuthObject]  # Table field - list of typed objects
    # Replacement message table entries.
    sslvpn: list[ReplacemsgGroupSslvpnObject]  # Table field - list of typed objects
    # Replacement message table entries.
    nac_quar: list[ReplacemsgGroupNacquarObject]  # Table field - list of typed objects
    # Replacement message table entries.
    traffic_quota: list[ReplacemsgGroupTrafficquotaObject]  # Table field - list of typed objects
    # Replacement message table entries.
    utm: list[ReplacemsgGroupUtmObject]  # Table field - list of typed objects
    # Replacement message table entries.
    custom_message: list[ReplacemsgGroupCustommessageObject]  # Table field - list of typed objects
    # Replacement message table entries.
    icap: list[ReplacemsgGroupIcapObject]  # Table field - list of typed objects
    # Replacement message table entries.
    automation: list[ReplacemsgGroupAutomationObject]  # Table field - list of typed objects
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> ReplacemsgGroupPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class ReplacemsgGroup:
    """
    Configure replacement message groups.
    
    Path: system/replacemsg_group
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
    ) -> ReplacemsgGroupObject: ...
    
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
    ) -> ReplacemsgGroupObject: ...
    
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
    ) -> list[ReplacemsgGroupObject]: ...
    
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
    ) -> ReplacemsgGroupResponse: ...
    
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
    ) -> ReplacemsgGroupResponse: ...
    
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
    ) -> list[ReplacemsgGroupResponse]: ...
    
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
    ) -> ReplacemsgGroupObject | list[ReplacemsgGroupObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: ReplacemsgGroupPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        group_type: Literal["default", "utm", "auth"] | None = ...,
        mail: str | list[str] | list[dict[str, Any]] | None = ...,
        http: str | list[str] | list[dict[str, Any]] | None = ...,
        webproxy: str | list[str] | list[dict[str, Any]] | None = ...,
        ftp: str | list[str] | list[dict[str, Any]] | None = ...,
        fortiguard_wf: str | list[str] | list[dict[str, Any]] | None = ...,
        spam: str | list[str] | list[dict[str, Any]] | None = ...,
        alertmail: str | list[str] | list[dict[str, Any]] | None = ...,
        admin: str | list[str] | list[dict[str, Any]] | None = ...,
        auth: str | list[str] | list[dict[str, Any]] | None = ...,
        sslvpn: str | list[str] | list[dict[str, Any]] | None = ...,
        nac_quar: str | list[str] | list[dict[str, Any]] | None = ...,
        traffic_quota: str | list[str] | list[dict[str, Any]] | None = ...,
        utm: str | list[str] | list[dict[str, Any]] | None = ...,
        custom_message: str | list[str] | list[dict[str, Any]] | None = ...,
        icap: str | list[str] | list[dict[str, Any]] | None = ...,
        automation: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ReplacemsgGroupObject: ...
    
    @overload
    def post(
        self,
        payload_dict: ReplacemsgGroupPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        group_type: Literal["default", "utm", "auth"] | None = ...,
        mail: str | list[str] | list[dict[str, Any]] | None = ...,
        http: str | list[str] | list[dict[str, Any]] | None = ...,
        webproxy: str | list[str] | list[dict[str, Any]] | None = ...,
        ftp: str | list[str] | list[dict[str, Any]] | None = ...,
        fortiguard_wf: str | list[str] | list[dict[str, Any]] | None = ...,
        spam: str | list[str] | list[dict[str, Any]] | None = ...,
        alertmail: str | list[str] | list[dict[str, Any]] | None = ...,
        admin: str | list[str] | list[dict[str, Any]] | None = ...,
        auth: str | list[str] | list[dict[str, Any]] | None = ...,
        sslvpn: str | list[str] | list[dict[str, Any]] | None = ...,
        nac_quar: str | list[str] | list[dict[str, Any]] | None = ...,
        traffic_quota: str | list[str] | list[dict[str, Any]] | None = ...,
        utm: str | list[str] | list[dict[str, Any]] | None = ...,
        custom_message: str | list[str] | list[dict[str, Any]] | None = ...,
        icap: str | list[str] | list[dict[str, Any]] | None = ...,
        automation: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: ReplacemsgGroupPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        group_type: Literal["default", "utm", "auth"] | None = ...,
        mail: str | list[str] | list[dict[str, Any]] | None = ...,
        http: str | list[str] | list[dict[str, Any]] | None = ...,
        webproxy: str | list[str] | list[dict[str, Any]] | None = ...,
        ftp: str | list[str] | list[dict[str, Any]] | None = ...,
        fortiguard_wf: str | list[str] | list[dict[str, Any]] | None = ...,
        spam: str | list[str] | list[dict[str, Any]] | None = ...,
        alertmail: str | list[str] | list[dict[str, Any]] | None = ...,
        admin: str | list[str] | list[dict[str, Any]] | None = ...,
        auth: str | list[str] | list[dict[str, Any]] | None = ...,
        sslvpn: str | list[str] | list[dict[str, Any]] | None = ...,
        nac_quar: str | list[str] | list[dict[str, Any]] | None = ...,
        traffic_quota: str | list[str] | list[dict[str, Any]] | None = ...,
        utm: str | list[str] | list[dict[str, Any]] | None = ...,
        custom_message: str | list[str] | list[dict[str, Any]] | None = ...,
        icap: str | list[str] | list[dict[str, Any]] | None = ...,
        automation: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: ReplacemsgGroupPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        group_type: Literal["default", "utm", "auth"] | None = ...,
        mail: str | list[str] | list[dict[str, Any]] | None = ...,
        http: str | list[str] | list[dict[str, Any]] | None = ...,
        webproxy: str | list[str] | list[dict[str, Any]] | None = ...,
        ftp: str | list[str] | list[dict[str, Any]] | None = ...,
        fortiguard_wf: str | list[str] | list[dict[str, Any]] | None = ...,
        spam: str | list[str] | list[dict[str, Any]] | None = ...,
        alertmail: str | list[str] | list[dict[str, Any]] | None = ...,
        admin: str | list[str] | list[dict[str, Any]] | None = ...,
        auth: str | list[str] | list[dict[str, Any]] | None = ...,
        sslvpn: str | list[str] | list[dict[str, Any]] | None = ...,
        nac_quar: str | list[str] | list[dict[str, Any]] | None = ...,
        traffic_quota: str | list[str] | list[dict[str, Any]] | None = ...,
        utm: str | list[str] | list[dict[str, Any]] | None = ...,
        custom_message: str | list[str] | list[dict[str, Any]] | None = ...,
        icap: str | list[str] | list[dict[str, Any]] | None = ...,
        automation: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: ReplacemsgGroupPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        group_type: Literal["default", "utm", "auth"] | None = ...,
        mail: str | list[str] | list[dict[str, Any]] | None = ...,
        http: str | list[str] | list[dict[str, Any]] | None = ...,
        webproxy: str | list[str] | list[dict[str, Any]] | None = ...,
        ftp: str | list[str] | list[dict[str, Any]] | None = ...,
        fortiguard_wf: str | list[str] | list[dict[str, Any]] | None = ...,
        spam: str | list[str] | list[dict[str, Any]] | None = ...,
        alertmail: str | list[str] | list[dict[str, Any]] | None = ...,
        admin: str | list[str] | list[dict[str, Any]] | None = ...,
        auth: str | list[str] | list[dict[str, Any]] | None = ...,
        sslvpn: str | list[str] | list[dict[str, Any]] | None = ...,
        nac_quar: str | list[str] | list[dict[str, Any]] | None = ...,
        traffic_quota: str | list[str] | list[dict[str, Any]] | None = ...,
        utm: str | list[str] | list[dict[str, Any]] | None = ...,
        custom_message: str | list[str] | list[dict[str, Any]] | None = ...,
        icap: str | list[str] | list[dict[str, Any]] | None = ...,
        automation: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ReplacemsgGroupObject: ...
    
    @overload
    def put(
        self,
        payload_dict: ReplacemsgGroupPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        group_type: Literal["default", "utm", "auth"] | None = ...,
        mail: str | list[str] | list[dict[str, Any]] | None = ...,
        http: str | list[str] | list[dict[str, Any]] | None = ...,
        webproxy: str | list[str] | list[dict[str, Any]] | None = ...,
        ftp: str | list[str] | list[dict[str, Any]] | None = ...,
        fortiguard_wf: str | list[str] | list[dict[str, Any]] | None = ...,
        spam: str | list[str] | list[dict[str, Any]] | None = ...,
        alertmail: str | list[str] | list[dict[str, Any]] | None = ...,
        admin: str | list[str] | list[dict[str, Any]] | None = ...,
        auth: str | list[str] | list[dict[str, Any]] | None = ...,
        sslvpn: str | list[str] | list[dict[str, Any]] | None = ...,
        nac_quar: str | list[str] | list[dict[str, Any]] | None = ...,
        traffic_quota: str | list[str] | list[dict[str, Any]] | None = ...,
        utm: str | list[str] | list[dict[str, Any]] | None = ...,
        custom_message: str | list[str] | list[dict[str, Any]] | None = ...,
        icap: str | list[str] | list[dict[str, Any]] | None = ...,
        automation: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: ReplacemsgGroupPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        group_type: Literal["default", "utm", "auth"] | None = ...,
        mail: str | list[str] | list[dict[str, Any]] | None = ...,
        http: str | list[str] | list[dict[str, Any]] | None = ...,
        webproxy: str | list[str] | list[dict[str, Any]] | None = ...,
        ftp: str | list[str] | list[dict[str, Any]] | None = ...,
        fortiguard_wf: str | list[str] | list[dict[str, Any]] | None = ...,
        spam: str | list[str] | list[dict[str, Any]] | None = ...,
        alertmail: str | list[str] | list[dict[str, Any]] | None = ...,
        admin: str | list[str] | list[dict[str, Any]] | None = ...,
        auth: str | list[str] | list[dict[str, Any]] | None = ...,
        sslvpn: str | list[str] | list[dict[str, Any]] | None = ...,
        nac_quar: str | list[str] | list[dict[str, Any]] | None = ...,
        traffic_quota: str | list[str] | list[dict[str, Any]] | None = ...,
        utm: str | list[str] | list[dict[str, Any]] | None = ...,
        custom_message: str | list[str] | list[dict[str, Any]] | None = ...,
        icap: str | list[str] | list[dict[str, Any]] | None = ...,
        automation: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: ReplacemsgGroupPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        group_type: Literal["default", "utm", "auth"] | None = ...,
        mail: str | list[str] | list[dict[str, Any]] | None = ...,
        http: str | list[str] | list[dict[str, Any]] | None = ...,
        webproxy: str | list[str] | list[dict[str, Any]] | None = ...,
        ftp: str | list[str] | list[dict[str, Any]] | None = ...,
        fortiguard_wf: str | list[str] | list[dict[str, Any]] | None = ...,
        spam: str | list[str] | list[dict[str, Any]] | None = ...,
        alertmail: str | list[str] | list[dict[str, Any]] | None = ...,
        admin: str | list[str] | list[dict[str, Any]] | None = ...,
        auth: str | list[str] | list[dict[str, Any]] | None = ...,
        sslvpn: str | list[str] | list[dict[str, Any]] | None = ...,
        nac_quar: str | list[str] | list[dict[str, Any]] | None = ...,
        traffic_quota: str | list[str] | list[dict[str, Any]] | None = ...,
        utm: str | list[str] | list[dict[str, Any]] | None = ...,
        custom_message: str | list[str] | list[dict[str, Any]] | None = ...,
        icap: str | list[str] | list[dict[str, Any]] | None = ...,
        automation: str | list[str] | list[dict[str, Any]] | None = ...,
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
    ) -> ReplacemsgGroupObject: ...
    
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
        payload_dict: ReplacemsgGroupPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        group_type: Literal["default", "utm", "auth"] | None = ...,
        mail: str | list[str] | list[dict[str, Any]] | None = ...,
        http: str | list[str] | list[dict[str, Any]] | None = ...,
        webproxy: str | list[str] | list[dict[str, Any]] | None = ...,
        ftp: str | list[str] | list[dict[str, Any]] | None = ...,
        fortiguard_wf: str | list[str] | list[dict[str, Any]] | None = ...,
        spam: str | list[str] | list[dict[str, Any]] | None = ...,
        alertmail: str | list[str] | list[dict[str, Any]] | None = ...,
        admin: str | list[str] | list[dict[str, Any]] | None = ...,
        auth: str | list[str] | list[dict[str, Any]] | None = ...,
        sslvpn: str | list[str] | list[dict[str, Any]] | None = ...,
        nac_quar: str | list[str] | list[dict[str, Any]] | None = ...,
        traffic_quota: str | list[str] | list[dict[str, Any]] | None = ...,
        utm: str | list[str] | list[dict[str, Any]] | None = ...,
        custom_message: str | list[str] | list[dict[str, Any]] | None = ...,
        icap: str | list[str] | list[dict[str, Any]] | None = ...,
        automation: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "ReplacemsgGroup",
    "ReplacemsgGroupPayload",
    "ReplacemsgGroupObject",
]