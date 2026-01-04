"""Type stubs for QOS category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import dot1p_map
    from . import ip_dscp_map
    from . import qos_policy
    from . import queue_policy


class Qos:
    """Type stub for Qos."""

    dot1p_map: dot1p_map.Dot1pMap
    ip_dscp_map: ip_dscp_map.IpDscpMap
    qos_policy: qos_policy.QosPolicy
    queue_policy: queue_policy.QueuePolicy

    def __init__(self, client: IHTTPClient) -> None: ...
