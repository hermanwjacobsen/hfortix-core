from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class LocalPayload(TypedDict, total=False):
    """
    Type hints for user/local payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: LocalPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Local user name.
    id: NotRequired[int]  # User ID.
    status: Literal["enable", "disable"]  # Enable/disable allowing the local user to authenticate with 
    type: Literal["password", "radius", "tacacs+", "ldap", "saml"]  # Authentication method.
    passwd: str  # User's password.
    ldap_server: str  # Name of LDAP server with which the user must authenticate.
    radius_server: str  # Name of RADIUS server with which the user must authenticate.
    tacacs+_server: str  # Name of TACACS+ server with which the user must authenticate
    saml_server: str  # Name of SAML server with which the user must authenticate.
    two_factor: NotRequired[Literal["disable", "fortitoken", "fortitoken-cloud", "email", "sms"]]  # Enable/disable two-factor authentication.
    two_factor_authentication: NotRequired[Literal["fortitoken", "email", "sms"]]  # Authentication method by FortiToken Cloud.
    two_factor_notification: NotRequired[Literal["email", "sms"]]  # Notification method for user activation by FortiToken Cloud.
    fortitoken: NotRequired[str]  # Two-factor recipient's FortiToken serial number.
    email_to: NotRequired[str]  # Two-factor recipient's email address.
    sms_server: NotRequired[Literal["fortiguard", "custom"]]  # Send SMS through FortiGuard or other external server.
    sms_custom_server: NotRequired[str]  # Two-factor recipient's SMS server.
    sms_phone: NotRequired[str]  # Two-factor recipient's mobile phone number.
    passwd_policy: NotRequired[str]  # Password policy to apply to this user, as defined in config 
    passwd_time: NotRequired[str]  # Time of the last password update.
    authtimeout: NotRequired[int]  # Time in minutes before the authentication timeout for a user
    workstation: NotRequired[str]  # Name of the remote user workstation, if you want to limit th
    auth_concurrent_override: NotRequired[Literal["enable", "disable"]]  # Enable/disable overriding the policy-auth-concurrent under c
    auth_concurrent_value: NotRequired[int]  # Maximum number of concurrent logins permitted from the same 
    ppk_secret: NotRequired[str]  # IKEv2 Postquantum Preshared Key (ASCII string or hexadecimal
    ppk_identity: NotRequired[str]  # IKEv2 Postquantum Preshared Key Identity.
    qkd_profile: NotRequired[str]  # Quantum Key Distribution (QKD) profile.
    username_sensitivity: NotRequired[Literal["disable", "enable"]]  # Enable/disable case and accent sensitivity when performing u


class Local:
    """
    Configure local users.
    
    Path: user/local
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
        payload_dict: LocalPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["password", "radius", "tacacs+", "ldap", "saml"] | None = ...,
        passwd: str | None = ...,
        ldap_server: str | None = ...,
        radius_server: str | None = ...,
        tacacs+_server: str | None = ...,
        saml_server: str | None = ...,
        two_factor: Literal["disable", "fortitoken", "fortitoken-cloud", "email", "sms"] | None = ...,
        two_factor_authentication: Literal["fortitoken", "email", "sms"] | None = ...,
        two_factor_notification: Literal["email", "sms"] | None = ...,
        fortitoken: str | None = ...,
        email_to: str | None = ...,
        sms_server: Literal["fortiguard", "custom"] | None = ...,
        sms_custom_server: str | None = ...,
        sms_phone: str | None = ...,
        passwd_policy: str | None = ...,
        passwd_time: str | None = ...,
        authtimeout: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: LocalPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["password", "radius", "tacacs+", "ldap", "saml"] | None = ...,
        passwd: str | None = ...,
        ldap_server: str | None = ...,
        radius_server: str | None = ...,
        tacacs+_server: str | None = ...,
        saml_server: str | None = ...,
        two_factor: Literal["disable", "fortitoken", "fortitoken-cloud", "email", "sms"] | None = ...,
        two_factor_authentication: Literal["fortitoken", "email", "sms"] | None = ...,
        two_factor_notification: Literal["email", "sms"] | None = ...,
        fortitoken: str | None = ...,
        email_to: str | None = ...,
        sms_server: Literal["fortiguard", "custom"] | None = ...,
        sms_custom_server: str | None = ...,
        sms_phone: str | None = ...,
        passwd_policy: str | None = ...,
        passwd_time: str | None = ...,
        authtimeout: int | None = ...,
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
        payload_dict: LocalPayload | None = ...,
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