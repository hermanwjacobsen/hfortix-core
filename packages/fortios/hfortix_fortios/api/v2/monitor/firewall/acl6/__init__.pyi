"""Type stubs for ACL6 category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .clear_counters import ClearCounters


class Acl6:
    """Type stub for Acl6."""

    clear_counters: ClearCounters

    def __init__(self, client: IHTTPClient) -> None: ...
