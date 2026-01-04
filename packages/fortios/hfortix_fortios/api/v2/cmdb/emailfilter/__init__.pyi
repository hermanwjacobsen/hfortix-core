"""Type stubs for EMAILFILTER category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import block_allow_list
    from . import bword
    from . import dnsbl
    from . import fortishield
    from . import iptrust
    from . import mheader
    from . import options
    from . import profile


class Emailfilter:
    """Type stub for Emailfilter."""

    block_allow_list: block_allow_list.BlockAllowList
    bword: bword.Bword
    dnsbl: dnsbl.Dnsbl
    fortishield: fortishield.Fortishield
    iptrust: iptrust.Iptrust
    mheader: mheader.Mheader
    options: options.Options
    profile: profile.Profile

    def __init__(self, client: IHTTPClient) -> None: ...
