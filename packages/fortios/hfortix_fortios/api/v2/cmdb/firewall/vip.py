"""
FortiOS CMDB - Firewall vip

Configuration endpoint for managing cmdb firewall/vip objects.

API Endpoints:
    GET    /cmdb/firewall/vip
    POST   /cmdb/firewall/vip
    PUT    /cmdb/firewall/vip/{identifier}
    DELETE /cmdb/firewall/vip/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.firewall_vip.get()

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


class Vip:
    """Vip Operations."""

    def __init__(self, client: "IHTTPClient"):
        """Initialize Vip endpoint."""
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
        Retrieve firewall/vip configuration.

        Configure virtual IP for IPv4.

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
            >>> # Get all firewall/vip objects
            >>> result = fgt.api.cmdb.firewall_vip.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific firewall/vip by name
            >>> result = fgt.api.cmdb.firewall_vip.get(name=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.firewall_vip.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.firewall_vip.get(action="schema")

        See Also:
            - post(): Create new firewall/vip object
            - put(): Update existing firewall/vip object
            - delete(): Remove firewall/vip object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = "/firewall/vip/" + str(name)
        else:
            endpoint = "/firewall/vip"
        
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
        server_type: str | None = None,
        dns_mapping_ttl: int | None = None,
        ldb_method: str | None = None,
        src_filter: str | list | None = None,
        src_vip_filter: str | None = None,
        service: str | list | None = None,
        extip: str | None = None,
        extaddr: str | list | None = None,
        h2_support: str | None = None,
        h3_support: str | None = None,
        quic: str | None = None,
        nat44: str | None = None,
        nat46: str | None = None,
        add_nat46_route: str | None = None,
        mappedip: str | list | None = None,
        mapped_addr: str | None = None,
        extintf: str | None = None,
        arp_reply: str | None = None,
        http_redirect: str | None = None,
        persistence: str | None = None,
        nat_source_vip: str | None = None,
        portforward: str | None = None,
        status: str | None = None,
        protocol: str | None = None,
        extport: str | None = None,
        mappedport: str | None = None,
        gratuitous_arp_interval: int | None = None,
        srcintf_filter: str | list | None = None,
        portmapping_type: str | None = None,
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
        http_multiplex_ttl: int | None = None,
        http_multiplex_max_request: int | None = None,
        http_multiplex_max_concurrent_request: int | None = None,
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
        ssl_server_renegotiation: str | None = None,
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
        color: int | None = None,
        ipv6_mappedip: str | None = None,
        ipv6_mappedport: str | None = None,
        one_click_gslb_server: str | None = None,
        gslb_hostname: str | None = None,
        gslb_domain_name: str | None = None,
        gslb_public_ips: str | list | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing firewall/vip object.

        Configure virtual IP for IPv4.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            name: Virtual IP name.
            id: Custom defined ID.
            uuid: Universally Unique Identifier (UUID; automatically assigned but can be manually reset).
            comment: Comment.
            type: Configure a static NAT, load balance, server load balance, access proxy, DNS translation, or FQDN VIP.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.firewall_vip.put(
            ...     name=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.firewall_vip.put(payload_dict=payload)

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
            server_type=server_type,
            dns_mapping_ttl=dns_mapping_ttl,
            ldb_method=ldb_method,
            src_filter=src_filter,
            src_vip_filter=src_vip_filter,
            service=service,
            extip=extip,
            extaddr=extaddr,
            h2_support=h2_support,
            h3_support=h3_support,
            quic=quic,
            nat44=nat44,
            nat46=nat46,
            add_nat46_route=add_nat46_route,
            mappedip=mappedip,
            mapped_addr=mapped_addr,
            extintf=extintf,
            arp_reply=arp_reply,
            http_redirect=http_redirect,
            persistence=persistence,
            nat_source_vip=nat_source_vip,
            portforward=portforward,
            status=status,
            protocol=protocol,
            extport=extport,
            mappedport=mappedport,
            gratuitous_arp_interval=gratuitous_arp_interval,
            srcintf_filter=srcintf_filter,
            portmapping_type=portmapping_type,
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
            http_multiplex_ttl=http_multiplex_ttl,
            http_multiplex_max_request=http_multiplex_max_request,
            http_multiplex_max_concurrent_request=http_multiplex_max_concurrent_request,
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
            ssl_server_renegotiation=ssl_server_renegotiation,
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
            color=color,
            ipv6_mappedip=ipv6_mappedip,
            ipv6_mappedport=ipv6_mappedport,
            one_click_gslb_server=one_click_gslb_server,
            gslb_hostname=gslb_hostname,
            gslb_domain_name=gslb_domain_name,
            gslb_public_ips=gslb_public_ips,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.vip import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/firewall/vip",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = "/firewall/vip/" + str(name_value)

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
        server_type: str | None = None,
        dns_mapping_ttl: int | None = None,
        ldb_method: str | None = None,
        src_filter: str | list | None = None,
        src_vip_filter: str | None = None,
        service: str | list | None = None,
        extip: str | None = None,
        extaddr: str | list | None = None,
        h2_support: str | None = None,
        h3_support: str | None = None,
        quic: str | None = None,
        nat44: str | None = None,
        nat46: str | None = None,
        add_nat46_route: str | None = None,
        mappedip: str | list | None = None,
        mapped_addr: str | None = None,
        extintf: str | None = None,
        arp_reply: str | None = None,
        http_redirect: str | None = None,
        persistence: str | None = None,
        nat_source_vip: str | None = None,
        portforward: str | None = None,
        status: str | None = None,
        protocol: str | None = None,
        extport: str | None = None,
        mappedport: str | None = None,
        gratuitous_arp_interval: int | None = None,
        srcintf_filter: str | list | None = None,
        portmapping_type: str | None = None,
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
        http_multiplex_ttl: int | None = None,
        http_multiplex_max_request: int | None = None,
        http_multiplex_max_concurrent_request: int | None = None,
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
        ssl_server_renegotiation: str | None = None,
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
        color: int | None = None,
        ipv6_mappedip: str | None = None,
        ipv6_mappedport: str | None = None,
        one_click_gslb_server: str | None = None,
        gslb_hostname: str | None = None,
        gslb_domain_name: str | None = None,
        gslb_public_ips: str | list | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create new firewall/vip object.

        Configure virtual IP for IPv4.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            name: Virtual IP name.
            id: Custom defined ID.
            uuid: Universally Unique Identifier (UUID; automatically assigned but can be manually reset).
            comment: Comment.
            type: Configure a static NAT, load balance, server load balance, access proxy, DNS translation, or FQDN VIP.
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            raw_json: If True, return raw API response without processing.
            **kwargs: Additional parameters

        Returns:
            API response dict containing created object with assigned name.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.firewall_vip.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created name: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = Vip.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.firewall_vip.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(Vip.required_fields()) }}
            
            Use Vip.help('field_name') to get field details.

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
            server_type=server_type,
            dns_mapping_ttl=dns_mapping_ttl,
            ldb_method=ldb_method,
            src_filter=src_filter,
            src_vip_filter=src_vip_filter,
            service=service,
            extip=extip,
            extaddr=extaddr,
            h2_support=h2_support,
            h3_support=h3_support,
            quic=quic,
            nat44=nat44,
            nat46=nat46,
            add_nat46_route=add_nat46_route,
            mappedip=mappedip,
            mapped_addr=mapped_addr,
            extintf=extintf,
            arp_reply=arp_reply,
            http_redirect=http_redirect,
            persistence=persistence,
            nat_source_vip=nat_source_vip,
            portforward=portforward,
            status=status,
            protocol=protocol,
            extport=extport,
            mappedport=mappedport,
            gratuitous_arp_interval=gratuitous_arp_interval,
            srcintf_filter=srcintf_filter,
            portmapping_type=portmapping_type,
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
            http_multiplex_ttl=http_multiplex_ttl,
            http_multiplex_max_request=http_multiplex_max_request,
            http_multiplex_max_concurrent_request=http_multiplex_max_concurrent_request,
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
            ssl_server_renegotiation=ssl_server_renegotiation,
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
            color=color,
            ipv6_mappedip=ipv6_mappedip,
            ipv6_mappedport=ipv6_mappedport,
            one_click_gslb_server=one_click_gslb_server,
            gslb_hostname=gslb_hostname,
            gslb_domain_name=gslb_domain_name,
            gslb_public_ips=gslb_public_ips,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.vip import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/firewall/vip",
            )

        endpoint = "/firewall/vip"
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
        Delete firewall/vip object.

        Configure virtual IP for IPv4.

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
            >>> result = fgt.api.cmdb.firewall_vip.delete(name=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not name:
            raise ValueError("name is required for DELETE")
        endpoint = "/firewall/vip/" + str(name)

        return self._client.delete(
            "cmdb", endpoint, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        name: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if firewall/vip object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            name: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.firewall_vip.exists(name=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.firewall_vip.exists(name=1):
            ...     fgt.api.cmdb.firewall_vip.delete(name=1)

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
        Create or update firewall/vip object (intelligent operation).

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
            >>> result = fgt.api.cmdb.firewall_vip.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.firewall_vip.set(payload_dict=obj_data)
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

    # ========================================================================
    # Metadata Helper Methods
    # Provide easy access to schema metadata without separate imports
    # ========================================================================

    @staticmethod
    def help(field_name: str | None = None) -> str:
        """
        Get help text for endpoint or specific field.

        Args:
            field_name: Optional field name to get help for. If None, shows endpoint help.

        Returns:
            Formatted help text

        Examples:
            >>> # Get endpoint information
            >>> print(Vip.help())
            
            >>> # Get field information
            >>> print(Vip.help("name"))
        """
        from ._helpers.vip import (
            get_schema_info,
            get_field_metadata,
        )

        if field_name is None:
            # Endpoint help
            info = get_schema_info()
            lines = [
                f"Endpoint: {info['endpoint']}",
                f"Category: {info['category']}",
                f"Help: {info.get('help', 'N/A')}",
                "",
                f"Total Fields: {info['total_fields']}",
                f"Required Fields: {info['required_fields_count']}",
                f"Fields with Defaults: {info['fields_with_defaults_count']}",
            ]
            if 'mkey' in info:
                lines.append(f"\nPrimary Key: {info['mkey']} ({info['mkey_type']})")
            return "\n".join(lines)
        
        # Field help
        meta = get_field_metadata(field_name)
        if meta is None:
            return f"Unknown field: {field_name}"

        lines = [
            f"Field: {meta['name']}",
            f"Type: {meta['type']}",
        ]
        if 'description' in meta:
            lines.append(f"Description: {meta['description']}")
        lines.append(f"Required: {'Yes' if meta.get('required', False) else 'No'}")
        if 'default' in meta:
            lines.append(f"Default: {meta['default']}")
        if 'options' in meta:
            lines.append(f"Options: {', '.join(meta['options'])}")
        if 'constraints' in meta:
            constraints = meta['constraints']
            if 'min' in constraints or 'max' in constraints:
                min_val = constraints.get('min', '?')
                max_val = constraints.get('max', '?')
                lines.append(f"Range: {min_val} - {max_val}")
            if 'max_length' in constraints:
                lines.append(f"Max Length: {constraints['max_length']}")

        return "\n".join(lines)

    @staticmethod
    def fields(detailed: bool = False) -> Union[list[str], dict[str, dict]]:
        """
        Get list of all field names or detailed field information.

        Args:
            detailed: If True, return dict with field metadata

        Returns:
            List of field names or dict of field metadata

        Examples:
            >>> # Simple list
            >>> fields = Vip.fields()
            >>> print(f"Available fields: {len(fields)}")
            
            >>> # Detailed info
            >>> fields = Vip.fields(detailed=True)
            >>> for name, meta in fields.items():
            ...     print(f"{name}: {meta['type']}")
        """
        from ._helpers.vip import get_all_fields, get_field_metadata

        field_names = get_all_fields()

        if not detailed:
            return field_names

        # Build detailed dict
        detailed_fields = {}
        for fname in field_names:
            meta = get_field_metadata(fname)
            if meta:
                detailed_fields[fname] = meta

        return detailed_fields

    @staticmethod
    def field_info(field_name: str) -> dict[str, Any] | None:
        """
        Get complete metadata for a specific field.

        Args:
            field_name: Name of the field

        Returns:
            Field metadata dict or None if field doesn't exist

        Examples:
            >>> info = Vip.field_info("name")
            >>> print(f"Type: {info['type']}")
            >>> if 'options' in info:
            ...     print(f"Options: {info['options']}")
        """
        from ._helpers.vip import get_field_metadata

        return get_field_metadata(field_name)

    @staticmethod
    def validate_field(field_name: str, value: Any) -> tuple[bool, str | None]:
        """
        Validate a field value against its constraints.

        Args:
            field_name: Name of the field
            value: Value to validate

        Returns:
            Tuple of (is_valid, error_message)

        Examples:
            >>> is_valid, error = Vip.validate_field("name", "test")
            >>> if not is_valid:
            ...     print(f"Validation error: {error}")
        """
        from ._helpers.vip import validate_field_value

        return validate_field_value(field_name, value)

    @staticmethod
    def required_fields() -> list[str]:
        """
        Get list of required field names.

        Note: Due to FortiOS schema quirks, some fields may be conditionally required.
        Always test with the actual API for authoritative requirements.

        Returns:
            List of required field names

        Examples:
            >>> required = Vip.required_fields()
            >>> print(f"Required fields: {', '.join(required)}")
        """
        from ._helpers.vip import REQUIRED_FIELDS

        return REQUIRED_FIELDS.copy()

    @staticmethod
    def defaults() -> dict[str, Any]:
        """
        Get all fields with default values.

        Returns:
            Dict mapping field names to default values

        Examples:
            >>> defaults = Vip.defaults()
            >>> print(f"Fields with defaults: {len(defaults)}")
            >>> # Use as starting point for payload
            >>> payload = defaults.copy()
            >>> payload['name'] = 'my-custom-name'
        """
        from ._helpers.vip import FIELDS_WITH_DEFAULTS

        return FIELDS_WITH_DEFAULTS.copy()

    @staticmethod
    def schema() -> dict[str, Any]:
        """
        Get complete schema information for this endpoint.

        Returns:
            Schema metadata dict containing endpoint info, field counts, and primary key

        Examples:
            >>> schema = Vip.schema()
            >>> print(f"Endpoint: {schema['endpoint']}")
            >>> print(f"Total fields: {schema['total_fields']}")
            >>> print(f"Primary key: {schema.get('mkey', 'N/A')}")
        """
        from ._helpers.vip import get_schema_info

        return get_schema_info()
