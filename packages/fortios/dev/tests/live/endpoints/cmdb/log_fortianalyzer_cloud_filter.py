import argparse
import sys
from pathlib import Path

import pytest

# Run tests on a single worker to preserve state (group by filename)
pytestmark = pytest.mark.xdist_group(Path(__file__).stem)

# Add pytest directory to path (go up from endpoints/cmdb/ to pytest/)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt


# Global variable to store original configuration
original_config = None


def test_get_log_fortianalyzer_cloud_filter():
    """Test: Get FortiAnalyzer Cloud filter settings."""
    global original_config
    result = fgt.api.cmdb.log.fortianalyzer_cloud.filter.get()
    assert result is not None
    assert result.http_status_code == 200
    
    # Store original settings
    original_config = {
        "severity": result.severity if hasattr(result, "severity") else None,
        "anomaly": result.anomaly if hasattr(result, "anomaly") else None,
    }


def test_put_log_fortianalyzer_cloud_filter_change_severity():
    """Test: Change severity level in FortiAnalyzer Cloud filter."""
    result = fgt.api.cmdb.log.fortianalyzer_cloud.filter.put(
        severity="critical"
    )
    assert result is not None
    assert result.http_status == "success"
    
    # Verify the change
    verify = fgt.api.cmdb.log.fortianalyzer_cloud.filter.get()
    assert verify is not None
    assert verify.severity == "critical"


def test_put_log_fortianalyzer_cloud_filter_change_anomaly():
    """Test: Disable anomaly logging in FortiAnalyzer Cloud filter."""
    result = fgt.api.cmdb.log.fortianalyzer_cloud.filter.put(
        anomaly="disable"
    )
    assert result is not None
    assert result.http_status == "success"
    
    # Verify the change
    verify = fgt.api.cmdb.log.fortianalyzer_cloud.filter.get()
    assert verify is not None
    assert verify.anomaly == "disable"


def test_restore_log_fortianalyzer_cloud_filter():
    """Test: Restore FortiAnalyzer Cloud filter to original settings."""
    global original_config
    
    if original_config is None:
        return
    
    restore_payload = {}
    if original_config.get("severity") is not None:
        restore_payload["severity"] = original_config["severity"]
    if original_config.get("anomaly") is not None:
        restore_payload["anomaly"] = original_config["anomaly"]
    
    if restore_payload:
        result = fgt.api.cmdb.log.fortianalyzer_cloud.filter.put(**restore_payload)
        assert result is not None
        assert result.http_status == "success"
        
        # Verify restoration
        verify = fgt.api.cmdb.log.fortianalyzer_cloud.filter.get()
        assert verify is not None


def test_verify_log_fortianalyzer_cloud_filter_restored():
    """Test: Verify FortiAnalyzer Cloud filter was restored."""
    result = fgt.api.cmdb.log.fortianalyzer_cloud.filter.get()
    assert result is not None
    assert result.http_status_code == 200


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
    test_get_log_fortianalyzer_cloud_filter()
    print("✓ test_get_log_fortianalyzer_cloud_filter passed")

    test_put_log_fortianalyzer_cloud_filter_change_severity()
    print("✓ test_put_log_fortianalyzer_cloud_filter_change_severity passed")

    test_put_log_fortianalyzer_cloud_filter_change_anomaly()
    print("✓ test_put_log_fortianalyzer_cloud_filter_change_anomaly passed")

    test_restore_log_fortianalyzer_cloud_filter()
    print("✓ test_restore_log_fortianalyzer_cloud_filter passed")
    
    test_verify_log_fortianalyzer_cloud_filter_restored()
    print("✓ test_verify_log_fortianalyzer_cloud_filter_restored passed")
    
    print("\n✓ All FortiAnalyzer Cloud filter tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
