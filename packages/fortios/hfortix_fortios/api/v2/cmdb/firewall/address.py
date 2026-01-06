"""
FortiOS CMDB - Firewall address

Configuration endpoint for managing cmdb firewall/address objects.

API Endpoints:
    GET    /cmdb/firewall/address
    POST   /cmdb/firewall/address
    PUT    /cmdb/firewall/address/{identifier}
    DELETE /cmdb/firewall/address/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.firewall_address.get()

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


class Address(MetadataMixin):
    """Address Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "address"
    
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
        """Initialize Address endpoint."""
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
        Retrieve firewall/address configuration.

        Configure IPv4 addresses.

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
            >>> # Get all firewall/address objects
            >>> result = fgt.api.cmdb.firewall_address.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific firewall/address by name
            >>> result = fgt.api.cmdb.firewall_address.get(name=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.firewall_address.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.firewall_address.get(action="schema")

        See Also:
            - post(): Create new firewall/address object
            - put(): Update existing firewall/address object
            - delete(): Remove firewall/address object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = "/firewall/address/" + str(name)
        else:
            endpoint = "/firewall/address"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        name: str | None = None,
        uuid: str | None = None,
        subnet: Any | None = None,
        type: Literal["ipmask", "iprange", "fqdn", "geography", "wildcard", "dynamic", "interface-subnet", "mac", "route-tag"] | None = None,
        route_tag: int | None = None,
        sub_type: Literal["sdn", "clearpass-spt", "fsso", "rsso", "ems-tag", "fortivoice-tag", "fortinac-tag", "swc-tag", "device-identification", "external-resource", "obsolete"] | None = None,
        clearpass_spt: Literal["unknown", "healthy", "quarantine", "checkup", "transient", "infected"] | None = None,
        macaddr: str | list | None = None,
        start_ip: str | None = None,
        end_ip: str | None = None,
        fqdn: str | None = None,
        country: str | None = None,
        wildcard_fqdn: str | None = None,
        cache_ttl: int | None = None,
        wildcard: Any | None = None,
        sdn: str | None = None,
        fsso_group: str | list | None = None,
        sso_attribute_value: str | list | None = None,
        interface: str | None = None,
        tenant: str | None = None,
        organization: str | None = None,
        epg_name: str | None = None,
        subnet_name: str | None = None,
        sdn_tag: str | None = None,
        policy_group: str | None = None,
        obj_tag: str | None = None,
        obj_type: Literal["ip", "mac"] | None = None,
        tag_detection_level: str | None = None,
        tag_type: str | None = None,
        hw_vendor: str | None = None,
        hw_model: str | None = None,
        os: str | None = None,
        sw_version: str | None = None,
        comment: str | None = None,
        associated_interface: str | None = None,
        color: int | None = None,
        filter: str | None = None,
        sdn_addr_type: Literal["private", "public", "all"] | None = None,
        node_ip_only: Literal["enable", "disable"] | None = None,
        obj_id: str | None = None,
        list: str | list | None = None,
        tagging: str | list | None = None,
        allow_routing: Literal["enable", "disable"] | None = None,
        passive_fqdn_learning: Literal["disable", "enable"] | None = None,
        fabric_object: Literal["enable", "disable"] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing firewall/address object.

        Configure IPv4 addresses.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            name: Address name.
            uuid: Universally Unique Identifier (UUID; automatically assigned but can be manually reset).
            subnet: IP address and subnet mask of address.
            type: Type of address.
            route_tag: route-tag address.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.firewall_address.put(
            ...     name=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.firewall_address.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            name=name,
            uuid=uuid,
            subnet=subnet,
            type=type,
            route_tag=route_tag,
            sub_type=sub_type,
            clearpass_spt=clearpass_spt,
            macaddr=macaddr,
            start_ip=start_ip,
            end_ip=end_ip,
            fqdn=fqdn,
            country=country,
            wildcard_fqdn=wildcard_fqdn,
            cache_ttl=cache_ttl,
            wildcard=wildcard,
            sdn=sdn,
            fsso_group=fsso_group,
            sso_attribute_value=sso_attribute_value,
            interface=interface,
            tenant=tenant,
            organization=organization,
            epg_name=epg_name,
            subnet_name=subnet_name,
            sdn_tag=sdn_tag,
            policy_group=policy_group,
            obj_tag=obj_tag,
            obj_type=obj_type,
            tag_detection_level=tag_detection_level,
            tag_type=tag_type,
            hw_vendor=hw_vendor,
            hw_model=hw_model,
            os=os,
            sw_version=sw_version,
            comment=comment,
            associated_interface=associated_interface,
            color=color,
            filter=filter,
            sdn_addr_type=sdn_addr_type,
            node_ip_only=node_ip_only,
            obj_id=obj_id,
            list=list,
            tagging=tagging,
            allow_routing=allow_routing,
            passive_fqdn_learning=passive_fqdn_learning,
            fabric_object=fabric_object,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.address import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/firewall/address",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = "/firewall/address/" + str(name_value)

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        name: str | None = None,
        uuid: str | None = None,
        subnet: Any | None = None,
        type: Literal["ipmask", "iprange", "fqdn", "geography", "wildcard", "dynamic", "interface-subnet", "mac", "route-tag"] | None = None,
        route_tag: int | None = None,
        sub_type: Literal["sdn", "clearpass-spt", "fsso", "rsso", "ems-tag", "fortivoice-tag", "fortinac-tag", "swc-tag", "device-identification", "external-resource", "obsolete"] | None = None,
        clearpass_spt: Literal["unknown", "healthy", "quarantine", "checkup", "transient", "infected"] | None = None,
        macaddr: str | list | None = None,
        start_ip: str | None = None,
        end_ip: str | None = None,
        fqdn: str | None = None,
        country: str | None = None,
        wildcard_fqdn: str | None = None,
        cache_ttl: int | None = None,
        wildcard: Any | None = None,
        sdn: str | None = None,
        fsso_group: str | list | None = None,
        sso_attribute_value: str | list | None = None,
        interface: str | None = None,
        tenant: str | None = None,
        organization: str | None = None,
        epg_name: str | None = None,
        subnet_name: str | None = None,
        sdn_tag: str | None = None,
        policy_group: str | None = None,
        obj_tag: str | None = None,
        obj_type: Literal["ip", "mac"] | None = None,
        tag_detection_level: str | None = None,
        tag_type: str | None = None,
        hw_vendor: str | None = None,
        hw_model: str | None = None,
        os: str | None = None,
        sw_version: str | None = None,
        comment: str | None = None,
        associated_interface: str | None = None,
        color: int | None = None,
        filter: str | None = None,
        sdn_addr_type: Literal["private", "public", "all"] | None = None,
        node_ip_only: Literal["enable", "disable"] | None = None,
        obj_id: str | None = None,
        list: str | list | None = None,
        tagging: str | list | None = None,
        allow_routing: Literal["enable", "disable"] | None = None,
        passive_fqdn_learning: Literal["disable", "enable"] | None = None,
        fabric_object: Literal["enable", "disable"] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create new firewall/address object.

        Configure IPv4 addresses.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            name: Address name.
            uuid: Universally Unique Identifier (UUID; automatically assigned but can be manually reset).
            subnet: IP address and subnet mask of address.
            type: Type of address.
            route_tag: route-tag address.
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            raw_json: If True, return raw API response without processing.
            **kwargs: Additional parameters

        Returns:
            API response dict containing created object with assigned name.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.firewall_address.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created name: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = Address.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.firewall_address.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(Address.required_fields()) }}
            
            Use Address.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            name=name,
            uuid=uuid,
            subnet=subnet,
            type=type,
            route_tag=route_tag,
            sub_type=sub_type,
            clearpass_spt=clearpass_spt,
            macaddr=macaddr,
            start_ip=start_ip,
            end_ip=end_ip,
            fqdn=fqdn,
            country=country,
            wildcard_fqdn=wildcard_fqdn,
            cache_ttl=cache_ttl,
            wildcard=wildcard,
            sdn=sdn,
            fsso_group=fsso_group,
            sso_attribute_value=sso_attribute_value,
            interface=interface,
            tenant=tenant,
            organization=organization,
            epg_name=epg_name,
            subnet_name=subnet_name,
            sdn_tag=sdn_tag,
            policy_group=policy_group,
            obj_tag=obj_tag,
            obj_type=obj_type,
            tag_detection_level=tag_detection_level,
            tag_type=tag_type,
            hw_vendor=hw_vendor,
            hw_model=hw_model,
            os=os,
            sw_version=sw_version,
            comment=comment,
            associated_interface=associated_interface,
            color=color,
            filter=filter,
            sdn_addr_type=sdn_addr_type,
            node_ip_only=node_ip_only,
            obj_id=obj_id,
            list=list,
            tagging=tagging,
            allow_routing=allow_routing,
            passive_fqdn_learning=passive_fqdn_learning,
            fabric_object=fabric_object,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.address import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/firewall/address",
            )

        endpoint = "/firewall/address"
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
        Delete firewall/address object.

        Configure IPv4 addresses.

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
            >>> result = fgt.api.cmdb.firewall_address.delete(name=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not name:
            raise ValueError("name is required for DELETE")
        endpoint = "/firewall/address/" + str(name)

        return self._client.delete(
            "cmdb", endpoint, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        name: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if firewall/address object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            name: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.firewall_address.exists(name=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.firewall_address.exists(name=1):
            ...     fgt.api.cmdb.firewall_address.delete(name=1)

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
        Create or update firewall/address object (intelligent operation).

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
            >>> result = fgt.api.cmdb.firewall_address.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.firewall_address.set(payload_dict=obj_data)
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
        Move firewall/address object to a new position.
        
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
            >>> fgt.api.cmdb.firewall_address.move(
            ...     name=100,
            ...     action="before",
            ...     reference_name=50
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/firewall/address",
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
        Clone firewall/address object.
        
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
            >>> fgt.api.cmdb.firewall_address.clone(
            ...     name=1,
            ...     new_name=100
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/firewall/address",
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
        Check if firewall/address object exists.
        
        Args:
            name: Identifier to check
            vdom: Virtual domain name
            
        Returns:
            True if object exists, False otherwise
            
        Example:
            >>> # Check before creating
            >>> if not fgt.api.cmdb.firewall_address.exists(name=1):
            ...     fgt.api.cmdb.firewall_address.post(payload_dict=data)
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

