from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class Hotspot20H2qpOsuProviderPayload(TypedDict, total=False):
    """
    Type hints for wireless-controller/hotspot20_h2qp_osu_provider payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: Hotspot20H2qpOsuProviderPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # OSU provider ID.
    friendly_name: NotRequired[list[dict[str, Any]]]  # OSU provider friendly name.
    server_uri: NotRequired[str]  # Server URI.
    osu_method: NotRequired[Literal["oma-dm", "soap-xml-spp", "reserved"]]  # OSU method list.
    osu_nai: NotRequired[str]  # OSU NAI.
    service_description: NotRequired[list[dict[str, Any]]]  # OSU service name.
    icon: NotRequired[str]  # OSU provider icon.


class Hotspot20H2qpOsuProvider:
    """
    Configure online sign up (OSU) provider list.
    
    Path: wireless-controller/hotspot20_h2qp_osu_provider
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
        payload_dict: Hotspot20H2qpOsuProviderPayload | None = ...,
        name: str | None = ...,
        friendly_name: list[dict[str, Any]] | None = ...,
        server_uri: str | None = ...,
        osu_method: Literal["oma-dm", "soap-xml-spp", "reserved"] | None = ...,
        osu_nai: str | None = ...,
        service_description: list[dict[str, Any]] | None = ...,
        icon: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: Hotspot20H2qpOsuProviderPayload | None = ...,
        name: str | None = ...,
        friendly_name: list[dict[str, Any]] | None = ...,
        server_uri: str | None = ...,
        osu_method: Literal["oma-dm", "soap-xml-spp", "reserved"] | None = ...,
        osu_nai: str | None = ...,
        service_description: list[dict[str, Any]] | None = ...,
        icon: str | None = ...,
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
        payload_dict: Hotspot20H2qpOsuProviderPayload | None = ...,
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