from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class ProfilePayload(TypedDict, total=False):
    """
    Type hints for dlp/profile payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
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


class Profile:
    """
    Configure DLP profiles.
    
    Path: dlp/profile
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
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        feature_set: Literal["flow", "proxy"] | None = ...,
        replacemsg_group: str | None = ...,
        rule: list[dict[str, Any]] | None = ...,
        dlp_log: Literal["enable", "disable"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        nac_quar_log: Literal["enable", "disable"] | None = ...,
        full_archive_proto: Literal["smtp", "pop3", "imap", "http-get", "http-post", "ftp", "nntp", "mapi", "ssh", "cifs"] | None = ...,
        summary_proto: Literal["smtp", "pop3", "imap", "http-get", "http-post", "ftp", "nntp", "mapi", "ssh", "cifs"] | None = ...,
        fortidata_error_action: Literal["log-only", "block", "ignore"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        feature_set: Literal["flow", "proxy"] | None = ...,
        replacemsg_group: str | None = ...,
        rule: list[dict[str, Any]] | None = ...,
        dlp_log: Literal["enable", "disable"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        nac_quar_log: Literal["enable", "disable"] | None = ...,
        full_archive_proto: Literal["smtp", "pop3", "imap", "http-get", "http-post", "ftp", "nntp", "mapi", "ssh", "cifs"] | None = ...,
        summary_proto: Literal["smtp", "pop3", "imap", "http-get", "http-post", "ftp", "nntp", "mapi", "ssh", "cifs"] | None = ...,
        fortidata_error_action: Literal["log-only", "block", "ignore"] | None = ...,
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
        payload_dict: ProfilePayload | None = ...,
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