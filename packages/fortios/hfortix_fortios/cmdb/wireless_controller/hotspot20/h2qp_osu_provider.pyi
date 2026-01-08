from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class H2qpOsuProviderPayload(TypedDict, total=False):
    """
    Type hints for wireless_controller/hotspot20/h2qp_osu_provider payload fields.
    
    Configure online sign up (OSU) provider list.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.wireless-controller.hotspot20.icon.IconEndpoint` (via: icon)

    **Usage:**
        payload: H2qpOsuProviderPayload = {
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


class H2qpOsuProviderObject(FortiObject[H2qpOsuProviderPayload]):
    """Typed FortiObject for wireless_controller/hotspot20/h2qp_osu_provider with IDE autocomplete support."""
    
    # OSU provider ID.
    name: str
    # OSU provider friendly name.
    friendly_name: list[str]  # Auto-flattened from member_table
    # Server URI.
    server_uri: str
    # OSU method list.
    osu_method: Literal["oma-dm", "soap-xml-spp", "reserved"]
    # OSU NAI.
    osu_nai: str
    # OSU service name.
    service_description: list[str]  # Auto-flattened from member_table
    # OSU provider icon.
    icon: str
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> H2qpOsuProviderPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class H2qpOsuProvider:
    """
    Configure online sign up (OSU) provider list.
    
    Path: wireless_controller/hotspot20/h2qp_osu_provider
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
    ) -> H2qpOsuProviderObject: ...
    
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
    ) -> list[H2qpOsuProviderObject]: ...
    
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
    ) -> H2qpOsuProviderObject | list[H2qpOsuProviderObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: H2qpOsuProviderPayload | None = ...,
        name: str | None = ...,
        friendly_name: str | list[str] | list[dict[str, Any]] | None = ...,
        server_uri: str | None = ...,
        osu_method: Literal["oma-dm", "soap-xml-spp", "reserved"] | list[str] | list[dict[str, Any]] | None = ...,
        osu_nai: str | None = ...,
        service_description: str | list[str] | list[dict[str, Any]] | None = ...,
        icon: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> H2qpOsuProviderObject: ...
    
    @overload
    def post(
        self,
        payload_dict: H2qpOsuProviderPayload | None = ...,
        name: str | None = ...,
        friendly_name: str | list[str] | list[dict[str, Any]] | None = ...,
        server_uri: str | None = ...,
        osu_method: Literal["oma-dm", "soap-xml-spp", "reserved"] | list[str] | list[dict[str, Any]] | None = ...,
        osu_nai: str | None = ...,
        service_description: str | list[str] | list[dict[str, Any]] | None = ...,
        icon: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: H2qpOsuProviderPayload | None = ...,
        name: str | None = ...,
        friendly_name: str | list[str] | list[dict[str, Any]] | None = ...,
        server_uri: str | None = ...,
        osu_method: Literal["oma-dm", "soap-xml-spp", "reserved"] | list[str] | list[dict[str, Any]] | None = ...,
        osu_nai: str | None = ...,
        service_description: str | list[str] | list[dict[str, Any]] | None = ...,
        icon: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: H2qpOsuProviderPayload | None = ...,
        name: str | None = ...,
        friendly_name: str | list[str] | list[dict[str, Any]] | None = ...,
        server_uri: str | None = ...,
        osu_method: Literal["oma-dm", "soap-xml-spp", "reserved"] | list[str] | list[dict[str, Any]] | None = ...,
        osu_nai: str | None = ...,
        service_description: str | list[str] | list[dict[str, Any]] | None = ...,
        icon: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: H2qpOsuProviderPayload | None = ...,
        name: str | None = ...,
        friendly_name: str | list[str] | list[dict[str, Any]] | None = ...,
        server_uri: str | None = ...,
        osu_method: Literal["oma-dm", "soap-xml-spp", "reserved"] | list[str] | list[dict[str, Any]] | None = ...,
        osu_nai: str | None = ...,
        service_description: str | list[str] | list[dict[str, Any]] | None = ...,
        icon: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> H2qpOsuProviderObject: ...
    
    @overload
    def put(
        self,
        payload_dict: H2qpOsuProviderPayload | None = ...,
        name: str | None = ...,
        friendly_name: str | list[str] | list[dict[str, Any]] | None = ...,
        server_uri: str | None = ...,
        osu_method: Literal["oma-dm", "soap-xml-spp", "reserved"] | list[str] | list[dict[str, Any]] | None = ...,
        osu_nai: str | None = ...,
        service_description: str | list[str] | list[dict[str, Any]] | None = ...,
        icon: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: H2qpOsuProviderPayload | None = ...,
        name: str | None = ...,
        friendly_name: str | list[str] | list[dict[str, Any]] | None = ...,
        server_uri: str | None = ...,
        osu_method: Literal["oma-dm", "soap-xml-spp", "reserved"] | list[str] | list[dict[str, Any]] | None = ...,
        osu_nai: str | None = ...,
        service_description: str | list[str] | list[dict[str, Any]] | None = ...,
        icon: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: H2qpOsuProviderPayload | None = ...,
        name: str | None = ...,
        friendly_name: str | list[str] | list[dict[str, Any]] | None = ...,
        server_uri: str | None = ...,
        osu_method: Literal["oma-dm", "soap-xml-spp", "reserved"] | list[str] | list[dict[str, Any]] | None = ...,
        osu_nai: str | None = ...,
        service_description: str | list[str] | list[dict[str, Any]] | None = ...,
        icon: str | None = ...,
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
    ) -> H2qpOsuProviderObject: ...
    
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
        payload_dict: H2qpOsuProviderPayload | None = ...,
        name: str | None = ...,
        friendly_name: str | list[str] | list[dict[str, Any]] | None = ...,
        server_uri: str | None = ...,
        osu_method: Literal["oma-dm", "soap-xml-spp", "reserved"] | list[str] | list[dict[str, Any]] | None = ...,
        osu_nai: str | None = ...,
        service_description: str | list[str] | list[dict[str, Any]] | None = ...,
        icon: str | None = ...,
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
    "H2qpOsuProvider",
    "H2qpOsuProviderPayload",
    "H2qpOsuProviderObject",
]