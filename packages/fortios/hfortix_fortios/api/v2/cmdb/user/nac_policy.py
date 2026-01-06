"""
FortiOS CMDB - User nac_policy

Configuration endpoint for managing cmdb user/nac_policy objects.

API Endpoints:
    GET    /cmdb/user/nac_policy
    POST   /cmdb/user/nac_policy
    PUT    /cmdb/user/nac_policy/{identifier}
    DELETE /cmdb/user/nac_policy/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.user_nac_policy.get()

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


class NacPolicy(MetadataMixin):
    """NacPolicy Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "nac_policy"

    def __init__(self, client: "IHTTPClient"):
        """Initialize NacPolicy endpoint."""
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
        Retrieve user/nac_policy configuration.

        Configure NAC policy matching pattern to identify matching NAC devices.

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
            >>> # Get all user/nac_policy objects
            >>> result = fgt.api.cmdb.user_nac_policy.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific user/nac_policy by name
            >>> result = fgt.api.cmdb.user_nac_policy.get(name=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.user_nac_policy.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.user_nac_policy.get(action="schema")

        See Also:
            - post(): Create new user/nac_policy object
            - put(): Update existing user/nac_policy object
            - delete(): Remove user/nac_policy object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = "/user/nac-policy/" + str(name)
        else:
            endpoint = "/user/nac-policy"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        name: str | None = None,
        description: str | None = None,
        category: str | None = None,
        status: str | None = None,
        match_type: str | None = None,
        match_period: int | None = None,
        match_remove: str | None = None,
        mac: str | None = None,
        hw_vendor: str | None = None,
        type: str | None = None,
        family: str | None = None,
        os: str | None = None,
        hw_version: str | None = None,
        sw_version: str | None = None,
        host: str | None = None,
        user: str | None = None,
        src: str | None = None,
        user_group: str | None = None,
        ems_tag: str | None = None,
        fortivoice_tag: str | None = None,
        severity: str | list | None = None,
        switch_fortilink: str | None = None,
        switch_group: str | list | None = None,
        switch_mac_policy: str | None = None,
        firewall_address: str | None = None,
        ssid_policy: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing user/nac_policy object.

        Configure NAC policy matching pattern to identify matching NAC devices.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            name: NAC policy name.
            description: Description for the NAC policy matching pattern.
            category: Category of NAC policy.
            status: Enable/disable NAC policy.
            match_type: Match and retain the devices based on the type.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.user_nac_policy.put(
            ...     name=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.user_nac_policy.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            name=name,
            description=description,
            category=category,
            status=status,
            match_type=match_type,
            match_period=match_period,
            match_remove=match_remove,
            mac=mac,
            hw_vendor=hw_vendor,
            type=type,
            family=family,
            os=os,
            hw_version=hw_version,
            sw_version=sw_version,
            host=host,
            user=user,
            src=src,
            user_group=user_group,
            ems_tag=ems_tag,
            fortivoice_tag=fortivoice_tag,
            severity=severity,
            switch_fortilink=switch_fortilink,
            switch_group=switch_group,
            switch_mac_policy=switch_mac_policy,
            firewall_address=firewall_address,
            ssid_policy=ssid_policy,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.nac_policy import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/user/nac_policy",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = "/user/nac-policy/" + str(name_value)

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        name: str | None = None,
        description: str | None = None,
        category: str | None = None,
        status: str | None = None,
        match_type: str | None = None,
        match_period: int | None = None,
        match_remove: str | None = None,
        mac: str | None = None,
        hw_vendor: str | None = None,
        type: str | None = None,
        family: str | None = None,
        os: str | None = None,
        hw_version: str | None = None,
        sw_version: str | None = None,
        host: str | None = None,
        user: str | None = None,
        src: str | None = None,
        user_group: str | None = None,
        ems_tag: str | None = None,
        fortivoice_tag: str | None = None,
        severity: str | list | None = None,
        switch_fortilink: str | None = None,
        switch_group: str | list | None = None,
        switch_mac_policy: str | None = None,
        firewall_address: str | None = None,
        ssid_policy: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create new user/nac_policy object.

        Configure NAC policy matching pattern to identify matching NAC devices.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            name: NAC policy name.
            description: Description for the NAC policy matching pattern.
            category: Category of NAC policy.
            status: Enable/disable NAC policy.
            match_type: Match and retain the devices based on the type.
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            raw_json: If True, return raw API response without processing.
            **kwargs: Additional parameters

        Returns:
            API response dict containing created object with assigned name.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.user_nac_policy.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created name: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = NacPolicy.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.user_nac_policy.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(NacPolicy.required_fields()) }}
            
            Use NacPolicy.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            name=name,
            description=description,
            category=category,
            status=status,
            match_type=match_type,
            match_period=match_period,
            match_remove=match_remove,
            mac=mac,
            hw_vendor=hw_vendor,
            type=type,
            family=family,
            os=os,
            hw_version=hw_version,
            sw_version=sw_version,
            host=host,
            user=user,
            src=src,
            user_group=user_group,
            ems_tag=ems_tag,
            fortivoice_tag=fortivoice_tag,
            severity=severity,
            switch_fortilink=switch_fortilink,
            switch_group=switch_group,
            switch_mac_policy=switch_mac_policy,
            firewall_address=firewall_address,
            ssid_policy=ssid_policy,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.nac_policy import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/user/nac_policy",
            )

        endpoint = "/user/nac-policy"
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
        Delete user/nac_policy object.

        Configure NAC policy matching pattern to identify matching NAC devices.

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
            >>> result = fgt.api.cmdb.user_nac_policy.delete(name=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not name:
            raise ValueError("name is required for DELETE")
        endpoint = "/user/nac-policy/" + str(name)

        return self._client.delete(
            "cmdb", endpoint, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        name: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if user/nac_policy object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            name: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.user_nac_policy.exists(name=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.user_nac_policy.exists(name=1):
            ...     fgt.api.cmdb.user_nac_policy.delete(name=1)

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
        Create or update user/nac_policy object (intelligent operation).

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
            >>> result = fgt.api.cmdb.user_nac_policy.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.user_nac_policy.set(payload_dict=obj_data)
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


