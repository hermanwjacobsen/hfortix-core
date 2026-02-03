import argparse
import sys
from pathlib import Path

import pytest

# Run tests on a single worker to preserve state (group by filename)
pytestmark = pytest.mark.xdist_group(Path(__file__).stem)

# Add pytest directory to path (go up from endpoints/cmdb/ to pytest/)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt


def cleanup():
    """Teardown: Reset ipmacbinding settings after tests"""
    try:
        fgt.api.cmdb.firewall.ipmacbinding.setting.put(bindtofw="disable")
    except Exception:
        pass

def test_get_ipmacbinding_setting():
    settings = fgt.api.cmdb.firewall.ipmacbinding.setting.get()
    print(settings.raw)
    assert settings is not None
    assert settings.http_status_code == 200

def test_put_ipmacbinding_setting(arp_reply="enable"):
    result = fgt.api.cmdb.firewall.ipmacbinding.setting.put(bindtofw="enable")
    assert result is not None
    assert result.http_status == "success"
    verify = fgt.api.cmdb.firewall.ipmacbinding.setting.get()
    assert verify is not None
    assert verify.http_status_code == 200
    assert verify.bindtofw == "enable"

def test_revert_ipmacbinding_setting():
    """Test: Revert ipmacbinding settings to default"""
    result = fgt.api.cmdb.firewall.ipmacbinding.setting.put(bindtofw="disable")
    assert result is not None
    assert result.http_status == "success"
    verify = fgt.api.cmdb.firewall.ipmacbinding.setting.get()
    assert verify is not None
    assert verify.http_status_code == 200
    assert verify.bindtofw == "disable"

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
    cleanup()
    print("✓ Pre-Cleanup passed")
    
    test_get_ipmacbinding_setting()
    print("✓ get_ipmacbinding_setting passed")

    test_put_ipmacbinding_setting()
    print("✓ put_ipmacbinding_setting passed")

    test_revert_ipmacbinding_setting()
    print("✓ revert_ipmacbinding_setting passed")

    cleanup()
    print("✓ post-Cleanup passed")
    
    print("\n✓ All tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
