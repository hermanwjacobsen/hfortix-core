from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class AuthPortalPayload(TypedDict, total=False):
    """
    Type hints for firewall/auth_portal payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: AuthPortalPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    groups: NotRequired[list[dict[str, Any]]]  # Firewall user groups permitted to authenticate through this 
    portal_addr: NotRequired[str]  # Address (or FQDN) of the authentication portal.
    portal_addr6: NotRequired[str]  # IPv6 address (or FQDN) of authentication portal.
    identity_based_route: NotRequired[str]  # Name of the identity-based route that applies to this portal
    proxy_auth: NotRequired[Literal["enable", "disable"]]  # Enable/disable authentication by proxy daemon (default = dis


class AuthPortal:
    """
    Configure firewall authentication portals.
    
    Path: firewall/auth_portal
    Category: cmdb
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
        payload_dict: AuthPortalPayload | None = ...,
        groups: list[dict[str, Any]] | None = ...,
        portal_addr: str | None = ...,
        portal_addr6: str | None = ...,
        identity_based_route: str | None = ...,
        proxy_auth: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: AuthPortalPayload | None = ...,
        groups: list[dict[str, Any]] | None = ...,
        portal_addr: str | None = ...,
        portal_addr6: str | None = ...,
        identity_based_route: str | None = ...,
        proxy_auth: Literal["enable", "disable"] | None = ...,
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
        payload_dict: AuthPortalPayload | None = ...,
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