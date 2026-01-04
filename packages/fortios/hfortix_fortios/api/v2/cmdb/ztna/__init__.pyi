"""Type stubs for ZTNA category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import reverse_connector
    from . import traffic_forward_proxy
    from . import web_portal
    from . import web_portal_bookmark
    from . import web_proxy


class Ztna:
    """Type stub for Ztna."""

    reverse_connector: reverse_connector.ReverseConnector
    traffic_forward_proxy: traffic_forward_proxy.TrafficForwardProxy
    web_portal: web_portal.WebPortal
    web_portal_bookmark: web_portal_bookmark.WebPortalBookmark
    web_proxy: web_proxy.WebProxy

    def __init__(self, client: IHTTPClient) -> None: ...
