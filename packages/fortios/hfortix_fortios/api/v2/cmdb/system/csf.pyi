from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class CsfPayload(TypedDict, total=False):
    """
    Type hints for system/csf payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
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


class Csf:
    """
    Add this FortiGate to a Security Fabric or set up a new Security Fabric on this FortiGate.
    
    Path: system/csf
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
        trusted_list: list[dict[str, Any]] | None = ...,
        fabric_connector: list[dict[str, Any]] | None = ...,
        forticloud_account_enforcement: Literal["enable", "disable"] | None = ...,
        file_mgmt: Literal["enable", "disable"] | None = ...,
        file_quota: int | None = ...,
        file_quota_warning: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
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
        trusted_list: list[dict[str, Any]] | None = ...,
        fabric_connector: list[dict[str, Any]] | None = ...,
        forticloud_account_enforcement: Literal["enable", "disable"] | None = ...,
        file_mgmt: Literal["enable", "disable"] | None = ...,
        file_quota: int | None = ...,
        file_quota_warning: int | None = ...,
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
        payload_dict: CsfPayload | None = ...,
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
    "Csf",
    "CsfPayload",
]