"""
CMDB Endpoint Tests: report/setting
Tests report settings configuration (VDOM scope).

Endpoint Information:
- Path: /api/v2/cmdb/report/setting
- Scope: VDOM
- Type: Singleton configuration endpoint
- Operations: GET, PUT

Test Strategy:
- Backup original configuration
- Change pdf_report to disable
- Verify change applied
- Change fortiview to disable
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
    """Get and store original report setting config"""
    global original_config
    
    print("\n1. Getting original report setting config...")
    result = fgt.api.cmdb.report.setting.get(vdom="test")
    
    assert result is not None, "Failed to get report setting config"
    assert result.http_status == "success", "Failed to get report setting config"
    
    original_config = {
        "pdf_report": result.pdf_report,
        "fortiview": result.fortiview
    }
    print(f"✓ Original pdf_report: {original_config['pdf_report']}, fortiview: {original_config['fortiview']}")


def test_put_change_pdf_report():
    """Change pdf_report to disable"""
    print("\n2. Changing pdf_report to disable...")
    
    result = fgt.api.cmdb.report.setting.put(
        pdf_report="disable",  # type: ignore
        vdom="test"
    )
    
    assert result is not None, "Failed to update pdf_report"
    assert result.http_status == "success", "Failed to update pdf_report"
    
    # Verify change
    verify = fgt.api.cmdb.report.setting.get(vdom="test")
    assert verify is not None, "Failed to get updated config"
    assert verify.pdf_report == "disable", f"pdf_report not updated, got: {verify.pdf_report}"
    print("✓ pdf_report changed to disable")


def test_put_change_fortiview():
    """Change fortiview to disable"""
    print("\n3. Changing fortiview to disable...")
    
    result = fgt.api.cmdb.report.setting.put(
        fortiview="disable",  # type: ignore
        vdom="test"
    )
    
    assert result is not None, "Failed to update fortiview"
    assert result.http_status == "success", "Failed to update fortiview"
    
    # Verify change
    verify = fgt.api.cmdb.report.setting.get(vdom="test")
    assert verify is not None, "Failed to get updated config"
    assert verify.fortiview == "disable", f"fortiview not updated, got: {verify.fortiview}"
    print("✓ fortiview changed to disable")


def test_restore():
    """Restore original configuration"""
    global original_config
    assert original_config is not None, "No original config to restore"
    
    print("\n4. Restoring original config...")
    
    result = fgt.api.cmdb.report.setting.put(
        pdf_report=original_config["pdf_report"],  # type: ignore
        fortiview=original_config["fortiview"],  # type: ignore
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
    
    verify = fgt.api.cmdb.report.setting.get(vdom="test")
    assert verify is not None, "Failed to get current config"
    
    assert verify.pdf_report == original_config["pdf_report"], \
        f"pdf_report not restored: expected {original_config['pdf_report']}, got {verify.pdf_report}"
    assert verify.fortiview == original_config["fortiview"], \
        f"fortiview not restored: expected {original_config['fortiview']}, got {verify.fortiview}"
    
    print(f"✓ pdf_report restored to: {verify.pdf_report}")
    print(f"✓ fortiview restored to: {verify.fortiview}")


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
        test_put_change_pdf_report()
        test_put_change_fortiview()
        test_restore()
        test_verify_restored()
        print("\n" + "="*50)
        print("All report setting tests passed!")
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
