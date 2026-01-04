"""Type stubs for WEBFILTER category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import content
    from . import content_header
    from . import fortiguard
    from . import ftgd_local_cat
    from . import ftgd_local_rating
    from . import ftgd_local_risk
    from . import ftgd_risk_level
    from . import ips_urlfilter_cache_setting
    from . import ips_urlfilter_setting
    from . import ips_urlfilter_setting6
    from . import override
    from . import profile
    from . import search_engine
    from . import urlfilter


class Webfilter:
    """Type stub for Webfilter."""

    content: content.Content
    content_header: content_header.ContentHeader
    fortiguard: fortiguard.Fortiguard
    ftgd_local_cat: ftgd_local_cat.FtgdLocalCat
    ftgd_local_rating: ftgd_local_rating.FtgdLocalRating
    ftgd_local_risk: ftgd_local_risk.FtgdLocalRisk
    ftgd_risk_level: ftgd_risk_level.FtgdRiskLevel
    ips_urlfilter_cache_setting: ips_urlfilter_cache_setting.IpsUrlfilterCacheSetting
    ips_urlfilter_setting: ips_urlfilter_setting.IpsUrlfilterSetting
    ips_urlfilter_setting6: ips_urlfilter_setting6.IpsUrlfilterSetting6
    override: override.Override
    profile: profile.Profile
    search_engine: search_engine.SearchEngine
    urlfilter: urlfilter.Urlfilter

    def __init__(self, client: IHTTPClient) -> None: ...
