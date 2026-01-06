from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class AnqpNetworkAuthTypePayload(TypedDict, total=False):
    """
    Type hints for wireless_controller/hotspot20/anqp_network_auth_type payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: AnqpNetworkAuthTypePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Authentication type name.
    auth_type: NotRequired[Literal[{"description": "Acceptance of terms and conditions", "help": "Acceptance of terms and conditions.", "label": "Acceptance Of Terms", "name": "acceptance-of-terms"}, {"description": "Online enrollment supported", "help": "Online enrollment supported.", "label": "Online Enrollment", "name": "online-enrollment"}, {"description": "HTTP and HTTPS redirection", "help": "HTTP and HTTPS redirection.", "label": "Http Redirection", "name": "http-redirection"}, {"description": "DNS redirection", "help": "DNS redirection.", "label": "Dns Redirection", "name": "dns-redirection"}]]  # Network authentication type.
    url: NotRequired[str]  # Redirect URL.


class AnqpNetworkAuthType:
    """
    Configure network authentication type.
    
    Path: wireless_controller/hotspot20/anqp_network_auth_type
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
        payload_dict: AnqpNetworkAuthTypePayload | None = ...,
        name: str | None = ...,
        auth_type: Literal[{"description": "Acceptance of terms and conditions", "help": "Acceptance of terms and conditions.", "label": "Acceptance Of Terms", "name": "acceptance-of-terms"}, {"description": "Online enrollment supported", "help": "Online enrollment supported.", "label": "Online Enrollment", "name": "online-enrollment"}, {"description": "HTTP and HTTPS redirection", "help": "HTTP and HTTPS redirection.", "label": "Http Redirection", "name": "http-redirection"}, {"description": "DNS redirection", "help": "DNS redirection.", "label": "Dns Redirection", "name": "dns-redirection"}] | None = ...,
        url: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: AnqpNetworkAuthTypePayload | None = ...,
        name: str | None = ...,
        auth_type: Literal[{"description": "Acceptance of terms and conditions", "help": "Acceptance of terms and conditions.", "label": "Acceptance Of Terms", "name": "acceptance-of-terms"}, {"description": "Online enrollment supported", "help": "Online enrollment supported.", "label": "Online Enrollment", "name": "online-enrollment"}, {"description": "HTTP and HTTPS redirection", "help": "HTTP and HTTPS redirection.", "label": "Http Redirection", "name": "http-redirection"}, {"description": "DNS redirection", "help": "DNS redirection.", "label": "Dns Redirection", "name": "dns-redirection"}] | None = ...,
        url: str | None = ...,
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
        payload_dict: AnqpNetworkAuthTypePayload | None = ...,
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
    "AnqpNetworkAuthType",
    "AnqpNetworkAuthTypePayload",
]