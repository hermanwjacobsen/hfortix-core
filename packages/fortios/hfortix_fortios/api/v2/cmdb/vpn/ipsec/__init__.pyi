"""Type stubs for IPSEC category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import concentrator
    from . import fec
    from . import manualkey
    from . import manualkey_interface
    from . import phase1
    from . import phase1_interface
    from . import phase2
    from . import phase2_interface


class Ipsec:
    """Type stub for Ipsec."""

    concentrator: concentrator.Concentrator
    fec: fec.Fec
    manualkey: manualkey.Manualkey
    manualkey_interface: manualkey_interface.ManualkeyInterface
    phase1: phase1.Phase1
    phase1_interface: phase1_interface.Phase1Interface
    phase2: phase2.Phase2
    phase2_interface: phase2_interface.Phase2Interface

    def __init__(self, client: IHTTPClient) -> None: ...
