from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class ProfilePayload(TypedDict, total=False):
    """
    Type hints for web_proxy/profile payload fields.
    
    Configure web proxy profiles.
    
    **Usage:**
        payload: ProfilePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Profile name.
    header_client_ip: NotRequired[Literal["pass", "add", "remove"]]  # Action to take on the HTTP client-IP header in forwarded req
    header_via_request: NotRequired[Literal["pass", "add", "remove"]]  # Action to take on the HTTP via header in forwarded requests:
    header_via_response: NotRequired[Literal["pass", "add", "remove"]]  # Action to take on the HTTP via header in forwarded responses
    header_client_cert: NotRequired[Literal["pass", "add", "remove"]]  # Action to take on the HTTP Client-Cert/Client-Cert-Chain hea
    header_x_forwarded_for: NotRequired[Literal["pass", "add", "remove"]]  # Action to take on the HTTP x-forwarded-for header in forward
    header_x_forwarded_client_cert: NotRequired[Literal["pass", "add", "remove"]]  # Action to take on the HTTP x-forwarded-client-cert header in
    header_front_end_https: NotRequired[Literal["pass", "add", "remove"]]  # Action to take on the HTTP front-end-HTTPS header in forward
    header_x_authenticated_user: NotRequired[Literal["pass", "add", "remove"]]  # Action to take on the HTTP x-authenticated-user header in fo
    header_x_authenticated_groups: NotRequired[Literal["pass", "add", "remove"]]  # Action to take on the HTTP x-authenticated-groups header in 
    strip_encoding: NotRequired[Literal["enable", "disable"]]  # Enable/disable stripping unsupported encoding from the reque
    log_header_change: NotRequired[Literal["enable", "disable"]]  # Enable/disable logging HTTP header changes.
    headers: NotRequired[list[dict[str, Any]]]  # Configure HTTP forwarded requests headers.


class ProfileObject(FortiObject[ProfilePayload]):
    """Typed FortiObject for web_proxy/profile with IDE autocomplete support."""
    
    # Profile name.
    name: str
    # Action to take on the HTTP client-IP header in forwarded requests: forwards (pas
    header_client_ip: Literal["pass", "add", "remove"]
    # Action to take on the HTTP via header in forwarded requests: forwards (pass), ad
    header_via_request: Literal["pass", "add", "remove"]
    # Action to take on the HTTP via header in forwarded responses: forwards (pass), a
    header_via_response: Literal["pass", "add", "remove"]
    # Action to take on the HTTP Client-Cert/Client-Cert-Chain headers in forwarded re
    header_client_cert: Literal["pass", "add", "remove"]
    # Action to take on the HTTP x-forwarded-for header in forwarded requests: forward
    header_x_forwarded_for: Literal["pass", "add", "remove"]
    # Action to take on the HTTP x-forwarded-client-cert header in forwarded requests:
    header_x_forwarded_client_cert: Literal["pass", "add", "remove"]
    # Action to take on the HTTP front-end-HTTPS header in forwarded requests: forward
    header_front_end_https: Literal["pass", "add", "remove"]
    # Action to take on the HTTP x-authenticated-user header in forwarded requests: fo
    header_x_authenticated_user: Literal["pass", "add", "remove"]
    # Action to take on the HTTP x-authenticated-groups header in forwarded requests: 
    header_x_authenticated_groups: Literal["pass", "add", "remove"]
    # Enable/disable stripping unsupported encoding from the request header.
    strip_encoding: Literal["enable", "disable"]
    # Enable/disable logging HTTP header changes.
    log_header_change: Literal["enable", "disable"]
    # Configure HTTP forwarded requests headers.
    headers: list[str]  # Auto-flattened from member_table
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> ProfilePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Profile:
    """
    Configure web proxy profiles.
    
    Path: web_proxy/profile
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
    ) -> ProfileObject: ...
    
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
    ) -> list[ProfileObject]: ...
    
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
    ) -> ProfileObject | list[ProfileObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        header_client_ip: Literal["pass", "add", "remove"] | None = ...,
        header_via_request: Literal["pass", "add", "remove"] | None = ...,
        header_via_response: Literal["pass", "add", "remove"] | None = ...,
        header_client_cert: Literal["pass", "add", "remove"] | None = ...,
        header_x_forwarded_for: Literal["pass", "add", "remove"] | None = ...,
        header_x_forwarded_client_cert: Literal["pass", "add", "remove"] | None = ...,
        header_front_end_https: Literal["pass", "add", "remove"] | None = ...,
        header_x_authenticated_user: Literal["pass", "add", "remove"] | None = ...,
        header_x_authenticated_groups: Literal["pass", "add", "remove"] | None = ...,
        strip_encoding: Literal["enable", "disable"] | None = ...,
        log_header_change: Literal["enable", "disable"] | None = ...,
        headers: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ProfileObject: ...
    
    @overload
    def post(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        header_client_ip: Literal["pass", "add", "remove"] | None = ...,
        header_via_request: Literal["pass", "add", "remove"] | None = ...,
        header_via_response: Literal["pass", "add", "remove"] | None = ...,
        header_client_cert: Literal["pass", "add", "remove"] | None = ...,
        header_x_forwarded_for: Literal["pass", "add", "remove"] | None = ...,
        header_x_forwarded_client_cert: Literal["pass", "add", "remove"] | None = ...,
        header_front_end_https: Literal["pass", "add", "remove"] | None = ...,
        header_x_authenticated_user: Literal["pass", "add", "remove"] | None = ...,
        header_x_authenticated_groups: Literal["pass", "add", "remove"] | None = ...,
        strip_encoding: Literal["enable", "disable"] | None = ...,
        log_header_change: Literal["enable", "disable"] | None = ...,
        headers: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        header_client_ip: Literal["pass", "add", "remove"] | None = ...,
        header_via_request: Literal["pass", "add", "remove"] | None = ...,
        header_via_response: Literal["pass", "add", "remove"] | None = ...,
        header_client_cert: Literal["pass", "add", "remove"] | None = ...,
        header_x_forwarded_for: Literal["pass", "add", "remove"] | None = ...,
        header_x_forwarded_client_cert: Literal["pass", "add", "remove"] | None = ...,
        header_front_end_https: Literal["pass", "add", "remove"] | None = ...,
        header_x_authenticated_user: Literal["pass", "add", "remove"] | None = ...,
        header_x_authenticated_groups: Literal["pass", "add", "remove"] | None = ...,
        strip_encoding: Literal["enable", "disable"] | None = ...,
        log_header_change: Literal["enable", "disable"] | None = ...,
        headers: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        header_client_ip: Literal["pass", "add", "remove"] | None = ...,
        header_via_request: Literal["pass", "add", "remove"] | None = ...,
        header_via_response: Literal["pass", "add", "remove"] | None = ...,
        header_client_cert: Literal["pass", "add", "remove"] | None = ...,
        header_x_forwarded_for: Literal["pass", "add", "remove"] | None = ...,
        header_x_forwarded_client_cert: Literal["pass", "add", "remove"] | None = ...,
        header_front_end_https: Literal["pass", "add", "remove"] | None = ...,
        header_x_authenticated_user: Literal["pass", "add", "remove"] | None = ...,
        header_x_authenticated_groups: Literal["pass", "add", "remove"] | None = ...,
        strip_encoding: Literal["enable", "disable"] | None = ...,
        log_header_change: Literal["enable", "disable"] | None = ...,
        headers: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        header_client_ip: Literal["pass", "add", "remove"] | None = ...,
        header_via_request: Literal["pass", "add", "remove"] | None = ...,
        header_via_response: Literal["pass", "add", "remove"] | None = ...,
        header_client_cert: Literal["pass", "add", "remove"] | None = ...,
        header_x_forwarded_for: Literal["pass", "add", "remove"] | None = ...,
        header_x_forwarded_client_cert: Literal["pass", "add", "remove"] | None = ...,
        header_front_end_https: Literal["pass", "add", "remove"] | None = ...,
        header_x_authenticated_user: Literal["pass", "add", "remove"] | None = ...,
        header_x_authenticated_groups: Literal["pass", "add", "remove"] | None = ...,
        strip_encoding: Literal["enable", "disable"] | None = ...,
        log_header_change: Literal["enable", "disable"] | None = ...,
        headers: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ProfileObject: ...
    
    @overload
    def put(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        header_client_ip: Literal["pass", "add", "remove"] | None = ...,
        header_via_request: Literal["pass", "add", "remove"] | None = ...,
        header_via_response: Literal["pass", "add", "remove"] | None = ...,
        header_client_cert: Literal["pass", "add", "remove"] | None = ...,
        header_x_forwarded_for: Literal["pass", "add", "remove"] | None = ...,
        header_x_forwarded_client_cert: Literal["pass", "add", "remove"] | None = ...,
        header_front_end_https: Literal["pass", "add", "remove"] | None = ...,
        header_x_authenticated_user: Literal["pass", "add", "remove"] | None = ...,
        header_x_authenticated_groups: Literal["pass", "add", "remove"] | None = ...,
        strip_encoding: Literal["enable", "disable"] | None = ...,
        log_header_change: Literal["enable", "disable"] | None = ...,
        headers: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        header_client_ip: Literal["pass", "add", "remove"] | None = ...,
        header_via_request: Literal["pass", "add", "remove"] | None = ...,
        header_via_response: Literal["pass", "add", "remove"] | None = ...,
        header_client_cert: Literal["pass", "add", "remove"] | None = ...,
        header_x_forwarded_for: Literal["pass", "add", "remove"] | None = ...,
        header_x_forwarded_client_cert: Literal["pass", "add", "remove"] | None = ...,
        header_front_end_https: Literal["pass", "add", "remove"] | None = ...,
        header_x_authenticated_user: Literal["pass", "add", "remove"] | None = ...,
        header_x_authenticated_groups: Literal["pass", "add", "remove"] | None = ...,
        strip_encoding: Literal["enable", "disable"] | None = ...,
        log_header_change: Literal["enable", "disable"] | None = ...,
        headers: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        header_client_ip: Literal["pass", "add", "remove"] | None = ...,
        header_via_request: Literal["pass", "add", "remove"] | None = ...,
        header_via_response: Literal["pass", "add", "remove"] | None = ...,
        header_client_cert: Literal["pass", "add", "remove"] | None = ...,
        header_x_forwarded_for: Literal["pass", "add", "remove"] | None = ...,
        header_x_forwarded_client_cert: Literal["pass", "add", "remove"] | None = ...,
        header_front_end_https: Literal["pass", "add", "remove"] | None = ...,
        header_x_authenticated_user: Literal["pass", "add", "remove"] | None = ...,
        header_x_authenticated_groups: Literal["pass", "add", "remove"] | None = ...,
        strip_encoding: Literal["enable", "disable"] | None = ...,
        log_header_change: Literal["enable", "disable"] | None = ...,
        headers: str | list[str] | list[dict[str, Any]] | None = ...,
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
    ) -> ProfileObject: ...
    
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
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        header_client_ip: Literal["pass", "add", "remove"] | None = ...,
        header_via_request: Literal["pass", "add", "remove"] | None = ...,
        header_via_response: Literal["pass", "add", "remove"] | None = ...,
        header_client_cert: Literal["pass", "add", "remove"] | None = ...,
        header_x_forwarded_for: Literal["pass", "add", "remove"] | None = ...,
        header_x_forwarded_client_cert: Literal["pass", "add", "remove"] | None = ...,
        header_front_end_https: Literal["pass", "add", "remove"] | None = ...,
        header_x_authenticated_user: Literal["pass", "add", "remove"] | None = ...,
        header_x_authenticated_groups: Literal["pass", "add", "remove"] | None = ...,
        strip_encoding: Literal["enable", "disable"] | None = ...,
        log_header_change: Literal["enable", "disable"] | None = ...,
        headers: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "Profile",
    "ProfilePayload",
    "ProfileObject",
]