"""Type stubs for LOG FortiOS 7 endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient

from hfortix_fortios.models import FortiObjectList


class Fortios7:
    """Fortios7 log operations."""
    x6_FortiOS_7: Fortios7X6Fortios7

    def __init__(self, client: IHTTPClient) -> None: ...


class Fortios7X6Fortios7:
    """Fortios7X6Fortios7 log category."""
    x6: Fortios7X6Fortios7X6

    def __init__(self, client: IHTTPClient) -> None: ...

class Fortios7X6Fortios7X6:
    """Fortios7X6Fortios7X6 log category."""
    x5_Log_API_disk: Fortios7X6Fortios7X6X5LogApiDisk
    x5_Log_API_fortianalyzer: Fortios7X6Fortios7X6X5LogApiFortianalyzer
    x5_Log_API_forticloud: Fortios7X6Fortios7X6X5LogApiForticloud
    x5_Log_API_memory: Fortios7X6Fortios7X6X5LogApiMemory
    x5_Log_API_search: Fortios7X6Fortios7X6X5LogApiSearch

    def __init__(self, client: IHTTPClient) -> None: ...

class Fortios7X6Fortios7X6X5LogApiDisk:
    """Fortios7 6 FortiOS 7 6 5 Log API disk log operations."""

    def __init__(self, client: IHTTPClient) -> None: ...

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
            rows: Number of rows to return
            session_id: Session ID for paginated retrieval
            serial_no: Retrieve logs from specific device
            is_ha_member: Whether the device is an HA member
            filter: Filter expression
            extra: Extra data flags
            vdom: Virtual domain

        Returns:
            FortiObjectList containing log records
        """
        ...

class Fortios7X6Fortios7X6X5LogApiFortianalyzer:
    """Fortios7 6 FortiOS 7 6 5 Log API fortianalyzer log operations."""

    def __init__(self, client: IHTTPClient) -> None: ...

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
            rows: Number of rows to return
            session_id: Session ID for paginated retrieval
            serial_no: Retrieve logs from specific device
            is_ha_member: Whether the device is an HA member
            filter: Filter expression
            extra: Extra data flags
            vdom: Virtual domain

        Returns:
            FortiObjectList containing log records
        """
        ...

class Fortios7X6Fortios7X6X5LogApiForticloud:
    """Fortios7 6 FortiOS 7 6 5 Log API forticloud log operations."""

    def __init__(self, client: IHTTPClient) -> None: ...

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
            rows: Number of rows to return
            session_id: Session ID for paginated retrieval
            serial_no: Retrieve logs from specific device
            is_ha_member: Whether the device is an HA member
            filter: Filter expression
            extra: Extra data flags
            vdom: Virtual domain

        Returns:
            FortiObjectList containing log records
        """
        ...

class Fortios7X6Fortios7X6X5LogApiMemory:
    """Fortios7 6 FortiOS 7 6 5 Log API memory log operations."""

    def __init__(self, client: IHTTPClient) -> None: ...

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
            rows: Number of rows to return
            session_id: Session ID for paginated retrieval
            serial_no: Retrieve logs from specific device
            is_ha_member: Whether the device is an HA member
            filter: Filter expression
            extra: Extra data flags
            vdom: Virtual domain

        Returns:
            FortiObjectList containing log records
        """
        ...

class Fortios7X6Fortios7X6X5LogApiSearch:
    """Fortios7 6 FortiOS 7 6 5 Log API search log operations."""

    def __init__(self, client: IHTTPClient) -> None: ...

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
            rows: Number of rows to return
            session_id: Session ID for paginated retrieval
            serial_no: Retrieve logs from specific device
            is_ha_member: Whether the device is an HA member
            filter: Filter expression
            extra: Extra data flags
            vdom: Virtual domain

        Returns:
            FortiObjectList containing log records
        """
        ...
