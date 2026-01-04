from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class MpskProfilePayload(TypedDict, total=False):
    """
    Type hints for wireless_controller/mpsk_profile payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: MpskProfilePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # MPSK profile name.
    mpsk_concurrent_clients: NotRequired[int]  # Maximum number of concurrent clients that connect using the 
    mpsk_external_server_auth: NotRequired[Literal["enable", "disable"]]  # Enable/Disable MPSK external server authentication (default 
    mpsk_external_server: NotRequired[str]  # RADIUS server to be used to authenticate MPSK users.
    mpsk_type: NotRequired[Literal["wpa2-personal", "wpa3-sae", "wpa3-sae-transition"]]  # Select the security type of keys for this profile.
    mpsk_group: NotRequired[list[dict[str, Any]]]  # List of multiple PSK groups.


class MpskProfile:
    """
    Configure MPSK profile.
    
    Path: wireless_controller/mpsk_profile
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
        payload_dict: MpskProfilePayload | None = ...,
        name: str | None = ...,
        mpsk_concurrent_clients: int | None = ...,
        mpsk_external_server_auth: Literal["enable", "disable"] | None = ...,
        mpsk_external_server: str | None = ...,
        mpsk_type: Literal["wpa2-personal", "wpa3-sae", "wpa3-sae-transition"] | None = ...,
        mpsk_group: list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: MpskProfilePayload | None = ...,
        name: str | None = ...,
        mpsk_concurrent_clients: int | None = ...,
        mpsk_external_server_auth: Literal["enable", "disable"] | None = ...,
        mpsk_external_server: str | None = ...,
        mpsk_type: Literal["wpa2-personal", "wpa3-sae", "wpa3-sae-transition"] | None = ...,
        mpsk_group: list[dict[str, Any]] | None = ...,
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
        payload_dict: MpskProfilePayload | None = ...,
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