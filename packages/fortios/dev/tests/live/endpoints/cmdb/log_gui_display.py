"""
CMDB Endpoint Tests: log/gui-display
Tests GUI display settings configuration (VDOM scope).

Endpoint Information:
- Path: /api/v2/cmdb/log/gui-display
- Scope: VDOM
- Type: Singleton configuration endpoint
- Operations: GET, PUT

Test Strategy:
- Backup original configuration
- Change resolve_hosts to disable
- Verify change applied
- Change resolve_apps to disable
- Verify change applied
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
    """Get and store original gui-display config"""
    global original_config
    
    print("\n1. Getting original gui-display config...")
    result = fgt.api.cmdb.log.gui_display.get(vdom="test")
    
    assert result is not None, "Failed to get gui-display config"
    assert result.http_status == "success", "Failed to get gui-display config"
    
    original_config = {
        "resolve_hosts": result.resolve_hosts,
        "resolve_apps": result.resolve_apps
    }
    print(f"✓ Original resolve_hosts: {original_config['resolve_hosts']}, resolve_apps: {original_config['resolve_apps']}")


def test_put_change_resolve_hosts():
    """Change resolve_hosts to disable"""
    print("\n2. Changing resolve_hosts to disable...")
    
    result = fgt.api.cmdb.log.gui_display.put(
        resolve_hosts="disable",  # type: ignore
        vdom="test"
    )
    
    assert result is not None, "Failed to update resolve_hosts"
    assert result.http_status == "success", "Failed to update resolve_hosts"
    
    # Verify change
    verify = fgt.api.cmdb.log.gui_display.get(vdom="test")
    assert verify is not None, "Failed to get updated config"
    assert verify.resolve_hosts == "disable", f"resolve_hosts not updated, got: {verify.resolve_hosts}"
    print("✓ resolve_hosts changed to disable")


def test_put_change_resolve_apps():
    """Change resolve_apps to disable"""
    print("\n3. Changing resolve_apps to disable...")
    
    result = fgt.api.cmdb.log.gui_display.put(
        resolve_apps="disable",  # type: ignore
        vdom="test"
    )
    
    assert result is not None, "Failed to update resolve_apps"
    assert result.http_status == "success", "Failed to update resolve_apps"
    
    # Verify change
    verify = fgt.api.cmdb.log.gui_display.get(vdom="test")
    assert verify is not None, "Failed to get updated config"
    assert verify.resolve_apps == "disable", f"resolve_apps not updated, got: {verify.resolve_apps}"
    print("✓ resolve_apps changed to disable")


def test_restore():
    """Restore original configuration"""
    global original_config
    assert original_config is not None, "No original config to restore"
    
    print("\n4. Restoring original config...")
    
    result = fgt.api.cmdb.log.gui_display.put(
        resolve_hosts=original_config["resolve_hosts"],  # type: ignore
        resolve_apps=original_config["resolve_apps"],  # type: ignore
        vdom="test"
    )
    assert result is not None, "Failed to restore config"
    assert result.http_status == "success", "Failed to restore config"
    print("✓ Config restored")


def test_verify_restored():
    """Verify restoration was successful"""
    global original_config
    assert original_config is not None, "No original config to verify"
    
    print("\n5. Verifying restoration...")
    
    verify = fgt.api.cmdb.log.gui_display.get(vdom="test")
    assert verify is not None, "Failed to get current config"
    
    assert verify.resolve_hosts == original_config["resolve_hosts"], \
        f"resolve_hosts not restored: expected {original_config['resolve_hosts']}, got {verify.resolve_hosts}"
    assert verify.resolve_apps == original_config["resolve_apps"], \
        f"resolve_apps not restored: expected {original_config['resolve_apps']}, got {verify.resolve_apps}"
    
    print(f"✓ resolve_hosts restored to: {verify.resolve_hosts}")
    print(f"✓ resolve_apps restored to: {verify.resolve_apps}")


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
        test_put_change_resolve_hosts()
        test_put_change_resolve_apps()
        test_restore()
        test_verify_restored()
        print("\n" + "="*50)
        print("All gui-display tests passed!")
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
