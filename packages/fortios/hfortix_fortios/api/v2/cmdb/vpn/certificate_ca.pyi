from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class CertificateCaPayload(TypedDict, total=False):
    """
    Type hints for vpn/certificate_ca payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: CertificateCaPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Name.
    ca: str  # CA certificate as a PEM file.
    range: NotRequired[Literal["global", "vdom"]]  # Either global or VDOM IP address range for the CA certificat
    source: NotRequired[Literal["factory", "user", "bundle"]]  # CA certificate source type.
    ssl_inspection_trusted: NotRequired[Literal["enable", "disable"]]  # Enable/disable this CA as a trusted CA for SSL inspection.
    scep_url: NotRequired[str]  # URL of the SCEP server.
    est_url: NotRequired[str]  # URL of the EST server.
    auto_update_days: NotRequired[int]  # Number of days to wait before requesting an updated CA certi
    auto_update_days_warning: NotRequired[int]  # Number of days before an expiry-warning message is generated
    source_ip: NotRequired[str]  # Source IP address for communications to the SCEP server.
    ca_identifier: NotRequired[str]  # CA identifier of the SCEP server.
    obsolete: NotRequired[Literal["disable", "enable"]]  # Enable/disable this CA as obsoleted.
    fabric_ca: NotRequired[Literal["disable", "enable"]]  # Enable/disable synchronization of CA across Security Fabric.
    details: NotRequired[str]  # Print CA certificate detailed information.


class CertificateCa:
    """
    CA certificate.
    
    Path: vpn/certificate_ca
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
        payload_dict: CertificateCaPayload | None = ...,
        name: str | None = ...,
        ca: str | None = ...,
        range: Literal["global", "vdom"] | None = ...,
        source: Literal["factory", "user", "bundle"] | None = ...,
        ssl_inspection_trusted: Literal["enable", "disable"] | None = ...,
        scep_url: str | None = ...,
        est_url: str | None = ...,
        auto_update_days: int | None = ...,
        auto_update_days_warning: int | None = ...,
        source_ip: str | None = ...,
        ca_identifier: str | None = ...,
        obsolete: Literal["disable", "enable"] | None = ...,
        fabric_ca: Literal["disable", "enable"] | None = ...,
        details: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: CertificateCaPayload | None = ...,
        name: str | None = ...,
        ca: str | None = ...,
        range: Literal["global", "vdom"] | None = ...,
        source: Literal["factory", "user", "bundle"] | None = ...,
        ssl_inspection_trusted: Literal["enable", "disable"] | None = ...,
        scep_url: str | None = ...,
        est_url: str | None = ...,
        auto_update_days: int | None = ...,
        auto_update_days_warning: int | None = ...,
        source_ip: str | None = ...,
        ca_identifier: str | None = ...,
        obsolete: Literal["disable", "enable"] | None = ...,
        fabric_ca: Literal["disable", "enable"] | None = ...,
        details: str | None = ...,
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
        payload_dict: CertificateCaPayload | None = ...,
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