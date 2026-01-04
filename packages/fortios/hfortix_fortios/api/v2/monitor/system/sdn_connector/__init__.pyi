"""Type stubs for SDN_CONNECTOR category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import update
    from . import validate_gcp_key


class SdnConnector:
    """Type stub for SdnConnector."""

    update: update.Update
    validate_gcp_key: validate_gcp_key.ValidateGcpKey

    def __init__(self, client: IHTTPClient) -> None: ...
