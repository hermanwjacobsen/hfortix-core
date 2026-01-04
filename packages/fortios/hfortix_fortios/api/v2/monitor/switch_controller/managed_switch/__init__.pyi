"""Type stubs for MANAGED_SWITCH category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import bounce_port
    from . import cable_status
    from . import faceplate_xml
    from . import factory_reset
    from . import poe_reset
    from . import port_stats_reset
    from . import restart
    from . import tx_rx
    from . import update


class ManagedSwitch:
    """Type stub for ManagedSwitch."""

    bounce_port: bounce_port.BouncePort
    cable_status: cable_status.CableStatus
    faceplate_xml: faceplate_xml.FaceplateXml
    factory_reset: factory_reset.FactoryReset
    poe_reset: poe_reset.PoeReset
    port_stats_reset: port_stats_reset.PortStatsReset
    restart: restart.Restart
    tx_rx: tx_rx.TxRx
    update: update.Update

    def __init__(self, client: IHTTPClient) -> None: ...
