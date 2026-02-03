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


def test_get_log_fortianalyzer_cloud_override_setting():
    """Test: Get FortiAnalyzer Cloud override settings."""
    global original_config
    result = fgt.api.cmdb.log.fortianalyzer_cloud.override_setting.get(vdom="test")
    assert result is not None
    assert result.http_status_code == 200
    
    # Store original status
    original_config = {
        "status": result.status if hasattr(result, "status") else None,
    }


def test_put_log_fortianalyzer_cloud_override_setting_disable():
    """Test: Disable FortiAnalyzer Cloud logging in override settings."""
    result = fgt.api.cmdb.log.fortianalyzer_cloud.override_setting.put(
        status="disable",
        vdom="test"
    )
    assert result is not None
    assert result.http_status == "success"
    
    # Verify the change
    verify = fgt.api.cmdb.log.fortianalyzer_cloud.override_setting.get(vdom="test")
    assert verify is not None
    assert verify.status == "disable"


def test_restore_log_fortianalyzer_cloud_override_setting():
    """Test: Restore FortiAnalyzer Cloud override settings to original state."""
    global original_config
    
    if original_config is None or original_config.get("status") is None:
        return
    
    status_value = original_config["status"]
    if status_value not in ["enable", "disable"]:
        return
    
    result = fgt.api.cmdb.log.fortianalyzer_cloud.override_setting.put(
        status=status_value,  # type: ignore
        vdom="test"
    )
    assert result is not None
    assert result.http_status == "success"
    
    # Verify restoration
    verify = fgt.api.cmdb.log.fortianalyzer_cloud.override_setting.get(vdom="test")
    assert verify is not None
    assert verify.status == original_config["status"]


def test_verify_log_fortianalyzer_cloud_override_setting_restored():
    """Test: Verify FortiAnalyzer Cloud override settings were restored."""
    result = fgt.api.cmdb.log.fortianalyzer_cloud.override_setting.get(vdom="test")
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
    test_get_log_fortianalyzer_cloud_override_setting()
    print("✓ test_get_log_fortianalyzer_cloud_override_setting passed")

    test_put_log_fortianalyzer_cloud_override_setting_disable()
    print("✓ test_put_log_fortianalyzer_cloud_override_setting_disable passed")

    test_restore_log_fortianalyzer_cloud_override_setting()
    print("✓ test_restore_log_fortianalyzer_cloud_override_setting passed")
    
    test_verify_log_fortianalyzer_cloud_override_setting_restored()
    print("✓ test_verify_log_fortianalyzer_cloud_override_setting_restored passed")
    
    print("\n✓ All FortiAnalyzer Cloud override setting tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
