""" - Type Stubs

Auto-generated stub file for type checking and IDE support.

Endpoint: system/replacemsg_group
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

class ReplacemsgGroupMailItem:
    """Nested item for mail field - supports attribute access."""
    msg_type: str
    buffer: str
    header: Literal["none", "http", "8bit"]
    format: Literal["none", "text", "html"]


class ReplacemsgGroupHttpItem:
    """Nested item for http field - supports attribute access."""
    msg_type: str
    buffer: str
    header: Literal["none", "http", "8bit"]
    format: Literal["none", "text", "html"]


class ReplacemsgGroupWebproxyItem:
    """Nested item for webproxy field - supports attribute access."""
    msg_type: str
    buffer: str
    header: Literal["none", "http", "8bit"]
    format: Literal["none", "text", "html"]


class ReplacemsgGroupFtpItem:
    """Nested item for ftp field - supports attribute access."""
    msg_type: str
    buffer: str
    header: Literal["none", "http", "8bit"]
    format: Literal["none", "text", "html"]


class ReplacemsgGroupFortiguardwfItem:
    """Nested item for fortiguard-wf field - supports attribute access."""
    msg_type: str
    buffer: str
    header: Literal["none", "http", "8bit"]
    format: Literal["none", "text", "html"]


class ReplacemsgGroupSpamItem:
    """Nested item for spam field - supports attribute access."""
    msg_type: str
    buffer: str
    header: Literal["none", "http", "8bit"]
    format: Literal["none", "text", "html"]


class ReplacemsgGroupAlertmailItem:
    """Nested item for alertmail field - supports attribute access."""
    msg_type: str
    buffer: str
    header: Literal["none", "http", "8bit"]
    format: Literal["none", "text", "html"]


class ReplacemsgGroupAdminItem:
    """Nested item for admin field - supports attribute access."""
    msg_type: str
    buffer: str
    header: Literal["none", "http", "8bit"]
    format: Literal["none", "text", "html"]


class ReplacemsgGroupAuthItem:
    """Nested item for auth field - supports attribute access."""
    msg_type: str
    buffer: str
    header: Literal["none", "http", "8bit"]
    format: Literal["none", "text", "html"]


class ReplacemsgGroupSslvpnItem:
    """Nested item for sslvpn field - supports attribute access."""
    msg_type: str
    buffer: str
    header: Literal["none", "http", "8bit"]
    format: Literal["none", "text", "html"]


class ReplacemsgGroupNacquarItem:
    """Nested item for nac-quar field - supports attribute access."""
    msg_type: str
    buffer: str
    header: Literal["none", "http", "8bit"]
    format: Literal["none", "text", "html"]


class ReplacemsgGroupTrafficquotaItem:
    """Nested item for traffic-quota field - supports attribute access."""
    msg_type: str
    buffer: str
    header: Literal["none", "http", "8bit"]
    format: Literal["none", "text", "html"]


class ReplacemsgGroupUtmItem:
    """Nested item for utm field - supports attribute access."""
    msg_type: str
    buffer: str
    header: Literal["none", "http", "8bit"]
    format: Literal["none", "text", "html"]


class ReplacemsgGroupCustommessageItem:
    """Nested item for custom-message field - supports attribute access."""
    msg_type: str
    buffer: str
    header: Literal["none", "http", "8bit"]
    format: Literal["none", "text", "html"]


class ReplacemsgGroupIcapItem:
    """Nested item for icap field - supports attribute access."""
    msg_type: str
    buffer: str
    header: Literal["none", "http", "8bit"]
    format: Literal["none", "text", "html"]


class ReplacemsgGroupAutomationItem:
    """Nested item for automation field - supports attribute access."""
    msg_type: str
    buffer: str
    header: Literal["none", "http", "8bit"]
    format: Literal["none", "text", "html"]


class ReplacemsgGroupPayload(TypedDict, total=False):
    """Payload type for ReplacemsgGroup operations."""
    name: str
    comment: str
    group_type: Literal["default", "utm", "auth"]
    mail: str | list[str] | list[dict[str, Any]] | list[ReplacemsgGroupMailItem]
    http: str | list[str] | list[dict[str, Any]] | list[ReplacemsgGroupHttpItem]
    webproxy: str | list[str] | list[dict[str, Any]] | list[ReplacemsgGroupWebproxyItem]
    ftp: str | list[str] | list[dict[str, Any]] | list[ReplacemsgGroupFtpItem]
    fortiguard_wf: str | list[str] | list[dict[str, Any]] | list[ReplacemsgGroupFortiguardwfItem]
    spam: str | list[str] | list[dict[str, Any]] | list[ReplacemsgGroupSpamItem]
    alertmail: str | list[str] | list[dict[str, Any]] | list[ReplacemsgGroupAlertmailItem]
    admin: str | list[str] | list[dict[str, Any]] | list[ReplacemsgGroupAdminItem]
    auth: str | list[str] | list[dict[str, Any]] | list[ReplacemsgGroupAuthItem]
    sslvpn: str | list[str] | list[dict[str, Any]] | list[ReplacemsgGroupSslvpnItem]
    nac_quar: str | list[str] | list[dict[str, Any]] | list[ReplacemsgGroupNacquarItem]
    traffic_quota: str | list[str] | list[dict[str, Any]] | list[ReplacemsgGroupTrafficquotaItem]
    utm: str | list[str] | list[dict[str, Any]] | list[ReplacemsgGroupUtmItem]
    custom_message: str | list[str] | list[dict[str, Any]] | list[ReplacemsgGroupCustommessageItem]
    icap: str | list[str] | list[dict[str, Any]] | list[ReplacemsgGroupIcapItem]
    automation: str | list[str] | list[dict[str, Any]] | list[ReplacemsgGroupAutomationItem]


# ================================================================
# Response Types (TypedDict for dict-style access)
# ================================================================

class ReplacemsgGroupResponse(TypedDict, total=False):
    """Response type for ReplacemsgGroup - use with .dict property for typed dict access."""
    name: str
    comment: str
    group_type: Literal["default", "utm", "auth"]
    mail: list[ReplacemsgGroupMailItem]
    http: list[ReplacemsgGroupHttpItem]
    webproxy: list[ReplacemsgGroupWebproxyItem]
    ftp: list[ReplacemsgGroupFtpItem]
    fortiguard_wf: list[ReplacemsgGroupFortiguardwfItem]
    spam: list[ReplacemsgGroupSpamItem]
    alertmail: list[ReplacemsgGroupAlertmailItem]
    admin: list[ReplacemsgGroupAdminItem]
    auth: list[ReplacemsgGroupAuthItem]
    sslvpn: list[ReplacemsgGroupSslvpnItem]
    nac_quar: list[ReplacemsgGroupNacquarItem]
    traffic_quota: list[ReplacemsgGroupTrafficquotaItem]
    utm: list[ReplacemsgGroupUtmItem]
    custom_message: list[ReplacemsgGroupCustommessageItem]
    icap: list[ReplacemsgGroupIcapItem]
    automation: list[ReplacemsgGroupAutomationItem]


# ================================================================
# Response Types (Class for attribute access)
# ================================================================


class ReplacemsgGroupObject(FortiObject):
    """Typed FortiObject for ReplacemsgGroup with field access."""
    name: str
    comment: str
    group_type: Literal["default", "utm", "auth"]
    mail: list[ReplacemsgGroupMailItem]
    http: list[ReplacemsgGroupHttpItem]
    webproxy: list[ReplacemsgGroupWebproxyItem]
    ftp: list[ReplacemsgGroupFtpItem]
    fortiguard_wf: list[ReplacemsgGroupFortiguardwfItem]
    spam: list[ReplacemsgGroupSpamItem]
    alertmail: list[ReplacemsgGroupAlertmailItem]
    admin: list[ReplacemsgGroupAdminItem]
    auth: list[ReplacemsgGroupAuthItem]
    sslvpn: list[ReplacemsgGroupSslvpnItem]
    nac_quar: list[ReplacemsgGroupNacquarItem]
    traffic_quota: list[ReplacemsgGroupTrafficquotaItem]
    utm: list[ReplacemsgGroupUtmItem]
    custom_message: list[ReplacemsgGroupCustommessageItem]
    icap: list[ReplacemsgGroupIcapItem]
    automation: list[ReplacemsgGroupAutomationItem]


# ================================================================
# Main Endpoint Class
# ================================================================

class ReplacemsgGroup:
    """
    
    Endpoint: system/replacemsg_group
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
    ) -> ReplacemsgGroupObject: ...
    
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
    ) -> FortiObjectList[ReplacemsgGroupObject]: ...
    
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
        payload_dict: ReplacemsgGroupPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        group_type: Literal["default", "utm", "auth"] | None = ...,
        mail: str | list[str] | list[dict[str, Any]] | list[ReplacemsgGroupMailItem] | None = ...,
        http: str | list[str] | list[dict[str, Any]] | list[ReplacemsgGroupHttpItem] | None = ...,
        webproxy: str | list[str] | list[dict[str, Any]] | list[ReplacemsgGroupWebproxyItem] | None = ...,
        ftp: str | list[str] | list[dict[str, Any]] | list[ReplacemsgGroupFtpItem] | None = ...,
        fortiguard_wf: str | list[str] | list[dict[str, Any]] | list[ReplacemsgGroupFortiguardwfItem] | None = ...,
        spam: str | list[str] | list[dict[str, Any]] | list[ReplacemsgGroupSpamItem] | None = ...,
        alertmail: str | list[str] | list[dict[str, Any]] | list[ReplacemsgGroupAlertmailItem] | None = ...,
        admin: str | list[str] | list[dict[str, Any]] | list[ReplacemsgGroupAdminItem] | None = ...,
        auth: str | list[str] | list[dict[str, Any]] | list[ReplacemsgGroupAuthItem] | None = ...,
        sslvpn: str | list[str] | list[dict[str, Any]] | list[ReplacemsgGroupSslvpnItem] | None = ...,
        nac_quar: str | list[str] | list[dict[str, Any]] | list[ReplacemsgGroupNacquarItem] | None = ...,
        traffic_quota: str | list[str] | list[dict[str, Any]] | list[ReplacemsgGroupTrafficquotaItem] | None = ...,
        utm: str | list[str] | list[dict[str, Any]] | list[ReplacemsgGroupUtmItem] | None = ...,
        custom_message: str | list[str] | list[dict[str, Any]] | list[ReplacemsgGroupCustommessageItem] | None = ...,
        icap: str | list[str] | list[dict[str, Any]] | list[ReplacemsgGroupIcapItem] | None = ...,
        automation: str | list[str] | list[dict[str, Any]] | list[ReplacemsgGroupAutomationItem] | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> ReplacemsgGroupObject: ...

    # ================================================================
    # PUT Method
    # ================================================================
    
    def put(
        self,
        payload_dict: ReplacemsgGroupPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        group_type: Literal["default", "utm", "auth"] | None = ...,
        mail: str | list[str] | list[dict[str, Any]] | list[ReplacemsgGroupMailItem] | None = ...,
        http: str | list[str] | list[dict[str, Any]] | list[ReplacemsgGroupHttpItem] | None = ...,
        webproxy: str | list[str] | list[dict[str, Any]] | list[ReplacemsgGroupWebproxyItem] | None = ...,
        ftp: str | list[str] | list[dict[str, Any]] | list[ReplacemsgGroupFtpItem] | None = ...,
        fortiguard_wf: str | list[str] | list[dict[str, Any]] | list[ReplacemsgGroupFortiguardwfItem] | None = ...,
        spam: str | list[str] | list[dict[str, Any]] | list[ReplacemsgGroupSpamItem] | None = ...,
        alertmail: str | list[str] | list[dict[str, Any]] | list[ReplacemsgGroupAlertmailItem] | None = ...,
        admin: str | list[str] | list[dict[str, Any]] | list[ReplacemsgGroupAdminItem] | None = ...,
        auth: str | list[str] | list[dict[str, Any]] | list[ReplacemsgGroupAuthItem] | None = ...,
        sslvpn: str | list[str] | list[dict[str, Any]] | list[ReplacemsgGroupSslvpnItem] | None = ...,
        nac_quar: str | list[str] | list[dict[str, Any]] | list[ReplacemsgGroupNacquarItem] | None = ...,
        traffic_quota: str | list[str] | list[dict[str, Any]] | list[ReplacemsgGroupTrafficquotaItem] | None = ...,
        utm: str | list[str] | list[dict[str, Any]] | list[ReplacemsgGroupUtmItem] | None = ...,
        custom_message: str | list[str] | list[dict[str, Any]] | list[ReplacemsgGroupCustommessageItem] | None = ...,
        icap: str | list[str] | list[dict[str, Any]] | list[ReplacemsgGroupIcapItem] | None = ...,
        automation: str | list[str] | list[dict[str, Any]] | list[ReplacemsgGroupAutomationItem] | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> ReplacemsgGroupObject: ...

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
        payload_dict: ReplacemsgGroupPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        group_type: Literal["default", "utm", "auth"] | None = ...,
        mail: str | list[str] | list[dict[str, Any]] | list[ReplacemsgGroupMailItem] | None = ...,
        http: str | list[str] | list[dict[str, Any]] | list[ReplacemsgGroupHttpItem] | None = ...,
        webproxy: str | list[str] | list[dict[str, Any]] | list[ReplacemsgGroupWebproxyItem] | None = ...,
        ftp: str | list[str] | list[dict[str, Any]] | list[ReplacemsgGroupFtpItem] | None = ...,
        fortiguard_wf: str | list[str] | list[dict[str, Any]] | list[ReplacemsgGroupFortiguardwfItem] | None = ...,
        spam: str | list[str] | list[dict[str, Any]] | list[ReplacemsgGroupSpamItem] | None = ...,
        alertmail: str | list[str] | list[dict[str, Any]] | list[ReplacemsgGroupAlertmailItem] | None = ...,
        admin: str | list[str] | list[dict[str, Any]] | list[ReplacemsgGroupAdminItem] | None = ...,
        auth: str | list[str] | list[dict[str, Any]] | list[ReplacemsgGroupAuthItem] | None = ...,
        sslvpn: str | list[str] | list[dict[str, Any]] | list[ReplacemsgGroupSslvpnItem] | None = ...,
        nac_quar: str | list[str] | list[dict[str, Any]] | list[ReplacemsgGroupNacquarItem] | None = ...,
        traffic_quota: str | list[str] | list[dict[str, Any]] | list[ReplacemsgGroupTrafficquotaItem] | None = ...,
        utm: str | list[str] | list[dict[str, Any]] | list[ReplacemsgGroupUtmItem] | None = ...,
        custom_message: str | list[str] | list[dict[str, Any]] | list[ReplacemsgGroupCustommessageItem] | None = ...,
        icap: str | list[str] | list[dict[str, Any]] | list[ReplacemsgGroupIcapItem] | None = ...,
        automation: str | list[str] | list[dict[str, Any]] | list[ReplacemsgGroupAutomationItem] | None = ...,
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
    "ReplacemsgGroup",
    "ReplacemsgGroupPayload",
    "ReplacemsgGroupResponse",
    "ReplacemsgGroupObject",
]