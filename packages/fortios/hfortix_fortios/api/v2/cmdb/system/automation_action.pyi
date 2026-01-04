from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class AutomationActionPayload(TypedDict, total=False):
    """
    Type hints for system/automation_action payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
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
    minimum_interval: NotRequired[int]  # Limit execution to no more than once in this interval (in se
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
    output_size: NotRequired[int]  # Number of megabytes to limit script output to (1 - 1024, def
    timeout: NotRequired[int]  # Maximum running time for this script in seconds (0 = no time
    duration: NotRequired[int]  # Maximum running time for this script in seconds.
    output_interval: NotRequired[int]  # Collect the outputs for each output-interval in seconds (0 =
    file_only: NotRequired[Literal["enable", "disable"]]  # Enable/disable the output in files only.
    execute_security_fabric: NotRequired[Literal["enable", "disable"]]  # Enable/disable execution of CLI script on all or only one Fo
    accprofile: NotRequired[str]  # Access profile for CLI script action to access FortiGate fea
    regular_expression: str  # Regular expression string.
    log_debug_print: NotRequired[Literal["enable", "disable"]]  # Enable/disable logging debug print output from diagnose acti
    security_tag: str  # NSX security tag.
    sdn_connector: NotRequired[list[dict[str, Any]]]  # NSX SDN connector names.


class AutomationAction:
    """
    Action for automation stitches.
    
    Path: system/automation_action
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
        payload_dict: AutomationActionPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        action_type: Literal["email", "fortiexplorer-notification", "alert", "disable-ssid", "system-actions", "quarantine", "quarantine-forticlient", "quarantine-nsx", "quarantine-fortinac", "ban-ip", "aws-lambda", "azure-function", "google-cloud-function", "alicloud-function", "webhook", "cli-script", "diagnose-script", "regular-expression", "slack-notification", "microsoft-teams-notification"] | None = ...,
        system_action: Literal["reboot", "shutdown", "backup-config"] | None = ...,
        tls_certificate: str | None = ...,
        forticare_email: Literal["enable", "disable"] | None = ...,
        email_to: list[dict[str, Any]] | None = ...,
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
        http_headers: list[dict[str, Any]] | None = ...,
        form_data: list[dict[str, Any]] | None = ...,
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
        sdn_connector: list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: AutomationActionPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        action_type: Literal["email", "fortiexplorer-notification", "alert", "disable-ssid", "system-actions", "quarantine", "quarantine-forticlient", "quarantine-nsx", "quarantine-fortinac", "ban-ip", "aws-lambda", "azure-function", "google-cloud-function", "alicloud-function", "webhook", "cli-script", "diagnose-script", "regular-expression", "slack-notification", "microsoft-teams-notification"] | None = ...,
        system_action: Literal["reboot", "shutdown", "backup-config"] | None = ...,
        tls_certificate: str | None = ...,
        forticare_email: Literal["enable", "disable"] | None = ...,
        email_to: list[dict[str, Any]] | None = ...,
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
        http_headers: list[dict[str, Any]] | None = ...,
        form_data: list[dict[str, Any]] | None = ...,
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
        sdn_connector: list[dict[str, Any]] | None = ...,
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
        payload_dict: AutomationActionPayload | None = ...,
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
    "AutomationAction",
    "AutomationActionPayload",
]