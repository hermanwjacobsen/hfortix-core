"""
CMDB Endpoint Tests: log/setting
Tests general log settings configuration (VDOM scope).

Endpoint Information:
- Path: /api/v2/cmdb/log/setting
- Scope: VDOM
- Type: Singleton configuration endpoint
- Operations: GET, PUT

Test Strategy:
- Backup original configuration
- Change resolve_ip to disable
- Verify change applied
- Change resolve_port to disable
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
    """Get and store original log setting config"""
    global original_config
    
    print("\n1. Getting original log setting config...")
    result = fgt.api.cmdb.log.setting.get(vdom="test")
    
    assert result is not None, "Failed to get log setting config"
    assert result.http_status == "success", "Failed to get log setting config"
    
    original_config = {
        "resolve_ip": result.resolve_ip,
        "resolve_port": result.resolve_port
    }
    print(f"✓ Original resolve_ip: {original_config['resolve_ip']}, resolve_port: {original_config['resolve_port']}")


def test_put_change_resolve_ip():
    """Change resolve_ip to disable"""
    print("\n2. Changing resolve_ip to disable...")
    
    result = fgt.api.cmdb.log.setting.put(
        resolve_ip="disable",  # type: ignore
        vdom="test"
    )
    
    assert result is not None, "Failed to update resolve_ip"
    assert result.http_status == "success", "Failed to update resolve_ip"
    
    # Verify change
    verify = fgt.api.cmdb.log.setting.get(vdom="test")
    assert verify is not None, "Failed to get updated config"
    assert verify.resolve_ip == "disable", f"resolve_ip not updated, got: {verify.resolve_ip}"
    print("✓ resolve_ip changed to disable")


def test_put_change_resolve_port():
    """Change resolve_port to disable"""
    print("\n3. Changing resolve_port to disable...")
    
    result = fgt.api.cmdb.log.setting.put(
        resolve_port="disable",  # type: ignore
        vdom="test"
    )
    
    assert result is not None, "Failed to update resolve_port"
    assert result.http_status == "success", "Failed to update resolve_port"
    
    # Verify change
    verify = fgt.api.cmdb.log.setting.get(vdom="test")
    assert verify is not None, "Failed to get updated config"
    assert verify.resolve_port == "disable", f"resolve_port not updated, got: {verify.resolve_port}"
    print("✓ resolve_port changed to disable")


def test_restore():
    """Restore original configuration"""
    global original_config
    assert original_config is not None, "No original config to restore"
    
    print("\n4. Restoring original config...")
    
    result = fgt.api.cmdb.log.setting.put(
        resolve_ip=original_config["resolve_ip"],  # type: ignore
        resolve_port=original_config["resolve_port"],  # type: ignore
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
    
    verify = fgt.api.cmdb.log.setting.get(vdom="test")
    assert verify is not None, "Failed to get current config"
    
    assert verify.resolve_ip == original_config["resolve_ip"], \
        f"resolve_ip not restored: expected {original_config['resolve_ip']}, got {verify.resolve_ip}"
    assert verify.resolve_port == original_config["resolve_port"], \
        f"resolve_port not restored: expected {original_config['resolve_port']}, got {verify.resolve_port}"
    
    print(f"✓ resolve_ip restored to: {verify.resolve_ip}")
    print(f"✓ resolve_port restored to: {verify.resolve_port}")


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
        test_put_change_resolve_ip()
        test_put_change_resolve_port()
        test_restore()
        test_verify_restored()
        print("\n" + "="*50)
        print("All log setting tests passed!")
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
