import argparse
import sys
from pathlib import Path

import pytest

# Run tests on a single worker to preserve state (group by filename)
pytestmark = pytest.mark.xdist_group(Path(__file__).stem)

# Add pytest directory to path (go up from endpoints/cmdb/ to pytest/)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt


ORIGINAL_BANNED_IP_PERSISTENCY = None

def test_get_firewall_global():
    """Test: Get global firewall settings."""
    global ORIGINAL_BANNED_IP_PERSISTENCY
    result = fgt.api.cmdb.firewall.global_.get()
    assert result is not None
    assert result.http_status_code == 200
    ORIGINAL_BANNED_IP_PERSISTENCY = result.banned_ip_persistency

def test_put_firewall_global():
    """Test: Update global firewall settings."""
    global ORIGINAL_BANNED_IP_PERSISTENCY
    # Toggle value for test
    new_value = "permanent-only" if ORIGINAL_BANNED_IP_PERSISTENCY != "permanent-only" else "all"
    result = fgt.api.cmdb.firewall.global_.put(
        banned_ip_persistency=new_value,
    )
    assert result is not None
    assert result.http_status == "success"
    # Verify
    verify = fgt.api.cmdb.firewall.global_.get()
    assert verify is not None
    assert verify.banned_ip_persistency == new_value

def test_revert_firewall_global():
    """Test: Revert global firewall settings to original."""
    global ORIGINAL_BANNED_IP_PERSISTENCY
    if ORIGINAL_BANNED_IP_PERSISTENCY is None:
        pytest.skip("Original value not captured")
    result = fgt.api.cmdb.firewall.global_.put(
        banned_ip_persistency=ORIGINAL_BANNED_IP_PERSISTENCY,
    )
    assert result is not None
    assert result.http_status == "success"
    # Verify
    verify = fgt.api.cmdb.firewall.global_.get()
    assert verify is not None
    assert verify.banned_ip_persistency == ORIGINAL_BANNED_IP_PERSISTENCY

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
    test_get_firewall_global()
    print("✓ test_get_firewall_global passed")

    test_put_firewall_global()
    print("✓ test_put_firewall_global passed")

    test_revert_firewall_global()
    print("✓ test_revert_firewall_global passed")
    
    print("\n✓ All tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
