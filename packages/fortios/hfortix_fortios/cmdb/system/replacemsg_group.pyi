from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
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


class ReplacemsgGroupObject(FortiObject[ReplacemsgGroupPayload]):
    """Typed FortiObject for system/replacemsg_group with IDE autocomplete support."""
    
    # Group name.
    name: str
    # Comment.
    comment: str
    # Group type.
    group_type: Literal["default", "utm", "auth"]
    # Replacement message table entries.
    mail: list[str]  # Auto-flattened from member_table
    # Replacement message table entries.
    http: list[str]  # Auto-flattened from member_table
    # Replacement message table entries.
    webproxy: list[str]  # Auto-flattened from member_table
    # Replacement message table entries.
    ftp: list[str]  # Auto-flattened from member_table
    # Replacement message table entries.
    fortiguard_wf: list[str]  # Auto-flattened from member_table
    # Replacement message table entries.
    spam: list[str]  # Auto-flattened from member_table
    # Replacement message table entries.
    alertmail: list[str]  # Auto-flattened from member_table
    # Replacement message table entries.
    admin: list[str]  # Auto-flattened from member_table
    # Replacement message table entries.
    auth: list[str]  # Auto-flattened from member_table
    # Replacement message table entries.
    sslvpn: list[str]  # Auto-flattened from member_table
    # Replacement message table entries.
    nac_quar: list[str]  # Auto-flattened from member_table
    # Replacement message table entries.
    traffic_quota: list[str]  # Auto-flattened from member_table
    # Replacement message table entries.
    utm: list[str]  # Auto-flattened from member_table
    # Replacement message table entries.
    custom_message: list[str]  # Auto-flattened from member_table
    # Replacement message table entries.
    icap: list[str]  # Auto-flattened from member_table
    # Replacement message table entries.
    automation: list[str]  # Auto-flattened from member_table
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> ReplacemsgGroupPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class ReplacemsgGroup:
    """
    Configure replacement message groups.
    
    Path: system/replacemsg_group
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
    ) -> ReplacemsgGroupObject: ...
    
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