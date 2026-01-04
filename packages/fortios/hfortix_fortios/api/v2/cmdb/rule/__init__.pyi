"""Type stubs for RULE category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import fmwp
    from . import iotd
    from . import otdt
    from . import otvp


class Rule:
    """Type stub for Rule."""

    fmwp: fmwp.Fmwp
    iotd: iotd.Iotd
    otdt: otdt.Otdt
    otvp: otvp.Otvp

    def __init__(self, client: IHTTPClient) -> None: ...
