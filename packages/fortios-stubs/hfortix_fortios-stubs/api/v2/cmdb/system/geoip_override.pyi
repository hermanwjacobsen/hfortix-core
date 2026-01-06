from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class GeoipOverridePayload(TypedDict, total=False):
    """
    Type hints for system/geoip_override payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: GeoipOverridePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Location name.
    description: NotRequired[str]  # Description.
    country_id: NotRequired[str]  # Two character Country ID code.
    ip_range: NotRequired[list[dict[str, Any]]]  # Table of IP ranges assigned to country.
    ip6_range: NotRequired[list[dict[str, Any]]]  # Table of IPv6 ranges assigned to country.


class GeoipOverride:
    """
    Configure geographical location mapping for IP address(es) to override mappings from FortiGuard.
    
    Path: system/geoip_override
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
        payload_dict: GeoipOverridePayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        country_id: str | None = ...,
        ip_range: list[dict[str, Any]] | None = ...,
        ip6_range: list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: GeoipOverridePayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        country_id: str | None = ...,
        ip_range: list[dict[str, Any]] | None = ...,
        ip6_range: list[dict[str, Any]] | None = ...,
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
        payload_dict: GeoipOverridePayload | None = ...,
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


__all__ = [
    "GeoipOverride",
    "GeoipOverridePayload",
]