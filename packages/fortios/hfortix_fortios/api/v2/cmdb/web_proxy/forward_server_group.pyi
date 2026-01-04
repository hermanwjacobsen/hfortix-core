from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class ForwardServerGroupPayload(TypedDict, total=False):
    """
    Type hints for web_proxy/forward_server_group payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: ForwardServerGroupPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Configure a forward server group consisting one or multiple 
    affinity: NotRequired[Literal["enable", "disable"]]  # Enable/disable affinity, attaching a source-ip's traffic to 
    ldb_method: NotRequired[Literal["weighted", "least-session", "active-passive"]]  # Load balance method: weighted or least-session.
    group_down_option: NotRequired[Literal["block", "pass"]]  # Action to take when all of the servers in the forward server
    server_list: NotRequired[list[dict[str, Any]]]  # Add web forward servers to a list to form a server group. Op


class ForwardServerGroup:
    """
    Configure a forward server group consisting or multiple forward servers. Supports failover and load balancing.
    
    Path: web_proxy/forward_server_group
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
        payload_dict: ForwardServerGroupPayload | None = ...,
        name: str | None = ...,
        affinity: Literal["enable", "disable"] | None = ...,
        ldb_method: Literal["weighted", "least-session", "active-passive"] | None = ...,
        group_down_option: Literal["block", "pass"] | None = ...,
        server_list: list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: ForwardServerGroupPayload | None = ...,
        name: str | None = ...,
        affinity: Literal["enable", "disable"] | None = ...,
        ldb_method: Literal["weighted", "least-session", "active-passive"] | None = ...,
        group_down_option: Literal["block", "pass"] | None = ...,
        server_list: list[dict[str, Any]] | None = ...,
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
        payload_dict: ForwardServerGroupPayload | None = ...,
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