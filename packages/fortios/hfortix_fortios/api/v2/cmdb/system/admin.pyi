from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class AdminPayload(TypedDict, total=False):
    """
    Type hints for system/admin payload fields.
    
    Configure admin users.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.certificate.remote.RemoteEndpoint` (via: ssh-certificate)
        - :class:`~.system.accprofile.AccprofileEndpoint` (via: accprofile)
        - :class:`~.system.custom-language.CustomLanguageEndpoint` (via: guest-lang)
        - :class:`~.system.sms-server.SmsServerEndpoint` (via: sms-custom-server)

    **Usage:**
        payload: AdminPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # User name.
    vdom: NotRequired[list[dict[str, Any]]]  # Virtual domain(s) that the administrator can access.
    remote_auth: NotRequired[Literal["enable", "disable"]]  # Enable/disable authentication using a remote RADIUS, LDAP, o
    remote_group: str  # User group name used for remote auth.
    wildcard: NotRequired[Literal["enable", "disable"]]  # Enable/disable wildcard RADIUS authentication.
    password: str  # Admin user password.
    peer_auth: NotRequired[Literal["enable", "disable"]]  # Set to enable peer certificate authentication
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

# Nested classes for table field children

@final
class AdminVdomObject:
    """Typed object for vdom table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Virtual domain name.
    name: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class AdminGuestusergroupsObject:
    """Typed object for guest-usergroups table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Select guest user groups.
    name: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...



# Response TypedDict for GET returns (all fields present in API response)
class AdminResponse(TypedDict):
    """
    Type hints for system/admin API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str
    vdom: list[dict[str, Any]]
    remote_auth: Literal["enable", "disable"]
    remote_group: str
    wildcard: Literal["enable", "disable"]
    password: str
    peer_auth: Literal["enable", "disable"]
    peer_group: str
    trusthost1: str
    trusthost2: str
    trusthost3: str
    trusthost4: str
    trusthost5: str
    trusthost6: str
    trusthost7: str
    trusthost8: str
    trusthost9: str
    trusthost10: str
    ip6_trusthost1: str
    ip6_trusthost2: str
    ip6_trusthost3: str
    ip6_trusthost4: str
    ip6_trusthost5: str
    ip6_trusthost6: str
    ip6_trusthost7: str
    ip6_trusthost8: str
    ip6_trusthost9: str
    ip6_trusthost10: str
    accprofile: str
    allow_remove_admin_session: Literal["enable", "disable"]
    comments: str
    ssh_public_key1: str
    ssh_public_key2: str
    ssh_public_key3: str
    ssh_certificate: str
    schedule: str
    accprofile_override: Literal["enable", "disable"]
    vdom_override: Literal["enable", "disable"]
    password_expire: str
    force_password_change: Literal["enable", "disable"]
    two_factor: Literal["disable", "fortitoken", "fortitoken-cloud", "email", "sms"]
    two_factor_authentication: Literal["fortitoken", "email", "sms"]
    two_factor_notification: Literal["email", "sms"]
    fortitoken: str
    email_to: str
    sms_server: Literal["fortiguard", "custom"]
    sms_custom_server: str
    sms_phone: str
    guest_auth: Literal["disable", "enable"]
    guest_usergroups: list[dict[str, Any]]
    guest_lang: str
    status: str
    list: str


@final
class AdminObject:
    """Typed FortiObject for system/admin with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # User name.
    name: str
    # Virtual domain(s) that the administrator can access.
    vdom: list[AdminVdomObject]  # Table field - list of typed objects
    # Enable/disable authentication using a remote RADIUS, LDAP, or TACACS+ server.
    remote_auth: Literal["enable", "disable"]
    # User group name used for remote auth.
    remote_group: str
    # Enable/disable wildcard RADIUS authentication.
    wildcard: Literal["enable", "disable"]
    # Admin user password.
    password: str
    # Set to enable peer certificate authentication (for HTTPS admin access).
    peer_auth: Literal["enable", "disable"]
    # Name of peer group defined under config user group which has PKI members. Used f
    peer_group: str
    # Any IPv4 address or subnet address and netmask from which the administrator can
    trusthost1: str
    # Any IPv4 address or subnet address and netmask from which the administrator can
    trusthost2: str
    # Any IPv4 address or subnet address and netmask from which the administrator can
    trusthost3: str
    # Any IPv4 address or subnet address and netmask from which the administrator can
    trusthost4: str
    # Any IPv4 address or subnet address and netmask from which the administrator can
    trusthost5: str
    # Any IPv4 address or subnet address and netmask from which the administrator can
    trusthost6: str
    # Any IPv4 address or subnet address and netmask from which the administrator can
    trusthost7: str
    # Any IPv4 address or subnet address and netmask from which the administrator can
    trusthost8: str
    # Any IPv4 address or subnet address and netmask from which the administrator can
    trusthost9: str
    # Any IPv4 address or subnet address and netmask from which the administrator can
    trusthost10: str
    # Any IPv6 address from which the administrator can connect to the FortiGate unit.
    ip6_trusthost1: str
    # Any IPv6 address from which the administrator can connect to the FortiGate unit.
    ip6_trusthost2: str
    # Any IPv6 address from which the administrator can connect to the FortiGate unit.
    ip6_trusthost3: str
    # Any IPv6 address from which the administrator can connect to the FortiGate unit.
    ip6_trusthost4: str
    # Any IPv6 address from which the administrator can connect to the FortiGate unit.
    ip6_trusthost5: str
    # Any IPv6 address from which the administrator can connect to the FortiGate unit.
    ip6_trusthost6: str
    # Any IPv6 address from which the administrator can connect to the FortiGate unit.
    ip6_trusthost7: str
    # Any IPv6 address from which the administrator can connect to the FortiGate unit.
    ip6_trusthost8: str
    # Any IPv6 address from which the administrator can connect to the FortiGate unit.
    ip6_trusthost9: str
    # Any IPv6 address from which the administrator can connect to the FortiGate unit.
    ip6_trusthost10: str
    # Access profile for this administrator. Access profiles control administrator acc
    accprofile: str
    # Enable/disable allow admin session to be removed by privileged admin users.
    allow_remove_admin_session: Literal["enable", "disable"]
    # Comment.
    comments: str
    # Public key of an SSH client. The client is authenticated without being asked for
    ssh_public_key1: str
    # Public key of an SSH client. The client is authenticated without being asked for
    ssh_public_key2: str
    # Public key of an SSH client. The client is authenticated without being asked for
    ssh_public_key3: str
    # Select the certificate to be used by the FortiGate for authentication with an SS
    ssh_certificate: str
    # Firewall schedule used to restrict when the administrator can log in. No schedul
    schedule: str
    # Enable to use the name of an access profile provided by the remote authenticatio
    accprofile_override: Literal["enable", "disable"]
    # Enable to use the names of VDOMs provided by the remote authentication server to
    vdom_override: Literal["enable", "disable"]
    # Password expire time.
    password_expire: str
    # Enable/disable force password change on next login.
    force_password_change: Literal["enable", "disable"]
    # Enable/disable two-factor authentication.
    two_factor: Literal["disable", "fortitoken", "fortitoken-cloud", "email", "sms"]
    # Authentication method by FortiToken Cloud.
    two_factor_authentication: Literal["fortitoken", "email", "sms"]
    # Notification method for user activation by FortiToken Cloud.
    two_factor_notification: Literal["email", "sms"]
    # This administrator's FortiToken serial number.
    fortitoken: str
    # This administrator's email address.
    email_to: str
    # Send SMS messages using the FortiGuard SMS server or a custom server.
    sms_server: Literal["fortiguard", "custom"]
    # Custom SMS server to send SMS messages to.
    sms_custom_server: str
    # Phone number on which the administrator receives SMS messages.
    sms_phone: str
    # Enable/disable guest authentication.
    guest_auth: Literal["disable", "enable"]
    # Select guest user groups.
    guest_usergroups: list[AdminGuestusergroupsObject]  # Table field - list of typed objects
    # Guest management portal language.
    guest_lang: str
    # print admin status information
    status: str
    # print admin list information
    list: str
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> AdminPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class Admin:
    """
    Configure admin users.
    
    Path: system/admin
    Category: cmdb
    Primary Key: name
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey/name provided as positional arg)
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
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> AdminObject: ...
    
    # Single object (mkey/name provided as keyword arg)
    @overload
    def get(
        self,
        *,
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
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> AdminObject: ...
    
    # List of objects (no mkey/name provided) - keyword-only signature
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
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> list[AdminObject]: ...
    
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
        raw_json: Literal[True] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Dict mode with mkey provided as positional arg (single dict)
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
    ) -> AdminResponse: ...
    
    # Dict mode with mkey provided as keyword arg (single dict)
    @overload
    def get(
        self,
        *,
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
    ) -> AdminResponse: ...
    
    # Dict mode - list of dicts (no mkey/name provided) - keyword-only signature
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
        response_mode: Literal["dict"] = ...,
        **kwargs: Any,
    ) -> list[AdminResponse]: ...
    
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
    ) -> AdminObject | list[AdminObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: AdminPayload | None = ...,
        name: str | None = ...,
        remote_auth: Literal["enable", "disable"] | None = ...,
        remote_group: str | None = ...,
        wildcard: Literal["enable", "disable"] | None = ...,
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
        ip6_trusthost4: str | None = ...,
        ip6_trusthost5: str | None = ...,
        ip6_trusthost6: str | None = ...,
        ip6_trusthost7: str | None = ...,
        ip6_trusthost8: str | None = ...,
        ip6_trusthost9: str | None = ...,
        ip6_trusthost10: str | None = ...,
        accprofile: str | None = ...,
        allow_remove_admin_session: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        ssh_public_key1: str | None = ...,
        ssh_public_key2: str | None = ...,
        ssh_public_key3: str | None = ...,
        ssh_certificate: str | None = ...,
        schedule: str | None = ...,
        accprofile_override: Literal["enable", "disable"] | None = ...,
        vdom_override: Literal["enable", "disable"] | None = ...,
        password_expire: str | None = ...,
        force_password_change: Literal["enable", "disable"] | None = ...,
        two_factor: Literal["disable", "fortitoken", "fortitoken-cloud", "email", "sms"] | None = ...,
        two_factor_authentication: Literal["fortitoken", "email", "sms"] | None = ...,
        two_factor_notification: Literal["email", "sms"] | None = ...,
        fortitoken: str | None = ...,
        email_to: str | None = ...,
        sms_server: Literal["fortiguard", "custom"] | None = ...,
        sms_custom_server: str | None = ...,
        sms_phone: str | None = ...,
        guest_auth: Literal["disable", "enable"] | None = ...,
        guest_usergroups: str | list[str] | list[dict[str, Any]] | None = ...,
        guest_lang: str | None = ...,
        status: str | None = ...,
        list: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> AdminObject: ...
    
    @overload
    def post(
        self,
        payload_dict: AdminPayload | None = ...,
        name: str | None = ...,
        remote_auth: Literal["enable", "disable"] | None = ...,
        remote_group: str | None = ...,
        wildcard: Literal["enable", "disable"] | None = ...,
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
        ip6_trusthost4: str | None = ...,
        ip6_trusthost5: str | None = ...,
        ip6_trusthost6: str | None = ...,
        ip6_trusthost7: str | None = ...,
        ip6_trusthost8: str | None = ...,
        ip6_trusthost9: str | None = ...,
        ip6_trusthost10: str | None = ...,
        accprofile: str | None = ...,
        allow_remove_admin_session: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        ssh_public_key1: str | None = ...,
        ssh_public_key2: str | None = ...,
        ssh_public_key3: str | None = ...,
        ssh_certificate: str | None = ...,
        schedule: str | None = ...,
        accprofile_override: Literal["enable", "disable"] | None = ...,
        vdom_override: Literal["enable", "disable"] | None = ...,
        password_expire: str | None = ...,
        force_password_change: Literal["enable", "disable"] | None = ...,
        two_factor: Literal["disable", "fortitoken", "fortitoken-cloud", "email", "sms"] | None = ...,
        two_factor_authentication: Literal["fortitoken", "email", "sms"] | None = ...,
        two_factor_notification: Literal["email", "sms"] | None = ...,
        fortitoken: str | None = ...,
        email_to: str | None = ...,
        sms_server: Literal["fortiguard", "custom"] | None = ...,
        sms_custom_server: str | None = ...,
        sms_phone: str | None = ...,
        guest_auth: Literal["disable", "enable"] | None = ...,
        guest_usergroups: str | list[str] | list[dict[str, Any]] | None = ...,
        guest_lang: str | None = ...,
        status: str | None = ...,
        list: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: AdminPayload | None = ...,
        name: str | None = ...,
        remote_auth: Literal["enable", "disable"] | None = ...,
        remote_group: str | None = ...,
        wildcard: Literal["enable", "disable"] | None = ...,
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
        ip6_trusthost4: str | None = ...,
        ip6_trusthost5: str | None = ...,
        ip6_trusthost6: str | None = ...,
        ip6_trusthost7: str | None = ...,
        ip6_trusthost8: str | None = ...,
        ip6_trusthost9: str | None = ...,
        ip6_trusthost10: str | None = ...,
        accprofile: str | None = ...,
        allow_remove_admin_session: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        ssh_public_key1: str | None = ...,
        ssh_public_key2: str | None = ...,
        ssh_public_key3: str | None = ...,
        ssh_certificate: str | None = ...,
        schedule: str | None = ...,
        accprofile_override: Literal["enable", "disable"] | None = ...,
        vdom_override: Literal["enable", "disable"] | None = ...,
        password_expire: str | None = ...,
        force_password_change: Literal["enable", "disable"] | None = ...,
        two_factor: Literal["disable", "fortitoken", "fortitoken-cloud", "email", "sms"] | None = ...,
        two_factor_authentication: Literal["fortitoken", "email", "sms"] | None = ...,
        two_factor_notification: Literal["email", "sms"] | None = ...,
        fortitoken: str | None = ...,
        email_to: str | None = ...,
        sms_server: Literal["fortiguard", "custom"] | None = ...,
        sms_custom_server: str | None = ...,
        sms_phone: str | None = ...,
        guest_auth: Literal["disable", "enable"] | None = ...,
        guest_usergroups: str | list[str] | list[dict[str, Any]] | None = ...,
        guest_lang: str | None = ...,
        status: str | None = ...,
        list: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: AdminPayload | None = ...,
        name: str | None = ...,
        remote_auth: Literal["enable", "disable"] | None = ...,
        remote_group: str | None = ...,
        wildcard: Literal["enable", "disable"] | None = ...,
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
        ip6_trusthost4: str | None = ...,
        ip6_trusthost5: str | None = ...,
        ip6_trusthost6: str | None = ...,
        ip6_trusthost7: str | None = ...,
        ip6_trusthost8: str | None = ...,
        ip6_trusthost9: str | None = ...,
        ip6_trusthost10: str | None = ...,
        accprofile: str | None = ...,
        allow_remove_admin_session: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        ssh_public_key1: str | None = ...,
        ssh_public_key2: str | None = ...,
        ssh_public_key3: str | None = ...,
        ssh_certificate: str | None = ...,
        schedule: str | None = ...,
        accprofile_override: Literal["enable", "disable"] | None = ...,
        vdom_override: Literal["enable", "disable"] | None = ...,
        password_expire: str | None = ...,
        force_password_change: Literal["enable", "disable"] | None = ...,
        two_factor: Literal["disable", "fortitoken", "fortitoken-cloud", "email", "sms"] | None = ...,
        two_factor_authentication: Literal["fortitoken", "email", "sms"] | None = ...,
        two_factor_notification: Literal["email", "sms"] | None = ...,
        fortitoken: str | None = ...,
        email_to: str | None = ...,
        sms_server: Literal["fortiguard", "custom"] | None = ...,
        sms_custom_server: str | None = ...,
        sms_phone: str | None = ...,
        guest_auth: Literal["disable", "enable"] | None = ...,
        guest_usergroups: str | list[str] | list[dict[str, Any]] | None = ...,
        guest_lang: str | None = ...,
        status: str | None = ...,
        list: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: AdminPayload | None = ...,
        name: str | None = ...,
        remote_auth: Literal["enable", "disable"] | None = ...,
        remote_group: str | None = ...,
        wildcard: Literal["enable", "disable"] | None = ...,
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
        ip6_trusthost4: str | None = ...,
        ip6_trusthost5: str | None = ...,
        ip6_trusthost6: str | None = ...,
        ip6_trusthost7: str | None = ...,
        ip6_trusthost8: str | None = ...,
        ip6_trusthost9: str | None = ...,
        ip6_trusthost10: str | None = ...,
        accprofile: str | None = ...,
        allow_remove_admin_session: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        ssh_public_key1: str | None = ...,
        ssh_public_key2: str | None = ...,
        ssh_public_key3: str | None = ...,
        ssh_certificate: str | None = ...,
        schedule: str | None = ...,
        accprofile_override: Literal["enable", "disable"] | None = ...,
        vdom_override: Literal["enable", "disable"] | None = ...,
        password_expire: str | None = ...,
        force_password_change: Literal["enable", "disable"] | None = ...,
        two_factor: Literal["disable", "fortitoken", "fortitoken-cloud", "email", "sms"] | None = ...,
        two_factor_authentication: Literal["fortitoken", "email", "sms"] | None = ...,
        two_factor_notification: Literal["email", "sms"] | None = ...,
        fortitoken: str | None = ...,
        email_to: str | None = ...,
        sms_server: Literal["fortiguard", "custom"] | None = ...,
        sms_custom_server: str | None = ...,
        sms_phone: str | None = ...,
        guest_auth: Literal["disable", "enable"] | None = ...,
        guest_usergroups: str | list[str] | list[dict[str, Any]] | None = ...,
        guest_lang: str | None = ...,
        status: str | None = ...,
        list: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> AdminObject: ...
    
    @overload
    def put(
        self,
        payload_dict: AdminPayload | None = ...,
        name: str | None = ...,
        remote_auth: Literal["enable", "disable"] | None = ...,
        remote_group: str | None = ...,
        wildcard: Literal["enable", "disable"] | None = ...,
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
        ip6_trusthost4: str | None = ...,
        ip6_trusthost5: str | None = ...,
        ip6_trusthost6: str | None = ...,
        ip6_trusthost7: str | None = ...,
        ip6_trusthost8: str | None = ...,
        ip6_trusthost9: str | None = ...,
        ip6_trusthost10: str | None = ...,
        accprofile: str | None = ...,
        allow_remove_admin_session: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        ssh_public_key1: str | None = ...,
        ssh_public_key2: str | None = ...,
        ssh_public_key3: str | None = ...,
        ssh_certificate: str | None = ...,
        schedule: str | None = ...,
        accprofile_override: Literal["enable", "disable"] | None = ...,
        vdom_override: Literal["enable", "disable"] | None = ...,
        password_expire: str | None = ...,
        force_password_change: Literal["enable", "disable"] | None = ...,
        two_factor: Literal["disable", "fortitoken", "fortitoken-cloud", "email", "sms"] | None = ...,
        two_factor_authentication: Literal["fortitoken", "email", "sms"] | None = ...,
        two_factor_notification: Literal["email", "sms"] | None = ...,
        fortitoken: str | None = ...,
        email_to: str | None = ...,
        sms_server: Literal["fortiguard", "custom"] | None = ...,
        sms_custom_server: str | None = ...,
        sms_phone: str | None = ...,
        guest_auth: Literal["disable", "enable"] | None = ...,
        guest_usergroups: str | list[str] | list[dict[str, Any]] | None = ...,
        guest_lang: str | None = ...,
        status: str | None = ...,
        list: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: AdminPayload | None = ...,
        name: str | None = ...,
        remote_auth: Literal["enable", "disable"] | None = ...,
        remote_group: str | None = ...,
        wildcard: Literal["enable", "disable"] | None = ...,
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
        ip6_trusthost4: str | None = ...,
        ip6_trusthost5: str | None = ...,
        ip6_trusthost6: str | None = ...,
        ip6_trusthost7: str | None = ...,
        ip6_trusthost8: str | None = ...,
        ip6_trusthost9: str | None = ...,
        ip6_trusthost10: str | None = ...,
        accprofile: str | None = ...,
        allow_remove_admin_session: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        ssh_public_key1: str | None = ...,
        ssh_public_key2: str | None = ...,
        ssh_public_key3: str | None = ...,
        ssh_certificate: str | None = ...,
        schedule: str | None = ...,
        accprofile_override: Literal["enable", "disable"] | None = ...,
        vdom_override: Literal["enable", "disable"] | None = ...,
        password_expire: str | None = ...,
        force_password_change: Literal["enable", "disable"] | None = ...,
        two_factor: Literal["disable", "fortitoken", "fortitoken-cloud", "email", "sms"] | None = ...,
        two_factor_authentication: Literal["fortitoken", "email", "sms"] | None = ...,
        two_factor_notification: Literal["email", "sms"] | None = ...,
        fortitoken: str | None = ...,
        email_to: str | None = ...,
        sms_server: Literal["fortiguard", "custom"] | None = ...,
        sms_custom_server: str | None = ...,
        sms_phone: str | None = ...,
        guest_auth: Literal["disable", "enable"] | None = ...,
        guest_usergroups: str | list[str] | list[dict[str, Any]] | None = ...,
        guest_lang: str | None = ...,
        status: str | None = ...,
        list: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: AdminPayload | None = ...,
        name: str | None = ...,
        remote_auth: Literal["enable", "disable"] | None = ...,
        remote_group: str | None = ...,
        wildcard: Literal["enable", "disable"] | None = ...,
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
        ip6_trusthost4: str | None = ...,
        ip6_trusthost5: str | None = ...,
        ip6_trusthost6: str | None = ...,
        ip6_trusthost7: str | None = ...,
        ip6_trusthost8: str | None = ...,
        ip6_trusthost9: str | None = ...,
        ip6_trusthost10: str | None = ...,
        accprofile: str | None = ...,
        allow_remove_admin_session: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        ssh_public_key1: str | None = ...,
        ssh_public_key2: str | None = ...,
        ssh_public_key3: str | None = ...,
        ssh_certificate: str | None = ...,
        schedule: str | None = ...,
        accprofile_override: Literal["enable", "disable"] | None = ...,
        vdom_override: Literal["enable", "disable"] | None = ...,
        password_expire: str | None = ...,
        force_password_change: Literal["enable", "disable"] | None = ...,
        two_factor: Literal["disable", "fortitoken", "fortitoken-cloud", "email", "sms"] | None = ...,
        two_factor_authentication: Literal["fortitoken", "email", "sms"] | None = ...,
        two_factor_notification: Literal["email", "sms"] | None = ...,
        fortitoken: str | None = ...,
        email_to: str | None = ...,
        sms_server: Literal["fortiguard", "custom"] | None = ...,
        sms_custom_server: str | None = ...,
        sms_phone: str | None = ...,
        guest_auth: Literal["disable", "enable"] | None = ...,
        guest_usergroups: str | list[str] | list[dict[str, Any]] | None = ...,
        guest_lang: str | None = ...,
        status: str | None = ...,
        list: str | None = ...,
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
    ) -> AdminObject: ...
    
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
        payload_dict: AdminPayload | None = ...,
        name: str | None = ...,
        remote_auth: Literal["enable", "disable"] | None = ...,
        remote_group: str | None = ...,
        wildcard: Literal["enable", "disable"] | None = ...,
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
        ip6_trusthost4: str | None = ...,
        ip6_trusthost5: str | None = ...,
        ip6_trusthost6: str | None = ...,
        ip6_trusthost7: str | None = ...,
        ip6_trusthost8: str | None = ...,
        ip6_trusthost9: str | None = ...,
        ip6_trusthost10: str | None = ...,
        accprofile: str | None = ...,
        allow_remove_admin_session: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        ssh_public_key1: str | None = ...,
        ssh_public_key2: str | None = ...,
        ssh_public_key3: str | None = ...,
        ssh_certificate: str | None = ...,
        schedule: str | None = ...,
        accprofile_override: Literal["enable", "disable"] | None = ...,
        vdom_override: Literal["enable", "disable"] | None = ...,
        password_expire: str | None = ...,
        force_password_change: Literal["enable", "disable"] | None = ...,
        two_factor: Literal["disable", "fortitoken", "fortitoken-cloud", "email", "sms"] | None = ...,
        two_factor_authentication: Literal["fortitoken", "email", "sms"] | None = ...,
        two_factor_notification: Literal["email", "sms"] | None = ...,
        fortitoken: str | None = ...,
        email_to: str | None = ...,
        sms_server: Literal["fortiguard", "custom"] | None = ...,
        sms_custom_server: str | None = ...,
        sms_phone: str | None = ...,
        guest_auth: Literal["disable", "enable"] | None = ...,
        guest_usergroups: str | list[str] | list[dict[str, Any]] | None = ...,
        guest_lang: str | None = ...,
        status: str | None = ...,
        list: str | None = ...,
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
    "Admin",
    "AdminPayload",
    "AdminObject",
]