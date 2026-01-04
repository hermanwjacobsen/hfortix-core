from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class AdminPayload(TypedDict, total=False):
    """
    Type hints for system/admin payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: AdminPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # User name.
    wildcard: NotRequired[Literal["enable", "disable"]]  # Enable/disable wildcard RADIUS authentication.
    remote_auth: NotRequired[Literal["enable", "disable"]]  # Enable/disable authentication using a remote RADIUS, LDAP, o
    remote_group: str  # User group name used for remote auth.
    password: str  # Admin user password.
    peer_auth: NotRequired[Literal["enable", "disable"]]  # Set to enable peer certificate authentication (for HTTPS adm
    peer_group: str  # Name of peer group defined under config user group which has
    trusthost1: NotRequired[str]  # Any IPv4 address or subnet address and netmask from which th
    trusthost2: NotRequired[str]  # Any IPv4 address or subnet address and netmask from which th
    trusthost3: NotRequired[str]  # Any IPv4 address or subnet address and netmask from which th
    trusthost4: NotRequired[str]  # Any IPv4 address or subnet address and netmask from which th
    trusthost5: NotRequired[str]  # Any IPv4 address or subnet address and netmask from which th
    trusthost6: NotRequired[str]  # Any IPv4 address or subnet address and netmask from which th
    trusthost7: NotRequired[str]  # Any IPv4 address or subnet address and netmask from which th
    trusthost8: NotRequired[str]  # Any IPv4 address or subnet address and netmask from which th
    trusthost9: NotRequired[str]  # Any IPv4 address or subnet address and netmask from which th
    trusthost10: NotRequired[str]  # Any IPv4 address or subnet address and netmask from which th
    ip6_trusthost1: NotRequired[str]  # Any IPv6 address from which the administrator can connect to
    ip6_trusthost2: NotRequired[str]  # Any IPv6 address from which the administrator can connect to
    ip6_trusthost3: NotRequired[str]  # Any IPv6 address from which the administrator can connect to
    ip6_trusthost4: NotRequired[str]  # Any IPv6 address from which the administrator can connect to
    ip6_trusthost5: NotRequired[str]  # Any IPv6 address from which the administrator can connect to
    ip6_trusthost6: NotRequired[str]  # Any IPv6 address from which the administrator can connect to
    ip6_trusthost7: NotRequired[str]  # Any IPv6 address from which the administrator can connect to
    ip6_trusthost8: NotRequired[str]  # Any IPv6 address from which the administrator can connect to
    ip6_trusthost9: NotRequired[str]  # Any IPv6 address from which the administrator can connect to
    ip6_trusthost10: NotRequired[str]  # Any IPv6 address from which the administrator can connect to
    accprofile: NotRequired[str]  # Access profile for this administrator. Access profiles contr
    allow_remove_admin_session: NotRequired[Literal["enable", "disable"]]  # Enable/disable allow admin session to be removed by privileg
    comments: NotRequired[str]  # Comment.
    vdom: NotRequired[list[dict[str, Any]]]  # Virtual domain(s) that the administrator can access.
    ssh_public_key1: NotRequired[str]  # Public key of an SSH client. The client is authenticated wit
    ssh_public_key2: NotRequired[str]  # Public key of an SSH client. The client is authenticated wit
    ssh_public_key3: NotRequired[str]  # Public key of an SSH client. The client is authenticated wit
    ssh_certificate: NotRequired[str]  # Select the certificate to be used by the FortiGate for authe
    schedule: NotRequired[str]  # Firewall schedule used to restrict when the administrator ca
    accprofile_override: NotRequired[Literal["enable", "disable"]]  # Enable to use the name of an access profile provided by the 
    vdom_override: NotRequired[Literal["enable", "disable"]]  # Enable to use the names of VDOMs provided by the remote auth
    password_expire: NotRequired[str]  # Password expire time.
    force_password_change: NotRequired[Literal["enable", "disable"]]  # Enable/disable force password change on next login.
    two_factor: NotRequired[Literal["disable", "fortitoken", "fortitoken-cloud", "email", "sms"]]  # Enable/disable two-factor authentication.
    two_factor_authentication: NotRequired[Literal["fortitoken", "email", "sms"]]  # Authentication method by FortiToken Cloud.
    two_factor_notification: NotRequired[Literal["email", "sms"]]  # Notification method for user activation by FortiToken Cloud.
    fortitoken: NotRequired[str]  # This administrator's FortiToken serial number.
    email_to: NotRequired[str]  # This administrator's email address.
    sms_server: NotRequired[Literal["fortiguard", "custom"]]  # Send SMS messages using the FortiGuard SMS server or a custo
    sms_custom_server: NotRequired[str]  # Custom SMS server to send SMS messages to.
    sms_phone: NotRequired[str]  # Phone number on which the administrator receives SMS message
    guest_auth: NotRequired[Literal["disable", "enable"]]  # Enable/disable guest authentication.
    guest_usergroups: NotRequired[list[dict[str, Any]]]  # Select guest user groups.
    guest_lang: NotRequired[str]  # Guest management portal language.
    status: NotRequired[str]  # print admin status information
    list: NotRequired[str]  # print admin list information


class Admin:
    """
    Configure admin users.
    
    Path: system/admin
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
        payload_dict: AdminPayload | None = ...,
        name: str | None = ...,
        wildcard: Literal["enable", "disable"] | None = ...,
        remote_auth: Literal["enable", "disable"] | None = ...,
        remote_group: str | None = ...,
        password: str | None = ...,
        peer_auth: Literal["enable", "disable"] | None = ...,
        peer_group: str | None = ...,
        trusthost1: str | None = ...,
        trusthost2: str | None = ...,
        trusthost3: str | None = ...,
        trusthost4: str | None = ...,
        trusthost5: str | None = ...,
        trusthost6: str | None = ...,
        trusthost7: str | None = ...,
        trusthost8: str | None = ...,
        trusthost9: str | None = ...,
        trusthost10: str | None = ...,
        ip6_trusthost1: str | None = ...,
        ip6_trusthost2: str | None = ...,
        ip6_trusthost3: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: AdminPayload | None = ...,
        name: str | None = ...,
        wildcard: Literal["enable", "disable"] | None = ...,
        remote_auth: Literal["enable", "disable"] | None = ...,
        remote_group: str | None = ...,
        password: str | None = ...,
        peer_auth: Literal["enable", "disable"] | None = ...,
        peer_group: str | None = ...,
        trusthost1: str | None = ...,
        trusthost2: str | None = ...,
        trusthost3: str | None = ...,
        trusthost4: str | None = ...,
        trusthost5: str | None = ...,
        trusthost6: str | None = ...,
        trusthost7: str | None = ...,
        trusthost8: str | None = ...,
        trusthost9: str | None = ...,
        trusthost10: str | None = ...,
        ip6_trusthost1: str | None = ...,
        ip6_trusthost2: str | None = ...,
        ip6_trusthost3: str | None = ...,
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
        payload_dict: AdminPayload | None = ...,
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