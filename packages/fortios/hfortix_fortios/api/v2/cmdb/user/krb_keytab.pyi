from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class KrbKeytabPayload(TypedDict, total=False):
    """
    Type hints for user/krb_keytab payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: KrbKeytabPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Kerberos keytab entry name.
    pac_data: NotRequired[Literal[{"description": "Enable parsing PAC data in the ticket", "help": "Enable parsing PAC data in the ticket.", "label": "Enable", "name": "enable"}, {"description": "Disable parsing PAC data in the ticket", "help": "Disable parsing PAC data in the ticket.", "label": "Disable", "name": "disable"}]]  # Enable/disable parsing PAC data in the ticket.
    principal: str  # Kerberos service principal. For example, HTTP/myfgt.example.
    ldap_server: NotRequired[list[dict[str, Any]]]  # LDAP server name(s).
    keytab: str  # Base64 coded keytab file containing a pre-shared key.


class KrbKeytab:
    """
    Configure Kerberos keytab entries.
    
    Path: user/krb_keytab
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
        payload_dict: KrbKeytabPayload | None = ...,
        name: str | None = ...,
        pac_data: Literal[{"description": "Enable parsing PAC data in the ticket", "help": "Enable parsing PAC data in the ticket.", "label": "Enable", "name": "enable"}, {"description": "Disable parsing PAC data in the ticket", "help": "Disable parsing PAC data in the ticket.", "label": "Disable", "name": "disable"}] | None = ...,
        principal: str | None = ...,
        ldap_server: list[dict[str, Any]] | None = ...,
        keytab: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: KrbKeytabPayload | None = ...,
        name: str | None = ...,
        pac_data: Literal[{"description": "Enable parsing PAC data in the ticket", "help": "Enable parsing PAC data in the ticket.", "label": "Enable", "name": "enable"}, {"description": "Disable parsing PAC data in the ticket", "help": "Disable parsing PAC data in the ticket.", "label": "Disable", "name": "disable"}] | None = ...,
        principal: str | None = ...,
        ldap_server: list[dict[str, Any]] | None = ...,
        keytab: str | None = ...,
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
        payload_dict: KrbKeytabPayload | None = ...,
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
    "KrbKeytab",
    "KrbKeytabPayload",
]