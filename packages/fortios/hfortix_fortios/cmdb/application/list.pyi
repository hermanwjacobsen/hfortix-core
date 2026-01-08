from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class ListPayload(TypedDict, total=False):
    """
    Type hints for application/list payload fields.
    
    Configure application control lists.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.replacemsg-group.ReplacemsgGroupEndpoint` (via: replacemsg-group)

    **Usage:**
        payload: ListPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # List name.
    comment: NotRequired[str]  # Comments.
    replacemsg_group: NotRequired[str]  # Replacement message group.
    extended_log: NotRequired[Literal["enable", "disable"]]  # Enable/disable extended logging.
    other_application_action: NotRequired[Literal["pass", "block"]]  # Action for other applications.
    app_replacemsg: NotRequired[Literal["disable", "enable"]]  # Enable/disable replacement messages for blocked applications
    other_application_log: NotRequired[Literal["disable", "enable"]]  # Enable/disable logging for other applications.
    enforce_default_app_port: NotRequired[Literal["disable", "enable"]]  # Enable/disable default application port enforcement for allo
    force_inclusion_ssl_di_sigs: NotRequired[Literal["disable", "enable"]]  # Enable/disable forced inclusion of SSL deep inspection signa
    unknown_application_action: NotRequired[Literal["pass", "block"]]  # Pass or block traffic from unknown applications.
    unknown_application_log: NotRequired[Literal["disable", "enable"]]  # Enable/disable logging for unknown applications.
    p2p_block_list: NotRequired[Literal["skype", "edonkey", "bittorrent"]]  # P2P applications to be block listed.
    deep_app_inspection: NotRequired[Literal["disable", "enable"]]  # Enable/disable deep application inspection.
    options: NotRequired[Literal["allow-dns", "allow-icmp", "allow-http", "allow-ssl"]]  # Basic application protocol signatures allowed by default.
    entries: NotRequired[list[dict[str, Any]]]  # Application list entries.
    control_default_network_services: NotRequired[Literal["disable", "enable"]]  # Enable/disable enforcement of protocols over selected ports.
    default_network_services: NotRequired[list[dict[str, Any]]]  # Default network service entries.


class ListObject(FortiObject[ListPayload]):
    """Typed FortiObject for application/list with IDE autocomplete support."""
    
    # List name.
    name: str
    # Comments.
    comment: str
    # Replacement message group.
    replacemsg_group: str
    # Enable/disable extended logging.
    extended_log: Literal["enable", "disable"]
    # Action for other applications.
    other_application_action: Literal["pass", "block"]
    # Enable/disable replacement messages for blocked applications.
    app_replacemsg: Literal["disable", "enable"]
    # Enable/disable logging for other applications.
    other_application_log: Literal["disable", "enable"]
    # Enable/disable default application port enforcement for allowed applications.
    enforce_default_app_port: Literal["disable", "enable"]
    # Enable/disable forced inclusion of SSL deep inspection signatures.
    force_inclusion_ssl_di_sigs: Literal["disable", "enable"]
    # Pass or block traffic from unknown applications.
    unknown_application_action: Literal["pass", "block"]
    # Enable/disable logging for unknown applications.
    unknown_application_log: Literal["disable", "enable"]
    # P2P applications to be block listed.
    p2p_block_list: Literal["skype", "edonkey", "bittorrent"]
    # Enable/disable deep application inspection.
    deep_app_inspection: Literal["disable", "enable"]
    # Basic application protocol signatures allowed by default.
    options: Literal["allow-dns", "allow-icmp", "allow-http", "allow-ssl"]
    # Application list entries.
    entries: list[str]  # Auto-flattened from member_table
    # Enable/disable enforcement of protocols over selected ports.
    control_default_network_services: Literal["disable", "enable"]
    # Default network service entries.
    default_network_services: list[str]  # Auto-flattened from member_table
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> ListPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class List:
    """
    Configure application control lists.
    
    Path: application/list
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
    ) -> ListObject: ...
    
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
    ) -> list[ListObject]: ...
    
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
    ) -> ListObject | list[ListObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: ListPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        replacemsg_group: str | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        other_application_action: Literal["pass", "block"] | None = ...,
        app_replacemsg: Literal["disable", "enable"] | None = ...,
        other_application_log: Literal["disable", "enable"] | None = ...,
        enforce_default_app_port: Literal["disable", "enable"] | None = ...,
        force_inclusion_ssl_di_sigs: Literal["disable", "enable"] | None = ...,
        unknown_application_action: Literal["pass", "block"] | None = ...,
        unknown_application_log: Literal["disable", "enable"] | None = ...,
        p2p_block_list: Literal["skype", "edonkey", "bittorrent"] | list[str] | list[dict[str, Any]] | None = ...,
        deep_app_inspection: Literal["disable", "enable"] | None = ...,
        options: Literal["allow-dns", "allow-icmp", "allow-http", "allow-ssl"] | list[str] | list[dict[str, Any]] | None = ...,
        entries: str | list[str] | list[dict[str, Any]] | None = ...,
        control_default_network_services: Literal["disable", "enable"] | None = ...,
        default_network_services: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ListObject: ...
    
    @overload
    def post(
        self,
        payload_dict: ListPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        replacemsg_group: str | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        other_application_action: Literal["pass", "block"] | None = ...,
        app_replacemsg: Literal["disable", "enable"] | None = ...,
        other_application_log: Literal["disable", "enable"] | None = ...,
        enforce_default_app_port: Literal["disable", "enable"] | None = ...,
        force_inclusion_ssl_di_sigs: Literal["disable", "enable"] | None = ...,
        unknown_application_action: Literal["pass", "block"] | None = ...,
        unknown_application_log: Literal["disable", "enable"] | None = ...,
        p2p_block_list: Literal["skype", "edonkey", "bittorrent"] | list[str] | list[dict[str, Any]] | None = ...,
        deep_app_inspection: Literal["disable", "enable"] | None = ...,
        options: Literal["allow-dns", "allow-icmp", "allow-http", "allow-ssl"] | list[str] | list[dict[str, Any]] | None = ...,
        entries: str | list[str] | list[dict[str, Any]] | None = ...,
        control_default_network_services: Literal["disable", "enable"] | None = ...,
        default_network_services: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: ListPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        replacemsg_group: str | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        other_application_action: Literal["pass", "block"] | None = ...,
        app_replacemsg: Literal["disable", "enable"] | None = ...,
        other_application_log: Literal["disable", "enable"] | None = ...,
        enforce_default_app_port: Literal["disable", "enable"] | None = ...,
        force_inclusion_ssl_di_sigs: Literal["disable", "enable"] | None = ...,
        unknown_application_action: Literal["pass", "block"] | None = ...,
        unknown_application_log: Literal["disable", "enable"] | None = ...,
        p2p_block_list: Literal["skype", "edonkey", "bittorrent"] | list[str] | list[dict[str, Any]] | None = ...,
        deep_app_inspection: Literal["disable", "enable"] | None = ...,
        options: Literal["allow-dns", "allow-icmp", "allow-http", "allow-ssl"] | list[str] | list[dict[str, Any]] | None = ...,
        entries: str | list[str] | list[dict[str, Any]] | None = ...,
        control_default_network_services: Literal["disable", "enable"] | None = ...,
        default_network_services: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: ListPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        replacemsg_group: str | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        other_application_action: Literal["pass", "block"] | None = ...,
        app_replacemsg: Literal["disable", "enable"] | None = ...,
        other_application_log: Literal["disable", "enable"] | None = ...,
        enforce_default_app_port: Literal["disable", "enable"] | None = ...,
        force_inclusion_ssl_di_sigs: Literal["disable", "enable"] | None = ...,
        unknown_application_action: Literal["pass", "block"] | None = ...,
        unknown_application_log: Literal["disable", "enable"] | None = ...,
        p2p_block_list: Literal["skype", "edonkey", "bittorrent"] | list[str] | list[dict[str, Any]] | None = ...,
        deep_app_inspection: Literal["disable", "enable"] | None = ...,
        options: Literal["allow-dns", "allow-icmp", "allow-http", "allow-ssl"] | list[str] | list[dict[str, Any]] | None = ...,
        entries: str | list[str] | list[dict[str, Any]] | None = ...,
        control_default_network_services: Literal["disable", "enable"] | None = ...,
        default_network_services: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: ListPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        replacemsg_group: str | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        other_application_action: Literal["pass", "block"] | None = ...,
        app_replacemsg: Literal["disable", "enable"] | None = ...,
        other_application_log: Literal["disable", "enable"] | None = ...,
        enforce_default_app_port: Literal["disable", "enable"] | None = ...,
        force_inclusion_ssl_di_sigs: Literal["disable", "enable"] | None = ...,
        unknown_application_action: Literal["pass", "block"] | None = ...,
        unknown_application_log: Literal["disable", "enable"] | None = ...,
        p2p_block_list: Literal["skype", "edonkey", "bittorrent"] | list[str] | list[dict[str, Any]] | None = ...,
        deep_app_inspection: Literal["disable", "enable"] | None = ...,
        options: Literal["allow-dns", "allow-icmp", "allow-http", "allow-ssl"] | list[str] | list[dict[str, Any]] | None = ...,
        entries: str | list[str] | list[dict[str, Any]] | None = ...,
        control_default_network_services: Literal["disable", "enable"] | None = ...,
        default_network_services: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ListObject: ...
    
    @overload
    def put(
        self,
        payload_dict: ListPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        replacemsg_group: str | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        other_application_action: Literal["pass", "block"] | None = ...,
        app_replacemsg: Literal["disable", "enable"] | None = ...,
        other_application_log: Literal["disable", "enable"] | None = ...,
        enforce_default_app_port: Literal["disable", "enable"] | None = ...,
        force_inclusion_ssl_di_sigs: Literal["disable", "enable"] | None = ...,
        unknown_application_action: Literal["pass", "block"] | None = ...,
        unknown_application_log: Literal["disable", "enable"] | None = ...,
        p2p_block_list: Literal["skype", "edonkey", "bittorrent"] | list[str] | list[dict[str, Any]] | None = ...,
        deep_app_inspection: Literal["disable", "enable"] | None = ...,
        options: Literal["allow-dns", "allow-icmp", "allow-http", "allow-ssl"] | list[str] | list[dict[str, Any]] | None = ...,
        entries: str | list[str] | list[dict[str, Any]] | None = ...,
        control_default_network_services: Literal["disable", "enable"] | None = ...,
        default_network_services: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: ListPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        replacemsg_group: str | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        other_application_action: Literal["pass", "block"] | None = ...,
        app_replacemsg: Literal["disable", "enable"] | None = ...,
        other_application_log: Literal["disable", "enable"] | None = ...,
        enforce_default_app_port: Literal["disable", "enable"] | None = ...,
        force_inclusion_ssl_di_sigs: Literal["disable", "enable"] | None = ...,
        unknown_application_action: Literal["pass", "block"] | None = ...,
        unknown_application_log: Literal["disable", "enable"] | None = ...,
        p2p_block_list: Literal["skype", "edonkey", "bittorrent"] | list[str] | list[dict[str, Any]] | None = ...,
        deep_app_inspection: Literal["disable", "enable"] | None = ...,
        options: Literal["allow-dns", "allow-icmp", "allow-http", "allow-ssl"] | list[str] | list[dict[str, Any]] | None = ...,
        entries: str | list[str] | list[dict[str, Any]] | None = ...,
        control_default_network_services: Literal["disable", "enable"] | None = ...,
        default_network_services: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: ListPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        replacemsg_group: str | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        other_application_action: Literal["pass", "block"] | None = ...,
        app_replacemsg: Literal["disable", "enable"] | None = ...,
        other_application_log: Literal["disable", "enable"] | None = ...,
        enforce_default_app_port: Literal["disable", "enable"] | None = ...,
        force_inclusion_ssl_di_sigs: Literal["disable", "enable"] | None = ...,
        unknown_application_action: Literal["pass", "block"] | None = ...,
        unknown_application_log: Literal["disable", "enable"] | None = ...,
        p2p_block_list: Literal["skype", "edonkey", "bittorrent"] | list[str] | list[dict[str, Any]] | None = ...,
        deep_app_inspection: Literal["disable", "enable"] | None = ...,
        options: Literal["allow-dns", "allow-icmp", "allow-http", "allow-ssl"] | list[str] | list[dict[str, Any]] | None = ...,
        entries: str | list[str] | list[dict[str, Any]] | None = ...,
        control_default_network_services: Literal["disable", "enable"] | None = ...,
        default_network_services: str | list[str] | list[dict[str, Any]] | None = ...,
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
    ) -> ListObject: ...
    
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
        payload_dict: ListPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        replacemsg_group: str | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        other_application_action: Literal["pass", "block"] | None = ...,
        app_replacemsg: Literal["disable", "enable"] | None = ...,
        other_application_log: Literal["disable", "enable"] | None = ...,
        enforce_default_app_port: Literal["disable", "enable"] | None = ...,
        force_inclusion_ssl_di_sigs: Literal["disable", "enable"] | None = ...,
        unknown_application_action: Literal["pass", "block"] | None = ...,
        unknown_application_log: Literal["disable", "enable"] | None = ...,
        p2p_block_list: Literal["skype", "edonkey", "bittorrent"] | list[str] | list[dict[str, Any]] | None = ...,
        deep_app_inspection: Literal["disable", "enable"] | None = ...,
        options: Literal["allow-dns", "allow-icmp", "allow-http", "allow-ssl"] | list[str] | list[dict[str, Any]] | None = ...,
        entries: str | list[str] | list[dict[str, Any]] | None = ...,
        control_default_network_services: Literal["disable", "enable"] | None = ...,
        default_network_services: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "List",
    "ListPayload",
    "ListObject",
]