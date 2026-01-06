"""
FortiOS CMDB - Firewall interface_policy6

Configuration endpoint for managing cmdb firewall/interface_policy6 objects.

API Endpoints:
    GET    /cmdb/firewall/interface_policy6
    POST   /cmdb/firewall/interface_policy6
    PUT    /cmdb/firewall/interface_policy6/{identifier}
    DELETE /cmdb/firewall/interface_policy6/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.firewall_interface_policy6.get()

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


class InterfacePolicy6(MetadataMixin):
    """InterfacePolicy6 Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "interface_policy6"

    def __init__(self, client: "IHTTPClient"):
        """Initialize InterfacePolicy6 endpoint."""
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
        Retrieve firewall/interface_policy6 configuration.

        Configure IPv6 interface policies.

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
            >>> # Get all firewall/interface_policy6 objects
            >>> result = fgt.api.cmdb.firewall_interface_policy6.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific firewall/interface_policy6 by policyid
            >>> result = fgt.api.cmdb.firewall_interface_policy6.get(policyid=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.firewall_interface_policy6.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.firewall_interface_policy6.get(action="schema")

        See Also:
            - post(): Create new firewall/interface_policy6 object
            - put(): Update existing firewall/interface_policy6 object
            - delete(): Remove firewall/interface_policy6 object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if policyid:
            endpoint = "/firewall/interface-policy6/" + str(policyid)
        else:
            endpoint = "/firewall/interface-policy6"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        policyid: int | None = None,
        uuid: str | None = None,
        status: str | None = None,
        comments: str | None = None,
        logtraffic: str | None = None,
        interface: str | None = None,
        srcaddr6: str | list | None = None,
        dstaddr6: str | list | None = None,
        service6: str | list | None = None,
        application_list_status: str | None = None,
        application_list: str | None = None,
        ips_sensor_status: str | None = None,
        ips_sensor: str | None = None,
        dsri: str | None = None,
        av_profile_status: str | None = None,
        av_profile: str | None = None,
        webfilter_profile_status: str | None = None,
        webfilter_profile: str | None = None,
        casb_profile_status: str | None = None,
        casb_profile: str | None = None,
        emailfilter_profile_status: str | None = None,
        emailfilter_profile: str | None = None,
        dlp_profile_status: str | None = None,
        dlp_profile: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing firewall/interface_policy6 object.

        Configure IPv6 interface policies.

        Args:
            payload_dict: Object data as dict. Must include policyid (primary key).
            policyid: Policy ID (0 - 4294967295).
            uuid: Universally Unique Identifier (UUID; automatically assigned but can be manually reset).
            status: Enable/disable this policy.
            comments: Comments.
            logtraffic: Logging type to be used in this policy (Options: all | utm | disable, Default: utm).
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If policyid is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.firewall_interface_policy6.put(
            ...     policyid=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "policyid": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.firewall_interface_policy6.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            policyid=policyid,
            uuid=uuid,
            status=status,
            comments=comments,
            logtraffic=logtraffic,
            interface=interface,
            srcaddr6=srcaddr6,
            dstaddr6=dstaddr6,
            service6=service6,
            application_list_status=application_list_status,
            application_list=application_list,
            ips_sensor_status=ips_sensor_status,
            ips_sensor=ips_sensor,
            dsri=dsri,
            av_profile_status=av_profile_status,
            av_profile=av_profile,
            webfilter_profile_status=webfilter_profile_status,
            webfilter_profile=webfilter_profile,
            casb_profile_status=casb_profile_status,
            casb_profile=casb_profile,
            emailfilter_profile_status=emailfilter_profile_status,
            emailfilter_profile=emailfilter_profile,
            dlp_profile_status=dlp_profile_status,
            dlp_profile=dlp_profile,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.interface_policy6 import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/firewall/interface_policy6",
            )
        
        policyid_value = payload_data.get("policyid")
        if not policyid_value:
            raise ValueError("policyid is required for PUT")
        endpoint = "/firewall/interface-policy6/" + str(policyid_value)

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        policyid: int | None = None,
        uuid: str | None = None,
        status: str | None = None,
        comments: str | None = None,
        logtraffic: str | None = None,
        interface: str | None = None,
        srcaddr6: str | list | None = None,
        dstaddr6: str | list | None = None,
        service6: str | list | None = None,
        application_list_status: str | None = None,
        application_list: str | None = None,
        ips_sensor_status: str | None = None,
        ips_sensor: str | None = None,
        dsri: str | None = None,
        av_profile_status: str | None = None,
        av_profile: str | None = None,
        webfilter_profile_status: str | None = None,
        webfilter_profile: str | None = None,
        casb_profile_status: str | None = None,
        casb_profile: str | None = None,
        emailfilter_profile_status: str | None = None,
        emailfilter_profile: str | None = None,
        dlp_profile_status: str | None = None,
        dlp_profile: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create new firewall/interface_policy6 object.

        Configure IPv6 interface policies.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            policyid: Policy ID (0 - 4294967295).
            uuid: Universally Unique Identifier (UUID; automatically assigned but can be manually reset).
            status: Enable/disable this policy.
            comments: Comments.
            logtraffic: Logging type to be used in this policy (Options: all | utm | disable, Default: utm).
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            raw_json: If True, return raw API response without processing.
            **kwargs: Additional parameters

        Returns:
            API response dict containing created object with assigned policyid.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.firewall_interface_policy6.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created policyid: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = InterfacePolicy6.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.firewall_interface_policy6.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(InterfacePolicy6.required_fields()) }}
            
            Use InterfacePolicy6.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            policyid=policyid,
            uuid=uuid,
            status=status,
            comments=comments,
            logtraffic=logtraffic,
            interface=interface,
            srcaddr6=srcaddr6,
            dstaddr6=dstaddr6,
            service6=service6,
            application_list_status=application_list_status,
            application_list=application_list,
            ips_sensor_status=ips_sensor_status,
            ips_sensor=ips_sensor,
            dsri=dsri,
            av_profile_status=av_profile_status,
            av_profile=av_profile,
            webfilter_profile_status=webfilter_profile_status,
            webfilter_profile=webfilter_profile,
            casb_profile_status=casb_profile_status,
            casb_profile=casb_profile,
            emailfilter_profile_status=emailfilter_profile_status,
            emailfilter_profile=emailfilter_profile,
            dlp_profile_status=dlp_profile_status,
            dlp_profile=dlp_profile,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.interface_policy6 import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/firewall/interface_policy6",
            )

        endpoint = "/firewall/interface-policy6"
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
        Delete firewall/interface_policy6 object.

        Configure IPv6 interface policies.

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
            >>> result = fgt.api.cmdb.firewall_interface_policy6.delete(policyid=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not policyid:
            raise ValueError("policyid is required for DELETE")
        endpoint = "/firewall/interface-policy6/" + str(policyid)

        return self._client.delete(
            "cmdb", endpoint, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        policyid: int,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if firewall/interface_policy6 object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            policyid: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.firewall_interface_policy6.exists(policyid=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.firewall_interface_policy6.exists(policyid=1):
            ...     fgt.api.cmdb.firewall_interface_policy6.delete(policyid=1)

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
        Create or update firewall/interface_policy6 object (intelligent operation).

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
            >>> result = fgt.api.cmdb.firewall_interface_policy6.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.firewall_interface_policy6.set(payload_dict=obj_data)
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


