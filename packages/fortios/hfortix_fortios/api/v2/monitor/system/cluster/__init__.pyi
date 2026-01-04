"""Type stubs for CLUSTER category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import state


class Cluster:
    """Type stub for Cluster."""

    state: state.State

    def __init__(self, client: IHTTPClient) -> None: ...
