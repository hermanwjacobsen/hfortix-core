"""
CMDB Endpoint Tests: log.tacacs+accounting2/filter
Tests TACACS+ accounting2 events filter configuration (VDOM scope).

Endpoint Information:
- Path: /api/v2/cmdb/log.tacacs+accounting2/filter
- Scope: VDOM
- Type: Singleton configuration endpoint
- Operations: GET, PUT

Test Strategy:
- Backup original configuration
- Change login_audit to disable
- Verify change applied
- Change cli_cmd_audit to disable
- Verify change applied
- Restore original configuration
- Verify restoration successful

Note: TACACS+ accounting uses login_audit and cli_cmd_audit fields
instead of the standard severity/anomaly fields used by other logging filters.
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
    """Get and store original TACACS+ accounting2 filter config"""
    global original_config
    
    print("\n1. Getting original TACACS+ accounting2 filter config...")
    result = fgt.api.cmdb.log.tacacs_plus_accounting2.filter.get(vdom="test")
    
    assert result is not None, "Failed to get filter config"
    assert result.http_status == "success", "Failed to get filter config"
    
    original_config = {
        "login_audit": result.login_audit,
        "cli_cmd_audit": result.cli_cmd_audit
    }
    print(f"✓ Original login_audit: {original_config['login_audit']}, cli_cmd_audit: {original_config['cli_cmd_audit']}")


def test_put_change_login_audit():
    """Change login_audit to disable"""
    print("\n2. Changing login_audit to disable...")
    
    result = fgt.api.cmdb.log.tacacs_plus_accounting2.filter.put(
        login_audit="disable",  # type: ignore
        vdom="test"
    )
    
    assert result is not None, "Failed to update login_audit"
    assert result.http_status == "success", "Failed to update login_audit"
    
    # Verify change
    verify = fgt.api.cmdb.log.tacacs_plus_accounting2.filter.get(vdom="test")
    assert verify is not None, "Failed to get updated config"
    assert verify.login_audit == "disable", f"login_audit not updated, got: {verify.login_audit}"
    print("✓ login_audit changed to disable")


def test_put_change_cli_cmd_audit():
    """Change cli_cmd_audit to disable"""
    print("\n3. Changing cli_cmd_audit to disable...")
    
    result = fgt.api.cmdb.log.tacacs_plus_accounting2.filter.put(
        cli_cmd_audit="disable",  # type: ignore
        vdom="test"
    )
    
    assert result is not None, "Failed to update cli_cmd_audit"
    assert result.http_status == "success", "Failed to update cli_cmd_audit"
    
    # Verify change
    verify = fgt.api.cmdb.log.tacacs_plus_accounting2.filter.get(vdom="test")
    assert verify is not None, "Failed to get updated config"
    assert verify.cli_cmd_audit == "disable", f"cli_cmd_audit not updated, got: {verify.cli_cmd_audit}"
    print("✓ cli_cmd_audit changed to disable")


def test_restore():
    """Restore original configuration"""
    global original_config
    assert original_config is not None, "No original config to restore"
    
    print("\n4. Restoring original config...")
    
    result = fgt.api.cmdb.log.tacacs_plus_accounting2.filter.put(
        login_audit=original_config["login_audit"],  # type: ignore
        cli_cmd_audit=original_config["cli_cmd_audit"],  # type: ignore
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
    
    verify = fgt.api.cmdb.log.tacacs_plus_accounting2.filter.get(vdom="test")
    assert verify is not None, "Failed to get current config"
    
    assert verify.login_audit == original_config["login_audit"], \
        f"login_audit not restored: expected {original_config['login_audit']}, got {verify.login_audit}"
    assert verify.cli_cmd_audit == original_config["cli_cmd_audit"], \
        f"cli_cmd_audit not restored: expected {original_config['cli_cmd_audit']}, got {verify.cli_cmd_audit}"
    
    print(f"✓ login_audit restored to: {verify.login_audit}")
    print(f"✓ cli_cmd_audit restored to: {verify.cli_cmd_audit}")


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
        test_put_change_login_audit()
        test_put_change_cli_cmd_audit()
        test_restore()
        test_verify_restored()
        print("\n" + "="*50)
        print("All TACACS+ accounting2 filter tests passed!")
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
