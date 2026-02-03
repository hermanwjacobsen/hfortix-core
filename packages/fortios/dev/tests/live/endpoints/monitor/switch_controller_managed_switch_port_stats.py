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



def test_get_switch_controller_managed_switch_port_stats():
    """Test GET /monitor/switch-controller/managed-switch/port-stats - Retrieve port statistics for FortiSwitches."""

    result = fgt.api.monitor.switch_controller.managed_switch.port_stats.get(vdom="root")
    assert result is not None
    assert result.http_status_code == 200
    print(f"✓ Retrieved port statistics for {len(result)} FortiSwitch(es)")


def test_get_switch_controller_managed_switch_port_stats_verify_structure():
    """Test: Verify port statistics structure if switches exist"""
    
    result = fgt.api.monitor.switch_controller.managed_switch.port_stats.get(vdom="root")
    assert result is not None
    
    # If FortiSwitches exist, verify their structure
    if len(result) > 0:
        switch = result[0]  # type: ignore
        
        # Verify expected fields exist
        assert hasattr(switch, 'serial'), "Switch should have 'serial' field"
        assert hasattr(switch, 'switch_id') or hasattr(switch, 'switch-id'), "Switch should have 'switch_id' or 'switch-id' field"
        
        serial = switch.serial
        switch_id = getattr(switch, 'switch_id', None) or getattr(switch, 'switch-id', None)
        
        print(f"✓ First switch: serial={serial}, switch_id={switch_id}")
        
        # Verify ports field exists
        if hasattr(switch, 'ports'):
            print(f"✓ Switch has 'ports' statistics map")
            
            # If ports is a dict, show first port
            if isinstance(switch.ports, dict) and switch.ports:
                first_port_name = list(switch.ports.keys())[0]
                print(f"✓ First port: {first_port_name}")
        else:
            print("⚠ Switch does not have 'ports' field (may be empty)")
    else:
        print("✓ No FortiSwitches connected (port statistics unavailable)")


def test_get_switch_controller_managed_switch_port_stats_with_filter():
    """Test: Get port statistics for specific FortiSwitch using mkey filter"""
    
    # First get all switches to see if any exist
    all_switches = fgt.api.monitor.switch_controller.managed_switch.port_stats.get(vdom="root")
    
    if len(all_switches) > 0:
        # Get the first switch's ID
        switch = all_switches[0]  # type: ignore
        switch_id = getattr(switch, 'switch_id', None) or getattr(switch, 'switch-id', None)
        
        # Query for specific switch using mkey parameter
        result = fgt.api.monitor.switch_controller.managed_switch.port_stats.get(
            vdom="root",
            mkey=switch_id
        )
        assert result is not None
        assert result.http_status_code == 200
        
        print(f"✓ Retrieved port statistics for FortiSwitch: {switch_id}")
        
        # Verify we got statistics for the requested switch
        if len(result) > 0:
            filtered_switch = result[0]  # type: ignore
            filtered_id = getattr(filtered_switch, 'switch_id', None) or getattr(filtered_switch, 'switch-id', None)
            assert filtered_id == switch_id, f"Expected switch_id={switch_id}, got {filtered_id}"
            print(f"✓ Filtered results match requested switch ID")
    else:
        print("✓ No FortiSwitches available to test mkey filter")


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
    test_get_switch_controller_managed_switch_port_stats()
    print("✓ test_get_switch_controller_managed_switch_port_stats passed")
    
    test_get_switch_controller_managed_switch_port_stats_verify_structure()
    print("✓ test_get_switch_controller_managed_switch_port_stats_verify_structure passed")
    
    test_get_switch_controller_managed_switch_port_stats_with_filter()
    print("✓ test_get_switch_controller_managed_switch_port_stats_with_filter passed")
    
    print("✓ All switch-controller/managed-switch/port-stats tests passed")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
