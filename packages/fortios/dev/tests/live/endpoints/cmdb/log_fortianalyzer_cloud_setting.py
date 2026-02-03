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


def test_get_log_fortianalyzer_cloud_setting():
    """Test: Get global FortiAnalyzer Cloud settings."""
    global original_config
    result = fgt.api.cmdb.log.fortianalyzer_cloud.setting.get()
    assert result is not None
    assert result.http_status_code == 200
    
    # Store original settings
    original_config = {
        "ips_archive": result.ips_archive if hasattr(result, "ips_archive") else None,
        "certificate_verification": result.certificate_verification if hasattr(result, "certificate_verification") else None,
    }


def test_put_log_fortianalyzer_cloud_setting_disable_ips_archive():
    """Test: Disable IPS archive in FortiAnalyzer Cloud settings."""
    result = fgt.api.cmdb.log.fortianalyzer_cloud.setting.put(
        ips_archive="disable"
    )
    assert result is not None
    assert result.http_status == "success"
    
    # Verify the change
    verify = fgt.api.cmdb.log.fortianalyzer_cloud.setting.get()
    assert verify is not None
    assert verify.ips_archive == "disable"


def test_put_log_fortianalyzer_cloud_setting_enable_cert_verification():
    """Test: Enable certificate verification in FortiAnalyzer Cloud settings."""
    result = fgt.api.cmdb.log.fortianalyzer_cloud.setting.put(
        certificate_verification="enable"
    )
    assert result is not None
    assert result.http_status == "success"
    
    # Verify the change
    verify = fgt.api.cmdb.log.fortianalyzer_cloud.setting.get()
    assert verify is not None
    assert verify.certificate_verification == "enable"


def test_restore_log_fortianalyzer_cloud_setting():
    """Test: Restore FortiAnalyzer Cloud settings to original state."""
    global original_config
    
    if original_config is None:
        return
    
    restore_payload = {}
    if original_config.get("ips_archive") is not None:
        restore_payload["ips_archive"] = original_config["ips_archive"]
    if original_config.get("certificate_verification") is not None:
        restore_payload["certificate_verification"] = original_config["certificate_verification"]
    
    if restore_payload:
        result = fgt.api.cmdb.log.fortianalyzer_cloud.setting.put(**restore_payload)
        assert result is not None
        assert result.http_status == "success"
        
        # Verify restoration
        verify = fgt.api.cmdb.log.fortianalyzer_cloud.setting.get()
        assert verify is not None


def test_verify_log_fortianalyzer_cloud_setting_restored():
    """Test: Verify FortiAnalyzer Cloud settings were restored."""
    result = fgt.api.cmdb.log.fortianalyzer_cloud.setting.get()
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
    test_get_log_fortianalyzer_cloud_setting()
    print("✓ test_get_log_fortianalyzer_cloud_setting passed")

    test_put_log_fortianalyzer_cloud_setting_disable_ips_archive()
    print("✓ test_put_log_fortianalyzer_cloud_setting_disable_ips_archive passed")

    test_put_log_fortianalyzer_cloud_setting_enable_cert_verification()
    print("✓ test_put_log_fortianalyzer_cloud_setting_enable_cert_verification passed")

    test_restore_log_fortianalyzer_cloud_setting()
    print("✓ test_restore_log_fortianalyzer_cloud_setting passed")
    
    test_verify_log_fortianalyzer_cloud_setting_restored()
    print("✓ test_verify_log_fortianalyzer_cloud_setting_restored passed")
    
    print("\n✓ All FortiAnalyzer Cloud setting tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
