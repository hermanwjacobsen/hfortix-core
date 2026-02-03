"""
CMDB Endpoint Tests: log.memory/global-setting
Tests memory global settings configuration.

Endpoint Information:
- Path: /api/v2/cmdb/log.memory/global-setting
- Scope: Global
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
    """Get and store original memory global setting config"""
    global original_config
    
    print("\n1. Getting original memory global setting config...")
    result = fgt.api.cmdb.log.memory.global_setting.get()
    
    assert result is not None, "Failed to get setting config"
    assert result.http_status == "success", "Failed to get setting config"
    
    original_config = {
        "full_first_warning_threshold": result.full_first_warning_threshold
    }
    print(f"✓ Original full_first_warning_threshold: {original_config['full_first_warning_threshold']}")


def test_put_change_full_first_warning_threshold():
    """Change full_first_warning_threshold to 80"""
    global original_config
    
    # Skip if already 80
    if original_config and original_config.get("full_first_warning_threshold") == 80:
        print("\n2. Skipping full_first_warning_threshold change (already 80)...")
        return
    
    print("\n2. Changing full_first_warning_threshold to 80...")
    
    result = fgt.api.cmdb.log.memory.global_setting.put(
        full_first_warning_threshold=80  # type: ignore
    )
    
    assert result is not None, "Failed to update full_first_warning_threshold"
    assert result.http_status == "success", "Failed to update full_first_warning_threshold"
    
    # Verify change
    verify = fgt.api.cmdb.log.memory.global_setting.get()
    assert verify is not None, "Failed to get updated config"
    assert verify.full_first_warning_threshold == 80, f"full_first_warning_threshold not updated, got: {verify.full_first_warning_threshold}"
    print("✓ full_first_warning_threshold changed to 80")


def test_restore():
    """Restore original configuration"""
    global original_config
    assert original_config is not None, "No original config to restore"
    
    print("\n3. Restoring original config...")
    
    result = fgt.api.cmdb.log.memory.global_setting.put(
        full_first_warning_threshold=original_config["full_first_warning_threshold"]  # type: ignore
    )
    assert result is not None, "Failed to restore config"
    assert result.http_status == "success", "Failed to restore config"
    print("✓ Config restored")


def test_verify_restored():
    """Verify restoration was successful"""
    global original_config
    assert original_config is not None, "No original config to verify"
    
    print("\n4. Verifying restoration...")
    
    verify = fgt.api.cmdb.log.memory.global_setting.get()
    assert verify is not None, "Failed to get current config"
    
    assert verify.full_first_warning_threshold == original_config["full_first_warning_threshold"], \
        f"full_first_warning_threshold not restored: expected {original_config['full_first_warning_threshold']}, got {verify.full_first_warning_threshold}"
    
    print(f"✓ full_first_warning_threshold restored to: {verify.full_first_warning_threshold}")


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
        test_put_change_full_first_warning_threshold()
        test_restore()
        test_verify_restored()
        print("\n" + "="*50)
        print("All memory global setting tests passed!")
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
