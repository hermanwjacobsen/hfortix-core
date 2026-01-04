"""Type stubs for ENDPOINT_CONTROL category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import avatar
    from . import ems
    from . import installer
    from . import record_list
    from . import summary


class EndpointControl:
    """Type stub for EndpointControl."""

    avatar: avatar.Avatar
    ems: ems.Ems
    installer: installer.Installer
    record_list: record_list.RecordList
    summary: summary.Summary

    def __init__(self, client: IHTTPClient) -> None: ...
