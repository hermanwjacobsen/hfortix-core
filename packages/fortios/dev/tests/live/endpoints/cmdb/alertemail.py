import argparse
import sys
from pathlib import Path

# Add pytest directory to path (go up from endpoints/cmdb/ to pytest/)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt



def test_get_alertemail():
    """Test: Get alertemail settings"""
    result = fgt.api.cmdb.alertemail.setting.get()
    assert result is not None
    # Direct attribute access on FortiObject
    assert hasattr(result, 'mailto1')


def test_update_alertemail():
    """Test: Update alertemail to specific email"""
    result = fgt.api.cmdb.alertemail.setting.put(mailto1="herman@wjacobsen.fo")
    assert result is not None

    # Verify update - direct attribute access
    settings = fgt.api.cmdb.alertemail.setting.get()
    assert settings.mailto1 == "herman@wjacobsen.fo"

def cleanup(module):
    """Teardown: Reset alertemail settings after tests"""
    fgt.api.cmdb.alertemail.setting.put(mailto1="")

def verify_cleanup(module):
    """Verify teardown"""
    settings = fgt.api.cmdb.alertemail.setting.get()
    assert settings.mailto1 == ""

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
    test_get_alertemail()
    print("✓ test_get_alertemail passed")

    test_update_alertemail()
    print("✓ test_update_alertemail passed")

    cleanup(None)
    verify_cleanup(None)
    print("✓ cleanup and verify_cleanup passed")
    print("\n✓ All tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
