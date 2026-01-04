"""
FortiOS LOG/EVENTFILTER - 

Configuration endpoint for managing log/eventfilter  objects.

API Endpoints:
    GET    /log/eventfilter/
    POST   /log/eventfilter/
    PUT    /log/eventfilter//{identifier}
    DELETE /log/eventfilter//{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.log/eventfilter..get()

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


class :
    """ Operations."""

    def __init__(self, client: "IHTTPClient"):
        """Initialize  endpoint."""
        self._client = client

    def get(
        self,
        name: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """Retrieve configuration objects."""
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"//{name}"
        else:
            endpoint = "/"
        
        params.update(kwargs)
        return self._client.get(
            "log/eventfilter", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """Update existing resource."""
        # Build payload using helper function
        data = build_cmdb_payload(
            data=payload_dict,
        )
        
        name_value = data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"//{name_value}"

        return self._client.put(
            "log/eventfilter", endpoint, data=data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """Create new resource."""
        # Build payload using helper function
        data = build_cmdb_payload(
            data=payload_dict,
        )

        endpoint = "/"
        return self._client.post(
            "log/eventfilter", endpoint, data=data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        name: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """Delete resource."""
        if not name:
            raise ValueError("name is required for DELETE")
        endpoint = f"//{name}"

        return self._client.delete(
            "log/eventfilter", endpoint, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        name: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """Check if resource exists."""
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
        """Create or update resource (intelligent PUT/POST).
        
        Automatically determines whether to create (POST) or update (PUT) based on
        whether the resource exists. Requires the primary key in the payload.
        
        Args:
            payload_dict: Resource data including primary key
            vdom: Virtual domain name
            **kwargs: Additional parameters passed to PUT or POST
            
        Returns:
            API response dictionary
            
        Raises:
            ValueError: If primary key is missing from payload
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
