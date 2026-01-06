"""
FortiOS CMDB - Extension_controller dataplan

Configuration endpoint for managing cmdb extension_controller/dataplan objects.

API Endpoints:
    GET    /cmdb/extension_controller/dataplan
    POST   /cmdb/extension_controller/dataplan
    PUT    /cmdb/extension_controller/dataplan/{identifier}
    DELETE /cmdb/extension_controller/dataplan/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.extension_controller_dataplan.get()

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


class Dataplan(MetadataMixin):
    """Dataplan Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "dataplan"

    def __init__(self, client: "IHTTPClient"):
        """Initialize Dataplan endpoint."""
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
        Retrieve extension_controller/dataplan configuration.

        FortiExtender dataplan configuration.

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
            >>> # Get all extension_controller/dataplan objects
            >>> result = fgt.api.cmdb.extension_controller_dataplan.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific extension_controller/dataplan by name
            >>> result = fgt.api.cmdb.extension_controller_dataplan.get(name=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.extension_controller_dataplan.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.extension_controller_dataplan.get(action="schema")

        See Also:
            - post(): Create new extension_controller/dataplan object
            - put(): Update existing extension_controller/dataplan object
            - delete(): Remove extension_controller/dataplan object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = "/extension-controller/dataplan/" + str(name)
        else:
            endpoint = "/extension-controller/dataplan"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        name: str | None = None,
        modem_id: str | None = None,
        type: str | None = None,
        slot: str | None = None,
        iccid: str | None = None,
        carrier: str | None = None,
        apn: str | None = None,
        auth_type: str | None = None,
        username: str | None = None,
        password: Any | None = None,
        pdn: str | None = None,
        signal_threshold: int | None = None,
        signal_period: int | None = None,
        capacity: int | None = None,
        monthly_fee: int | None = None,
        billing_date: int | None = None,
        overage: str | None = None,
        preferred_subnet: int | None = None,
        private_network: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing extension_controller/dataplan object.

        FortiExtender dataplan configuration.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            name: FortiExtender data plan name.
            modem_id: Dataplan's modem specifics, if any.
            type: Type preferences configuration.
            slot: SIM slot configuration.
            iccid: ICCID configuration.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.extension_controller_dataplan.put(
            ...     name=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.extension_controller_dataplan.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            name=name,
            modem_id=modem_id,
            type=type,
            slot=slot,
            iccid=iccid,
            carrier=carrier,
            apn=apn,
            auth_type=auth_type,
            username=username,
            password=password,
            pdn=pdn,
            signal_threshold=signal_threshold,
            signal_period=signal_period,
            capacity=capacity,
            monthly_fee=monthly_fee,
            billing_date=billing_date,
            overage=overage,
            preferred_subnet=preferred_subnet,
            private_network=private_network,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.dataplan import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/extension_controller/dataplan",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = "/extension-controller/dataplan/" + str(name_value)

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        name: str | None = None,
        modem_id: str | None = None,
        type: str | None = None,
        slot: str | None = None,
        iccid: str | None = None,
        carrier: str | None = None,
        apn: str | None = None,
        auth_type: str | None = None,
        username: str | None = None,
        password: Any | None = None,
        pdn: str | None = None,
        signal_threshold: int | None = None,
        signal_period: int | None = None,
        capacity: int | None = None,
        monthly_fee: int | None = None,
        billing_date: int | None = None,
        overage: str | None = None,
        preferred_subnet: int | None = None,
        private_network: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create new extension_controller/dataplan object.

        FortiExtender dataplan configuration.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            name: FortiExtender data plan name.
            modem_id: Dataplan's modem specifics, if any.
            type: Type preferences configuration.
            slot: SIM slot configuration.
            iccid: ICCID configuration.
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            raw_json: If True, return raw API response without processing.
            **kwargs: Additional parameters

        Returns:
            API response dict containing created object with assigned name.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.extension_controller_dataplan.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created name: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = Dataplan.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.extension_controller_dataplan.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(Dataplan.required_fields()) }}
            
            Use Dataplan.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            name=name,
            modem_id=modem_id,
            type=type,
            slot=slot,
            iccid=iccid,
            carrier=carrier,
            apn=apn,
            auth_type=auth_type,
            username=username,
            password=password,
            pdn=pdn,
            signal_threshold=signal_threshold,
            signal_period=signal_period,
            capacity=capacity,
            monthly_fee=monthly_fee,
            billing_date=billing_date,
            overage=overage,
            preferred_subnet=preferred_subnet,
            private_network=private_network,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.dataplan import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/extension_controller/dataplan",
            )

        endpoint = "/extension-controller/dataplan"
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
        Delete extension_controller/dataplan object.

        FortiExtender dataplan configuration.

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
            >>> result = fgt.api.cmdb.extension_controller_dataplan.delete(name=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not name:
            raise ValueError("name is required for DELETE")
        endpoint = "/extension-controller/dataplan/" + str(name)

        return self._client.delete(
            "cmdb", endpoint, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        name: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if extension_controller/dataplan object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            name: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.extension_controller_dataplan.exists(name=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.extension_controller_dataplan.exists(name=1):
            ...     fgt.api.cmdb.extension_controller_dataplan.delete(name=1)

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
        Create or update extension_controller/dataplan object (intelligent operation).

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
            >>> result = fgt.api.cmdb.extension_controller_dataplan.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.extension_controller_dataplan.set(payload_dict=obj_data)
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


