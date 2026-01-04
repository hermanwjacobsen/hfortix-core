"""Type stubs for WEB_PROXY category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import debug_url
    from . import explicit
    from . import fast_fallback
    from . import forward_server
    from . import forward_server_group
    from . import global_setting
    from . import isolator_server
    from . import profile
    from . import url_match
    from . import wisp


class WebProxy:
    """Type stub for WebProxy."""

    debug_url: debug_url.DebugUrl
    explicit: explicit.Explicit
    fast_fallback: fast_fallback.FastFallback
    forward_server: forward_server.ForwardServer
    forward_server_group: forward_server_group.ForwardServerGroup
    global_setting: global_setting.GlobalSetting
    isolator_server: isolator_server.IsolatorServer
    profile: profile.Profile
    url_match: url_match.UrlMatch
    wisp: wisp.Wisp

    def __init__(self, client: IHTTPClient) -> None: ...
