import argparse
import sys
from pathlib import Path

import pytest

# Run tests on a single worker to preserve state (group by filename)
pytestmark = pytest.mark.xdist_group(Path(__file__).stem)

# Add pytest directory to path (go up from endpoints/cmdb/ to pytest/)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt


TEST_NAME = "test_wildcard_fqdn_group1"
TEST_MEMBER1 = "test_wfqdn_member1"
TEST_MEMBER2 = "test_wfqdn_member2"


def cleanup():
    """Clean up test wildcard FQDN groups and members."""
    # Delete groups first (they reference members)
    try:
        groups = fgt.api.cmdb.firewall.wildcard_fqdn.group.get()
        for group in groups:
            if group.name and str(group.name).startswith("test_"):
                try:
                    fgt.api.cmdb.firewall.wildcard_fqdn.group.delete(name=group.name)
                except Exception:
                    pass
    except Exception:
        pass
    
    # Then delete custom wildcard FQDNs
    try:
        customs = fgt.api.cmdb.firewall.wildcard_fqdn.custom.get()
        for custom in customs:
            if custom.name and str(custom.name).startswith("test_"):
                try:
                    fgt.api.cmdb.firewall.wildcard_fqdn.custom.delete(name=custom.name)
                except Exception:
                    pass
    except Exception:
        pass


def setup_members():
    """Create wildcard FQDN members for group testing."""
    # Check if members already exist
    try:
        fgt.api.cmdb.firewall.wildcard_fqdn.custom.get(name=TEST_MEMBER1)
    except Exception:
        fgt.api.cmdb.firewall.wildcard_fqdn.custom.post(
            name=TEST_MEMBER1,
            wildcard_fqdn="*.member1.example.com"
        )
    try:
        fgt.api.cmdb.firewall.wildcard_fqdn.custom.get(name=TEST_MEMBER2)
    except Exception:
        fgt.api.cmdb.firewall.wildcard_fqdn.custom.post(
            name=TEST_MEMBER2,
            wildcard_fqdn="*.member2.example.com"
        )


@pytest.fixture(scope="module", autouse=True)
def setup_and_teardown():
    """Setup members before tests and cleanup after."""
    cleanup()
    setup_members()
    yield
    cleanup()


def test_get_wildcard_fqdn_groups():
    """Test: Get all wildcard FQDN groups."""
    result = fgt.api.cmdb.firewall.wildcard_fqdn.group.get()
    assert result is not None
    assert result.http_status_code == 200


def test_post_wildcard_fqdn_group():
    """Test: Create wildcard FQDN group with members."""
    result = fgt.api.cmdb.firewall.wildcard_fqdn.group.post(
        name=TEST_NAME,
        member=[{"name": TEST_MEMBER1}],
        comment="Test Wildcard FQDN Group"
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_wildcard_fqdn_group():
    """Test: Update wildcard FQDN group - add second member."""
    result = fgt.api.cmdb.firewall.wildcard_fqdn.group.put(
        name=TEST_NAME,
        member=[{"name": TEST_MEMBER1}, {"name": TEST_MEMBER2}],
        comment="Updated Test Wildcard FQDN Group"
    )
    assert result is not None
    assert result.http_status == "success"
    
    # Verify the update
    verify = fgt.api.cmdb.firewall.wildcard_fqdn.group.get(name=TEST_NAME)
    assert verify is not None
    assert verify.comment == "Updated Test Wildcard FQDN Group"
    member_names = [m.name for m in verify.member]
    assert TEST_MEMBER2 in member_names


def test_get_specific_wildcard_fqdn_group():
    """Test: Get specific wildcard FQDN group."""
    result = fgt.api.cmdb.firewall.wildcard_fqdn.group.get(name=TEST_NAME)
    assert result is not None
    assert result.name == TEST_NAME


def test_delete_wildcard_fqdn_group():
    """Test: Delete wildcard FQDN group."""
    result = fgt.api.cmdb.firewall.wildcard_fqdn.group.delete(name=TEST_NAME)
    assert result is not None
    assert result.http_status == "success"
    
    # Verify deletion
    groups = fgt.api.cmdb.firewall.wildcard_fqdn.group.get()
    group_names = [g.name for g in groups]
    assert TEST_NAME not in group_names, "Wildcard FQDN group should have been deleted"


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
    
    setup_members()
    print("✓ Setup members passed")
        
    test_get_wildcard_fqdn_groups()
    print("✓ test_get_wildcard_fqdn_groups passed")

    test_post_wildcard_fqdn_group()
    print("✓ test_post_wildcard_fqdn_group passed")

    test_put_wildcard_fqdn_group()
    print("✓ test_put_wildcard_fqdn_group passed")

    test_get_specific_wildcard_fqdn_group()
    print("✓ test_get_specific_wildcard_fqdn_group passed")

    test_delete_wildcard_fqdn_group()
    print("✓ test_delete_wildcard_fqdn_group passed")

    cleanup()
    print("✓ post-Cleanup passed")
    
    print("\n✓ All tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
