from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class ProfilePayload(TypedDict, total=False):
    """
    Type hints for antivirus/profile payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: ProfilePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Profile name.
    comment: NotRequired[str]  # Comment.
    replacemsg_group: NotRequired[str]  # Replacement message group customized for this profile.
    feature_set: NotRequired[Literal["flow", "proxy"]]  # Flow/proxy feature set.
    fortisandbox_mode: NotRequired[Literal["inline", "analytics-suspicious", "analytics-everything"]]  # FortiSandbox scan modes.
    fortisandbox_max_upload: NotRequired[int]  # Maximum size of files that can be uploaded to FortiSandbox i
    analytics_ignore_filetype: NotRequired[int]  # Do not submit files matching this DLP file-pattern to FortiS
    analytics_accept_filetype: NotRequired[int]  # Only submit files matching this DLP file-pattern to FortiSan
    analytics_db: NotRequired[Literal["disable", "enable"]]  # Enable/disable using the FortiSandbox signature database to 
    mobile_malware_db: NotRequired[Literal["disable", "enable"]]  # Enable/disable using the mobile malware signature database.
    http: NotRequired[str]  # Configure HTTP AntiVirus options.
    ftp: NotRequired[str]  # Configure FTP AntiVirus options.
    imap: NotRequired[str]  # Configure IMAP AntiVirus options.
    pop3: NotRequired[str]  # Configure POP3 AntiVirus options.
    smtp: NotRequired[str]  # Configure SMTP AntiVirus options.
    mapi: NotRequired[str]  # Configure MAPI AntiVirus options.
    nntp: NotRequired[str]  # Configure NNTP AntiVirus options.
    cifs: NotRequired[str]  # Configure CIFS AntiVirus options.
    ssh: NotRequired[str]  # Configure SFTP and SCP AntiVirus options.
    nac_quar: NotRequired[str]  # Configure AntiVirus quarantine settings.
    content_disarm: NotRequired[str]  # AV Content Disarm and Reconstruction settings.
    outbreak_prevention_archive_scan: NotRequired[Literal["disable", "enable"]]  # Enable/disable outbreak-prevention archive scanning.
    external_blocklist_enable_all: NotRequired[Literal["disable", "enable"]]  # Enable/disable all external blocklists.
    external_blocklist: NotRequired[list[dict[str, Any]]]  # One or more external malware block lists.
    ems_threat_feed: NotRequired[Literal["disable", "enable"]]  # Enable/disable use of EMS threat feed when performing AntiVi
    fortindr_error_action: NotRequired[Literal["log-only", "block", "ignore"]]  # Action to take if FortiNDR encounters an error.
    fortindr_timeout_action: NotRequired[Literal["log-only", "block", "ignore"]]  # Action to take if FortiNDR encounters a scan timeout.
    fortisandbox_error_action: NotRequired[Literal["log-only", "block", "ignore"]]  # Action to take if FortiSandbox inline scan encounters an err
    fortisandbox_timeout_action: NotRequired[Literal["log-only", "block", "ignore"]]  # Action to take if FortiSandbox inline scan encounters a scan
    av_virus_log: NotRequired[Literal["enable", "disable"]]  # Enable/disable AntiVirus logging.
    extended_log: NotRequired[Literal["enable", "disable"]]  # Enable/disable extended logging for antivirus.
    scan_mode: NotRequired[Literal["default", "legacy"]]  # Configure scan mode (default or legacy).


class Profile:
    """
    Configure AntiVirus profiles.
    
    Path: antivirus/profile
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
        external_blocklist: list[dict[str, Any]] | None = ...,
        ems_threat_feed: Literal["disable", "enable"] | None = ...,
        fortindr_error_action: Literal["log-only", "block", "ignore"] | None = ...,
        fortindr_timeout_action: Literal["log-only", "block", "ignore"] | None = ...,
        fortisandbox_error_action: Literal["log-only", "block", "ignore"] | None = ...,
        fortisandbox_timeout_action: Literal["log-only", "block", "ignore"] | None = ...,
        av_virus_log: Literal["enable", "disable"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        scan_mode: Literal["default", "legacy"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
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
        external_blocklist: list[dict[str, Any]] | None = ...,
        ems_threat_feed: Literal["disable", "enable"] | None = ...,
        fortindr_error_action: Literal["log-only", "block", "ignore"] | None = ...,
        fortindr_timeout_action: Literal["log-only", "block", "ignore"] | None = ...,
        fortisandbox_error_action: Literal["log-only", "block", "ignore"] | None = ...,
        fortisandbox_timeout_action: Literal["log-only", "block", "ignore"] | None = ...,
        av_virus_log: Literal["enable", "disable"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        scan_mode: Literal["default", "legacy"] | None = ...,
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


__all__ = [
    "Profile",
    "ProfilePayload",
]