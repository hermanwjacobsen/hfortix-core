from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class FtgdLocalRatingPayload(TypedDict, total=False):
    """
    Type hints for webfilter/ftgd_local_rating payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: FtgdLocalRatingPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    url: str  # URL to rate locally.
    status: NotRequired[Literal["enable", "disable"]]  # Enable/disable local rating.
    comment: NotRequired[str]  # Comment.
    rating: str  # Local rating.


class FtgdLocalRating:
    """
    Configure local FortiGuard Web Filter local ratings.
    
    Path: webfilter/ftgd_local_rating
    Category: cmdb
    Primary Key: url
    """
    
    def get(
        self,
        url: str | None = ...,
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
        payload_dict: FtgdLocalRatingPayload | None = ...,
        url: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        comment: str | None = ...,
        rating: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: FtgdLocalRatingPayload | None = ...,
        url: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        comment: str | None = ...,
        rating: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def delete(
        self,
        url: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def exists(
        self,
        url: str,
        vdom: str | bool | None = ...,
    ) -> Union[bool, Coroutine[Any, Any, bool]]: ...
    
    def set(
        self,
        payload_dict: FtgdLocalRatingPayload | None = ...,
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