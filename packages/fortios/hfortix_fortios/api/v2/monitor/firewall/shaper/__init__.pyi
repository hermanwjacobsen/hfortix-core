"""Type stubs for SHAPER category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .multi_class_shaper import MultiClassShaper
    from .reset import Reset


class Shaper:
    """Type stub for Shaper."""

    multi_class_shaper: MultiClassShaper
    reset: Reset

    def __init__(self, client: IHTTPClient) -> None: ...
