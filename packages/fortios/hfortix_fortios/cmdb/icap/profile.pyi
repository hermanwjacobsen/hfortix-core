from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class ProfilePayload(TypedDict, total=False):
    """
    Type hints for icap/profile payload fields.
    
    Configure ICAP profiles.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.icap.server.ServerEndpoint` (via: file-transfer-server, request-server, response-server)
        - :class:`~.icap.server-group.ServerGroupEndpoint` (via: file-transfer-server, request-server, response-server)
        - :class:`~.system.replacemsg-group.ReplacemsgGroupEndpoint` (via: replacemsg-group)

    **Usage:**
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
    size_limit_204: NotRequired[int]  # 204 response size limit to be saved by ICAP client in megaby
    response_204: NotRequired[Literal["disable", "enable"]]  # Enable/disable allowance of 204 response from ICAP server.
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


class ProfileObject(FortiObject[ProfilePayload]):
    """Typed FortiObject for icap/profile with IDE autocomplete support."""
    
    # Replacement message group.
    replacemsg_group: str
    # ICAP profile name.
    name: str
    # Comment.
    comment: str
    # Enable/disable whether an HTTP request is passed to an ICAP server.
    request: Literal["disable", "enable"]
    # Enable/disable whether an HTTP response is passed to an ICAP server.
    response: Literal["disable", "enable"]
    # Configure the file transfer protocols to pass transferred files to an ICAP serve
    file_transfer: Literal["ssh", "ftp"]
    # Enable/disable bypassing of ICAP server for streaming content.
    streaming_content_bypass: Literal["disable", "enable"]
    # Enable/disable this FortiGate unit to submit only OCR interested content to the 
    ocr_only: Literal["disable", "enable"]
    # 204 response size limit to be saved by ICAP client in megabytes (1 - 10, default
    size_limit_204: int
    # Enable/disable allowance of 204 response from ICAP server.
    response_204: Literal["disable", "enable"]
    # Enable/disable preview of data to ICAP server.
    preview: Literal["disable", "enable"]
    # Preview data length to be sent to ICAP server.
    preview_data_length: int
    # ICAP server to use for an HTTP request.
    request_server: str
    # ICAP server to use for an HTTP response.
    response_server: str
    # ICAP server to use for a file transfer.
    file_transfer_server: str
    # Action to take if the ICAP server cannot be contacted when processing an HTTP re
    request_failure: Literal["error", "bypass"]
    # Action to take if the ICAP server cannot be contacted when processing an HTTP re
    response_failure: Literal["error", "bypass"]
    # Action to take if the ICAP server cannot be contacted when processing a file tra
    file_transfer_failure: Literal["error", "bypass"]
    # Path component of the ICAP URI that identifies the HTTP request processing servi
    request_path: str
    # Path component of the ICAP URI that identifies the HTTP response processing serv
    response_path: str
    # Path component of the ICAP URI that identifies the file transfer processing serv
    file_transfer_path: str
    # The allowed HTTP methods that will be sent to ICAP server for further processing
    methods: Literal["delete", "get", "head", "options", "post", "put", "trace", "connect", "other"]
    # Enable/disable addition of req-hdr for ICAP response modification (respmod) proc
    response_req_hdr: Literal["disable", "enable"]
    # Default action to ICAP response modification (respmod) processing.
    respmod_default_action: Literal["forward", "bypass"]
    # Enable/disable UTM log when infection found (default = disable).
    icap_block_log: Literal["disable", "enable"]
    # Enable/disable chunked encapsulation (default = disable).
    chunk_encap: Literal["disable", "enable"]
    # Enable/disable ICAP extension features.
    extension_feature: Literal["scan-progress"]
    # Scan progress interval value.
    scan_progress_interval: int
    # Time (in seconds) that ICAP client waits for the response from ICAP server.
    timeout: int
    # Configure ICAP forwarded request headers.
    icap_headers: list[str]  # Auto-flattened from member_table
    # ICAP response mode forward rules.
    respmod_forward_rules: list[str]  # Auto-flattened from member_table
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> ProfilePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Profile:
    """
    Configure ICAP profiles.
    
    Path: icap/profile
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
        replacemsg_group: str | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        request: Literal["disable", "enable"] | None = ...,
        response: Literal["disable", "enable"] | None = ...,
        file_transfer: Literal["ssh", "ftp"] | list[str] | list[dict[str, Any]] | None = ...,
        streaming_content_bypass: Literal["disable", "enable"] | None = ...,
        ocr_only: Literal["disable", "enable"] | None = ...,
        size_limit_204: int | None = ...,
        response_204: Literal["disable", "enable"] | None = ...,
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
        methods: Literal["delete", "get", "head", "options", "post", "put", "trace", "connect", "other"] | list[str] | list[dict[str, Any]] | None = ...,
        response_req_hdr: Literal["disable", "enable"] | None = ...,
        respmod_default_action: Literal["forward", "bypass"] | None = ...,
        icap_block_log: Literal["disable", "enable"] | None = ...,
        chunk_encap: Literal["disable", "enable"] | None = ...,
        extension_feature: Literal["scan-progress"] | list[str] | list[dict[str, Any]] | None = ...,
        scan_progress_interval: int | None = ...,
        timeout: int | None = ...,
        icap_headers: str | list[str] | list[dict[str, Any]] | None = ...,
        respmod_forward_rules: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ProfileObject: ...
    
    @overload
    def post(
        self,
        payload_dict: ProfilePayload | None = ...,
        replacemsg_group: str | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        request: Literal["disable", "enable"] | None = ...,
        response: Literal["disable", "enable"] | None = ...,
        file_transfer: Literal["ssh", "ftp"] | list[str] | list[dict[str, Any]] | None = ...,
        streaming_content_bypass: Literal["disable", "enable"] | None = ...,
        ocr_only: Literal["disable", "enable"] | None = ...,
        size_limit_204: int | None = ...,
        response_204: Literal["disable", "enable"] | None = ...,
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
        methods: Literal["delete", "get", "head", "options", "post", "put", "trace", "connect", "other"] | list[str] | list[dict[str, Any]] | None = ...,
        response_req_hdr: Literal["disable", "enable"] | None = ...,
        respmod_default_action: Literal["forward", "bypass"] | None = ...,
        icap_block_log: Literal["disable", "enable"] | None = ...,
        chunk_encap: Literal["disable", "enable"] | None = ...,
        extension_feature: Literal["scan-progress"] | list[str] | list[dict[str, Any]] | None = ...,
        scan_progress_interval: int | None = ...,
        timeout: int | None = ...,
        icap_headers: str | list[str] | list[dict[str, Any]] | None = ...,
        respmod_forward_rules: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: ProfilePayload | None = ...,
        replacemsg_group: str | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        request: Literal["disable", "enable"] | None = ...,
        response: Literal["disable", "enable"] | None = ...,
        file_transfer: Literal["ssh", "ftp"] | list[str] | list[dict[str, Any]] | None = ...,
        streaming_content_bypass: Literal["disable", "enable"] | None = ...,
        ocr_only: Literal["disable", "enable"] | None = ...,
        size_limit_204: int | None = ...,
        response_204: Literal["disable", "enable"] | None = ...,
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
        methods: Literal["delete", "get", "head", "options", "post", "put", "trace", "connect", "other"] | list[str] | list[dict[str, Any]] | None = ...,
        response_req_hdr: Literal["disable", "enable"] | None = ...,
        respmod_default_action: Literal["forward", "bypass"] | None = ...,
        icap_block_log: Literal["disable", "enable"] | None = ...,
        chunk_encap: Literal["disable", "enable"] | None = ...,
        extension_feature: Literal["scan-progress"] | list[str] | list[dict[str, Any]] | None = ...,
        scan_progress_interval: int | None = ...,
        timeout: int | None = ...,
        icap_headers: str | list[str] | list[dict[str, Any]] | None = ...,
        respmod_forward_rules: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: ProfilePayload | None = ...,
        replacemsg_group: str | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        request: Literal["disable", "enable"] | None = ...,
        response: Literal["disable", "enable"] | None = ...,
        file_transfer: Literal["ssh", "ftp"] | list[str] | list[dict[str, Any]] | None = ...,
        streaming_content_bypass: Literal["disable", "enable"] | None = ...,
        ocr_only: Literal["disable", "enable"] | None = ...,
        size_limit_204: int | None = ...,
        response_204: Literal["disable", "enable"] | None = ...,
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
        methods: Literal["delete", "get", "head", "options", "post", "put", "trace", "connect", "other"] | list[str] | list[dict[str, Any]] | None = ...,
        response_req_hdr: Literal["disable", "enable"] | None = ...,
        respmod_default_action: Literal["forward", "bypass"] | None = ...,
        icap_block_log: Literal["disable", "enable"] | None = ...,
        chunk_encap: Literal["disable", "enable"] | None = ...,
        extension_feature: Literal["scan-progress"] | list[str] | list[dict[str, Any]] | None = ...,
        scan_progress_interval: int | None = ...,
        timeout: int | None = ...,
        icap_headers: str | list[str] | list[dict[str, Any]] | None = ...,
        respmod_forward_rules: str | list[str] | list[dict[str, Any]] | None = ...,
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
        replacemsg_group: str | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        request: Literal["disable", "enable"] | None = ...,
        response: Literal["disable", "enable"] | None = ...,
        file_transfer: Literal["ssh", "ftp"] | list[str] | list[dict[str, Any]] | None = ...,
        streaming_content_bypass: Literal["disable", "enable"] | None = ...,
        ocr_only: Literal["disable", "enable"] | None = ...,
        size_limit_204: int | None = ...,
        response_204: Literal["disable", "enable"] | None = ...,
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
        methods: Literal["delete", "get", "head", "options", "post", "put", "trace", "connect", "other"] | list[str] | list[dict[str, Any]] | None = ...,
        response_req_hdr: Literal["disable", "enable"] | None = ...,
        respmod_default_action: Literal["forward", "bypass"] | None = ...,
        icap_block_log: Literal["disable", "enable"] | None = ...,
        chunk_encap: Literal["disable", "enable"] | None = ...,
        extension_feature: Literal["scan-progress"] | list[str] | list[dict[str, Any]] | None = ...,
        scan_progress_interval: int | None = ...,
        timeout: int | None = ...,
        icap_headers: str | list[str] | list[dict[str, Any]] | None = ...,
        respmod_forward_rules: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ProfileObject: ...
    
    @overload
    def put(
        self,
        payload_dict: ProfilePayload | None = ...,
        replacemsg_group: str | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        request: Literal["disable", "enable"] | None = ...,
        response: Literal["disable", "enable"] | None = ...,
        file_transfer: Literal["ssh", "ftp"] | list[str] | list[dict[str, Any]] | None = ...,
        streaming_content_bypass: Literal["disable", "enable"] | None = ...,
        ocr_only: Literal["disable", "enable"] | None = ...,
        size_limit_204: int | None = ...,
        response_204: Literal["disable", "enable"] | None = ...,
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
        methods: Literal["delete", "get", "head", "options", "post", "put", "trace", "connect", "other"] | list[str] | list[dict[str, Any]] | None = ...,
        response_req_hdr: Literal["disable", "enable"] | None = ...,
        respmod_default_action: Literal["forward", "bypass"] | None = ...,
        icap_block_log: Literal["disable", "enable"] | None = ...,
        chunk_encap: Literal["disable", "enable"] | None = ...,
        extension_feature: Literal["scan-progress"] | list[str] | list[dict[str, Any]] | None = ...,
        scan_progress_interval: int | None = ...,
        timeout: int | None = ...,
        icap_headers: str | list[str] | list[dict[str, Any]] | None = ...,
        respmod_forward_rules: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: ProfilePayload | None = ...,
        replacemsg_group: str | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        request: Literal["disable", "enable"] | None = ...,
        response: Literal["disable", "enable"] | None = ...,
        file_transfer: Literal["ssh", "ftp"] | list[str] | list[dict[str, Any]] | None = ...,
        streaming_content_bypass: Literal["disable", "enable"] | None = ...,
        ocr_only: Literal["disable", "enable"] | None = ...,
        size_limit_204: int | None = ...,
        response_204: Literal["disable", "enable"] | None = ...,
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
        methods: Literal["delete", "get", "head", "options", "post", "put", "trace", "connect", "other"] | list[str] | list[dict[str, Any]] | None = ...,
        response_req_hdr: Literal["disable", "enable"] | None = ...,
        respmod_default_action: Literal["forward", "bypass"] | None = ...,
        icap_block_log: Literal["disable", "enable"] | None = ...,
        chunk_encap: Literal["disable", "enable"] | None = ...,
        extension_feature: Literal["scan-progress"] | list[str] | list[dict[str, Any]] | None = ...,
        scan_progress_interval: int | None = ...,
        timeout: int | None = ...,
        icap_headers: str | list[str] | list[dict[str, Any]] | None = ...,
        respmod_forward_rules: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: ProfilePayload | None = ...,
        replacemsg_group: str | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        request: Literal["disable", "enable"] | None = ...,
        response: Literal["disable", "enable"] | None = ...,
        file_transfer: Literal["ssh", "ftp"] | list[str] | list[dict[str, Any]] | None = ...,
        streaming_content_bypass: Literal["disable", "enable"] | None = ...,
        ocr_only: Literal["disable", "enable"] | None = ...,
        size_limit_204: int | None = ...,
        response_204: Literal["disable", "enable"] | None = ...,
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
        methods: Literal["delete", "get", "head", "options", "post", "put", "trace", "connect", "other"] | list[str] | list[dict[str, Any]] | None = ...,
        response_req_hdr: Literal["disable", "enable"] | None = ...,
        respmod_default_action: Literal["forward", "bypass"] | None = ...,
        icap_block_log: Literal["disable", "enable"] | None = ...,
        chunk_encap: Literal["disable", "enable"] | None = ...,
        extension_feature: Literal["scan-progress"] | list[str] | list[dict[str, Any]] | None = ...,
        scan_progress_interval: int | None = ...,
        timeout: int | None = ...,
        icap_headers: str | list[str] | list[dict[str, Any]] | None = ...,
        respmod_forward_rules: str | list[str] | list[dict[str, Any]] | None = ...,
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
        replacemsg_group: str | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        request: Literal["disable", "enable"] | None = ...,
        response: Literal["disable", "enable"] | None = ...,
        file_transfer: Literal["ssh", "ftp"] | list[str] | list[dict[str, Any]] | None = ...,
        streaming_content_bypass: Literal["disable", "enable"] | None = ...,
        ocr_only: Literal["disable", "enable"] | None = ...,
        size_limit_204: int | None = ...,
        response_204: Literal["disable", "enable"] | None = ...,
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
        methods: Literal["delete", "get", "head", "options", "post", "put", "trace", "connect", "other"] | list[str] | list[dict[str, Any]] | None = ...,
        response_req_hdr: Literal["disable", "enable"] | None = ...,
        respmod_default_action: Literal["forward", "bypass"] | None = ...,
        icap_block_log: Literal["disable", "enable"] | None = ...,
        chunk_encap: Literal["disable", "enable"] | None = ...,
        extension_feature: Literal["scan-progress"] | list[str] | list[dict[str, Any]] | None = ...,
        scan_progress_interval: int | None = ...,
        timeout: int | None = ...,
        icap_headers: str | list[str] | list[dict[str, Any]] | None = ...,
        respmod_forward_rules: str | list[str] | list[dict[str, Any]] | None = ...,
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