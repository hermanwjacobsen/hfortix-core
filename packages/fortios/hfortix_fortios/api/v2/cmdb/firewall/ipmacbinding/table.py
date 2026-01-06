"""
FortiOS CMDB - Firewall ipmacbinding table

Configuration endpoint for managing cmdb firewall/ipmacbinding/table objects.

API Endpoints:
    GET    /cmdb/firewall/ipmacbinding/table
    POST   /cmdb/firewall/ipmacbinding/table
    PUT    /cmdb/firewall/ipmacbinding/table/{identifier}
    DELETE /cmdb/firewall/ipmacbinding/table/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.firewall_ipmacbinding_table.get()

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


class Table(MetadataMixin):
    """Table Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "table"

    def __init__(self, client: "IHTTPClient"):
        """Initialize Table endpoint."""
        self._client = client

    def get(
        self,
        seq_num: int | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve firewall/ipmacbinding/table configuration.

        Configure IP to MAC address pairs in the IP/MAC binding table.

        Args:
            seq_num: Integer identifier to retrieve specific object.
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
            >>> # Get all firewall/ipmacbinding/table objects
            >>> result = fgt.api.cmdb.firewall_ipmacbinding_table.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific firewall/ipmacbinding/table by seq-num
            >>> result = fgt.api.cmdb.firewall_ipmacbinding_table.get(seq_num=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.firewall_ipmacbinding_table.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.firewall_ipmacbinding_table.get(action="schema")

        See Also:
            - post(): Create new firewall/ipmacbinding/table object
            - put(): Update existing firewall/ipmacbinding/table object
            - delete(): Remove firewall/ipmacbinding/table object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if seq_num:
            endpoint = "/firewall.ipmacbinding/table/" + str(seq_num)
        else:
            endpoint = "/firewall.ipmacbinding/table"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        seq_num: int | None = None,
        ip: str | None = None,
        mac: str | None = None,
        name: str | None = None,
        status: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing firewall/ipmacbinding/table object.

        Configure IP to MAC address pairs in the IP/MAC binding table.

        Args:
            payload_dict: Object data as dict. Must include seq-num (primary key).
            seq_num: Entry number.
            ip: IPv4 address portion of the pair (format: xxx.xxx.xxx.xxx).
            mac: MAC address portion of the pair (format = xx:xx:xx:xx:xx:xx in hexadecimal).
            name: Name of the pair (optional, default = no name).
            status: Enable/disable this IP-mac binding pair.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If seq-num is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.firewall_ipmacbinding_table.put(
            ...     seq_num=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "seq-num": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.firewall_ipmacbinding_table.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            seq_num=seq_num,
            ip=ip,
            mac=mac,
            name=name,
            status=status,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.table import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/firewall/ipmacbinding/table",
            )
        
        seq_num_value = payload_data.get("seq-num")
        if not seq_num_value:
            raise ValueError("seq-num is required for PUT")
        endpoint = "/firewall.ipmacbinding/table/" + str(seq_num_value)

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        seq_num: int | None = None,
        ip: str | None = None,
        mac: str | None = None,
        name: str | None = None,
        status: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create new firewall/ipmacbinding/table object.

        Configure IP to MAC address pairs in the IP/MAC binding table.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            seq_num: Entry number.
            ip: IPv4 address portion of the pair (format: xxx.xxx.xxx.xxx).
            mac: MAC address portion of the pair (format = xx:xx:xx:xx:xx:xx in hexadecimal).
            name: Name of the pair (optional, default = no name).
            status: Enable/disable this IP-mac binding pair.
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            raw_json: If True, return raw API response without processing.
            **kwargs: Additional parameters

        Returns:
            API response dict containing created object with assigned seq-num.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.firewall_ipmacbinding_table.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created seq-num: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = Table.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.firewall_ipmacbinding_table.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(Table.required_fields()) }}
            
            Use Table.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            seq_num=seq_num,
            ip=ip,
            mac=mac,
            name=name,
            status=status,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.table import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/firewall/ipmacbinding/table",
            )

        endpoint = "/firewall.ipmacbinding/table"
        return self._client.post(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        seq_num: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Delete firewall/ipmacbinding/table object.

        Configure IP to MAC address pairs in the IP/MAC binding table.

        Args:
            seq_num: Primary key identifier
            vdom: Virtual domain name
            raw_json: If True, return raw API response
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If seq-num is not provided

        Examples:
            >>> # Delete specific object
            >>> result = fgt.api.cmdb.firewall_ipmacbinding_table.delete(seq_num=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not seq_num:
            raise ValueError("seq-num is required for DELETE")
        endpoint = "/firewall.ipmacbinding/table/" + str(seq_num)

        return self._client.delete(
            "cmdb", endpoint, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        seq_num: int,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if firewall/ipmacbinding/table object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            seq_num: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.firewall_ipmacbinding_table.exists(seq_num=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.firewall_ipmacbinding_table.exists(seq_num=1):
            ...     fgt.api.cmdb.firewall_ipmacbinding_table.delete(seq_num=1)

        See Also:
            - get(): Retrieve full object data
            - set(): Create or update automatically based on existence
        """
        try:
            response = self.get(seq_num=seq_num, vdom=vdom, raw_json=True)
            
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
        Create or update firewall/ipmacbinding/table object (intelligent operation).

        Automatically determines whether to create (POST) or update (PUT) based on
        whether the resource exists. Requires the primary key (seq-num) in the payload.

        Args:
            payload_dict: Resource data including seq-num (primary key)
            vdom: Virtual domain name
            **kwargs: Additional parameters passed to PUT or POST

        Returns:
            API response dictionary

        Raises:
            ValueError: If seq-num is missing from payload

        Examples:
            >>> # Intelligent create or update - no need to check exists()
            >>> payload = {
            ...     "seq-num": 1,
            ...     "field1": "value1",
            ...     "field2": "value2",
            ... }
            >>> result = fgt.api.cmdb.firewall_ipmacbinding_table.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.firewall_ipmacbinding_table.set(payload_dict=obj_data)
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
        
        mkey_value = payload_dict.get("seq-num")
        if not mkey_value:
            raise ValueError("seq-num is required in payload_dict for set()")
        
        # Check if resource exists
        if self.exists(seq_num=mkey_value, vdom=vdom):
            # Update existing resource
            return self.put(payload_dict=payload_dict, vdom=vdom, **kwargs)
        else:
            # Create new resource
            return self.post(payload_dict=payload_dict, vdom=vdom, **kwargs)


