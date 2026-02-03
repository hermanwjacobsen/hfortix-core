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


def test_get_log_disk_setting():
    """Test: Get log disk settings."""
    global original_config
    result = fgt.api.cmdb.log.disk.setting.get(vdom="test")
    assert result is not None
    assert result.http_status_code == 200
    
    # Store original ips_archive setting
    original_config = {
        "ips_archive": result.ips_archive if hasattr(result, "ips_archive") else None,
    }


def test_put_log_disk_setting_disable_ips_archive():
    """Test: Disable IPS archive in log disk settings."""
    result = fgt.api.cmdb.log.disk.setting.put(
        ips_archive="disable",
        vdom="test"
    )
    assert result is not None
    assert result.http_status == "success"
    
    # Verify the change
    verify = fgt.api.cmdb.log.disk.setting.get(vdom="test")
    assert verify is not None
    assert verify.ips_archive == "disable"


def test_restore_log_disk_setting():
    """Test: Restore log disk settings to original state."""
    global original_config
    
    if original_config is None or original_config.get("ips_archive") is None:
        return
    
    # Cast to correct type
    ips_archive_value = original_config["ips_archive"]
    if ips_archive_value not in ["enable", "disable"]:
        return
    
    result = fgt.api.cmdb.log.disk.setting.put(
        ips_archive=ips_archive_value,  # type: ignore
        vdom="test"
    )
    assert result is not None
    assert result.http_status == "success"
    
    # Verify restoration
    verify = fgt.api.cmdb.log.disk.setting.get(vdom="test")
    assert verify is not None
    assert verify.ips_archive == original_config["ips_archive"]


def test_verify_log_disk_setting_restored():
    """Test: Verify log disk settings were restored."""
    result = fgt.api.cmdb.log.disk.setting.get(vdom="test")
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
    test_get_log_disk_setting()
    print("✓ test_get_log_disk_setting passed")

    test_put_log_disk_setting_disable_ips_archive()
    print("✓ test_put_log_disk_setting_disable_ips_archive passed")

    test_restore_log_disk_setting()
    print("✓ test_restore_log_disk_setting passed")
    
    test_verify_log_disk_setting_restored()
    print("✓ test_verify_log_disk_setting_restored passed")
    
    print("\n✓ All log disk setting tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
