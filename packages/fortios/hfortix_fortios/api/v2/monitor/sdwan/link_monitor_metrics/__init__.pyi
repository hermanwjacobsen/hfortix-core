"""Type stubs for LINK_MONITOR_METRICS category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import report


class LinkMonitorMetrics:
    """Type stub for LinkMonitorMetrics."""

    report: report.Report

    def __init__(self, client: IHTTPClient) -> None: ...
