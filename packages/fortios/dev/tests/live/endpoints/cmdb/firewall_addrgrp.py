import argparse
import sys
from pathlib import Path

import pytest

# Run tests on a single worker to preserve state (group by filename)
pytestmark = pytest.mark.xdist_group(Path(__file__).stem)

# Add pytest directory to path (go up from endpoints/cmdb/ to pytest/)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt


TEST_NAME = "test_addrgrp1"
TEST_MEMBER1 = "test_addr_member1"
TEST_MEMBER2 = "test_addr_member2"


def cleanup():
    """Clean up test address groups and member addresses."""
    # Delete address groups first (they reference addresses)
    try:
        groups = fgt.api.cmdb.firewall.addrgrp.get()
        for grp in groups:
            if grp.name and str(grp.name).startswith("test"):
                try:
                    fgt.api.cmdb.firewall.addrgrp.delete(name=grp.name)
                except Exception:
                    pass
    except Exception:
        pass
    
    # Then delete member addresses
    try:
        addresses = fgt.api.cmdb.firewall.address.get()
        for addr in addresses:
            if addr.name and str(addr.name).startswith("test_addr_member"):
                try:
                    fgt.api.cmdb.firewall.address.delete(name=addr.name)
                except Exception:
                    pass
    except Exception:
        pass


def setup_members():
    """Create member addresses for the group."""
    # Create first member address
    fgt.api.cmdb.firewall.address.post(
        name=TEST_MEMBER1,
        type="ipmask",
        subnet="192.168.200.0/24",
    )
    # Create second member address
    fgt.api.cmdb.firewall.address.post(
        name=TEST_MEMBER2,
        type="ipmask",
        subnet="192.168.201.0/24",
    )


@pytest.fixture(scope="module", autouse=True)
def setup_and_teardown():
    """Setup and teardown for pytest."""
    cleanup()
    setup_members()
    yield
    cleanup()


def test_get_addrgrps():
    """Test: Get all IPv4 address groups."""
    result = fgt.api.cmdb.firewall.addrgrp.get()
    assert result is not None
    assert result.http_status_code == 200


def test_post_addrgrp():
    """Test: Create IPv4 address group."""
    result = fgt.api.cmdb.firewall.addrgrp.post(
        name=TEST_NAME,
        member=[{"name": TEST_MEMBER1}],
        comment="Test IPv4 address group",
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_addrgrp():
    """Test: Update IPv4 address group."""
    result = fgt.api.cmdb.firewall.addrgrp.put(
        name=TEST_NAME,
        member=[{"name": TEST_MEMBER1}, {"name": TEST_MEMBER2}],
        comment="Updated IPv4 address group",
    )
    assert result is not None
    assert result.http_status == "success"
    
    # Verify the update
    verify = fgt.api.cmdb.firewall.addrgrp.get(name=TEST_NAME)
    assert verify is not None
    assert verify.comment == "Updated IPv4 address group"
    assert len(verify.member) == 2


def test_get_specific_addrgrp():
    """Test: Get specific IPv4 address group."""
    result = fgt.api.cmdb.firewall.addrgrp.get(name=TEST_NAME)
    assert result is not None
    assert result.name == TEST_NAME


def test_delete_addrgrp():
    """Test: Delete IPv4 address group."""
    result = fgt.api.cmdb.firewall.addrgrp.delete(name=TEST_NAME)
    assert result is not None
    assert result.http_status == "success"
    
    # Verify deletion
    groups = fgt.api.cmdb.firewall.addrgrp.get()
    group_names = [g.name for g in groups]
    assert TEST_NAME not in group_names, "Address group should have been deleted"


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
    setup_members()
    print("✓ Pre-Cleanup and Setup passed")
        
    test_get_addrgrps()
    print("✓ test_get_addrgrps passed")

    test_post_addrgrp()
    print("✓ test_post_addrgrp passed")

    test_put_addrgrp()
    print("✓ test_put_addrgrp passed")

    test_get_specific_addrgrp()
    print("✓ test_get_specific_addrgrp passed")

    test_delete_addrgrp()
    print("✓ test_delete_addrgrp passed")

    cleanup()
    print("✓ post-Cleanup passed")
    
    print("\n✓ All tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
