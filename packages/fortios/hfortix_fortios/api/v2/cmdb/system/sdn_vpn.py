"""
FortiOS CMDB - System sdn_vpn

Configuration endpoint for managing cmdb system/sdn_vpn objects.

API Endpoints:
    GET    /cmdb/system/sdn_vpn
    POST   /cmdb/system/sdn_vpn
    PUT    /cmdb/system/sdn_vpn/{identifier}
    DELETE /cmdb/system/sdn_vpn/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system_sdn_vpn.get()

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


class SdnVpn(MetadataMixin):
    """SdnVpn Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "sdn_vpn"

    def __init__(self, client: "IHTTPClient"):
        """Initialize SdnVpn endpoint."""
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
        Retrieve system/sdn_vpn configuration.

        Configure public cloud VPN service.

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
            >>> # Get all system/sdn_vpn objects
            >>> result = fgt.api.cmdb.system_sdn_vpn.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific system/sdn_vpn by name
            >>> result = fgt.api.cmdb.system_sdn_vpn.get(name=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.system_sdn_vpn.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.system_sdn_vpn.get(action="schema")

        See Also:
            - post(): Create new system/sdn_vpn object
            - put(): Update existing system/sdn_vpn object
            - delete(): Remove system/sdn_vpn object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = "/system/sdn-vpn/" + str(name)
        else:
            endpoint = "/system/sdn-vpn"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        name: str | None = None,
        sdn: str | None = None,
        remote_type: str | None = None,
        routing_type: str | None = None,
        vgw_id: str | None = None,
        tgw_id: str | None = None,
        subnet_id: str | None = None,
        bgp_as: int | None = None,
        cgw_gateway: str | None = None,
        nat_traversal: str | None = None,
        tunnel_interface: str | None = None,
        internal_interface: str | None = None,
        local_cidr: str | None = None,
        remote_cidr: str | None = None,
        cgw_name: str | None = None,
        psksecret: Any | None = None,
        type: int | None = None,
        status: int | None = None,
        code: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing system/sdn_vpn object.

        Configure public cloud VPN service.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            name: Public cloud VPN name.
            sdn: SDN connector name.
            remote_type: Type of remote device.
            routing_type: Type of routing.
            vgw_id: Virtual private gateway id.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.system_sdn_vpn.put(
            ...     name=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.system_sdn_vpn.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            name=name,
            sdn=sdn,
            remote_type=remote_type,
            routing_type=routing_type,
            vgw_id=vgw_id,
            tgw_id=tgw_id,
            subnet_id=subnet_id,
            bgp_as=bgp_as,
            cgw_gateway=cgw_gateway,
            nat_traversal=nat_traversal,
            tunnel_interface=tunnel_interface,
            internal_interface=internal_interface,
            local_cidr=local_cidr,
            remote_cidr=remote_cidr,
            cgw_name=cgw_name,
            psksecret=psksecret,
            type=type,
            status=status,
            code=code,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.sdn_vpn import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/sdn_vpn",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = "/system/sdn-vpn/" + str(name_value)

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        name: str | None = None,
        sdn: str | None = None,
        remote_type: str | None = None,
        routing_type: str | None = None,
        vgw_id: str | None = None,
        tgw_id: str | None = None,
        subnet_id: str | None = None,
        bgp_as: int | None = None,
        cgw_gateway: str | None = None,
        nat_traversal: str | None = None,
        tunnel_interface: str | None = None,
        internal_interface: str | None = None,
        local_cidr: str | None = None,
        remote_cidr: str | None = None,
        cgw_name: str | None = None,
        psksecret: Any | None = None,
        type: int | None = None,
        status: int | None = None,
        code: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create new system/sdn_vpn object.

        Configure public cloud VPN service.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            name: Public cloud VPN name.
            sdn: SDN connector name.
            remote_type: Type of remote device.
            routing_type: Type of routing.
            vgw_id: Virtual private gateway id.
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            raw_json: If True, return raw API response without processing.
            **kwargs: Additional parameters

        Returns:
            API response dict containing created object with assigned name.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.system_sdn_vpn.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created name: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = SdnVpn.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.system_sdn_vpn.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(SdnVpn.required_fields()) }}
            
            Use SdnVpn.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            name=name,
            sdn=sdn,
            remote_type=remote_type,
            routing_type=routing_type,
            vgw_id=vgw_id,
            tgw_id=tgw_id,
            subnet_id=subnet_id,
            bgp_as=bgp_as,
            cgw_gateway=cgw_gateway,
            nat_traversal=nat_traversal,
            tunnel_interface=tunnel_interface,
            internal_interface=internal_interface,
            local_cidr=local_cidr,
            remote_cidr=remote_cidr,
            cgw_name=cgw_name,
            psksecret=psksecret,
            type=type,
            status=status,
            code=code,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.sdn_vpn import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/sdn_vpn",
            )

        endpoint = "/system/sdn-vpn"
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
        Delete system/sdn_vpn object.

        Configure public cloud VPN service.

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
            >>> result = fgt.api.cmdb.system_sdn_vpn.delete(name=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not name:
            raise ValueError("name is required for DELETE")
        endpoint = "/system/sdn-vpn/" + str(name)

        return self._client.delete(
            "cmdb", endpoint, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        name: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if system/sdn_vpn object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            name: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.system_sdn_vpn.exists(name=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.system_sdn_vpn.exists(name=1):
            ...     fgt.api.cmdb.system_sdn_vpn.delete(name=1)

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
        Create or update system/sdn_vpn object (intelligent operation).

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
            >>> result = fgt.api.cmdb.system_sdn_vpn.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.system_sdn_vpn.set(payload_dict=obj_data)
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


