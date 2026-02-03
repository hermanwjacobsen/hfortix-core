import argparse
import sys
from pathlib import Path

import pytest

# Run tests on a single worker to preserve state (group by filename)
pytestmark = pytest.mark.xdist_group(Path(__file__).stem)

# Add pytest directory to path (go up from endpoints/cmdb/ to pytest/)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt


TEST_NAME = "test_schedule_group1"


def cleanup():
    """Clean up test schedule groups."""
    try:
        groups = fgt.api.cmdb.firewall.schedule.group.get()
        for group in groups:
            if group.name and str(group.name).startswith("test_"):
                try:
                    fgt.api.cmdb.firewall.schedule.group.delete(name=group.name)
                except Exception:
                    pass
    except Exception:
        pass


def test_get_schedule_groups():
    """Test: Get all schedule groups."""
    result = fgt.api.cmdb.firewall.schedule.group.get()
    assert result is not None
    assert result.http_status_code == 200


def test_post_schedule_group():
    """Test: Create schedule group."""
    result = fgt.api.cmdb.firewall.schedule.group.post(
        name=TEST_NAME,
        member=["always", "none"]  # Use existing recurring schedules
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_schedule_group():
    """Test: Update schedule group."""
    result = fgt.api.cmdb.firewall.schedule.group.put(
        name=TEST_NAME,
        member=["always"]  # Update to single member
    )
    assert result is not None
    assert result.http_status == "success"
    
    # Verify the update
    verify = fgt.api.cmdb.firewall.schedule.group.get(name=TEST_NAME)
    assert verify is not None
    assert len(verify.member) == 1


def test_get_specific_schedule_group():
    """Test: Get specific schedule group."""
    result = fgt.api.cmdb.firewall.schedule.group.get(name=TEST_NAME)
    assert result is not None
    assert result.name == TEST_NAME


def test_delete_schedule_group():
    """Test: Delete schedule group."""
    result = fgt.api.cmdb.firewall.schedule.group.delete(name=TEST_NAME)
    assert result is not None
    assert result.http_status == "success"
    
    # Verify deletion
    groups = fgt.api.cmdb.firewall.schedule.group.get()
    group_names = [g.name for g in groups]
    assert TEST_NAME not in group_names, "Group should have been deleted"


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
        
    test_get_schedule_groups()
    print("✓ test_get_schedule_groups passed")

    test_post_schedule_group()
    print("✓ test_post_schedule_group passed")

    test_put_schedule_group()
    print("✓ test_put_schedule_group passed")

    test_get_specific_schedule_group()
    print("✓ test_get_specific_schedule_group passed")

    test_delete_schedule_group()
    print("✓ test_delete_schedule_group passed")

    cleanup()
    print("✓ post-Cleanup passed")
    
    print("\n✓ All tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
