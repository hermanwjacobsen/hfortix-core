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



def test_get_switch_controller_managed_switch_port_health():
    """Test GET /monitor/switch-controller/managed-switch/port-health - Retrieve port health statistics for managed FortiSwitches."""

    result = fgt.api.monitor.switch_controller.managed_switch.port_health.get(vdom="root")
    assert result is not None
    assert result.http_status_code == 200
    print(f"✓ Retrieved port health statistics")


def test_get_switch_controller_managed_switch_port_health_structure():
    """Test: Explore port health data structure"""
    
    result = fgt.api.monitor.switch_controller.managed_switch.port_health.get(vdom="root")
    assert result is not None
    
    print(f"✓ Port health data type: {type(result)}")
    
    # Port health returns a FortiObject with switch serials as keys
    result_dict = dict(result)
    print(f"✓ Port health structure: dict with {len(result_dict)} switch(es)")
    
    for switch_serial, ports in result_dict.items():
        print(f"✓ Switch {switch_serial}: {len(ports)} port(s) with health data")
        if ports and len(ports) > 0:
            first_port = ports[0]
            print(f"  First port structure: {type(first_port).__name__}")
            if hasattr(first_port, '__dict__'):
                attrs = [attr for attr in dir(first_port) if not attr.startswith('_')]
                print(f"  Available attributes: {', '.join(attrs[:10])}")




def test_get_switch_controller_managed_switch_port_health_with_filter():
    """Test: Get port health for specific FortiSwitch using mkey filter"""
    
    # First get all port health to find a valid switch serial
    all_health = fgt.api.monitor.switch_controller.managed_switch.port_health.get(vdom="root")
    
    all_health_dict = dict(all_health)
    if len(all_health_dict) == 0:
        skip_test("No managed switches in port health data")
    
    # Get first switch serial (the key in the dict)
    switch_serial = list(all_health_dict.keys())[0]
    
    # Get port health for specific switch
    result = fgt.api.monitor.switch_controller.managed_switch.port_health.get(
        vdom="root",
        mkey=switch_serial
    )
    
    assert result is not None
    assert result.http_status_code == 200
    
    result_dict = dict(result)
    print(f"✓ Got port health for FortiSwitch: {switch_serial} ({len(result_dict)} switch(es) in response)")
    
    # Verify the requested switch is in the response
    assert switch_serial in result_dict, f"Expected switch {switch_serial} in response"



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
    test_get_switch_controller_managed_switch_port_health()
    print("✓ test_get_switch_controller_managed_switch_port_health passed")
    test_get_switch_controller_managed_switch_port_health_structure()
    print("✓ test_get_switch_controller_managed_switch_port_health_structure passed")
    test_get_switch_controller_managed_switch_port_health_with_filter()
    print("✓ test_get_switch_controller_managed_switch_port_health_with_filter passed")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
