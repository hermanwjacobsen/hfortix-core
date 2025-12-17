"""
FortiOS CMDB - System LldpNetworkPolicy

Configure LLDP network policy.

API Endpoints:
    GET    /system.lldp/network-policy           - List all lldp network-policy
    GET    /system.lldp/network-policy/{name}   - Get specific lldp network-policy
    POST   /system.lldp/network-policy           - Create lldp network-policy
    PUT    /system.lldp/network-policy/{name}   - Update lldp network-policy
    DELETE /system.lldp/network-policy/{name}   - Delete lldp network-policy
"""
from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient

from hfortix.FortiOS.http_client import encode_path_component


class LldpNetworkPolicy:
    """lldp network-policy endpoint"""

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize LldpNetworkPolicy endpoint

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def list(self, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        """
        List all lldp network-policy

        Args:
            vdom (str/bool, optional): Virtual domain, False to skip
            **kwargs: Additional query parameters

        Returns:
            dict: API response with list of lldp network-policy

        Examples:
            >>> # List all lldp network-policy
            >>> result = fgt.api.cmdb.system.lldp_network_policy.list()
            >>> for item in result['results']:
            ...     print(item['name'])
        """
        return self.get(vdom=vdom, **kwargs)

    def get(
        self,
        name: Optional[str] = None,
        datasource: Optional[bool] = None,
        with_meta: Optional[bool] = None,
        skip: Optional[bool] = None,
        action: Optional[str] = None,
        format: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[int] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Get lldp network-policy

        Args:
            name (str, optional): Object name (get specific object)
            datasource (bool, optional): Include datasource information
            with_meta (bool, optional): Include metadata
            skip (bool, optional): Enable CLI skip operator
            action (str, optional): Special actions
            format (str, optional): Field list to return
            filter (str, optional): Filter expression
            count (int, optional): Maximum number of entries
            vdom (str/bool, optional): Virtual domain, False to skip
            **kwargs: Additional query parameters

        Returns:
            dict: API response

        Examples:
            >>> # Get all
            >>> result = fgt.api.cmdb.system.lldp_network_policy.get()
            
            >>> # Get specific by name
            >>> result = fgt.api.cmdb.system.lldp_network_policy.get(name='obj1')
        """
        params = {}
        
        param_map = {
            "datasource": datasource,
            "with_meta": with_meta,
            "skip": skip,
            "action": action,
            "format": format,
            "filter": filter,
            "count": count,
        }
        
        for key, value in param_map.items():
            if value is not None:
                params[key] = value
        
        params.update(kwargs)
        
        path = "system.lldp/network-policy"
        if name:
            path = f"{path}/{encode_path_component(name)}"
        
        return self._client.get("cmdb", path, params=params if params else None, vdom=vdom)

    def create(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Create new lldp network-policy

        Args:
            payload_dict (dict, optional): Complete configuration as dictionary
            name (str, optional): Object name
            vdom (str/bool, optional): Virtual domain, False to skip
            **kwargs: Additional parameters

        Returns:
            dict: API response

        Examples:
            >>> # Create with dictionary
            >>> result = fgt.api.cmdb.system.lldp_network_policy.create(
            ...     payload_dict={'name': 'obj1', 'comment': 'Test'}
            ... )
            
            >>> # Create with parameters
            >>> result = fgt.api.cmdb.system.lldp_network_policy.create(
            ...     name='obj1',
            ...     comment='Test'
            ... )
        """
        data = payload_dict.copy() if payload_dict else {}
        
        if name is not None:
            data["name"] = name
        
        for key, value in kwargs.items():
            if value is not None:
                api_key = key.replace("_", "-")
                data[api_key] = value
        
        return self._client.post("cmdb", "system.lldp/network-policy", data=data, vdom=vdom)

    def update(
        self,
        name: str,
        payload_dict: Optional[Dict[str, Any]] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update lldp network-policy

        Args:
            name (str): Object name (required)
            payload_dict (dict, optional): Complete configuration as dictionary
            vdom (str/bool, optional): Virtual domain, False to skip
            **kwargs: Additional parameters to update

        Returns:
            dict: API response

        Examples:
            >>> # Update with dictionary
            >>> result = fgt.api.cmdb.system.lldp_network_policy.update(
            ...     name='obj1',
            ...     payload_dict={'comment': 'Updated'}
            ... )
            
            >>> # Update with parameters
            >>> result = fgt.api.cmdb.system.lldp_network_policy.update(
            ...     name='obj1',
            ...     comment='Updated'
            ... )
        """
        data = payload_dict.copy() if payload_dict else {}
        
        for key, value in kwargs.items():
            if value is not None:
                api_key = key.replace("_", "-")
                data[api_key] = value
        
        return self._client.put("cmdb", f"system.lldp/network-policy/{encode_path_component(name)}", data=data, vdom=vdom)

    def delete(
        self,
        name: str,
        vdom: Optional[Union[str, bool]] = None,
    ) -> dict[str, Any]:
        """
        Delete lldp network-policy

        Args:
            name (str): Object name to delete
            vdom (str/bool, optional): Virtual domain, False to skip

        Returns:
            dict: API response

        Examples:
            >>> result = fgt.api.cmdb.system.lldp_network_policy.delete('obj1')
        """
        return self._client.delete("cmdb", f"system.lldp/network-policy/{encode_path_component(name)}", vdom=vdom)

    def exists(self, name: str, vdom: Optional[Union[str, bool]] = None) -> bool:
        """
        Check if lldp network-policy exists

        Args:
            name (str): Object name to check
            vdom (str/bool, optional): Virtual domain, False to skip

        Returns:
            bool: True if exists, False otherwise

        Examples:
            >>> if fgt.api.cmdb.system.lldp_network_policy.exists('obj1'):
            ...     print("Exists")
        """
        try:
            result = self.get(name=name, vdom=vdom)
            return result.get("status") == "success"
        except Exception:
            return False
