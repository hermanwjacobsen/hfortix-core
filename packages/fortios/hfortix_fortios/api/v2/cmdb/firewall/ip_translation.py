"""
FortiOS CMDB - Firewall ip_translation

Configuration endpoint for managing cmdb firewall/ip_translation objects.

API Endpoints:
    GET    /cmdb/firewall/ip_translation
    POST   /cmdb/firewall/ip_translation
    PUT    /cmdb/firewall/ip_translation/{identifier}
    DELETE /cmdb/firewall/ip_translation/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.firewall_ip_translation.get()

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


class IpTranslation(MetadataMixin):
    """IpTranslation Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "ip_translation"

    def __init__(self, client: "IHTTPClient"):
        """Initialize IpTranslation endpoint."""
        self._client = client

    def get(
        self,
        transid: int | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve firewall/ip_translation configuration.

        Configure firewall IP-translation.

        Args:
            transid: Integer identifier to retrieve specific object.
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
            >>> # Get all firewall/ip_translation objects
            >>> result = fgt.api.cmdb.firewall_ip_translation.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific firewall/ip_translation by transid
            >>> result = fgt.api.cmdb.firewall_ip_translation.get(transid=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.firewall_ip_translation.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.firewall_ip_translation.get(action="schema")

        See Also:
            - post(): Create new firewall/ip_translation object
            - put(): Update existing firewall/ip_translation object
            - delete(): Remove firewall/ip_translation object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if transid:
            endpoint = "/firewall/ip-translation/" + str(transid)
        else:
            endpoint = "/firewall/ip-translation"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        transid: int | None = None,
        type: str | None = None,
        startip: str | None = None,
        endip: str | None = None,
        map_startip: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing firewall/ip_translation object.

        Configure firewall IP-translation.

        Args:
            payload_dict: Object data as dict. Must include transid (primary key).
            transid: IP translation ID.
            type: IP translation type (option: SCTP).
            startip: First IPv4 address (inclusive) in the range of the addresses to be translated (format xxx.xxx.xxx.xxx, default: 0.0.0.0).
            endip: Final IPv4 address (inclusive) in the range of the addresses to be translated (format xxx.xxx.xxx.xxx, default: 0.0.0.0).
            map_startip: Address to be used as the starting point for translation in the range (format xxx.xxx.xxx.xxx, default: 0.0.0.0).
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If transid is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.firewall_ip_translation.put(
            ...     transid=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "transid": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.firewall_ip_translation.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            transid=transid,
            type=type,
            startip=startip,
            endip=endip,
            map_startip=map_startip,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.ip_translation import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/firewall/ip_translation",
            )
        
        transid_value = payload_data.get("transid")
        if not transid_value:
            raise ValueError("transid is required for PUT")
        endpoint = "/firewall/ip-translation/" + str(transid_value)

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        transid: int | None = None,
        type: str | None = None,
        startip: str | None = None,
        endip: str | None = None,
        map_startip: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create new firewall/ip_translation object.

        Configure firewall IP-translation.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            transid: IP translation ID.
            type: IP translation type (option: SCTP).
            startip: First IPv4 address (inclusive) in the range of the addresses to be translated (format xxx.xxx.xxx.xxx, default: 0.0.0.0).
            endip: Final IPv4 address (inclusive) in the range of the addresses to be translated (format xxx.xxx.xxx.xxx, default: 0.0.0.0).
            map_startip: Address to be used as the starting point for translation in the range (format xxx.xxx.xxx.xxx, default: 0.0.0.0).
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            raw_json: If True, return raw API response without processing.
            **kwargs: Additional parameters

        Returns:
            API response dict containing created object with assigned transid.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.firewall_ip_translation.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created transid: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = IpTranslation.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.firewall_ip_translation.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(IpTranslation.required_fields()) }}
            
            Use IpTranslation.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            transid=transid,
            type=type,
            startip=startip,
            endip=endip,
            map_startip=map_startip,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.ip_translation import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/firewall/ip_translation",
            )

        endpoint = "/firewall/ip-translation"
        return self._client.post(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        transid: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Delete firewall/ip_translation object.

        Configure firewall IP-translation.

        Args:
            transid: Primary key identifier
            vdom: Virtual domain name
            raw_json: If True, return raw API response
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If transid is not provided

        Examples:
            >>> # Delete specific object
            >>> result = fgt.api.cmdb.firewall_ip_translation.delete(transid=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not transid:
            raise ValueError("transid is required for DELETE")
        endpoint = "/firewall/ip-translation/" + str(transid)

        return self._client.delete(
            "cmdb", endpoint, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        transid: int,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if firewall/ip_translation object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            transid: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.firewall_ip_translation.exists(transid=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.firewall_ip_translation.exists(transid=1):
            ...     fgt.api.cmdb.firewall_ip_translation.delete(transid=1)

        See Also:
            - get(): Retrieve full object data
            - set(): Create or update automatically based on existence
        """
        try:
            response = self.get(transid=transid, vdom=vdom, raw_json=True)
            
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
        Create or update firewall/ip_translation object (intelligent operation).

        Automatically determines whether to create (POST) or update (PUT) based on
        whether the resource exists. Requires the primary key (transid) in the payload.

        Args:
            payload_dict: Resource data including transid (primary key)
            vdom: Virtual domain name
            **kwargs: Additional parameters passed to PUT or POST

        Returns:
            API response dictionary

        Raises:
            ValueError: If transid is missing from payload

        Examples:
            >>> # Intelligent create or update - no need to check exists()
            >>> payload = {
            ...     "transid": 1,
            ...     "field1": "value1",
            ...     "field2": "value2",
            ... }
            >>> result = fgt.api.cmdb.firewall_ip_translation.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.firewall_ip_translation.set(payload_dict=obj_data)
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
        
        mkey_value = payload_dict.get("transid")
        if not mkey_value:
            raise ValueError("transid is required in payload_dict for set()")
        
        # Check if resource exists
        if self.exists(transid=mkey_value, vdom=vdom):
            # Update existing resource
            return self.put(payload_dict=payload_dict, vdom=vdom, **kwargs)
        else:
            # Create new resource
            return self.post(payload_dict=payload_dict, vdom=vdom, **kwargs)


