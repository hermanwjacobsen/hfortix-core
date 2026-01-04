from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class SecurityPolicyLocalAccessPayload(TypedDict, total=False):
    """
    Type hints for switch-controller/security_policy_local_access payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: SecurityPolicyLocalAccessPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Policy name.
    mgmt_allowaccess: NotRequired[Literal["https", "ping", "ssh", "snmp", "http", "telnet", "radius-acct"]]  # Allowed access on the switch management interface.
    internal_allowaccess: NotRequired[Literal["https", "ping", "ssh", "snmp", "http", "telnet", "radius-acct"]]  # Allowed access on the switch internal interface.


class SecurityPolicyLocalAccess:
    """
    Configure allowaccess list for mgmt and internal interfaces on managed FortiSwitch units.
    
    Path: switch-controller/security_policy_local_access
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
        payload_dict: SecurityPolicyLocalAccessPayload | None = ...,
        name: str | None = ...,
        mgmt_allowaccess: Literal["https", "ping", "ssh", "snmp", "http", "telnet", "radius-acct"] | None = ...,
        internal_allowaccess: Literal["https", "ping", "ssh", "snmp", "http", "telnet", "radius-acct"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: SecurityPolicyLocalAccessPayload | None = ...,
        name: str | None = ...,
        mgmt_allowaccess: Literal["https", "ping", "ssh", "snmp", "http", "telnet", "radius-acct"] | None = ...,
        internal_allowaccess: Literal["https", "ping", "ssh", "snmp", "http", "telnet", "radius-acct"] | None = ...,
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
        payload_dict: SecurityPolicyLocalAccessPayload | None = ...,
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