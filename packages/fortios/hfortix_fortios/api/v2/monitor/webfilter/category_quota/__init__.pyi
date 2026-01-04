"""Type stubs for CATEGORY_QUOTA category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import reset


class CategoryQuota:
    """Type stub for CategoryQuota."""

    reset: reset.Reset

    def __init__(self, client: IHTTPClient) -> None: ...
