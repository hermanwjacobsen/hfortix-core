"""
CMDB Endpoint Tests: log.fortiguard/filter
Tests FortiCloud filter configuration.

Endpoint Information:
- Path: /api/v2/cmdb/log.fortiguard/filter
- Scope: Global (no vdom parameter)
- Type: Singleton configuration endpoint
- Operations: GET, PUT

Test Strategy:
- Backup original configuration
- Change severity and anomaly settings
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
    """Get and store original FortiGuard filter config"""
    global original_config
    
    print("\n1. Getting original FortiGuard filter config...")
    result = fgt.api.cmdb.log.fortiguard.filter.get()
    
    assert result is not None, "Failed to get filter config"
    assert result.http_status == "success", "Failed to get filter config"
    
    original_config = {
        "severity": result.severity,
        "anomaly": result.anomaly
    }
    print(f"✓ Original severity: {original_config['severity']}")
    print(f"✓ Original anomaly: {original_config['anomaly']}")


def test_put_change_severity():
    """Change severity to critical"""
    print("\n2. Changing severity to critical...")
    
    result = fgt.api.cmdb.log.fortiguard.filter.put(
        severity="critical"  # type: ignore
    )
    
    assert result is not None, "Failed to update severity"
    assert result.http_status == "success", "Failed to update severity"
    
    # Verify change
    verify = fgt.api.cmdb.log.fortiguard.filter.get()
    assert verify is not None, "Failed to get updated config"
    assert verify.severity == "critical", f"Severity not updated, got: {verify.severity}"
    print("✓ Severity changed to critical")


def test_put_change_anomaly():
    """Change anomaly to disable"""
    print("\n3. Changing anomaly to disable...")
    
    result = fgt.api.cmdb.log.fortiguard.filter.put(
        anomaly="disable"  # type: ignore
    )
    
    assert result is not None, "Failed to update anomaly"
    assert result.http_status == "success", "Failed to update anomaly"
    
    # Verify change
    verify = fgt.api.cmdb.log.fortiguard.filter.get()
    assert verify is not None, "Failed to get updated config"
    assert verify.anomaly == "disable", f"Anomaly not updated, got: {verify.anomaly}"
    print("✓ Anomaly changed to disable")


def test_restore():
    """Restore original configuration"""
    global original_config
    assert original_config is not None, "No original config to restore"
    
    print("\n4. Restoring original config...")
    
    # Restore both settings
    result = fgt.api.cmdb.log.fortiguard.filter.put(
        severity=original_config["severity"],  # type: ignore
        anomaly=original_config["anomaly"]  # type: ignore
    )
    assert result is not None, "Failed to restore config"
    assert result.http_status == "success", "Failed to restore config"
    print("✓ Config restored")


def test_verify_restored():
    """Verify restoration was successful"""
    global original_config
    assert original_config is not None, "No original config to verify"
    
    print("\n5. Verifying restoration...")
    
    verify = fgt.api.cmdb.log.fortiguard.filter.get()
    assert verify is not None, "Failed to get current config"
    
    assert verify.severity == original_config["severity"], \
        f"Severity not restored: expected {original_config['severity']}, got {verify.severity}"
    assert verify.anomaly == original_config["anomaly"], \
        f"Anomaly not restored: expected {original_config['anomaly']}, got {verify.anomaly}"
    
    print(f"✓ Severity restored to: {verify.severity}")
    print(f"✓ Anomaly restored to: {verify.anomaly}")


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
        test_put_change_anomaly()
        test_restore()
        test_verify_restored()
        print("\n" + "="*50)
        print("All FortiGuard filter tests passed!")
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
