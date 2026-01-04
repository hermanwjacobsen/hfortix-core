"""FortiOS Monitor - Sdwan category"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient

from .link_monitor_metrics.report import Report

class LinkMonitorMetricsEndpoints:
    """Endpoints under link_monitor_metrics."""

    def __init__(self, client):
        self.report = Report(client)


class Sdwan:
    """Sdwan endpoints wrapper for Monitor API."""

    def __init__(self, client: "IHTTPClient"):
        """Sdwan endpoints."""
        self.link_monitor_metrics = LinkMonitorMetricsEndpoints(client)


__all__ = ["Sdwan"]
