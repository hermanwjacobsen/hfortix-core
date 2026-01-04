"""Type stubs for AZURE category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import application_list


class Azure:
    """Type stub for Azure."""

    application_list: application_list.ApplicationList

    def __init__(self, client: IHTTPClient) -> None: ...
