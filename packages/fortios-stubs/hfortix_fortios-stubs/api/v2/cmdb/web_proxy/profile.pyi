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
    header_client_ip: NotRequired[Literal[{"description": "Forward the same HTTP header", "help": "Forward the same HTTP header.", "label": "Pass", "name": "pass"}, {"description": "Add the HTTP header", "help": "Add the HTTP header.", "label": "Add", "name": "add"}, {"description": "Remove the HTTP header", "help": "Remove the HTTP header.", "label": "Remove", "name": "remove"}]]  # Action to take on the HTTP client-IP header in forwarded req
    header_via_request: NotRequired[Literal[{"description": "Forward the same HTTP header", "help": "Forward the same HTTP header.", "label": "Pass", "name": "pass"}, {"description": "Add the HTTP header", "help": "Add the HTTP header.", "label": "Add", "name": "add"}, {"description": "Remove the HTTP header", "help": "Remove the HTTP header.", "label": "Remove", "name": "remove"}]]  # Action to take on the HTTP via header in forwarded requests:
    header_via_response: NotRequired[Literal[{"description": "Forward the same HTTP header", "help": "Forward the same HTTP header.", "label": "Pass", "name": "pass"}, {"description": "Add the HTTP header", "help": "Add the HTTP header.", "label": "Add", "name": "add"}, {"description": "Remove the HTTP header", "help": "Remove the HTTP header.", "label": "Remove", "name": "remove"}]]  # Action to take on the HTTP via header in forwarded responses
    header_client_cert: NotRequired[Literal[{"description": "Forward the same HTTP header", "help": "Forward the same HTTP header.", "label": "Pass", "name": "pass"}, {"description": "Add the HTTP header", "help": "Add the HTTP header.", "label": "Add", "name": "add"}, {"description": "Remove the HTTP header", "help": "Remove the HTTP header.", "label": "Remove", "name": "remove"}]]  # Action to take on the HTTP Client-Cert/Client-Cert-Chain hea
    header_x_forwarded_for: NotRequired[Literal[{"description": "Forward the same HTTP header", "help": "Forward the same HTTP header.", "label": "Pass", "name": "pass"}, {"description": "Add the HTTP header", "help": "Add the HTTP header.", "label": "Add", "name": "add"}, {"description": "Remove the HTTP header", "help": "Remove the HTTP header.", "label": "Remove", "name": "remove"}]]  # Action to take on the HTTP x-forwarded-for header in forward
    header_x_forwarded_client_cert: NotRequired[Literal[{"description": "Forward the same HTTP header", "help": "Forward the same HTTP header.", "label": "Pass", "name": "pass"}, {"description": "Add the HTTP header", "help": "Add the HTTP header.", "label": "Add", "name": "add"}, {"description": "Remove the HTTP header", "help": "Remove the HTTP header.", "label": "Remove", "name": "remove"}]]  # Action to take on the HTTP x-forwarded-client-cert header in
    header_front_end_https: NotRequired[Literal[{"description": "Forward the same HTTP header", "help": "Forward the same HTTP header.", "label": "Pass", "name": "pass"}, {"description": "Add the HTTP header", "help": "Add the HTTP header.", "label": "Add", "name": "add"}, {"description": "Remove the HTTP header", "help": "Remove the HTTP header.", "label": "Remove", "name": "remove"}]]  # Action to take on the HTTP front-end-HTTPS header in forward
    header_x_authenticated_user: NotRequired[Literal[{"description": "Forward the same HTTP header", "help": "Forward the same HTTP header.", "label": "Pass", "name": "pass"}, {"description": "Add the HTTP header", "help": "Add the HTTP header.", "label": "Add", "name": "add"}, {"description": "Remove the HTTP header", "help": "Remove the HTTP header.", "label": "Remove", "name": "remove"}]]  # Action to take on the HTTP x-authenticated-user header in fo
    header_x_authenticated_groups: NotRequired[Literal[{"description": "Forward the same HTTP header", "help": "Forward the same HTTP header.", "label": "Pass", "name": "pass"}, {"description": "Add the HTTP header", "help": "Add the HTTP header.", "label": "Add", "name": "add"}, {"description": "Remove the HTTP header", "help": "Remove the HTTP header.", "label": "Remove", "name": "remove"}]]  # Action to take on the HTTP x-authenticated-groups header in 
    strip_encoding: NotRequired[Literal[{"description": "Enable stripping of unsupported encoding from the request header", "help": "Enable stripping of unsupported encoding from the request header.", "label": "Enable", "name": "enable"}, {"description": "Disable stripping of unsupported encoding from the request header", "help": "Disable stripping of unsupported encoding from the request header.", "label": "Disable", "name": "disable"}]]  # Enable/disable stripping unsupported encoding from the reque
    log_header_change: NotRequired[Literal[{"description": "Enable Enable/disable logging HTTP header changes", "help": "Enable Enable/disable logging HTTP header changes.", "label": "Enable", "name": "enable"}, {"description": "Disable Enable/disable logging HTTP header changes", "help": "Disable Enable/disable logging HTTP header changes.", "label": "Disable", "name": "disable"}]]  # Enable/disable logging HTTP header changes.
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
        header_client_ip: Literal[{"description": "Forward the same HTTP header", "help": "Forward the same HTTP header.", "label": "Pass", "name": "pass"}, {"description": "Add the HTTP header", "help": "Add the HTTP header.", "label": "Add", "name": "add"}, {"description": "Remove the HTTP header", "help": "Remove the HTTP header.", "label": "Remove", "name": "remove"}] | None = ...,
        header_via_request: Literal[{"description": "Forward the same HTTP header", "help": "Forward the same HTTP header.", "label": "Pass", "name": "pass"}, {"description": "Add the HTTP header", "help": "Add the HTTP header.", "label": "Add", "name": "add"}, {"description": "Remove the HTTP header", "help": "Remove the HTTP header.", "label": "Remove", "name": "remove"}] | None = ...,
        header_via_response: Literal[{"description": "Forward the same HTTP header", "help": "Forward the same HTTP header.", "label": "Pass", "name": "pass"}, {"description": "Add the HTTP header", "help": "Add the HTTP header.", "label": "Add", "name": "add"}, {"description": "Remove the HTTP header", "help": "Remove the HTTP header.", "label": "Remove", "name": "remove"}] | None = ...,
        header_client_cert: Literal[{"description": "Forward the same HTTP header", "help": "Forward the same HTTP header.", "label": "Pass", "name": "pass"}, {"description": "Add the HTTP header", "help": "Add the HTTP header.", "label": "Add", "name": "add"}, {"description": "Remove the HTTP header", "help": "Remove the HTTP header.", "label": "Remove", "name": "remove"}] | None = ...,
        header_x_forwarded_for: Literal[{"description": "Forward the same HTTP header", "help": "Forward the same HTTP header.", "label": "Pass", "name": "pass"}, {"description": "Add the HTTP header", "help": "Add the HTTP header.", "label": "Add", "name": "add"}, {"description": "Remove the HTTP header", "help": "Remove the HTTP header.", "label": "Remove", "name": "remove"}] | None = ...,
        header_x_forwarded_client_cert: Literal[{"description": "Forward the same HTTP header", "help": "Forward the same HTTP header.", "label": "Pass", "name": "pass"}, {"description": "Add the HTTP header", "help": "Add the HTTP header.", "label": "Add", "name": "add"}, {"description": "Remove the HTTP header", "help": "Remove the HTTP header.", "label": "Remove", "name": "remove"}] | None = ...,
        header_front_end_https: Literal[{"description": "Forward the same HTTP header", "help": "Forward the same HTTP header.", "label": "Pass", "name": "pass"}, {"description": "Add the HTTP header", "help": "Add the HTTP header.", "label": "Add", "name": "add"}, {"description": "Remove the HTTP header", "help": "Remove the HTTP header.", "label": "Remove", "name": "remove"}] | None = ...,
        header_x_authenticated_user: Literal[{"description": "Forward the same HTTP header", "help": "Forward the same HTTP header.", "label": "Pass", "name": "pass"}, {"description": "Add the HTTP header", "help": "Add the HTTP header.", "label": "Add", "name": "add"}, {"description": "Remove the HTTP header", "help": "Remove the HTTP header.", "label": "Remove", "name": "remove"}] | None = ...,
        header_x_authenticated_groups: Literal[{"description": "Forward the same HTTP header", "help": "Forward the same HTTP header.", "label": "Pass", "name": "pass"}, {"description": "Add the HTTP header", "help": "Add the HTTP header.", "label": "Add", "name": "add"}, {"description": "Remove the HTTP header", "help": "Remove the HTTP header.", "label": "Remove", "name": "remove"}] | None = ...,
        strip_encoding: Literal[{"description": "Enable stripping of unsupported encoding from the request header", "help": "Enable stripping of unsupported encoding from the request header.", "label": "Enable", "name": "enable"}, {"description": "Disable stripping of unsupported encoding from the request header", "help": "Disable stripping of unsupported encoding from the request header.", "label": "Disable", "name": "disable"}] | None = ...,
        log_header_change: Literal[{"description": "Enable Enable/disable logging HTTP header changes", "help": "Enable Enable/disable logging HTTP header changes.", "label": "Enable", "name": "enable"}, {"description": "Disable Enable/disable logging HTTP header changes", "help": "Disable Enable/disable logging HTTP header changes.", "label": "Disable", "name": "disable"}] | None = ...,
        headers: list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        header_client_ip: Literal[{"description": "Forward the same HTTP header", "help": "Forward the same HTTP header.", "label": "Pass", "name": "pass"}, {"description": "Add the HTTP header", "help": "Add the HTTP header.", "label": "Add", "name": "add"}, {"description": "Remove the HTTP header", "help": "Remove the HTTP header.", "label": "Remove", "name": "remove"}] | None = ...,
        header_via_request: Literal[{"description": "Forward the same HTTP header", "help": "Forward the same HTTP header.", "label": "Pass", "name": "pass"}, {"description": "Add the HTTP header", "help": "Add the HTTP header.", "label": "Add", "name": "add"}, {"description": "Remove the HTTP header", "help": "Remove the HTTP header.", "label": "Remove", "name": "remove"}] | None = ...,
        header_via_response: Literal[{"description": "Forward the same HTTP header", "help": "Forward the same HTTP header.", "label": "Pass", "name": "pass"}, {"description": "Add the HTTP header", "help": "Add the HTTP header.", "label": "Add", "name": "add"}, {"description": "Remove the HTTP header", "help": "Remove the HTTP header.", "label": "Remove", "name": "remove"}] | None = ...,
        header_client_cert: Literal[{"description": "Forward the same HTTP header", "help": "Forward the same HTTP header.", "label": "Pass", "name": "pass"}, {"description": "Add the HTTP header", "help": "Add the HTTP header.", "label": "Add", "name": "add"}, {"description": "Remove the HTTP header", "help": "Remove the HTTP header.", "label": "Remove", "name": "remove"}] | None = ...,
        header_x_forwarded_for: Literal[{"description": "Forward the same HTTP header", "help": "Forward the same HTTP header.", "label": "Pass", "name": "pass"}, {"description": "Add the HTTP header", "help": "Add the HTTP header.", "label": "Add", "name": "add"}, {"description": "Remove the HTTP header", "help": "Remove the HTTP header.", "label": "Remove", "name": "remove"}] | None = ...,
        header_x_forwarded_client_cert: Literal[{"description": "Forward the same HTTP header", "help": "Forward the same HTTP header.", "label": "Pass", "name": "pass"}, {"description": "Add the HTTP header", "help": "Add the HTTP header.", "label": "Add", "name": "add"}, {"description": "Remove the HTTP header", "help": "Remove the HTTP header.", "label": "Remove", "name": "remove"}] | None = ...,
        header_front_end_https: Literal[{"description": "Forward the same HTTP header", "help": "Forward the same HTTP header.", "label": "Pass", "name": "pass"}, {"description": "Add the HTTP header", "help": "Add the HTTP header.", "label": "Add", "name": "add"}, {"description": "Remove the HTTP header", "help": "Remove the HTTP header.", "label": "Remove", "name": "remove"}] | None = ...,
        header_x_authenticated_user: Literal[{"description": "Forward the same HTTP header", "help": "Forward the same HTTP header.", "label": "Pass", "name": "pass"}, {"description": "Add the HTTP header", "help": "Add the HTTP header.", "label": "Add", "name": "add"}, {"description": "Remove the HTTP header", "help": "Remove the HTTP header.", "label": "Remove", "name": "remove"}] | None = ...,
        header_x_authenticated_groups: Literal[{"description": "Forward the same HTTP header", "help": "Forward the same HTTP header.", "label": "Pass", "name": "pass"}, {"description": "Add the HTTP header", "help": "Add the HTTP header.", "label": "Add", "name": "add"}, {"description": "Remove the HTTP header", "help": "Remove the HTTP header.", "label": "Remove", "name": "remove"}] | None = ...,
        strip_encoding: Literal[{"description": "Enable stripping of unsupported encoding from the request header", "help": "Enable stripping of unsupported encoding from the request header.", "label": "Enable", "name": "enable"}, {"description": "Disable stripping of unsupported encoding from the request header", "help": "Disable stripping of unsupported encoding from the request header.", "label": "Disable", "name": "disable"}] | None = ...,
        log_header_change: Literal[{"description": "Enable Enable/disable logging HTTP header changes", "help": "Enable Enable/disable logging HTTP header changes.", "label": "Enable", "name": "enable"}, {"description": "Disable Enable/disable logging HTTP header changes", "help": "Disable Enable/disable logging HTTP header changes.", "label": "Disable", "name": "disable"}] | None = ...,
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


__all__ = [
    "Profile",
    "ProfilePayload",
]