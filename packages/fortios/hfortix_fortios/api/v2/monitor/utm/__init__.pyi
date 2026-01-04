"""Type stubs for UTM category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import antivirus
    from . import app_lookup
    from . import application_categories
    from . import blacklisted_certificates
    from . import rating_lookup


class Utm:
    """Type stub for Utm."""

    rating_lookup: rating_lookup.RatingLookup
    antivirus: antivirus.Antivirus
    app_lookup: app_lookup.AppLookup
    application_categories: application_categories.ApplicationCategories
    blacklisted_certificates: blacklisted_certificates.BlacklistedCertificates

    def __init__(self, client: IHTTPClient) -> None: ...
