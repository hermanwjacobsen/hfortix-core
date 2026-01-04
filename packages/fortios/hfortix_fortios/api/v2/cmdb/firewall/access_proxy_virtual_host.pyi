from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class AccessProxyVirtualHostPayload(TypedDict, total=False):
    """
    Type hints for firewall/access_proxy_virtual_host payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: AccessProxyVirtualHostPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Virtual host name.
    ssl_certificate: list[dict[str, Any]]  # SSL certificates for this host.
    host: str  # The host name.
    host_type: Literal["sub-string", "wildcard"]  # Type of host pattern.
    replacemsg_group: NotRequired[str]  # Access-proxy-virtual-host replacement message override group
    empty_cert_action: NotRequired[Literal["accept", "block", "accept-unmanageable"]]  # Action for an empty client certificate.
    user_agent_detect: NotRequired[Literal["disable", "enable"]]  # Enable/disable detecting device type by HTTP user-agent if n
    client_cert: NotRequired[Literal["disable", "enable"]]  # Enable/disable requesting client certificate.


class AccessProxyVirtualHost:
    """
    Configure Access Proxy virtual hosts.
    
    Path: firewall/access_proxy_virtual_host
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
        payload_dict: AccessProxyVirtualHostPayload | None = ...,
        name: str | None = ...,
        ssl_certificate: list[dict[str, Any]] | None = ...,
        host: str | None = ...,
        host_type: Literal["sub-string", "wildcard"] | None = ...,
        replacemsg_group: str | None = ...,
        empty_cert_action: Literal["accept", "block", "accept-unmanageable"] | None = ...,
        user_agent_detect: Literal["disable", "enable"] | None = ...,
        client_cert: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: AccessProxyVirtualHostPayload | None = ...,
        name: str | None = ...,
        ssl_certificate: list[dict[str, Any]] | None = ...,
        host: str | None = ...,
        host_type: Literal["sub-string", "wildcard"] | None = ...,
        replacemsg_group: str | None = ...,
        empty_cert_action: Literal["accept", "block", "accept-unmanageable"] | None = ...,
        user_agent_detect: Literal["disable", "enable"] | None = ...,
        client_cert: Literal["disable", "enable"] | None = ...,
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
        payload_dict: AccessProxyVirtualHostPayload | None = ...,
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