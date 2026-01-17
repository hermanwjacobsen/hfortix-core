""" - Type Stubs

Auto-generated stub file for type checking and IDE support.

Endpoint: firewall/profile_protocol_options
Category: cmdb
"""

from __future__ import annotations

from typing import (
    Any,
    ClassVar,
    Literal,
    TypedDict,
    overload,
)

from hfortix_fortios.models import (
    FortiObject,
    FortiObjectList,
)


# ================================================================
# TypedDict Payloads
# ================================================================

class ProfileProtocolOptionsPayload(TypedDict, total=False):
    """Payload type for ProfileProtocolOptions operations."""
    name: str
    comment: str
    replacemsg_group: str
    oversize_log: Literal["disable", "enable"]
    switching_protocols_log: Literal["disable", "enable"]
    http: str
    ftp: str
    imap: str
    mapi: str
    pop3: str
    smtp: str
    nntp: str
    ssh: str
    dns: str
    cifs: str
    mail_signature: str
    rpc_over_http: Literal["enable", "disable"]


# ================================================================
# Response Types (TypedDict for dict-style access)
# ================================================================

class ProfileProtocolOptionsResponse(TypedDict, total=False):
    """Response type for ProfileProtocolOptions - use with .dict property for typed dict access."""
    name: str
    comment: str
    replacemsg_group: str
    oversize_log: Literal["disable", "enable"]
    switching_protocols_log: Literal["disable", "enable"]
    http: str
    ftp: str
    imap: str
    mapi: str
    pop3: str
    smtp: str
    nntp: str
    ssh: str
    dns: str
    cifs: str
    mail_signature: str
    rpc_over_http: Literal["enable", "disable"]


# ================================================================
# Response Types (Class for attribute access)
# ================================================================


class ProfileProtocolOptionsObject(FortiObject):
    """Typed FortiObject for ProfileProtocolOptions with field access."""
    name: str
    comment: str
    replacemsg_group: str
    oversize_log: Literal["disable", "enable"]
    switching_protocols_log: Literal["disable", "enable"]
    http: str
    ftp: str
    imap: str
    mapi: str
    pop3: str
    smtp: str
    nntp: str
    ssh: str
    dns: str
    cifs: str
    mail_signature: str
    rpc_over_http: Literal["enable", "disable"]


# ================================================================
# Main Endpoint Class
# ================================================================

class ProfileProtocolOptions:
    """
    
    Endpoint: firewall/profile_protocol_options
    Category: cmdb
    MKey: name
    """
    
    # Class attributes for introspection
    endpoint: ClassVar[str] = ...
    path: ClassVar[str] = ...
    category: ClassVar[str] = ...
    mkey: ClassVar[str] = ...
    capabilities: ClassVar[dict[str, Any]] = ...
    
    def __init__(self, client: Any) -> None:
        """Initialize endpoint with HTTP client."""
        ...
    
    # ================================================================
    # GET Methods
    # ================================================================
    
    # CMDB with mkey - overloads for single vs list returns
    @overload
    def get(
        self,
        name: str,
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
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> ProfileProtocolOptionsObject: ...
    
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
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> FortiObjectList[ProfileProtocolOptionsObject]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...

    # ================================================================
    # POST Method
    # ================================================================
    
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
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> ProfileProtocolOptionsObject: ...

    # ================================================================
    # PUT Method
    # ================================================================
    
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
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> ProfileProtocolOptionsObject: ...

    # ================================================================
    # DELETE Method
    # ================================================================
    
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> FortiObject: ...

    # ================================================================
    # Utility Methods
    # ================================================================
    
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
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> FortiObject: ...
    
    # Helper methods
    @staticmethod
    def help(field_name: str | None = ...) -> str: ...
    
    @staticmethod
    def fields(detailed: bool = ...) -> list[str] | list[dict[str, Any]]: ...
    
    @staticmethod
    def field_info(field_name: str) -> FortiObject: ...
    
    @staticmethod
    def validate_field(name: str, value: Any) -> bool: ...
    
    @staticmethod
    def required_fields() -> list[str]: ...
    
    @staticmethod
    def defaults() -> FortiObject: ...
    
    @staticmethod
    def schema() -> FortiObject: ...


__all__ = [
    "ProfileProtocolOptions",
    "ProfileProtocolOptionsPayload",
    "ProfileProtocolOptionsResponse",
    "ProfileProtocolOptionsObject",
]