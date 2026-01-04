"""Type stubs for LOG category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import av_archive
    from . import current_disk_usage
    from . import device
    from . import feature_set
    from . import fortianalyzer
    from . import fortianalyzer_queue
    from . import forticloud
    from . import forticloud_report
    from . import forticloud_report_list
    from . import historic_daily_remote_logs
    from . import hourly_disk_usage
    from . import local_report
    from . import local_report_list
    from . import policy_archive
    from . import stats


class Log:
    """Type stub for Log."""

    av_archive: av_archive.AvArchive
    forticloud_report: forticloud_report.ForticloudReport
    local_report: local_report.LocalReport
    policy_archive: policy_archive.PolicyArchive
    stats: stats.Stats
    current_disk_usage: current_disk_usage.CurrentDiskUsage
    device: device.Device
    feature_set: feature_set.FeatureSet
    fortianalyzer: fortianalyzer.Fortianalyzer
    fortianalyzer_queue: fortianalyzer_queue.FortianalyzerQueue
    forticloud: forticloud.Forticloud
    forticloud_report_list: forticloud_report_list.ForticloudReportList
    historic_daily_remote_logs: historic_daily_remote_logs.HistoricDailyRemoteLogs
    hourly_disk_usage: hourly_disk_usage.HourlyDiskUsage
    local_report_list: local_report_list.LocalReportList

    def __init__(self, client: IHTTPClient) -> None: ...
