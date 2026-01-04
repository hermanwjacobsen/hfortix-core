"""Type stubs for ACL category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import group
    from . import ingress


class Acl:
    """Type stub for Acl."""

    group: group.Group
    ingress: ingress.Ingress

    def __init__(self, client: IHTTPClient) -> None: ...
