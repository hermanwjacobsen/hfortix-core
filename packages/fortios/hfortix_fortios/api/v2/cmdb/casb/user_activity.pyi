from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class UserActivityPayload(TypedDict, total=False):
    """
    Type hints for casb/user_activity payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: UserActivityPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # CASB user activity name.
    uuid: NotRequired[str]  # Universally Unique Identifier (UUID; automatically assigned 
    status: NotRequired[Literal["enable", "disable"]]  # CASB user activity status.
    description: NotRequired[str]  # CASB user activity description.
    type: NotRequired[Literal["built-in", "customized"]]  # CASB user activity type.
    casb_name: NotRequired[str]  # CASB user activity signature name.
    application: str  # CASB SaaS application name.
    category: NotRequired[Literal["activity-control", "tenant-control", "domain-control", "safe-search-control", "advanced-tenant-control", "other"]]  # CASB user activity category.
    match_strategy: NotRequired[Literal["and", "or"]]  # CASB user activity match strategy.
    match: NotRequired[list[dict[str, Any]]]  # CASB user activity match rules.
    control_options: NotRequired[list[dict[str, Any]]]  # CASB control options.


class UserActivity:
    """
    Configure CASB user activity.
    
    Path: casb/user_activity
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
        payload_dict: UserActivityPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        description: str | None = ...,
        type: Literal["built-in", "customized"] | None = ...,
        casb_name: str | None = ...,
        application: str | None = ...,
        category: Literal["activity-control", "tenant-control", "domain-control", "safe-search-control", "advanced-tenant-control", "other"] | None = ...,
        match_strategy: Literal["and", "or"] | None = ...,
        match: list[dict[str, Any]] | None = ...,
        control_options: list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: UserActivityPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        description: str | None = ...,
        type: Literal["built-in", "customized"] | None = ...,
        casb_name: str | None = ...,
        application: str | None = ...,
        category: Literal["activity-control", "tenant-control", "domain-control", "safe-search-control", "advanced-tenant-control", "other"] | None = ...,
        match_strategy: Literal["and", "or"] | None = ...,
        match: list[dict[str, Any]] | None = ...,
        control_options: list[dict[str, Any]] | None = ...,
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
        payload_dict: UserActivityPayload | None = ...,
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