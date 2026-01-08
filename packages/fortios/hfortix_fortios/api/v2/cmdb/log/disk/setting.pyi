from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class SettingPayload(TypedDict, total=False):
    """
    Type hints for log/disk/setting payload fields.
    
    Settings for local disk logging.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: interface)

    **Usage:**
        payload: SettingPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    status: Literal["enable", "disable"]  # Enable/disable local disk logging.
    ips_archive: NotRequired[Literal["enable", "disable"]]  # Enable/disable IPS packet archiving to the local disk.
    max_log_file_size: NotRequired[int]  # Maximum log file size before rolling (1 - 100 Mbytes).
    max_policy_packet_capture_size: NotRequired[int]  # Maximum size of policy sniffer in MB (0 means unlimited).
    roll_schedule: NotRequired[Literal["daily", "weekly"]]  # Frequency to check log file for rolling.
    roll_day: NotRequired[Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]]  # Day of week on which to roll log file.
    roll_time: NotRequired[str]  # Time of day to roll the log file (hh:mm).
    diskfull: NotRequired[Literal["overwrite", "nolog"]]  # Action to take when disk is full. The system can overwrite t
    log_quota: NotRequired[int]  # Disk log quota (MB).
    dlp_archive_quota: NotRequired[int]  # DLP archive quota (MB).
    report_quota: NotRequired[int]  # Report db quota (MB).
    maximum_log_age: NotRequired[int]  # Delete log files older than (days).
    upload: NotRequired[Literal["enable", "disable"]]  # Enable/disable uploading log files when they are rolled.
    upload_destination: NotRequired[Literal["ftp-server"]]  # The type of server to upload log files to. Only FTP is curre
    uploadip: str  # IP address of the FTP server to upload log files to.
    uploadport: NotRequired[int]  # TCP port to use for communicating with the FTP server
    source_ip: NotRequired[str]  # Source IP address to use for uploading disk log files.
    uploaduser: str  # Username required to log into the FTP server to upload disk
    uploadpass: NotRequired[str]  # Password required to log into the FTP server to upload disk
    uploaddir: NotRequired[str]  # The remote directory on the FTP server to upload log files t
    uploadtype: NotRequired[Literal["traffic", "event", "virus", "webfilter", "IPS", "emailfilter", "dlp-archive", "anomaly", "voip", "dlp", "app-ctrl", "waf", "gtp", "dns", "ssh", "ssl", "file-filter", "icap", "virtual-patch", "debug"]]  # Types of log files to upload. Separate multiple entries with
    uploadsched: NotRequired[Literal["disable", "enable"]]  # Set the schedule for uploading log files to the FTP server
    uploadtime: NotRequired[str]  # Time of day at which log files are uploaded if uploadsched i
    upload_delete_files: NotRequired[Literal["enable", "disable"]]  # Delete log files after uploading (default = enable).
    upload_ssl_conn: NotRequired[Literal["default", "high", "low", "disable"]]  # Enable/disable encrypted FTPS communication to upload log fi
    full_first_warning_threshold: NotRequired[int]  # Log full first warning threshold as a percent
    full_second_warning_threshold: NotRequired[int]  # Log full second warning threshold as a percent
    full_final_warning_threshold: NotRequired[int]  # Log full final warning threshold as a percent
    interface_select_method: NotRequired[Literal["auto", "sdwan", "specify"]]  # Specify how to select outgoing interface to reach server.
    interface: str  # Specify outgoing interface to reach server.
    vrf_select: NotRequired[int]  # VRF ID used for connection to server.

# Nested classes for table field children


# Response TypedDict for GET returns (all fields present in API response)
class SettingResponse(TypedDict):
    """
    Type hints for log/disk/setting API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    status: Literal["enable", "disable"]
    ips_archive: Literal["enable", "disable"]
    max_log_file_size: int
    max_policy_packet_capture_size: int
    roll_schedule: Literal["daily", "weekly"]
    roll_day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
    roll_time: str
    diskfull: Literal["overwrite", "nolog"]
    log_quota: int
    dlp_archive_quota: int
    report_quota: int
    maximum_log_age: int
    upload: Literal["enable", "disable"]
    upload_destination: Literal["ftp-server"]
    uploadip: str
    uploadport: int
    source_ip: str
    uploaduser: str
    uploadpass: str
    uploaddir: str
    uploadtype: Literal["traffic", "event", "virus", "webfilter", "IPS", "emailfilter", "dlp-archive", "anomaly", "voip", "dlp", "app-ctrl", "waf", "gtp", "dns", "ssh", "ssl", "file-filter", "icap", "virtual-patch", "debug"]
    uploadsched: Literal["disable", "enable"]
    uploadtime: str
    upload_delete_files: Literal["enable", "disable"]
    upload_ssl_conn: Literal["default", "high", "low", "disable"]
    full_first_warning_threshold: int
    full_second_warning_threshold: int
    full_final_warning_threshold: int
    interface_select_method: Literal["auto", "sdwan", "specify"]
    interface: str
    vrf_select: int


@final
class SettingObject:
    """Typed FortiObject for log/disk/setting with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Enable/disable local disk logging.
    status: Literal["enable", "disable"]
    # Enable/disable IPS packet archiving to the local disk.
    ips_archive: Literal["enable", "disable"]
    # Maximum log file size before rolling (1 - 100 Mbytes).
    max_log_file_size: int
    # Maximum size of policy sniffer in MB (0 means unlimited).
    max_policy_packet_capture_size: int
    # Frequency to check log file for rolling.
    roll_schedule: Literal["daily", "weekly"]
    # Day of week on which to roll log file.
    roll_day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
    # Time of day to roll the log file (hh:mm).
    roll_time: str
    # Action to take when disk is full. The system can overwrite the oldest log messag
    diskfull: Literal["overwrite", "nolog"]
    # Disk log quota (MB).
    log_quota: int
    # DLP archive quota (MB).
    dlp_archive_quota: int
    # Report db quota (MB).
    report_quota: int
    # Delete log files older than (days).
    maximum_log_age: int
    # Enable/disable uploading log files when they are rolled.
    upload: Literal["enable", "disable"]
    # The type of server to upload log files to. Only FTP is currently supported.
    upload_destination: Literal["ftp-server"]
    # IP address of the FTP server to upload log files to.
    uploadip: str
    # TCP port to use for communicating with the FTP server (default = 21).
    uploadport: int
    # Source IP address to use for uploading disk log files.
    source_ip: str
    # Username required to log into the FTP server to upload disk log files.
    uploaduser: str
    # Password required to log into the FTP server to upload disk log files.
    uploadpass: str
    # The remote directory on the FTP server to upload log files to.
    uploaddir: str
    # Types of log files to upload. Separate multiple entries with a space.
    uploadtype: Literal["traffic", "event", "virus", "webfilter", "IPS", "emailfilter", "dlp-archive", "anomaly", "voip", "dlp", "app-ctrl", "waf", "gtp", "dns", "ssh", "ssl", "file-filter", "icap", "virtual-patch", "debug"]
    # Set the schedule for uploading log files to the FTP server
    uploadsched: Literal["disable", "enable"]
    # Time of day at which log files are uploaded if uploadsched is enabled
    uploadtime: str
    # Delete log files after uploading (default = enable).
    upload_delete_files: Literal["enable", "disable"]
    # Enable/disable encrypted FTPS communication to upload log files.
    upload_ssl_conn: Literal["default", "high", "low", "disable"]
    # Log full first warning threshold as a percent (1 - 98, default = 75).
    full_first_warning_threshold: int
    # Log full second warning threshold as a percent (2 - 99, default = 90).
    full_second_warning_threshold: int
    # Log full final warning threshold as a percent (3 - 100, default = 95).
    full_final_warning_threshold: int
    # Specify how to select outgoing interface to reach server.
    interface_select_method: Literal["auto", "sdwan", "specify"]
    # Specify outgoing interface to reach server.
    interface: str
    # VRF ID used for connection to server.
    vrf_select: int
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> SettingPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class Setting:
    """
    Settings for local disk logging.
    
    Path: log/disk/setting
    Category: cmdb
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
    ) -> SettingObject: ...
    
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
    ) -> SettingObject: ...
    
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
    ) -> SettingObject: ...
    
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
    ) -> SettingResponse: ...
    
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
    ) -> SettingResponse: ...
    
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
    ) -> SettingResponse: ...
    
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
    ) -> dict[str, Any]: ...
    
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
    ) -> SettingObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: SettingPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        ips_archive: Literal["enable", "disable"] | None = ...,
        max_log_file_size: int | None = ...,
        max_policy_packet_capture_size: int | None = ...,
        roll_schedule: Literal["daily", "weekly"] | None = ...,
        roll_day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | list[str] | None = ...,
        roll_time: str | None = ...,
        diskfull: Literal["overwrite", "nolog"] | None = ...,
        log_quota: int | None = ...,
        dlp_archive_quota: int | None = ...,
        report_quota: int | None = ...,
        maximum_log_age: int | None = ...,
        upload: Literal["enable", "disable"] | None = ...,
        upload_destination: Literal["ftp-server"] | None = ...,
        uploadip: str | None = ...,
        uploadport: int | None = ...,
        source_ip: str | None = ...,
        uploaduser: str | None = ...,
        uploadpass: str | None = ...,
        uploaddir: str | None = ...,
        uploadtype: Literal["traffic", "event", "virus", "webfilter", "IPS", "emailfilter", "dlp-archive", "anomaly", "voip", "dlp", "app-ctrl", "waf", "gtp", "dns", "ssh", "ssl", "file-filter", "icap", "virtual-patch", "debug"] | list[str] | None = ...,
        uploadsched: Literal["disable", "enable"] | None = ...,
        uploadtime: str | None = ...,
        upload_delete_files: Literal["enable", "disable"] | None = ...,
        upload_ssl_conn: Literal["default", "high", "low", "disable"] | None = ...,
        full_first_warning_threshold: int | None = ...,
        full_second_warning_threshold: int | None = ...,
        full_final_warning_threshold: int | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> SettingObject: ...
    
    @overload
    def put(
        self,
        payload_dict: SettingPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        ips_archive: Literal["enable", "disable"] | None = ...,
        max_log_file_size: int | None = ...,
        max_policy_packet_capture_size: int | None = ...,
        roll_schedule: Literal["daily", "weekly"] | None = ...,
        roll_day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | list[str] | None = ...,
        roll_time: str | None = ...,
        diskfull: Literal["overwrite", "nolog"] | None = ...,
        log_quota: int | None = ...,
        dlp_archive_quota: int | None = ...,
        report_quota: int | None = ...,
        maximum_log_age: int | None = ...,
        upload: Literal["enable", "disable"] | None = ...,
        upload_destination: Literal["ftp-server"] | None = ...,
        uploadip: str | None = ...,
        uploadport: int | None = ...,
        source_ip: str | None = ...,
        uploaduser: str | None = ...,
        uploadpass: str | None = ...,
        uploaddir: str | None = ...,
        uploadtype: Literal["traffic", "event", "virus", "webfilter", "IPS", "emailfilter", "dlp-archive", "anomaly", "voip", "dlp", "app-ctrl", "waf", "gtp", "dns", "ssh", "ssl", "file-filter", "icap", "virtual-patch", "debug"] | list[str] | None = ...,
        uploadsched: Literal["disable", "enable"] | None = ...,
        uploadtime: str | None = ...,
        upload_delete_files: Literal["enable", "disable"] | None = ...,
        upload_ssl_conn: Literal["default", "high", "low", "disable"] | None = ...,
        full_first_warning_threshold: int | None = ...,
        full_second_warning_threshold: int | None = ...,
        full_final_warning_threshold: int | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: SettingPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        ips_archive: Literal["enable", "disable"] | None = ...,
        max_log_file_size: int | None = ...,
        max_policy_packet_capture_size: int | None = ...,
        roll_schedule: Literal["daily", "weekly"] | None = ...,
        roll_day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | list[str] | None = ...,
        roll_time: str | None = ...,
        diskfull: Literal["overwrite", "nolog"] | None = ...,
        log_quota: int | None = ...,
        dlp_archive_quota: int | None = ...,
        report_quota: int | None = ...,
        maximum_log_age: int | None = ...,
        upload: Literal["enable", "disable"] | None = ...,
        upload_destination: Literal["ftp-server"] | None = ...,
        uploadip: str | None = ...,
        uploadport: int | None = ...,
        source_ip: str | None = ...,
        uploaduser: str | None = ...,
        uploadpass: str | None = ...,
        uploaddir: str | None = ...,
        uploadtype: Literal["traffic", "event", "virus", "webfilter", "IPS", "emailfilter", "dlp-archive", "anomaly", "voip", "dlp", "app-ctrl", "waf", "gtp", "dns", "ssh", "ssl", "file-filter", "icap", "virtual-patch", "debug"] | list[str] | None = ...,
        uploadsched: Literal["disable", "enable"] | None = ...,
        uploadtime: str | None = ...,
        upload_delete_files: Literal["enable", "disable"] | None = ...,
        upload_ssl_conn: Literal["default", "high", "low", "disable"] | None = ...,
        full_first_warning_threshold: int | None = ...,
        full_second_warning_threshold: int | None = ...,
        full_final_warning_threshold: int | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: SettingPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        ips_archive: Literal["enable", "disable"] | None = ...,
        max_log_file_size: int | None = ...,
        max_policy_packet_capture_size: int | None = ...,
        roll_schedule: Literal["daily", "weekly"] | None = ...,
        roll_day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | list[str] | None = ...,
        roll_time: str | None = ...,
        diskfull: Literal["overwrite", "nolog"] | None = ...,
        log_quota: int | None = ...,
        dlp_archive_quota: int | None = ...,
        report_quota: int | None = ...,
        maximum_log_age: int | None = ...,
        upload: Literal["enable", "disable"] | None = ...,
        upload_destination: Literal["ftp-server"] | None = ...,
        uploadip: str | None = ...,
        uploadport: int | None = ...,
        source_ip: str | None = ...,
        uploaduser: str | None = ...,
        uploadpass: str | None = ...,
        uploaddir: str | None = ...,
        uploadtype: Literal["traffic", "event", "virus", "webfilter", "IPS", "emailfilter", "dlp-archive", "anomaly", "voip", "dlp", "app-ctrl", "waf", "gtp", "dns", "ssh", "ssl", "file-filter", "icap", "virtual-patch", "debug"] | list[str] | None = ...,
        uploadsched: Literal["disable", "enable"] | None = ...,
        uploadtime: str | None = ...,
        upload_delete_files: Literal["enable", "disable"] | None = ...,
        upload_ssl_conn: Literal["default", "high", "low", "disable"] | None = ...,
        full_first_warning_threshold: int | None = ...,
        full_second_warning_threshold: int | None = ...,
        full_final_warning_threshold: int | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: SettingPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        ips_archive: Literal["enable", "disable"] | None = ...,
        max_log_file_size: int | None = ...,
        max_policy_packet_capture_size: int | None = ...,
        roll_schedule: Literal["daily", "weekly"] | None = ...,
        roll_day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | list[str] | None = ...,
        roll_time: str | None = ...,
        diskfull: Literal["overwrite", "nolog"] | None = ...,
        log_quota: int | None = ...,
        dlp_archive_quota: int | None = ...,
        report_quota: int | None = ...,
        maximum_log_age: int | None = ...,
        upload: Literal["enable", "disable"] | None = ...,
        upload_destination: Literal["ftp-server"] | None = ...,
        uploadip: str | None = ...,
        uploadport: int | None = ...,
        source_ip: str | None = ...,
        uploaduser: str | None = ...,
        uploadpass: str | None = ...,
        uploaddir: str | None = ...,
        uploadtype: Literal["traffic", "event", "virus", "webfilter", "IPS", "emailfilter", "dlp-archive", "anomaly", "voip", "dlp", "app-ctrl", "waf", "gtp", "dns", "ssh", "ssl", "file-filter", "icap", "virtual-patch", "debug"] | list[str] | None = ...,
        uploadsched: Literal["disable", "enable"] | None = ...,
        uploadtime: str | None = ...,
        upload_delete_files: Literal["enable", "disable"] | None = ...,
        upload_ssl_conn: Literal["default", "high", "low", "disable"] | None = ...,
        full_first_warning_threshold: int | None = ...,
        full_second_warning_threshold: int | None = ...,
        full_final_warning_threshold: int | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
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
    "Setting",
    "SettingPayload",
    "SettingObject",
]