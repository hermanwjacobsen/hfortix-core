from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class ProfilePayload(TypedDict, total=False):
    """
    Type hints for web_proxy/profile payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: ProfilePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Profile name.
    header_client_ip: NotRequired[Literal["pass", "add", "remove"]]  # Action to take on the HTTP client-IP header in forwarded req
    header_via_request: NotRequired[Literal["pass", "add", "remove"]]  # Action to take on the HTTP via header in forwarded requests:
    header_via_response: NotRequired[Literal["pass", "add", "remove"]]  # Action to take on the HTTP via header in forwarded responses
    header_x_forwarded_for: NotRequired[Literal["pass", "add", "remove"]]  # Action to take on the HTTP x-forwarded-for header in forward
    header_x_forwarded_client_cert: NotRequired[Literal["pass", "add", "remove"]]  # Action to take on the HTTP x-forwarded-client-cert header in
    header_front_end_https: NotRequired[Literal["pass", "add", "remove"]]  # Action to take on the HTTP front-end-HTTPS header in forward
    header_x_authenticated_user: NotRequired[Literal["pass", "add", "remove"]]  # Action to take on the HTTP x-authenticated-user header in fo
    header_x_authenticated_groups: NotRequired[Literal["pass", "add", "remove"]]  # Action to take on the HTTP x-authenticated-groups header in 
    strip_encoding: NotRequired[Literal["enable", "disable"]]  # Enable/disable stripping unsupported encoding from the reque
    log_header_change: NotRequired[Literal["enable", "disable"]]  # Enable/disable logging HTTP header changes.
    headers: NotRequired[list[dict[str, Any]]]  # Configure HTTP forwarded requests headers.


class Profile:
    """
    Configure web proxy profiles.
    
    Path: web_proxy/profile
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
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        header_client_ip: Literal["pass", "add", "remove"] | None = ...,
        header_via_request: Literal["pass", "add", "remove"] | None = ...,
        header_via_response: Literal["pass", "add", "remove"] | None = ...,
        header_x_forwarded_for: Literal["pass", "add", "remove"] | None = ...,
        header_x_forwarded_client_cert: Literal["pass", "add", "remove"] | None = ...,
        header_front_end_https: Literal["pass", "add", "remove"] | None = ...,
        header_x_authenticated_user: Literal["pass", "add", "remove"] | None = ...,
        header_x_authenticated_groups: Literal["pass", "add", "remove"] | None = ...,
        strip_encoding: Literal["enable", "disable"] | None = ...,
        log_header_change: Literal["enable", "disable"] | None = ...,
        headers: list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        header_client_ip: Literal["pass", "add", "remove"] | None = ...,
        header_via_request: Literal["pass", "add", "remove"] | None = ...,
        header_via_response: Literal["pass", "add", "remove"] | None = ...,
        header_x_forwarded_for: Literal["pass", "add", "remove"] | None = ...,
        header_x_forwarded_client_cert: Literal["pass", "add", "remove"] | None = ...,
        header_front_end_https: Literal["pass", "add", "remove"] | None = ...,
        header_x_authenticated_user: Literal["pass", "add", "remove"] | None = ...,
        header_x_authenticated_groups: Literal["pass", "add", "remove"] | None = ...,
        strip_encoding: Literal["enable", "disable"] | None = ...,
        log_header_change: Literal["enable", "disable"] | None = ...,
        headers: list[dict[str, Any]] | None = ...,
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
        payload_dict: ProfilePayload | None = ...,
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