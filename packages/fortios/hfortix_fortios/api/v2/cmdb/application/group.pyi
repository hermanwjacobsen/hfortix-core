from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class GroupPayload(TypedDict, total=False):
    """
    Type hints for application/group payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: GroupPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Application group name.
    comment: NotRequired[str]  # Comments.
    type: NotRequired[Literal["application", "filter"]]  # Application group type.
    application: NotRequired[list[dict[str, Any]]]  # Application ID list.
    category: NotRequired[list[dict[str, Any]]]  # Application category ID list.
    risk: NotRequired[list[dict[str, Any]]]  # Risk, or impact, of allowing traffic from this application t
    protocols: NotRequired[str]  # Application protocol filter.
    vendor: NotRequired[str]  # Application vendor filter.
    technology: NotRequired[str]  # Application technology filter.
    behavior: NotRequired[str]  # Application behavior filter.
    popularity: NotRequired[Literal["1", "2", "3", "4", "5"]]  # Application popularity filter (1 - 5, from least to most pop


class Group:
    """
    Configure firewall application groups.
    
    Path: application/group
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
        payload_dict: GroupPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        type: Literal["application", "filter"] | None = ...,
        application: list[dict[str, Any]] | None = ...,
        category: list[dict[str, Any]] | None = ...,
        risk: list[dict[str, Any]] | None = ...,
        protocols: str | None = ...,
        vendor: str | None = ...,
        technology: str | None = ...,
        behavior: str | None = ...,
        popularity: Literal["1", "2", "3", "4", "5"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: GroupPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        type: Literal["application", "filter"] | None = ...,
        application: list[dict[str, Any]] | None = ...,
        category: list[dict[str, Any]] | None = ...,
        risk: list[dict[str, Any]] | None = ...,
        protocols: str | None = ...,
        vendor: str | None = ...,
        technology: str | None = ...,
        behavior: str | None = ...,
        popularity: Literal["1", "2", "3", "4", "5"] | None = ...,
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
        payload_dict: GroupPayload | None = ...,
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