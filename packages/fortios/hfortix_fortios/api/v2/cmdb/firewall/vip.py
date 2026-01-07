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

from typing import TYPE_CHECKING, Any, Union, Literal
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


class Vip(MetadataMixin):
    """Vip Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "vip"
    
    # ========================================================================
    # Capabilities (from schema metadata)
    # ========================================================================
    SUPPORTS_CREATE = True
    SUPPORTS_READ = True
    SUPPORTS_UPDATE = True
    SUPPORTS_DELETE = True
    SUPPORTS_MOVE = True
    SUPPORTS_CLONE = True
    SUPPORTS_FILTERING = True
    SUPPORTS_PAGINATION = True
    SUPPORTS_SEARCH = False
    SUPPORTS_SORTING = False

    def __init__(self, client: "IHTTPClient"):
        """Initialize Vip endpoint."""
        self._client = client

    def get(
        self,
        name: str | None = None,
        filter: list[str] | None = None,
        count: int | None = None,
        start: int | None = None,
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
            filter: List of filter expressions to limit results.
                Each filter uses format: "field==value" or "field!=value"
                Operators: ==, !=, =@ (contains), !@ (not contains), <=, <, >=, >
                Multiple filters use AND logic. For OR, use comma in single string.
                Example: ["name==test", "status==enable"] or ["name==test,name==prod"]
            count: Maximum number of entries to return (pagination).
            start: Starting entry index for pagination (0-based).
            payload_dict: Additional query parameters for advanced options:
                - datasource (bool): Include datasource information
                - with_meta (bool): Include metadata about each object
                - with_contents_hash (bool): Include checksum of object contents
                - format (list[str]): Property names to include (e.g., ["policyid", "srcintf"])
                - scope (str): Query scope - "global", "vdom", or "both"
                - action (str): Special actions - "schema", "default"
                See FortiOS REST API documentation for complete list.
            vdom: Virtual domain name. Use True for global, string for specific VDOM, None for default.
            raw_json: If True, return raw API response without processing.
            **kwargs: Additional query parameters passed directly to API.

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
            ...     filter=["name==test", "status==enable"]
            ... )
            
            >>> # Get with pagination
            >>> result = fgt.api.cmdb.firewall_vip.get(
            ...     start=0, count=100
            ... )
            
            >>> # Get schema information  
            >>> schema = fgt.api.cmdb.firewall_vip.get_schema()

        See Also:
            - post(): Create new firewall/vip object
            - put(): Update existing firewall/vip object
            - delete(): Remove firewall/vip object
            - exists(): Check if object exists
            - get_schema(): Get endpoint schema/metadata
        """
        params = payload_dict.copy() if payload_dict else {}
        
        # Add explicit query parameters
        if filter is not None:
            params["filter"] = filter
        if count is not None:
            params["count"] = count
        if start is not None:
            params["start"] = start
        
        if name:
            endpoint = "/firewall/vip/" + str(name)
        else:
            endpoint = "/firewall/vip"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def get_schema(
        self,
        vdom: str | None = None,
        format: str = "schema",
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Get schema/metadata for this endpoint.
        
        Returns the FortiOS schema definition including available fields,
        their types, required vs optional properties, enum values, nested
        structures, and default values.
        
        This queries the live firewall for its current schema, which may
        vary between FortiOS versions.
        
        Args:
            vdom: Virtual domain. None uses default VDOM.
            format: Schema format - "schema" (FortiOS native) or "json-schema" (JSON Schema standard).
                Defaults to "schema".
                
        Returns:
            Schema definition as dict. Returns Coroutine if using async client.
            
        Example:
            >>> # Get FortiOS native schema
            >>> schema = fgt.api.cmdb.firewall_vip.get_schema()
            >>> print(schema['results'])
            
            >>> # Get JSON Schema format (if supported)
            >>> json_schema = fgt.api.cmdb.firewall_vip.get_schema(format="json-schema")
        
        Note:
            Not all endpoints support all schema formats. The "schema" format
            is most widely supported.
        """
        return self.get(action=format, vdom=vdom)


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        name: str | None = None,
        id: int | None = None,
        uuid: str | None = None,
        comment: str | None = None,
        type: Literal["static-nat", "load-balance", "server-load-balance", "dns-translation", "fqdn", "access-proxy"] | None = None,
        server_type: Literal["http", "https", "imaps", "pop3s", "smtps", "ssl", "tcp", "udp", "ip"] | None = None,
        dns_mapping_ttl: int | None = None,
        ldb_method: Literal["static", "round-robin", "weighted", "least-session", "least-rtt", "first-alive", "http-host"] | None = None,
        src_filter: str | list | None = None,
        src_vip_filter: Literal["disable", "enable"] | None = None,
        service: str | list | None = None,
        extip: str | None = None,
        extaddr: str | list | None = None,
        h2_support: Literal["enable", "disable"] | None = None,
        h3_support: Literal["enable", "disable"] | None = None,
        quic: str | None = None,
        nat44: Literal["disable", "enable"] | None = None,
        nat46: Literal["disable", "enable"] | None = None,
        add_nat46_route: Literal["disable", "enable"] | None = None,
        mappedip: str | list | None = None,
        mapped_addr: str | None = None,
        extintf: str | None = None,
        arp_reply: Literal["disable", "enable"] | None = None,
        http_redirect: Literal["enable", "disable"] | None = None,
        persistence: Literal["none", "http-cookie", "ssl-session-id"] | None = None,
        nat_source_vip: Literal["disable", "enable"] | None = None,
        portforward: Literal["disable", "enable"] | None = None,
        status: Literal["disable", "enable"] | None = None,
        protocol: Literal["tcp", "udp", "sctp", "icmp"] | None = None,
        extport: str | None = None,
        mappedport: str | None = None,
        gratuitous_arp_interval: int | None = None,
        srcintf_filter: str | list | None = None,
        portmapping_type: Literal["1-to-1", "m-to-n"] | None = None,
        empty_cert_action: Literal["accept", "block", "accept-unmanageable"] | None = None,
        user_agent_detect: Literal["disable", "enable"] | None = None,
        client_cert: Literal["disable", "enable"] | None = None,
        realservers: str | list | None = None,
        http_cookie_domain_from_host: Literal["disable", "enable"] | None = None,
        http_cookie_domain: str | None = None,
        http_cookie_path: str | None = None,
        http_cookie_generation: int | None = None,
        http_cookie_age: int | None = None,
        http_cookie_share: Literal["disable", "same-ip"] | None = None,
        https_cookie_secure: Literal["disable", "enable"] | None = None,
        http_multiplex: Literal["enable", "disable"] | None = None,
        http_multiplex_ttl: int | None = None,
        http_multiplex_max_request: int | None = None,
        http_multiplex_max_concurrent_request: int | None = None,
        http_ip_header: Literal["enable", "disable"] | None = None,
        http_ip_header_name: str | None = None,
        outlook_web_access: Literal["disable", "enable"] | None = None,
        weblogic_server: Literal["disable", "enable"] | None = None,
        websphere_server: Literal["disable", "enable"] | None = None,
        ssl_mode: Literal["half", "full"] | None = None,
        ssl_certificate: str | list | None = None,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048", "3072", "4096"] | None = None,
        ssl_algorithm: Literal["high", "medium", "low", "custom"] | None = None,
        ssl_cipher_suites: str | list | None = None,
        ssl_server_algorithm: Literal["high", "medium", "low", "custom", "client"] | None = None,
        ssl_server_cipher_suites: str | list | None = None,
        ssl_pfs: Literal["require", "deny", "allow"] | None = None,
        ssl_min_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = None,
        ssl_max_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = None,
        ssl_server_min_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3", "client"] | None = None,
        ssl_server_max_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3", "client"] | None = None,
        ssl_accept_ffdhe_groups: Literal["enable", "disable"] | None = None,
        ssl_send_empty_frags: Literal["enable", "disable"] | None = None,
        ssl_client_fallback: Literal["disable", "enable"] | None = None,
        ssl_client_renegotiation: Literal["allow", "deny", "secure"] | None = None,
        ssl_client_session_state_type: Literal["disable", "time", "count", "both"] | None = None,
        ssl_client_session_state_timeout: int | None = None,
        ssl_client_session_state_max: int | None = None,
        ssl_client_rekey_count: int | None = None,
        ssl_server_renegotiation: Literal["enable", "disable"] | None = None,
        ssl_server_session_state_type: Literal["disable", "time", "count", "both"] | None = None,
        ssl_server_session_state_timeout: int | None = None,
        ssl_server_session_state_max: int | None = None,
        ssl_http_location_conversion: Literal["enable", "disable"] | None = None,
        ssl_http_match_host: Literal["enable", "disable"] | None = None,
        ssl_hpkp: Literal["disable", "enable", "report-only"] | None = None,
        ssl_hpkp_primary: str | None = None,
        ssl_hpkp_backup: str | None = None,
        ssl_hpkp_age: int | None = None,
        ssl_hpkp_report_uri: str | None = None,
        ssl_hpkp_include_subdomains: Literal["disable", "enable"] | None = None,
        ssl_hsts: Literal["disable", "enable"] | None = None,
        ssl_hsts_age: int | None = None,
        ssl_hsts_include_subdomains: Literal["disable", "enable"] | None = None,
        monitor: str | list | None = None,
        max_embryonic_connections: int | None = None,
        color: int | None = None,
        ipv6_mappedip: str | None = None,
        ipv6_mappedport: str | None = None,
        one_click_gslb_server: Literal["disable", "enable"] | None = None,
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
        type: Literal["static-nat", "load-balance", "server-load-balance", "dns-translation", "fqdn", "access-proxy"] | None = None,
        server_type: Literal["http", "https", "imaps", "pop3s", "smtps", "ssl", "tcp", "udp", "ip"] | None = None,
        dns_mapping_ttl: int | None = None,
        ldb_method: Literal["static", "round-robin", "weighted", "least-session", "least-rtt", "first-alive", "http-host"] | None = None,
        src_filter: str | list | None = None,
        src_vip_filter: Literal["disable", "enable"] | None = None,
        service: str | list | None = None,
        extip: str | None = None,
        extaddr: str | list | None = None,
        h2_support: Literal["enable", "disable"] | None = None,
        h3_support: Literal["enable", "disable"] | None = None,
        quic: str | None = None,
        nat44: Literal["disable", "enable"] | None = None,
        nat46: Literal["disable", "enable"] | None = None,
        add_nat46_route: Literal["disable", "enable"] | None = None,
        mappedip: str | list | None = None,
        mapped_addr: str | None = None,
        extintf: str | None = None,
        arp_reply: Literal["disable", "enable"] | None = None,
        http_redirect: Literal["enable", "disable"] | None = None,
        persistence: Literal["none", "http-cookie", "ssl-session-id"] | None = None,
        nat_source_vip: Literal["disable", "enable"] | None = None,
        portforward: Literal["disable", "enable"] | None = None,
        status: Literal["disable", "enable"] | None = None,
        protocol: Literal["tcp", "udp", "sctp", "icmp"] | None = None,
        extport: str | None = None,
        mappedport: str | None = None,
        gratuitous_arp_interval: int | None = None,
        srcintf_filter: str | list | None = None,
        portmapping_type: Literal["1-to-1", "m-to-n"] | None = None,
        empty_cert_action: Literal["accept", "block", "accept-unmanageable"] | None = None,
        user_agent_detect: Literal["disable", "enable"] | None = None,
        client_cert: Literal["disable", "enable"] | None = None,
        realservers: str | list | None = None,
        http_cookie_domain_from_host: Literal["disable", "enable"] | None = None,
        http_cookie_domain: str | None = None,
        http_cookie_path: str | None = None,
        http_cookie_generation: int | None = None,
        http_cookie_age: int | None = None,
        http_cookie_share: Literal["disable", "same-ip"] | None = None,
        https_cookie_secure: Literal["disable", "enable"] | None = None,
        http_multiplex: Literal["enable", "disable"] | None = None,
        http_multiplex_ttl: int | None = None,
        http_multiplex_max_request: int | None = None,
        http_multiplex_max_concurrent_request: int | None = None,
        http_ip_header: Literal["enable", "disable"] | None = None,
        http_ip_header_name: str | None = None,
        outlook_web_access: Literal["disable", "enable"] | None = None,
        weblogic_server: Literal["disable", "enable"] | None = None,
        websphere_server: Literal["disable", "enable"] | None = None,
        ssl_mode: Literal["half", "full"] | None = None,
        ssl_certificate: str | list | None = None,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048", "3072", "4096"] | None = None,
        ssl_algorithm: Literal["high", "medium", "low", "custom"] | None = None,
        ssl_cipher_suites: str | list | None = None,
        ssl_server_algorithm: Literal["high", "medium", "low", "custom", "client"] | None = None,
        ssl_server_cipher_suites: str | list | None = None,
        ssl_pfs: Literal["require", "deny", "allow"] | None = None,
        ssl_min_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = None,
        ssl_max_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = None,
        ssl_server_min_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3", "client"] | None = None,
        ssl_server_max_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3", "client"] | None = None,
        ssl_accept_ffdhe_groups: Literal["enable", "disable"] | None = None,
        ssl_send_empty_frags: Literal["enable", "disable"] | None = None,
        ssl_client_fallback: Literal["disable", "enable"] | None = None,
        ssl_client_renegotiation: Literal["allow", "deny", "secure"] | None = None,
        ssl_client_session_state_type: Literal["disable", "time", "count", "both"] | None = None,
        ssl_client_session_state_timeout: int | None = None,
        ssl_client_session_state_max: int | None = None,
        ssl_client_rekey_count: int | None = None,
        ssl_server_renegotiation: Literal["enable", "disable"] | None = None,
        ssl_server_session_state_type: Literal["disable", "time", "count", "both"] | None = None,
        ssl_server_session_state_timeout: int | None = None,
        ssl_server_session_state_max: int | None = None,
        ssl_http_location_conversion: Literal["enable", "disable"] | None = None,
        ssl_http_match_host: Literal["enable", "disable"] | None = None,
        ssl_hpkp: Literal["disable", "enable", "report-only"] | None = None,
        ssl_hpkp_primary: str | None = None,
        ssl_hpkp_backup: str | None = None,
        ssl_hpkp_age: int | None = None,
        ssl_hpkp_report_uri: str | None = None,
        ssl_hpkp_include_subdomains: Literal["disable", "enable"] | None = None,
        ssl_hsts: Literal["disable", "enable"] | None = None,
        ssl_hsts_age: int | None = None,
        ssl_hsts_include_subdomains: Literal["disable", "enable"] | None = None,
        monitor: str | list | None = None,
        max_embryonic_connections: int | None = None,
        color: int | None = None,
        ipv6_mappedip: str | None = None,
        ipv6_mappedport: str | None = None,
        one_click_gslb_server: Literal["disable", "enable"] | None = None,
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
        # Try to fetch the object - 404 means it doesn't exist
        try:
            response = self.get(
                name=name,
                vdom=vdom,
                raw_json=True
            )
            
            if isinstance(response, dict):
                # Synchronous response - check status
                return is_success(response)
            else:
                # Asynchronous response
                async def _check() -> bool:
                    r = await response
                    return is_success(r)
                return _check()
        except Exception as e:
            # 404 means object doesn't exist - return False
            # Any other error should be re-raised
            error_str = str(e)
            if '404' in error_str or 'Not Found' in error_str or 'ResourceNotFoundError' in str(type(e)):
                return False
            raise


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
    # Action: Move
    # ========================================================================
    
    def move(
        self,
        name: str,
        action: Literal["before", "after"],
        reference_name: str,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Move firewall/vip object to a new position.
        
        Reorders objects by moving one before or after another.
        
        Args:
            name: Identifier of object to move
            action: Move "before" or "after" reference object
            reference_name: Identifier of reference object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Move policy 100 before policy 50
            >>> fgt.api.cmdb.firewall_vip.move(
            ...     name=100,
            ...     action="before",
            ...     reference_name=50
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/firewall/vip",
            params={
                "name": name,
                "action": "move",
                action: reference_name,
                "vdom": vdom,
                **kwargs,
            },
        )

    # ========================================================================
    # Action: Clone
    # ========================================================================
    
    def clone(
        self,
        name: str,
        new_name: str,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Clone firewall/vip object.
        
        Creates a copy of an existing object with a new identifier.
        
        Args:
            name: Identifier of object to clone
            new_name: Identifier for the cloned object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Clone an existing object
            >>> fgt.api.cmdb.firewall_vip.clone(
            ...     name=1,
            ...     new_name=100
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/firewall/vip",
            params={
                "name": name,
                "new_name": new_name,
                "action": "clone",
                "vdom": vdom,
                **kwargs,
            },
        )

    # ========================================================================
    # Helper: Check Existence
    # ========================================================================
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = None,
    ) -> bool:
        """
        Check if firewall/vip object exists.
        
        Args:
            name: Identifier to check
            vdom: Virtual domain name
            
        Returns:
            True if object exists, False otherwise
            
        Example:
            >>> # Check before creating
            >>> if not fgt.api.cmdb.firewall_vip.exists(name=1):
            ...     fgt.api.cmdb.firewall_vip.post(payload_dict=data)
        """
        # Try to fetch the object - 404 means it doesn't exist
        try:
            response = self.get(
                name=name,
                vdom=vdom,
                raw_json=True
            )
            # Check if response indicates success
            return is_success(response)
        except Exception as e:
            # 404 means object doesn't exist - return False
            # Any other error should be re-raised
            error_str = str(e)
            if '404' in error_str or 'Not Found' in error_str or 'ResourceNotFoundError' in str(type(e)):
                return False
            raise

