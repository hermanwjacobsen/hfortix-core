from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class SettingsPayload(TypedDict, total=False):
    """
    Type hints for antivirus/settings payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: SettingsPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    machine_learning_detection: NotRequired[Literal["enable", "monitor", "disable"]]  # Use machine learning based malware detection.
    use_extreme_db: NotRequired[Literal["enable", "disable"]]  # Enable/disable the use of Extreme AVDB.
    grayware: NotRequired[Literal["enable", "disable"]]  # Enable/disable grayware detection when an AntiVirus profile 
    override_timeout: NotRequired[int]  # Override the large file scan timeout value in seconds (30 - 
    cache_infected_result: NotRequired[Literal["enable", "disable"]]  # Enable/disable cache of infected scan results (default = ena


class Settings:
    """
    Configure AntiVirus settings.
    
    Path: antivirus/settings
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
        payload_dict: SettingsPayload | None = ...,
        machine_learning_detection: Literal["enable", "monitor", "disable"] | None = ...,
        use_extreme_db: Literal["enable", "disable"] | None = ...,
        grayware: Literal["enable", "disable"] | None = ...,
        override_timeout: int | None = ...,
        cache_infected_result: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: SettingsPayload | None = ...,
        machine_learning_detection: Literal["enable", "monitor", "disable"] | None = ...,
        use_extreme_db: Literal["enable", "disable"] | None = ...,
        grayware: Literal["enable", "disable"] | None = ...,
        override_timeout: int | None = ...,
        cache_infected_result: Literal["enable", "disable"] | None = ...,
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
        payload_dict: SettingsPayload | None = ...,
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