from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class CsfPayload(TypedDict, total=False):
    """
    Type hints for system/csf payload fields.
    
    Add this FortiGate to a Security Fabric or set up a new Security Fabric on this FortiGate.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.certificate.local.LocalEndpoint` (via: certificate)
        - :class:`~.system.accprofile.AccprofileEndpoint` (via: downstream-accprofile)
        - :class:`~.system.interface.InterfaceEndpoint` (via: upstream-interface)

    **Usage:**
        payload: CsfPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    status: Literal["enable", "disable"]  # Enable/disable Security Fabric.
    uid: NotRequired[str]  # Unique ID of the current CSF node
    upstream: NotRequired[str]  # IP/FQDN of the FortiGate upstream from this FortiGate in the
    source_ip: NotRequired[str]  # Source IP address for communication with the upstream FortiG
    upstream_interface_select_method: NotRequired[Literal["auto", "sdwan", "specify"]]  # Specify how to select outgoing interface to reach server.
    upstream_interface: str  # Specify outgoing interface to reach server.
    upstream_port: NotRequired[int]  # The port number to use to communicate with the FortiGate ups
    group_name: NotRequired[str]  # Security Fabric group name. All FortiGates in a Security Fab
    group_password: NotRequired[str]  # Security Fabric group password. For legacy authentication, f
    accept_auth_by_cert: NotRequired[Literal["disable", "enable"]]  # Accept connections with unknown certificates and ask admin f
    log_unification: NotRequired[Literal["disable", "enable"]]  # Enable/disable broadcast of discovery messages for log unifi
    authorization_request_type: NotRequired[Literal["serial", "certificate"]]  # Authorization request type.
    certificate: NotRequired[str]  # Certificate.
    fabric_workers: NotRequired[int]  # Number of worker processes for Security Fabric daemon.
    downstream_access: NotRequired[Literal["enable", "disable"]]  # Enable/disable downstream device access to this device's con
    legacy_authentication: NotRequired[Literal["disable", "enable"]]  # Enable/disable legacy authentication.
    downstream_accprofile: str  # Default access profile for requests from downstream devices.
    configuration_sync: Literal["default", "local"]  # Configuration sync mode.
    fabric_object_unification: NotRequired[Literal["default", "local"]]  # Fabric CMDB Object Unification.
    saml_configuration_sync: NotRequired[Literal["default", "local"]]  # SAML setting configuration synchronization.
    trusted_list: NotRequired[list[dict[str, Any]]]  # Pre-authorized and blocked security fabric nodes.
    fabric_connector: NotRequired[list[dict[str, Any]]]  # Fabric connector configuration.
    forticloud_account_enforcement: NotRequired[Literal["enable", "disable"]]  # Fabric FortiCloud account unification.
    file_mgmt: NotRequired[Literal["enable", "disable"]]  # Enable/disable Security Fabric daemon file management.
    file_quota: NotRequired[int]  # Maximum amount of memory that can be used by the daemon file
    file_quota_warning: NotRequired[int]  # Warn when the set percentage of quota has been used.


class CsfObject(FortiObject[CsfPayload]):
    """Typed FortiObject for system/csf with IDE autocomplete support."""
    
    # Enable/disable Security Fabric.
    status: Literal["enable", "disable"]
    # Unique ID of the current CSF node
    uid: str
    # IP/FQDN of the FortiGate upstream from this FortiGate in the Security Fabric.
    upstream: str
    # Source IP address for communication with the upstream FortiGate.
    source_ip: str
    # Specify how to select outgoing interface to reach server.
    upstream_interface_select_method: Literal["auto", "sdwan", "specify"]
    # Specify outgoing interface to reach server.
    upstream_interface: str
    # The port number to use to communicate with the FortiGate upstream from this Fort
    upstream_port: int
    # Security Fabric group name. All FortiGates in a Security Fabric must have the sa
    group_name: str
    # Security Fabric group password. For legacy authentication, fabric members must h
    group_password: str
    # Accept connections with unknown certificates and ask admin for approval.
    accept_auth_by_cert: Literal["disable", "enable"]
    # Enable/disable broadcast of discovery messages for log unification.
    log_unification: Literal["disable", "enable"]
    # Authorization request type.
    authorization_request_type: Literal["serial", "certificate"]
    # Certificate.
    certificate: str
    # Number of worker processes for Security Fabric daemon.
    fabric_workers: int
    # Enable/disable downstream device access to this device's configuration and data.
    downstream_access: Literal["enable", "disable"]
    # Enable/disable legacy authentication.
    legacy_authentication: Literal["disable", "enable"]
    # Default access profile for requests from downstream devices.
    downstream_accprofile: str
    # Configuration sync mode.
    configuration_sync: Literal["default", "local"]
    # Fabric CMDB Object Unification.
    fabric_object_unification: Literal["default", "local"]
    # SAML setting configuration synchronization.
    saml_configuration_sync: Literal["default", "local"]
    # Pre-authorized and blocked security fabric nodes.
    trusted_list: list[str]  # Auto-flattened from member_table
    # Fabric connector configuration.
    fabric_connector: list[str]  # Auto-flattened from member_table
    # Fabric FortiCloud account unification.
    forticloud_account_enforcement: Literal["enable", "disable"]
    # Enable/disable Security Fabric daemon file management.
    file_mgmt: Literal["enable", "disable"]
    # Maximum amount of memory that can be used by the daemon files (in bytes).
    file_quota: int
    # Warn when the set percentage of quota has been used.
    file_quota_warning: int
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> CsfPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Csf:
    """
    Add this FortiGate to a Security Fabric or set up a new Security Fabric on this FortiGate.
    
    Path: system/csf
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
    ) -> CsfObject: ...
    
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
    ) -> CsfObject: ...
    
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
    ) -> CsfObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: CsfPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        uid: str | None = ...,
        upstream: str | None = ...,
        source_ip: str | None = ...,
        upstream_interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        upstream_interface: str | None = ...,
        upstream_port: int | None = ...,
        group_name: str | None = ...,
        group_password: str | None = ...,
        accept_auth_by_cert: Literal["disable", "enable"] | None = ...,
        log_unification: Literal["disable", "enable"] | None = ...,
        authorization_request_type: Literal["serial", "certificate"] | None = ...,
        certificate: str | None = ...,
        fabric_workers: int | None = ...,
        downstream_access: Literal["enable", "disable"] | None = ...,
        legacy_authentication: Literal["disable", "enable"] | None = ...,
        downstream_accprofile: str | None = ...,
        configuration_sync: Literal["default", "local"] | None = ...,
        fabric_object_unification: Literal["default", "local"] | None = ...,
        saml_configuration_sync: Literal["default", "local"] | None = ...,
        trusted_list: str | list[str] | list[dict[str, Any]] | None = ...,
        fabric_connector: str | list[str] | list[dict[str, Any]] | None = ...,
        forticloud_account_enforcement: Literal["enable", "disable"] | None = ...,
        file_mgmt: Literal["enable", "disable"] | None = ...,
        file_quota: int | None = ...,
        file_quota_warning: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> CsfObject: ...
    
    @overload
    def put(
        self,
        payload_dict: CsfPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        uid: str | None = ...,
        upstream: str | None = ...,
        source_ip: str | None = ...,
        upstream_interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        upstream_interface: str | None = ...,
        upstream_port: int | None = ...,
        group_name: str | None = ...,
        group_password: str | None = ...,
        accept_auth_by_cert: Literal["disable", "enable"] | None = ...,
        log_unification: Literal["disable", "enable"] | None = ...,
        authorization_request_type: Literal["serial", "certificate"] | None = ...,
        certificate: str | None = ...,
        fabric_workers: int | None = ...,
        downstream_access: Literal["enable", "disable"] | None = ...,
        legacy_authentication: Literal["disable", "enable"] | None = ...,
        downstream_accprofile: str | None = ...,
        configuration_sync: Literal["default", "local"] | None = ...,
        fabric_object_unification: Literal["default", "local"] | None = ...,
        saml_configuration_sync: Literal["default", "local"] | None = ...,
        trusted_list: str | list[str] | list[dict[str, Any]] | None = ...,
        fabric_connector: str | list[str] | list[dict[str, Any]] | None = ...,
        forticloud_account_enforcement: Literal["enable", "disable"] | None = ...,
        file_mgmt: Literal["enable", "disable"] | None = ...,
        file_quota: int | None = ...,
        file_quota_warning: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: CsfPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        uid: str | None = ...,
        upstream: str | None = ...,
        source_ip: str | None = ...,
        upstream_interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        upstream_interface: str | None = ...,
        upstream_port: int | None = ...,
        group_name: str | None = ...,
        group_password: str | None = ...,
        accept_auth_by_cert: Literal["disable", "enable"] | None = ...,
        log_unification: Literal["disable", "enable"] | None = ...,
        authorization_request_type: Literal["serial", "certificate"] | None = ...,
        certificate: str | None = ...,
        fabric_workers: int | None = ...,
        downstream_access: Literal["enable", "disable"] | None = ...,
        legacy_authentication: Literal["disable", "enable"] | None = ...,
        downstream_accprofile: str | None = ...,
        configuration_sync: Literal["default", "local"] | None = ...,
        fabric_object_unification: Literal["default", "local"] | None = ...,
        saml_configuration_sync: Literal["default", "local"] | None = ...,
        trusted_list: str | list[str] | list[dict[str, Any]] | None = ...,
        fabric_connector: str | list[str] | list[dict[str, Any]] | None = ...,
        forticloud_account_enforcement: Literal["enable", "disable"] | None = ...,
        file_mgmt: Literal["enable", "disable"] | None = ...,
        file_quota: int | None = ...,
        file_quota_warning: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: CsfPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        uid: str | None = ...,
        upstream: str | None = ...,
        source_ip: str | None = ...,
        upstream_interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        upstream_interface: str | None = ...,
        upstream_port: int | None = ...,
        group_name: str | None = ...,
        group_password: str | None = ...,
        accept_auth_by_cert: Literal["disable", "enable"] | None = ...,
        log_unification: Literal["disable", "enable"] | None = ...,
        authorization_request_type: Literal["serial", "certificate"] | None = ...,
        certificate: str | None = ...,
        fabric_workers: int | None = ...,
        downstream_access: Literal["enable", "disable"] | None = ...,
        legacy_authentication: Literal["disable", "enable"] | None = ...,
        downstream_accprofile: str | None = ...,
        configuration_sync: Literal["default", "local"] | None = ...,
        fabric_object_unification: Literal["default", "local"] | None = ...,
        saml_configuration_sync: Literal["default", "local"] | None = ...,
        trusted_list: str | list[str] | list[dict[str, Any]] | None = ...,
        fabric_connector: str | list[str] | list[dict[str, Any]] | None = ...,
        forticloud_account_enforcement: Literal["enable", "disable"] | None = ...,
        file_mgmt: Literal["enable", "disable"] | None = ...,
        file_quota: int | None = ...,
        file_quota_warning: int | None = ...,
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
        payload_dict: CsfPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        uid: str | None = ...,
        upstream: str | None = ...,
        source_ip: str | None = ...,
        upstream_interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        upstream_interface: str | None = ...,
        upstream_port: int | None = ...,
        group_name: str | None = ...,
        group_password: str | None = ...,
        accept_auth_by_cert: Literal["disable", "enable"] | None = ...,
        log_unification: Literal["disable", "enable"] | None = ...,
        authorization_request_type: Literal["serial", "certificate"] | None = ...,
        certificate: str | None = ...,
        fabric_workers: int | None = ...,
        downstream_access: Literal["enable", "disable"] | None = ...,
        legacy_authentication: Literal["disable", "enable"] | None = ...,
        downstream_accprofile: str | None = ...,
        configuration_sync: Literal["default", "local"] | None = ...,
        fabric_object_unification: Literal["default", "local"] | None = ...,
        saml_configuration_sync: Literal["default", "local"] | None = ...,
        trusted_list: str | list[str] | list[dict[str, Any]] | None = ...,
        fabric_connector: str | list[str] | list[dict[str, Any]] | None = ...,
        forticloud_account_enforcement: Literal["enable", "disable"] | None = ...,
        file_mgmt: Literal["enable", "disable"] | None = ...,
        file_quota: int | None = ...,
        file_quota_warning: int | None = ...,
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
    "Csf",
    "CsfPayload",
    "CsfObject",
]