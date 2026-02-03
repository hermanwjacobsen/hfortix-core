import argparse
import sys
from pathlib import Path

import pytest

# Run tests on a single worker to preserve state (group by filename)
pytestmark = pytest.mark.xdist_group(Path(__file__).stem)

# Add pytest directory to path (go up from endpoints/cmdb/ to pytest/)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt


TEST_NAME = "test_address1"


def cleanup():
    """Clean up test addresses."""
    try:
        addresses = fgt.api.cmdb.firewall.address.get()
        for addr in addresses:
            if addr.name and str(addr.name).startswith("test"):
                try:
                    fgt.api.cmdb.firewall.address.delete(name=addr.name)
                except Exception:
                    pass
    except Exception:
        pass


def test_get_addresses():
    """Test: Get all IPv4 addresses."""
    result = fgt.api.cmdb.firewall.address.get()
    assert result is not None
    assert result.http_status_code == 200


def test_post_address():
    """Test: Create IPv4 address."""
    result = fgt.api.cmdb.firewall.address.post(
        name=TEST_NAME,
        type="ipmask",
        subnet="192.168.100.0/24",
        comment="Test IPv4 address",
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_address():
    """Test: Update IPv4 address."""
    result = fgt.api.cmdb.firewall.address.put(
        name=TEST_NAME,
        comment="Updated IPv4 address",
    )
    assert result is not None
    assert result.http_status == "success"
    
    # Verify the update
    verify = fgt.api.cmdb.firewall.address.get(name=TEST_NAME)
    assert verify is not None
    assert verify.comment == "Updated IPv4 address"


def test_get_specific_address():
    """Test: Get specific IPv4 address."""
    result = fgt.api.cmdb.firewall.address.get(name=TEST_NAME)
    assert result is not None
    assert result.name == TEST_NAME


def test_delete_address():
    """Test: Delete IPv4 address."""
    result = fgt.api.cmdb.firewall.address.delete(name=TEST_NAME)
    assert result is not None
    assert result.http_status == "success"
    
    # Verify deletion
    addresses = fgt.api.cmdb.firewall.address.get()
    addr_names = [a.name for a in addresses]
    assert TEST_NAME not in addr_names, "Address should have been deleted"


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
        
    test_get_addresses()
    print("✓ test_get_addresses passed")

    test_post_address()
    print("✓ test_post_address passed")

    test_put_address()
    print("✓ test_put_address passed")

    test_get_specific_address()
    print("✓ test_get_specific_address passed")

    test_delete_address()
    print("✓ test_delete_address passed")

    cleanup()
    print("✓ post-Cleanup passed")
    
    print("\n✓ All tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
