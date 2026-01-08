from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
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

# Nested classes for table field children

@final
class CsfTrustedlistObject:
    """Typed object for trusted-list table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Name.
    name: str
    # Authorization type.
    authorization_type: Literal["serial", "certificate"]
    # Serial.
    serial: str
    # Certificate.
    certificate: str
    # Security fabric authorization action.
    action: Literal["accept", "deny"]
    # HA members.
    ha_members: str
    # Trust authorizations by this node's administrator.
    downstream_authorization: Literal["enable", "disable"]
    # Index of the downstream in tree.
    index: int
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class CsfFabricconnectorObject:
    """Typed object for fabric-connector table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Serial.
    serial: str
    # Override access profile.
    accprofile: str
    # Enable/disable downstream device write access to configuration.
    configuration_write_access: Literal["enable", "disable"]
    # Virtual domains that the connector has access to. If none are set, the connector
    vdom: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...



# Response TypedDict for GET returns (all fields present in API response)
class CsfResponse(TypedDict):
    """
    Type hints for system/csf API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    status: Literal["enable", "disable"]
    uid: str
    upstream: str
    source_ip: str
    upstream_interface_select_method: Literal["auto", "sdwan", "specify"]
    upstream_interface: str
    upstream_port: int
    group_name: str
    group_password: str
    accept_auth_by_cert: Literal["disable", "enable"]
    log_unification: Literal["disable", "enable"]
    authorization_request_type: Literal["serial", "certificate"]
    certificate: str
    fabric_workers: int
    downstream_access: Literal["enable", "disable"]
    legacy_authentication: Literal["disable", "enable"]
    downstream_accprofile: str
    configuration_sync: Literal["default", "local"]
    fabric_object_unification: Literal["default", "local"]
    saml_configuration_sync: Literal["default", "local"]
    trusted_list: list[dict[str, Any]]
    fabric_connector: list[dict[str, Any]]
    forticloud_account_enforcement: Literal["enable", "disable"]
    file_mgmt: Literal["enable", "disable"]
    file_quota: int
    file_quota_warning: int


@final
class CsfObject:
    """Typed FortiObject for system/csf with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
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
    trusted_list: list[CsfTrustedlistObject]  # Table field - list of typed objects
    # Fabric connector configuration.
    fabric_connector: list[CsfFabricconnectorObject]  # Table field - list of typed objects
    # Fabric FortiCloud account unification.
    forticloud_account_enforcement: Literal["enable", "disable"]
    # Enable/disable Security Fabric daemon file management.
    file_mgmt: Literal["enable", "disable"]
    # Maximum amount of memory that can be used by the daemon files (in bytes).
    file_quota: int
    # Warn when the set percentage of quota has been used.
    file_quota_warning: int
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> CsfPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class Csf:
    """
    Add this FortiGate to a Security Fabric or set up a new Security Fabric on this FortiGate.
    
    Path: system/csf
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
    ) -> CsfObject: ...
    
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
    ) -> CsfObject: ...
    
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
    ) -> CsfResponse: ...
    
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
    ) -> CsfResponse: ...
    
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
    ) -> CsfResponse: ...
    
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