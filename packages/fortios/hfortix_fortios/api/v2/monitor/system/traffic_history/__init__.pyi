"""Type stubs for TRAFFIC_HISTORY category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import enable_app_bandwidth_tracking
    from . import interface
    from . import top_applications


class TrafficHistory:
    """Type stub for TrafficHistory."""

    enable_app_bandwidth_tracking: enable_app_bandwidth_tracking.EnableAppBandwidthTracking
    interface: interface.Interface
    top_applications: top_applications.TopApplications

    def __init__(self, client: IHTTPClient) -> None: ...
