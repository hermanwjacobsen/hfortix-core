"""Type stubs for VDOM category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import add_license


class Vdom:
    """Type stub for Vdom."""

    add_license: add_license.AddLicense

    def __init__(self, client: IHTTPClient) -> None: ...
