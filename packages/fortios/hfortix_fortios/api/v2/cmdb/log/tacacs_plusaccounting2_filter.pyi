from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class TacacsPlusaccounting2FilterPayload(TypedDict, total=False):
    """
    Type hints for log/tacacs_plusaccounting2_filter payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: TacacsPlusaccounting2FilterPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    login_audit: NotRequired[Literal["enable", "disable"]]  # Enable/disable TACACS+ accounting for login events audit.
    config_change_audit: NotRequired[Literal["enable", "disable"]]  # Enable/disable TACACS+ accounting for configuration change e
    cli_cmd_audit: NotRequired[Literal["enable", "disable"]]  # Enable/disable TACACS+ accounting for CLI commands audit.


class TacacsPlusaccounting2Filter:
    """
    Settings for TACACS+ accounting events filter.
    
    Path: log/tacacs_plusaccounting2_filter
    Category: cmdb
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
        payload_dict: TacacsPlusaccounting2FilterPayload | None = ...,
        login_audit: Literal["enable", "disable"] | None = ...,
        config_change_audit: Literal["enable", "disable"] | None = ...,
        cli_cmd_audit: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: TacacsPlusaccounting2FilterPayload | None = ...,
        login_audit: Literal["enable", "disable"] | None = ...,
        config_change_audit: Literal["enable", "disable"] | None = ...,
        cli_cmd_audit: Literal["enable", "disable"] | None = ...,
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
        payload_dict: TacacsPlusaccounting2FilterPayload | None = ...,
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