"""Auto-generated category __init__ file."""

from typing import TYPE_CHECKING

from .current_disk_usage import CurrentDiskUsage
from .feature_set import FeatureSet
from .fortianalyzer import Fortianalyzer
from .fortianalyzer_queue import FortianalyzerQueue
from .forticloud import Forticloud
from .forticloud_base import Forticloud
from .hourly_disk_usage import HourlyDiskUsage
from .local_report_list import LocalReportList
from .stats import Stats
from .stats_base import Stats

if TYPE_CHECKING:
    from hfortix_core.client import FortinetClient


class Log:
    """Container for {category_name} endpoints."""

    def __init__(self, client: "FortinetClient"):
        self.current_disk_usage = CurrentDiskUsage(client)
        self.feature_set = FeatureSet(client)
        self.fortianalyzer = Fortianalyzer(client)
        self.fortianalyzer_queue = FortianalyzerQueue(client)
        self.forticloud = Forticloud(client)
        self.forticloud = Forticloud(client)
        self.hourly_disk_usage = HourlyDiskUsage(client)
        self.local_report_list = LocalReportList(client)
        self.stats = Stats(client)
        self.stats = Stats(client)
