from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList




# Response TypedDict for GET returns (all fields present in API response)
class StatusResponse(TypedDict):
    """
    Type hints for license/status API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    antivirus: str
    appctrl: str
    genai_app: str
    forticare: str
    ips: str
    ot_detection: str
    iot_detection: str
    vm: str
    web_filtering: str
    security_rating: str
    mobile_malware: str
    ai_malware_detection: str
    industrial_db: str
    internet_service_db: str
    device_os_id: str
    botnet_domain: str
    data_leak_prevention: str
    psirt_security_rating: str
    fortitelemetry: str
    timezone_database: str
    geoip_db: str
    trusted_cert_db: str
    outbreak_security_rating: str
    icdb: str
    inline_casb: str
    local_in_virtual_patching: str
    malicious_urls: str
    blacklisted_certificates: str
    firmware_updates: str
    outbreak_prevention: str
    antispam: str
    sdwan_network_monitor: str
    forticloud: str
    forticloud_logging: str
    forticloud_sandbox: str
    fortianalyzer_cloud: str
    fortianalyzer_cloud_premium: str
    fortimanager_cloud: str
    fortisandbox_cloud: str
    fortiguard_ai_based_sandbox: str
    forticonverter: str
    sdwan_overlay_aas: str
    sovereign_sase: str
    fortiems_cloud: str
    fortimanager_cloud_alci: str
    fortisandbox_cloud_alci: str
    vdom: str
    sms: str
    load_balance_fpc: str


@final
class StatusObject:
    """Typed FortiObject for license/status with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # antivirus
    antivirus: str
    # appctrl
    appctrl: str
    # genai_app
    genai_app: str
    # forticare
    forticare: str
    # ips
    ips: str
    # ot_detection
    ot_detection: str
    # iot_detection
    iot_detection: str
    # vm
    vm: str
    # web_filtering
    web_filtering: str
    # security_rating
    security_rating: str
    # mobile_malware
    mobile_malware: str
    # ai_malware_detection
    ai_malware_detection: str
    # industrial_db
    industrial_db: str
    # internet_service_db
    internet_service_db: str
    # device_os_id
    device_os_id: str
    # botnet_domain
    botnet_domain: str
    # data_leak_prevention
    data_leak_prevention: str
    # psirt_security_rating
    psirt_security_rating: str
    # fortitelemetry
    fortitelemetry: str
    # timezone_database
    timezone_database: str
    # geoip_db
    geoip_db: str
    # trusted_cert_db
    trusted_cert_db: str
    # outbreak_security_rating
    outbreak_security_rating: str
    # icdb
    icdb: str
    # inline_casb
    inline_casb: str
    # local_in_virtual_patching
    local_in_virtual_patching: str
    # malicious_urls
    malicious_urls: str
    # blacklisted_certificates
    blacklisted_certificates: str
    # firmware_updates
    firmware_updates: str
    # outbreak_prevention
    outbreak_prevention: str
    # antispam
    antispam: str
    # sdwan_network_monitor
    sdwan_network_monitor: str
    # forticloud
    forticloud: str
    # forticloud_logging
    forticloud_logging: str
    # forticloud_sandbox
    forticloud_sandbox: str
    # fortianalyzer_cloud
    fortianalyzer_cloud: str
    # fortianalyzer_cloud_premium
    fortianalyzer_cloud_premium: str
    # fortimanager_cloud
    fortimanager_cloud: str
    # fortisandbox_cloud
    fortisandbox_cloud: str
    # fortiguard_ai_based_sandbox
    fortiguard_ai_based_sandbox: str
    # forticonverter
    forticonverter: str
    # sdwan_overlay_aas
    sdwan_overlay_aas: str
    # sovereign_sase
    sovereign_sase: str
    # fortiems_cloud
    fortiems_cloud: str
    # fortimanager_cloud_alci
    fortimanager_cloud_alci: str
    # fortisandbox_cloud_alci
    fortisandbox_cloud_alci: str
    # vdom
    vdom: str
    # sms
    sms: str
    # load_balance_fpc
    load_balance_fpc: str
    
    # Common API response fields
    status: str
    http_status: int | None
    http_status_code: int | None
    http_method: str | None
    http_response_time: float | None
    vdom: str | None
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> str:
        """Get pretty-printed JSON string."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> StatusPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Status:
    """
    Get current license & registration status.
    
    Path: license/status
    Category: monitor
    """
    
    # ================================================================
    # GET OVERLOADS - Always returns FortiObject
    # Pylance matches overloads top-to-bottom, so these must come first!
    # ================================================================
    
    # With mkey as positional arg -> returns FortiObject
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
    ) -> FortiObject: ...
    
    # With mkey as keyword arg -> returns FortiObject
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
    ) -> FortiObject: ...
    
    # Without mkey -> returns list of FortiObjects
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
    ) -> FortiObject: ...
    
    # ================================================================
    # (removed - all GET now returns FortiObject)
    # ================================================================
    
    # With mkey as positional arg -> returns single object
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
    ) -> FortiObject: ...
    
    # With mkey as keyword arg -> returns single object
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
    ) -> FortiObject: ...
    
    # With no mkey -> returns list of objects
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
    ) -> FortiObject: ...
    
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
    ) -> FortiObject: ...
    
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
    ) -> FortiObject: ...
    
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
    ) -> FortiObject: ...
    
    # Fallback overload for all other cases
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
    ) -> dict[str, Any] | FortiObject: ...
    
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
    ) -> FortiObject | dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: dict[str, Any] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    @overload
    def put(
        self,
        payload_dict: dict[str, Any] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: dict[str, Any] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: dict[str, Any] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: dict[str, Any] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Helper methods
    @staticmethod
    def help(field_name: str | None = ...) -> str: ...
    
    @staticmethod
    def fields(detailed: bool = ...) -> Union[list[str], list[dict[str, Any]]]: ...
    
    @staticmethod
    def field_info(field_name: str) -> FortiObject: ...
    
    @staticmethod
    def validate_field(name: str, value: Any) -> bool: ...
    
    @staticmethod
    def required_fields() -> list[str]: ...
    
    @staticmethod
    def defaults() -> FortiObject: ...
    
    @staticmethod
    def schema() -> FortiObject: ...


# ================================================================


__all__ = [
    "Status",
]