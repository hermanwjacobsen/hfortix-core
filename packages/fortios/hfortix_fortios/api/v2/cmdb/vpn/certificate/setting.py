"""
FortiOS CMDB - Vpn certificate setting

Configuration endpoint for managing cmdb vpn/certificate/setting objects.

API Endpoints:
    GET    /cmdb/vpn/certificate/setting
    POST   /cmdb/vpn/certificate/setting
    PUT    /cmdb/vpn/certificate/setting/{identifier}
    DELETE /cmdb/vpn/certificate/setting/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.vpn_certificate_setting.get()

Important:
    - Use **POST** to create new objects
    - Use **PUT** to update existing objects
    - Use **GET** to retrieve configuration
    - Use **DELETE** to remove objects
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Union

if TYPE_CHECKING:
    from collections.abc import Coroutine
    from hfortix_core.http.interface import IHTTPClient

# Import helper functions from central _helpers module
from hfortix_fortios._helpers import (
    build_cmdb_payload,
    is_success,
)
# Import metadata mixin for schema introspection
from hfortix_fortios._helpers.metadata_mixin import MetadataMixin


class Setting(MetadataMixin):
    """Setting Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "setting"

    def __init__(self, client: "IHTTPClient"):
        """Initialize Setting endpoint."""
        self._client = client

    def get(
        self,
        name: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve vpn/certificate/setting configuration.

        VPN certificate setting.

        Args:
            name: Name identifier to retrieve specific object. If None, returns all objects.
            payload_dict: Additional query parameters (filters, format, etc.)
            vdom: Virtual domain name. Use True for global, string for specific VDOM, None for default.
            raw_json: If True, return raw API response without processing.
            **kwargs: Additional query parameters (action, format, etc.)

        Returns:
            Configuration data as dict. Returns Coroutine if using async client.
            
            Response structure:
                - http_method: GET
                - results: Configuration object(s)
                - vdom: Virtual domain
                - path: API path
                - name: Object name (single object queries)
                - status: success/error
                - http_status: HTTP status code
                - build: FortiOS build number

        Examples:
            >>> # Get all vpn/certificate/setting objects
            >>> result = fgt.api.cmdb.vpn_certificate_setting.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.vpn_certificate_setting.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.vpn_certificate_setting.get(action="schema")

        See Also:
            - post(): Create new vpn/certificate/setting object
            - put(): Update existing vpn/certificate/setting object
            - delete(): Remove vpn/certificate/setting object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/vpn.certificate/setting/{name}"
        else:
            endpoint = "/vpn.certificate/setting"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        ocsp_status: str | None = None,
        ocsp_option: str | None = None,
        proxy: str | None = None,
        proxy_port: int | None = None,
        proxy_username: str | None = None,
        proxy_password: Any | None = None,
        source_ip: str | None = None,
        ocsp_default_server: str | None = None,
        interface_select_method: str | None = None,
        interface: str | None = None,
        vrf_select: int | None = None,
        check_ca_cert: str | None = None,
        check_ca_chain: str | None = None,
        subject_match: str | None = None,
        subject_set: str | None = None,
        cn_match: str | None = None,
        cn_allow_multi: str | None = None,
        crl_verification: str | None = None,
        strict_ocsp_check: str | None = None,
        ssl_min_proto_version: str | None = None,
        cmp_save_extra_certs: str | None = None,
        cmp_key_usage_checking: str | None = None,
        cert_expire_warning: int | None = None,
        certname_rsa1024: str | None = None,
        certname_rsa2048: str | None = None,
        certname_rsa4096: str | None = None,
        certname_dsa1024: str | None = None,
        certname_dsa2048: str | None = None,
        certname_ecdsa256: str | None = None,
        certname_ecdsa384: str | None = None,
        certname_ecdsa521: str | None = None,
        certname_ed25519: str | None = None,
        certname_ed448: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing vpn/certificate/setting object.

        VPN certificate setting.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            ocsp_status: Enable/disable receiving certificates using the OCSP.
            ocsp_option: Specify whether the OCSP URL is from certificate or configured OCSP server.
            proxy: Proxy server FQDN or IP for OCSP/CA queries during certificate verification.
            proxy_port: Proxy server port (1 - 65535, default = 8080).
            proxy_username: Proxy server user name.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.vpn_certificate_setting.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.vpn_certificate_setting.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            ocsp_status=ocsp_status,
            ocsp_option=ocsp_option,
            proxy=proxy,
            proxy_port=proxy_port,
            proxy_username=proxy_username,
            proxy_password=proxy_password,
            source_ip=source_ip,
            ocsp_default_server=ocsp_default_server,
            interface_select_method=interface_select_method,
            interface=interface,
            vrf_select=vrf_select,
            check_ca_cert=check_ca_cert,
            check_ca_chain=check_ca_chain,
            subject_match=subject_match,
            subject_set=subject_set,
            cn_match=cn_match,
            cn_allow_multi=cn_allow_multi,
            crl_verification=crl_verification,
            strict_ocsp_check=strict_ocsp_check,
            ssl_min_proto_version=ssl_min_proto_version,
            cmp_save_extra_certs=cmp_save_extra_certs,
            cmp_key_usage_checking=cmp_key_usage_checking,
            cert_expire_warning=cert_expire_warning,
            certname_rsa1024=certname_rsa1024,
            certname_rsa2048=certname_rsa2048,
            certname_rsa4096=certname_rsa4096,
            certname_dsa1024=certname_dsa1024,
            certname_dsa2048=certname_dsa2048,
            certname_ecdsa256=certname_ecdsa256,
            certname_ecdsa384=certname_ecdsa384,
            certname_ecdsa521=certname_ecdsa521,
            certname_ed25519=certname_ed25519,
            certname_ed448=certname_ed448,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.setting import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/vpn/certificate/setting",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/vpn.certificate/setting/{name_value}"

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )





