from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class SyslogProfilePayload(TypedDict, total=False):
    """
    Type hints for wireless_controller/syslog_profile payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: SyslogProfilePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # WTP system log server profile name.
    comment: NotRequired[str]  # Comment.
    server_status: NotRequired[Literal["enable", "disable"]]  # Enable/disable FortiAP units to send log messages to a syslo
    server_addr_type: NotRequired[Literal["fqdn", "ip"]]  # Syslog server address type (default = ip).
    server_fqdn: NotRequired[str]  # FQDN of syslog server that FortiAP units send log messages t
    server_ip: NotRequired[str]  # IP address of syslog server that FortiAP units send log mess
    server_port: NotRequired[int]  # Port number of syslog server that FortiAP units send log mes
    server_type: NotRequired[Literal["standard", "fortianalyzer"]]  # Configure syslog server type (default = standard).
    log_level: NotRequired[Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debugging"]]  # Lowest level of log messages that FortiAP units send to this


class SyslogProfile:
    """
    Configure Wireless Termination Points (WTP) system log server profile.
    
    Path: wireless_controller/syslog_profile
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
        payload_dict: SyslogProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        server_status: Literal["enable", "disable"] | None = ...,
        server_addr_type: Literal["fqdn", "ip"] | None = ...,
        server_fqdn: str | None = ...,
        server_ip: str | None = ...,
        server_port: int | None = ...,
        server_type: Literal["standard", "fortianalyzer"] | None = ...,
        log_level: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debugging"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: SyslogProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        server_status: Literal["enable", "disable"] | None = ...,
        server_addr_type: Literal["fqdn", "ip"] | None = ...,
        server_fqdn: str | None = ...,
        server_ip: str | None = ...,
        server_port: int | None = ...,
        server_type: Literal["standard", "fortianalyzer"] | None = ...,
        log_level: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debugging"] | None = ...,
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
        payload_dict: SyslogProfilePayload | None = ...,
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