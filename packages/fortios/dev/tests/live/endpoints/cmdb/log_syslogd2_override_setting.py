"""
CMDB Endpoint Tests: log.syslogd2/override-setting
Tests syslogd2 override settings configuration (VDOM scope).

Endpoint Information:
- Path: /api/v2/cmdb/log.syslogd2/override-setting
- Scope: VDOM
- Type: Singleton configuration endpoint
- Operations: GET, PUT

Test Strategy:
- Backup original configuration
- Change status setting
- Verify changes applied
- Restore original configuration
- Verify restoration successful
"""

import argparse
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(project_root))
from fgtclient import fgt


# Store original config globally
original_config = None


def test_get():
    """Get and store original syslogd2 override setting config"""
    global original_config
    
    print("\n1. Getting original syslogd2 override setting config...")
    result = fgt.api.cmdb.log.syslogd2.override_setting.get(vdom="test")
    
    assert result is not None, "Failed to get override setting config"
    assert result.http_status == "success", "Failed to get override setting config"
    
    original_config = {
        "status": result.status
    }
    print(f"✓ Original status: {original_config['status']}")


def test_put_change_status():
    """Change status to disable"""
    global original_config
    
    # Skip if already disabled
    if original_config and original_config.get("status") == "disable":
        print("\n2. Skipping status change (already disabled)...")
        return
    
    print("\n2. Changing status to disable...")
    
    result = fgt.api.cmdb.log.syslogd2.override_setting.put(
        status="disable",  # type: ignore
        vdom="test"
    )
    
    assert result is not None, "Failed to update status"
    assert result.http_status == "success", "Failed to update status"
    
    # Verify change
    verify = fgt.api.cmdb.log.syslogd2.override_setting.get(vdom="test")
    assert verify is not None, "Failed to get updated config"
    assert verify.status == "disable", f"Status not updated, got: {verify.status}"
    print("✓ Status changed to disable")


def test_restore():
    """Restore original configuration"""
    global original_config
    assert original_config is not None, "No original config to restore"
    
    print("\n3. Restoring original config...")
    
    result = fgt.api.cmdb.log.syslogd2.override_setting.put(
        status=original_config["status"],  # type: ignore
        vdom="test"
    )
    assert result is not None, "Failed to restore config"
    assert result.http_status == "success", "Failed to restore config"
    print("✓ Config restored")


def test_verify_restored():
    """Verify restoration was successful"""
    global original_config
    assert original_config is not None, "No original config to verify"
    
    print("\n4. Verifying restoration...")
    
    verify = fgt.api.cmdb.log.syslogd2.override_setting.get(vdom="test")
    assert verify is not None, "Failed to get current config"
    
    assert verify.status == original_config["status"], \
        f"Status not restored: expected {original_config['status']}, got {verify.status}"
    
    print(f"✓ Status restored to: {verify.status}")


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
    try:
        test_get()
        test_put_change_status()
        test_restore()
        test_verify_restored()
        print("\n" + "="*50)
        print("All syslogd2 override setting tests passed!")
        print("="*50)
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
