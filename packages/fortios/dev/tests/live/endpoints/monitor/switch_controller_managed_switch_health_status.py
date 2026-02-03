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



def test_get_switch_controller_managed_switch_health_status():
    """Test GET /monitor/switch-controller/managed-switch/health-status - Retrieve health statistics for managed FortiSwitches."""

    result = fgt.api.monitor.switch_controller.managed_switch.health_status.get(vdom="root")
    assert result is not None
    assert result.http_status_code == 200
    print(f"✓ Retrieved health status for {len(result)} managed switch(es)")


def test_get_switch_controller_managed_switch_health_status_structure():
    """Test: Verify health status structure if switches exist"""
    
    result = fgt.api.monitor.switch_controller.managed_switch.health_status.get(vdom="root")
    assert result is not None
    
    # If FortiSwitches exist, verify their structure
    if len(result) > 0:
        switch = result[0]  # type: ignore
        
        # Verify expected fields exist
        serial = getattr(switch, 'serial', None)
        switch_id = getattr(switch, 'switch-id', None) or getattr(switch, 'switch_id', None)
        
        print(f"✓ First switch: serial={serial}, switch_id={switch_id}")
        
        # Check for health status components
        if hasattr(switch, 'poe'):
            print(f"✓ POE health data available")
        
        if hasattr(switch, 'performance'):
            perf = switch.performance
            if hasattr(perf, 'cpu'):
                print(f"✓ CPU status: {perf.cpu}")
            if hasattr(perf, 'memory'):
                print(f"✓ Memory status: {perf.memory}")
            if hasattr(perf, 'uptime'):
                print(f"✓ Uptime status: {perf.uptime}")
        
        if hasattr(switch, 'temperature') and switch.temperature:
            print(f"✓ Temperature sensors: {len(switch.temperature)}")
        
        if hasattr(switch, 'fan') and switch.fan:
            print(f"✓ Fans: {len(switch.fan)}")
        
        if hasattr(switch, 'psu') and switch.psu:
            print(f"✓ Power supplies: {len(switch.psu)}")
        
        if hasattr(switch, 'summary'):
            summary = switch.summary
            if hasattr(summary, 'overall'):
                print(f"✓ Overall health rating: {summary.overall}")
    else:
        print("✓ No FortiSwitches connected (health status unavailable)")


def test_get_switch_controller_managed_switch_health_status_with_filter():
    """Test: Get health status for specific FortiSwitch using serial filter"""
    
    # First get all switches to see if any exist
    all_switches = fgt.api.monitor.switch_controller.managed_switch.health_status.get(vdom="root")
    
    if len(all_switches) == 0:
        skip_test("No managed switches to filter")
    
    # Get serial number from first switch
    first_switch = all_switches[0]  # type: ignore
    switch_serial = getattr(first_switch, 'serial', None)
    
    if not switch_serial:
        skip_test("Switch does not have serial number")
    
    # Get health status for specific switch
    result = fgt.api.monitor.switch_controller.managed_switch.health_status.get(
        vdom="root",
        serial=switch_serial
    )
    
    assert result is not None
    assert result.http_status_code == 200
    
    # Verify we got the right switch
    if len(result) > 0:
        returned_switch = result[0]  # type: ignore
        returned_serial = getattr(returned_switch, 'serial', None)
        assert returned_serial == switch_serial, f"Expected serial {switch_serial}, got {returned_serial}"
        print(f"✓ Got health status for FortiSwitch serial: {switch_serial}")


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
    test_get_switch_controller_managed_switch_health_status()
    print("✓ test_get_switch_controller_managed_switch_health_status passed")
    test_get_switch_controller_managed_switch_health_status_structure()
    print("✓ test_get_switch_controller_managed_switch_health_status_structure passed")
    test_get_switch_controller_managed_switch_health_status_with_filter()
    print("✓ test_get_switch_controller_managed_switch_health_status_with_filter passed")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
