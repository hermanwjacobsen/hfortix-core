"""
FortiOS CMDB - Firewall vip6

Configuration endpoint for managing cmdb firewall/vip6 objects.

API Endpoints:
    GET    /cmdb/firewall/vip6
    POST   /cmdb/firewall/vip6
    PUT    /cmdb/firewall/vip6/{identifier}
    DELETE /cmdb/firewall/vip6/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.firewall_vip6.get()

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


class Vip6(MetadataMixin):
    """Vip6 Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "vip6"

    def __init__(self, client: "IHTTPClient"):
        """Initialize Vip6 endpoint."""
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
        Retrieve firewall/vip6 configuration.

        Configure virtual IP for IPv6.

        Args:
            name: String identifier to retrieve specific object.
                If None, returns all objects.
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
            >>> # Get all firewall/vip6 objects
            >>> result = fgt.api.cmdb.firewall_vip6.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific firewall/vip6 by name
            >>> result = fgt.api.cmdb.firewall_vip6.get(name=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.firewall_vip6.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.firewall_vip6.get(action="schema")

        See Also:
            - post(): Create new firewall/vip6 object
            - put(): Update existing firewall/vip6 object
            - delete(): Remove firewall/vip6 object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = "/firewall/vip6/" + str(name)
        else:
            endpoint = "/firewall/vip6"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        name: str | None = None,
        id: int | None = None,
        uuid: str | None = None,
        comment: str | None = None,
        type: str | None = None,
        src_filter: str | list | None = None,
        src_vip_filter: str | None = None,
        extip: str | None = None,
        mappedip: str | None = None,
        nat_source_vip: str | None = None,
        ndp_reply: str | None = None,
        portforward: str | None = None,
        protocol: str | None = None,
        extport: str | None = None,
        mappedport: str | None = None,
        color: int | None = None,
        ldb_method: str | None = None,
        server_type: str | None = None,
        http_redirect: str | None = None,
        persistence: str | None = None,
        h2_support: str | None = None,
        h3_support: str | None = None,
        quic: str | None = None,
        nat66: str | None = None,
        nat64: str | None = None,
        add_nat64_route: str | None = None,
        empty_cert_action: str | None = None,
        user_agent_detect: str | None = None,
        client_cert: str | None = None,
        realservers: str | list | None = None,
        http_cookie_domain_from_host: str | None = None,
        http_cookie_domain: str | None = None,
        http_cookie_path: str | None = None,
        http_cookie_generation: int | None = None,
        http_cookie_age: int | None = None,
        http_cookie_share: str | None = None,
        https_cookie_secure: str | None = None,
        http_multiplex: str | None = None,
        http_ip_header: str | None = None,
        http_ip_header_name: str | None = None,
        outlook_web_access: str | None = None,
        weblogic_server: str | None = None,
        websphere_server: str | None = None,
        ssl_mode: str | None = None,
        ssl_certificate: str | list | None = None,
        ssl_dh_bits: str | None = None,
        ssl_algorithm: str | None = None,
        ssl_cipher_suites: str | list | None = None,
        ssl_server_renegotiation: str | None = None,
        ssl_server_algorithm: str | None = None,
        ssl_server_cipher_suites: str | list | None = None,
        ssl_pfs: str | None = None,
        ssl_min_version: str | None = None,
        ssl_max_version: str | None = None,
        ssl_server_min_version: str | None = None,
        ssl_server_max_version: str | None = None,
        ssl_accept_ffdhe_groups: str | None = None,
        ssl_send_empty_frags: str | None = None,
        ssl_client_fallback: str | None = None,
        ssl_client_renegotiation: str | None = None,
        ssl_client_session_state_type: str | None = None,
        ssl_client_session_state_timeout: int | None = None,
        ssl_client_session_state_max: int | None = None,
        ssl_client_rekey_count: int | None = None,
        ssl_server_session_state_type: str | None = None,
        ssl_server_session_state_timeout: int | None = None,
        ssl_server_session_state_max: int | None = None,
        ssl_http_location_conversion: str | None = None,
        ssl_http_match_host: str | None = None,
        ssl_hpkp: str | None = None,
        ssl_hpkp_primary: str | None = None,
        ssl_hpkp_backup: str | None = None,
        ssl_hpkp_age: int | None = None,
        ssl_hpkp_report_uri: str | None = None,
        ssl_hpkp_include_subdomains: str | None = None,
        ssl_hsts: str | None = None,
        ssl_hsts_age: int | None = None,
        ssl_hsts_include_subdomains: str | None = None,
        monitor: str | list | None = None,
        max_embryonic_connections: int | None = None,
        embedded_ipv4_address: str | None = None,
        ipv4_mappedip: str | None = None,
        ipv4_mappedport: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing firewall/vip6 object.

        Configure virtual IP for IPv6.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            name: Virtual ip6 name.
            id: Custom defined ID.
            uuid: Universally Unique Identifier (UUID; automatically assigned but can be manually reset).
            comment: Comment.
            type: Configure a static NAT server load balance VIP or access proxy.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.firewall_vip6.put(
            ...     name=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.firewall_vip6.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            name=name,
            id=id,
            uuid=uuid,
            comment=comment,
            type=type,
            src_filter=src_filter,
            src_vip_filter=src_vip_filter,
            extip=extip,
            mappedip=mappedip,
            nat_source_vip=nat_source_vip,
            ndp_reply=ndp_reply,
            portforward=portforward,
            protocol=protocol,
            extport=extport,
            mappedport=mappedport,
            color=color,
            ldb_method=ldb_method,
            server_type=server_type,
            http_redirect=http_redirect,
            persistence=persistence,
            h2_support=h2_support,
            h3_support=h3_support,
            quic=quic,
            nat66=nat66,
            nat64=nat64,
            add_nat64_route=add_nat64_route,
            empty_cert_action=empty_cert_action,
            user_agent_detect=user_agent_detect,
            client_cert=client_cert,
            realservers=realservers,
            http_cookie_domain_from_host=http_cookie_domain_from_host,
            http_cookie_domain=http_cookie_domain,
            http_cookie_path=http_cookie_path,
            http_cookie_generation=http_cookie_generation,
            http_cookie_age=http_cookie_age,
            http_cookie_share=http_cookie_share,
            https_cookie_secure=https_cookie_secure,
            http_multiplex=http_multiplex,
            http_ip_header=http_ip_header,
            http_ip_header_name=http_ip_header_name,
            outlook_web_access=outlook_web_access,
            weblogic_server=weblogic_server,
            websphere_server=websphere_server,
            ssl_mode=ssl_mode,
            ssl_certificate=ssl_certificate,
            ssl_dh_bits=ssl_dh_bits,
            ssl_algorithm=ssl_algorithm,
            ssl_cipher_suites=ssl_cipher_suites,
            ssl_server_renegotiation=ssl_server_renegotiation,
            ssl_server_algorithm=ssl_server_algorithm,
            ssl_server_cipher_suites=ssl_server_cipher_suites,
            ssl_pfs=ssl_pfs,
            ssl_min_version=ssl_min_version,
            ssl_max_version=ssl_max_version,
            ssl_server_min_version=ssl_server_min_version,
            ssl_server_max_version=ssl_server_max_version,
            ssl_accept_ffdhe_groups=ssl_accept_ffdhe_groups,
            ssl_send_empty_frags=ssl_send_empty_frags,
            ssl_client_fallback=ssl_client_fallback,
            ssl_client_renegotiation=ssl_client_renegotiation,
            ssl_client_session_state_type=ssl_client_session_state_type,
            ssl_client_session_state_timeout=ssl_client_session_state_timeout,
            ssl_client_session_state_max=ssl_client_session_state_max,
            ssl_client_rekey_count=ssl_client_rekey_count,
            ssl_server_session_state_type=ssl_server_session_state_type,
            ssl_server_session_state_timeout=ssl_server_session_state_timeout,
            ssl_server_session_state_max=ssl_server_session_state_max,
            ssl_http_location_conversion=ssl_http_location_conversion,
            ssl_http_match_host=ssl_http_match_host,
            ssl_hpkp=ssl_hpkp,
            ssl_hpkp_primary=ssl_hpkp_primary,
            ssl_hpkp_backup=ssl_hpkp_backup,
            ssl_hpkp_age=ssl_hpkp_age,
            ssl_hpkp_report_uri=ssl_hpkp_report_uri,
            ssl_hpkp_include_subdomains=ssl_hpkp_include_subdomains,
            ssl_hsts=ssl_hsts,
            ssl_hsts_age=ssl_hsts_age,
            ssl_hsts_include_subdomains=ssl_hsts_include_subdomains,
            monitor=monitor,
            max_embryonic_connections=max_embryonic_connections,
            embedded_ipv4_address=embedded_ipv4_address,
            ipv4_mappedip=ipv4_mappedip,
            ipv4_mappedport=ipv4_mappedport,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.vip6 import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/firewall/vip6",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = "/firewall/vip6/" + str(name_value)

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        name: str | None = None,
        id: int | None = None,
        uuid: str | None = None,
        comment: str | None = None,
        type: str | None = None,
        src_filter: str | list | None = None,
        src_vip_filter: str | None = None,
        extip: str | None = None,
        mappedip: str | None = None,
        nat_source_vip: str | None = None,
        ndp_reply: str | None = None,
        portforward: str | None = None,
        protocol: str | None = None,
        extport: str | None = None,
        mappedport: str | None = None,
        color: int | None = None,
        ldb_method: str | None = None,
        server_type: str | None = None,
        http_redirect: str | None = None,
        persistence: str | None = None,
        h2_support: str | None = None,
        h3_support: str | None = None,
        quic: str | None = None,
        nat66: str | None = None,
        nat64: str | None = None,
        add_nat64_route: str | None = None,
        empty_cert_action: str | None = None,
        user_agent_detect: str | None = None,
        client_cert: str | None = None,
        realservers: str | list | None = None,
        http_cookie_domain_from_host: str | None = None,
        http_cookie_domain: str | None = None,
        http_cookie_path: str | None = None,
        http_cookie_generation: int | None = None,
        http_cookie_age: int | None = None,
        http_cookie_share: str | None = None,
        https_cookie_secure: str | None = None,
        http_multiplex: str | None = None,
        http_ip_header: str | None = None,
        http_ip_header_name: str | None = None,
        outlook_web_access: str | None = None,
        weblogic_server: str | None = None,
        websphere_server: str | None = None,
        ssl_mode: str | None = None,
        ssl_certificate: str | list | None = None,
        ssl_dh_bits: str | None = None,
        ssl_algorithm: str | None = None,
        ssl_cipher_suites: str | list | None = None,
        ssl_server_renegotiation: str | None = None,
        ssl_server_algorithm: str | None = None,
        ssl_server_cipher_suites: str | list | None = None,
        ssl_pfs: str | None = None,
        ssl_min_version: str | None = None,
        ssl_max_version: str | None = None,
        ssl_server_min_version: str | None = None,
        ssl_server_max_version: str | None = None,
        ssl_accept_ffdhe_groups: str | None = None,
        ssl_send_empty_frags: str | None = None,
        ssl_client_fallback: str | None = None,
        ssl_client_renegotiation: str | None = None,
        ssl_client_session_state_type: str | None = None,
        ssl_client_session_state_timeout: int | None = None,
        ssl_client_session_state_max: int | None = None,
        ssl_client_rekey_count: int | None = None,
        ssl_server_session_state_type: str | None = None,
        ssl_server_session_state_timeout: int | None = None,
        ssl_server_session_state_max: int | None = None,
        ssl_http_location_conversion: str | None = None,
        ssl_http_match_host: str | None = None,
        ssl_hpkp: str | None = None,
        ssl_hpkp_primary: str | None = None,
        ssl_hpkp_backup: str | None = None,
        ssl_hpkp_age: int | None = None,
        ssl_hpkp_report_uri: str | None = None,
        ssl_hpkp_include_subdomains: str | None = None,
        ssl_hsts: str | None = None,
        ssl_hsts_age: int | None = None,
        ssl_hsts_include_subdomains: str | None = None,
        monitor: str | list | None = None,
        max_embryonic_connections: int | None = None,
        embedded_ipv4_address: str | None = None,
        ipv4_mappedip: str | None = None,
        ipv4_mappedport: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create new firewall/vip6 object.

        Configure virtual IP for IPv6.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            name: Virtual ip6 name.
            id: Custom defined ID.
            uuid: Universally Unique Identifier (UUID; automatically assigned but can be manually reset).
            comment: Comment.
            type: Configure a static NAT server load balance VIP or access proxy.
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            raw_json: If True, return raw API response without processing.
            **kwargs: Additional parameters

        Returns:
            API response dict containing created object with assigned name.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.firewall_vip6.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created name: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = Vip6.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.firewall_vip6.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(Vip6.required_fields()) }}
            
            Use Vip6.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            name=name,
            id=id,
            uuid=uuid,
            comment=comment,
            type=type,
            src_filter=src_filter,
            src_vip_filter=src_vip_filter,
            extip=extip,
            mappedip=mappedip,
            nat_source_vip=nat_source_vip,
            ndp_reply=ndp_reply,
            portforward=portforward,
            protocol=protocol,
            extport=extport,
            mappedport=mappedport,
            color=color,
            ldb_method=ldb_method,
            server_type=server_type,
            http_redirect=http_redirect,
            persistence=persistence,
            h2_support=h2_support,
            h3_support=h3_support,
            quic=quic,
            nat66=nat66,
            nat64=nat64,
            add_nat64_route=add_nat64_route,
            empty_cert_action=empty_cert_action,
            user_agent_detect=user_agent_detect,
            client_cert=client_cert,
            realservers=realservers,
            http_cookie_domain_from_host=http_cookie_domain_from_host,
            http_cookie_domain=http_cookie_domain,
            http_cookie_path=http_cookie_path,
            http_cookie_generation=http_cookie_generation,
            http_cookie_age=http_cookie_age,
            http_cookie_share=http_cookie_share,
            https_cookie_secure=https_cookie_secure,
            http_multiplex=http_multiplex,
            http_ip_header=http_ip_header,
            http_ip_header_name=http_ip_header_name,
            outlook_web_access=outlook_web_access,
            weblogic_server=weblogic_server,
            websphere_server=websphere_server,
            ssl_mode=ssl_mode,
            ssl_certificate=ssl_certificate,
            ssl_dh_bits=ssl_dh_bits,
            ssl_algorithm=ssl_algorithm,
            ssl_cipher_suites=ssl_cipher_suites,
            ssl_server_renegotiation=ssl_server_renegotiation,
            ssl_server_algorithm=ssl_server_algorithm,
            ssl_server_cipher_suites=ssl_server_cipher_suites,
            ssl_pfs=ssl_pfs,
            ssl_min_version=ssl_min_version,
            ssl_max_version=ssl_max_version,
            ssl_server_min_version=ssl_server_min_version,
            ssl_server_max_version=ssl_server_max_version,
            ssl_accept_ffdhe_groups=ssl_accept_ffdhe_groups,
            ssl_send_empty_frags=ssl_send_empty_frags,
            ssl_client_fallback=ssl_client_fallback,
            ssl_client_renegotiation=ssl_client_renegotiation,
            ssl_client_session_state_type=ssl_client_session_state_type,
            ssl_client_session_state_timeout=ssl_client_session_state_timeout,
            ssl_client_session_state_max=ssl_client_session_state_max,
            ssl_client_rekey_count=ssl_client_rekey_count,
            ssl_server_session_state_type=ssl_server_session_state_type,
            ssl_server_session_state_timeout=ssl_server_session_state_timeout,
            ssl_server_session_state_max=ssl_server_session_state_max,
            ssl_http_location_conversion=ssl_http_location_conversion,
            ssl_http_match_host=ssl_http_match_host,
            ssl_hpkp=ssl_hpkp,
            ssl_hpkp_primary=ssl_hpkp_primary,
            ssl_hpkp_backup=ssl_hpkp_backup,
            ssl_hpkp_age=ssl_hpkp_age,
            ssl_hpkp_report_uri=ssl_hpkp_report_uri,
            ssl_hpkp_include_subdomains=ssl_hpkp_include_subdomains,
            ssl_hsts=ssl_hsts,
            ssl_hsts_age=ssl_hsts_age,
            ssl_hsts_include_subdomains=ssl_hsts_include_subdomains,
            monitor=monitor,
            max_embryonic_connections=max_embryonic_connections,
            embedded_ipv4_address=embedded_ipv4_address,
            ipv4_mappedip=ipv4_mappedip,
            ipv4_mappedport=ipv4_mappedport,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.vip6 import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/firewall/vip6",
            )

        endpoint = "/firewall/vip6"
        return self._client.post(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        name: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Delete firewall/vip6 object.

        Configure virtual IP for IPv6.

        Args:
            name: Primary key identifier
            vdom: Virtual domain name
            raw_json: If True, return raw API response
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is not provided

        Examples:
            >>> # Delete specific object
            >>> result = fgt.api.cmdb.firewall_vip6.delete(name=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not name:
            raise ValueError("name is required for DELETE")
        endpoint = "/firewall/vip6/" + str(name)

        return self._client.delete(
            "cmdb", endpoint, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        name: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if firewall/vip6 object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            name: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.firewall_vip6.exists(name=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.firewall_vip6.exists(name=1):
            ...     fgt.api.cmdb.firewall_vip6.delete(name=1)

        See Also:
            - get(): Retrieve full object data
            - set(): Create or update automatically based on existence
        """
        try:
            response = self.get(name=name, vdom=vdom, raw_json=True)
            
            if isinstance(response, dict):
                # Use helper function to check success
                return is_success(response)
            else:
                async def _check() -> bool:
                    r = await response
                    return is_success(r)
                return _check()
        except Exception:
            # Resource not found or other error - return False
            return False


    def set(
        self,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create or update firewall/vip6 object (intelligent operation).

        Automatically determines whether to create (POST) or update (PUT) based on
        whether the resource exists. Requires the primary key (name) in the payload.

        Args:
            payload_dict: Resource data including name (primary key)
            vdom: Virtual domain name
            **kwargs: Additional parameters passed to PUT or POST

        Returns:
            API response dictionary

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Intelligent create or update - no need to check exists()
            >>> payload = {
            ...     "name": 1,
            ...     "field1": "value1",
            ...     "field2": "value2",
            ... }
            >>> result = fgt.api.cmdb.firewall_vip6.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.firewall_vip6.set(payload_dict=obj_data)
            >>> # Safely applies configuration regardless of current state

        Note:
            This method internally calls exists() then either post() or put().
            For performance-critical code with known state, call post() or put() directly.

        See Also:
            - post(): Create new object
            - put(): Update existing object
            - exists(): Check existence manually
        """
        if payload_dict is None:
            payload_dict = {}
        
        mkey_value = payload_dict.get("name")
        if not mkey_value:
            raise ValueError("name is required in payload_dict for set()")
        
        # Check if resource exists
        if self.exists(name=mkey_value, vdom=vdom):
            # Update existing resource
            return self.put(payload_dict=payload_dict, vdom=vdom, **kwargs)
        else:
            # Create new resource
            return self.post(payload_dict=payload_dict, vdom=vdom, **kwargs)


