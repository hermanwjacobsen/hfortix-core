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


def test_get_log_fortianalyzer_cloud_override_filter():
    """Test: Get FortiAnalyzer Cloud override filter settings."""
    global original_config
    result = fgt.api.cmdb.log.fortianalyzer_cloud.override_filter.get(vdom="test")
    assert result is not None
    assert result.http_status_code == 200
    
    # Store original settings
    original_config = {
        "severity": result.severity if hasattr(result, "severity") else None,
        "voip": result.voip if hasattr(result, "voip") else None,
    }


def test_put_log_fortianalyzer_cloud_override_filter_change_severity():
    """Test: Change severity level in FortiAnalyzer Cloud override filter."""
    result = fgt.api.cmdb.log.fortianalyzer_cloud.override_filter.put(
        severity="error",
        vdom="test"
    )
    assert result is not None
    assert result.http_status == "success"
    
    # Verify the change
    verify = fgt.api.cmdb.log.fortianalyzer_cloud.override_filter.get(vdom="test")
    assert verify is not None
    assert verify.severity == "error"


def test_put_log_fortianalyzer_cloud_override_filter_change_voip():
    """Test: Enable VoIP logging in FortiAnalyzer Cloud override filter."""
    result = fgt.api.cmdb.log.fortianalyzer_cloud.override_filter.put(
        voip="enable",
        vdom="test"
    )
    assert result is not None
    assert result.http_status == "success"
    
    # Verify the change
    verify = fgt.api.cmdb.log.fortianalyzer_cloud.override_filter.get(vdom="test")
    assert verify is not None
    assert verify.voip == "enable"


def test_restore_log_fortianalyzer_cloud_override_filter():
    """Test: Restore FortiAnalyzer Cloud override filter to original settings."""
    global original_config
    
    if original_config is None:
        return
    
    restore_payload = {}
    if original_config.get("severity") is not None:
        restore_payload["severity"] = original_config["severity"]
    if original_config.get("voip") is not None:
        restore_payload["voip"] = original_config["voip"]
    
    if restore_payload:
        restore_payload["vdom"] = "test"
        result = fgt.api.cmdb.log.fortianalyzer_cloud.override_filter.put(**restore_payload)
        assert result is not None
        assert result.http_status == "success"
        
        # Verify restoration
        verify = fgt.api.cmdb.log.fortianalyzer_cloud.override_filter.get(vdom="test")
        assert verify is not None


def test_verify_log_fortianalyzer_cloud_override_filter_restored():
    """Test: Verify FortiAnalyzer Cloud override filter was restored."""
    result = fgt.api.cmdb.log.fortianalyzer_cloud.override_filter.get(vdom="test")
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
    test_get_log_fortianalyzer_cloud_override_filter()
    print("✓ test_get_log_fortianalyzer_cloud_override_filter passed")

    test_put_log_fortianalyzer_cloud_override_filter_change_severity()
    print("✓ test_put_log_fortianalyzer_cloud_override_filter_change_severity passed")

    test_put_log_fortianalyzer_cloud_override_filter_change_voip()
    print("✓ test_put_log_fortianalyzer_cloud_override_filter_change_voip passed")

    test_restore_log_fortianalyzer_cloud_override_filter()
    print("✓ test_restore_log_fortianalyzer_cloud_override_filter passed")
    
    test_verify_log_fortianalyzer_cloud_override_filter_restored()
    print("✓ test_verify_log_fortianalyzer_cloud_override_filter_restored passed")
    
    print("\n✓ All FortiAnalyzer Cloud override filter tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
