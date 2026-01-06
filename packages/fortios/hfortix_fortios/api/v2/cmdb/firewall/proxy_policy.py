"""
FortiOS CMDB - Firewall proxy_policy

Configuration endpoint for managing cmdb firewall/proxy_policy objects.

API Endpoints:
    GET    /cmdb/firewall/proxy_policy
    POST   /cmdb/firewall/proxy_policy
    PUT    /cmdb/firewall/proxy_policy/{identifier}
    DELETE /cmdb/firewall/proxy_policy/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.firewall_proxy_policy.get()

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


class ProxyPolicy(MetadataMixin):
    """ProxyPolicy Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "proxy_policy"
    
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
        """Initialize ProxyPolicy endpoint."""
        self._client = client

    def get(
        self,
        policyid: int | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve firewall/proxy_policy configuration.

        Configure proxy policies.

        Args:
            policyid: Integer identifier to retrieve specific object.
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
            >>> # Get all firewall/proxy_policy objects
            >>> result = fgt.api.cmdb.firewall_proxy_policy.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific firewall/proxy_policy by policyid
            >>> result = fgt.api.cmdb.firewall_proxy_policy.get(policyid=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.firewall_proxy_policy.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.firewall_proxy_policy.get(action="schema")

        See Also:
            - post(): Create new firewall/proxy_policy object
            - put(): Update existing firewall/proxy_policy object
            - delete(): Remove firewall/proxy_policy object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if policyid:
            endpoint = "/firewall/proxy-policy/" + str(policyid)
        else:
            endpoint = "/firewall/proxy-policy"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        uuid: str | None = None,
        policyid: int | None = None,
        name: str | None = None,
        proxy: Literal["explicit-web", "transparent-web", "ftp", "ssh", "ssh-tunnel", "access-proxy", "ztna-proxy", "wanopt"] | None = None,
        access_proxy: str | list | None = None,
        access_proxy6: str | list | None = None,
        ztna_proxy: str | list | None = None,
        srcintf: str | list | None = None,
        dstintf: str | list | None = None,
        srcaddr: str | list | None = None,
        poolname: str | list | None = None,
        poolname6: str | list | None = None,
        dstaddr: str | list | None = None,
        ztna_ems_tag: str | list | None = None,
        ztna_tags_match_logic: Literal["or", "and"] | None = None,
        device_ownership: Literal["enable", "disable"] | None = None,
        url_risk: str | list | None = None,
        internet_service: Literal["enable", "disable"] | None = None,
        internet_service_negate: Literal["enable", "disable"] | None = None,
        internet_service_name: str | list | None = None,
        internet_service_group: str | list | None = None,
        internet_service_custom: str | list | None = None,
        internet_service_custom_group: str | list | None = None,
        internet_service_fortiguard: str | list | None = None,
        internet_service6: Literal["enable", "disable"] | None = None,
        internet_service6_negate: Literal["enable", "disable"] | None = None,
        internet_service6_name: str | list | None = None,
        internet_service6_group: str | list | None = None,
        internet_service6_custom: str | list | None = None,
        internet_service6_custom_group: str | list | None = None,
        internet_service6_fortiguard: str | list | None = None,
        service: str | list | None = None,
        srcaddr_negate: Literal["enable", "disable"] | None = None,
        dstaddr_negate: Literal["enable", "disable"] | None = None,
        ztna_ems_tag_negate: Literal["enable", "disable"] | None = None,
        service_negate: Literal["enable", "disable"] | None = None,
        action: Literal["accept", "deny", "redirect", "isolate"] | None = None,
        status: Literal["enable", "disable"] | None = None,
        schedule: str | None = None,
        logtraffic: Literal["all", "utm", "disable"] | None = None,
        session_ttl: int | None = None,
        srcaddr6: str | list | None = None,
        dstaddr6: str | list | None = None,
        groups: str | list | None = None,
        users: str | list | None = None,
        http_tunnel_auth: Literal["enable", "disable"] | None = None,
        ssh_policy_redirect: Literal["enable", "disable"] | None = None,
        webproxy_forward_server: str | None = None,
        isolator_server: str | None = None,
        webproxy_profile: str | None = None,
        transparent: Literal["enable", "disable"] | None = None,
        webcache: Literal["enable", "disable"] | None = None,
        webcache_https: Literal["disable", "enable"] | None = None,
        disclaimer: Literal["disable", "domain", "policy", "user"] | None = None,
        utm_status: Literal["enable", "disable"] | None = None,
        profile_type: Literal["single", "group"] | None = None,
        profile_group: str | None = None,
        profile_protocol_options: str | None = None,
        ssl_ssh_profile: str | None = None,
        av_profile: str | None = None,
        webfilter_profile: str | None = None,
        dnsfilter_profile: str | None = None,
        emailfilter_profile: str | None = None,
        dlp_profile: str | None = None,
        file_filter_profile: str | None = None,
        ips_sensor: str | None = None,
        application_list: str | None = None,
        ips_voip_filter: str | None = None,
        sctp_filter_profile: str | None = None,
        icap_profile: str | None = None,
        videofilter_profile: str | None = None,
        waf_profile: str | None = None,
        ssh_filter_profile: str | None = None,
        casb_profile: str | None = None,
        replacemsg_override_group: str | None = None,
        logtraffic_start: Literal["enable", "disable"] | None = None,
        log_http_transaction: Literal["enable", "disable"] | None = None,
        comments: str | None = None,
        block_notification: Literal["enable", "disable"] | None = None,
        redirect_url: str | None = None,
        https_sub_category: Literal["enable", "disable"] | None = None,
        decrypted_traffic_mirror: str | None = None,
        detect_https_in_http_request: Literal["enable", "disable"] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing firewall/proxy_policy object.

        Configure proxy policies.

        Args:
            payload_dict: Object data as dict. Must include policyid (primary key).
            uuid: Universally Unique Identifier (UUID; automatically assigned but can be manually reset).
            policyid: Policy ID.
            name: Policy name.
            proxy: Type of explicit proxy.
            access_proxy: IPv4 access proxy.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If policyid is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.firewall_proxy_policy.put(
            ...     policyid=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "policyid": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.firewall_proxy_policy.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            uuid=uuid,
            policyid=policyid,
            name=name,
            proxy=proxy,
            access_proxy=access_proxy,
            access_proxy6=access_proxy6,
            ztna_proxy=ztna_proxy,
            srcintf=srcintf,
            dstintf=dstintf,
            srcaddr=srcaddr,
            poolname=poolname,
            poolname6=poolname6,
            dstaddr=dstaddr,
            ztna_ems_tag=ztna_ems_tag,
            ztna_tags_match_logic=ztna_tags_match_logic,
            device_ownership=device_ownership,
            url_risk=url_risk,
            internet_service=internet_service,
            internet_service_negate=internet_service_negate,
            internet_service_name=internet_service_name,
            internet_service_group=internet_service_group,
            internet_service_custom=internet_service_custom,
            internet_service_custom_group=internet_service_custom_group,
            internet_service_fortiguard=internet_service_fortiguard,
            internet_service6=internet_service6,
            internet_service6_negate=internet_service6_negate,
            internet_service6_name=internet_service6_name,
            internet_service6_group=internet_service6_group,
            internet_service6_custom=internet_service6_custom,
            internet_service6_custom_group=internet_service6_custom_group,
            internet_service6_fortiguard=internet_service6_fortiguard,
            service=service,
            srcaddr_negate=srcaddr_negate,
            dstaddr_negate=dstaddr_negate,
            ztna_ems_tag_negate=ztna_ems_tag_negate,
            service_negate=service_negate,
            action=action,
            status=status,
            schedule=schedule,
            logtraffic=logtraffic,
            session_ttl=session_ttl,
            srcaddr6=srcaddr6,
            dstaddr6=dstaddr6,
            groups=groups,
            users=users,
            http_tunnel_auth=http_tunnel_auth,
            ssh_policy_redirect=ssh_policy_redirect,
            webproxy_forward_server=webproxy_forward_server,
            isolator_server=isolator_server,
            webproxy_profile=webproxy_profile,
            transparent=transparent,
            webcache=webcache,
            webcache_https=webcache_https,
            disclaimer=disclaimer,
            utm_status=utm_status,
            profile_type=profile_type,
            profile_group=profile_group,
            profile_protocol_options=profile_protocol_options,
            ssl_ssh_profile=ssl_ssh_profile,
            av_profile=av_profile,
            webfilter_profile=webfilter_profile,
            dnsfilter_profile=dnsfilter_profile,
            emailfilter_profile=emailfilter_profile,
            dlp_profile=dlp_profile,
            file_filter_profile=file_filter_profile,
            ips_sensor=ips_sensor,
            application_list=application_list,
            ips_voip_filter=ips_voip_filter,
            sctp_filter_profile=sctp_filter_profile,
            icap_profile=icap_profile,
            videofilter_profile=videofilter_profile,
            waf_profile=waf_profile,
            ssh_filter_profile=ssh_filter_profile,
            casb_profile=casb_profile,
            replacemsg_override_group=replacemsg_override_group,
            logtraffic_start=logtraffic_start,
            log_http_transaction=log_http_transaction,
            comments=comments,
            block_notification=block_notification,
            redirect_url=redirect_url,
            https_sub_category=https_sub_category,
            decrypted_traffic_mirror=decrypted_traffic_mirror,
            detect_https_in_http_request=detect_https_in_http_request,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.proxy_policy import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/firewall/proxy_policy",
            )
        
        policyid_value = payload_data.get("policyid")
        if not policyid_value:
            raise ValueError("policyid is required for PUT")
        endpoint = "/firewall/proxy-policy/" + str(policyid_value)

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        uuid: str | None = None,
        policyid: int | None = None,
        name: str | None = None,
        proxy: Literal["explicit-web", "transparent-web", "ftp", "ssh", "ssh-tunnel", "access-proxy", "ztna-proxy", "wanopt"] | None = None,
        access_proxy: str | list | None = None,
        access_proxy6: str | list | None = None,
        ztna_proxy: str | list | None = None,
        srcintf: str | list | None = None,
        dstintf: str | list | None = None,
        srcaddr: str | list | None = None,
        poolname: str | list | None = None,
        poolname6: str | list | None = None,
        dstaddr: str | list | None = None,
        ztna_ems_tag: str | list | None = None,
        ztna_tags_match_logic: Literal["or", "and"] | None = None,
        device_ownership: Literal["enable", "disable"] | None = None,
        url_risk: str | list | None = None,
        internet_service: Literal["enable", "disable"] | None = None,
        internet_service_negate: Literal["enable", "disable"] | None = None,
        internet_service_name: str | list | None = None,
        internet_service_group: str | list | None = None,
        internet_service_custom: str | list | None = None,
        internet_service_custom_group: str | list | None = None,
        internet_service_fortiguard: str | list | None = None,
        internet_service6: Literal["enable", "disable"] | None = None,
        internet_service6_negate: Literal["enable", "disable"] | None = None,
        internet_service6_name: str | list | None = None,
        internet_service6_group: str | list | None = None,
        internet_service6_custom: str | list | None = None,
        internet_service6_custom_group: str | list | None = None,
        internet_service6_fortiguard: str | list | None = None,
        service: str | list | None = None,
        srcaddr_negate: Literal["enable", "disable"] | None = None,
        dstaddr_negate: Literal["enable", "disable"] | None = None,
        ztna_ems_tag_negate: Literal["enable", "disable"] | None = None,
        service_negate: Literal["enable", "disable"] | None = None,
        action: Literal["accept", "deny", "redirect", "isolate"] | None = None,
        status: Literal["enable", "disable"] | None = None,
        schedule: str | None = None,
        logtraffic: Literal["all", "utm", "disable"] | None = None,
        session_ttl: int | None = None,
        srcaddr6: str | list | None = None,
        dstaddr6: str | list | None = None,
        groups: str | list | None = None,
        users: str | list | None = None,
        http_tunnel_auth: Literal["enable", "disable"] | None = None,
        ssh_policy_redirect: Literal["enable", "disable"] | None = None,
        webproxy_forward_server: str | None = None,
        isolator_server: str | None = None,
        webproxy_profile: str | None = None,
        transparent: Literal["enable", "disable"] | None = None,
        webcache: Literal["enable", "disable"] | None = None,
        webcache_https: Literal["disable", "enable"] | None = None,
        disclaimer: Literal["disable", "domain", "policy", "user"] | None = None,
        utm_status: Literal["enable", "disable"] | None = None,
        profile_type: Literal["single", "group"] | None = None,
        profile_group: str | None = None,
        profile_protocol_options: str | None = None,
        ssl_ssh_profile: str | None = None,
        av_profile: str | None = None,
        webfilter_profile: str | None = None,
        dnsfilter_profile: str | None = None,
        emailfilter_profile: str | None = None,
        dlp_profile: str | None = None,
        file_filter_profile: str | None = None,
        ips_sensor: str | None = None,
        application_list: str | None = None,
        ips_voip_filter: str | None = None,
        sctp_filter_profile: str | None = None,
        icap_profile: str | None = None,
        videofilter_profile: str | None = None,
        waf_profile: str | None = None,
        ssh_filter_profile: str | None = None,
        casb_profile: str | None = None,
        replacemsg_override_group: str | None = None,
        logtraffic_start: Literal["enable", "disable"] | None = None,
        log_http_transaction: Literal["enable", "disable"] | None = None,
        comments: str | None = None,
        block_notification: Literal["enable", "disable"] | None = None,
        redirect_url: str | None = None,
        https_sub_category: Literal["enable", "disable"] | None = None,
        decrypted_traffic_mirror: str | None = None,
        detect_https_in_http_request: Literal["enable", "disable"] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create new firewall/proxy_policy object.

        Configure proxy policies.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            uuid: Universally Unique Identifier (UUID; automatically assigned but can be manually reset).
            policyid: Policy ID.
            name: Policy name.
            proxy: Type of explicit proxy.
            access_proxy: IPv4 access proxy.
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            raw_json: If True, return raw API response without processing.
            **kwargs: Additional parameters

        Returns:
            API response dict containing created object with assigned policyid.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.firewall_proxy_policy.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created policyid: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = ProxyPolicy.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.firewall_proxy_policy.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(ProxyPolicy.required_fields()) }}
            
            Use ProxyPolicy.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            uuid=uuid,
            policyid=policyid,
            name=name,
            proxy=proxy,
            access_proxy=access_proxy,
            access_proxy6=access_proxy6,
            ztna_proxy=ztna_proxy,
            srcintf=srcintf,
            dstintf=dstintf,
            srcaddr=srcaddr,
            poolname=poolname,
            poolname6=poolname6,
            dstaddr=dstaddr,
            ztna_ems_tag=ztna_ems_tag,
            ztna_tags_match_logic=ztna_tags_match_logic,
            device_ownership=device_ownership,
            url_risk=url_risk,
            internet_service=internet_service,
            internet_service_negate=internet_service_negate,
            internet_service_name=internet_service_name,
            internet_service_group=internet_service_group,
            internet_service_custom=internet_service_custom,
            internet_service_custom_group=internet_service_custom_group,
            internet_service_fortiguard=internet_service_fortiguard,
            internet_service6=internet_service6,
            internet_service6_negate=internet_service6_negate,
            internet_service6_name=internet_service6_name,
            internet_service6_group=internet_service6_group,
            internet_service6_custom=internet_service6_custom,
            internet_service6_custom_group=internet_service6_custom_group,
            internet_service6_fortiguard=internet_service6_fortiguard,
            service=service,
            srcaddr_negate=srcaddr_negate,
            dstaddr_negate=dstaddr_negate,
            ztna_ems_tag_negate=ztna_ems_tag_negate,
            service_negate=service_negate,
            action=action,
            status=status,
            schedule=schedule,
            logtraffic=logtraffic,
            session_ttl=session_ttl,
            srcaddr6=srcaddr6,
            dstaddr6=dstaddr6,
            groups=groups,
            users=users,
            http_tunnel_auth=http_tunnel_auth,
            ssh_policy_redirect=ssh_policy_redirect,
            webproxy_forward_server=webproxy_forward_server,
            isolator_server=isolator_server,
            webproxy_profile=webproxy_profile,
            transparent=transparent,
            webcache=webcache,
            webcache_https=webcache_https,
            disclaimer=disclaimer,
            utm_status=utm_status,
            profile_type=profile_type,
            profile_group=profile_group,
            profile_protocol_options=profile_protocol_options,
            ssl_ssh_profile=ssl_ssh_profile,
            av_profile=av_profile,
            webfilter_profile=webfilter_profile,
            dnsfilter_profile=dnsfilter_profile,
            emailfilter_profile=emailfilter_profile,
            dlp_profile=dlp_profile,
            file_filter_profile=file_filter_profile,
            ips_sensor=ips_sensor,
            application_list=application_list,
            ips_voip_filter=ips_voip_filter,
            sctp_filter_profile=sctp_filter_profile,
            icap_profile=icap_profile,
            videofilter_profile=videofilter_profile,
            waf_profile=waf_profile,
            ssh_filter_profile=ssh_filter_profile,
            casb_profile=casb_profile,
            replacemsg_override_group=replacemsg_override_group,
            logtraffic_start=logtraffic_start,
            log_http_transaction=log_http_transaction,
            comments=comments,
            block_notification=block_notification,
            redirect_url=redirect_url,
            https_sub_category=https_sub_category,
            decrypted_traffic_mirror=decrypted_traffic_mirror,
            detect_https_in_http_request=detect_https_in_http_request,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.proxy_policy import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/firewall/proxy_policy",
            )

        endpoint = "/firewall/proxy-policy"
        return self._client.post(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        policyid: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Delete firewall/proxy_policy object.

        Configure proxy policies.

        Args:
            policyid: Primary key identifier
            vdom: Virtual domain name
            raw_json: If True, return raw API response
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If policyid is not provided

        Examples:
            >>> # Delete specific object
            >>> result = fgt.api.cmdb.firewall_proxy_policy.delete(policyid=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not policyid:
            raise ValueError("policyid is required for DELETE")
        endpoint = "/firewall/proxy-policy/" + str(policyid)

        return self._client.delete(
            "cmdb", endpoint, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        policyid: int,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if firewall/proxy_policy object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            policyid: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.firewall_proxy_policy.exists(policyid=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.firewall_proxy_policy.exists(policyid=1):
            ...     fgt.api.cmdb.firewall_proxy_policy.delete(policyid=1)

        See Also:
            - get(): Retrieve full object data
            - set(): Create or update automatically based on existence
        """
        # Try to fetch the object - 404 means it doesn't exist
        try:
            response = self.get(
                policyid=policyid,
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
        Create or update firewall/proxy_policy object (intelligent operation).

        Automatically determines whether to create (POST) or update (PUT) based on
        whether the resource exists. Requires the primary key (policyid) in the payload.

        Args:
            payload_dict: Resource data including policyid (primary key)
            vdom: Virtual domain name
            **kwargs: Additional parameters passed to PUT or POST

        Returns:
            API response dictionary

        Raises:
            ValueError: If policyid is missing from payload

        Examples:
            >>> # Intelligent create or update - no need to check exists()
            >>> payload = {
            ...     "policyid": 1,
            ...     "field1": "value1",
            ...     "field2": "value2",
            ... }
            >>> result = fgt.api.cmdb.firewall_proxy_policy.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.firewall_proxy_policy.set(payload_dict=obj_data)
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
        
        mkey_value = payload_dict.get("policyid")
        if not mkey_value:
            raise ValueError("policyid is required in payload_dict for set()")
        
        # Check if resource exists
        if self.exists(policyid=mkey_value, vdom=vdom):
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
        policyid: int,
        action: Literal["before", "after"],
        reference_policyid: int,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Move firewall/proxy_policy object to a new position.
        
        Reorders objects by moving one before or after another.
        
        Args:
            policyid: Identifier of object to move
            action: Move "before" or "after" reference object
            reference_policyid: Identifier of reference object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Move policy 100 before policy 50
            >>> fgt.api.cmdb.firewall_proxy_policy.move(
            ...     policyid=100,
            ...     action="before",
            ...     reference_policyid=50
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/firewall/proxy-policy",
            params={
                "policyid": policyid,
                "action": "move",
                action: reference_policyid,
                "vdom": vdom,
                **kwargs,
            },
        )

    # ========================================================================
    # Action: Clone
    # ========================================================================
    
    def clone(
        self,
        policyid: int,
        new_policyid: int,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Clone firewall/proxy_policy object.
        
        Creates a copy of an existing object with a new identifier.
        
        Args:
            policyid: Identifier of object to clone
            new_policyid: Identifier for the cloned object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Clone an existing object
            >>> fgt.api.cmdb.firewall_proxy_policy.clone(
            ...     policyid=1,
            ...     new_policyid=100
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/firewall/proxy-policy",
            params={
                "policyid": policyid,
                "new_policyid": new_policyid,
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
        policyid: int,
        vdom: str | bool | None = None,
    ) -> bool:
        """
        Check if firewall/proxy_policy object exists.
        
        Args:
            policyid: Identifier to check
            vdom: Virtual domain name
            
        Returns:
            True if object exists, False otherwise
            
        Example:
            >>> # Check before creating
            >>> if not fgt.api.cmdb.firewall_proxy_policy.exists(policyid=1):
            ...     fgt.api.cmdb.firewall_proxy_policy.post(payload_dict=data)
        """
        # Try to fetch the object - 404 means it doesn't exist
        try:
            response = self.get(
                policyid=policyid,
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

