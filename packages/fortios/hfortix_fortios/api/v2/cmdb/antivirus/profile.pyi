from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class ProfilePayload(TypedDict, total=False):
    """
    Type hints for antivirus/profile payload fields.
    
    Configure AntiVirus profiles.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.dlp.filepattern.FilepatternEndpoint` (via: analytics-accept-filetype, analytics-ignore-filetype)
        - :class:`~.system.replacemsg-group.ReplacemsgGroupEndpoint` (via: replacemsg-group)

    **Usage:**
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
    fortisandbox_scan_timeout: NotRequired[int]  # FortiSandbox inline scan timeout in seconds
    fortisandbox_error_action: NotRequired[Literal["log-only", "block", "ignore"]]  # Action to take if FortiSandbox inline scan encounters an err
    fortisandbox_timeout_action: NotRequired[Literal["log-only", "block", "ignore"]]  # Action to take if FortiSandbox inline scan encounters a scan
    av_virus_log: NotRequired[Literal["enable", "disable"]]  # Enable/disable AntiVirus logging.
    extended_log: NotRequired[Literal["enable", "disable"]]  # Enable/disable extended logging for antivirus.
    scan_mode: NotRequired[Literal["default", "legacy"]]  # Configure scan mode (default or legacy).

# Nested classes for table field children

@final
class ProfileExternalblocklistObject:
    """Typed object for external-blocklist table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # External blocklist.
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
class ProfileResponse(TypedDict):
    """
    Type hints for antivirus/profile API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
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
    external_blocklist: list[dict[str, Any]]
    ems_threat_feed: Literal["disable", "enable"]
    fortindr_error_action: Literal["log-only", "block", "ignore"]
    fortindr_timeout_action: Literal["log-only", "block", "ignore"]
    fortisandbox_scan_timeout: int
    fortisandbox_error_action: Literal["log-only", "block", "ignore"]
    fortisandbox_timeout_action: Literal["log-only", "block", "ignore"]
    av_virus_log: Literal["enable", "disable"]
    extended_log: Literal["enable", "disable"]
    scan_mode: Literal["default", "legacy"]


@final
class ProfileObject:
    """Typed FortiObject for antivirus/profile with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Profile name.
    name: str
    # Comment.
    comment: str
    # Replacement message group customized for this profile.
    replacemsg_group: str
    # Flow/proxy feature set.
    feature_set: Literal["flow", "proxy"]
    # FortiSandbox scan modes.
    fortisandbox_mode: Literal["inline", "analytics-suspicious", "analytics-everything"]
    # Maximum size of files that can be uploaded to FortiSandbox in Mbytes.
    fortisandbox_max_upload: int
    # Do not submit files matching this DLP file-pattern to FortiSandbox
    analytics_ignore_filetype: int
    # Only submit files matching this DLP file-pattern to FortiSandbox
    analytics_accept_filetype: int
    # Enable/disable using the FortiSandbox signature database to supplement the AV si
    analytics_db: Literal["disable", "enable"]
    # Enable/disable using the mobile malware signature database.
    mobile_malware_db: Literal["disable", "enable"]
    # Configure HTTP AntiVirus options.
    http: str
    # Configure FTP AntiVirus options.
    ftp: str
    # Configure IMAP AntiVirus options.
    imap: str
    # Configure POP3 AntiVirus options.
    pop3: str
    # Configure SMTP AntiVirus options.
    smtp: str
    # Configure MAPI AntiVirus options.
    mapi: str
    # Configure NNTP AntiVirus options.
    nntp: str
    # Configure CIFS AntiVirus options.
    cifs: str
    # Configure SFTP and SCP AntiVirus options.
    ssh: str
    # Configure AntiVirus quarantine settings.
    nac_quar: str
    # AV Content Disarm and Reconstruction settings.
    content_disarm: str
    # Enable/disable outbreak-prevention archive scanning.
    outbreak_prevention_archive_scan: Literal["disable", "enable"]
    # Enable/disable all external blocklists.
    external_blocklist_enable_all: Literal["disable", "enable"]
    # One or more external malware block lists.
    external_blocklist: list[ProfileExternalblocklistObject]  # Table field - list of typed objects
    # Enable/disable use of EMS threat feed when performing AntiVirus scan. Analyzes f
    ems_threat_feed: Literal["disable", "enable"]
    # Action to take if FortiNDR encounters an error.
    fortindr_error_action: Literal["log-only", "block", "ignore"]
    # Action to take if FortiNDR encounters a scan timeout.
    fortindr_timeout_action: Literal["log-only", "block", "ignore"]
    # FortiSandbox inline scan timeout in seconds (30 - 180, default = 60).
    fortisandbox_scan_timeout: int
    # Action to take if FortiSandbox inline scan encounters an error.
    fortisandbox_error_action: Literal["log-only", "block", "ignore"]
    # Action to take if FortiSandbox inline scan encounters a scan timeout.
    fortisandbox_timeout_action: Literal["log-only", "block", "ignore"]
    # Enable/disable AntiVirus logging.
    av_virus_log: Literal["enable", "disable"]
    # Enable/disable extended logging for antivirus.
    extended_log: Literal["enable", "disable"]
    # Configure scan mode (default or legacy).
    scan_mode: Literal["default", "legacy"]
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> ProfilePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class Profile:
    """
    Configure AntiVirus profiles.
    
    Path: antivirus/profile
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
    ) -> ProfileObject: ...
    
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
    ) -> ProfileObject: ...
    
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
    ) -> ProfileResponse: ...
    
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
    ) -> ProfileResponse: ...
    
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
    ) -> list[ProfileResponse]: ...
    
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
        external_blocklist: str | list[str] | list[dict[str, Any]] | None = ...,
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
        external_blocklist: str | list[str] | list[dict[str, Any]] | None = ...,
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
        external_blocklist: str | list[str] | list[dict[str, Any]] | None = ...,
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
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
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
        external_blocklist: str | list[str] | list[dict[str, Any]] | None = ...,
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
        external_blocklist: str | list[str] | list[dict[str, Any]] | None = ...,
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
        external_blocklist: str | list[str] | list[dict[str, Any]] | None = ...,
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
        external_blocklist: str | list[str] | list[dict[str, Any]] | None = ...,
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
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
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
        external_blocklist: str | list[str] | list[dict[str, Any]] | None = ...,
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
        external_blocklist: str | list[str] | list[dict[str, Any]] | None = ...,
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