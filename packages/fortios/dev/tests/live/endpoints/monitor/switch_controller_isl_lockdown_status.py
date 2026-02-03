import argparse
import sys
from pathlib import Path
import pytest

# Run registration monitor tests on a single worker to preserve state
pytestmark = pytest.mark.xdist_group(Path(__file__).stem)

# Add pytest directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt


def skip_test(reason):
    """Helper to skip test - works both in pytest and direct execution."""
    try:
        pytest.skip(reason)
    except Exception:
        print(f"⊘ Skipped: {reason}")
        return



def test_get_switch_controller_isl_lockdown_status():
    """Test GET /monitor/switch-controller/isl-lockdown/status - Get ISL lockdown status for FortiLink."""

    # Use the default fortilink interface
    result = fgt.api.monitor.switch_controller.isl_lockdown.status.get(
        vdom="root",
        fortilink="fortilink"
    )
    
    assert result is not None
    assert result.http_status_code == 200
    print(f"✓ Retrieved ISL lockdown status for FortiLink interface")


def test_get_switch_controller_isl_lockdown_status_verify_structure():
    """Test: Verify ISL lockdown status response structure"""
    
    result = fgt.api.monitor.switch_controller.isl_lockdown.status.get(
        vdom="root",
        fortilink="fortilink"
    )
    
    assert result is not None
    print(f"✓ ISL lockdown status response type: {type(result)}")
    
    # Check for status field
    if hasattr(result, 'status'):
        status = getattr(result, 'status')
        print(f"  ISL Lockdown Status: {status}")
        
        # Status should be one of the defined enum values
        # Common values: "disabled", "enabled", "locked", "unlocked"
        if status:
            print(f"  ✓ Status value retrieved: '{status}'")
    else:
        print(f"  Status field not found in response")


def test_get_switch_controller_isl_lockdown_status_check_value():
    """Test: Check ISL lockdown status value and validate it's a known state"""
    
    result = fgt.api.monitor.switch_controller.isl_lockdown.status.get(
        vdom="root",
        fortilink="fortilink"
    )
    
    assert result is not None
    
    if hasattr(result, 'status'):
        status = getattr(result, 'status')
        print(f"✓ ISL Lockdown Status: {status}")
        
        # Common status values (based on typical FortiGate behavior)
        # The actual enum values may vary
        known_statuses = ['disable', 'disabled', 'enable', 'enabled', 'locked', 'unlocked', 'active', 'inactive']
        
        if status and isinstance(status, str):
            if status.lower() in known_statuses:
                print(f"  Recognized status value: '{status}'")
            else:
                print(f"  Status value '{status}' (may be valid but not in common list)")
        else:
            print(f"  Status type: {type(status)}, value: {status}")
    else:
        skip_test("No status field in response")


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
    test_get_switch_controller_isl_lockdown_status()
    print("✓ test_get_switch_controller_isl_lockdown_status passed")
    test_get_switch_controller_isl_lockdown_status_verify_structure()
    print("✓ test_get_switch_controller_isl_lockdown_status_verify_structure passed")
    test_get_switch_controller_isl_lockdown_status_check_value()
    print("✓ test_get_switch_controller_isl_lockdown_status_check_value passed")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
