import argparse
import sys
from pathlib import Path

import pytest

# Run tests on a single worker to preserve state (group by filename)
pytestmark = pytest.mark.xdist_group(Path(__file__).stem)

# Add pytest directory to path (go up from endpoints/cmdb/ to pytest/)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt


TEST_NAME = "test_address6_1"


def cleanup():
    """Clean up test IPv6 addresses."""
    try:
        addresses = fgt.api.cmdb.firewall.address6.get()
        for addr in addresses:
            if addr.name and str(addr.name).startswith("test"):
                try:
                    fgt.api.cmdb.firewall.address6.delete(name=addr.name)
                except Exception:
                    pass
    except Exception:
        pass


def test_get_addresses6():
    """Test: Get all IPv6 addresses."""
    result = fgt.api.cmdb.firewall.address6.get()
    assert result is not None
    assert result.http_status_code == 200


def test_post_address6():
    """Test: Create IPv6 address."""
    result = fgt.api.cmdb.firewall.address6.post(
        name=TEST_NAME,
        type="ipprefix",
        ip6="2001:db8:100::/64",
        comment="Test IPv6 address",
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_address6():
    """Test: Update IPv6 address."""
    result = fgt.api.cmdb.firewall.address6.put(
        name=TEST_NAME,
        comment="Updated IPv6 address",
    )
    assert result is not None
    assert result.http_status == "success"
    
    # Verify the update
    verify = fgt.api.cmdb.firewall.address6.get(name=TEST_NAME)
    assert verify is not None
    assert verify.comment == "Updated IPv6 address"


def test_get_specific_address6():
    """Test: Get specific IPv6 address."""
    result = fgt.api.cmdb.firewall.address6.get(name=TEST_NAME)
    assert result is not None
    assert result.name == TEST_NAME


def test_delete_address6():
    """Test: Delete IPv6 address."""
    result = fgt.api.cmdb.firewall.address6.delete(name=TEST_NAME)
    assert result is not None
    assert result.http_status == "success"
    
    # Verify deletion
    addresses = fgt.api.cmdb.firewall.address6.get()
    addr_names = [a.name for a in addresses]
    assert TEST_NAME not in addr_names, "IPv6 address should have been deleted"


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
        
    test_get_addresses6()
    print("✓ test_get_addresses6 passed")

    test_post_address6()
    print("✓ test_post_address6 passed")

    test_put_address6()
    print("✓ test_put_address6 passed")

    test_get_specific_address6()
    print("✓ test_get_specific_address6 passed")

    test_delete_address6()
    print("✓ test_delete_address6 passed")

    cleanup()
    print("✓ post-Cleanup passed")
    
    print("\n✓ All tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
