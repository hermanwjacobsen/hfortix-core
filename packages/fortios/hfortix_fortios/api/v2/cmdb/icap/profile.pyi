from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class ProfilePayload(TypedDict, total=False):
    """
    Type hints for icap/profile payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: ProfilePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    replacemsg_group: NotRequired[str]  # Replacement message group.
    name: NotRequired[str]  # ICAP profile name.
    comment: NotRequired[str]  # Comment.
    request: NotRequired[Literal["disable", "enable"]]  # Enable/disable whether an HTTP request is passed to an ICAP 
    response: NotRequired[Literal["disable", "enable"]]  # Enable/disable whether an HTTP response is passed to an ICAP
    file_transfer: NotRequired[Literal["ssh", "ftp"]]  # Configure the file transfer protocols to pass transferred fi
    streaming_content_bypass: NotRequired[Literal["disable", "enable"]]  # Enable/disable bypassing of ICAP server for streaming conten
    ocr_only: NotRequired[Literal["disable", "enable"]]  # Enable/disable this FortiGate unit to submit only OCR intere
    204_size_limit: NotRequired[int]  # 204 response size limit to be saved by ICAP client in megaby
    204_response: NotRequired[Literal["disable", "enable"]]  # Enable/disable allowance of 204 response from ICAP server.
    preview: NotRequired[Literal["disable", "enable"]]  # Enable/disable preview of data to ICAP server.
    preview_data_length: NotRequired[int]  # Preview data length to be sent to ICAP server.
    request_server: str  # ICAP server to use for an HTTP request.
    response_server: str  # ICAP server to use for an HTTP response.
    file_transfer_server: str  # ICAP server to use for a file transfer.
    request_failure: NotRequired[Literal["error", "bypass"]]  # Action to take if the ICAP server cannot be contacted when p
    response_failure: NotRequired[Literal["error", "bypass"]]  # Action to take if the ICAP server cannot be contacted when p
    file_transfer_failure: NotRequired[Literal["error", "bypass"]]  # Action to take if the ICAP server cannot be contacted when p
    request_path: NotRequired[str]  # Path component of the ICAP URI that identifies the HTTP requ
    response_path: NotRequired[str]  # Path component of the ICAP URI that identifies the HTTP resp
    file_transfer_path: NotRequired[str]  # Path component of the ICAP URI that identifies the file tran
    methods: NotRequired[Literal["delete", "get", "head", "options", "post", "put", "trace", "connect", "other"]]  # The allowed HTTP methods that will be sent to ICAP server fo
    response_req_hdr: NotRequired[Literal["disable", "enable"]]  # Enable/disable addition of req-hdr for ICAP response modific
    respmod_default_action: NotRequired[Literal["forward", "bypass"]]  # Default action to ICAP response modification (respmod) proce
    icap_block_log: NotRequired[Literal["disable", "enable"]]  # Enable/disable UTM log when infection found (default = disab
    chunk_encap: NotRequired[Literal["disable", "enable"]]  # Enable/disable chunked encapsulation (default = disable).
    extension_feature: NotRequired[Literal["scan-progress"]]  # Enable/disable ICAP extension features.
    scan_progress_interval: NotRequired[int]  # Scan progress interval value.
    timeout: NotRequired[int]  # Time (in seconds) that ICAP client waits for the response fr
    icap_headers: NotRequired[list[dict[str, Any]]]  # Configure ICAP forwarded request headers.
    respmod_forward_rules: NotRequired[list[dict[str, Any]]]  # ICAP response mode forward rules.


class Profile:
    """
    Configure ICAP profiles.
    
    Path: icap/profile
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
        replacemsg_group: str | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        request: Literal["disable", "enable"] | None = ...,
        response: Literal["disable", "enable"] | None = ...,
        file_transfer: Literal["ssh", "ftp"] | None = ...,
        streaming_content_bypass: Literal["disable", "enable"] | None = ...,
        ocr_only: Literal["disable", "enable"] | None = ...,
        204_size_limit: int | None = ...,
        204_response: Literal["disable", "enable"] | None = ...,
        preview: Literal["disable", "enable"] | None = ...,
        preview_data_length: int | None = ...,
        request_server: str | None = ...,
        response_server: str | None = ...,
        file_transfer_server: str | None = ...,
        request_failure: Literal["error", "bypass"] | None = ...,
        response_failure: Literal["error", "bypass"] | None = ...,
        file_transfer_failure: Literal["error", "bypass"] | None = ...,
        request_path: str | None = ...,
        response_path: str | None = ...,
        file_transfer_path: str | None = ...,
        methods: Literal["delete", "get", "head", "options", "post", "put", "trace", "connect", "other"] | None = ...,
        response_req_hdr: Literal["disable", "enable"] | None = ...,
        respmod_default_action: Literal["forward", "bypass"] | None = ...,
        icap_block_log: Literal["disable", "enable"] | None = ...,
        chunk_encap: Literal["disable", "enable"] | None = ...,
        extension_feature: Literal["scan-progress"] | None = ...,
        scan_progress_interval: int | None = ...,
        timeout: int | None = ...,
        icap_headers: list[dict[str, Any]] | None = ...,
        respmod_forward_rules: list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: ProfilePayload | None = ...,
        replacemsg_group: str | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        request: Literal["disable", "enable"] | None = ...,
        response: Literal["disable", "enable"] | None = ...,
        file_transfer: Literal["ssh", "ftp"] | None = ...,
        streaming_content_bypass: Literal["disable", "enable"] | None = ...,
        ocr_only: Literal["disable", "enable"] | None = ...,
        204_size_limit: int | None = ...,
        204_response: Literal["disable", "enable"] | None = ...,
        preview: Literal["disable", "enable"] | None = ...,
        preview_data_length: int | None = ...,
        request_server: str | None = ...,
        response_server: str | None = ...,
        file_transfer_server: str | None = ...,
        request_failure: Literal["error", "bypass"] | None = ...,
        response_failure: Literal["error", "bypass"] | None = ...,
        file_transfer_failure: Literal["error", "bypass"] | None = ...,
        request_path: str | None = ...,
        response_path: str | None = ...,
        file_transfer_path: str | None = ...,
        methods: Literal["delete", "get", "head", "options", "post", "put", "trace", "connect", "other"] | None = ...,
        response_req_hdr: Literal["disable", "enable"] | None = ...,
        respmod_default_action: Literal["forward", "bypass"] | None = ...,
        icap_block_log: Literal["disable", "enable"] | None = ...,
        chunk_encap: Literal["disable", "enable"] | None = ...,
        extension_feature: Literal["scan-progress"] | None = ...,
        scan_progress_interval: int | None = ...,
        timeout: int | None = ...,
        icap_headers: list[dict[str, Any]] | None = ...,
        respmod_forward_rules: list[dict[str, Any]] | None = ...,
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