from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class QuarantinePayload(TypedDict, total=False):
    """
    Type hints for antivirus/quarantine payload fields.
    
    Configure quarantine options.
    
    **Usage:**
        payload: QuarantinePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    agelimit: NotRequired[int]  # Age limit for quarantined files (0 - 479 hours, 0 means fore
    maxfilesize: NotRequired[int]  # Maximum file size to quarantine (0 - 500 Mbytes, 0 means unl
    quarantine_quota: NotRequired[int]  # The amount of disk space to reserve for quarantining files (
    drop_infected: NotRequired[Literal["imap", "smtp", "pop3", "http", "ftp", "nntp", "imaps", "smtps", "pop3s", "https", "ftps", "mapi", "cifs", "ssh"]]  # Do not quarantine infected files found in sessions using the
    store_infected: NotRequired[Literal["imap", "smtp", "pop3", "http", "ftp", "nntp", "imaps", "smtps", "pop3s", "https", "ftps", "mapi", "cifs", "ssh"]]  # Quarantine infected files found in sessions using the select
    drop_machine_learning: NotRequired[Literal["imap", "smtp", "pop3", "http", "ftp", "nntp", "imaps", "smtps", "pop3s", "https", "ftps", "mapi", "cifs", "ssh"]]  # Do not quarantine files detected by machine learning found i
    store_machine_learning: NotRequired[Literal["imap", "smtp", "pop3", "http", "ftp", "nntp", "imaps", "smtps", "pop3s", "https", "ftps", "mapi", "cifs", "ssh"]]  # Quarantine files detected by machine learning found in sessi
    lowspace: NotRequired[Literal["drop-new", "ovrw-old"]]  # Select the method for handling additional files when running
    destination: NotRequired[Literal["NULL", "disk", "FortiAnalyzer"]]  # Choose whether to quarantine files to the FortiGate disk or 


class QuarantineObject(FortiObject[QuarantinePayload]):
    """Typed FortiObject for antivirus/quarantine with IDE autocomplete support."""
    
    # Age limit for quarantined files (0 - 479 hours, 0 means forever).
    agelimit: int
    # Maximum file size to quarantine (0 - 500 Mbytes, 0 means unlimited).
    maxfilesize: int
    # The amount of disk space to reserve for quarantining files (0 - 4294967295 Mbyte
    quarantine_quota: int
    # Do not quarantine infected files found in sessions using the selected protocols.
    drop_infected: Literal["imap", "smtp", "pop3", "http", "ftp", "nntp", "imaps", "smtps", "pop3s", "https", "ftps", "mapi", "cifs", "ssh"]
    # Quarantine infected files found in sessions using the selected protocols.
    store_infected: Literal["imap", "smtp", "pop3", "http", "ftp", "nntp", "imaps", "smtps", "pop3s", "https", "ftps", "mapi", "cifs", "ssh"]
    # Do not quarantine files detected by machine learning found in sessions using the
    drop_machine_learning: Literal["imap", "smtp", "pop3", "http", "ftp", "nntp", "imaps", "smtps", "pop3s", "https", "ftps", "mapi", "cifs", "ssh"]
    # Quarantine files detected by machine learning found in sessions using the select
    store_machine_learning: Literal["imap", "smtp", "pop3", "http", "ftp", "nntp", "imaps", "smtps", "pop3s", "https", "ftps", "mapi", "cifs", "ssh"]
    # Select the method for handling additional files when running low on disk space.
    lowspace: Literal["drop-new", "ovrw-old"]
    # Choose whether to quarantine files to the FortiGate disk or to FortiAnalyzer or 
    destination: Literal["NULL", "disk", "FortiAnalyzer"]
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> QuarantinePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Quarantine:
    """
    Configure quarantine options.
    
    Path: antivirus/quarantine
    Category: cmdb
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
    ) -> QuarantineObject: ...
    
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
    ) -> QuarantineObject: ...
    
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
    ) -> QuarantineObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: QuarantinePayload | None = ...,
        agelimit: int | None = ...,
        maxfilesize: int | None = ...,
        quarantine_quota: int | None = ...,
        drop_infected: Literal["imap", "smtp", "pop3", "http", "ftp", "nntp", "imaps", "smtps", "pop3s", "https", "ftps", "mapi", "cifs", "ssh"] | list[str] | list[dict[str, Any]] | None = ...,
        store_infected: Literal["imap", "smtp", "pop3", "http", "ftp", "nntp", "imaps", "smtps", "pop3s", "https", "ftps", "mapi", "cifs", "ssh"] | list[str] | list[dict[str, Any]] | None = ...,
        drop_machine_learning: Literal["imap", "smtp", "pop3", "http", "ftp", "nntp", "imaps", "smtps", "pop3s", "https", "ftps", "mapi", "cifs", "ssh"] | list[str] | list[dict[str, Any]] | None = ...,
        store_machine_learning: Literal["imap", "smtp", "pop3", "http", "ftp", "nntp", "imaps", "smtps", "pop3s", "https", "ftps", "mapi", "cifs", "ssh"] | list[str] | list[dict[str, Any]] | None = ...,
        lowspace: Literal["drop-new", "ovrw-old"] | None = ...,
        destination: Literal["NULL", "disk", "FortiAnalyzer"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> QuarantineObject: ...
    
    @overload
    def put(
        self,
        payload_dict: QuarantinePayload | None = ...,
        agelimit: int | None = ...,
        maxfilesize: int | None = ...,
        quarantine_quota: int | None = ...,
        drop_infected: Literal["imap", "smtp", "pop3", "http", "ftp", "nntp", "imaps", "smtps", "pop3s", "https", "ftps", "mapi", "cifs", "ssh"] | list[str] | list[dict[str, Any]] | None = ...,
        store_infected: Literal["imap", "smtp", "pop3", "http", "ftp", "nntp", "imaps", "smtps", "pop3s", "https", "ftps", "mapi", "cifs", "ssh"] | list[str] | list[dict[str, Any]] | None = ...,
        drop_machine_learning: Literal["imap", "smtp", "pop3", "http", "ftp", "nntp", "imaps", "smtps", "pop3s", "https", "ftps", "mapi", "cifs", "ssh"] | list[str] | list[dict[str, Any]] | None = ...,
        store_machine_learning: Literal["imap", "smtp", "pop3", "http", "ftp", "nntp", "imaps", "smtps", "pop3s", "https", "ftps", "mapi", "cifs", "ssh"] | list[str] | list[dict[str, Any]] | None = ...,
        lowspace: Literal["drop-new", "ovrw-old"] | None = ...,
        destination: Literal["NULL", "disk", "FortiAnalyzer"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: QuarantinePayload | None = ...,
        agelimit: int | None = ...,
        maxfilesize: int | None = ...,
        quarantine_quota: int | None = ...,
        drop_infected: Literal["imap", "smtp", "pop3", "http", "ftp", "nntp", "imaps", "smtps", "pop3s", "https", "ftps", "mapi", "cifs", "ssh"] | list[str] | list[dict[str, Any]] | None = ...,
        store_infected: Literal["imap", "smtp", "pop3", "http", "ftp", "nntp", "imaps", "smtps", "pop3s", "https", "ftps", "mapi", "cifs", "ssh"] | list[str] | list[dict[str, Any]] | None = ...,
        drop_machine_learning: Literal["imap", "smtp", "pop3", "http", "ftp", "nntp", "imaps", "smtps", "pop3s", "https", "ftps", "mapi", "cifs", "ssh"] | list[str] | list[dict[str, Any]] | None = ...,
        store_machine_learning: Literal["imap", "smtp", "pop3", "http", "ftp", "nntp", "imaps", "smtps", "pop3s", "https", "ftps", "mapi", "cifs", "ssh"] | list[str] | list[dict[str, Any]] | None = ...,
        lowspace: Literal["drop-new", "ovrw-old"] | None = ...,
        destination: Literal["NULL", "disk", "FortiAnalyzer"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: QuarantinePayload | None = ...,
        agelimit: int | None = ...,
        maxfilesize: int | None = ...,
        quarantine_quota: int | None = ...,
        drop_infected: Literal["imap", "smtp", "pop3", "http", "ftp", "nntp", "imaps", "smtps", "pop3s", "https", "ftps", "mapi", "cifs", "ssh"] | list[str] | list[dict[str, Any]] | None = ...,
        store_infected: Literal["imap", "smtp", "pop3", "http", "ftp", "nntp", "imaps", "smtps", "pop3s", "https", "ftps", "mapi", "cifs", "ssh"] | list[str] | list[dict[str, Any]] | None = ...,
        drop_machine_learning: Literal["imap", "smtp", "pop3", "http", "ftp", "nntp", "imaps", "smtps", "pop3s", "https", "ftps", "mapi", "cifs", "ssh"] | list[str] | list[dict[str, Any]] | None = ...,
        store_machine_learning: Literal["imap", "smtp", "pop3", "http", "ftp", "nntp", "imaps", "smtps", "pop3s", "https", "ftps", "mapi", "cifs", "ssh"] | list[str] | list[dict[str, Any]] | None = ...,
        lowspace: Literal["drop-new", "ovrw-old"] | None = ...,
        destination: Literal["NULL", "disk", "FortiAnalyzer"] | None = ...,
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
        payload_dict: QuarantinePayload | None = ...,
        agelimit: int | None = ...,
        maxfilesize: int | None = ...,
        quarantine_quota: int | None = ...,
        drop_infected: Literal["imap", "smtp", "pop3", "http", "ftp", "nntp", "imaps", "smtps", "pop3s", "https", "ftps", "mapi", "cifs", "ssh"] | list[str] | list[dict[str, Any]] | None = ...,
        store_infected: Literal["imap", "smtp", "pop3", "http", "ftp", "nntp", "imaps", "smtps", "pop3s", "https", "ftps", "mapi", "cifs", "ssh"] | list[str] | list[dict[str, Any]] | None = ...,
        drop_machine_learning: Literal["imap", "smtp", "pop3", "http", "ftp", "nntp", "imaps", "smtps", "pop3s", "https", "ftps", "mapi", "cifs", "ssh"] | list[str] | list[dict[str, Any]] | None = ...,
        store_machine_learning: Literal["imap", "smtp", "pop3", "http", "ftp", "nntp", "imaps", "smtps", "pop3s", "https", "ftps", "mapi", "cifs", "ssh"] | list[str] | list[dict[str, Any]] | None = ...,
        lowspace: Literal["drop-new", "ovrw-old"] | None = ...,
        destination: Literal["NULL", "disk", "FortiAnalyzer"] | None = ...,
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
    "Quarantine",
    "QuarantinePayload",
    "QuarantineObject",
]