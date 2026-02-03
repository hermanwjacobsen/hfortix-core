import argparse
import sys
from pathlib import Path

import pytest

# Run tests on a single worker to preserve state (group by filename)
pytestmark = pytest.mark.xdist_group(Path(__file__).stem)

# Add pytest directory to path (go up from endpoints/cmdb/ to pytest/)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt


TEST_NAME = "test_service_group1"


def cleanup():
    """Clean up test service groups."""
    try:
        groups = fgt.api.cmdb.firewall.service.group.get()
        for group in groups:
            if group.name and str(group.name).startswith("test_"):
                try:
                    fgt.api.cmdb.firewall.service.group.delete(name=group.name)
                except Exception:
                    pass
    except Exception:
        pass


def test_get_service_groups():
    """Test: Get all service groups."""
    result = fgt.api.cmdb.firewall.service.group.get()
    assert result is not None
    assert result.http_status_code == 200


def test_post_service_group():
    """Test: Create service group with HTTP and HTTPS members."""
    result = fgt.api.cmdb.firewall.service.group.post(
        name=TEST_NAME,
        member=[{"name": "HTTP"}, {"name": "HTTPS"}],
        comment="Test Service Group"
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_service_group():
    """Test: Update service group - add SSH to members."""
    result = fgt.api.cmdb.firewall.service.group.put(
        name=TEST_NAME,
        member=[{"name": "HTTP"}, {"name": "HTTPS"}, {"name": "SSH"}],
        comment="Updated Test Service Group"
    )
    assert result is not None
    assert result.http_status == "success"
    
    # Verify the update
    verify = fgt.api.cmdb.firewall.service.group.get(name=TEST_NAME)
    assert verify is not None
    assert verify.comment == "Updated Test Service Group"
    member_names = [m.name for m in verify.member]
    assert "SSH" in member_names


def test_get_specific_service_group():
    """Test: Get specific service group."""
    result = fgt.api.cmdb.firewall.service.group.get(name=TEST_NAME)
    assert result is not None
    assert result.name == TEST_NAME


def test_delete_service_group():
    """Test: Delete service group."""
    result = fgt.api.cmdb.firewall.service.group.delete(name=TEST_NAME)
    assert result is not None
    assert result.http_status == "success"
    
    # Verify deletion
    groups = fgt.api.cmdb.firewall.service.group.get()
    group_names = [g.name for g in groups]
    assert TEST_NAME not in group_names, "Service group should have been deleted"


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
        
    test_get_service_groups()
    print("✓ test_get_service_groups passed")

    test_post_service_group()
    print("✓ test_post_service_group passed")

    test_put_service_group()
    print("✓ test_put_service_group passed")

    test_get_specific_service_group()
    print("✓ test_get_specific_service_group passed")

    test_delete_service_group()
    print("✓ test_delete_service_group passed")

    cleanup()
    print("✓ post-Cleanup passed")
    
    print("\n✓ All tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
