"""Type stubs for ROGUE_AP category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .clear_all import ClearAll
    from .set_status import SetStatus


class RogueAp:
    """Type stub for RogueAp."""

    clear_all: ClearAll
    set_status: SetStatus

    def __init__(self, client: IHTTPClient) -> None: ...
