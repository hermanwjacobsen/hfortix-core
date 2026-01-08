from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class FssoPollingPayload(TypedDict, total=False):
    """
    Type hints for user/fsso_polling payload fields.
    
    Configure FSSO active directory servers for polling mode.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.user.ldap.LdapEndpoint` (via: ldap-server)

    **Usage:**
        payload: FssoPollingPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    id: NotRequired[int]  # Active Directory server ID.
    status: NotRequired[Literal["enable", "disable"]]  # Enable/disable polling for the status of this Active Directo
    server: str  # Host name or IP address of the Active Directory server.
    default_domain: NotRequired[str]  # Default domain managed by this Active Directory server.
    port: NotRequired[int]  # Port to communicate with this Active Directory server.
    user: str  # User name required to log into this Active Directory server.
    password: NotRequired[str]  # Password required to log into this Active Directory server.
    ldap_server: str  # LDAP server name used in LDAP connection strings.
    logon_history: NotRequired[int]  # Number of hours of logon history to keep, 0 means keep all h
    polling_frequency: NotRequired[int]  # Polling frequency (every 1 to 30 seconds).
    adgrp: NotRequired[list[dict[str, Any]]]  # LDAP Group Info.
    smbv1: NotRequired[Literal["enable", "disable"]]  # Enable/disable support of SMBv1 for Samba.
    smb_ntlmv1_auth: NotRequired[Literal["enable", "disable"]]  # Enable/disable support of NTLMv1 for Samba authentication.


class FssoPollingObject(FortiObject[FssoPollingPayload]):
    """Typed FortiObject for user/fsso_polling with IDE autocomplete support."""
    
    # Active Directory server ID.
    id: int
    # Enable/disable polling for the status of this Active Directory server.
    status: Literal["enable", "disable"]
    # Host name or IP address of the Active Directory server.
    server: str
    # Default domain managed by this Active Directory server.
    default_domain: str
    # Port to communicate with this Active Directory server.
    port: int
    # User name required to log into this Active Directory server.
    user: str
    # Password required to log into this Active Directory server.
    password: str
    # LDAP server name used in LDAP connection strings.
    ldap_server: str
    # Number of hours of logon history to keep, 0 means keep all history.
    logon_history: int
    # Polling frequency (every 1 to 30 seconds).
    polling_frequency: int
    # LDAP Group Info.
    adgrp: list[str]  # Auto-flattened from member_table
    # Enable/disable support of SMBv1 for Samba.
    smbv1: Literal["enable", "disable"]
    # Enable/disable support of NTLMv1 for Samba authentication.
    smb_ntlmv1_auth: Literal["enable", "disable"]
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FssoPollingPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class FssoPolling:
    """
    Configure FSSO active directory servers for polling mode.
    
    Path: user/fsso_polling
    Category: cmdb
    Primary Key: id
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey provided)
    @overload
    def get(
        self,
        id: int,
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
    ) -> FssoPollingObject: ...
    
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
    ) -> list[FssoPollingObject]: ...
    
    @overload
    def get(
        self,
        id: int | None = ...,
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
        id: int,
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
        id: None = None,
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
        id: int | None = ...,
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
        id: int | None = ...,
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
    ) -> FssoPollingObject | list[FssoPollingObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: FssoPollingPayload | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        server: str | None = ...,
        default_domain: str | None = ...,
        port: int | None = ...,
        user: str | None = ...,
        password: str | None = ...,
        ldap_server: str | None = ...,
        logon_history: int | None = ...,
        polling_frequency: int | None = ...,
        adgrp: str | list[str] | list[dict[str, Any]] | None = ...,
        smbv1: Literal["enable", "disable"] | None = ...,
        smb_ntlmv1_auth: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> FssoPollingObject: ...
    
    @overload
    def post(
        self,
        payload_dict: FssoPollingPayload | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        server: str | None = ...,
        default_domain: str | None = ...,
        port: int | None = ...,
        user: str | None = ...,
        password: str | None = ...,
        ldap_server: str | None = ...,
        logon_history: int | None = ...,
        polling_frequency: int | None = ...,
        adgrp: str | list[str] | list[dict[str, Any]] | None = ...,
        smbv1: Literal["enable", "disable"] | None = ...,
        smb_ntlmv1_auth: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: FssoPollingPayload | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        server: str | None = ...,
        default_domain: str | None = ...,
        port: int | None = ...,
        user: str | None = ...,
        password: str | None = ...,
        ldap_server: str | None = ...,
        logon_history: int | None = ...,
        polling_frequency: int | None = ...,
        adgrp: str | list[str] | list[dict[str, Any]] | None = ...,
        smbv1: Literal["enable", "disable"] | None = ...,
        smb_ntlmv1_auth: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: FssoPollingPayload | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        server: str | None = ...,
        default_domain: str | None = ...,
        port: int | None = ...,
        user: str | None = ...,
        password: str | None = ...,
        ldap_server: str | None = ...,
        logon_history: int | None = ...,
        polling_frequency: int | None = ...,
        adgrp: str | list[str] | list[dict[str, Any]] | None = ...,
        smbv1: Literal["enable", "disable"] | None = ...,
        smb_ntlmv1_auth: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: FssoPollingPayload | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        server: str | None = ...,
        default_domain: str | None = ...,
        port: int | None = ...,
        user: str | None = ...,
        password: str | None = ...,
        ldap_server: str | None = ...,
        logon_history: int | None = ...,
        polling_frequency: int | None = ...,
        adgrp: str | list[str] | list[dict[str, Any]] | None = ...,
        smbv1: Literal["enable", "disable"] | None = ...,
        smb_ntlmv1_auth: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> FssoPollingObject: ...
    
    @overload
    def put(
        self,
        payload_dict: FssoPollingPayload | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        server: str | None = ...,
        default_domain: str | None = ...,
        port: int | None = ...,
        user: str | None = ...,
        password: str | None = ...,
        ldap_server: str | None = ...,
        logon_history: int | None = ...,
        polling_frequency: int | None = ...,
        adgrp: str | list[str] | list[dict[str, Any]] | None = ...,
        smbv1: Literal["enable", "disable"] | None = ...,
        smb_ntlmv1_auth: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: FssoPollingPayload | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        server: str | None = ...,
        default_domain: str | None = ...,
        port: int | None = ...,
        user: str | None = ...,
        password: str | None = ...,
        ldap_server: str | None = ...,
        logon_history: int | None = ...,
        polling_frequency: int | None = ...,
        adgrp: str | list[str] | list[dict[str, Any]] | None = ...,
        smbv1: Literal["enable", "disable"] | None = ...,
        smb_ntlmv1_auth: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: FssoPollingPayload | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        server: str | None = ...,
        default_domain: str | None = ...,
        port: int | None = ...,
        user: str | None = ...,
        password: str | None = ...,
        ldap_server: str | None = ...,
        logon_history: int | None = ...,
        polling_frequency: int | None = ...,
        adgrp: str | list[str] | list[dict[str, Any]] | None = ...,
        smbv1: Literal["enable", "disable"] | None = ...,
        smb_ntlmv1_auth: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> FssoPollingObject: ...
    
    @overload
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def exists(
        self,
        id: int,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: FssoPollingPayload | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        server: str | None = ...,
        default_domain: str | None = ...,
        port: int | None = ...,
        user: str | None = ...,
        password: str | None = ...,
        ldap_server: str | None = ...,
        logon_history: int | None = ...,
        polling_frequency: int | None = ...,
        adgrp: str | list[str] | list[dict[str, Any]] | None = ...,
        smbv1: Literal["enable", "disable"] | None = ...,
        smb_ntlmv1_auth: Literal["enable", "disable"] | None = ...,
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
    "FssoPolling",
    "FssoPollingPayload",
    "FssoPollingObject",
]