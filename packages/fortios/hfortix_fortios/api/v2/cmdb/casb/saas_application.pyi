from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class SaasApplicationPayload(TypedDict, total=False):
    """
    Type hints for casb/saas_application payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: SaasApplicationPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # SaaS application name.
    uuid: NotRequired[str]  # Universally Unique Identifier (UUID; automatically assigned 
    status: NotRequired[Literal["enable", "disable"]]  # Enable/disable setting.
    type: NotRequired[Literal["built-in", "customized"]]  # SaaS application type.
    casb_name: NotRequired[str]  # SaaS application signature name.
    description: NotRequired[str]  # SaaS application description.
    domains: NotRequired[list[dict[str, Any]]]  # SaaS application domain list.
    output_attributes: NotRequired[list[dict[str, Any]]]  # SaaS application output attributes.
    input_attributes: NotRequired[list[dict[str, Any]]]  # SaaS application input attributes.


class SaasApplication:
    """
    Configure CASB SaaS application.
    
    Path: casb/saas_application
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
        payload_dict: SaasApplicationPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["built-in", "customized"] | None = ...,
        casb_name: str | None = ...,
        description: str | None = ...,
        domains: list[dict[str, Any]] | None = ...,
        output_attributes: list[dict[str, Any]] | None = ...,
        input_attributes: list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: SaasApplicationPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["built-in", "customized"] | None = ...,
        casb_name: str | None = ...,
        description: str | None = ...,
        domains: list[dict[str, Any]] | None = ...,
        output_attributes: list[dict[str, Any]] | None = ...,
        input_attributes: list[dict[str, Any]] | None = ...,
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
        payload_dict: SaasApplicationPayload | None = ...,
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