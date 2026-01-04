"""Type stubs for RECOMMENDATION category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import pse_config


class Recommendation:
    """Type stub for Recommendation."""

    pse_config: pse_config.PseConfig

    def __init__(self, client: IHTTPClient) -> None: ...
