"""Type stubs for OVERRIDE category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .delete import Delete


class Override:
    """Type stub for Override."""

    delete: Delete

    def __init__(self, client: IHTTPClient) -> None: ...
