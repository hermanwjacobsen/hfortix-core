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
    status: NotRequired[Literal[{"description": "Enable setting", "help": "Enable setting.", "label": "Enable", "name": "enable"}, {"description": "Disable setting", "help": "Disable setting.", "label": "Disable", "name": "disable"}]]  # CASB user activity status.
    description: NotRequired[str]  # CASB user activity description.
    type: NotRequired[Literal[{"description": "Built-in CASB user-activity", "help": "Built-in CASB user-activity.", "label": "Built In", "name": "built-in"}, {"description": "User customized CASB user-activity", "help": "User customized CASB user-activity.", "label": "Customized", "name": "customized"}]]  # CASB user activity type.
    casb_name: NotRequired[str]  # CASB user activity signature name.
    application: str  # CASB SaaS application name.
    category: NotRequired[Literal[{"description": "Activity control", "help": "Activity control.", "label": "Activity Control", "name": "activity-control"}, {"description": "Tenant control", "help": "Tenant control.", "label": "Tenant Control", "name": "tenant-control"}, {"description": "Domain control", "help": "Domain control.", "label": "Domain Control", "name": "domain-control"}, {"description": "Safe search control", "help": "Safe search control.", "label": "Safe Search Control", "name": "safe-search-control"}, {"description": "Advanced tenant control", "help": "Advanced tenant control.", "label": "Advanced Tenant Control", "name": "advanced-tenant-control"}, {"description": "User customized category", "help": "User customized category.", "label": "Other", "name": "other"}]]  # CASB user activity category.
    match_strategy: NotRequired[Literal[{"description": "Match user activity using a logical AND operator", "help": "Match user activity using a logical AND operator.", "label": "And", "name": "and"}, {"description": "Match user activity using a logical OR operator", "help": "Match user activity using a logical OR operator.", "label": "Or", "name": "or"}]]  # CASB user activity match strategy.
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
        status: Literal[{"description": "Enable setting", "help": "Enable setting.", "label": "Enable", "name": "enable"}, {"description": "Disable setting", "help": "Disable setting.", "label": "Disable", "name": "disable"}] | None = ...,
        description: str | None = ...,
        type: Literal[{"description": "Built-in CASB user-activity", "help": "Built-in CASB user-activity.", "label": "Built In", "name": "built-in"}, {"description": "User customized CASB user-activity", "help": "User customized CASB user-activity.", "label": "Customized", "name": "customized"}] | None = ...,
        casb_name: str | None = ...,
        application: str | None = ...,
        category: Literal[{"description": "Activity control", "help": "Activity control.", "label": "Activity Control", "name": "activity-control"}, {"description": "Tenant control", "help": "Tenant control.", "label": "Tenant Control", "name": "tenant-control"}, {"description": "Domain control", "help": "Domain control.", "label": "Domain Control", "name": "domain-control"}, {"description": "Safe search control", "help": "Safe search control.", "label": "Safe Search Control", "name": "safe-search-control"}, {"description": "Advanced tenant control", "help": "Advanced tenant control.", "label": "Advanced Tenant Control", "name": "advanced-tenant-control"}, {"description": "User customized category", "help": "User customized category.", "label": "Other", "name": "other"}] | None = ...,
        match_strategy: Literal[{"description": "Match user activity using a logical AND operator", "help": "Match user activity using a logical AND operator.", "label": "And", "name": "and"}, {"description": "Match user activity using a logical OR operator", "help": "Match user activity using a logical OR operator.", "label": "Or", "name": "or"}] | None = ...,
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
        status: Literal[{"description": "Enable setting", "help": "Enable setting.", "label": "Enable", "name": "enable"}, {"description": "Disable setting", "help": "Disable setting.", "label": "Disable", "name": "disable"}] | None = ...,
        description: str | None = ...,
        type: Literal[{"description": "Built-in CASB user-activity", "help": "Built-in CASB user-activity.", "label": "Built In", "name": "built-in"}, {"description": "User customized CASB user-activity", "help": "User customized CASB user-activity.", "label": "Customized", "name": "customized"}] | None = ...,
        casb_name: str | None = ...,
        application: str | None = ...,
        category: Literal[{"description": "Activity control", "help": "Activity control.", "label": "Activity Control", "name": "activity-control"}, {"description": "Tenant control", "help": "Tenant control.", "label": "Tenant Control", "name": "tenant-control"}, {"description": "Domain control", "help": "Domain control.", "label": "Domain Control", "name": "domain-control"}, {"description": "Safe search control", "help": "Safe search control.", "label": "Safe Search Control", "name": "safe-search-control"}, {"description": "Advanced tenant control", "help": "Advanced tenant control.", "label": "Advanced Tenant Control", "name": "advanced-tenant-control"}, {"description": "User customized category", "help": "User customized category.", "label": "Other", "name": "other"}] | None = ...,
        match_strategy: Literal[{"description": "Match user activity using a logical AND operator", "help": "Match user activity using a logical AND operator.", "label": "And", "name": "and"}, {"description": "Match user activity using a logical OR operator", "help": "Match user activity using a logical OR operator.", "label": "Or", "name": "or"}] | None = ...,
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


__all__ = [
    "UserActivity",
    "UserActivityPayload",
]