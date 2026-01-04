from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class ApiUserPayload(TypedDict, total=False):
    """
    Type hints for system/api_user payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: ApiUserPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # User name.
    comments: NotRequired[str]  # Comment.
    api_key: NotRequired[str]  # Admin user password.
    accprofile: str  # Admin user access profile.
    vdom: NotRequired[list[dict[str, Any]]]  # Virtual domains.
    schedule: NotRequired[str]  # Schedule name.
    cors_allow_origin: NotRequired[str]  # Value for Access-Control-Allow-Origin on API responses. Avoi
    peer_auth: NotRequired[Literal["enable", "disable"]]  # Enable/disable peer authentication.
    peer_group: str  # Peer group name.
    trusthost: NotRequired[list[dict[str, Any]]]  # Trusthost.


class ApiUser:
    """
    Configure API users.
    
    Path: system/api_user
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
        payload_dict: ApiUserPayload | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        api_key: str | None = ...,
        accprofile: str | None = ...,
        schedule: str | None = ...,
        cors_allow_origin: str | None = ...,
        peer_auth: Literal["enable", "disable"] | None = ...,
        peer_group: str | None = ...,
        trusthost: list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: ApiUserPayload | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        api_key: str | None = ...,
        accprofile: str | None = ...,
        schedule: str | None = ...,
        cors_allow_origin: str | None = ...,
        peer_auth: Literal["enable", "disable"] | None = ...,
        peer_group: str | None = ...,
        trusthost: list[dict[str, Any]] | None = ...,
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
        payload_dict: ApiUserPayload | None = ...,
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