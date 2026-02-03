"""
CMDB Endpoint Tests: log.fortiguard/override-filter
Tests FortiCloud override filter configuration.

Endpoint Information:
- Path: /api/v2/cmdb/log.fortiguard/override-filter
- Scope: VDOM (vdom parameter required)
- Type: Singleton configuration endpoint
- Operations: GET, PUT

Test Strategy:
- Backup original configuration
- Change severity and voip settings
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
    """Get and store original FortiGuard override filter config"""
    global original_config
    
    print("\n1. Getting original FortiGuard override filter config...")
    result = fgt.api.cmdb.log.fortiguard.override_filter.get(vdom="test")
    
    assert result is not None, "Failed to get override filter config"
    assert result.http_status == "success", "Failed to get override filter config"
    
    original_config = {
        "severity": result.severity,
        "voip": result.voip
    }
    print(f"✓ Original severity: {original_config['severity']}")
    print(f"✓ Original voip: {original_config['voip']}")


def test_put_change_severity():
    """Change severity to error"""
    print("\n2. Changing severity to error...")
    
    result = fgt.api.cmdb.log.fortiguard.override_filter.put(
        vdom="test",
        severity="error"  # type: ignore
    )
    
    assert result is not None, "Failed to update severity"
    assert result.http_status == "success", "Failed to update severity"
    
    # Verify change
    verify = fgt.api.cmdb.log.fortiguard.override_filter.get(vdom="test")
    assert verify is not None, "Failed to get updated config"
    assert verify.severity == "error", f"Severity not updated, got: {verify.severity}"
    print("✓ Severity changed to error")


def test_put_change_voip():
    """Change voip to enable"""
    print("\n3. Changing voip to enable...")
    
    result = fgt.api.cmdb.log.fortiguard.override_filter.put(
        vdom="test",
        voip="enable"  # type: ignore
    )
    
    assert result is not None, "Failed to update voip"
    assert result.http_status == "success", "Failed to update voip"
    
    # Verify change
    verify = fgt.api.cmdb.log.fortiguard.override_filter.get(vdom="test")
    assert verify is not None, "Failed to get updated config"
    assert verify.voip == "enable", f"VoIP not updated, got: {verify.voip}"
    print("✓ VoIP changed to enable")


def test_restore():
    """Restore original configuration"""
    global original_config
    assert original_config is not None, "No original config to restore"
    
    print("\n4. Restoring original config...")
    
    # Restore both settings
    result = fgt.api.cmdb.log.fortiguard.override_filter.put(
        vdom="test",
        severity=original_config["severity"],  # type: ignore
        voip=original_config["voip"]  # type: ignore
    )
    assert result is not None, "Failed to restore config"
    assert result.http_status == "success", "Failed to restore config"
    print("✓ Config restored")


def test_verify_restored():
    """Verify restoration was successful"""
    global original_config
    assert original_config is not None, "No original config to verify"
    
    print("\n5. Verifying restoration...")
    
    verify = fgt.api.cmdb.log.fortiguard.override_filter.get(vdom="test")
    assert verify is not None, "Failed to get current config"
    
    assert verify.severity == original_config["severity"], \
        f"Severity not restored: expected {original_config['severity']}, got {verify.severity}"
    assert verify.voip == original_config["voip"], \
        f"VoIP not restored: expected {original_config['voip']}, got {verify.voip}"
    
    print(f"✓ Severity restored to: {verify.severity}")
    print(f"✓ VoIP restored to: {verify.voip}")


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
        test_put_change_severity()
        test_put_change_voip()
        test_restore()
        test_verify_restored()
        print("\n" + "="*50)
        print("All FortiGuard override filter tests passed!")
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
