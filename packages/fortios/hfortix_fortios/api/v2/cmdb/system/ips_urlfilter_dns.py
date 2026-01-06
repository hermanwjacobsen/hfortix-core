"""
FortiOS CMDB - System ips_urlfilter_dns

Configuration endpoint for managing cmdb system/ips_urlfilter_dns objects.

API Endpoints:
    GET    /cmdb/system/ips_urlfilter_dns
    POST   /cmdb/system/ips_urlfilter_dns
    PUT    /cmdb/system/ips_urlfilter_dns/{identifier}
    DELETE /cmdb/system/ips_urlfilter_dns/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system_ips_urlfilter_dns.get()

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


class IpsUrlfilterDns(MetadataMixin):
    """IpsUrlfilterDns Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "ips_urlfilter_dns"

    def __init__(self, client: "IHTTPClient"):
        """Initialize IpsUrlfilterDns endpoint."""
        self._client = client

    def get(
        self,
        address: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve system/ips_urlfilter_dns configuration.

        Configure IPS URL filter DNS servers.

        Args:
            address: Ipv4-address identifier to retrieve specific object.
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
            >>> # Get all system/ips_urlfilter_dns objects
            >>> result = fgt.api.cmdb.system_ips_urlfilter_dns.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific system/ips_urlfilter_dns by address
            >>> result = fgt.api.cmdb.system_ips_urlfilter_dns.get(address=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.system_ips_urlfilter_dns.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.system_ips_urlfilter_dns.get(action="schema")

        See Also:
            - post(): Create new system/ips_urlfilter_dns object
            - put(): Update existing system/ips_urlfilter_dns object
            - delete(): Remove system/ips_urlfilter_dns object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if address:
            endpoint = "/system/ips-urlfilter-dns/" + str(address)
        else:
            endpoint = "/system/ips-urlfilter-dns"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        address: str | None = None,
        status: str | None = None,
        ipv6_capability: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing system/ips_urlfilter_dns object.

        Configure IPS URL filter DNS servers.

        Args:
            payload_dict: Object data as dict. Must include address (primary key).
            address: DNS server IP address.
            status: Enable/disable using this DNS server for IPS URL filter DNS queries.
            ipv6_capability: Enable/disable this server for IPv6 queries.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If address is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.system_ips_urlfilter_dns.put(
            ...     address=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "address": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.system_ips_urlfilter_dns.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            address=address,
            status=status,
            ipv6_capability=ipv6_capability,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.ips_urlfilter_dns import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/ips_urlfilter_dns",
            )
        
        address_value = payload_data.get("address")
        if not address_value:
            raise ValueError("address is required for PUT")
        endpoint = "/system/ips-urlfilter-dns/" + str(address_value)

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        address: str | None = None,
        status: str | None = None,
        ipv6_capability: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create new system/ips_urlfilter_dns object.

        Configure IPS URL filter DNS servers.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            address: DNS server IP address.
            status: Enable/disable using this DNS server for IPS URL filter DNS queries.
            ipv6_capability: Enable/disable this server for IPv6 queries.
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            raw_json: If True, return raw API response without processing.
            **kwargs: Additional parameters

        Returns:
            API response dict containing created object with assigned address.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.system_ips_urlfilter_dns.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created address: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = IpsUrlfilterDns.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.system_ips_urlfilter_dns.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(IpsUrlfilterDns.required_fields()) }}
            
            Use IpsUrlfilterDns.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            address=address,
            status=status,
            ipv6_capability=ipv6_capability,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.ips_urlfilter_dns import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/ips_urlfilter_dns",
            )

        endpoint = "/system/ips-urlfilter-dns"
        return self._client.post(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        address: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Delete system/ips_urlfilter_dns object.

        Configure IPS URL filter DNS servers.

        Args:
            address: Primary key identifier
            vdom: Virtual domain name
            raw_json: If True, return raw API response
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If address is not provided

        Examples:
            >>> # Delete specific object
            >>> result = fgt.api.cmdb.system_ips_urlfilter_dns.delete(address=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not address:
            raise ValueError("address is required for DELETE")
        endpoint = "/system/ips-urlfilter-dns/" + str(address)

        return self._client.delete(
            "cmdb", endpoint, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        address: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if system/ips_urlfilter_dns object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            address: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.system_ips_urlfilter_dns.exists(address=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.system_ips_urlfilter_dns.exists(address=1):
            ...     fgt.api.cmdb.system_ips_urlfilter_dns.delete(address=1)

        See Also:
            - get(): Retrieve full object data
            - set(): Create or update automatically based on existence
        """
        try:
            response = self.get(address=address, vdom=vdom, raw_json=True)
            
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
        Create or update system/ips_urlfilter_dns object (intelligent operation).

        Automatically determines whether to create (POST) or update (PUT) based on
        whether the resource exists. Requires the primary key (address) in the payload.

        Args:
            payload_dict: Resource data including address (primary key)
            vdom: Virtual domain name
            **kwargs: Additional parameters passed to PUT or POST

        Returns:
            API response dictionary

        Raises:
            ValueError: If address is missing from payload

        Examples:
            >>> # Intelligent create or update - no need to check exists()
            >>> payload = {
            ...     "address": 1,
            ...     "field1": "value1",
            ...     "field2": "value2",
            ... }
            >>> result = fgt.api.cmdb.system_ips_urlfilter_dns.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.system_ips_urlfilter_dns.set(payload_dict=obj_data)
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
        
        mkey_value = payload_dict.get("address")
        if not mkey_value:
            raise ValueError("address is required in payload_dict for set()")
        
        # Check if resource exists
        if self.exists(address=mkey_value, vdom=vdom):
            # Update existing resource
            return self.put(payload_dict=payload_dict, vdom=vdom, **kwargs)
        else:
            # Create new resource
            return self.post(payload_dict=payload_dict, vdom=vdom, **kwargs)


