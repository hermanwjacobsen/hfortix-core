from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class ListPayload(TypedDict, total=False):
    """
    Type hints for application/list payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
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


class List:
    """
    Configure application control lists.
    
    Path: application/list
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
        p2p_block_list: Literal["skype", "edonkey", "bittorrent"] | None = ...,
        deep_app_inspection: Literal["disable", "enable"] | None = ...,
        options: Literal["allow-dns", "allow-icmp", "allow-http", "allow-ssl"] | None = ...,
        entries: list[dict[str, Any]] | None = ...,
        control_default_network_services: Literal["disable", "enable"] | None = ...,
        default_network_services: list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
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
        p2p_block_list: Literal["skype", "edonkey", "bittorrent"] | None = ...,
        deep_app_inspection: Literal["disable", "enable"] | None = ...,
        options: Literal["allow-dns", "allow-icmp", "allow-http", "allow-ssl"] | None = ...,
        entries: list[dict[str, Any]] | None = ...,
        control_default_network_services: Literal["disable", "enable"] | None = ...,
        default_network_services: list[dict[str, Any]] | None = ...,
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
        payload_dict: ListPayload | None = ...,
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