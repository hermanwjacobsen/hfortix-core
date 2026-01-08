from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class AutomationActionPayload(TypedDict, total=False):
    """
    Type hints for system/automation_action payload fields.
    
    Action for automation stitches.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.certificate.local.LocalEndpoint` (via: tls-certificate)
        - :class:`~.system.accprofile.AccprofileEndpoint` (via: accprofile)
        - :class:`~.system.replacemsg-group.ReplacemsgGroupEndpoint` (via: replacemsg-group)

    **Usage:**
        payload: AutomationActionPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Name.
    description: NotRequired[str]  # Description.
    action_type: NotRequired[Literal["email", "fortiexplorer-notification", "alert", "disable-ssid", "system-actions", "quarantine", "quarantine-forticlient", "quarantine-nsx", "quarantine-fortinac", "ban-ip", "aws-lambda", "azure-function", "google-cloud-function", "alicloud-function", "webhook", "cli-script", "diagnose-script", "regular-expression", "slack-notification", "microsoft-teams-notification"]]  # Action type.
    system_action: Literal["reboot", "shutdown", "backup-config"]  # System action type.
    tls_certificate: NotRequired[str]  # Custom TLS certificate for API request.
    forticare_email: Literal["enable", "disable"]  # Enable/disable use of your FortiCare email address as the em
    email_to: NotRequired[list[dict[str, Any]]]  # Email addresses.
    email_from: NotRequired[str]  # Email sender name.
    email_subject: NotRequired[str]  # Email subject.
    minimum_interval: NotRequired[int]  # Limit execution to no more than once in this interval
    aws_api_key: str  # AWS API Gateway API key.
    azure_function_authorization: Literal["anonymous", "function", "admin"]  # Azure function authorization level.
    azure_api_key: NotRequired[str]  # Azure function API key.
    alicloud_function_authorization: Literal["anonymous", "function"]  # AliCloud function authorization type.
    alicloud_access_key_id: str  # AliCloud AccessKey ID.
    alicloud_access_key_secret: str  # AliCloud AccessKey secret.
    message_type: Literal["text", "json", "form-data"]  # Message type.
    message: str  # Message content.
    replacement_message: Literal["enable", "disable"]  # Enable/disable replacement message.
    replacemsg_group: NotRequired[str]  # Replacement message group.
    protocol: Literal["http", "https"]  # Request protocol.
    method: Literal["post", "put", "get", "patch", "delete"]  # Request method (POST, PUT, GET, PATCH or DELETE).
    uri: str  # Request API URI.
    http_body: NotRequired[str]  # Request body (if necessary). Should be serialized json strin
    port: NotRequired[int]  # Protocol port.
    http_headers: NotRequired[list[dict[str, Any]]]  # Request headers.
    form_data: NotRequired[list[dict[str, Any]]]  # Form data parts for content type multipart/form-data.
    verify_host_cert: NotRequired[Literal["enable", "disable"]]  # Enable/disable verification of the remote host certificate.
    script: str  # CLI script.
    output_size: NotRequired[int]  # Number of megabytes to limit script output to
    timeout: NotRequired[int]  # Maximum running time for this script in seconds
    duration: NotRequired[int]  # Maximum running time for this script in seconds.
    output_interval: NotRequired[int]  # Collect the outputs for each output-interval in seconds
    file_only: NotRequired[Literal["enable", "disable"]]  # Enable/disable the output in files only.
    execute_security_fabric: NotRequired[Literal["enable", "disable"]]  # Enable/disable execution of CLI script on all or only one Fo
    accprofile: NotRequired[str]  # Access profile for CLI script action to access FortiGate fea
    regular_expression: str  # Regular expression string.
    log_debug_print: NotRequired[Literal["enable", "disable"]]  # Enable/disable logging debug print output from diagnose acti
    security_tag: str  # NSX security tag.
    sdn_connector: NotRequired[list[dict[str, Any]]]  # NSX SDN connector names.

# Nested classes for table field children

@final
class AutomationActionEmailtoObject:
    """Typed object for email-to table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Email address.
    name: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class AutomationActionHttpheadersObject:
    """Typed object for http-headers table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Entry ID.
    id: int
    # Request header key.
    key: str
    # Request header value.
    value: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class AutomationActionFormdataObject:
    """Typed object for form-data table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Entry ID.
    id: int
    # Key of the part of Multipart/form-data.
    key: str
    # Value of the part of Multipart/form-data.
    value: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class AutomationActionSdnconnectorObject:
    """Typed object for sdn-connector table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # SDN connector name.
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
class AutomationActionResponse(TypedDict):
    """
    Type hints for system/automation_action API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str
    description: str
    action_type: Literal["email", "fortiexplorer-notification", "alert", "disable-ssid", "system-actions", "quarantine", "quarantine-forticlient", "quarantine-nsx", "quarantine-fortinac", "ban-ip", "aws-lambda", "azure-function", "google-cloud-function", "alicloud-function", "webhook", "cli-script", "diagnose-script", "regular-expression", "slack-notification", "microsoft-teams-notification"]
    system_action: Literal["reboot", "shutdown", "backup-config"]
    tls_certificate: str
    forticare_email: Literal["enable", "disable"]
    email_to: list[dict[str, Any]]
    email_from: str
    email_subject: str
    minimum_interval: int
    aws_api_key: str
    azure_function_authorization: Literal["anonymous", "function", "admin"]
    azure_api_key: str
    alicloud_function_authorization: Literal["anonymous", "function"]
    alicloud_access_key_id: str
    alicloud_access_key_secret: str
    message_type: Literal["text", "json", "form-data"]
    message: str
    replacement_message: Literal["enable", "disable"]
    replacemsg_group: str
    protocol: Literal["http", "https"]
    method: Literal["post", "put", "get", "patch", "delete"]
    uri: str
    http_body: str
    port: int
    http_headers: list[dict[str, Any]]
    form_data: list[dict[str, Any]]
    verify_host_cert: Literal["enable", "disable"]
    script: str
    output_size: int
    timeout: int
    duration: int
    output_interval: int
    file_only: Literal["enable", "disable"]
    execute_security_fabric: Literal["enable", "disable"]
    accprofile: str
    regular_expression: str
    log_debug_print: Literal["enable", "disable"]
    security_tag: str
    sdn_connector: list[dict[str, Any]]


@final
class AutomationActionObject:
    """Typed FortiObject for system/automation_action with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Name.
    name: str
    # Description.
    description: str
    # Action type.
    action_type: Literal["email", "fortiexplorer-notification", "alert", "disable-ssid", "system-actions", "quarantine", "quarantine-forticlient", "quarantine-nsx", "quarantine-fortinac", "ban-ip", "aws-lambda", "azure-function", "google-cloud-function", "alicloud-function", "webhook", "cli-script", "diagnose-script", "regular-expression", "slack-notification", "microsoft-teams-notification"]
    # System action type.
    system_action: Literal["reboot", "shutdown", "backup-config"]
    # Custom TLS certificate for API request.
    tls_certificate: str
    # Enable/disable use of your FortiCare email address as the email-to address.
    forticare_email: Literal["enable", "disable"]
    # Email addresses.
    email_to: list[AutomationActionEmailtoObject]  # Table field - list of typed objects
    # Email sender name.
    email_from: str
    # Email subject.
    email_subject: str
    # Limit execution to no more than once in this interval (in seconds).
    minimum_interval: int
    # AWS API Gateway API key.
    aws_api_key: str
    # Azure function authorization level.
    azure_function_authorization: Literal["anonymous", "function", "admin"]
    # Azure function API key.
    azure_api_key: str
    # AliCloud function authorization type.
    alicloud_function_authorization: Literal["anonymous", "function"]
    # AliCloud AccessKey ID.
    alicloud_access_key_id: str
    # AliCloud AccessKey secret.
    alicloud_access_key_secret: str
    # Message type.
    message_type: Literal["text", "json", "form-data"]
    # Message content.
    message: str
    # Enable/disable replacement message.
    replacement_message: Literal["enable", "disable"]
    # Replacement message group.
    replacemsg_group: str
    # Request protocol.
    protocol: Literal["http", "https"]
    # Request method (POST, PUT, GET, PATCH or DELETE).
    method: Literal["post", "put", "get", "patch", "delete"]
    # Request API URI.
    uri: str
    # Request body (if necessary). Should be serialized json string.
    http_body: str
    # Protocol port.
    port: int
    # Request headers.
    http_headers: list[AutomationActionHttpheadersObject]  # Table field - list of typed objects
    # Form data parts for content type multipart/form-data.
    form_data: list[AutomationActionFormdataObject]  # Table field - list of typed objects
    # Enable/disable verification of the remote host certificate.
    verify_host_cert: Literal["enable", "disable"]
    # CLI script.
    script: str
    # Number of megabytes to limit script output to (1 - 1024, default = 10).
    output_size: int
    # Maximum running time for this script in seconds (0 = no timeout).
    timeout: int
    # Maximum running time for this script in seconds.
    duration: int
    # Collect the outputs for each output-interval in seconds
    output_interval: int
    # Enable/disable the output in files only.
    file_only: Literal["enable", "disable"]
    # Enable/disable execution of CLI script on all or only one FortiGate unit in the
    execute_security_fabric: Literal["enable", "disable"]
    # Access profile for CLI script action to access FortiGate features.
    accprofile: str
    # Regular expression string.
    regular_expression: str
    # Enable/disable logging debug print output from diagnose action.
    log_debug_print: Literal["enable", "disable"]
    # NSX security tag.
    security_tag: str
    # NSX SDN connector names.
    sdn_connector: list[AutomationActionSdnconnectorObject]  # Table field - list of typed objects
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> AutomationActionPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class AutomationAction:
    """
    Action for automation stitches.
    
    Path: system/automation_action
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
    ) -> AutomationActionObject: ...
    
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
    ) -> AutomationActionObject: ...
    
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
    ) -> list[AutomationActionObject]: ...
    
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
    ) -> AutomationActionResponse: ...
    
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
    ) -> AutomationActionResponse: ...
    
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
    ) -> list[AutomationActionResponse]: ...
    
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
    ) -> AutomationActionObject | list[AutomationActionObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: AutomationActionPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        action_type: Literal["email", "fortiexplorer-notification", "alert", "disable-ssid", "system-actions", "quarantine", "quarantine-forticlient", "quarantine-nsx", "quarantine-fortinac", "ban-ip", "aws-lambda", "azure-function", "google-cloud-function", "alicloud-function", "webhook", "cli-script", "diagnose-script", "regular-expression", "slack-notification", "microsoft-teams-notification"] | None = ...,
        system_action: Literal["reboot", "shutdown", "backup-config"] | None = ...,
        tls_certificate: str | None = ...,
        forticare_email: Literal["enable", "disable"] | None = ...,
        email_to: str | list[str] | list[dict[str, Any]] | None = ...,
        email_from: str | None = ...,
        email_subject: str | None = ...,
        minimum_interval: int | None = ...,
        aws_api_key: str | None = ...,
        azure_function_authorization: Literal["anonymous", "function", "admin"] | None = ...,
        azure_api_key: str | None = ...,
        alicloud_function_authorization: Literal["anonymous", "function"] | None = ...,
        alicloud_access_key_id: str | None = ...,
        alicloud_access_key_secret: str | None = ...,
        message_type: Literal["text", "json", "form-data"] | None = ...,
        message: str | None = ...,
        replacement_message: Literal["enable", "disable"] | None = ...,
        replacemsg_group: str | None = ...,
        protocol: Literal["http", "https"] | None = ...,
        method: Literal["post", "put", "get", "patch", "delete"] | None = ...,
        uri: str | None = ...,
        http_body: str | None = ...,
        port: int | None = ...,
        http_headers: str | list[str] | list[dict[str, Any]] | None = ...,
        form_data: str | list[str] | list[dict[str, Any]] | None = ...,
        verify_host_cert: Literal["enable", "disable"] | None = ...,
        script: str | None = ...,
        output_size: int | None = ...,
        timeout: int | None = ...,
        duration: int | None = ...,
        output_interval: int | None = ...,
        file_only: Literal["enable", "disable"] | None = ...,
        execute_security_fabric: Literal["enable", "disable"] | None = ...,
        accprofile: str | None = ...,
        regular_expression: str | None = ...,
        log_debug_print: Literal["enable", "disable"] | None = ...,
        security_tag: str | None = ...,
        sdn_connector: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> AutomationActionObject: ...
    
    @overload
    def post(
        self,
        payload_dict: AutomationActionPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        action_type: Literal["email", "fortiexplorer-notification", "alert", "disable-ssid", "system-actions", "quarantine", "quarantine-forticlient", "quarantine-nsx", "quarantine-fortinac", "ban-ip", "aws-lambda", "azure-function", "google-cloud-function", "alicloud-function", "webhook", "cli-script", "diagnose-script", "regular-expression", "slack-notification", "microsoft-teams-notification"] | None = ...,
        system_action: Literal["reboot", "shutdown", "backup-config"] | None = ...,
        tls_certificate: str | None = ...,
        forticare_email: Literal["enable", "disable"] | None = ...,
        email_to: str | list[str] | list[dict[str, Any]] | None = ...,
        email_from: str | None = ...,
        email_subject: str | None = ...,
        minimum_interval: int | None = ...,
        aws_api_key: str | None = ...,
        azure_function_authorization: Literal["anonymous", "function", "admin"] | None = ...,
        azure_api_key: str | None = ...,
        alicloud_function_authorization: Literal["anonymous", "function"] | None = ...,
        alicloud_access_key_id: str | None = ...,
        alicloud_access_key_secret: str | None = ...,
        message_type: Literal["text", "json", "form-data"] | None = ...,
        message: str | None = ...,
        replacement_message: Literal["enable", "disable"] | None = ...,
        replacemsg_group: str | None = ...,
        protocol: Literal["http", "https"] | None = ...,
        method: Literal["post", "put", "get", "patch", "delete"] | None = ...,
        uri: str | None = ...,
        http_body: str | None = ...,
        port: int | None = ...,
        http_headers: str | list[str] | list[dict[str, Any]] | None = ...,
        form_data: str | list[str] | list[dict[str, Any]] | None = ...,
        verify_host_cert: Literal["enable", "disable"] | None = ...,
        script: str | None = ...,
        output_size: int | None = ...,
        timeout: int | None = ...,
        duration: int | None = ...,
        output_interval: int | None = ...,
        file_only: Literal["enable", "disable"] | None = ...,
        execute_security_fabric: Literal["enable", "disable"] | None = ...,
        accprofile: str | None = ...,
        regular_expression: str | None = ...,
        log_debug_print: Literal["enable", "disable"] | None = ...,
        security_tag: str | None = ...,
        sdn_connector: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: AutomationActionPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        action_type: Literal["email", "fortiexplorer-notification", "alert", "disable-ssid", "system-actions", "quarantine", "quarantine-forticlient", "quarantine-nsx", "quarantine-fortinac", "ban-ip", "aws-lambda", "azure-function", "google-cloud-function", "alicloud-function", "webhook", "cli-script", "diagnose-script", "regular-expression", "slack-notification", "microsoft-teams-notification"] | None = ...,
        system_action: Literal["reboot", "shutdown", "backup-config"] | None = ...,
        tls_certificate: str | None = ...,
        forticare_email: Literal["enable", "disable"] | None = ...,
        email_to: str | list[str] | list[dict[str, Any]] | None = ...,
        email_from: str | None = ...,
        email_subject: str | None = ...,
        minimum_interval: int | None = ...,
        aws_api_key: str | None = ...,
        azure_function_authorization: Literal["anonymous", "function", "admin"] | None = ...,
        azure_api_key: str | None = ...,
        alicloud_function_authorization: Literal["anonymous", "function"] | None = ...,
        alicloud_access_key_id: str | None = ...,
        alicloud_access_key_secret: str | None = ...,
        message_type: Literal["text", "json", "form-data"] | None = ...,
        message: str | None = ...,
        replacement_message: Literal["enable", "disable"] | None = ...,
        replacemsg_group: str | None = ...,
        protocol: Literal["http", "https"] | None = ...,
        method: Literal["post", "put", "get", "patch", "delete"] | None = ...,
        uri: str | None = ...,
        http_body: str | None = ...,
        port: int | None = ...,
        http_headers: str | list[str] | list[dict[str, Any]] | None = ...,
        form_data: str | list[str] | list[dict[str, Any]] | None = ...,
        verify_host_cert: Literal["enable", "disable"] | None = ...,
        script: str | None = ...,
        output_size: int | None = ...,
        timeout: int | None = ...,
        duration: int | None = ...,
        output_interval: int | None = ...,
        file_only: Literal["enable", "disable"] | None = ...,
        execute_security_fabric: Literal["enable", "disable"] | None = ...,
        accprofile: str | None = ...,
        regular_expression: str | None = ...,
        log_debug_print: Literal["enable", "disable"] | None = ...,
        security_tag: str | None = ...,
        sdn_connector: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: AutomationActionPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        action_type: Literal["email", "fortiexplorer-notification", "alert", "disable-ssid", "system-actions", "quarantine", "quarantine-forticlient", "quarantine-nsx", "quarantine-fortinac", "ban-ip", "aws-lambda", "azure-function", "google-cloud-function", "alicloud-function", "webhook", "cli-script", "diagnose-script", "regular-expression", "slack-notification", "microsoft-teams-notification"] | None = ...,
        system_action: Literal["reboot", "shutdown", "backup-config"] | None = ...,
        tls_certificate: str | None = ...,
        forticare_email: Literal["enable", "disable"] | None = ...,
        email_to: str | list[str] | list[dict[str, Any]] | None = ...,
        email_from: str | None = ...,
        email_subject: str | None = ...,
        minimum_interval: int | None = ...,
        aws_api_key: str | None = ...,
        azure_function_authorization: Literal["anonymous", "function", "admin"] | None = ...,
        azure_api_key: str | None = ...,
        alicloud_function_authorization: Literal["anonymous", "function"] | None = ...,
        alicloud_access_key_id: str | None = ...,
        alicloud_access_key_secret: str | None = ...,
        message_type: Literal["text", "json", "form-data"] | None = ...,
        message: str | None = ...,
        replacement_message: Literal["enable", "disable"] | None = ...,
        replacemsg_group: str | None = ...,
        protocol: Literal["http", "https"] | None = ...,
        method: Literal["post", "put", "get", "patch", "delete"] | None = ...,
        uri: str | None = ...,
        http_body: str | None = ...,
        port: int | None = ...,
        http_headers: str | list[str] | list[dict[str, Any]] | None = ...,
        form_data: str | list[str] | list[dict[str, Any]] | None = ...,
        verify_host_cert: Literal["enable", "disable"] | None = ...,
        script: str | None = ...,
        output_size: int | None = ...,
        timeout: int | None = ...,
        duration: int | None = ...,
        output_interval: int | None = ...,
        file_only: Literal["enable", "disable"] | None = ...,
        execute_security_fabric: Literal["enable", "disable"] | None = ...,
        accprofile: str | None = ...,
        regular_expression: str | None = ...,
        log_debug_print: Literal["enable", "disable"] | None = ...,
        security_tag: str | None = ...,
        sdn_connector: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: AutomationActionPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        action_type: Literal["email", "fortiexplorer-notification", "alert", "disable-ssid", "system-actions", "quarantine", "quarantine-forticlient", "quarantine-nsx", "quarantine-fortinac", "ban-ip", "aws-lambda", "azure-function", "google-cloud-function", "alicloud-function", "webhook", "cli-script", "diagnose-script", "regular-expression", "slack-notification", "microsoft-teams-notification"] | None = ...,
        system_action: Literal["reboot", "shutdown", "backup-config"] | None = ...,
        tls_certificate: str | None = ...,
        forticare_email: Literal["enable", "disable"] | None = ...,
        email_to: str | list[str] | list[dict[str, Any]] | None = ...,
        email_from: str | None = ...,
        email_subject: str | None = ...,
        minimum_interval: int | None = ...,
        aws_api_key: str | None = ...,
        azure_function_authorization: Literal["anonymous", "function", "admin"] | None = ...,
        azure_api_key: str | None = ...,
        alicloud_function_authorization: Literal["anonymous", "function"] | None = ...,
        alicloud_access_key_id: str | None = ...,
        alicloud_access_key_secret: str | None = ...,
        message_type: Literal["text", "json", "form-data"] | None = ...,
        message: str | None = ...,
        replacement_message: Literal["enable", "disable"] | None = ...,
        replacemsg_group: str | None = ...,
        protocol: Literal["http", "https"] | None = ...,
        method: Literal["post", "put", "get", "patch", "delete"] | None = ...,
        uri: str | None = ...,
        http_body: str | None = ...,
        port: int | None = ...,
        http_headers: str | list[str] | list[dict[str, Any]] | None = ...,
        form_data: str | list[str] | list[dict[str, Any]] | None = ...,
        verify_host_cert: Literal["enable", "disable"] | None = ...,
        script: str | None = ...,
        output_size: int | None = ...,
        timeout: int | None = ...,
        duration: int | None = ...,
        output_interval: int | None = ...,
        file_only: Literal["enable", "disable"] | None = ...,
        execute_security_fabric: Literal["enable", "disable"] | None = ...,
        accprofile: str | None = ...,
        regular_expression: str | None = ...,
        log_debug_print: Literal["enable", "disable"] | None = ...,
        security_tag: str | None = ...,
        sdn_connector: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> AutomationActionObject: ...
    
    @overload
    def put(
        self,
        payload_dict: AutomationActionPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        action_type: Literal["email", "fortiexplorer-notification", "alert", "disable-ssid", "system-actions", "quarantine", "quarantine-forticlient", "quarantine-nsx", "quarantine-fortinac", "ban-ip", "aws-lambda", "azure-function", "google-cloud-function", "alicloud-function", "webhook", "cli-script", "diagnose-script", "regular-expression", "slack-notification", "microsoft-teams-notification"] | None = ...,
        system_action: Literal["reboot", "shutdown", "backup-config"] | None = ...,
        tls_certificate: str | None = ...,
        forticare_email: Literal["enable", "disable"] | None = ...,
        email_to: str | list[str] | list[dict[str, Any]] | None = ...,
        email_from: str | None = ...,
        email_subject: str | None = ...,
        minimum_interval: int | None = ...,
        aws_api_key: str | None = ...,
        azure_function_authorization: Literal["anonymous", "function", "admin"] | None = ...,
        azure_api_key: str | None = ...,
        alicloud_function_authorization: Literal["anonymous", "function"] | None = ...,
        alicloud_access_key_id: str | None = ...,
        alicloud_access_key_secret: str | None = ...,
        message_type: Literal["text", "json", "form-data"] | None = ...,
        message: str | None = ...,
        replacement_message: Literal["enable", "disable"] | None = ...,
        replacemsg_group: str | None = ...,
        protocol: Literal["http", "https"] | None = ...,
        method: Literal["post", "put", "get", "patch", "delete"] | None = ...,
        uri: str | None = ...,
        http_body: str | None = ...,
        port: int | None = ...,
        http_headers: str | list[str] | list[dict[str, Any]] | None = ...,
        form_data: str | list[str] | list[dict[str, Any]] | None = ...,
        verify_host_cert: Literal["enable", "disable"] | None = ...,
        script: str | None = ...,
        output_size: int | None = ...,
        timeout: int | None = ...,
        duration: int | None = ...,
        output_interval: int | None = ...,
        file_only: Literal["enable", "disable"] | None = ...,
        execute_security_fabric: Literal["enable", "disable"] | None = ...,
        accprofile: str | None = ...,
        regular_expression: str | None = ...,
        log_debug_print: Literal["enable", "disable"] | None = ...,
        security_tag: str | None = ...,
        sdn_connector: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: AutomationActionPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        action_type: Literal["email", "fortiexplorer-notification", "alert", "disable-ssid", "system-actions", "quarantine", "quarantine-forticlient", "quarantine-nsx", "quarantine-fortinac", "ban-ip", "aws-lambda", "azure-function", "google-cloud-function", "alicloud-function", "webhook", "cli-script", "diagnose-script", "regular-expression", "slack-notification", "microsoft-teams-notification"] | None = ...,
        system_action: Literal["reboot", "shutdown", "backup-config"] | None = ...,
        tls_certificate: str | None = ...,
        forticare_email: Literal["enable", "disable"] | None = ...,
        email_to: str | list[str] | list[dict[str, Any]] | None = ...,
        email_from: str | None = ...,
        email_subject: str | None = ...,
        minimum_interval: int | None = ...,
        aws_api_key: str | None = ...,
        azure_function_authorization: Literal["anonymous", "function", "admin"] | None = ...,
        azure_api_key: str | None = ...,
        alicloud_function_authorization: Literal["anonymous", "function"] | None = ...,
        alicloud_access_key_id: str | None = ...,
        alicloud_access_key_secret: str | None = ...,
        message_type: Literal["text", "json", "form-data"] | None = ...,
        message: str | None = ...,
        replacement_message: Literal["enable", "disable"] | None = ...,
        replacemsg_group: str | None = ...,
        protocol: Literal["http", "https"] | None = ...,
        method: Literal["post", "put", "get", "patch", "delete"] | None = ...,
        uri: str | None = ...,
        http_body: str | None = ...,
        port: int | None = ...,
        http_headers: str | list[str] | list[dict[str, Any]] | None = ...,
        form_data: str | list[str] | list[dict[str, Any]] | None = ...,
        verify_host_cert: Literal["enable", "disable"] | None = ...,
        script: str | None = ...,
        output_size: int | None = ...,
        timeout: int | None = ...,
        duration: int | None = ...,
        output_interval: int | None = ...,
        file_only: Literal["enable", "disable"] | None = ...,
        execute_security_fabric: Literal["enable", "disable"] | None = ...,
        accprofile: str | None = ...,
        regular_expression: str | None = ...,
        log_debug_print: Literal["enable", "disable"] | None = ...,
        security_tag: str | None = ...,
        sdn_connector: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: AutomationActionPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        action_type: Literal["email", "fortiexplorer-notification", "alert", "disable-ssid", "system-actions", "quarantine", "quarantine-forticlient", "quarantine-nsx", "quarantine-fortinac", "ban-ip", "aws-lambda", "azure-function", "google-cloud-function", "alicloud-function", "webhook", "cli-script", "diagnose-script", "regular-expression", "slack-notification", "microsoft-teams-notification"] | None = ...,
        system_action: Literal["reboot", "shutdown", "backup-config"] | None = ...,
        tls_certificate: str | None = ...,
        forticare_email: Literal["enable", "disable"] | None = ...,
        email_to: str | list[str] | list[dict[str, Any]] | None = ...,
        email_from: str | None = ...,
        email_subject: str | None = ...,
        minimum_interval: int | None = ...,
        aws_api_key: str | None = ...,
        azure_function_authorization: Literal["anonymous", "function", "admin"] | None = ...,
        azure_api_key: str | None = ...,
        alicloud_function_authorization: Literal["anonymous", "function"] | None = ...,
        alicloud_access_key_id: str | None = ...,
        alicloud_access_key_secret: str | None = ...,
        message_type: Literal["text", "json", "form-data"] | None = ...,
        message: str | None = ...,
        replacement_message: Literal["enable", "disable"] | None = ...,
        replacemsg_group: str | None = ...,
        protocol: Literal["http", "https"] | None = ...,
        method: Literal["post", "put", "get", "patch", "delete"] | None = ...,
        uri: str | None = ...,
        http_body: str | None = ...,
        port: int | None = ...,
        http_headers: str | list[str] | list[dict[str, Any]] | None = ...,
        form_data: str | list[str] | list[dict[str, Any]] | None = ...,
        verify_host_cert: Literal["enable", "disable"] | None = ...,
        script: str | None = ...,
        output_size: int | None = ...,
        timeout: int | None = ...,
        duration: int | None = ...,
        output_interval: int | None = ...,
        file_only: Literal["enable", "disable"] | None = ...,
        execute_security_fabric: Literal["enable", "disable"] | None = ...,
        accprofile: str | None = ...,
        regular_expression: str | None = ...,
        log_debug_print: Literal["enable", "disable"] | None = ...,
        security_tag: str | None = ...,
        sdn_connector: str | list[str] | list[dict[str, Any]] | None = ...,
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
    ) -> AutomationActionObject: ...
    
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
        payload_dict: AutomationActionPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        action_type: Literal["email", "fortiexplorer-notification", "alert", "disable-ssid", "system-actions", "quarantine", "quarantine-forticlient", "quarantine-nsx", "quarantine-fortinac", "ban-ip", "aws-lambda", "azure-function", "google-cloud-function", "alicloud-function", "webhook", "cli-script", "diagnose-script", "regular-expression", "slack-notification", "microsoft-teams-notification"] | None = ...,
        system_action: Literal["reboot", "shutdown", "backup-config"] | None = ...,
        tls_certificate: str | None = ...,
        forticare_email: Literal["enable", "disable"] | None = ...,
        email_to: str | list[str] | list[dict[str, Any]] | None = ...,
        email_from: str | None = ...,
        email_subject: str | None = ...,
        minimum_interval: int | None = ...,
        aws_api_key: str | None = ...,
        azure_function_authorization: Literal["anonymous", "function", "admin"] | None = ...,
        azure_api_key: str | None = ...,
        alicloud_function_authorization: Literal["anonymous", "function"] | None = ...,
        alicloud_access_key_id: str | None = ...,
        alicloud_access_key_secret: str | None = ...,
        message_type: Literal["text", "json", "form-data"] | None = ...,
        message: str | None = ...,
        replacement_message: Literal["enable", "disable"] | None = ...,
        replacemsg_group: str | None = ...,
        protocol: Literal["http", "https"] | None = ...,
        method: Literal["post", "put", "get", "patch", "delete"] | None = ...,
        uri: str | None = ...,
        http_body: str | None = ...,
        port: int | None = ...,
        http_headers: str | list[str] | list[dict[str, Any]] | None = ...,
        form_data: str | list[str] | list[dict[str, Any]] | None = ...,
        verify_host_cert: Literal["enable", "disable"] | None = ...,
        script: str | None = ...,
        output_size: int | None = ...,
        timeout: int | None = ...,
        duration: int | None = ...,
        output_interval: int | None = ...,
        file_only: Literal["enable", "disable"] | None = ...,
        execute_security_fabric: Literal["enable", "disable"] | None = ...,
        accprofile: str | None = ...,
        regular_expression: str | None = ...,
        log_debug_print: Literal["enable", "disable"] | None = ...,
        security_tag: str | None = ...,
        sdn_connector: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "AutomationAction",
    "AutomationActionPayload",
    "AutomationActionObject",
]