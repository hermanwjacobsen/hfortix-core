import argparse
import sys
from pathlib import Path

import pytest

# Run tests on a single worker to preserve state (group by filename)
pytestmark = pytest.mark.xdist_group(Path(__file__).stem)

# Add pytest directory to path (go up from endpoints/cmdb/ to pytest/)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt


TEST_NAME = "test_wildcard_fqdn1"


def cleanup():
    """Clean up test wildcard FQDN addresses."""
    try:
        addresses = fgt.api.cmdb.firewall.wildcard_fqdn.custom.get()
        for addr in addresses:
            if addr.name and str(addr.name).startswith("test_"):
                try:
                    fgt.api.cmdb.firewall.wildcard_fqdn.custom.delete(name=addr.name)
                except Exception:
                    pass
    except Exception:
        pass


def test_get_wildcard_fqdn_custom():
    """Test: Get all wildcard FQDN addresses."""
    result = fgt.api.cmdb.firewall.wildcard_fqdn.custom.get()
    assert result is not None
    assert result.http_status_code == 200


def test_post_wildcard_fqdn_custom():
    """Test: Create wildcard FQDN address."""
    result = fgt.api.cmdb.firewall.wildcard_fqdn.custom.post(
        name=TEST_NAME,
        wildcard_fqdn="*.example.com",
        comment="Test Wildcard FQDN"
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_wildcard_fqdn_custom():
    """Test: Update wildcard FQDN address."""
    result = fgt.api.cmdb.firewall.wildcard_fqdn.custom.put(
        name=TEST_NAME,
        wildcard_fqdn="*.test.example.com",
        comment="Updated Test Wildcard FQDN"
    )
    assert result is not None
    assert result.http_status == "success"
    
    # Verify the update
    verify = fgt.api.cmdb.firewall.wildcard_fqdn.custom.get(name=TEST_NAME)
    assert verify is not None
    assert verify.wildcard_fqdn == "*.test.example.com"
    assert verify.comment == "Updated Test Wildcard FQDN"


def test_get_specific_wildcard_fqdn_custom():
    """Test: Get specific wildcard FQDN address."""
    result = fgt.api.cmdb.firewall.wildcard_fqdn.custom.get(name=TEST_NAME)
    assert result is not None
    assert result.name == TEST_NAME


def test_delete_wildcard_fqdn_custom():
    """Test: Delete wildcard FQDN address."""
    result = fgt.api.cmdb.firewall.wildcard_fqdn.custom.delete(name=TEST_NAME)
    assert result is not None
    assert result.http_status == "success"
    
    # Verify deletion
    addresses = fgt.api.cmdb.firewall.wildcard_fqdn.custom.get()
    addr_names = [a.name for a in addresses]
    assert TEST_NAME not in addr_names, "Wildcard FQDN should have been deleted"


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
        
    test_get_wildcard_fqdn_custom()
    print("✓ test_get_wildcard_fqdn_custom passed")

    test_post_wildcard_fqdn_custom()
    print("✓ test_post_wildcard_fqdn_custom passed")

    test_put_wildcard_fqdn_custom()
    print("✓ test_put_wildcard_fqdn_custom passed")

    test_get_specific_wildcard_fqdn_custom()
    print("✓ test_get_specific_wildcard_fqdn_custom passed")

    test_delete_wildcard_fqdn_custom()
    print("✓ test_delete_wildcard_fqdn_custom passed")

    cleanup()
    print("✓ post-Cleanup passed")
    
    print("\n✓ All tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
