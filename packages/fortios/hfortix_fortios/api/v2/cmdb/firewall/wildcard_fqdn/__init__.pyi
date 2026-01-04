"""Type stubs for WILDCARD_FQDN category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import custom
    from . import group


class WildcardFqdn:
    """Type stub for WildcardFqdn."""

    custom: custom.Custom
    group: group.Group

    def __init__(self, client: IHTTPClient) -> None: ...
