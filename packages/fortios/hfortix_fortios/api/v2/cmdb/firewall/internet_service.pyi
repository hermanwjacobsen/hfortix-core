from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class InternetServicePayload(TypedDict, total=False):
    """
    Type hints for firewall/internet_service payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: InternetServicePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    id: NotRequired[int]  # Internet Service ID.
    name: NotRequired[str]  # Internet Service name.
    icon_id: NotRequired[int]  # Icon ID of Internet Service.
    direction: NotRequired[Literal["src", "dst", "both"]]  # How this service may be used in a firewall policy (source, d
    database: NotRequired[Literal["isdb", "irdb"]]  # Database name this Internet Service belongs to.
    ip_range_number: NotRequired[int]  # Number of IPv4 ranges.
    extra_ip_range_number: NotRequired[int]  # Extra number of IPv4 ranges.
    ip_number: NotRequired[int]  # Total number of IPv4 addresses.
    ip6_range_number: NotRequired[int]  # Number of IPv6 ranges.
    extra_ip6_range_number: NotRequired[int]  # Extra number of IPv6 ranges.
    singularity: NotRequired[int]  # Singular level of the Internet Service.
    obsolete: NotRequired[int]  # Indicates whether the Internet Service can be used.


class InternetService:
    """
    Show Internet Service application.
    
    Path: firewall/internet_service
    Category: cmdb
    Primary Key: id
    """
    
    def get(
        self,
        id: int | None = ...,
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
        payload_dict: InternetServicePayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        icon_id: int | None = ...,
        direction: Literal["src", "dst", "both"] | None = ...,
        database: Literal["isdb", "irdb"] | None = ...,
        ip_range_number: int | None = ...,
        extra_ip_range_number: int | None = ...,
        ip_number: int | None = ...,
        ip6_range_number: int | None = ...,
        extra_ip6_range_number: int | None = ...,
        singularity: int | None = ...,
        obsolete: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: InternetServicePayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        icon_id: int | None = ...,
        direction: Literal["src", "dst", "both"] | None = ...,
        database: Literal["isdb", "irdb"] | None = ...,
        ip_range_number: int | None = ...,
        extra_ip_range_number: int | None = ...,
        ip_number: int | None = ...,
        ip6_range_number: int | None = ...,
        extra_ip6_range_number: int | None = ...,
        singularity: int | None = ...,
        obsolete: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def exists(
        self,
        id: int,
        vdom: str | bool | None = ...,
    ) -> Union[bool, Coroutine[Any, Any, bool]]: ...
    
    def set(
        self,
        payload_dict: InternetServicePayload | None = ...,
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