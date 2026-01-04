"""FortiOS CMDB - Fortianalyzer category"""

from . import virus

__all__ = [
    "Fortianalyzer",
    "Virus",
]


class Fortianalyzer:
    """Fortianalyzer endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """Fortianalyzer endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.virus = virus.Virus(client)
