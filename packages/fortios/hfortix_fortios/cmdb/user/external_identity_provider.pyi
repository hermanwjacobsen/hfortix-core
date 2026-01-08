from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class ExternalIdentityProviderPayload(TypedDict, total=False):
    """
    Type hints for user/external_identity_provider payload fields.
    
    Configure external identity provider.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: interface)

    **Usage:**
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


class ExternalIdentityProviderObject(FortiObject[ExternalIdentityProviderPayload]):
    """Typed FortiObject for user/external_identity_provider with IDE autocomplete support."""
    
    # External identity provider name.
    name: str
    # External identity provider type.
    type: Literal["ms-graph"]
    # External identity API version.
    version: Literal["v1.0", "beta"]
    # External identity provider URL (e.g. "https://example.com:8080/api/v1").
    url: str
    # User attribute name in authentication query.
    user_attr_name: str
    # Group attribute name in authentication query.
    group_attr_name: str
    # External identity provider service port number (0 to use default).
    port: int
    # Use this IPv4/v6 address to connect to the external identity provider.
    source_ip: str
    # Specify how to select outgoing interface to reach server.
    interface_select_method: Literal["auto", "sdwan", "specify"]
    # Specify outgoing interface to reach server.
    interface: str
    # VRF ID used for connection to server.
    vrf_select: int
    # Enable/disable server's identity check against its certificate and subject alter
    server_identity_check: Literal["disable", "enable"]
    # Connection timeout value in seconds (default=5).
    timeout: int
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> ExternalIdentityProviderPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class ExternalIdentityProvider:
    """
    Configure external identity provider.
    
    Path: user/external_identity_provider
    Category: cmdb
    Primary Key: name
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey provided)
    @overload
    def get(
        self,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        *,
        response_mode: Literal["object"],
        **kwargs: Any,
    ) -> ExternalIdentityProviderObject: ...
    
    # List of objects (no mkey provided - most specific for list returns)
    # For singleton endpoints (no mkey), returns single object; for table endpoints, returns list
    @overload
    def get(
        self,
        *,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"],
        **kwargs: Any,
    ) -> list[ExternalIdentityProviderObject]: ...
    
    @overload
    def get(
        self,
        name: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True],
        *,
        response_mode: Literal["object"],
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Dict mode with mkey provided (single dict)
    @overload
    def get(
        self,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Dict mode without mkey (returns dict with results array)
    @overload
    def get(
        self,
        name: None = None,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Default overload for dict mode
    @overload
    def get(
        self,
        name: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], list[dict[str, Any]]]: ...
    
    def get(
        self,
        name: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: str | None = ...,
        **kwargs: Any,
    ) -> ExternalIdentityProviderObject | list[ExternalIdentityProviderObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ExternalIdentityProviderObject: ...
    
    @overload
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
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
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
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
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ExternalIdentityProviderObject: ...
    
    @overload
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
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
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
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
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ExternalIdentityProviderObject: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
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
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
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
    "ExternalIdentityProvider",
    "ExternalIdentityProviderPayload",
    "ExternalIdentityProviderObject",
]