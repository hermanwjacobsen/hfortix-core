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



def test_get_switch_controller_matched_devices():
    """Test GET /monitor/switch-controller/matched-devices - Return devices matching NAC and/or dynamic port policies."""

    result = fgt.api.monitor.switch_controller.matched_devices.get(vdom="root")
    assert result is not None
    assert result.http_status_code == 200
    print(f"✓ Retrieved matched devices (NAC/dynamic port policies)")


def test_get_switch_controller_matched_devices_verify_structure():
    """Test: Verify matched devices response structure"""
    
    result = fgt.api.monitor.switch_controller.matched_devices.get(vdom="root")
    assert result is not None
    
    print(f"✓ Matched devices response type: {type(result)}")
    print(f"✓ Number of matched devices: {len(result)}")
    
    # If devices match policies, show structure
    if len(result) > 0:
        first_device = result[0]  # type: ignore
        print(f"\n  Sample matched device:")
        
        # Common fields to check
        for attr in ['mac_address', 'mac-address', 'switch_id', 'switch-id', 'port', 'interface',
                     'policy', 'policy_name', 'policy-name', 'vlan', 'matched_on', 'matched-on']:
            if hasattr(first_device, attr):
                value = getattr(first_device, attr)
                print(f"    {attr}: {value}")
    else:
        print("  No devices match NAC or dynamic port policies")


def test_get_switch_controller_matched_devices_with_mkey():
    """Test: Get matched devices for specific FortiSwitch using mkey filter"""
    
    # First get a switch ID
    switches = fgt.api.monitor.switch_controller.managed_switch.status.get(vdom="root")
    
    if len(switches) == 0:
        skip_test("No managed switches available for mkey filter test")
    
    first_switch = switches[0]  # type: ignore
    switch_id = getattr(first_switch, 'switch_id', None)
    
    if not switch_id:
        skip_test("Switch does not have ID")
    
    # Get matched devices for specific switch
    result = fgt.api.monitor.switch_controller.matched_devices.get(
        vdom="root",
        mkey=switch_id
    )
    
    assert result is not None
    assert result.http_status_code == 200
    print(f"✓ Got matched devices for FortiSwitch: {switch_id} ({len(result)} device(s))")


def test_get_switch_controller_matched_devices_with_include_dynamic():
    """Test: Get matched devices including dynamic port policies"""
    
    # Test with include_dynamic parameter set to true
    result = fgt.api.monitor.switch_controller.matched_devices.get(
        vdom="root",
        include_dynamic=True
    )
    
    assert result is not None
    assert result.http_status_code == 200
    print(f"✓ Retrieved matched devices with include_dynamic=true ({len(result)} device(s))")


def test_get_switch_controller_matched_devices_with_mac():
    """Test: Get matched devices filtered by MAC address"""
    
    # First try to get all matched devices to find a MAC
    all_devices = fgt.api.monitor.switch_controller.matched_devices.get(vdom="root")
    
    if len(all_devices) == 0:
        skip_test("No matched devices available to filter by MAC")
    
    # Get first device's MAC
    first_device = all_devices[0]  # type: ignore
    device_mac = getattr(first_device, 'mac_address', None) or getattr(first_device, 'mac-address', None)
    
    if not device_mac:
        skip_test("Could not find MAC address in matched device")
    
    # Get matched devices for specific MAC
    result = fgt.api.monitor.switch_controller.matched_devices.get(
        vdom="root",
        mac=device_mac
    )
    
    assert result is not None
    assert result.http_status_code == 200
    print(f"✓ Got matched devices for MAC: {device_mac} ({len(result)} device(s))")


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
    test_get_switch_controller_matched_devices()
    print("✓ test_get_switch_controller_matched_devices passed")
    test_get_switch_controller_matched_devices_verify_structure()
    print("✓ test_get_switch_controller_matched_devices_verify_structure passed")
    test_get_switch_controller_matched_devices_with_mkey()
    print("✓ test_get_switch_controller_matched_devices_with_mkey passed")
    test_get_switch_controller_matched_devices_with_include_dynamic()
    print("✓ test_get_switch_controller_matched_devices_with_include_dynamic passed")
    test_get_switch_controller_matched_devices_with_mac()
    print("✓ test_get_switch_controller_matched_devices_with_mac passed")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
