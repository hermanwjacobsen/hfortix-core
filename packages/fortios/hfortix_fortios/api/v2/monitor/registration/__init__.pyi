"""Type stubs for REGISTRATION category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import forticare
    from . import forticloud
    from . import vdom


class Registration:
    """Type stub for Registration."""

    forticare: forticare.Forticare
    forticloud: forticloud.Forticloud
    vdom: vdom.Vdom

    def __init__(self, client: IHTTPClient) -> None: ...
