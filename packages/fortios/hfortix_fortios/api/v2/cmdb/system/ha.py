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

from typing import TYPE_CHECKING, Any, Union

if TYPE_CHECKING:
    from collections.abc import Coroutine
    from hfortix_core.http.interface import IHTTPClient

# Import helper functions from central _helpers module
from hfortix_fortios._helpers import (
    build_cmdb_payload,
    is_success,
)


class Ha:
    """Ha Operations."""

    def __init__(self, client: "IHTTPClient"):
        """Initialize Ha endpoint."""
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
        Retrieve system/ha configuration.

        Configure HA.

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
            >>> # Get all system/ha objects
            >>> result = fgt.api.cmdb.system_ha.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.system_ha.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.system_ha.get(action="schema")

        See Also:
            - post(): Create new system/ha object
            - put(): Update existing system/ha object
            - delete(): Remove system/ha object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/system/ha/{name}"
        else:
            endpoint = "/system/ha"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        group_id: int | None = None,
        group_name: str | None = None,
        mode: str | None = None,
        sync_packet_balance: str | None = None,
        password: Any | None = None,
        key: Any | None = None,
        hbdev: str | None = None,
        auto_virtual_mac_interface: str | list | None = None,
        backup_hbdev: str | list | None = None,
        unicast_hb: str | None = None,
        unicast_hb_peerip: str | None = None,
        unicast_hb_netmask: str | None = None,
        session_sync_dev: str | None = None,
        route_ttl: int | None = None,
        route_wait: int | None = None,
        route_hold: int | None = None,
        multicast_ttl: int | None = None,
        evpn_ttl: int | None = None,
        load_balance_all: str | None = None,
        sync_config: str | None = None,
        encryption: str | None = None,
        authentication: str | None = None,
        hb_interval: int | None = None,
        hb_interval_in_milliseconds: str | None = None,
        hb_lost_threshold: int | None = None,
        hello_holddown: int | None = None,
        gratuitous_arps: str | None = None,
        arps: int | None = None,
        arps_interval: int | None = None,
        session_pickup: str | None = None,
        session_pickup_connectionless: str | None = None,
        session_pickup_expectation: str | None = None,
        session_pickup_nat: str | None = None,
        session_pickup_delay: str | None = None,
        link_failed_signal: str | None = None,
        upgrade_mode: str | None = None,
        uninterruptible_primary_wait: int | None = None,
        standalone_mgmt_vdom: str | None = None,
        ha_mgmt_status: str | None = None,
        ha_mgmt_interfaces: str | list | None = None,
        ha_eth_type: str | None = None,
        hc_eth_type: str | None = None,
        l2ep_eth_type: str | None = None,
        ha_uptime_diff_margin: int | None = None,
        standalone_config_sync: str | None = None,
        unicast_status: str | None = None,
        unicast_gateway: str | None = None,
        unicast_peers: str | list | None = None,
        schedule: str | None = None,
        weight: str | None = None,
        cpu_threshold: str | None = None,
        memory_threshold: str | None = None,
        http_proxy_threshold: str | None = None,
        ftp_proxy_threshold: str | None = None,
        imap_proxy_threshold: str | None = None,
        nntp_proxy_threshold: str | None = None,
        pop3_proxy_threshold: str | None = None,
        smtp_proxy_threshold: str | None = None,
        override: str | None = None,
        priority: int | None = None,
        override_wait_time: int | None = None,
        monitor: str | None = None,
        pingserver_monitor_interface: str | None = None,
        pingserver_failover_threshold: int | None = None,
        pingserver_secondary_force_reset: str | None = None,
        pingserver_flip_timeout: int | None = None,
        vcluster_status: str | None = None,
        vcluster: str | list | None = None,
        ha_direct: str | None = None,
        ssd_failover: str | None = None,
        memory_compatible_mode: str | None = None,
        memory_based_failover: str | None = None,
        memory_failover_threshold: int | None = None,
        memory_failover_monitor_period: int | None = None,
        memory_failover_sample_rate: int | None = None,
        memory_failover_flip_timeout: int | None = None,
        failover_hold_time: int | None = None,
        check_secondary_dev_health: str | None = None,
        ipsec_phase2_proposal: str | None = None,
        bounce_intf_upon_failover: str | None = None,
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

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        group_id: int | None = None,
        group_name: str | None = None,
        mode: str | None = None,
        sync_packet_balance: str | None = None,
        password: Any | None = None,
        key: Any | None = None,
        hbdev: str | None = None,
        auto_virtual_mac_interface: str | list | None = None,
        backup_hbdev: str | list | None = None,
        unicast_hb: str | None = None,
        unicast_hb_peerip: str | None = None,
        unicast_hb_netmask: str | None = None,
        session_sync_dev: str | None = None,
        route_ttl: int | None = None,
        route_wait: int | None = None,
        route_hold: int | None = None,
        multicast_ttl: int | None = None,
        evpn_ttl: int | None = None,
        load_balance_all: str | None = None,
        sync_config: str | None = None,
        encryption: str | None = None,
        authentication: str | None = None,
        hb_interval: int | None = None,
        hb_interval_in_milliseconds: str | None = None,
        hb_lost_threshold: int | None = None,
        hello_holddown: int | None = None,
        gratuitous_arps: str | None = None,
        arps: int | None = None,
        arps_interval: int | None = None,
        session_pickup: str | None = None,
        session_pickup_connectionless: str | None = None,
        session_pickup_expectation: str | None = None,
        session_pickup_nat: str | None = None,
        session_pickup_delay: str | None = None,
        link_failed_signal: str | None = None,
        upgrade_mode: str | None = None,
        uninterruptible_primary_wait: int | None = None,
        standalone_mgmt_vdom: str | None = None,
        ha_mgmt_status: str | None = None,
        ha_mgmt_interfaces: str | list | None = None,
        ha_eth_type: str | None = None,
        hc_eth_type: str | None = None,
        l2ep_eth_type: str | None = None,
        ha_uptime_diff_margin: int | None = None,
        standalone_config_sync: str | None = None,
        unicast_status: str | None = None,
        unicast_gateway: str | None = None,
        unicast_peers: str | list | None = None,
        schedule: str | None = None,
        weight: str | None = None,
        cpu_threshold: str | None = None,
        memory_threshold: str | None = None,
        http_proxy_threshold: str | None = None,
        ftp_proxy_threshold: str | None = None,
        imap_proxy_threshold: str | None = None,
        nntp_proxy_threshold: str | None = None,
        pop3_proxy_threshold: str | None = None,
        smtp_proxy_threshold: str | None = None,
        override: str | None = None,
        priority: int | None = None,
        override_wait_time: int | None = None,
        monitor: str | None = None,
        pingserver_monitor_interface: str | None = None,
        pingserver_failover_threshold: int | None = None,
        pingserver_secondary_force_reset: str | None = None,
        pingserver_flip_timeout: int | None = None,
        vcluster_status: str | None = None,
        vcluster: str | list | None = None,
        ha_direct: str | None = None,
        ssd_failover: str | None = None,
        memory_compatible_mode: str | None = None,
        memory_based_failover: str | None = None,
        memory_failover_threshold: int | None = None,
        memory_failover_monitor_period: int | None = None,
        memory_failover_sample_rate: int | None = None,
        memory_failover_flip_timeout: int | None = None,
        failover_hold_time: int | None = None,
        check_secondary_dev_health: str | None = None,
        ipsec_phase2_proposal: str | None = None,
        bounce_intf_upon_failover: str | None = None,
        status: Any | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create new system/ha object.

        Configure HA.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            group_id: HA group ID  (0 - 1023;  or 0 - 7 when there are more than 2 vclusters). Must be the same for all members.
            group_name: Cluster group name. Must be the same for all members.
            mode: HA mode. Must be the same for all members. FGSP requires standalone.
            sync_packet_balance: Enable/disable HA packet distribution to multiple CPUs.
            password: Cluster password. Must be the same for all members.
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            raw_json: If True, return raw API response without processing.
            **kwargs: Additional parameters

        Returns:
            API response dict containing created object with assigned identifier.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.system_ha.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created object: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = Ha.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.system_ha.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(Ha.required_fields()) }}
            
            Use Ha.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
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

        endpoint = "/system/ha"
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
        Delete system/ha object.

        Configure HA.

        Args:
            name: Object name (primary key)
            vdom: Virtual domain name
            raw_json: If True, return raw API response
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is not provided

        Examples:
            >>> # Delete specific object
            >>> result = fgt.api.cmdb.system_ha.delete(name="object-to-delete")
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not name:
            raise ValueError("name is required for DELETE")
        endpoint = f"/system/ha/{name}"

        return self._client.delete(
            "cmdb", endpoint, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        name: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if system/ha object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            name: Object name (primary key)
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.system_ha.exists(name="my-object"):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.system_ha.exists(name="old-object"):
            ...     fgt.api.cmdb.system_ha.delete(name="old-object")

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
        Create or update system/ha object (intelligent operation).

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
            ...     "name": "my-object",
            ...     "field1": "value1",
            ...     "field2": "value2",
            ... }
            >>> result = fgt.api.cmdb.system_ha.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.system_ha.set(payload_dict=obj_data)
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
            >>> print(Ha.help())
            
            >>> # Get field information
            >>> print(Ha.help("group-id"))
        """
        from ._helpers.ha import (
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
            >>> fields = Ha.fields()
            >>> print(f"Available fields: {len(fields)}")
            
            >>> # Detailed info
            >>> fields = Ha.fields(detailed=True)
            >>> for name, meta in fields.items():
            ...     print(f"{name}: {meta['type']}")
        """
        from ._helpers.ha import get_all_fields, get_field_metadata

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
            >>> info = Ha.field_info("group-id")
            >>> print(f"Type: {info['type']}")
            >>> if 'options' in info:
            ...     print(f"Options: {info['options']}")
        """
        from ._helpers.ha import get_field_metadata

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
            >>> is_valid, error = Ha.validate_field("group-id", "test")
            >>> if not is_valid:
            ...     print(f"Validation error: {error}")
        """
        from ._helpers.ha import validate_field_value

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
            >>> required = Ha.required_fields()
            >>> print(f"Required fields: {', '.join(required)}")
        """
        from ._helpers.ha import REQUIRED_FIELDS

        return REQUIRED_FIELDS.copy()

    @staticmethod
    def defaults() -> dict[str, Any]:
        """
        Get all fields with default values.

        Returns:
            Dict mapping field names to default values

        Examples:
            >>> defaults = Ha.defaults()
            >>> print(f"Fields with defaults: {len(defaults)}")
            >>> # Use as starting point for payload
            >>> payload = defaults.copy()
            >>> payload['name'] = 'my-custom-name'
        """
        from ._helpers.ha import FIELDS_WITH_DEFAULTS

        return FIELDS_WITH_DEFAULTS.copy()

    @staticmethod
    def schema() -> dict[str, Any]:
        """
        Get complete schema information for this endpoint.

        Returns:
            Schema metadata dict containing endpoint info, field counts, and primary key

        Examples:
            >>> schema = Ha.schema()
            >>> print(f"Endpoint: {schema['endpoint']}")
            >>> print(f"Total fields: {schema['total_fields']}")
            >>> print(f"Primary key: {schema.get('mkey', 'N/A')}")
        """
        from ._helpers.ha import get_schema_info

        return get_schema_info()
