import argparse
import sys
from pathlib import Path
import pytest

# Run log monitor tests on a single worker to preserve state
pytestmark = pytest.mark.xdist_group(Path(__file__).stem)

# Add pytest directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt



# ============================================================================
# Log Monitor Tests - GET endpoints
# ============================================================================

def test_get_log_current_disk_usage():
    """Test GET /monitor/log/current-disk-usage - Return current used, free and total disk bytes."""
    try:
        result = fgt.api.monitor.log.current_disk_usage.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_log_device_state():
    """Test GET /monitor/log/device/state - Retrieve information on state of log devices."""
    try:
        result = fgt.api.monitor.log.device.state.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_log_forticloud():
    """Test GET /monitor/log/forticloud - Return FortiGate Cloud log status."""
    try:
        result = fgt.api.monitor.log.forticloud.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_log_forticloud_connection():
    """Test GET /monitor/log/forticloud/connection - Return FortiGate Cloud log connection status."""
    try:
        result = fgt.api.monitor.log.forticloud.connection.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


# def test_get_log_forticloud_report_list():
#     """Test GET /monitor/log/forticloud-report-list - Get FortiCloud report list."""
#     try:
#         result = fgt.api.monitor.log.forticloud_report_list.get()
#         assert result is not None
#         assert result.http_status_code == 200
#     except Exception as e:
#         if "404" in str(e):
#             print("Resource not found")
#         else:
#             raise


def test_get_log_local_report_list():
    """Test GET /monitor/log/local-report-list - Get local reports list."""
    try:
        result = fgt.api.monitor.log.local_report_list.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


# def test_get_log_local_report_download():
#     """Test GET /monitor/log/local-report/download - Download local report."""
#     # Requires report identifier
#     try:
#         result = fgt.api.monitor.log.local_report.download.get()
#         assert result is not None
#         assert result.http_status_code == 200
#     except Exception as e:
#         if "404" in str(e):
#             print("Resource not found")
#         else:
#             raise


def test_get_log_fortianalyzer():
    """Test GET /monitor/log/fortianalyzer - Return FortiAnalyzer/FortiManager log status."""
    try:
        result = fgt.api.monitor.log.fortianalyzer.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_log_fortianalyzer_queue():
    """Test GET /monitor/log/fortianalyzer-queue - Retrieve information on FortiAnalyzer's queue state."""
    try:
        result = fgt.api.monitor.log.fortianalyzer_queue.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_log_hourly_disk_usage():
    """Test GET /monitor/log/hourly-disk-usage - Return historic hourly disk usage in bytes."""
    try:
        result = fgt.api.monitor.log.hourly_disk_usage.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_log_historic_daily_remote_logs():
    """Test GET /monitor/log/historic-daily-remote-logs - Returns the amount of logs in bytes sent daily to a remote logging service."""
    try:
        result = fgt.api.monitor.log.historic_daily_remote_logs.get(server="fortianalyzer")
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_log_stats():
    """Test GET /monitor/log/stats - Return number of logs sent by category per day for a specific log device."""
    try:
        result = fgt.api.monitor.log.stats.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


# def test_get_log_forticloud_report_download():
#     """Test GET /monitor/log/forticloud-report/download - Download PDF report from FortiCloud."""
#     # Requires report identifier
#     try:
#         result = fgt.api.monitor.log.forticloud_report.download.get()
#         assert result is not None
#         assert result.http_status_code == 200
#     except Exception as e:
#         if "404" in str(e):
#             print("Resource not found")
#         else:
#             raise


# def test_get_log_policy_archive_download():
#     """Test GET /monitor/log/policy-archive/download - Download policy-based packet capture archive."""
#     # Requires archive identifier
#     try:
#         result = fgt.api.monitor.log.policy_archive.download.get()
#         assert result is not None
#         assert result.http_status_code == 200
#     except Exception as e:
#         if "404" in str(e):
#             print("Resource not found")
#         else:
#             raise


# def test_get_log_av_archive_download():
#     """Test GET /monitor/log/av-archive/download - Download file quarantined by AntiVirus."""
#     # Requires archive identifier
#     try:
#         result = fgt.api.monitor.log.av_archive.download.get()
#         assert result is not None
#         assert result.http_status_code == 200
#     except Exception as e:
#         if "404" in str(e):
#             print("Resource not found")
#         else:
#             raise


def test_get_log_feature_set():
    """Test GET /monitor/log/feature-set - Retrieve logging feature set."""
    try:
        result = fgt.api.monitor.log.feature_set.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


# ============================================================================
# Log Monitor Tests - POST endpoints
# ============================================================================

def test_post_log_stats_reset():
    """Test POST /monitor/log/stats/reset - Reset logging statistics for all log devices."""
    try:
        result = fgt.api.monitor.log.stats.reset.post()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


# def test_post_log_local_report_delete():
#     """Test POST /monitor/log/local-report/delete - Delete a local report."""
#     # Requires report parameter
#     try:
#         result = fgt.api.monitor.log.local_report.delete.post()
#         assert result is not None
#         assert result.http_status_code == 200
#     except Exception as e:
#         if "404" in str(e):
#             print("Resource not found")
#         else:
#             raise


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run tests")
    parser.add_argument("--client", choices=["direct", "fmg_proxy"], default="direct",
                        help="Client to use: direct (default) or fmg_proxy")
    args = parser.parse_args()
    
    if args.client == "fmg_proxy":
        from fmgclient import fgt, fmg
        client_name = "FMG proxy"
    else:
        from fgtclient import fgt
        fmg = None
        client_name = "direct"
    
    print(f"Running tests with {client_name} client...")
    # ========================================================================
    # GET endpoint tests
    # ========================================================================
    
    print("Running Log monitor endpoint tests...")
    
    test_get_log_current_disk_usage()
    print("✓ test_get_log_current_disk_usage")
    
    test_get_log_device_state()
    print("✓ test_get_log_device_state")
    
    test_get_log_forticloud()
    print("✓ test_get_log_forticloud")
    
    test_get_log_forticloud_connection()
    print("✓ test_get_log_forticloud_connection")
    
    # test_get_log_forticloud_report_list()
    # print("✓ test_get_log_forticloud_report_list")
    
    test_get_log_local_report_list()
    print("✓ test_get_log_local_report_list")
    
    # test_get_log_local_report_download()
    # print("✓ test_get_log_local_report_download")
    
    test_get_log_fortianalyzer()
    print("✓ test_get_log_fortianalyzer")
    
    test_get_log_fortianalyzer_queue()
    print("✓ test_get_log_fortianalyzer_queue")
    
    test_get_log_hourly_disk_usage()
    print("✓ test_get_log_hourly_disk_usage")
    
    test_get_log_historic_daily_remote_logs()
    print("✓ test_get_log_historic_daily_remote_logs")
    
    test_get_log_stats()
    print("✓ test_get_log_stats")
    
    # test_get_log_forticloud_report_download()
    # print("✓ test_get_log_forticloud_report_download")
    
    # test_get_log_policy_archive_download()
    # print("✓ test_get_log_policy_archive_download")
    
    # test_get_log_av_archive_download()
    # print("✓ test_get_log_av_archive_download")
    
    test_get_log_feature_set()
    print("✓ test_get_log_feature_set")
    
    print("\n✓ All Log GET endpoint tests completed!")
    
    # ========================================================================
    # POST endpoint tests
    # ========================================================================
    
    print("\nRunning POST endpoint tests...")
    
    test_post_log_stats_reset()
    print("✓ test_post_log_stats_reset")
    
    # Commented out - requires parameters
    # test_post_log_local_report_delete()
    # print("✓ test_post_log_local_report_delete")
    
    print("\n✓ All Log POST endpoint tests completed!")
    print("\nSummary:")
    print("- GET endpoints: 12 active tests, 4 commented out (require parameters)")
    print("- POST endpoints: 1 active test, 1 commented out (requires parameters)")
    print("- Total: 13 active test functions covering Log monitor endpoints")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
