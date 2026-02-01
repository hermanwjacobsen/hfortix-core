"""Type stubs for LOG category."""

from typing import TYPE_CHECKING

from .FortiOS 7 import Fortios7 as Fortios7

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
    FortiOS 7: Fortios7

    def __init__(self, client: IHTTPClient) -> None: ...