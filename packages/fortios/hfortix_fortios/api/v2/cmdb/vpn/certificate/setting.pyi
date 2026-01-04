from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class SettingPayload(TypedDict, total=False):
    """
    Type hints for vpn/certificate/setting payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: SettingPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    ocsp_status: NotRequired[Literal["enable", "mandatory", "disable"]]  # Enable/disable receiving certificates using the OCSP.
    ocsp_option: NotRequired[Literal["certificate", "server"]]  # Specify whether the OCSP URL is from certificate or configur
    proxy: NotRequired[str]  # Proxy server FQDN or IP for OCSP/CA queries during certifica
    proxy_port: NotRequired[int]  # Proxy server port (1 - 65535, default = 8080).
    proxy_username: NotRequired[str]  # Proxy server user name.
    proxy_password: NotRequired[str]  # Proxy server password.
    source_ip: NotRequired[str]  # Source IP address for dynamic AIA and OCSP queries.
    ocsp_default_server: NotRequired[str]  # Default OCSP server.
    interface_select_method: NotRequired[Literal["auto", "sdwan", "specify"]]  # Specify how to select outgoing interface to reach server.
    interface: str  # Specify outgoing interface to reach server.
    vrf_select: NotRequired[int]  # VRF ID used for connection to server.
    check_ca_cert: NotRequired[Literal["enable", "disable"]]  # Enable/disable verification of the user certificate and pass
    check_ca_chain: NotRequired[Literal["enable", "disable"]]  # Enable/disable verification of the entire certificate chain 
    subject_match: NotRequired[Literal["substring", "value"]]  # When searching for a matching certificate, control how to do
    subject_set: NotRequired[Literal["subset", "superset"]]  # When searching for a matching certificate, control how to do
    cn_match: NotRequired[Literal["substring", "value"]]  # When searching for a matching certificate, control how to do
    cn_allow_multi: NotRequired[Literal["disable", "enable"]]  # When searching for a matching certificate, allow multiple CN
    crl_verification: NotRequired[str]  # CRL verification options.
    strict_ocsp_check: NotRequired[Literal["enable", "disable"]]  # Enable/disable strict mode OCSP checking.
    ssl_min_proto_version: NotRequired[Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"]]  # Minimum supported protocol version for SSL/TLS connections (
    cmp_save_extra_certs: NotRequired[Literal["enable", "disable"]]  # Enable/disable saving extra certificates in CMP mode (defaul
    cmp_key_usage_checking: NotRequired[Literal["enable", "disable"]]  # Enable/disable server certificate key usage checking in CMP 
    cert_expire_warning: NotRequired[int]  # Number of days before a certificate expires to send a warnin
    certname_rsa1024: str  # 1024 bit RSA key certificate for re-signing server certifica
    certname_rsa2048: str  # 2048 bit RSA key certificate for re-signing server certifica
    certname_rsa4096: str  # 4096 bit RSA key certificate for re-signing server certifica
    certname_dsa1024: str  # 1024 bit DSA key certificate for re-signing server certifica
    certname_dsa2048: str  # 2048 bit DSA key certificate for re-signing server certifica
    certname_ecdsa256: str  # 256 bit ECDSA key certificate for re-signing server certific
    certname_ecdsa384: str  # 384 bit ECDSA key certificate for re-signing server certific
    certname_ecdsa521: str  # 521 bit ECDSA key certificate for re-signing server certific
    certname_ed25519: str  # 253 bit EdDSA key certificate for re-signing server certific
    certname_ed448: str  # 456 bit EdDSA key certificate for re-signing server certific


class Setting:
    """
    VPN certificate setting.
    
    Path: vpn/certificate/setting
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
        payload_dict: SettingPayload | None = ...,
        ocsp_status: Literal["enable", "mandatory", "disable"] | None = ...,
        ocsp_option: Literal["certificate", "server"] | None = ...,
        proxy: str | None = ...,
        proxy_port: int | None = ...,
        proxy_username: str | None = ...,
        proxy_password: str | None = ...,
        source_ip: str | None = ...,
        ocsp_default_server: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        check_ca_cert: Literal["enable", "disable"] | None = ...,
        check_ca_chain: Literal["enable", "disable"] | None = ...,
        subject_match: Literal["substring", "value"] | None = ...,
        subject_set: Literal["subset", "superset"] | None = ...,
        cn_match: Literal["substring", "value"] | None = ...,
        cn_allow_multi: Literal["disable", "enable"] | None = ...,
        crl_verification: str | None = ...,
        strict_ocsp_check: Literal["enable", "disable"] | None = ...,
        ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        cmp_save_extra_certs: Literal["enable", "disable"] | None = ...,
        cmp_key_usage_checking: Literal["enable", "disable"] | None = ...,
        cert_expire_warning: int | None = ...,
        certname_rsa1024: str | None = ...,
        certname_rsa2048: str | None = ...,
        certname_rsa4096: str | None = ...,
        certname_dsa1024: str | None = ...,
        certname_dsa2048: str | None = ...,
        certname_ecdsa256: str | None = ...,
        certname_ecdsa384: str | None = ...,
        certname_ecdsa521: str | None = ...,
        certname_ed25519: str | None = ...,
        certname_ed448: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: SettingPayload | None = ...,
        ocsp_status: Literal["enable", "mandatory", "disable"] | None = ...,
        ocsp_option: Literal["certificate", "server"] | None = ...,
        proxy: str | None = ...,
        proxy_port: int | None = ...,
        proxy_username: str | None = ...,
        proxy_password: str | None = ...,
        source_ip: str | None = ...,
        ocsp_default_server: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        check_ca_cert: Literal["enable", "disable"] | None = ...,
        check_ca_chain: Literal["enable", "disable"] | None = ...,
        subject_match: Literal["substring", "value"] | None = ...,
        subject_set: Literal["subset", "superset"] | None = ...,
        cn_match: Literal["substring", "value"] | None = ...,
        cn_allow_multi: Literal["disable", "enable"] | None = ...,
        crl_verification: str | None = ...,
        strict_ocsp_check: Literal["enable", "disable"] | None = ...,
        ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        cmp_save_extra_certs: Literal["enable", "disable"] | None = ...,
        cmp_key_usage_checking: Literal["enable", "disable"] | None = ...,
        cert_expire_warning: int | None = ...,
        certname_rsa1024: str | None = ...,
        certname_rsa2048: str | None = ...,
        certname_rsa4096: str | None = ...,
        certname_dsa1024: str | None = ...,
        certname_dsa2048: str | None = ...,
        certname_ecdsa256: str | None = ...,
        certname_ecdsa384: str | None = ...,
        certname_ecdsa521: str | None = ...,
        certname_ed25519: str | None = ...,
        certname_ed448: str | None = ...,
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
        payload_dict: SettingPayload | None = ...,
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
    "Setting",
    "SettingPayload",
]