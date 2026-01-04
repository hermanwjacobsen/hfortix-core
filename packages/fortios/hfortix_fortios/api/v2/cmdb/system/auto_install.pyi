from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class AutoInstallPayload(TypedDict, total=False):
    """
    Type hints for system/auto_install payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: AutoInstallPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    auto_install_config: NotRequired[Literal["enable", "disable"]]  # Enable/disable auto install the config in USB disk.
    auto_install_image: NotRequired[Literal["enable", "disable"]]  # Enable/disable auto install the image in USB disk.
    default_config_file: NotRequired[str]  # Default config file name in USB disk.
    default_image_file: NotRequired[str]  # Default image file name in USB disk.


class AutoInstall:
    """
    Configure USB auto installation.
    
    Path: system/auto_install
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
        payload_dict: AutoInstallPayload | None = ...,
        auto_install_config: Literal["enable", "disable"] | None = ...,
        auto_install_image: Literal["enable", "disable"] | None = ...,
        default_config_file: str | None = ...,
        default_image_file: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: AutoInstallPayload | None = ...,
        auto_install_config: Literal["enable", "disable"] | None = ...,
        auto_install_image: Literal["enable", "disable"] | None = ...,
        default_config_file: str | None = ...,
        default_image_file: str | None = ...,
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
        payload_dict: AutoInstallPayload | None = ...,
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