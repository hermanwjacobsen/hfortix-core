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



def test_get_switch_controller_detected_device():
    """Test GET /monitor/switch-controller/detected-device - Retrieve devices detected on all switches."""

    result = fgt.api.monitor.switch_controller.detected_device.get(vdom="root")
    assert result is not None
    assert result.http_status_code == 200
    print(f"✓ Retrieved detected devices from FortiSwitches")


def test_get_switch_controller_detected_device_verify_structure():
    """Test: Verify detected device response structure"""
    
    result = fgt.api.monitor.switch_controller.detected_device.get(vdom="root")
    assert result is not None
    
    print(f"✓ Detected devices response type: {type(result)}")
    print(f"✓ Number of detected devices: {len(result)}")
    
    # If devices are detected, show structure
    if len(result) > 0:
        first_device = result[0]  # type: ignore
        print(f"\n  Sample detected device:")
        
        # Common fields to check
        for attr in ['mac', 'port_name', 'port-name', 'switch_id', 'switch-id', 'vlan_id', 'vlan-id',
                     'port_id', 'port-id', 'last_seen', 'last-seen', 'vdom']:
            if hasattr(first_device, attr):
                value = getattr(first_device, attr)
                if value is not None:
                    print(f"    {attr}: {value}")
    else:
        print("  No devices detected on switches")


def test_get_switch_controller_detected_device_count():
    """Test: Count total detected devices across all switches"""
    
    result = fgt.api.monitor.switch_controller.detected_device.get(vdom="root")
    assert result is not None
    
    device_count = len(result)
    print(f"✓ Total detected devices: {device_count}")
    
    if device_count > 0:
        # Try to group by switch
        switches = {}
        for device in result:  # type: ignore
            switch_id = getattr(device, 'switch_id', None) or getattr(device, 'switch-id', None)
            if switch_id:
                switches[switch_id] = switches.get(switch_id, 0) + 1
        
        print(f"  Devices per switch:")
        for switch_id, count in switches.items():
            print(f"    {switch_id}: {count} device(s)")


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
    test_get_switch_controller_detected_device()
    print("✓ test_get_switch_controller_detected_device passed")
    test_get_switch_controller_detected_device_verify_structure()
    print("✓ test_get_switch_controller_detected_device_verify_structure passed")
    test_get_switch_controller_detected_device_count()
    print("✓ test_get_switch_controller_detected_device_count passed")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
