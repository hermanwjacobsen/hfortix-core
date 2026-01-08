from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class ProfileProtocolOptionsPayload(TypedDict, total=False):
    """
    Type hints for firewall/profile_protocol_options payload fields.
    
    Configure protocol options.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.replacemsg-group.ReplacemsgGroupEndpoint` (via: replacemsg-group)

    **Usage:**
        payload: ProfileProtocolOptionsPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Name.
    comment: NotRequired[str]  # Optional comments.
    replacemsg_group: NotRequired[str]  # Name of the replacement message group to be used.
    oversize_log: NotRequired[Literal["disable", "enable"]]  # Enable/disable logging for antivirus oversize file blocking.
    switching_protocols_log: NotRequired[Literal["disable", "enable"]]  # Enable/disable logging for HTTP/HTTPS switching protocols.
    http: NotRequired[str]  # Configure HTTP protocol options.
    ftp: NotRequired[str]  # Configure FTP protocol options.
    imap: NotRequired[str]  # Configure IMAP protocol options.
    mapi: NotRequired[str]  # Configure MAPI protocol options.
    pop3: NotRequired[str]  # Configure POP3 protocol options.
    smtp: NotRequired[str]  # Configure SMTP protocol options.
    nntp: NotRequired[str]  # Configure NNTP protocol options.
    ssh: NotRequired[str]  # Configure SFTP and SCP protocol options.
    dns: NotRequired[str]  # Configure DNS protocol options.
    cifs: NotRequired[str]  # Configure CIFS protocol options.
    mail_signature: NotRequired[str]  # Configure Mail signature.
    rpc_over_http: NotRequired[Literal["enable", "disable"]]  # Enable/disable inspection of RPC over HTTP.


class ProfileProtocolOptionsObject(FortiObject[ProfileProtocolOptionsPayload]):
    """Typed FortiObject for firewall/profile_protocol_options with IDE autocomplete support."""
    
    # Name.
    name: str
    # Optional comments.
    comment: str
    # Name of the replacement message group to be used.
    replacemsg_group: str
    # Enable/disable logging for antivirus oversize file blocking.
    oversize_log: Literal["disable", "enable"]
    # Enable/disable logging for HTTP/HTTPS switching protocols.
    switching_protocols_log: Literal["disable", "enable"]
    # Configure HTTP protocol options.
    http: str
    # Configure FTP protocol options.
    ftp: str
    # Configure IMAP protocol options.
    imap: str
    # Configure MAPI protocol options.
    mapi: str
    # Configure POP3 protocol options.
    pop3: str
    # Configure SMTP protocol options.
    smtp: str
    # Configure NNTP protocol options.
    nntp: str
    # Configure SFTP and SCP protocol options.
    ssh: str
    # Configure DNS protocol options.
    dns: str
    # Configure CIFS protocol options.
    cifs: str
    # Configure Mail signature.
    mail_signature: str
    # Enable/disable inspection of RPC over HTTP.
    rpc_over_http: Literal["enable", "disable"]
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> ProfileProtocolOptionsPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class ProfileProtocolOptions:
    """
    Configure protocol options.
    
    Path: firewall/profile_protocol_options
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
    ) -> ProfileProtocolOptionsObject: ...
    
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
    ) -> list[ProfileProtocolOptionsObject]: ...
    
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
    ) -> ProfileProtocolOptionsObject | list[ProfileProtocolOptionsObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: ProfileProtocolOptionsPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        replacemsg_group: str | None = ...,
        oversize_log: Literal["disable", "enable"] | None = ...,
        switching_protocols_log: Literal["disable", "enable"] | None = ...,
        http: str | None = ...,
        ftp: str | None = ...,
        imap: str | None = ...,
        mapi: str | None = ...,
        pop3: str | None = ...,
        smtp: str | None = ...,
        nntp: str | None = ...,
        ssh: str | None = ...,
        dns: str | None = ...,
        cifs: str | None = ...,
        mail_signature: str | None = ...,
        rpc_over_http: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ProfileProtocolOptionsObject: ...
    
    @overload
    def post(
        self,
        payload_dict: ProfileProtocolOptionsPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        replacemsg_group: str | None = ...,
        oversize_log: Literal["disable", "enable"] | None = ...,
        switching_protocols_log: Literal["disable", "enable"] | None = ...,
        http: str | None = ...,
        ftp: str | None = ...,
        imap: str | None = ...,
        mapi: str | None = ...,
        pop3: str | None = ...,
        smtp: str | None = ...,
        nntp: str | None = ...,
        ssh: str | None = ...,
        dns: str | None = ...,
        cifs: str | None = ...,
        mail_signature: str | None = ...,
        rpc_over_http: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: ProfileProtocolOptionsPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        replacemsg_group: str | None = ...,
        oversize_log: Literal["disable", "enable"] | None = ...,
        switching_protocols_log: Literal["disable", "enable"] | None = ...,
        http: str | None = ...,
        ftp: str | None = ...,
        imap: str | None = ...,
        mapi: str | None = ...,
        pop3: str | None = ...,
        smtp: str | None = ...,
        nntp: str | None = ...,
        ssh: str | None = ...,
        dns: str | None = ...,
        cifs: str | None = ...,
        mail_signature: str | None = ...,
        rpc_over_http: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: ProfileProtocolOptionsPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        replacemsg_group: str | None = ...,
        oversize_log: Literal["disable", "enable"] | None = ...,
        switching_protocols_log: Literal["disable", "enable"] | None = ...,
        http: str | None = ...,
        ftp: str | None = ...,
        imap: str | None = ...,
        mapi: str | None = ...,
        pop3: str | None = ...,
        smtp: str | None = ...,
        nntp: str | None = ...,
        ssh: str | None = ...,
        dns: str | None = ...,
        cifs: str | None = ...,
        mail_signature: str | None = ...,
        rpc_over_http: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: ProfileProtocolOptionsPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        replacemsg_group: str | None = ...,
        oversize_log: Literal["disable", "enable"] | None = ...,
        switching_protocols_log: Literal["disable", "enable"] | None = ...,
        http: str | None = ...,
        ftp: str | None = ...,
        imap: str | None = ...,
        mapi: str | None = ...,
        pop3: str | None = ...,
        smtp: str | None = ...,
        nntp: str | None = ...,
        ssh: str | None = ...,
        dns: str | None = ...,
        cifs: str | None = ...,
        mail_signature: str | None = ...,
        rpc_over_http: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ProfileProtocolOptionsObject: ...
    
    @overload
    def put(
        self,
        payload_dict: ProfileProtocolOptionsPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        replacemsg_group: str | None = ...,
        oversize_log: Literal["disable", "enable"] | None = ...,
        switching_protocols_log: Literal["disable", "enable"] | None = ...,
        http: str | None = ...,
        ftp: str | None = ...,
        imap: str | None = ...,
        mapi: str | None = ...,
        pop3: str | None = ...,
        smtp: str | None = ...,
        nntp: str | None = ...,
        ssh: str | None = ...,
        dns: str | None = ...,
        cifs: str | None = ...,
        mail_signature: str | None = ...,
        rpc_over_http: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: ProfileProtocolOptionsPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        replacemsg_group: str | None = ...,
        oversize_log: Literal["disable", "enable"] | None = ...,
        switching_protocols_log: Literal["disable", "enable"] | None = ...,
        http: str | None = ...,
        ftp: str | None = ...,
        imap: str | None = ...,
        mapi: str | None = ...,
        pop3: str | None = ...,
        smtp: str | None = ...,
        nntp: str | None = ...,
        ssh: str | None = ...,
        dns: str | None = ...,
        cifs: str | None = ...,
        mail_signature: str | None = ...,
        rpc_over_http: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: ProfileProtocolOptionsPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        replacemsg_group: str | None = ...,
        oversize_log: Literal["disable", "enable"] | None = ...,
        switching_protocols_log: Literal["disable", "enable"] | None = ...,
        http: str | None = ...,
        ftp: str | None = ...,
        imap: str | None = ...,
        mapi: str | None = ...,
        pop3: str | None = ...,
        smtp: str | None = ...,
        nntp: str | None = ...,
        ssh: str | None = ...,
        dns: str | None = ...,
        cifs: str | None = ...,
        mail_signature: str | None = ...,
        rpc_over_http: Literal["enable", "disable"] | None = ...,
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
    ) -> ProfileProtocolOptionsObject: ...
    
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
        payload_dict: ProfileProtocolOptionsPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        replacemsg_group: str | None = ...,
        oversize_log: Literal["disable", "enable"] | None = ...,
        switching_protocols_log: Literal["disable", "enable"] | None = ...,
        http: str | None = ...,
        ftp: str | None = ...,
        imap: str | None = ...,
        mapi: str | None = ...,
        pop3: str | None = ...,
        smtp: str | None = ...,
        nntp: str | None = ...,
        ssh: str | None = ...,
        dns: str | None = ...,
        cifs: str | None = ...,
        mail_signature: str | None = ...,
        rpc_over_http: Literal["enable", "disable"] | None = ...,
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
    "ProfileProtocolOptions",
    "ProfileProtocolOptionsPayload",
    "ProfileProtocolOptionsObject",
]