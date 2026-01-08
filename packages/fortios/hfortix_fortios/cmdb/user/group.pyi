from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class GroupPayload(TypedDict, total=False):
    """
    Type hints for user/group payload fields.
    
    Configure user groups.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.sms-server.SmsServerEndpoint` (via: sms-custom-server)

    **Usage:**
        payload: GroupPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Group name.
    id: NotRequired[int]  # Group ID.
    group_type: NotRequired[Literal["firewall", "fsso-service", "rsso", "guest"]]  # Set the group to be for firewall authentication, FSSO, RSSO,
    authtimeout: NotRequired[int]  # Authentication timeout in minutes for this user group. 0 to 
    auth_concurrent_override: NotRequired[Literal["enable", "disable"]]  # Enable/disable overriding the global number of concurrent au
    auth_concurrent_value: NotRequired[int]  # Maximum number of concurrent authenticated connections per u
    http_digest_realm: NotRequired[str]  # Realm attribute for MD5-digest authentication.
    sso_attribute_value: NotRequired[str]  # RADIUS attribute value.
    member: NotRequired[list[dict[str, Any]]]  # Names of users, peers, LDAP severs, RADIUS servers or extern
    match: NotRequired[list[dict[str, Any]]]  # Group matches.
    user_id: NotRequired[Literal["email", "auto-generate", "specify"]]  # Guest user ID type.
    password: NotRequired[Literal["auto-generate", "specify", "disable"]]  # Guest user password type.
    user_name: NotRequired[Literal["disable", "enable"]]  # Enable/disable the guest user name entry.
    sponsor: NotRequired[Literal["optional", "mandatory", "disabled"]]  # Set the action for the sponsor guest user field.
    company: NotRequired[Literal["optional", "mandatory", "disabled"]]  # Set the action for the company guest user field.
    email: NotRequired[Literal["disable", "enable"]]  # Enable/disable the guest user email address field.
    mobile_phone: NotRequired[Literal["disable", "enable"]]  # Enable/disable the guest user mobile phone number field.
    sms_server: NotRequired[Literal["fortiguard", "custom"]]  # Send SMS through FortiGuard or other external server.
    sms_custom_server: NotRequired[str]  # SMS server.
    expire_type: NotRequired[Literal["immediately", "first-successful-login"]]  # Determine when the expiration countdown begins.
    expire: NotRequired[int]  # Time in seconds before guest user accounts expire (1 - 31536
    max_accounts: NotRequired[int]  # Maximum number of guest accounts that can be created for thi
    multiple_guest_add: NotRequired[Literal["disable", "enable"]]  # Enable/disable addition of multiple guests.
    guest: NotRequired[list[dict[str, Any]]]  # Guest User.


class GroupObject(FortiObject[GroupPayload]):
    """Typed FortiObject for user/group with IDE autocomplete support."""
    
    # Group name.
    name: str
    # Group ID.
    id: int
    # Set the group to be for firewall authentication, FSSO, RSSO, or guest users.
    group_type: Literal["firewall", "fsso-service", "rsso", "guest"]
    # Authentication timeout in minutes for this user group. 0 to use the global user 
    authtimeout: int
    # Enable/disable overriding the global number of concurrent authentication session
    auth_concurrent_override: Literal["enable", "disable"]
    # Maximum number of concurrent authenticated connections per user (0 - 100).
    auth_concurrent_value: int
    # Realm attribute for MD5-digest authentication.
    http_digest_realm: str
    # RADIUS attribute value.
    sso_attribute_value: str
    # Names of users, peers, LDAP severs, RADIUS servers or external idp servers to ad
    member: list[str]  # Auto-flattened from member_table
    # Group matches.
    match: list[str]  # Auto-flattened from member_table
    # Guest user ID type.
    user_id: Literal["email", "auto-generate", "specify"]
    # Guest user password type.
    password: Literal["auto-generate", "specify", "disable"]
    # Enable/disable the guest user name entry.
    user_name: Literal["disable", "enable"]
    # Set the action for the sponsor guest user field.
    sponsor: Literal["optional", "mandatory", "disabled"]
    # Set the action for the company guest user field.
    company: Literal["optional", "mandatory", "disabled"]
    # Enable/disable the guest user email address field.
    email: Literal["disable", "enable"]
    # Enable/disable the guest user mobile phone number field.
    mobile_phone: Literal["disable", "enable"]
    # Send SMS through FortiGuard or other external server.
    sms_server: Literal["fortiguard", "custom"]
    # SMS server.
    sms_custom_server: str
    # Determine when the expiration countdown begins.
    expire_type: Literal["immediately", "first-successful-login"]
    # Time in seconds before guest user accounts expire (1 - 31536000).
    expire: int
    # Maximum number of guest accounts that can be created for this group (0 means unl
    max_accounts: int
    # Enable/disable addition of multiple guests.
    multiple_guest_add: Literal["disable", "enable"]
    # Guest User.
    guest: list[str]  # Auto-flattened from member_table
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> GroupPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Group:
    """
    Configure user groups.
    
    Path: user/group
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
    ) -> GroupObject: ...
    
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
    ) -> list[GroupObject]: ...
    
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
    ) -> GroupObject | list[GroupObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: GroupPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        group_type: Literal["firewall", "fsso-service", "rsso", "guest"] | None = ...,
        authtimeout: int | None = ...,
        auth_concurrent_override: Literal["enable", "disable"] | None = ...,
        auth_concurrent_value: int | None = ...,
        http_digest_realm: str | None = ...,
        sso_attribute_value: str | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        match: str | list[str] | list[dict[str, Any]] | None = ...,
        user_id: Literal["email", "auto-generate", "specify"] | None = ...,
        password: Literal["auto-generate", "specify", "disable"] | None = ...,
        user_name: Literal["disable", "enable"] | None = ...,
        sponsor: Literal["optional", "mandatory", "disabled"] | None = ...,
        company: Literal["optional", "mandatory", "disabled"] | None = ...,
        email: Literal["disable", "enable"] | None = ...,
        mobile_phone: Literal["disable", "enable"] | None = ...,
        sms_server: Literal["fortiguard", "custom"] | None = ...,
        sms_custom_server: str | None = ...,
        expire_type: Literal["immediately", "first-successful-login"] | None = ...,
        expire: int | None = ...,
        max_accounts: int | None = ...,
        multiple_guest_add: Literal["disable", "enable"] | None = ...,
        guest: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> GroupObject: ...
    
    @overload
    def post(
        self,
        payload_dict: GroupPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        group_type: Literal["firewall", "fsso-service", "rsso", "guest"] | None = ...,
        authtimeout: int | None = ...,
        auth_concurrent_override: Literal["enable", "disable"] | None = ...,
        auth_concurrent_value: int | None = ...,
        http_digest_realm: str | None = ...,
        sso_attribute_value: str | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        match: str | list[str] | list[dict[str, Any]] | None = ...,
        user_id: Literal["email", "auto-generate", "specify"] | None = ...,
        password: Literal["auto-generate", "specify", "disable"] | None = ...,
        user_name: Literal["disable", "enable"] | None = ...,
        sponsor: Literal["optional", "mandatory", "disabled"] | None = ...,
        company: Literal["optional", "mandatory", "disabled"] | None = ...,
        email: Literal["disable", "enable"] | None = ...,
        mobile_phone: Literal["disable", "enable"] | None = ...,
        sms_server: Literal["fortiguard", "custom"] | None = ...,
        sms_custom_server: str | None = ...,
        expire_type: Literal["immediately", "first-successful-login"] | None = ...,
        expire: int | None = ...,
        max_accounts: int | None = ...,
        multiple_guest_add: Literal["disable", "enable"] | None = ...,
        guest: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: GroupPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        group_type: Literal["firewall", "fsso-service", "rsso", "guest"] | None = ...,
        authtimeout: int | None = ...,
        auth_concurrent_override: Literal["enable", "disable"] | None = ...,
        auth_concurrent_value: int | None = ...,
        http_digest_realm: str | None = ...,
        sso_attribute_value: str | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        match: str | list[str] | list[dict[str, Any]] | None = ...,
        user_id: Literal["email", "auto-generate", "specify"] | None = ...,
        password: Literal["auto-generate", "specify", "disable"] | None = ...,
        user_name: Literal["disable", "enable"] | None = ...,
        sponsor: Literal["optional", "mandatory", "disabled"] | None = ...,
        company: Literal["optional", "mandatory", "disabled"] | None = ...,
        email: Literal["disable", "enable"] | None = ...,
        mobile_phone: Literal["disable", "enable"] | None = ...,
        sms_server: Literal["fortiguard", "custom"] | None = ...,
        sms_custom_server: str | None = ...,
        expire_type: Literal["immediately", "first-successful-login"] | None = ...,
        expire: int | None = ...,
        max_accounts: int | None = ...,
        multiple_guest_add: Literal["disable", "enable"] | None = ...,
        guest: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: GroupPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        group_type: Literal["firewall", "fsso-service", "rsso", "guest"] | None = ...,
        authtimeout: int | None = ...,
        auth_concurrent_override: Literal["enable", "disable"] | None = ...,
        auth_concurrent_value: int | None = ...,
        http_digest_realm: str | None = ...,
        sso_attribute_value: str | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        match: str | list[str] | list[dict[str, Any]] | None = ...,
        user_id: Literal["email", "auto-generate", "specify"] | None = ...,
        password: Literal["auto-generate", "specify", "disable"] | None = ...,
        user_name: Literal["disable", "enable"] | None = ...,
        sponsor: Literal["optional", "mandatory", "disabled"] | None = ...,
        company: Literal["optional", "mandatory", "disabled"] | None = ...,
        email: Literal["disable", "enable"] | None = ...,
        mobile_phone: Literal["disable", "enable"] | None = ...,
        sms_server: Literal["fortiguard", "custom"] | None = ...,
        sms_custom_server: str | None = ...,
        expire_type: Literal["immediately", "first-successful-login"] | None = ...,
        expire: int | None = ...,
        max_accounts: int | None = ...,
        multiple_guest_add: Literal["disable", "enable"] | None = ...,
        guest: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: GroupPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        group_type: Literal["firewall", "fsso-service", "rsso", "guest"] | None = ...,
        authtimeout: int | None = ...,
        auth_concurrent_override: Literal["enable", "disable"] | None = ...,
        auth_concurrent_value: int | None = ...,
        http_digest_realm: str | None = ...,
        sso_attribute_value: str | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        match: str | list[str] | list[dict[str, Any]] | None = ...,
        user_id: Literal["email", "auto-generate", "specify"] | None = ...,
        password: Literal["auto-generate", "specify", "disable"] | None = ...,
        user_name: Literal["disable", "enable"] | None = ...,
        sponsor: Literal["optional", "mandatory", "disabled"] | None = ...,
        company: Literal["optional", "mandatory", "disabled"] | None = ...,
        email: Literal["disable", "enable"] | None = ...,
        mobile_phone: Literal["disable", "enable"] | None = ...,
        sms_server: Literal["fortiguard", "custom"] | None = ...,
        sms_custom_server: str | None = ...,
        expire_type: Literal["immediately", "first-successful-login"] | None = ...,
        expire: int | None = ...,
        max_accounts: int | None = ...,
        multiple_guest_add: Literal["disable", "enable"] | None = ...,
        guest: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> GroupObject: ...
    
    @overload
    def put(
        self,
        payload_dict: GroupPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        group_type: Literal["firewall", "fsso-service", "rsso", "guest"] | None = ...,
        authtimeout: int | None = ...,
        auth_concurrent_override: Literal["enable", "disable"] | None = ...,
        auth_concurrent_value: int | None = ...,
        http_digest_realm: str | None = ...,
        sso_attribute_value: str | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        match: str | list[str] | list[dict[str, Any]] | None = ...,
        user_id: Literal["email", "auto-generate", "specify"] | None = ...,
        password: Literal["auto-generate", "specify", "disable"] | None = ...,
        user_name: Literal["disable", "enable"] | None = ...,
        sponsor: Literal["optional", "mandatory", "disabled"] | None = ...,
        company: Literal["optional", "mandatory", "disabled"] | None = ...,
        email: Literal["disable", "enable"] | None = ...,
        mobile_phone: Literal["disable", "enable"] | None = ...,
        sms_server: Literal["fortiguard", "custom"] | None = ...,
        sms_custom_server: str | None = ...,
        expire_type: Literal["immediately", "first-successful-login"] | None = ...,
        expire: int | None = ...,
        max_accounts: int | None = ...,
        multiple_guest_add: Literal["disable", "enable"] | None = ...,
        guest: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: GroupPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        group_type: Literal["firewall", "fsso-service", "rsso", "guest"] | None = ...,
        authtimeout: int | None = ...,
        auth_concurrent_override: Literal["enable", "disable"] | None = ...,
        auth_concurrent_value: int | None = ...,
        http_digest_realm: str | None = ...,
        sso_attribute_value: str | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        match: str | list[str] | list[dict[str, Any]] | None = ...,
        user_id: Literal["email", "auto-generate", "specify"] | None = ...,
        password: Literal["auto-generate", "specify", "disable"] | None = ...,
        user_name: Literal["disable", "enable"] | None = ...,
        sponsor: Literal["optional", "mandatory", "disabled"] | None = ...,
        company: Literal["optional", "mandatory", "disabled"] | None = ...,
        email: Literal["disable", "enable"] | None = ...,
        mobile_phone: Literal["disable", "enable"] | None = ...,
        sms_server: Literal["fortiguard", "custom"] | None = ...,
        sms_custom_server: str | None = ...,
        expire_type: Literal["immediately", "first-successful-login"] | None = ...,
        expire: int | None = ...,
        max_accounts: int | None = ...,
        multiple_guest_add: Literal["disable", "enable"] | None = ...,
        guest: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: GroupPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        group_type: Literal["firewall", "fsso-service", "rsso", "guest"] | None = ...,
        authtimeout: int | None = ...,
        auth_concurrent_override: Literal["enable", "disable"] | None = ...,
        auth_concurrent_value: int | None = ...,
        http_digest_realm: str | None = ...,
        sso_attribute_value: str | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        match: str | list[str] | list[dict[str, Any]] | None = ...,
        user_id: Literal["email", "auto-generate", "specify"] | None = ...,
        password: Literal["auto-generate", "specify", "disable"] | None = ...,
        user_name: Literal["disable", "enable"] | None = ...,
        sponsor: Literal["optional", "mandatory", "disabled"] | None = ...,
        company: Literal["optional", "mandatory", "disabled"] | None = ...,
        email: Literal["disable", "enable"] | None = ...,
        mobile_phone: Literal["disable", "enable"] | None = ...,
        sms_server: Literal["fortiguard", "custom"] | None = ...,
        sms_custom_server: str | None = ...,
        expire_type: Literal["immediately", "first-successful-login"] | None = ...,
        expire: int | None = ...,
        max_accounts: int | None = ...,
        multiple_guest_add: Literal["disable", "enable"] | None = ...,
        guest: str | list[str] | list[dict[str, Any]] | None = ...,
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
    ) -> GroupObject: ...
    
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
        payload_dict: GroupPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        group_type: Literal["firewall", "fsso-service", "rsso", "guest"] | None = ...,
        authtimeout: int | None = ...,
        auth_concurrent_override: Literal["enable", "disable"] | None = ...,
        auth_concurrent_value: int | None = ...,
        http_digest_realm: str | None = ...,
        sso_attribute_value: str | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        match: str | list[str] | list[dict[str, Any]] | None = ...,
        user_id: Literal["email", "auto-generate", "specify"] | None = ...,
        password: Literal["auto-generate", "specify", "disable"] | None = ...,
        user_name: Literal["disable", "enable"] | None = ...,
        sponsor: Literal["optional", "mandatory", "disabled"] | None = ...,
        company: Literal["optional", "mandatory", "disabled"] | None = ...,
        email: Literal["disable", "enable"] | None = ...,
        mobile_phone: Literal["disable", "enable"] | None = ...,
        sms_server: Literal["fortiguard", "custom"] | None = ...,
        sms_custom_server: str | None = ...,
        expire_type: Literal["immediately", "first-successful-login"] | None = ...,
        expire: int | None = ...,
        max_accounts: int | None = ...,
        multiple_guest_add: Literal["disable", "enable"] | None = ...,
        guest: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "Group",
    "GroupPayload",
    "GroupObject",
]