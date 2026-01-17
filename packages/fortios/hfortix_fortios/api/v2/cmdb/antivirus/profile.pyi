""" - Type Stubs

Auto-generated stub file for type checking and IDE support.

Endpoint: antivirus/profile
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

class ProfileExternalblocklistItem:
    """Nested item for external-blocklist field - supports attribute access."""
    name: str


class ProfilePayload(TypedDict, total=False):
    """Payload type for Profile operations."""
    name: str
    comment: str
    replacemsg_group: str
    feature_set: Literal["flow", "proxy"]
    fortisandbox_mode: Literal["inline", "analytics-suspicious", "analytics-everything"]
    fortisandbox_max_upload: int
    analytics_ignore_filetype: int
    analytics_accept_filetype: int
    analytics_db: Literal["disable", "enable"]
    mobile_malware_db: Literal["disable", "enable"]
    http: str
    ftp: str
    imap: str
    pop3: str
    smtp: str
    mapi: str
    nntp: str
    cifs: str
    ssh: str
    nac_quar: str
    content_disarm: str
    outbreak_prevention_archive_scan: Literal["disable", "enable"]
    external_blocklist_enable_all: Literal["disable", "enable"]
    external_blocklist: str | list[str] | list[dict[str, Any]] | list[ProfileExternalblocklistItem]
    ems_threat_feed: Literal["disable", "enable"]
    fortindr_error_action: Literal["log-only", "block", "ignore"]
    fortindr_timeout_action: Literal["log-only", "block", "ignore"]
    fortisandbox_scan_timeout: int
    fortisandbox_error_action: Literal["log-only", "block", "ignore"]
    fortisandbox_timeout_action: Literal["log-only", "block", "ignore"]
    av_virus_log: Literal["enable", "disable"]
    extended_log: Literal["enable", "disable"]
    scan_mode: Literal["default", "legacy"]


# ================================================================
# Response Types (TypedDict for dict-style access)
# ================================================================

class ProfileResponse(TypedDict, total=False):
    """Response type for Profile - use with .dict property for typed dict access."""
    name: str
    comment: str
    replacemsg_group: str
    feature_set: Literal["flow", "proxy"]
    fortisandbox_mode: Literal["inline", "analytics-suspicious", "analytics-everything"]
    fortisandbox_max_upload: int
    analytics_ignore_filetype: int
    analytics_accept_filetype: int
    analytics_db: Literal["disable", "enable"]
    mobile_malware_db: Literal["disable", "enable"]
    http: str
    ftp: str
    imap: str
    pop3: str
    smtp: str
    mapi: str
    nntp: str
    cifs: str
    ssh: str
    nac_quar: str
    content_disarm: str
    outbreak_prevention_archive_scan: Literal["disable", "enable"]
    external_blocklist_enable_all: Literal["disable", "enable"]
    external_blocklist: list[ProfileExternalblocklistItem]
    ems_threat_feed: Literal["disable", "enable"]
    fortindr_error_action: Literal["log-only", "block", "ignore"]
    fortindr_timeout_action: Literal["log-only", "block", "ignore"]
    fortisandbox_scan_timeout: int
    fortisandbox_error_action: Literal["log-only", "block", "ignore"]
    fortisandbox_timeout_action: Literal["log-only", "block", "ignore"]
    av_virus_log: Literal["enable", "disable"]
    extended_log: Literal["enable", "disable"]
    scan_mode: Literal["default", "legacy"]


# ================================================================
# Response Types (Class for attribute access)
# ================================================================


class ProfileObject(FortiObject):
    """Typed FortiObject for Profile with field access."""
    name: str
    comment: str
    replacemsg_group: str
    feature_set: Literal["flow", "proxy"]
    fortisandbox_mode: Literal["inline", "analytics-suspicious", "analytics-everything"]
    fortisandbox_max_upload: int
    analytics_ignore_filetype: int
    analytics_accept_filetype: int
    analytics_db: Literal["disable", "enable"]
    mobile_malware_db: Literal["disable", "enable"]
    http: str
    ftp: str
    imap: str
    pop3: str
    smtp: str
    mapi: str
    nntp: str
    cifs: str
    ssh: str
    nac_quar: str
    content_disarm: str
    outbreak_prevention_archive_scan: Literal["disable", "enable"]
    external_blocklist_enable_all: Literal["disable", "enable"]
    external_blocklist: list[ProfileExternalblocklistItem]
    ems_threat_feed: Literal["disable", "enable"]
    fortindr_error_action: Literal["log-only", "block", "ignore"]
    fortindr_timeout_action: Literal["log-only", "block", "ignore"]
    fortisandbox_scan_timeout: int
    fortisandbox_error_action: Literal["log-only", "block", "ignore"]
    fortisandbox_timeout_action: Literal["log-only", "block", "ignore"]
    av_virus_log: Literal["enable", "disable"]
    extended_log: Literal["enable", "disable"]
    scan_mode: Literal["default", "legacy"]


# ================================================================
# Main Endpoint Class
# ================================================================

class Profile:
    """
    
    Endpoint: antivirus/profile
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
    ) -> ProfileObject: ...
    
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
    ) -> FortiObjectList[ProfileObject]: ...
    
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
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        replacemsg_group: str | None = ...,
        feature_set: Literal["flow", "proxy"] | None = ...,
        fortisandbox_mode: Literal["inline", "analytics-suspicious", "analytics-everything"] | None = ...,
        fortisandbox_max_upload: int | None = ...,
        analytics_ignore_filetype: int | None = ...,
        analytics_accept_filetype: int | None = ...,
        analytics_db: Literal["disable", "enable"] | None = ...,
        mobile_malware_db: Literal["disable", "enable"] | None = ...,
        http: str | None = ...,
        ftp: str | None = ...,
        imap: str | None = ...,
        pop3: str | None = ...,
        smtp: str | None = ...,
        mapi: str | None = ...,
        nntp: str | None = ...,
        cifs: str | None = ...,
        ssh: str | None = ...,
        nac_quar: str | None = ...,
        content_disarm: str | None = ...,
        outbreak_prevention_archive_scan: Literal["disable", "enable"] | None = ...,
        external_blocklist_enable_all: Literal["disable", "enable"] | None = ...,
        external_blocklist: str | list[str] | list[dict[str, Any]] | list[ProfileExternalblocklistItem] | None = ...,
        ems_threat_feed: Literal["disable", "enable"] | None = ...,
        fortindr_error_action: Literal["log-only", "block", "ignore"] | None = ...,
        fortindr_timeout_action: Literal["log-only", "block", "ignore"] | None = ...,
        fortisandbox_scan_timeout: int | None = ...,
        fortisandbox_error_action: Literal["log-only", "block", "ignore"] | None = ...,
        fortisandbox_timeout_action: Literal["log-only", "block", "ignore"] | None = ...,
        av_virus_log: Literal["enable", "disable"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        scan_mode: Literal["default", "legacy"] | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> ProfileObject: ...

    # ================================================================
    # PUT Method
    # ================================================================
    
    def put(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        replacemsg_group: str | None = ...,
        feature_set: Literal["flow", "proxy"] | None = ...,
        fortisandbox_mode: Literal["inline", "analytics-suspicious", "analytics-everything"] | None = ...,
        fortisandbox_max_upload: int | None = ...,
        analytics_ignore_filetype: int | None = ...,
        analytics_accept_filetype: int | None = ...,
        analytics_db: Literal["disable", "enable"] | None = ...,
        mobile_malware_db: Literal["disable", "enable"] | None = ...,
        http: str | None = ...,
        ftp: str | None = ...,
        imap: str | None = ...,
        pop3: str | None = ...,
        smtp: str | None = ...,
        mapi: str | None = ...,
        nntp: str | None = ...,
        cifs: str | None = ...,
        ssh: str | None = ...,
        nac_quar: str | None = ...,
        content_disarm: str | None = ...,
        outbreak_prevention_archive_scan: Literal["disable", "enable"] | None = ...,
        external_blocklist_enable_all: Literal["disable", "enable"] | None = ...,
        external_blocklist: str | list[str] | list[dict[str, Any]] | list[ProfileExternalblocklistItem] | None = ...,
        ems_threat_feed: Literal["disable", "enable"] | None = ...,
        fortindr_error_action: Literal["log-only", "block", "ignore"] | None = ...,
        fortindr_timeout_action: Literal["log-only", "block", "ignore"] | None = ...,
        fortisandbox_scan_timeout: int | None = ...,
        fortisandbox_error_action: Literal["log-only", "block", "ignore"] | None = ...,
        fortisandbox_timeout_action: Literal["log-only", "block", "ignore"] | None = ...,
        av_virus_log: Literal["enable", "disable"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        scan_mode: Literal["default", "legacy"] | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> ProfileObject: ...

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
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        replacemsg_group: str | None = ...,
        feature_set: Literal["flow", "proxy"] | None = ...,
        fortisandbox_mode: Literal["inline", "analytics-suspicious", "analytics-everything"] | None = ...,
        fortisandbox_max_upload: int | None = ...,
        analytics_ignore_filetype: int | None = ...,
        analytics_accept_filetype: int | None = ...,
        analytics_db: Literal["disable", "enable"] | None = ...,
        mobile_malware_db: Literal["disable", "enable"] | None = ...,
        http: str | None = ...,
        ftp: str | None = ...,
        imap: str | None = ...,
        pop3: str | None = ...,
        smtp: str | None = ...,
        mapi: str | None = ...,
        nntp: str | None = ...,
        cifs: str | None = ...,
        ssh: str | None = ...,
        nac_quar: str | None = ...,
        content_disarm: str | None = ...,
        outbreak_prevention_archive_scan: Literal["disable", "enable"] | None = ...,
        external_blocklist_enable_all: Literal["disable", "enable"] | None = ...,
        external_blocklist: str | list[str] | list[dict[str, Any]] | list[ProfileExternalblocklistItem] | None = ...,
        ems_threat_feed: Literal["disable", "enable"] | None = ...,
        fortindr_error_action: Literal["log-only", "block", "ignore"] | None = ...,
        fortindr_timeout_action: Literal["log-only", "block", "ignore"] | None = ...,
        fortisandbox_scan_timeout: int | None = ...,
        fortisandbox_error_action: Literal["log-only", "block", "ignore"] | None = ...,
        fortisandbox_timeout_action: Literal["log-only", "block", "ignore"] | None = ...,
        av_virus_log: Literal["enable", "disable"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        scan_mode: Literal["default", "legacy"] | None = ...,
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
    "Profile",
    "ProfilePayload",
    "ProfileResponse",
    "ProfileObject",
]