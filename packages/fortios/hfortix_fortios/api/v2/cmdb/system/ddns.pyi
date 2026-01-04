from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class DdnsPayload(TypedDict, total=False):
    """
    Type hints for system/ddns payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: DdnsPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    ddnsid: NotRequired[int]  # DDNS ID.
    ddns_server: Literal["dyndns.org", "dyns.net", "tzo.com", "vavic.com", "dipdns.net", "now.net.cn", "dhs.org", "easydns.com", "genericDDNS", "FortiGuardDDNS", "noip.com"]  # Select a DDNS service provider.
    addr_type: NotRequired[Literal["ipv4", "ipv6"]]  # Address type of interface address in DDNS update.
    server_type: NotRequired[Literal["ipv4", "ipv6"]]  # Address type of the DDNS server.
    ddns_server_addr: NotRequired[list[dict[str, Any]]]  # Generic DDNS server IP/FQDN list.
    ddns_zone: NotRequired[str]  # Zone of your domain name (for example, DDNS.com).
    ddns_ttl: NotRequired[int]  # Time-to-live for DDNS packets.
    ddns_auth: NotRequired[Literal["disable", "tsig"]]  # Enable/disable TSIG authentication for your DDNS server.
    ddns_keyname: NotRequired[str]  # DDNS update key name.
    ddns_key: NotRequired[str]  # DDNS update key (base 64 encoding).
    ddns_domain: NotRequired[str]  # Your fully qualified domain name. For example, yourname.ddns
    ddns_username: NotRequired[str]  # DDNS user name.
    ddns_sn: NotRequired[str]  # DDNS Serial Number.
    ddns_password: NotRequired[str]  # DDNS password.
    use_public_ip: NotRequired[Literal["disable", "enable"]]  # Enable/disable use of public IP address.
    update_interval: NotRequired[int]  # DDNS update interval (60 - 2592000 sec, 0 means default).
    clear_text: NotRequired[Literal["disable", "enable"]]  # Enable/disable use of clear text connections.
    ssl_certificate: NotRequired[str]  # Name of local certificate for SSL connections.
    bound_ip: NotRequired[str]  # Bound IP address.
    monitor_interface: list[dict[str, Any]]  # Monitored interface.


class Ddns:
    """
    Configure DDNS.
    
    Path: system/ddns
    Category: cmdb
    Primary Key: ddnsid
    """
    
    def get(
        self,
        ddnsid: int | None = ...,
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
        payload_dict: DdnsPayload | None = ...,
        ddnsid: int | None = ...,
        ddns_server: Literal["dyndns.org", "dyns.net", "tzo.com", "vavic.com", "dipdns.net", "now.net.cn", "dhs.org", "easydns.com", "genericDDNS", "FortiGuardDDNS", "noip.com"] | None = ...,
        addr_type: Literal["ipv4", "ipv6"] | None = ...,
        server_type: Literal["ipv4", "ipv6"] | None = ...,
        ddns_server_addr: list[dict[str, Any]] | None = ...,
        ddns_zone: str | None = ...,
        ddns_ttl: int | None = ...,
        ddns_auth: Literal["disable", "tsig"] | None = ...,
        ddns_keyname: str | None = ...,
        ddns_key: str | None = ...,
        ddns_domain: str | None = ...,
        ddns_username: str | None = ...,
        ddns_sn: str | None = ...,
        ddns_password: str | None = ...,
        use_public_ip: Literal["disable", "enable"] | None = ...,
        update_interval: int | None = ...,
        clear_text: Literal["disable", "enable"] | None = ...,
        ssl_certificate: str | None = ...,
        bound_ip: str | None = ...,
        monitor_interface: list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: DdnsPayload | None = ...,
        ddnsid: int | None = ...,
        ddns_server: Literal["dyndns.org", "dyns.net", "tzo.com", "vavic.com", "dipdns.net", "now.net.cn", "dhs.org", "easydns.com", "genericDDNS", "FortiGuardDDNS", "noip.com"] | None = ...,
        addr_type: Literal["ipv4", "ipv6"] | None = ...,
        server_type: Literal["ipv4", "ipv6"] | None = ...,
        ddns_server_addr: list[dict[str, Any]] | None = ...,
        ddns_zone: str | None = ...,
        ddns_ttl: int | None = ...,
        ddns_auth: Literal["disable", "tsig"] | None = ...,
        ddns_keyname: str | None = ...,
        ddns_key: str | None = ...,
        ddns_domain: str | None = ...,
        ddns_username: str | None = ...,
        ddns_sn: str | None = ...,
        ddns_password: str | None = ...,
        use_public_ip: Literal["disable", "enable"] | None = ...,
        update_interval: int | None = ...,
        clear_text: Literal["disable", "enable"] | None = ...,
        ssl_certificate: str | None = ...,
        bound_ip: str | None = ...,
        monitor_interface: list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def delete(
        self,
        ddnsid: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def exists(
        self,
        ddnsid: int,
        vdom: str | bool | None = ...,
    ) -> Union[bool, Coroutine[Any, Any, bool]]: ...
    
    def set(
        self,
        payload_dict: DdnsPayload | None = ...,
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