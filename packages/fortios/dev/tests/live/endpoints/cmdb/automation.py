import argparse
import sys
from pathlib import Path

import pytest

# Add pytest directory to path (go up from endpoints/cmdb/ to pytest/)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt



def _get(obj, key):
    if isinstance(obj, dict):
        return obj.get(key)
    return getattr(obj, key, None)


pytestmark = pytest.mark.xdist_group("cmdb_automation")

def test_automation_setting_get():
    """Test: Get automation settings"""
    result = fgt.api.cmdb.automation.setting.get()
    assert result is not None
    assert _get(result, "max_concurrent_stitches") is not None

def test_automation_setting_put():
    """Test: Update automation settings"""
    result = fgt.api.cmdb.automation.setting.put(
        max_concurrent_stitches=500
    )
    assert result is not None
    assert result.http_status == "success"
    
    # Verify update
    settings = fgt.api.cmdb.automation.setting.get()
    assert _get(settings, 'max_concurrent_stitches') == 500

def cleanup(module):
    """Teardown: Reset automation settings after tests"""
    fgt.api.cmdb.automation.setting.put(
        max_concurrent_stitches=512
    )
    settings = fgt.api.cmdb.automation.setting.get()
    assert _get(settings, 'max_concurrent_stitches') == 512   

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
    test_automation_setting_get()
    print("✓ test_automation_setting_get passed")

    test_automation_setting_put()
    print("✓ test_automation_setting_put passed")

    cleanup(None)
    print("✓ cleanup passed")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
