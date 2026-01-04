"""FortiOS CMDB - Utm category"""

from . import rating_lookup
from .antivirus import Antivirus
from .app_lookup import AppLookup
from .application_categories import ApplicationCategories
from .blacklisted_certificates import BlacklistedCertificates

__all__ = [
    "Antivirus",
    "AppLookup",
    "ApplicationCategories",
    "BlacklistedCertificates",
    "RatingLookup",
    "Utm",
]


class Utm:
    """Utm endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """Utm endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.rating_lookup = rating_lookup.RatingLookup(client)
        self.antivirus = Antivirus(client)
        self.app_lookup = AppLookup(client)
        self.application_categories = ApplicationCategories(client)
        self.blacklisted_certificates = BlacklistedCertificates(client)
