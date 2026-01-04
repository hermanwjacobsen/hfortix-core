from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class ExternalIdentityProviderPayload(TypedDict, total=False):
    """
    Type hints for user/external_identity_provider payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: ExternalIdentityProviderPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # External identity provider name.
    type: Literal["ms-graph"]  # External identity provider type.
    version: NotRequired[Literal["v1.0", "beta"]]  # External identity API version.
    url: NotRequired[str]  # External identity provider URL (e.g. "https://example.com:80
    user_attr_name: NotRequired[str]  # User attribute name in authentication query.
    group_attr_name: NotRequired[str]  # Group attribute name in authentication query.
    port: NotRequired[int]  # External identity provider service port number (0 to use def
    source_ip: NotRequired[str]  # Use this IPv4/v6 address to connect to the external identity
    interface_select_method: NotRequired[Literal["auto", "sdwan", "specify"]]  # Specify how to select outgoing interface to reach server.
    interface: str  # Specify outgoing interface to reach server.
    vrf_select: NotRequired[int]  # VRF ID used for connection to server.
    server_identity_check: NotRequired[Literal["disable", "enable"]]  # Enable/disable server's identity check against its certifica
    timeout: NotRequired[int]  # Connection timeout value in seconds (default=5).


class ExternalIdentityProvider:
    """
    Configure external identity provider.
    
    Path: user/external_identity_provider
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
        payload_dict: ExternalIdentityProviderPayload | None = ...,
        name: str | None = ...,
        type: Literal["ms-graph"] | None = ...,
        version: Literal["v1.0", "beta"] | None = ...,
        url: str | None = ...,
        user_attr_name: str | None = ...,
        group_attr_name: str | None = ...,
        port: int | None = ...,
        source_ip: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        server_identity_check: Literal["disable", "enable"] | None = ...,
        timeout: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: ExternalIdentityProviderPayload | None = ...,
        name: str | None = ...,
        type: Literal["ms-graph"] | None = ...,
        version: Literal["v1.0", "beta"] | None = ...,
        url: str | None = ...,
        user_attr_name: str | None = ...,
        group_attr_name: str | None = ...,
        port: int | None = ...,
        source_ip: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        server_identity_check: Literal["disable", "enable"] | None = ...,
        timeout: int | None = ...,
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
        payload_dict: ExternalIdentityProviderPayload | None = ...,
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