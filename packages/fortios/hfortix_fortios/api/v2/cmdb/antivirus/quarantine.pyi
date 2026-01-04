from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class QuarantinePayload(TypedDict, total=False):
    """
    Type hints for antivirus/quarantine payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
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


class Quarantine:
    """
    Configure quarantine options.
    
    Path: antivirus/quarantine
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
        payload_dict: QuarantinePayload | None = ...,
        agelimit: int | None = ...,
        maxfilesize: int | None = ...,
        quarantine_quota: int | None = ...,
        drop_infected: Literal["imap", "smtp", "pop3", "http", "ftp", "nntp", "imaps", "smtps", "pop3s", "https", "ftps", "mapi", "cifs", "ssh"] | None = ...,
        store_infected: Literal["imap", "smtp", "pop3", "http", "ftp", "nntp", "imaps", "smtps", "pop3s", "https", "ftps", "mapi", "cifs", "ssh"] | None = ...,
        drop_machine_learning: Literal["imap", "smtp", "pop3", "http", "ftp", "nntp", "imaps", "smtps", "pop3s", "https", "ftps", "mapi", "cifs", "ssh"] | None = ...,
        store_machine_learning: Literal["imap", "smtp", "pop3", "http", "ftp", "nntp", "imaps", "smtps", "pop3s", "https", "ftps", "mapi", "cifs", "ssh"] | None = ...,
        lowspace: Literal["drop-new", "ovrw-old"] | None = ...,
        destination: Literal["NULL", "disk", "FortiAnalyzer"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: QuarantinePayload | None = ...,
        agelimit: int | None = ...,
        maxfilesize: int | None = ...,
        quarantine_quota: int | None = ...,
        drop_infected: Literal["imap", "smtp", "pop3", "http", "ftp", "nntp", "imaps", "smtps", "pop3s", "https", "ftps", "mapi", "cifs", "ssh"] | None = ...,
        store_infected: Literal["imap", "smtp", "pop3", "http", "ftp", "nntp", "imaps", "smtps", "pop3s", "https", "ftps", "mapi", "cifs", "ssh"] | None = ...,
        drop_machine_learning: Literal["imap", "smtp", "pop3", "http", "ftp", "nntp", "imaps", "smtps", "pop3s", "https", "ftps", "mapi", "cifs", "ssh"] | None = ...,
        store_machine_learning: Literal["imap", "smtp", "pop3", "http", "ftp", "nntp", "imaps", "smtps", "pop3s", "https", "ftps", "mapi", "cifs", "ssh"] | None = ...,
        lowspace: Literal["drop-new", "ovrw-old"] | None = ...,
        destination: Literal["NULL", "disk", "FortiAnalyzer"] | None = ...,
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
        payload_dict: QuarantinePayload | None = ...,
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