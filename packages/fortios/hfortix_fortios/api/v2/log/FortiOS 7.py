"""
FortiOS LOG API - Fortios7

Log query endpoints for FortiOS 7 logs.

Note: LOG endpoints are read-only (GET only) and return log data.
They use nested classes to represent path parameters.

Example Usage:
    >>> fgt.api.log.FortiOS 7.6 FortiOS 7.6.5 Log API disk.get(rows=100)
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient

from hfortix_fortios.models import FortiObjectList


class Fortios7:
    """Fortios7 log operations.
    
    Provides access to FortiOS 7 log endpoints with nested classes
    for different log types and subtypes.
    """

    def __init__(self, client: "IHTTPClient"):
        """Initialize Fortios7 endpoint."""
        self._client = client
        self.x6_FortiOS_7 = Fortios7X6Fortios7(client)


class Fortios7X6Fortios7:
    """Fortios7X6Fortios7 log category."""

    def __init__(self, client: "IHTTPClient"):
        """Initialize Fortios7X6Fortios7."""
        self._client = client
        self.x6 = Fortios7X6Fortios7X6(client)

class Fortios7X6Fortios7X6:
    """Fortios7X6Fortios7X6 log category."""

    def __init__(self, client: "IHTTPClient"):
        """Initialize Fortios7X6Fortios7X6."""
        self._client = client
        self.x5_Log_API_disk = Fortios7X6Fortios7X6X5LogApiDisk(client)
        self.x5_Log_API_fortianalyzer = Fortios7X6Fortios7X6X5LogApiFortianalyzer(client)
        self.x5_Log_API_forticloud = Fortios7X6Fortios7X6X5LogApiForticloud(client)
        self.x5_Log_API_memory = Fortios7X6Fortios7X6X5LogApiMemory(client)
        self.x5_Log_API_search = Fortios7X6Fortios7X6X5LogApiSearch(client)

class Fortios7X6Fortios7X6X5LogApiDisk:
    """Fortios7 6 FortiOS 7 6 5 Log API disk log operations."""

    def __init__(self, client: "IHTTPClient"):
        """Initialize Fortios7X6Fortios7X6X5LogApiDisk."""
        self._client = client

    def get(
        self,
        *,
        rows: int | None = None,
        session_id: int | None = None,
        serial_no: str | None = None,
        is_ha_member: bool | None = None,
        filter: str | None = None,
        extra: str | None = None,
        vdom: str | None = None,
    ) -> FortiObjectList:
        """
        Get 6 FortiOS 7 6 5 Log API disk logs.

        Args:
            rows: Number of rows to return (default: server decides)
            session_id: Session ID for paginated retrieval (from previous response)
            serial_no: Retrieve logs from specific device serial number
            is_ha_member: Whether the device is an HA member
            filter: Filter expression (e.g., "srcip==192.168.1.1")
            extra: Extra data flags [reverse_lookup|country_id]
            vdom: Virtual domain (if not using default)

        Returns:
            FortiObjectList containing log records with metadata

        Example:
            >>> logs = fgt.api.log.FortiOS 7.6 FortiOS 7.6.5 Log API disk.get(rows=100)
            >>> for log in logs:
            ...     print(log.srcip, log.dstip)
        """
        params: dict[str, Any] = {}
        if rows is not None:
            params["rows"] = rows
        if session_id is not None:
            params["session_id"] = session_id
        if serial_no is not None:
            params["serial_no"] = serial_no
        if is_ha_member is not None:
            params["is_ha_member"] = is_ha_member
        if filter is not None:
            params["filter"] = filter
        if extra is not None:
            params["extra"] = extra
        if vdom is not None:
            params["vdom"] = vdom

        result = self._client.get("log", "FortiOS 7/6 FortiOS 7/6/5 Log API disk", params=params if params else None)
        return result

class Fortios7X6Fortios7X6X5LogApiFortianalyzer:
    """Fortios7 6 FortiOS 7 6 5 Log API fortianalyzer log operations."""

    def __init__(self, client: "IHTTPClient"):
        """Initialize Fortios7X6Fortios7X6X5LogApiFortianalyzer."""
        self._client = client

    def get(
        self,
        *,
        rows: int | None = None,
        session_id: int | None = None,
        serial_no: str | None = None,
        is_ha_member: bool | None = None,
        filter: str | None = None,
        extra: str | None = None,
        vdom: str | None = None,
    ) -> FortiObjectList:
        """
        Get 6 FortiOS 7 6 5 Log API fortianalyzer logs.

        Args:
            rows: Number of rows to return (default: server decides)
            session_id: Session ID for paginated retrieval (from previous response)
            serial_no: Retrieve logs from specific device serial number
            is_ha_member: Whether the device is an HA member
            filter: Filter expression (e.g., "srcip==192.168.1.1")
            extra: Extra data flags [reverse_lookup|country_id]
            vdom: Virtual domain (if not using default)

        Returns:
            FortiObjectList containing log records with metadata

        Example:
            >>> logs = fgt.api.log.FortiOS 7.6 FortiOS 7.6.5 Log API fortianalyzer.get(rows=100)
            >>> for log in logs:
            ...     print(log.srcip, log.dstip)
        """
        params: dict[str, Any] = {}
        if rows is not None:
            params["rows"] = rows
        if session_id is not None:
            params["session_id"] = session_id
        if serial_no is not None:
            params["serial_no"] = serial_no
        if is_ha_member is not None:
            params["is_ha_member"] = is_ha_member
        if filter is not None:
            params["filter"] = filter
        if extra is not None:
            params["extra"] = extra
        if vdom is not None:
            params["vdom"] = vdom

        result = self._client.get("log", "FortiOS 7/6 FortiOS 7/6/5 Log API fortianalyzer", params=params if params else None)
        return result

class Fortios7X6Fortios7X6X5LogApiForticloud:
    """Fortios7 6 FortiOS 7 6 5 Log API forticloud log operations."""

    def __init__(self, client: "IHTTPClient"):
        """Initialize Fortios7X6Fortios7X6X5LogApiForticloud."""
        self._client = client

    def get(
        self,
        *,
        rows: int | None = None,
        session_id: int | None = None,
        serial_no: str | None = None,
        is_ha_member: bool | None = None,
        filter: str | None = None,
        extra: str | None = None,
        vdom: str | None = None,
    ) -> FortiObjectList:
        """
        Get 6 FortiOS 7 6 5 Log API forticloud logs.

        Args:
            rows: Number of rows to return (default: server decides)
            session_id: Session ID for paginated retrieval (from previous response)
            serial_no: Retrieve logs from specific device serial number
            is_ha_member: Whether the device is an HA member
            filter: Filter expression (e.g., "srcip==192.168.1.1")
            extra: Extra data flags [reverse_lookup|country_id]
            vdom: Virtual domain (if not using default)

        Returns:
            FortiObjectList containing log records with metadata

        Example:
            >>> logs = fgt.api.log.FortiOS 7.6 FortiOS 7.6.5 Log API forticloud.get(rows=100)
            >>> for log in logs:
            ...     print(log.srcip, log.dstip)
        """
        params: dict[str, Any] = {}
        if rows is not None:
            params["rows"] = rows
        if session_id is not None:
            params["session_id"] = session_id
        if serial_no is not None:
            params["serial_no"] = serial_no
        if is_ha_member is not None:
            params["is_ha_member"] = is_ha_member
        if filter is not None:
            params["filter"] = filter
        if extra is not None:
            params["extra"] = extra
        if vdom is not None:
            params["vdom"] = vdom

        result = self._client.get("log", "FortiOS 7/6 FortiOS 7/6/5 Log API forticloud", params=params if params else None)
        return result

class Fortios7X6Fortios7X6X5LogApiMemory:
    """Fortios7 6 FortiOS 7 6 5 Log API memory log operations."""

    def __init__(self, client: "IHTTPClient"):
        """Initialize Fortios7X6Fortios7X6X5LogApiMemory."""
        self._client = client

    def get(
        self,
        *,
        rows: int | None = None,
        session_id: int | None = None,
        serial_no: str | None = None,
        is_ha_member: bool | None = None,
        filter: str | None = None,
        extra: str | None = None,
        vdom: str | None = None,
    ) -> FortiObjectList:
        """
        Get 6 FortiOS 7 6 5 Log API memory logs.

        Args:
            rows: Number of rows to return (default: server decides)
            session_id: Session ID for paginated retrieval (from previous response)
            serial_no: Retrieve logs from specific device serial number
            is_ha_member: Whether the device is an HA member
            filter: Filter expression (e.g., "srcip==192.168.1.1")
            extra: Extra data flags [reverse_lookup|country_id]
            vdom: Virtual domain (if not using default)

        Returns:
            FortiObjectList containing log records with metadata

        Example:
            >>> logs = fgt.api.log.FortiOS 7.6 FortiOS 7.6.5 Log API memory.get(rows=100)
            >>> for log in logs:
            ...     print(log.srcip, log.dstip)
        """
        params: dict[str, Any] = {}
        if rows is not None:
            params["rows"] = rows
        if session_id is not None:
            params["session_id"] = session_id
        if serial_no is not None:
            params["serial_no"] = serial_no
        if is_ha_member is not None:
            params["is_ha_member"] = is_ha_member
        if filter is not None:
            params["filter"] = filter
        if extra is not None:
            params["extra"] = extra
        if vdom is not None:
            params["vdom"] = vdom

        result = self._client.get("log", "FortiOS 7/6 FortiOS 7/6/5 Log API memory", params=params if params else None)
        return result

class Fortios7X6Fortios7X6X5LogApiSearch:
    """Fortios7 6 FortiOS 7 6 5 Log API search log operations."""

    def __init__(self, client: "IHTTPClient"):
        """Initialize Fortios7X6Fortios7X6X5LogApiSearch."""
        self._client = client

    def get(
        self,
        *,
        rows: int | None = None,
        session_id: int | None = None,
        serial_no: str | None = None,
        is_ha_member: bool | None = None,
        filter: str | None = None,
        extra: str | None = None,
        vdom: str | None = None,
    ) -> FortiObjectList:
        """
        Get 6 FortiOS 7 6 5 Log API search logs.

        Args:
            rows: Number of rows to return (default: server decides)
            session_id: Session ID for paginated retrieval (from previous response)
            serial_no: Retrieve logs from specific device serial number
            is_ha_member: Whether the device is an HA member
            filter: Filter expression (e.g., "srcip==192.168.1.1")
            extra: Extra data flags [reverse_lookup|country_id]
            vdom: Virtual domain (if not using default)

        Returns:
            FortiObjectList containing log records with metadata

        Example:
            >>> logs = fgt.api.log.FortiOS 7.6 FortiOS 7.6.5 Log API search.get(rows=100)
            >>> for log in logs:
            ...     print(log.srcip, log.dstip)
        """
        params: dict[str, Any] = {}
        if rows is not None:
            params["rows"] = rows
        if session_id is not None:
            params["session_id"] = session_id
        if serial_no is not None:
            params["serial_no"] = serial_no
        if is_ha_member is not None:
            params["is_ha_member"] = is_ha_member
        if filter is not None:
            params["filter"] = filter
        if extra is not None:
            params["extra"] = extra
        if vdom is not None:
            params["vdom"] = vdom

        result = self._client.get("log", "FortiOS 7/6 FortiOS 7/6/5 Log API search", params=params if params else None)
        return result
