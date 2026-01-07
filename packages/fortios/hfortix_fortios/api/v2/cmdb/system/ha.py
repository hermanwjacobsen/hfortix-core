"""
FortiOS CMDB - System ha

Configuration endpoint for managing cmdb system/ha objects.

API Endpoints:
    GET    /cmdb/system/ha
    POST   /cmdb/system/ha
    PUT    /cmdb/system/ha/{identifier}
    DELETE /cmdb/system/ha/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system_ha.get()

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


class Ha(MetadataMixin):
    """Ha Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "ha"
    
    # ========================================================================
    # Capabilities (from schema metadata)
    # ========================================================================
    SUPPORTS_CREATE = False
    SUPPORTS_READ = True
    SUPPORTS_UPDATE = True
    SUPPORTS_DELETE = False
    SUPPORTS_MOVE = True
    SUPPORTS_CLONE = True
    SUPPORTS_FILTERING = True
    SUPPORTS_PAGINATION = True
    SUPPORTS_SEARCH = False
    SUPPORTS_SORTING = False

    def __init__(self, client: "IHTTPClient"):
        """Initialize Ha endpoint."""
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
        Retrieve system/ha configuration.

        Configure HA.

        Args:
            name: Name identifier to retrieve specific object. If None, returns all objects.
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
            >>> # Get all system/ha objects
            >>> result = fgt.api.cmdb.system_ha.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.system_ha.get(
            ...     filter=["name==test", "status==enable"]
            ... )
            
            >>> # Get with pagination
            >>> result = fgt.api.cmdb.system_ha.get(
            ...     start=0, count=100
            ... )
            
            >>> # Get schema information  
            >>> schema = fgt.api.cmdb.system_ha.get_schema()

        See Also:
            - post(): Create new system/ha object
            - put(): Update existing system/ha object
            - delete(): Remove system/ha object
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
            endpoint = f"/system/ha/{name}"
        else:
            endpoint = "/system/ha"
        
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
            >>> schema = fgt.api.cmdb.system_ha.get_schema()
            >>> print(schema['results'])
            
            >>> # Get JSON Schema format (if supported)
            >>> json_schema = fgt.api.cmdb.system_ha.get_schema(format="json-schema")
        
        Note:
            Not all endpoints support all schema formats. The "schema" format
            is most widely supported.
        """
        return self.get(action=format, vdom=vdom)


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        group_id: int | None = None,
        group_name: str | None = None,
        mode: Literal["standalone", "a-a", "a-p"] | None = None,
        sync_packet_balance: Literal["enable", "disable"] | None = None,
        password: Any | None = None,
        key: Any | None = None,
        hbdev: str | list | None = None,
        auto_virtual_mac_interface: str | list | None = None,
        backup_hbdev: str | list | None = None,
        unicast_hb: Literal["enable", "disable"] | None = None,
        unicast_hb_peerip: str | None = None,
        unicast_hb_netmask: str | None = None,
        session_sync_dev: str | list | None = None,
        route_ttl: int | None = None,
        route_wait: int | None = None,
        route_hold: int | None = None,
        multicast_ttl: int | None = None,
        evpn_ttl: int | None = None,
        load_balance_all: Literal["enable", "disable"] | None = None,
        sync_config: Literal["enable", "disable"] | None = None,
        encryption: Literal["enable", "disable"] | None = None,
        authentication: Literal["enable", "disable"] | None = None,
        hb_interval: int | None = None,
        hb_interval_in_milliseconds: Literal["100ms", "10ms"] | None = None,
        hb_lost_threshold: int | None = None,
        hello_holddown: int | None = None,
        gratuitous_arps: Literal["enable", "disable"] | None = None,
        arps: int | None = None,
        arps_interval: int | None = None,
        session_pickup: Literal["enable", "disable"] | None = None,
        session_pickup_connectionless: Literal["enable", "disable"] | None = None,
        session_pickup_expectation: Literal["enable", "disable"] | None = None,
        session_pickup_nat: Literal["enable", "disable"] | None = None,
        session_pickup_delay: Literal["enable", "disable"] | None = None,
        link_failed_signal: Literal["enable", "disable"] | None = None,
        upgrade_mode: Literal["simultaneous", "uninterruptible", "local-only", "secondary-only"] | None = None,
        uninterruptible_primary_wait: int | None = None,
        standalone_mgmt_vdom: Literal["enable", "disable"] | None = None,
        ha_mgmt_status: Literal["enable", "disable"] | None = None,
        ha_mgmt_interfaces: str | list | None = None,
        ha_eth_type: str | None = None,
        hc_eth_type: str | None = None,
        l2ep_eth_type: str | None = None,
        ha_uptime_diff_margin: int | None = None,
        standalone_config_sync: Literal["enable", "disable"] | None = None,
        unicast_status: Literal["enable", "disable"] | None = None,
        unicast_gateway: str | None = None,
        unicast_peers: str | list | None = None,
        schedule: Literal["none", "leastconnection", "round-robin", "weight-round-robin", "random", "ip", "ipport"] | None = None,
        weight: str | None = None,
        cpu_threshold: str | None = None,
        memory_threshold: str | None = None,
        http_proxy_threshold: str | None = None,
        ftp_proxy_threshold: str | None = None,
        imap_proxy_threshold: str | None = None,
        nntp_proxy_threshold: str | None = None,
        pop3_proxy_threshold: str | None = None,
        smtp_proxy_threshold: str | None = None,
        override: Literal["enable", "disable"] | None = None,
        priority: int | None = None,
        override_wait_time: int | None = None,
        monitor: str | list | None = None,
        pingserver_monitor_interface: str | list | None = None,
        pingserver_failover_threshold: int | None = None,
        pingserver_secondary_force_reset: Literal["enable", "disable"] | None = None,
        pingserver_flip_timeout: int | None = None,
        vcluster_status: Literal["enable", "disable"] | None = None,
        vcluster: str | list | None = None,
        ha_direct: Literal["enable", "disable"] | None = None,
        ssd_failover: Literal["enable", "disable"] | None = None,
        memory_compatible_mode: Literal["enable", "disable"] | None = None,
        memory_based_failover: Literal["enable", "disable"] | None = None,
        memory_failover_threshold: int | None = None,
        memory_failover_monitor_period: int | None = None,
        memory_failover_sample_rate: int | None = None,
        memory_failover_flip_timeout: int | None = None,
        failover_hold_time: int | None = None,
        check_secondary_dev_health: Literal["enable", "disable"] | None = None,
        ipsec_phase2_proposal: Literal["aes128-sha1", "aes128-sha256", "aes128-sha384", "aes128-sha512", "aes192-sha1", "aes192-sha256", "aes192-sha384", "aes192-sha512", "aes256-sha1", "aes256-sha256", "aes256-sha384", "aes256-sha512", "aes128gcm", "aes256gcm", "chacha20poly1305"] | list | None = None,
        bounce_intf_upon_failover: Literal["enable", "disable"] | None = None,
        status: Any | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing system/ha object.

        Configure HA.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            group_id: HA group ID  (0 - 1023;  or 0 - 7 when there are more than 2 vclusters). Must be the same for all members.
            group_name: Cluster group name. Must be the same for all members.
            mode: HA mode. Must be the same for all members. FGSP requires standalone.
            sync_packet_balance: Enable/disable HA packet distribution to multiple CPUs.
            password: Cluster password. Must be the same for all members.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.system_ha.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.system_ha.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            group_id=group_id,
            group_name=group_name,
            mode=mode,
            sync_packet_balance=sync_packet_balance,
            password=password,
            key=key,
            hbdev=hbdev,
            auto_virtual_mac_interface=auto_virtual_mac_interface,
            backup_hbdev=backup_hbdev,
            unicast_hb=unicast_hb,
            unicast_hb_peerip=unicast_hb_peerip,
            unicast_hb_netmask=unicast_hb_netmask,
            session_sync_dev=session_sync_dev,
            route_ttl=route_ttl,
            route_wait=route_wait,
            route_hold=route_hold,
            multicast_ttl=multicast_ttl,
            evpn_ttl=evpn_ttl,
            load_balance_all=load_balance_all,
            sync_config=sync_config,
            encryption=encryption,
            authentication=authentication,
            hb_interval=hb_interval,
            hb_interval_in_milliseconds=hb_interval_in_milliseconds,
            hb_lost_threshold=hb_lost_threshold,
            hello_holddown=hello_holddown,
            gratuitous_arps=gratuitous_arps,
            arps=arps,
            arps_interval=arps_interval,
            session_pickup=session_pickup,
            session_pickup_connectionless=session_pickup_connectionless,
            session_pickup_expectation=session_pickup_expectation,
            session_pickup_nat=session_pickup_nat,
            session_pickup_delay=session_pickup_delay,
            link_failed_signal=link_failed_signal,
            upgrade_mode=upgrade_mode,
            uninterruptible_primary_wait=uninterruptible_primary_wait,
            standalone_mgmt_vdom=standalone_mgmt_vdom,
            ha_mgmt_status=ha_mgmt_status,
            ha_mgmt_interfaces=ha_mgmt_interfaces,
            ha_eth_type=ha_eth_type,
            hc_eth_type=hc_eth_type,
            l2ep_eth_type=l2ep_eth_type,
            ha_uptime_diff_margin=ha_uptime_diff_margin,
            standalone_config_sync=standalone_config_sync,
            unicast_status=unicast_status,
            unicast_gateway=unicast_gateway,
            unicast_peers=unicast_peers,
            schedule=schedule,
            weight=weight,
            cpu_threshold=cpu_threshold,
            memory_threshold=memory_threshold,
            http_proxy_threshold=http_proxy_threshold,
            ftp_proxy_threshold=ftp_proxy_threshold,
            imap_proxy_threshold=imap_proxy_threshold,
            nntp_proxy_threshold=nntp_proxy_threshold,
            pop3_proxy_threshold=pop3_proxy_threshold,
            smtp_proxy_threshold=smtp_proxy_threshold,
            override=override,
            priority=priority,
            override_wait_time=override_wait_time,
            monitor=monitor,
            pingserver_monitor_interface=pingserver_monitor_interface,
            pingserver_failover_threshold=pingserver_failover_threshold,
            pingserver_secondary_force_reset=pingserver_secondary_force_reset,
            pingserver_flip_timeout=pingserver_flip_timeout,
            vcluster_status=vcluster_status,
            vcluster=vcluster,
            ha_direct=ha_direct,
            ssd_failover=ssd_failover,
            memory_compatible_mode=memory_compatible_mode,
            memory_based_failover=memory_based_failover,
            memory_failover_threshold=memory_failover_threshold,
            memory_failover_monitor_period=memory_failover_monitor_period,
            memory_failover_sample_rate=memory_failover_sample_rate,
            memory_failover_flip_timeout=memory_failover_flip_timeout,
            failover_hold_time=failover_hold_time,
            check_secondary_dev_health=check_secondary_dev_health,
            ipsec_phase2_proposal=ipsec_phase2_proposal,
            bounce_intf_upon_failover=bounce_intf_upon_failover,
            status=status,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.ha import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/ha",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/system/ha/{name_value}"

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )





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
        Move system/ha object to a new position.
        
        Reorders objects by moving one before or after another.
        
        Args:
            name: Name of object to move
            action: Move "before" or "after" reference object
            reference_name: Name of reference object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Move policy 100 before policy 50
            >>> fgt.api.cmdb.system_ha.move(
            ...     name="object1",
            ...     action="before",
            ...     reference_name="object2"
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/system/ha",
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
        Clone system/ha object.
        
        Creates a copy of an existing object with a new identifier.
        
        Args:
            name: Name of object to clone
            new_name: Name for the cloned object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Clone an existing object
            >>> fgt.api.cmdb.system_ha.clone(
            ...     name="template",
            ...     new_name="new-from-template"
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/system/ha",
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
        Check if system/ha object exists.
        
        Args:
            name: Name to check
            vdom: Virtual domain name
            
        Returns:
            True if object exists, False otherwise
            
        Example:
            >>> # Check before creating
            >>> if not fgt.api.cmdb.system_ha.exists(name="myobj"):
            ...     fgt.api.cmdb.system_ha.post(payload_dict=data)
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

