"""
FortiOS CMDB - Vpn ipsec phase2_interface

Configuration endpoint for managing cmdb vpn/ipsec/phase2_interface objects.

API Endpoints:
    GET    /cmdb/vpn/ipsec/phase2_interface
    POST   /cmdb/vpn/ipsec/phase2_interface
    PUT    /cmdb/vpn/ipsec/phase2_interface/{identifier}
    DELETE /cmdb/vpn/ipsec/phase2_interface/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.vpn_ipsec_phase2_interface.get()

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


class Phase2Interface(MetadataMixin):
    """Phase2Interface Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "phase2_interface"

    def __init__(self, client: "IHTTPClient"):
        """Initialize Phase2Interface endpoint."""
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
        Retrieve vpn/ipsec/phase2_interface configuration.

        Configure VPN autokey tunnel.

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
            >>> # Get all vpn/ipsec/phase2_interface objects
            >>> result = fgt.api.cmdb.vpn_ipsec_phase2_interface.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific vpn/ipsec/phase2_interface by name
            >>> result = fgt.api.cmdb.vpn_ipsec_phase2_interface.get(name=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.vpn_ipsec_phase2_interface.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.vpn_ipsec_phase2_interface.get(action="schema")

        See Also:
            - post(): Create new vpn/ipsec/phase2_interface object
            - put(): Update existing vpn/ipsec/phase2_interface object
            - delete(): Remove vpn/ipsec/phase2_interface object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = "/vpn.ipsec/phase2-interface/" + str(name)
        else:
            endpoint = "/vpn.ipsec/phase2-interface"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        name: str | None = None,
        phase1name: str | None = None,
        dhcp_ipsec: str | None = None,
        proposal: str | list | None = None,
        pfs: str | None = None,
        dhgrp: str | list | None = None,
        addke1: str | list | None = None,
        addke2: str | list | None = None,
        addke3: str | list | None = None,
        addke4: str | list | None = None,
        addke5: str | list | None = None,
        addke6: str | list | None = None,
        addke7: str | list | None = None,
        replay: str | None = None,
        keepalive: str | None = None,
        auto_negotiate: str | None = None,
        add_route: str | None = None,
        inbound_dscp_copy: str | None = None,
        auto_discovery_sender: str | None = None,
        auto_discovery_forwarder: str | None = None,
        keylifeseconds: int | None = None,
        keylifekbs: int | None = None,
        keylife_type: str | None = None,
        single_source: str | None = None,
        route_overlap: str | None = None,
        encapsulation: str | None = None,
        l2tp: str | None = None,
        comments: str | None = None,
        initiator_ts_narrow: str | None = None,
        diffserv: str | None = None,
        diffservcode: str | None = None,
        protocol: int | None = None,
        src_name: str | None = None,
        src_name6: str | None = None,
        src_addr_type: str | None = None,
        src_start_ip: str | None = None,
        src_start_ip6: str | None = None,
        src_end_ip: str | None = None,
        src_end_ip6: str | None = None,
        src_subnet: Any | None = None,
        src_subnet6: str | None = None,
        src_port: int | None = None,
        dst_name: str | None = None,
        dst_name6: str | None = None,
        dst_addr_type: str | None = None,
        dst_start_ip: str | None = None,
        dst_start_ip6: str | None = None,
        dst_end_ip: str | None = None,
        dst_end_ip6: str | None = None,
        dst_subnet: Any | None = None,
        dst_subnet6: str | None = None,
        dst_port: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing vpn/ipsec/phase2_interface object.

        Configure VPN autokey tunnel.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            name: IPsec tunnel name.
            phase1name: Phase 1 determines the options required for phase 2.
            dhcp_ipsec: Enable/disable DHCP-IPsec.
            proposal: Phase2 proposal.
            pfs: Enable/disable PFS feature.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.vpn_ipsec_phase2_interface.put(
            ...     name=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.vpn_ipsec_phase2_interface.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            name=name,
            phase1name=phase1name,
            dhcp_ipsec=dhcp_ipsec,
            proposal=proposal,
            pfs=pfs,
            dhgrp=dhgrp,
            addke1=addke1,
            addke2=addke2,
            addke3=addke3,
            addke4=addke4,
            addke5=addke5,
            addke6=addke6,
            addke7=addke7,
            replay=replay,
            keepalive=keepalive,
            auto_negotiate=auto_negotiate,
            add_route=add_route,
            inbound_dscp_copy=inbound_dscp_copy,
            auto_discovery_sender=auto_discovery_sender,
            auto_discovery_forwarder=auto_discovery_forwarder,
            keylifeseconds=keylifeseconds,
            keylifekbs=keylifekbs,
            keylife_type=keylife_type,
            single_source=single_source,
            route_overlap=route_overlap,
            encapsulation=encapsulation,
            l2tp=l2tp,
            comments=comments,
            initiator_ts_narrow=initiator_ts_narrow,
            diffserv=diffserv,
            diffservcode=diffservcode,
            protocol=protocol,
            src_name=src_name,
            src_name6=src_name6,
            src_addr_type=src_addr_type,
            src_start_ip=src_start_ip,
            src_start_ip6=src_start_ip6,
            src_end_ip=src_end_ip,
            src_end_ip6=src_end_ip6,
            src_subnet=src_subnet,
            src_subnet6=src_subnet6,
            src_port=src_port,
            dst_name=dst_name,
            dst_name6=dst_name6,
            dst_addr_type=dst_addr_type,
            dst_start_ip=dst_start_ip,
            dst_start_ip6=dst_start_ip6,
            dst_end_ip=dst_end_ip,
            dst_end_ip6=dst_end_ip6,
            dst_subnet=dst_subnet,
            dst_subnet6=dst_subnet6,
            dst_port=dst_port,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.phase2_interface import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/vpn/ipsec/phase2_interface",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = "/vpn.ipsec/phase2-interface/" + str(name_value)

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        name: str | None = None,
        phase1name: str | None = None,
        dhcp_ipsec: str | None = None,
        proposal: str | list | None = None,
        pfs: str | None = None,
        dhgrp: str | list | None = None,
        addke1: str | list | None = None,
        addke2: str | list | None = None,
        addke3: str | list | None = None,
        addke4: str | list | None = None,
        addke5: str | list | None = None,
        addke6: str | list | None = None,
        addke7: str | list | None = None,
        replay: str | None = None,
        keepalive: str | None = None,
        auto_negotiate: str | None = None,
        add_route: str | None = None,
        inbound_dscp_copy: str | None = None,
        auto_discovery_sender: str | None = None,
        auto_discovery_forwarder: str | None = None,
        keylifeseconds: int | None = None,
        keylifekbs: int | None = None,
        keylife_type: str | None = None,
        single_source: str | None = None,
        route_overlap: str | None = None,
        encapsulation: str | None = None,
        l2tp: str | None = None,
        comments: str | None = None,
        initiator_ts_narrow: str | None = None,
        diffserv: str | None = None,
        diffservcode: str | None = None,
        protocol: int | None = None,
        src_name: str | None = None,
        src_name6: str | None = None,
        src_addr_type: str | None = None,
        src_start_ip: str | None = None,
        src_start_ip6: str | None = None,
        src_end_ip: str | None = None,
        src_end_ip6: str | None = None,
        src_subnet: Any | None = None,
        src_subnet6: str | None = None,
        src_port: int | None = None,
        dst_name: str | None = None,
        dst_name6: str | None = None,
        dst_addr_type: str | None = None,
        dst_start_ip: str | None = None,
        dst_start_ip6: str | None = None,
        dst_end_ip: str | None = None,
        dst_end_ip6: str | None = None,
        dst_subnet: Any | None = None,
        dst_subnet6: str | None = None,
        dst_port: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create new vpn/ipsec/phase2_interface object.

        Configure VPN autokey tunnel.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            name: IPsec tunnel name.
            phase1name: Phase 1 determines the options required for phase 2.
            dhcp_ipsec: Enable/disable DHCP-IPsec.
            proposal: Phase2 proposal.
            pfs: Enable/disable PFS feature.
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            raw_json: If True, return raw API response without processing.
            **kwargs: Additional parameters

        Returns:
            API response dict containing created object with assigned name.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.vpn_ipsec_phase2_interface.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created name: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = Phase2Interface.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.vpn_ipsec_phase2_interface.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(Phase2Interface.required_fields()) }}
            
            Use Phase2Interface.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            name=name,
            phase1name=phase1name,
            dhcp_ipsec=dhcp_ipsec,
            proposal=proposal,
            pfs=pfs,
            dhgrp=dhgrp,
            addke1=addke1,
            addke2=addke2,
            addke3=addke3,
            addke4=addke4,
            addke5=addke5,
            addke6=addke6,
            addke7=addke7,
            replay=replay,
            keepalive=keepalive,
            auto_negotiate=auto_negotiate,
            add_route=add_route,
            inbound_dscp_copy=inbound_dscp_copy,
            auto_discovery_sender=auto_discovery_sender,
            auto_discovery_forwarder=auto_discovery_forwarder,
            keylifeseconds=keylifeseconds,
            keylifekbs=keylifekbs,
            keylife_type=keylife_type,
            single_source=single_source,
            route_overlap=route_overlap,
            encapsulation=encapsulation,
            l2tp=l2tp,
            comments=comments,
            initiator_ts_narrow=initiator_ts_narrow,
            diffserv=diffserv,
            diffservcode=diffservcode,
            protocol=protocol,
            src_name=src_name,
            src_name6=src_name6,
            src_addr_type=src_addr_type,
            src_start_ip=src_start_ip,
            src_start_ip6=src_start_ip6,
            src_end_ip=src_end_ip,
            src_end_ip6=src_end_ip6,
            src_subnet=src_subnet,
            src_subnet6=src_subnet6,
            src_port=src_port,
            dst_name=dst_name,
            dst_name6=dst_name6,
            dst_addr_type=dst_addr_type,
            dst_start_ip=dst_start_ip,
            dst_start_ip6=dst_start_ip6,
            dst_end_ip=dst_end_ip,
            dst_end_ip6=dst_end_ip6,
            dst_subnet=dst_subnet,
            dst_subnet6=dst_subnet6,
            dst_port=dst_port,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.phase2_interface import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/vpn/ipsec/phase2_interface",
            )

        endpoint = "/vpn.ipsec/phase2-interface"
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
        Delete vpn/ipsec/phase2_interface object.

        Configure VPN autokey tunnel.

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
            >>> result = fgt.api.cmdb.vpn_ipsec_phase2_interface.delete(name=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not name:
            raise ValueError("name is required for DELETE")
        endpoint = "/vpn.ipsec/phase2-interface/" + str(name)

        return self._client.delete(
            "cmdb", endpoint, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        name: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if vpn/ipsec/phase2_interface object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            name: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.vpn_ipsec_phase2_interface.exists(name=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.vpn_ipsec_phase2_interface.exists(name=1):
            ...     fgt.api.cmdb.vpn_ipsec_phase2_interface.delete(name=1)

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
        Create or update vpn/ipsec/phase2_interface object (intelligent operation).

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
            >>> result = fgt.api.cmdb.vpn_ipsec_phase2_interface.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.vpn_ipsec_phase2_interface.set(payload_dict=obj_data)
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


