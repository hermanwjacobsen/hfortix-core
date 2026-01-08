from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class LocalPayload(TypedDict, total=False):
    """
    Type hints for user/local payload fields.
    
    Configure local users.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.sms-server.SmsServerEndpoint` (via: sms-custom-server)
        - :class:`~.user.fortitoken.FortitokenEndpoint` (via: fortitoken)
        - :class:`~.user.ldap.LdapEndpoint` (via: ldap-server)
        - :class:`~.user.password-policy.PasswordPolicyEndpoint` (via: passwd-policy)
        - :class:`~.user.radius.RadiusEndpoint` (via: radius-server)
        - :class:`~.user.saml.SamlEndpoint` (via: saml-server)
        - :class:`~.user.tacacs+.TacacsPlusEndpoint` (via: tacacs+-server)
        - :class:`~.vpn.qkd.QkdEndpoint` (via: qkd-profile)

    **Usage:**
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
    tacacs_plus_server: str  # Name of TACACS+ server with which the user must authenticate
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


class LocalObject(FortiObject[LocalPayload]):
    """Typed FortiObject for user/local with IDE autocomplete support."""
    
    # Local user name.
    name: str
    # User ID.
    id: int
    # Enable/disable allowing the local user to authenticate with the FortiGate unit.
    status: Literal["enable", "disable"]
    # Authentication method.
    type: Literal["password", "radius", "tacacs+", "ldap", "saml"]
    # User's password.
    passwd: str
    # Name of LDAP server with which the user must authenticate.
    ldap_server: str
    # Name of RADIUS server with which the user must authenticate.
    radius_server: str
    # Name of TACACS+ server with which the user must authenticate.
    tacacs_plus_server: str
    # Name of SAML server with which the user must authenticate.
    saml_server: str
    # Enable/disable two-factor authentication.
    two_factor: Literal["disable", "fortitoken", "fortitoken-cloud", "email", "sms"]
    # Authentication method by FortiToken Cloud.
    two_factor_authentication: Literal["fortitoken", "email", "sms"]
    # Notification method for user activation by FortiToken Cloud.
    two_factor_notification: Literal["email", "sms"]
    # Two-factor recipient's FortiToken serial number.
    fortitoken: str
    # Two-factor recipient's email address.
    email_to: str
    # Send SMS through FortiGuard or other external server.
    sms_server: Literal["fortiguard", "custom"]
    # Two-factor recipient's SMS server.
    sms_custom_server: str
    # Two-factor recipient's mobile phone number.
    sms_phone: str
    # Password policy to apply to this user, as defined in config user password-policy
    passwd_policy: str
    # Time of the last password update.
    passwd_time: str
    # Time in minutes before the authentication timeout for a user is reached.
    authtimeout: int
    # Name of the remote user workstation, if you want to limit the user to authentica
    workstation: str
    # Enable/disable overriding the policy-auth-concurrent under config system global.
    auth_concurrent_override: Literal["enable", "disable"]
    # Maximum number of concurrent logins permitted from the same user.
    auth_concurrent_value: int
    # IKEv2 Postquantum Preshared Key (ASCII string or hexadecimal encoded with a lead
    ppk_secret: str
    # IKEv2 Postquantum Preshared Key Identity.
    ppk_identity: str
    # Quantum Key Distribution (QKD) profile.
    qkd_profile: str
    # Enable/disable case and accent sensitivity when performing username matching (ac
    username_sensitivity: Literal["disable", "enable"]
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> LocalPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Local:
    """
    Configure local users.
    
    Path: user/local
    Category: cmdb
    Primary Key: name
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey provided)
    @overload
    def get(
        self,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        *,
        response_mode: Literal["object"],
        **kwargs: Any,
    ) -> LocalObject: ...
    
    # List of objects (no mkey provided - most specific for list returns)
    # For singleton endpoints (no mkey), returns single object; for table endpoints, returns list
    @overload
    def get(
        self,
        *,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"],
        **kwargs: Any,
    ) -> list[LocalObject]: ...
    
    @overload
    def get(
        self,
        name: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True],
        *,
        response_mode: Literal["object"],
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Dict mode with mkey provided (single dict)
    @overload
    def get(
        self,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Dict mode without mkey (returns dict with results array)
    @overload
    def get(
        self,
        name: None = None,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Default overload for dict mode
    @overload
    def get(
        self,
        name: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], list[dict[str, Any]]]: ...
    
    def get(
        self,
        name: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: str | None = ...,
        **kwargs: Any,
    ) -> LocalObject | list[LocalObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
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
        tacacs_plus_server: str | None = ...,
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
        workstation: str | None = ...,
        auth_concurrent_override: Literal["enable", "disable"] | None = ...,
        auth_concurrent_value: int | None = ...,
        ppk_secret: str | None = ...,
        ppk_identity: str | None = ...,
        qkd_profile: str | None = ...,
        username_sensitivity: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> LocalObject: ...
    
    @overload
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
        tacacs_plus_server: str | None = ...,
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
        workstation: str | None = ...,
        auth_concurrent_override: Literal["enable", "disable"] | None = ...,
        auth_concurrent_value: int | None = ...,
        ppk_secret: str | None = ...,
        ppk_identity: str | None = ...,
        qkd_profile: str | None = ...,
        username_sensitivity: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
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
        tacacs_plus_server: str | None = ...,
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
        workstation: str | None = ...,
        auth_concurrent_override: Literal["enable", "disable"] | None = ...,
        auth_concurrent_value: int | None = ...,
        ppk_secret: str | None = ...,
        ppk_identity: str | None = ...,
        qkd_profile: str | None = ...,
        username_sensitivity: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
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
        tacacs_plus_server: str | None = ...,
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
        workstation: str | None = ...,
        auth_concurrent_override: Literal["enable", "disable"] | None = ...,
        auth_concurrent_value: int | None = ...,
        ppk_secret: str | None = ...,
        ppk_identity: str | None = ...,
        qkd_profile: str | None = ...,
        username_sensitivity: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
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
        tacacs_plus_server: str | None = ...,
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
        workstation: str | None = ...,
        auth_concurrent_override: Literal["enable", "disable"] | None = ...,
        auth_concurrent_value: int | None = ...,
        ppk_secret: str | None = ...,
        ppk_identity: str | None = ...,
        qkd_profile: str | None = ...,
        username_sensitivity: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> LocalObject: ...
    
    @overload
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
        tacacs_plus_server: str | None = ...,
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
        workstation: str | None = ...,
        auth_concurrent_override: Literal["enable", "disable"] | None = ...,
        auth_concurrent_value: int | None = ...,
        ppk_secret: str | None = ...,
        ppk_identity: str | None = ...,
        qkd_profile: str | None = ...,
        username_sensitivity: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
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
        tacacs_plus_server: str | None = ...,
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
        workstation: str | None = ...,
        auth_concurrent_override: Literal["enable", "disable"] | None = ...,
        auth_concurrent_value: int | None = ...,
        ppk_secret: str | None = ...,
        ppk_identity: str | None = ...,
        qkd_profile: str | None = ...,
        username_sensitivity: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
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
        tacacs_plus_server: str | None = ...,
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
        workstation: str | None = ...,
        auth_concurrent_override: Literal["enable", "disable"] | None = ...,
        auth_concurrent_value: int | None = ...,
        ppk_secret: str | None = ...,
        ppk_identity: str | None = ...,
        qkd_profile: str | None = ...,
        username_sensitivity: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> LocalObject: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: LocalPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["password", "radius", "tacacs+", "ldap", "saml"] | None = ...,
        passwd: str | None = ...,
        ldap_server: str | None = ...,
        radius_server: str | None = ...,
        tacacs_plus_server: str | None = ...,
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
        workstation: str | None = ...,
        auth_concurrent_override: Literal["enable", "disable"] | None = ...,
        auth_concurrent_value: int | None = ...,
        ppk_secret: str | None = ...,
        ppk_identity: str | None = ...,
        qkd_profile: str | None = ...,
        username_sensitivity: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
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
    "Local",
    "LocalPayload",
    "LocalObject",
]