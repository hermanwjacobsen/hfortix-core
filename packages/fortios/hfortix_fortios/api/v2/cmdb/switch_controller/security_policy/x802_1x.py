"""
FortiOS CMDB - Switch_controller security_policy x802_1x

Configuration endpoint for managing cmdb switch_controller/security_policy/x802_1x objects.

API Endpoints:
    GET    /cmdb/switch_controller/security_policy/x802_1x
    POST   /cmdb/switch_controller/security_policy/x802_1x
    PUT    /cmdb/switch_controller/security_policy/x802_1x/{identifier}
    DELETE /cmdb/switch_controller/security_policy/x802_1x/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.switch_controller_security_policy_x802_1x.get()

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


class X8021x(MetadataMixin):
    """X8021x Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "x802_1x"

    def __init__(self, client: "IHTTPClient"):
        """Initialize X8021x endpoint."""
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
        Retrieve switch_controller/security_policy/x802_1x configuration.

        Configure 802.1x MAC Authentication Bypass (MAB) policies.

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
            >>> # Get all switch_controller/security_policy/x802_1x objects
            >>> result = fgt.api.cmdb.switch_controller_security_policy_x802_1x.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific switch_controller/security_policy/x802_1x by name
            >>> result = fgt.api.cmdb.switch_controller_security_policy_x802_1x.get(name=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.switch_controller_security_policy_x802_1x.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.switch_controller_security_policy_x802_1x.get(action="schema")

        See Also:
            - post(): Create new switch_controller/security_policy/x802_1x object
            - put(): Update existing switch_controller/security_policy/x802_1x object
            - delete(): Remove switch_controller/security_policy/x802_1x object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = "/switch-controller.security-policy/802-1X/" + str(name)
        else:
            endpoint = "/switch-controller.security-policy/802-1X"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        name: str | None = None,
        security_mode: str | None = None,
        user_group: str | list | None = None,
        mac_auth_bypass: str | None = None,
        auth_order: str | None = None,
        auth_priority: str | None = None,
        open_auth: str | None = None,
        eap_passthru: str | None = None,
        eap_auto_untagged_vlans: str | None = None,
        guest_vlan: str | None = None,
        guest_vlan_id: str | None = None,
        guest_auth_delay: int | None = None,
        auth_fail_vlan: str | None = None,
        auth_fail_vlan_id: str | None = None,
        framevid_apply: str | None = None,
        radius_timeout_overwrite: str | None = None,
        policy_type: str | None = None,
        authserver_timeout_period: int | None = None,
        authserver_timeout_vlan: str | None = None,
        authserver_timeout_vlanid: str | None = None,
        authserver_timeout_tagged: str | None = None,
        authserver_timeout_tagged_vlanid: str | None = None,
        dacl: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing switch_controller/security_policy/x802_1x object.

        Configure 802.1x MAC Authentication Bypass (MAB) policies.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            name: Policy name.
            security_mode: Port or MAC based 802.1X security mode.
            user_group: Name of user-group to assign to this MAC Authentication Bypass (MAB) policy.
            mac_auth_bypass: Enable/disable MAB for this policy.
            auth_order: Configure authentication order.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.switch_controller_security_policy_x802_1x.put(
            ...     name=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.switch_controller_security_policy_x802_1x.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            name=name,
            security_mode=security_mode,
            user_group=user_group,
            mac_auth_bypass=mac_auth_bypass,
            auth_order=auth_order,
            auth_priority=auth_priority,
            open_auth=open_auth,
            eap_passthru=eap_passthru,
            eap_auto_untagged_vlans=eap_auto_untagged_vlans,
            guest_vlan=guest_vlan,
            guest_vlan_id=guest_vlan_id,
            guest_auth_delay=guest_auth_delay,
            auth_fail_vlan=auth_fail_vlan,
            auth_fail_vlan_id=auth_fail_vlan_id,
            framevid_apply=framevid_apply,
            radius_timeout_overwrite=radius_timeout_overwrite,
            policy_type=policy_type,
            authserver_timeout_period=authserver_timeout_period,
            authserver_timeout_vlan=authserver_timeout_vlan,
            authserver_timeout_vlanid=authserver_timeout_vlanid,
            authserver_timeout_tagged=authserver_timeout_tagged,
            authserver_timeout_tagged_vlanid=authserver_timeout_tagged_vlanid,
            dacl=dacl,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.x802_1x import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/switch_controller/security_policy/x802_1x",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = "/switch-controller.security-policy/802-1X/" + str(name_value)

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        name: str | None = None,
        security_mode: str | None = None,
        user_group: str | list | None = None,
        mac_auth_bypass: str | None = None,
        auth_order: str | None = None,
        auth_priority: str | None = None,
        open_auth: str | None = None,
        eap_passthru: str | None = None,
        eap_auto_untagged_vlans: str | None = None,
        guest_vlan: str | None = None,
        guest_vlan_id: str | None = None,
        guest_auth_delay: int | None = None,
        auth_fail_vlan: str | None = None,
        auth_fail_vlan_id: str | None = None,
        framevid_apply: str | None = None,
        radius_timeout_overwrite: str | None = None,
        policy_type: str | None = None,
        authserver_timeout_period: int | None = None,
        authserver_timeout_vlan: str | None = None,
        authserver_timeout_vlanid: str | None = None,
        authserver_timeout_tagged: str | None = None,
        authserver_timeout_tagged_vlanid: str | None = None,
        dacl: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create new switch_controller/security_policy/x802_1x object.

        Configure 802.1x MAC Authentication Bypass (MAB) policies.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            name: Policy name.
            security_mode: Port or MAC based 802.1X security mode.
            user_group: Name of user-group to assign to this MAC Authentication Bypass (MAB) policy.
            mac_auth_bypass: Enable/disable MAB for this policy.
            auth_order: Configure authentication order.
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            raw_json: If True, return raw API response without processing.
            **kwargs: Additional parameters

        Returns:
            API response dict containing created object with assigned name.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.switch_controller_security_policy_x802_1x.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created name: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = X8021x.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.switch_controller_security_policy_x802_1x.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(X8021x.required_fields()) }}
            
            Use X8021x.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            name=name,
            security_mode=security_mode,
            user_group=user_group,
            mac_auth_bypass=mac_auth_bypass,
            auth_order=auth_order,
            auth_priority=auth_priority,
            open_auth=open_auth,
            eap_passthru=eap_passthru,
            eap_auto_untagged_vlans=eap_auto_untagged_vlans,
            guest_vlan=guest_vlan,
            guest_vlan_id=guest_vlan_id,
            guest_auth_delay=guest_auth_delay,
            auth_fail_vlan=auth_fail_vlan,
            auth_fail_vlan_id=auth_fail_vlan_id,
            framevid_apply=framevid_apply,
            radius_timeout_overwrite=radius_timeout_overwrite,
            policy_type=policy_type,
            authserver_timeout_period=authserver_timeout_period,
            authserver_timeout_vlan=authserver_timeout_vlan,
            authserver_timeout_vlanid=authserver_timeout_vlanid,
            authserver_timeout_tagged=authserver_timeout_tagged,
            authserver_timeout_tagged_vlanid=authserver_timeout_tagged_vlanid,
            dacl=dacl,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.x802_1x import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/switch_controller/security_policy/x802_1x",
            )

        endpoint = "/switch-controller.security-policy/802-1X"
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
        Delete switch_controller/security_policy/x802_1x object.

        Configure 802.1x MAC Authentication Bypass (MAB) policies.

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
            >>> result = fgt.api.cmdb.switch_controller_security_policy_x802_1x.delete(name=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not name:
            raise ValueError("name is required for DELETE")
        endpoint = "/switch-controller.security-policy/802-1X/" + str(name)

        return self._client.delete(
            "cmdb", endpoint, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        name: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if switch_controller/security_policy/x802_1x object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            name: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.switch_controller_security_policy_x802_1x.exists(name=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.switch_controller_security_policy_x802_1x.exists(name=1):
            ...     fgt.api.cmdb.switch_controller_security_policy_x802_1x.delete(name=1)

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
        Create or update switch_controller/security_policy/x802_1x object (intelligent operation).

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
            >>> result = fgt.api.cmdb.switch_controller_security_policy_x802_1x.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.switch_controller_security_policy_x802_1x.set(payload_dict=obj_data)
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


