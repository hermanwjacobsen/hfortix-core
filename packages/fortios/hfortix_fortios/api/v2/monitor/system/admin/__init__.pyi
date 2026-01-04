"""Type stubs for ADMIN category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import change_vdom_mode


class Admin:
    """Type stub for Admin."""

    change_vdom_mode: change_vdom_mode.ChangeVdomMode

    def __init__(self, client: IHTTPClient) -> None: ...
