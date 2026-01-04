"""Type stubs for WAF category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import main_class
    from . import profile
    from . import signature


class Waf:
    """Type stub for Waf."""

    main_class: main_class.MainClass
    profile: profile.Profile
    signature: signature.Signature

    def __init__(self, client: IHTTPClient) -> None: ...
