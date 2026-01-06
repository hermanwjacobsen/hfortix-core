"""
FortiOS CMDB - System ddns

Configuration endpoint for managing cmdb system/ddns objects.

API Endpoints:
    GET    /cmdb/system/ddns
    POST   /cmdb/system/ddns
    PUT    /cmdb/system/ddns/{identifier}
    DELETE /cmdb/system/ddns/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system_ddns.get()

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


class Ddns(MetadataMixin):
    """Ddns Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "ddns"

    def __init__(self, client: "IHTTPClient"):
        """Initialize Ddns endpoint."""
        self._client = client

    def get(
        self,
        ddnsid: int | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve system/ddns configuration.

        Configure DDNS.

        Args:
            ddnsid: Integer identifier to retrieve specific object.
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
            >>> # Get all system/ddns objects
            >>> result = fgt.api.cmdb.system_ddns.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific system/ddns by ddnsid
            >>> result = fgt.api.cmdb.system_ddns.get(ddnsid=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.system_ddns.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.system_ddns.get(action="schema")

        See Also:
            - post(): Create new system/ddns object
            - put(): Update existing system/ddns object
            - delete(): Remove system/ddns object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if ddnsid:
            endpoint = "/system/ddns/" + str(ddnsid)
        else:
            endpoint = "/system/ddns"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        ddnsid: int | None = None,
        ddns_server: str | None = None,
        addr_type: str | None = None,
        server_type: str | None = None,
        ddns_server_addr: str | list | None = None,
        ddns_zone: str | None = None,
        ddns_ttl: int | None = None,
        ddns_auth: str | None = None,
        ddns_keyname: str | None = None,
        ddns_key: Any | None = None,
        ddns_domain: str | None = None,
        ddns_username: str | None = None,
        ddns_sn: str | None = None,
        ddns_password: Any | None = None,
        use_public_ip: str | None = None,
        update_interval: int | None = None,
        clear_text: str | None = None,
        ssl_certificate: str | None = None,
        bound_ip: str | None = None,
        monitor_interface: str | list | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing system/ddns object.

        Configure DDNS.

        Args:
            payload_dict: Object data as dict. Must include ddnsid (primary key).
            ddnsid: DDNS ID.
            ddns_server: Select a DDNS service provider.
            addr_type: Address type of interface address in DDNS update.
            server_type: Address type of the DDNS server.
            ddns_server_addr: Generic DDNS server IP/FQDN list.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If ddnsid is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.system_ddns.put(
            ...     ddnsid=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "ddnsid": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.system_ddns.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            ddnsid=ddnsid,
            ddns_server=ddns_server,
            addr_type=addr_type,
            server_type=server_type,
            ddns_server_addr=ddns_server_addr,
            ddns_zone=ddns_zone,
            ddns_ttl=ddns_ttl,
            ddns_auth=ddns_auth,
            ddns_keyname=ddns_keyname,
            ddns_key=ddns_key,
            ddns_domain=ddns_domain,
            ddns_username=ddns_username,
            ddns_sn=ddns_sn,
            ddns_password=ddns_password,
            use_public_ip=use_public_ip,
            update_interval=update_interval,
            clear_text=clear_text,
            ssl_certificate=ssl_certificate,
            bound_ip=bound_ip,
            monitor_interface=monitor_interface,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.ddns import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/ddns",
            )
        
        ddnsid_value = payload_data.get("ddnsid")
        if not ddnsid_value:
            raise ValueError("ddnsid is required for PUT")
        endpoint = "/system/ddns/" + str(ddnsid_value)

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        ddnsid: int | None = None,
        ddns_server: str | None = None,
        addr_type: str | None = None,
        server_type: str | None = None,
        ddns_server_addr: str | list | None = None,
        ddns_zone: str | None = None,
        ddns_ttl: int | None = None,
        ddns_auth: str | None = None,
        ddns_keyname: str | None = None,
        ddns_key: Any | None = None,
        ddns_domain: str | None = None,
        ddns_username: str | None = None,
        ddns_sn: str | None = None,
        ddns_password: Any | None = None,
        use_public_ip: str | None = None,
        update_interval: int | None = None,
        clear_text: str | None = None,
        ssl_certificate: str | None = None,
        bound_ip: str | None = None,
        monitor_interface: str | list | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create new system/ddns object.

        Configure DDNS.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            ddnsid: DDNS ID.
            ddns_server: Select a DDNS service provider.
            addr_type: Address type of interface address in DDNS update.
            server_type: Address type of the DDNS server.
            ddns_server_addr: Generic DDNS server IP/FQDN list.
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            raw_json: If True, return raw API response without processing.
            **kwargs: Additional parameters

        Returns:
            API response dict containing created object with assigned ddnsid.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.system_ddns.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created ddnsid: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = Ddns.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.system_ddns.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(Ddns.required_fields()) }}
            
            Use Ddns.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            ddnsid=ddnsid,
            ddns_server=ddns_server,
            addr_type=addr_type,
            server_type=server_type,
            ddns_server_addr=ddns_server_addr,
            ddns_zone=ddns_zone,
            ddns_ttl=ddns_ttl,
            ddns_auth=ddns_auth,
            ddns_keyname=ddns_keyname,
            ddns_key=ddns_key,
            ddns_domain=ddns_domain,
            ddns_username=ddns_username,
            ddns_sn=ddns_sn,
            ddns_password=ddns_password,
            use_public_ip=use_public_ip,
            update_interval=update_interval,
            clear_text=clear_text,
            ssl_certificate=ssl_certificate,
            bound_ip=bound_ip,
            monitor_interface=monitor_interface,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.ddns import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/ddns",
            )

        endpoint = "/system/ddns"
        return self._client.post(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        ddnsid: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Delete system/ddns object.

        Configure DDNS.

        Args:
            ddnsid: Primary key identifier
            vdom: Virtual domain name
            raw_json: If True, return raw API response
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If ddnsid is not provided

        Examples:
            >>> # Delete specific object
            >>> result = fgt.api.cmdb.system_ddns.delete(ddnsid=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not ddnsid:
            raise ValueError("ddnsid is required for DELETE")
        endpoint = "/system/ddns/" + str(ddnsid)

        return self._client.delete(
            "cmdb", endpoint, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        ddnsid: int,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if system/ddns object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            ddnsid: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.system_ddns.exists(ddnsid=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.system_ddns.exists(ddnsid=1):
            ...     fgt.api.cmdb.system_ddns.delete(ddnsid=1)

        See Also:
            - get(): Retrieve full object data
            - set(): Create or update automatically based on existence
        """
        try:
            response = self.get(ddnsid=ddnsid, vdom=vdom, raw_json=True)
            
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
        Create or update system/ddns object (intelligent operation).

        Automatically determines whether to create (POST) or update (PUT) based on
        whether the resource exists. Requires the primary key (ddnsid) in the payload.

        Args:
            payload_dict: Resource data including ddnsid (primary key)
            vdom: Virtual domain name
            **kwargs: Additional parameters passed to PUT or POST

        Returns:
            API response dictionary

        Raises:
            ValueError: If ddnsid is missing from payload

        Examples:
            >>> # Intelligent create or update - no need to check exists()
            >>> payload = {
            ...     "ddnsid": 1,
            ...     "field1": "value1",
            ...     "field2": "value2",
            ... }
            >>> result = fgt.api.cmdb.system_ddns.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.system_ddns.set(payload_dict=obj_data)
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
        
        mkey_value = payload_dict.get("ddnsid")
        if not mkey_value:
            raise ValueError("ddnsid is required in payload_dict for set()")
        
        # Check if resource exists
        if self.exists(ddnsid=mkey_value, vdom=vdom):
            # Update existing resource
            return self.put(payload_dict=payload_dict, vdom=vdom, **kwargs)
        else:
            # Create new resource
            return self.post(payload_dict=payload_dict, vdom=vdom, **kwargs)


