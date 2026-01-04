from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class CertificateOcspServerPayload(TypedDict, total=False):
    """
    Type hints for vpn/certificate_ocsp_server payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: CertificateOcspServerPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # OCSP server entry name.
    url: NotRequired[str]  # OCSP server URL.
    cert: NotRequired[str]  # OCSP server certificate.
    secondary_url: NotRequired[str]  # Secondary OCSP server URL.
    secondary_cert: NotRequired[str]  # Secondary OCSP server certificate.
    unavail_action: NotRequired[Literal["revoke", "ignore"]]  # Action when server is unavailable (revoke the certificate or
    source_ip: NotRequired[str]  # Source IP address for dynamic AIA and OCSP queries.


class CertificateOcspServer:
    """
    OCSP server configuration.
    
    Path: vpn/certificate_ocsp_server
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
        payload_dict: CertificateOcspServerPayload | None = ...,
        name: str | None = ...,
        url: str | None = ...,
        cert: str | None = ...,
        secondary_url: str | None = ...,
        secondary_cert: str | None = ...,
        unavail_action: Literal["revoke", "ignore"] | None = ...,
        source_ip: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: CertificateOcspServerPayload | None = ...,
        name: str | None = ...,
        url: str | None = ...,
        cert: str | None = ...,
        secondary_url: str | None = ...,
        secondary_cert: str | None = ...,
        unavail_action: Literal["revoke", "ignore"] | None = ...,
        source_ip: str | None = ...,
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
        payload_dict: CertificateOcspServerPayload | None = ...,
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