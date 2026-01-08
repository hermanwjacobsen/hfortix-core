from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class ProfilePayload(TypedDict, total=False):
    """
    Type hints for dlp/profile payload fields.
    
    Configure DLP profiles.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.replacemsg-group.ReplacemsgGroupEndpoint` (via: replacemsg-group)

    **Usage:**
        payload: ProfilePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Name of the DLP profile.
    comment: NotRequired[str]  # Comment.
    feature_set: NotRequired[Literal["flow", "proxy"]]  # Flow/proxy feature set.
    replacemsg_group: NotRequired[str]  # Replacement message group used by this DLP profile.
    rule: NotRequired[list[dict[str, Any]]]  # Set up DLP rules for this profile.
    dlp_log: NotRequired[Literal["enable", "disable"]]  # Enable/disable DLP logging.
    extended_log: NotRequired[Literal["enable", "disable"]]  # Enable/disable extended logging for data loss prevention.
    nac_quar_log: NotRequired[Literal["enable", "disable"]]  # Enable/disable NAC quarantine logging.
    full_archive_proto: NotRequired[Literal["smtp", "pop3", "imap", "http-get", "http-post", "ftp", "nntp", "mapi", "ssh", "cifs"]]  # Protocols to always content archive.
    summary_proto: NotRequired[Literal["smtp", "pop3", "imap", "http-get", "http-post", "ftp", "nntp", "mapi", "ssh", "cifs"]]  # Protocols to always log summary.
    fortidata_error_action: NotRequired[Literal["log-only", "block", "ignore"]]  # Action to take if FortiData query fails.


class ProfileObject(FortiObject[ProfilePayload]):
    """Typed FortiObject for dlp/profile with IDE autocomplete support."""
    
    # Name of the DLP profile.
    name: str
    # Comment.
    comment: str
    # Flow/proxy feature set.
    feature_set: Literal["flow", "proxy"]
    # Replacement message group used by this DLP profile.
    replacemsg_group: str
    # Set up DLP rules for this profile.
    rule: list[str]  # Auto-flattened from member_table
    # Enable/disable DLP logging.
    dlp_log: Literal["enable", "disable"]
    # Enable/disable extended logging for data loss prevention.
    extended_log: Literal["enable", "disable"]
    # Enable/disable NAC quarantine logging.
    nac_quar_log: Literal["enable", "disable"]
    # Protocols to always content archive.
    full_archive_proto: Literal["smtp", "pop3", "imap", "http-get", "http-post", "ftp", "nntp", "mapi", "ssh", "cifs"]
    # Protocols to always log summary.
    summary_proto: Literal["smtp", "pop3", "imap", "http-get", "http-post", "ftp", "nntp", "mapi", "ssh", "cifs"]
    # Action to take if FortiData query fails.
    fortidata_error_action: Literal["log-only", "block", "ignore"]
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> ProfilePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Profile:
    """
    Configure DLP profiles.
    
    Path: dlp/profile
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
    ) -> ProfileObject: ...
    
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
    ) -> list[ProfileObject]: ...
    
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
    ) -> ProfileObject | list[ProfileObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        feature_set: Literal["flow", "proxy"] | None = ...,
        replacemsg_group: str | None = ...,
        rule: str | list[str] | list[dict[str, Any]] | None = ...,
        dlp_log: Literal["enable", "disable"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        nac_quar_log: Literal["enable", "disable"] | None = ...,
        full_archive_proto: Literal["smtp", "pop3", "imap", "http-get", "http-post", "ftp", "nntp", "mapi", "ssh", "cifs"] | list[str] | list[dict[str, Any]] | None = ...,
        summary_proto: Literal["smtp", "pop3", "imap", "http-get", "http-post", "ftp", "nntp", "mapi", "ssh", "cifs"] | list[str] | list[dict[str, Any]] | None = ...,
        fortidata_error_action: Literal["log-only", "block", "ignore"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ProfileObject: ...
    
    @overload
    def post(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        feature_set: Literal["flow", "proxy"] | None = ...,
        replacemsg_group: str | None = ...,
        rule: str | list[str] | list[dict[str, Any]] | None = ...,
        dlp_log: Literal["enable", "disable"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        nac_quar_log: Literal["enable", "disable"] | None = ...,
        full_archive_proto: Literal["smtp", "pop3", "imap", "http-get", "http-post", "ftp", "nntp", "mapi", "ssh", "cifs"] | list[str] | list[dict[str, Any]] | None = ...,
        summary_proto: Literal["smtp", "pop3", "imap", "http-get", "http-post", "ftp", "nntp", "mapi", "ssh", "cifs"] | list[str] | list[dict[str, Any]] | None = ...,
        fortidata_error_action: Literal["log-only", "block", "ignore"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        feature_set: Literal["flow", "proxy"] | None = ...,
        replacemsg_group: str | None = ...,
        rule: str | list[str] | list[dict[str, Any]] | None = ...,
        dlp_log: Literal["enable", "disable"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        nac_quar_log: Literal["enable", "disable"] | None = ...,
        full_archive_proto: Literal["smtp", "pop3", "imap", "http-get", "http-post", "ftp", "nntp", "mapi", "ssh", "cifs"] | list[str] | list[dict[str, Any]] | None = ...,
        summary_proto: Literal["smtp", "pop3", "imap", "http-get", "http-post", "ftp", "nntp", "mapi", "ssh", "cifs"] | list[str] | list[dict[str, Any]] | None = ...,
        fortidata_error_action: Literal["log-only", "block", "ignore"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        feature_set: Literal["flow", "proxy"] | None = ...,
        replacemsg_group: str | None = ...,
        rule: str | list[str] | list[dict[str, Any]] | None = ...,
        dlp_log: Literal["enable", "disable"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        nac_quar_log: Literal["enable", "disable"] | None = ...,
        full_archive_proto: Literal["smtp", "pop3", "imap", "http-get", "http-post", "ftp", "nntp", "mapi", "ssh", "cifs"] | list[str] | list[dict[str, Any]] | None = ...,
        summary_proto: Literal["smtp", "pop3", "imap", "http-get", "http-post", "ftp", "nntp", "mapi", "ssh", "cifs"] | list[str] | list[dict[str, Any]] | None = ...,
        fortidata_error_action: Literal["log-only", "block", "ignore"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        feature_set: Literal["flow", "proxy"] | None = ...,
        replacemsg_group: str | None = ...,
        rule: str | list[str] | list[dict[str, Any]] | None = ...,
        dlp_log: Literal["enable", "disable"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        nac_quar_log: Literal["enable", "disable"] | None = ...,
        full_archive_proto: Literal["smtp", "pop3", "imap", "http-get", "http-post", "ftp", "nntp", "mapi", "ssh", "cifs"] | list[str] | list[dict[str, Any]] | None = ...,
        summary_proto: Literal["smtp", "pop3", "imap", "http-get", "http-post", "ftp", "nntp", "mapi", "ssh", "cifs"] | list[str] | list[dict[str, Any]] | None = ...,
        fortidata_error_action: Literal["log-only", "block", "ignore"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ProfileObject: ...
    
    @overload
    def put(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        feature_set: Literal["flow", "proxy"] | None = ...,
        replacemsg_group: str | None = ...,
        rule: str | list[str] | list[dict[str, Any]] | None = ...,
        dlp_log: Literal["enable", "disable"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        nac_quar_log: Literal["enable", "disable"] | None = ...,
        full_archive_proto: Literal["smtp", "pop3", "imap", "http-get", "http-post", "ftp", "nntp", "mapi", "ssh", "cifs"] | list[str] | list[dict[str, Any]] | None = ...,
        summary_proto: Literal["smtp", "pop3", "imap", "http-get", "http-post", "ftp", "nntp", "mapi", "ssh", "cifs"] | list[str] | list[dict[str, Any]] | None = ...,
        fortidata_error_action: Literal["log-only", "block", "ignore"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        feature_set: Literal["flow", "proxy"] | None = ...,
        replacemsg_group: str | None = ...,
        rule: str | list[str] | list[dict[str, Any]] | None = ...,
        dlp_log: Literal["enable", "disable"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        nac_quar_log: Literal["enable", "disable"] | None = ...,
        full_archive_proto: Literal["smtp", "pop3", "imap", "http-get", "http-post", "ftp", "nntp", "mapi", "ssh", "cifs"] | list[str] | list[dict[str, Any]] | None = ...,
        summary_proto: Literal["smtp", "pop3", "imap", "http-get", "http-post", "ftp", "nntp", "mapi", "ssh", "cifs"] | list[str] | list[dict[str, Any]] | None = ...,
        fortidata_error_action: Literal["log-only", "block", "ignore"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        feature_set: Literal["flow", "proxy"] | None = ...,
        replacemsg_group: str | None = ...,
        rule: str | list[str] | list[dict[str, Any]] | None = ...,
        dlp_log: Literal["enable", "disable"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        nac_quar_log: Literal["enable", "disable"] | None = ...,
        full_archive_proto: Literal["smtp", "pop3", "imap", "http-get", "http-post", "ftp", "nntp", "mapi", "ssh", "cifs"] | list[str] | list[dict[str, Any]] | None = ...,
        summary_proto: Literal["smtp", "pop3", "imap", "http-get", "http-post", "ftp", "nntp", "mapi", "ssh", "cifs"] | list[str] | list[dict[str, Any]] | None = ...,
        fortidata_error_action: Literal["log-only", "block", "ignore"] | None = ...,
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
    ) -> ProfileObject: ...
    
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
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        feature_set: Literal["flow", "proxy"] | None = ...,
        replacemsg_group: str | None = ...,
        rule: str | list[str] | list[dict[str, Any]] | None = ...,
        dlp_log: Literal["enable", "disable"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        nac_quar_log: Literal["enable", "disable"] | None = ...,
        full_archive_proto: Literal["smtp", "pop3", "imap", "http-get", "http-post", "ftp", "nntp", "mapi", "ssh", "cifs"] | list[str] | list[dict[str, Any]] | None = ...,
        summary_proto: Literal["smtp", "pop3", "imap", "http-get", "http-post", "ftp", "nntp", "mapi", "ssh", "cifs"] | list[str] | list[dict[str, Any]] | None = ...,
        fortidata_error_action: Literal["log-only", "block", "ignore"] | None = ...,
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
    "Profile",
    "ProfilePayload",
    "ProfileObject",
]