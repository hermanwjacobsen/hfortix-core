"""
FortiOS CMDB - System ssh_config

Configuration endpoint for managing cmdb system/ssh_config objects.

API Endpoints:
    GET    /cmdb/system/ssh_config
    POST   /cmdb/system/ssh_config
    PUT    /cmdb/system/ssh_config/{identifier}
    DELETE /cmdb/system/ssh_config/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system_ssh_config.get()

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


class SshConfig(MetadataMixin):
    """SshConfig Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "ssh_config"

    def __init__(self, client: "IHTTPClient"):
        """Initialize SshConfig endpoint."""
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
        Retrieve system/ssh_config configuration.

        Configure SSH config.

        Args:
            name: Name identifier to retrieve specific object. If None, returns all objects.
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
            >>> # Get all system/ssh_config objects
            >>> result = fgt.api.cmdb.system_ssh_config.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.system_ssh_config.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.system_ssh_config.get(action="schema")

        See Also:
            - post(): Create new system/ssh_config object
            - put(): Update existing system/ssh_config object
            - delete(): Remove system/ssh_config object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/system/ssh-config/{name}"
        else:
            endpoint = "/system/ssh-config"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        ssh_kex_algo: str | list | None = None,
        ssh_enc_algo: str | list | None = None,
        ssh_mac_algo: str | list | None = None,
        ssh_hsk_algo: str | list | None = None,
        ssh_hsk_override: str | None = None,
        ssh_hsk_password: Any | None = None,
        ssh_hsk: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing system/ssh_config object.

        Configure SSH config.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            ssh_kex_algo: Select one or more SSH kex algorithms.
            ssh_enc_algo: Select one or more SSH ciphers.
            ssh_mac_algo: Select one or more SSH MAC algorithms.
            ssh_hsk_algo: Select one or more SSH hostkey algorithms.
            ssh_hsk_override: Enable/disable SSH host key override in SSH daemon.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.system_ssh_config.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.system_ssh_config.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            ssh_kex_algo=ssh_kex_algo,
            ssh_enc_algo=ssh_enc_algo,
            ssh_mac_algo=ssh_mac_algo,
            ssh_hsk_algo=ssh_hsk_algo,
            ssh_hsk_override=ssh_hsk_override,
            ssh_hsk_password=ssh_hsk_password,
            ssh_hsk=ssh_hsk,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.ssh_config import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/ssh_config",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/system/ssh-config/{name_value}"

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )





