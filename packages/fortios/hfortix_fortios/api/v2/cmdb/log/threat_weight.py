"""
FortiOS CMDB - Log threat_weight

Configuration endpoint for managing cmdb log/threat_weight objects.

API Endpoints:
    GET    /cmdb/log/threat_weight
    POST   /cmdb/log/threat_weight
    PUT    /cmdb/log/threat_weight/{identifier}
    DELETE /cmdb/log/threat_weight/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.log_threat_weight.get()

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


class ThreatWeight(MetadataMixin):
    """ThreatWeight Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "threat_weight"

    def __init__(self, client: "IHTTPClient"):
        """Initialize ThreatWeight endpoint."""
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
        Retrieve log/threat_weight configuration.

        Configure threat weight settings.

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
            >>> # Get all log/threat_weight objects
            >>> result = fgt.api.cmdb.log_threat_weight.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.log_threat_weight.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.log_threat_weight.get(action="schema")

        See Also:
            - post(): Create new log/threat_weight object
            - put(): Update existing log/threat_weight object
            - delete(): Remove log/threat_weight object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/log/threat-weight/{name}"
        else:
            endpoint = "/log/threat-weight"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        status: str | None = None,
        level: str | None = None,
        blocked_connection: str | None = None,
        failed_connection: str | None = None,
        url_block_detected: str | None = None,
        botnet_connection_detected: str | None = None,
        malware: str | None = None,
        ips: str | None = None,
        web: str | list | None = None,
        geolocation: str | list | None = None,
        application: str | list | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing log/threat_weight object.

        Configure threat weight settings.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            status: Enable/disable the threat weight feature.
            level: Score mapping for threat weight levels.
            blocked_connection: Threat weight score for blocked connections.
            failed_connection: Threat weight score for failed connections.
            url_block_detected: Threat weight score for URL blocking.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.log_threat_weight.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.log_threat_weight.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            status=status,
            level=level,
            blocked_connection=blocked_connection,
            failed_connection=failed_connection,
            url_block_detected=url_block_detected,
            botnet_connection_detected=botnet_connection_detected,
            malware=malware,
            ips=ips,
            web=web,
            geolocation=geolocation,
            application=application,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.threat_weight import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/log/threat_weight",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/log/threat-weight/{name_value}"

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )





