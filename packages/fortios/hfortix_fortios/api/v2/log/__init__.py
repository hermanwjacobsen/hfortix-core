"""LOG API - Auto-generated __init__ file."""

from typing import TYPE_CHECKING

from .FortiOS 7 import Fortios7

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient


class Log:
    """Container for LOG endpoints.
    
    Provides access to log query endpoints for different storage locations:
    - disk: Logs stored on local disk
    - memory: Logs stored in memory
    - fortianalyzer: Logs from FortiAnalyzer
    - forticloud: Logs from FortiCloud
    - search: Log search operations
    """

    def __init__(self, client: "IHTTPClient"):
        """Initialize LOG category."""
        self.FortiOS 7 = Fortios7(client)
