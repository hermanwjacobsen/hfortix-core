"""Type stubs for REGION_IMAGE category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .upload import Upload


class RegionImage:
    """Type stub for RegionImage."""

    upload: Upload

    def __init__(self, client: IHTTPClient) -> None: ...
