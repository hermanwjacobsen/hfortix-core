"""FortiOS CMDB - BlacklistedCertificates category"""

from .statistics import Statistics

__all__ = [
    "BlacklistedCertificates",
    "Statistics",
]


class BlacklistedCertificates:
    """BlacklistedCertificates endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """BlacklistedCertificates endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.statistics = Statistics(client)
