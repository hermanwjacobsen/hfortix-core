"""Type stubs for SERVICE category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import category
    from . import custom
    from . import group


class Service:
    """Type stub for Service."""

    category: category.Category
    custom: custom.Custom
    group: group.Group

    def __init__(self, client: IHTTPClient) -> None: ...
