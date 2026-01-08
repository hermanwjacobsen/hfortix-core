from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class InternetServiceNamePayload(TypedDict, total=False):
    """
    Type hints for firewall/internet_service_name payload fields.
    
    Define internet service names.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.firewall.city.CityEndpoint` (via: city-id)
        - :class:`~.firewall.country.CountryEndpoint` (via: country-id)
        - :class:`~.firewall.internet-service.InternetServiceEndpoint` (via: internet-service-id)
        - :class:`~.firewall.region.RegionEndpoint` (via: region-id)

    **Usage:**
        payload: InternetServiceNamePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Internet Service name.
    type: NotRequired[Literal["default", "location"]]  # Internet Service name type.
    internet_service_id: int  # Internet Service ID.
    country_id: NotRequired[int]  # Country or Area ID.
    region_id: NotRequired[int]  # Region ID.
    city_id: NotRequired[int]  # City ID.


class InternetServiceNameObject(FortiObject[InternetServiceNamePayload]):
    """Typed FortiObject for firewall/internet_service_name with IDE autocomplete support."""
    
    # Internet Service name.
    name: str
    # Internet Service name type.
    type: Literal["default", "location"]
    # Internet Service ID.
    internet_service_id: int
    # Country or Area ID.
    country_id: int
    # Region ID.
    region_id: int
    # City ID.
    city_id: int
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> InternetServiceNamePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class InternetServiceName:
    """
    Define internet service names.
    
    Path: firewall/internet_service_name
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
    ) -> InternetServiceNameObject: ...
    
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
    ) -> list[InternetServiceNameObject]: ...
    
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
    ) -> InternetServiceNameObject | list[InternetServiceNameObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: InternetServiceNamePayload | None = ...,
        name: str | None = ...,
        type: Literal["default", "location"] | None = ...,
        internet_service_id: int | None = ...,
        country_id: int | None = ...,
        region_id: int | None = ...,
        city_id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> InternetServiceNameObject: ...
    
    @overload
    def post(
        self,
        payload_dict: InternetServiceNamePayload | None = ...,
        name: str | None = ...,
        type: Literal["default", "location"] | None = ...,
        internet_service_id: int | None = ...,
        country_id: int | None = ...,
        region_id: int | None = ...,
        city_id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: InternetServiceNamePayload | None = ...,
        name: str | None = ...,
        type: Literal["default", "location"] | None = ...,
        internet_service_id: int | None = ...,
        country_id: int | None = ...,
        region_id: int | None = ...,
        city_id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: InternetServiceNamePayload | None = ...,
        name: str | None = ...,
        type: Literal["default", "location"] | None = ...,
        internet_service_id: int | None = ...,
        country_id: int | None = ...,
        region_id: int | None = ...,
        city_id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: InternetServiceNamePayload | None = ...,
        name: str | None = ...,
        type: Literal["default", "location"] | None = ...,
        internet_service_id: int | None = ...,
        country_id: int | None = ...,
        region_id: int | None = ...,
        city_id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> InternetServiceNameObject: ...
    
    @overload
    def put(
        self,
        payload_dict: InternetServiceNamePayload | None = ...,
        name: str | None = ...,
        type: Literal["default", "location"] | None = ...,
        internet_service_id: int | None = ...,
        country_id: int | None = ...,
        region_id: int | None = ...,
        city_id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: InternetServiceNamePayload | None = ...,
        name: str | None = ...,
        type: Literal["default", "location"] | None = ...,
        internet_service_id: int | None = ...,
        country_id: int | None = ...,
        region_id: int | None = ...,
        city_id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: InternetServiceNamePayload | None = ...,
        name: str | None = ...,
        type: Literal["default", "location"] | None = ...,
        internet_service_id: int | None = ...,
        country_id: int | None = ...,
        region_id: int | None = ...,
        city_id: int | None = ...,
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
    ) -> InternetServiceNameObject: ...
    
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
        payload_dict: InternetServiceNamePayload | None = ...,
        name: str | None = ...,
        type: Literal["default", "location"] | None = ...,
        internet_service_id: int | None = ...,
        country_id: int | None = ...,
        region_id: int | None = ...,
        city_id: int | None = ...,
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
    "InternetServiceName",
    "InternetServiceNamePayload",
    "InternetServiceNameObject",
]