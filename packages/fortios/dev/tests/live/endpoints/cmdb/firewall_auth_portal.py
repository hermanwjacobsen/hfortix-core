import argparse
import sys
from pathlib import Path

import pytest

# Run tests on a single worker to preserve state (group by filename)
pytestmark = pytest.mark.xdist_group(Path(__file__).stem)

# Add pytest directory to path (go up from endpoints/cmdb/ to pytest/)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt


ORIGINAL_PROXY_AUTH = None


def test_get_auth_portal():
    """Test: Get firewall auth portal settings."""
    global ORIGINAL_PROXY_AUTH
    
    result = fgt.api.cmdb.firewall.auth_portal.get()
    assert result is not None
    assert result.http_status_code == 200
    
    # Store original value for restoration
    ORIGINAL_PROXY_AUTH = result.proxy_auth


def test_put_auth_portal():
    """Test: Update firewall auth portal settings."""
    global ORIGINAL_PROXY_AUTH
    
    # Determine new value (toggle from original)
    new_value = "disable" if ORIGINAL_PROXY_AUTH == "enable" else "enable"
    
    result = fgt.api.cmdb.firewall.auth_portal.put(
        proxy_auth=new_value,
    )
    assert result is not None
    assert result.http_status == "success"
    
    # Verify the update
    verify = fgt.api.cmdb.firewall.auth_portal.get()
    assert verify is not None
    assert verify.proxy_auth == new_value


def test_revert_auth_portal():
    """Test: Revert firewall auth portal settings to original."""
    global ORIGINAL_PROXY_AUTH
    
    if ORIGINAL_PROXY_AUTH is None:
        pytest.skip("Original value not captured")
    
    result = fgt.api.cmdb.firewall.auth_portal.put(
        proxy_auth=ORIGINAL_PROXY_AUTH,
    )
    assert result is not None
    assert result.http_status == "success"
    
    # Verify restoration
    verify = fgt.api.cmdb.firewall.auth_portal.get()
    assert verify is not None
    assert verify.proxy_auth == ORIGINAL_PROXY_AUTH


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
    test_get_auth_portal()
    print("✓ test_get_auth_portal passed")

    test_put_auth_portal()
    print("✓ test_put_auth_portal passed")

    test_revert_auth_portal()
    print("✓ test_revert_auth_portal passed")
    
    print("\n✓ All tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
