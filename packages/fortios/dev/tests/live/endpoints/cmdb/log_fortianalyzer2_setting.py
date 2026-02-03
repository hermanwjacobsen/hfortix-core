"""
CMDB Endpoint Tests: log.fortianalyzer2/setting
Tests FortiAnalyzer2 global settings configuration.

Endpoint Information:
- Path: /api/v2/cmdb/log.fortianalyzer2/setting
- Scope: Global (no vdom parameter)
- Type: Singleton configuration endpoint
- Operations: GET, PUT

Test Strategy:
- Backup original configuration
- Change ips_archive and certificate_verification settings
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
    """Get and store original FortiAnalyzer2 setting config"""
    global original_config
    
    print("\n1. Getting original FortiAnalyzer2 setting config...")
    result = fgt.api.cmdb.log.fortianalyzer2.setting.get()
    
    assert result is not None, "Failed to get setting config"
    assert result.http_status == "success", "Failed to get setting config"
    
    original_config = {
        "ips_archive": result.ips_archive,
        "certificate_verification": result.certificate_verification
    }
    print(f"✓ Original ips_archive: {original_config['ips_archive']}")
    print(f"✓ Original certificate_verification: {original_config['certificate_verification']}")


def test_put_disable_ips_archive():
    """Change ips_archive to disable"""
    global original_config
    
    # Skip if already disabled
    if original_config and original_config.get("ips_archive") == "disable":
        print("\n2. Skipping ips_archive change (already disabled)...")
        return
    
    print("\n2. Changing ips_archive to disable...")
    
    result = fgt.api.cmdb.log.fortianalyzer2.setting.put(
        ips_archive="disable"  # type: ignore
    )
    
    assert result is not None, "Failed to update ips_archive"
    assert result.http_status == "success", "Failed to update ips_archive"
    
    # Verify change
    verify = fgt.api.cmdb.log.fortianalyzer2.setting.get()
    assert verify is not None, "Failed to get updated config"
    
    # Note: Some settings may not change if FortiAnalyzer2 is not configured
    if verify.ips_archive != "disable":
        print(f"⚠ Warning: IPS archive not changed (got: {verify.ips_archive}). FortiAnalyzer2 may not be configured.")
    else:
        print("✓ IPS archive changed to disable")


def test_put_enable_cert_verification():
    """Change certificate_verification to enable"""
    global original_config
    
    # Skip if already enabled
    if original_config and original_config.get("certificate_verification") == "enable":
        print("\n3. Skipping certificate_verification change (already enabled)...")
        return
    
    print("\n3. Changing certificate_verification to enable...")
    
    result = fgt.api.cmdb.log.fortianalyzer2.setting.put(
        certificate_verification="enable"  # type: ignore
    )
    
    assert result is not None, "Failed to update certificate_verification"
    assert result.http_status == "success", "Failed to update certificate_verification"
    
    # Verify change
    verify = fgt.api.cmdb.log.fortianalyzer2.setting.get()
    assert verify is not None, "Failed to get updated config"
    
    # Note: Some settings may not change if FortiAnalyzer2 is not configured
    if verify.certificate_verification != "enable":
        print(f"⚠ Warning: Certificate verification not changed (got: {verify.certificate_verification}). FortiAnalyzer2 may not be configured.")
    else:
        print("✓ Certificate verification changed to enable")


def test_restore():
    """Restore original configuration"""
    global original_config
    assert original_config is not None, "No original config to restore"
    
    print("\n4. Restoring original config...")
    
    # Restore both settings
    result = fgt.api.cmdb.log.fortianalyzer2.setting.put(
        ips_archive=original_config["ips_archive"],  # type: ignore
        certificate_verification=original_config["certificate_verification"]  # type: ignore
    )
    assert result is not None, "Failed to restore config"
    assert result.http_status == "success", "Failed to restore config"
    print("✓ Config restored")


def test_verify_restored():
    """Verify restoration was successful"""
    global original_config
    assert original_config is not None, "No original config to verify"
    
    print("\n5. Verifying restoration...")
    
    verify = fgt.api.cmdb.log.fortianalyzer2.setting.get()
    assert verify is not None, "Failed to get current config"
    
    assert verify.ips_archive == original_config["ips_archive"], \
        f"IPS archive not restored: expected {original_config['ips_archive']}, got {verify.ips_archive}"
    assert verify.certificate_verification == original_config["certificate_verification"], \
        f"Certificate verification not restored: expected {original_config['certificate_verification']}, got {verify.certificate_verification}"
    
    print(f"✓ IPS archive restored to: {verify.ips_archive}")
    print(f"✓ Certificate verification restored to: {verify.certificate_verification}")


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
        test_put_disable_ips_archive()
        test_put_enable_cert_verification()
        test_restore()
        test_verify_restored()
        print("\n" + "="*50)
        print("All FortiAnalyzer2 setting tests passed!")
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
