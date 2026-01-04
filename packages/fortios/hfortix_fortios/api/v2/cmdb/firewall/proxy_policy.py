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

from typing import TYPE_CHECKING, Any, Union

if TYPE_CHECKING:
    from collections.abc import Coroutine
    from hfortix_core.http.interface import IHTTPClient

# Import helper functions from central _helpers module
from hfortix_fortios._helpers import (
    build_cmdb_payload,
    is_success,
)


class ProxyPolicy:
    """ProxyPolicy Operations."""

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
        proxy: str | None = None,
        access_proxy: str | list | None = None,
        access_proxy6: str | list | None = None,
        ztna_proxy: str | list | None = None,
        srcintf: str | list | None = None,
        dstintf: str | list | None = None,
        srcaddr: str | list | None = None,
        poolname: str | list | None = None,
        dstaddr: str | list | None = None,
        ztna_ems_tag: str | list | None = None,
        ztna_tags_match_logic: str | None = None,
        device_ownership: str | None = None,
        url_risk: str | list | None = None,
        internet_service: str | None = None,
        internet_service_negate: str | None = None,
        internet_service_name: str | list | None = None,
        internet_service_group: str | list | None = None,
        internet_service_custom: str | list | None = None,
        internet_service_custom_group: str | list | None = None,
        internet_service_fortiguard: str | list | None = None,
        internet_service6: str | None = None,
        internet_service6_negate: str | None = None,
        internet_service6_name: str | list | None = None,
        internet_service6_group: str | list | None = None,
        internet_service6_custom: str | list | None = None,
        internet_service6_custom_group: str | list | None = None,
        internet_service6_fortiguard: str | list | None = None,
        service: str | list | None = None,
        srcaddr_negate: str | None = None,
        dstaddr_negate: str | None = None,
        ztna_ems_tag_negate: str | None = None,
        service_negate: str | None = None,
        action: str | None = None,
        status: str | None = None,
        schedule: str | None = None,
        logtraffic: str | None = None,
        session_ttl: int | None = None,
        srcaddr6: str | list | None = None,
        dstaddr6: str | list | None = None,
        groups: str | list | None = None,
        users: str | list | None = None,
        http_tunnel_auth: str | None = None,
        ssh_policy_redirect: str | None = None,
        webproxy_forward_server: str | None = None,
        isolator_server: str | None = None,
        webproxy_profile: str | None = None,
        transparent: str | None = None,
        webcache: str | None = None,
        webcache_https: str | None = None,
        disclaimer: str | None = None,
        utm_status: str | None = None,
        profile_type: str | None = None,
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
        logtraffic_start: str | None = None,
        log_http_transaction: str | None = None,
        comments: str | None = None,
        block_notification: str | None = None,
        redirect_url: str | None = None,
        https_sub_category: str | None = None,
        decrypted_traffic_mirror: str | None = None,
        detect_https_in_http_request: str | None = None,
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
        proxy: str | None = None,
        access_proxy: str | list | None = None,
        access_proxy6: str | list | None = None,
        ztna_proxy: str | list | None = None,
        srcintf: str | list | None = None,
        dstintf: str | list | None = None,
        srcaddr: str | list | None = None,
        poolname: str | list | None = None,
        dstaddr: str | list | None = None,
        ztna_ems_tag: str | list | None = None,
        ztna_tags_match_logic: str | None = None,
        device_ownership: str | None = None,
        url_risk: str | list | None = None,
        internet_service: str | None = None,
        internet_service_negate: str | None = None,
        internet_service_name: str | list | None = None,
        internet_service_group: str | list | None = None,
        internet_service_custom: str | list | None = None,
        internet_service_custom_group: str | list | None = None,
        internet_service_fortiguard: str | list | None = None,
        internet_service6: str | None = None,
        internet_service6_negate: str | None = None,
        internet_service6_name: str | list | None = None,
        internet_service6_group: str | list | None = None,
        internet_service6_custom: str | list | None = None,
        internet_service6_custom_group: str | list | None = None,
        internet_service6_fortiguard: str | list | None = None,
        service: str | list | None = None,
        srcaddr_negate: str | None = None,
        dstaddr_negate: str | None = None,
        ztna_ems_tag_negate: str | None = None,
        service_negate: str | None = None,
        action: str | None = None,
        status: str | None = None,
        schedule: str | None = None,
        logtraffic: str | None = None,
        session_ttl: int | None = None,
        srcaddr6: str | list | None = None,
        dstaddr6: str | list | None = None,
        groups: str | list | None = None,
        users: str | list | None = None,
        http_tunnel_auth: str | None = None,
        ssh_policy_redirect: str | None = None,
        webproxy_forward_server: str | None = None,
        isolator_server: str | None = None,
        webproxy_profile: str | None = None,
        transparent: str | None = None,
        webcache: str | None = None,
        webcache_https: str | None = None,
        disclaimer: str | None = None,
        utm_status: str | None = None,
        profile_type: str | None = None,
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
        logtraffic_start: str | None = None,
        log_http_transaction: str | None = None,
        comments: str | None = None,
        block_notification: str | None = None,
        redirect_url: str | None = None,
        https_sub_category: str | None = None,
        decrypted_traffic_mirror: str | None = None,
        detect_https_in_http_request: str | None = None,
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
        try:
            response = self.get(policyid=policyid, vdom=vdom, raw_json=True)
            
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
            >>> print(ProxyPolicy.help())
            
            >>> # Get field information
            >>> print(ProxyPolicy.help("uuid"))
        """
        from ._helpers.proxy_policy import (
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
            >>> fields = ProxyPolicy.fields()
            >>> print(f"Available fields: {len(fields)}")
            
            >>> # Detailed info
            >>> fields = ProxyPolicy.fields(detailed=True)
            >>> for name, meta in fields.items():
            ...     print(f"{name}: {meta['type']}")
        """
        from ._helpers.proxy_policy import get_all_fields, get_field_metadata

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
            >>> info = ProxyPolicy.field_info("uuid")
            >>> print(f"Type: {info['type']}")
            >>> if 'options' in info:
            ...     print(f"Options: {info['options']}")
        """
        from ._helpers.proxy_policy import get_field_metadata

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
            >>> is_valid, error = ProxyPolicy.validate_field("uuid", "test")
            >>> if not is_valid:
            ...     print(f"Validation error: {error}")
        """
        from ._helpers.proxy_policy import validate_field_value

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
            >>> required = ProxyPolicy.required_fields()
            >>> print(f"Required fields: {', '.join(required)}")
        """
        from ._helpers.proxy_policy import REQUIRED_FIELDS

        return REQUIRED_FIELDS.copy()

    @staticmethod
    def defaults() -> dict[str, Any]:
        """
        Get all fields with default values.

        Returns:
            Dict mapping field names to default values

        Examples:
            >>> defaults = ProxyPolicy.defaults()
            >>> print(f"Fields with defaults: {len(defaults)}")
            >>> # Use as starting point for payload
            >>> payload = defaults.copy()
            >>> payload['name'] = 'my-custom-name'
        """
        from ._helpers.proxy_policy import FIELDS_WITH_DEFAULTS

        return FIELDS_WITH_DEFAULTS.copy()

    @staticmethod
    def schema() -> dict[str, Any]:
        """
        Get complete schema information for this endpoint.

        Returns:
            Schema metadata dict containing endpoint info, field counts, and primary key

        Examples:
            >>> schema = ProxyPolicy.schema()
            >>> print(f"Endpoint: {schema['endpoint']}")
            >>> print(f"Total fields: {schema['total_fields']}")
            >>> print(f"Primary key: {schema.get('mkey', 'N/A')}")
        """
        from ._helpers.proxy_policy import get_schema_info

        return get_schema_info()
