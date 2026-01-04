"""Type stubs for PRIVATE_DATA_ENCRYPTION category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import set


class PrivateDataEncryption:
    """Type stub for PrivateDataEncryption."""

    set: set.Set

    def __init__(self, client: IHTTPClient) -> None: ...
