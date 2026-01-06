"""
FortiOS CMDB - System dhcp server

Configuration endpoint for managing cmdb system/dhcp/server objects.

API Endpoints:
    GET    /cmdb/system/dhcp/server
    POST   /cmdb/system/dhcp/server
    PUT    /cmdb/system/dhcp/server/{identifier}
    DELETE /cmdb/system/dhcp/server/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system_dhcp_server.get()

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


class Server(MetadataMixin):
    """Server Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "server"
    
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
        """Initialize Server endpoint."""
        self._client = client

    def get(
        self,
        id: int | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve system/dhcp/server configuration.

        Configure DHCP servers.

        Args:
            id: Integer identifier to retrieve specific object.
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
            >>> # Get all system/dhcp/server objects
            >>> result = fgt.api.cmdb.system_dhcp_server.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific system/dhcp/server by id
            >>> result = fgt.api.cmdb.system_dhcp_server.get(id=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.system_dhcp_server.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.system_dhcp_server.get(action="schema")

        See Also:
            - post(): Create new system/dhcp/server object
            - put(): Update existing system/dhcp/server object
            - delete(): Remove system/dhcp/server object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if id:
            endpoint = "/system.dhcp/server/" + str(id)
        else:
            endpoint = "/system.dhcp/server"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        id: int | None = None,
        status: Literal["disable", "enable"] | None = None,
        lease_time: int | None = None,
        mac_acl_default_action: Literal["assign", "block"] | None = None,
        forticlient_on_net_status: Literal["disable", "enable"] | None = None,
        dns_service: Literal["local", "default", "specify"] | None = None,
        dns_server1: str | None = None,
        dns_server2: str | None = None,
        dns_server3: str | None = None,
        dns_server4: str | None = None,
        wifi_ac_service: Literal["specify", "local"] | None = None,
        wifi_ac1: str | None = None,
        wifi_ac2: str | None = None,
        wifi_ac3: str | None = None,
        ntp_service: Literal["local", "default", "specify"] | None = None,
        ntp_server1: str | None = None,
        ntp_server2: str | None = None,
        ntp_server3: str | None = None,
        domain: str | None = None,
        wins_server1: str | None = None,
        wins_server2: str | None = None,
        default_gateway: str | None = None,
        next_server: str | None = None,
        netmask: str | None = None,
        interface: str | None = None,
        ip_range: str | list | None = None,
        timezone_option: Literal["disable", "default", "specify"] | None = None,
        timezone: str | None = None,
        tftp_server: str | list | None = None,
        filename: str | None = None,
        options: str | list | None = None,
        server_type: Literal["regular", "ipsec"] | None = None,
        ip_mode: Literal["range", "usrgrp"] | None = None,
        conflicted_ip_timeout: int | None = None,
        ipsec_lease_hold: int | None = None,
        auto_configuration: Literal["disable", "enable"] | None = None,
        dhcp_settings_from_fortiipam: Literal["disable", "enable"] | None = None,
        auto_managed_status: Literal["disable", "enable"] | None = None,
        ddns_update: Literal["disable", "enable"] | None = None,
        ddns_update_override: Literal["disable", "enable"] | None = None,
        ddns_server_ip: str | None = None,
        ddns_zone: str | None = None,
        ddns_auth: Literal["disable", "tsig"] | None = None,
        ddns_keyname: str | None = None,
        ddns_key: Any | None = None,
        ddns_ttl: int | None = None,
        vci_match: Literal["disable", "enable"] | None = None,
        vci_string: str | list | None = None,
        exclude_range: str | list | None = None,
        shared_subnet: Literal["disable", "enable"] | None = None,
        relay_agent: str | None = None,
        reserved_address: str | list | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing system/dhcp/server object.

        Configure DHCP servers.

        Args:
            payload_dict: Object data as dict. Must include id (primary key).
            id: ID.
            status: Enable/disable this DHCP configuration.
            lease_time: Lease time in seconds, 0 means unlimited.
            mac_acl_default_action: MAC access control default action (allow or block assigning IP settings).
            forticlient_on_net_status: Enable/disable FortiClient-On-Net service for this DHCP server.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If id is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.system_dhcp_server.put(
            ...     id=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "id": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.system_dhcp_server.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            id=id,
            status=status,
            lease_time=lease_time,
            mac_acl_default_action=mac_acl_default_action,
            forticlient_on_net_status=forticlient_on_net_status,
            dns_service=dns_service,
            dns_server1=dns_server1,
            dns_server2=dns_server2,
            dns_server3=dns_server3,
            dns_server4=dns_server4,
            wifi_ac_service=wifi_ac_service,
            wifi_ac1=wifi_ac1,
            wifi_ac2=wifi_ac2,
            wifi_ac3=wifi_ac3,
            ntp_service=ntp_service,
            ntp_server1=ntp_server1,
            ntp_server2=ntp_server2,
            ntp_server3=ntp_server3,
            domain=domain,
            wins_server1=wins_server1,
            wins_server2=wins_server2,
            default_gateway=default_gateway,
            next_server=next_server,
            netmask=netmask,
            interface=interface,
            ip_range=ip_range,
            timezone_option=timezone_option,
            timezone=timezone,
            tftp_server=tftp_server,
            filename=filename,
            options=options,
            server_type=server_type,
            ip_mode=ip_mode,
            conflicted_ip_timeout=conflicted_ip_timeout,
            ipsec_lease_hold=ipsec_lease_hold,
            auto_configuration=auto_configuration,
            dhcp_settings_from_fortiipam=dhcp_settings_from_fortiipam,
            auto_managed_status=auto_managed_status,
            ddns_update=ddns_update,
            ddns_update_override=ddns_update_override,
            ddns_server_ip=ddns_server_ip,
            ddns_zone=ddns_zone,
            ddns_auth=ddns_auth,
            ddns_keyname=ddns_keyname,
            ddns_key=ddns_key,
            ddns_ttl=ddns_ttl,
            vci_match=vci_match,
            vci_string=vci_string,
            exclude_range=exclude_range,
            shared_subnet=shared_subnet,
            relay_agent=relay_agent,
            reserved_address=reserved_address,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.server import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/dhcp/server",
            )
        
        id_value = payload_data.get("id")
        if not id_value:
            raise ValueError("id is required for PUT")
        endpoint = "/system.dhcp/server/" + str(id_value)

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        id: int | None = None,
        status: Literal["disable", "enable"] | None = None,
        lease_time: int | None = None,
        mac_acl_default_action: Literal["assign", "block"] | None = None,
        forticlient_on_net_status: Literal["disable", "enable"] | None = None,
        dns_service: Literal["local", "default", "specify"] | None = None,
        dns_server1: str | None = None,
        dns_server2: str | None = None,
        dns_server3: str | None = None,
        dns_server4: str | None = None,
        wifi_ac_service: Literal["specify", "local"] | None = None,
        wifi_ac1: str | None = None,
        wifi_ac2: str | None = None,
        wifi_ac3: str | None = None,
        ntp_service: Literal["local", "default", "specify"] | None = None,
        ntp_server1: str | None = None,
        ntp_server2: str | None = None,
        ntp_server3: str | None = None,
        domain: str | None = None,
        wins_server1: str | None = None,
        wins_server2: str | None = None,
        default_gateway: str | None = None,
        next_server: str | None = None,
        netmask: str | None = None,
        interface: str | None = None,
        ip_range: str | list | None = None,
        timezone_option: Literal["disable", "default", "specify"] | None = None,
        timezone: str | None = None,
        tftp_server: str | list | None = None,
        filename: str | None = None,
        options: str | list | None = None,
        server_type: Literal["regular", "ipsec"] | None = None,
        ip_mode: Literal["range", "usrgrp"] | None = None,
        conflicted_ip_timeout: int | None = None,
        ipsec_lease_hold: int | None = None,
        auto_configuration: Literal["disable", "enable"] | None = None,
        dhcp_settings_from_fortiipam: Literal["disable", "enable"] | None = None,
        auto_managed_status: Literal["disable", "enable"] | None = None,
        ddns_update: Literal["disable", "enable"] | None = None,
        ddns_update_override: Literal["disable", "enable"] | None = None,
        ddns_server_ip: str | None = None,
        ddns_zone: str | None = None,
        ddns_auth: Literal["disable", "tsig"] | None = None,
        ddns_keyname: str | None = None,
        ddns_key: Any | None = None,
        ddns_ttl: int | None = None,
        vci_match: Literal["disable", "enable"] | None = None,
        vci_string: str | list | None = None,
        exclude_range: str | list | None = None,
        shared_subnet: Literal["disable", "enable"] | None = None,
        relay_agent: str | None = None,
        reserved_address: str | list | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create new system/dhcp/server object.

        Configure DHCP servers.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            id: ID.
            status: Enable/disable this DHCP configuration.
            lease_time: Lease time in seconds, 0 means unlimited.
            mac_acl_default_action: MAC access control default action (allow or block assigning IP settings).
            forticlient_on_net_status: Enable/disable FortiClient-On-Net service for this DHCP server.
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            raw_json: If True, return raw API response without processing.
            **kwargs: Additional parameters

        Returns:
            API response dict containing created object with assigned id.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.system_dhcp_server.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created id: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = Server.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.system_dhcp_server.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(Server.required_fields()) }}
            
            Use Server.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            id=id,
            status=status,
            lease_time=lease_time,
            mac_acl_default_action=mac_acl_default_action,
            forticlient_on_net_status=forticlient_on_net_status,
            dns_service=dns_service,
            dns_server1=dns_server1,
            dns_server2=dns_server2,
            dns_server3=dns_server3,
            dns_server4=dns_server4,
            wifi_ac_service=wifi_ac_service,
            wifi_ac1=wifi_ac1,
            wifi_ac2=wifi_ac2,
            wifi_ac3=wifi_ac3,
            ntp_service=ntp_service,
            ntp_server1=ntp_server1,
            ntp_server2=ntp_server2,
            ntp_server3=ntp_server3,
            domain=domain,
            wins_server1=wins_server1,
            wins_server2=wins_server2,
            default_gateway=default_gateway,
            next_server=next_server,
            netmask=netmask,
            interface=interface,
            ip_range=ip_range,
            timezone_option=timezone_option,
            timezone=timezone,
            tftp_server=tftp_server,
            filename=filename,
            options=options,
            server_type=server_type,
            ip_mode=ip_mode,
            conflicted_ip_timeout=conflicted_ip_timeout,
            ipsec_lease_hold=ipsec_lease_hold,
            auto_configuration=auto_configuration,
            dhcp_settings_from_fortiipam=dhcp_settings_from_fortiipam,
            auto_managed_status=auto_managed_status,
            ddns_update=ddns_update,
            ddns_update_override=ddns_update_override,
            ddns_server_ip=ddns_server_ip,
            ddns_zone=ddns_zone,
            ddns_auth=ddns_auth,
            ddns_keyname=ddns_keyname,
            ddns_key=ddns_key,
            ddns_ttl=ddns_ttl,
            vci_match=vci_match,
            vci_string=vci_string,
            exclude_range=exclude_range,
            shared_subnet=shared_subnet,
            relay_agent=relay_agent,
            reserved_address=reserved_address,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.server import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/dhcp/server",
            )

        endpoint = "/system.dhcp/server"
        return self._client.post(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        id: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Delete system/dhcp/server object.

        Configure DHCP servers.

        Args:
            id: Primary key identifier
            vdom: Virtual domain name
            raw_json: If True, return raw API response
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If id is not provided

        Examples:
            >>> # Delete specific object
            >>> result = fgt.api.cmdb.system_dhcp_server.delete(id=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not id:
            raise ValueError("id is required for DELETE")
        endpoint = "/system.dhcp/server/" + str(id)

        return self._client.delete(
            "cmdb", endpoint, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        id: int,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if system/dhcp/server object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            id: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.system_dhcp_server.exists(id=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.system_dhcp_server.exists(id=1):
            ...     fgt.api.cmdb.system_dhcp_server.delete(id=1)

        See Also:
            - get(): Retrieve full object data
            - set(): Create or update automatically based on existence
        """
        # Try to fetch the object - 404 means it doesn't exist
        try:
            response = self.get(
                id=id,
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
        Create or update system/dhcp/server object (intelligent operation).

        Automatically determines whether to create (POST) or update (PUT) based on
        whether the resource exists. Requires the primary key (id) in the payload.

        Args:
            payload_dict: Resource data including id (primary key)
            vdom: Virtual domain name
            **kwargs: Additional parameters passed to PUT or POST

        Returns:
            API response dictionary

        Raises:
            ValueError: If id is missing from payload

        Examples:
            >>> # Intelligent create or update - no need to check exists()
            >>> payload = {
            ...     "id": 1,
            ...     "field1": "value1",
            ...     "field2": "value2",
            ... }
            >>> result = fgt.api.cmdb.system_dhcp_server.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.system_dhcp_server.set(payload_dict=obj_data)
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
        
        mkey_value = payload_dict.get("id")
        if not mkey_value:
            raise ValueError("id is required in payload_dict for set()")
        
        # Check if resource exists
        if self.exists(id=mkey_value, vdom=vdom):
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
        id: int,
        action: Literal["before", "after"],
        reference_id: int,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Move system/dhcp/server object to a new position.
        
        Reorders objects by moving one before or after another.
        
        Args:
            id: Identifier of object to move
            action: Move "before" or "after" reference object
            reference_id: Identifier of reference object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Move policy 100 before policy 50
            >>> fgt.api.cmdb.system_dhcp_server.move(
            ...     id=100,
            ...     action="before",
            ...     reference_id=50
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/system.dhcp/server",
            params={
                "id": id,
                "action": "move",
                action: reference_id,
                "vdom": vdom,
                **kwargs,
            },
        )

    # ========================================================================
    # Action: Clone
    # ========================================================================
    
    def clone(
        self,
        id: int,
        new_id: int,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Clone system/dhcp/server object.
        
        Creates a copy of an existing object with a new identifier.
        
        Args:
            id: Identifier of object to clone
            new_id: Identifier for the cloned object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Clone an existing object
            >>> fgt.api.cmdb.system_dhcp_server.clone(
            ...     id=1,
            ...     new_id=100
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/system.dhcp/server",
            params={
                "id": id,
                "new_id": new_id,
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
        id: int,
        vdom: str | bool | None = None,
    ) -> bool:
        """
        Check if system/dhcp/server object exists.
        
        Args:
            id: Identifier to check
            vdom: Virtual domain name
            
        Returns:
            True if object exists, False otherwise
            
        Example:
            >>> # Check before creating
            >>> if not fgt.api.cmdb.system_dhcp_server.exists(id=1):
            ...     fgt.api.cmdb.system_dhcp_server.post(payload_dict=data)
        """
        # Try to fetch the object - 404 means it doesn't exist
        try:
            response = self.get(
                id=id,
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

