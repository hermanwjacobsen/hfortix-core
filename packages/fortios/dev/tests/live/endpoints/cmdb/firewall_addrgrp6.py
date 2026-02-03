import argparse
import sys
from pathlib import Path

import pytest

# Run tests on a single worker to preserve state (group by filename)
pytestmark = pytest.mark.xdist_group(Path(__file__).stem)

# Add pytest directory to path (go up from endpoints/cmdb/ to pytest/)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt


TEST_NAME = "test_addrgrp6_1"
TEST_MEMBER1 = "test_addr6_member1"
TEST_MEMBER2 = "test_addr6_member2"


def cleanup():
    """Clean up test IPv6 address groups and member addresses."""
    # Delete address groups first (they reference addresses)
    try:
        groups = fgt.api.cmdb.firewall.addrgrp6.get()
        for grp in groups:
            if grp.name and str(grp.name).startswith("test"):
                try:
                    fgt.api.cmdb.firewall.addrgrp6.delete(name=grp.name)
                except Exception:
                    pass
    except Exception:
        pass
    
    # Then delete member addresses
    try:
        addresses = fgt.api.cmdb.firewall.address6.get()
        for addr in addresses:
            if addr.name and str(addr.name).startswith("test_addr6_member"):
                try:
                    fgt.api.cmdb.firewall.address6.delete(name=addr.name)
                except Exception:
                    pass
    except Exception:
        pass


def setup_members():
    """Create member IPv6 addresses for the group."""
    # Create first member address
    fgt.api.cmdb.firewall.address6.post(
        name=TEST_MEMBER1,
        type="ipprefix",
        ip6="2001:db8:200::/64",
    )
    # Create second member address
    fgt.api.cmdb.firewall.address6.post(
        name=TEST_MEMBER2,
        type="ipprefix",
        ip6="2001:db8:201::/64",
    )


@pytest.fixture(scope="module", autouse=True)
def setup_and_teardown():
    """Setup and teardown for pytest."""
    cleanup()
    setup_members()
    yield
    cleanup()


def test_get_addrgrps6():
    """Test: Get all IPv6 address groups."""
    result = fgt.api.cmdb.firewall.addrgrp6.get()
    assert result is not None
    assert result.http_status_code == 200


def test_post_addrgrp6():
    """Test: Create IPv6 address group."""
    result = fgt.api.cmdb.firewall.addrgrp6.post(
        name=TEST_NAME,
        member=[{"name": TEST_MEMBER1}],
        comment="Test IPv6 address group",
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_addrgrp6():
    """Test: Update IPv6 address group."""
    result = fgt.api.cmdb.firewall.addrgrp6.put(
        name=TEST_NAME,
        member=[{"name": TEST_MEMBER1}, {"name": TEST_MEMBER2}],
        comment="Updated IPv6 address group",
    )
    assert result is not None
    assert result.http_status == "success"
    
    # Verify the update
    verify = fgt.api.cmdb.firewall.addrgrp6.get(name=TEST_NAME)
    assert verify is not None
    assert verify.comment == "Updated IPv6 address group"
    assert len(verify.member) == 2


def test_get_specific_addrgrp6():
    """Test: Get specific IPv6 address group."""
    result = fgt.api.cmdb.firewall.addrgrp6.get(name=TEST_NAME)
    assert result is not None
    assert result.name == TEST_NAME


def test_delete_addrgrp6():
    """Test: Delete IPv6 address group."""
    result = fgt.api.cmdb.firewall.addrgrp6.delete(name=TEST_NAME)
    assert result is not None
    assert result.http_status == "success"
    
    # Verify deletion
    groups = fgt.api.cmdb.firewall.addrgrp6.get()
    group_names = [g.name for g in groups]
    assert TEST_NAME not in group_names, "IPv6 address group should have been deleted"


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
        
    test_get_addrgrps6()
    print("✓ test_get_addrgrps6 passed")

    test_post_addrgrp6()
    print("✓ test_post_addrgrp6 passed")

    test_put_addrgrp6()
    print("✓ test_put_addrgrp6 passed")

    test_get_specific_addrgrp6()
    print("✓ test_get_specific_addrgrp6 passed")

    test_delete_addrgrp6()
    print("✓ test_delete_addrgrp6 passed")

    cleanup()
    print("✓ post-Cleanup passed")
    
    print("\n✓ All tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
