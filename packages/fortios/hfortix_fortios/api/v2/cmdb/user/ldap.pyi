from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class LdapPayload(TypedDict, total=False):
    """
    Type hints for user/ldap payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: LdapPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # LDAP server entry name.
    server: str  # LDAP server CN domain name or IP.
    secondary_server: NotRequired[str]  # Secondary LDAP server CN domain name or IP.
    tertiary_server: NotRequired[str]  # Tertiary LDAP server CN domain name or IP.
    status_ttl: NotRequired[int]  # Time for which server reachability is cached so that when a 
    server_identity_check: NotRequired[Literal["enable", "disable"]]  # Enable/disable LDAP server identity check (verify server dom
    source_ip: NotRequired[str]  # FortiGate IP address to be used for communication with the L
    source_ip_interface: NotRequired[str]  # Source interface for communication with the LDAP server.
    source_port: NotRequired[int]  # Source port to be used for communication with the LDAP serve
    cnid: NotRequired[str]  # Common name identifier for the LDAP server. The common name 
    dn: str  # Distinguished name used to look up entries on the LDAP serve
    type: NotRequired[Literal["simple", "anonymous", "regular"]]  # Authentication type for LDAP searches.
    two_factor: NotRequired[Literal["disable", "fortitoken-cloud"]]  # Enable/disable two-factor authentication.
    two_factor_authentication: NotRequired[Literal["fortitoken", "email", "sms"]]  # Authentication method by FortiToken Cloud.
    two_factor_notification: NotRequired[Literal["email", "sms"]]  # Notification method for user activation by FortiToken Cloud.
    two_factor_filter: NotRequired[str]  # Filter used to synchronize users to FortiToken Cloud.
    username: str  # Username (full DN) for initial binding.
    password: NotRequired[str]  # Password for initial binding.
    group_member_check: NotRequired[Literal["user-attr", "group-object", "posix-group-object"]]  # Group member checking methods.
    group_search_base: NotRequired[str]  # Search base used for group searching.
    group_object_filter: NotRequired[str]  # Filter used for group searching.
    group_filter: NotRequired[str]  # Filter used for group matching.
    secure: NotRequired[Literal["disable", "starttls", "ldaps"]]  # Port to be used for authentication.
    ssl_min_proto_version: NotRequired[Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"]]  # Minimum supported protocol version for SSL/TLS connections (
    ca_cert: NotRequired[str]  # CA certificate name.
    port: NotRequired[int]  # Port to be used for communication with the LDAP server (defa
    password_expiry_warning: NotRequired[Literal["enable", "disable"]]  # Enable/disable password expiry warnings.
    password_renewal: NotRequired[Literal["enable", "disable"]]  # Enable/disable online password renewal.
    member_attr: NotRequired[str]  # Name of attribute from which to get group membership.
    account_key_processing: NotRequired[Literal["same", "strip"]]  # Account key processing operation. The FortiGate will keep ei
    account_key_cert_field: NotRequired[Literal["othername", "rfc822name", "dnsname", "cn"]]  # Define subject identity field in certificate for user access
    account_key_filter: NotRequired[str]  # Account key filter, using the UPN as the search filter.
    search_type: NotRequired[Literal["recursive"]]  # Search type.
    client_cert_auth: NotRequired[Literal["enable", "disable"]]  # Enable/disable using client certificate for TLS authenticati
    client_cert: NotRequired[str]  # Client certificate name.
    obtain_user_info: NotRequired[Literal["enable", "disable"]]  # Enable/disable obtaining of user information.
    user_info_exchange_server: NotRequired[str]  # MS Exchange server from which to fetch user information.
    interface_select_method: NotRequired[Literal["auto", "sdwan", "specify"]]  # Specify how to select outgoing interface to reach server.
    interface: str  # Specify outgoing interface to reach server.
    vrf_select: NotRequired[int]  # VRF ID used for connection to server.
    antiphish: NotRequired[Literal["enable", "disable"]]  # Enable/disable AntiPhishing credential backend.
    password_attr: NotRequired[str]  # Name of attribute to get password hash.


class Ldap:
    """
    Configure LDAP server entries.
    
    Path: user/ldap
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
        payload_dict: LdapPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        secondary_server: str | None = ...,
        tertiary_server: str | None = ...,
        status_ttl: int | None = ...,
        server_identity_check: Literal["enable", "disable"] | None = ...,
        source_ip: str | None = ...,
        source_ip_interface: str | None = ...,
        source_port: int | None = ...,
        cnid: str | None = ...,
        dn: str | None = ...,
        type: Literal["simple", "anonymous", "regular"] | None = ...,
        two_factor: Literal["disable", "fortitoken-cloud"] | None = ...,
        two_factor_authentication: Literal["fortitoken", "email", "sms"] | None = ...,
        two_factor_notification: Literal["email", "sms"] | None = ...,
        two_factor_filter: str | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        group_member_check: Literal["user-attr", "group-object", "posix-group-object"] | None = ...,
        group_search_base: str | None = ...,
        group_object_filter: str | None = ...,
        group_filter: str | None = ...,
        secure: Literal["disable", "starttls", "ldaps"] | None = ...,
        ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        ca_cert: str | None = ...,
        port: int | None = ...,
        password_expiry_warning: Literal["enable", "disable"] | None = ...,
        password_renewal: Literal["enable", "disable"] | None = ...,
        member_attr: str | None = ...,
        account_key_processing: Literal["same", "strip"] | None = ...,
        account_key_cert_field: Literal["othername", "rfc822name", "dnsname", "cn"] | None = ...,
        account_key_filter: str | None = ...,
        search_type: Literal["recursive"] | None = ...,
        client_cert_auth: Literal["enable", "disable"] | None = ...,
        client_cert: str | None = ...,
        obtain_user_info: Literal["enable", "disable"] | None = ...,
        user_info_exchange_server: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        antiphish: Literal["enable", "disable"] | None = ...,
        password_attr: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: LdapPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        secondary_server: str | None = ...,
        tertiary_server: str | None = ...,
        status_ttl: int | None = ...,
        server_identity_check: Literal["enable", "disable"] | None = ...,
        source_ip: str | None = ...,
        source_ip_interface: str | None = ...,
        source_port: int | None = ...,
        cnid: str | None = ...,
        dn: str | None = ...,
        type: Literal["simple", "anonymous", "regular"] | None = ...,
        two_factor: Literal["disable", "fortitoken-cloud"] | None = ...,
        two_factor_authentication: Literal["fortitoken", "email", "sms"] | None = ...,
        two_factor_notification: Literal["email", "sms"] | None = ...,
        two_factor_filter: str | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        group_member_check: Literal["user-attr", "group-object", "posix-group-object"] | None = ...,
        group_search_base: str | None = ...,
        group_object_filter: str | None = ...,
        group_filter: str | None = ...,
        secure: Literal["disable", "starttls", "ldaps"] | None = ...,
        ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        ca_cert: str | None = ...,
        port: int | None = ...,
        password_expiry_warning: Literal["enable", "disable"] | None = ...,
        password_renewal: Literal["enable", "disable"] | None = ...,
        member_attr: str | None = ...,
        account_key_processing: Literal["same", "strip"] | None = ...,
        account_key_cert_field: Literal["othername", "rfc822name", "dnsname", "cn"] | None = ...,
        account_key_filter: str | None = ...,
        search_type: Literal["recursive"] | None = ...,
        client_cert_auth: Literal["enable", "disable"] | None = ...,
        client_cert: str | None = ...,
        obtain_user_info: Literal["enable", "disable"] | None = ...,
        user_info_exchange_server: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        antiphish: Literal["enable", "disable"] | None = ...,
        password_attr: str | None = ...,
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
        payload_dict: LdapPayload | None = ...,
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
    "Ldap",
    "LdapPayload",
]