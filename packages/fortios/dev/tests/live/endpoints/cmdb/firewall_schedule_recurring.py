import argparse
import sys
from pathlib import Path

import pytest

# Run tests on a single worker to preserve state (group by filename)
pytestmark = pytest.mark.xdist_group(Path(__file__).stem)

# Add pytest directory to path (go up from endpoints/cmdb/ to pytest/)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt


TEST_NAME = "test_recurring_schedule1"


def cleanup():
    """Clean up test recurring schedules."""
    try:
        schedules = fgt.api.cmdb.firewall.schedule.recurring.get()
        for schedule in schedules:
            if schedule.name and str(schedule.name).startswith("test_"):
                try:
                    fgt.api.cmdb.firewall.schedule.recurring.delete(name=schedule.name)
                except Exception:
                    pass
    except Exception:
        pass


def test_get_recurring_schedules():
    """Test: Get all recurring schedules."""
    result = fgt.api.cmdb.firewall.schedule.recurring.get()
    assert result is not None
    assert result.http_status_code == 200


def test_post_recurring_schedule():
    """Test: Create recurring schedule."""
    result = fgt.api.cmdb.firewall.schedule.recurring.post(
        name=TEST_NAME,
        start="08:00",
        end="17:00",
        day="monday tuesday wednesday thursday friday"  # Space-separated weekdays
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_recurring_schedule():
    """Test: Update recurring schedule."""
    result = fgt.api.cmdb.firewall.schedule.recurring.put(
        name=TEST_NAME,
        start="09:00",
        end="18:00",
        day="monday wednesday friday"  # Mon/Wed/Fri only
    )
    assert result is not None
    assert result.http_status == "success"
    
    # Verify the update
    verify = fgt.api.cmdb.firewall.schedule.recurring.get(name=TEST_NAME)
    assert verify is not None
    assert verify.start == "09:00"


def test_get_specific_recurring_schedule():
    """Test: Get specific recurring schedule."""
    result = fgt.api.cmdb.firewall.schedule.recurring.get(name=TEST_NAME)
    assert result is not None
    assert result.name == TEST_NAME


def test_delete_recurring_schedule():
    """Test: Delete recurring schedule."""
    result = fgt.api.cmdb.firewall.schedule.recurring.delete(name=TEST_NAME)
    assert result is not None
    assert result.http_status == "success"
    
    # Verify deletion
    schedules = fgt.api.cmdb.firewall.schedule.recurring.get()
    schedule_names = [s.name for s in schedules]
    assert TEST_NAME not in schedule_names, "Schedule should have been deleted"


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
        
    test_get_recurring_schedules()
    print("✓ test_get_recurring_schedules passed")

    test_post_recurring_schedule()
    print("✓ test_post_recurring_schedule passed")

    test_put_recurring_schedule()
    print("✓ test_put_recurring_schedule passed")

    test_get_specific_recurring_schedule()
    print("✓ test_get_specific_recurring_schedule passed")

    test_delete_recurring_schedule()
    print("✓ test_delete_recurring_schedule passed")

    cleanup()
    print("✓ post-Cleanup passed")
    
    print("\n✓ All tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
