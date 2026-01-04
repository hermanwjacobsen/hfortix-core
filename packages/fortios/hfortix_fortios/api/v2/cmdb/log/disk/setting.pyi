from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class SettingPayload(TypedDict, total=False):
    """
    Type hints for log/disk/setting payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
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
    uploadport: NotRequired[int]  # TCP port to use for communicating with the FTP server (defau
    source_ip: NotRequired[str]  # Source IP address to use for uploading disk log files.
    uploaduser: str  # Username required to log into the FTP server to upload disk 
    uploadpass: NotRequired[str]  # Password required to log into the FTP server to upload disk 
    uploaddir: NotRequired[str]  # The remote directory on the FTP server to upload log files t
    uploadtype: NotRequired[Literal["traffic", "event", "virus", "webfilter", "IPS", "emailfilter", "dlp-archive", "anomaly", "voip", "dlp", "app-ctrl", "waf", "gtp", "dns", "ssh", "ssl", "file-filter", "icap", "virtual-patch", "debug"]]  # Types of log files to upload. Separate multiple entries with
    uploadsched: NotRequired[Literal["disable", "enable"]]  # Set the schedule for uploading log files to the FTP server (
    uploadtime: NotRequired[str]  # Time of day at which log files are uploaded if uploadsched i
    upload_delete_files: NotRequired[Literal["enable", "disable"]]  # Delete log files after uploading (default = enable).
    upload_ssl_conn: NotRequired[Literal["default", "high", "low", "disable"]]  # Enable/disable encrypted FTPS communication to upload log fi
    full_first_warning_threshold: NotRequired[int]  # Log full first warning threshold as a percent (1 - 98, defau
    full_second_warning_threshold: NotRequired[int]  # Log full second warning threshold as a percent (2 - 99, defa
    full_final_warning_threshold: NotRequired[int]  # Log full final warning threshold as a percent (3 - 100, defa
    interface_select_method: NotRequired[Literal["auto", "sdwan", "specify"]]  # Specify how to select outgoing interface to reach server.
    interface: str  # Specify outgoing interface to reach server.
    vrf_select: NotRequired[int]  # VRF ID used for connection to server.


class Setting:
    """
    Settings for local disk logging.
    
    Path: log/disk/setting
    Category: cmdb
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
        payload_dict: SettingPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        ips_archive: Literal["enable", "disable"] | None = ...,
        max_log_file_size: int | None = ...,
        max_policy_packet_capture_size: int | None = ...,
        roll_schedule: Literal["daily", "weekly"] | None = ...,
        roll_day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | None = ...,
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
        uploadtype: Literal["traffic", "event", "virus", "webfilter", "IPS", "emailfilter", "dlp-archive", "anomaly", "voip", "dlp", "app-ctrl", "waf", "gtp", "dns", "ssh", "ssl", "file-filter", "icap", "virtual-patch", "debug"] | None = ...,
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
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: SettingPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        ips_archive: Literal["enable", "disable"] | None = ...,
        max_log_file_size: int | None = ...,
        max_policy_packet_capture_size: int | None = ...,
        roll_schedule: Literal["daily", "weekly"] | None = ...,
        roll_day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | None = ...,
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
        uploadtype: Literal["traffic", "event", "virus", "webfilter", "IPS", "emailfilter", "dlp-archive", "anomaly", "voip", "dlp", "app-ctrl", "waf", "gtp", "dns", "ssh", "ssl", "file-filter", "icap", "virtual-patch", "debug"] | None = ...,
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
        payload_dict: SettingPayload | None = ...,
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
    "Setting",
    "SettingPayload",
]