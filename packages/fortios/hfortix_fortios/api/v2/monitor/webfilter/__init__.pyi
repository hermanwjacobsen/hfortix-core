"""Type stubs for WEBFILTER category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import category_quota
    from . import fortiguard_categories
    from . import malicious_urls
    from . import override
    from . import trusted_urls


class Webfilter:
    """Type stub for Webfilter."""

    category_quota: category_quota.CategoryQuota
    override: override.Override
    fortiguard_categories: fortiguard_categories.FortiguardCategories
    malicious_urls: malicious_urls.MaliciousUrls
    trusted_urls: trusted_urls.TrustedUrls

    def __init__(self, client: IHTTPClient) -> None: ...
