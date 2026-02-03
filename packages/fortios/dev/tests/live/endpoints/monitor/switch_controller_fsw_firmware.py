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



def test_get_switch_controller_fsw_firmware():
    """Test GET /monitor/switch-controller/fsw-firmware - Retrieve recommended firmware for managed FortiSwitches."""

    result = fgt.api.monitor.switch_controller.fsw_firmware.get(vdom="root")
    assert result is not None
    assert result.http_status_code == 200
    print(f"✓ Retrieved FortiSwitch firmware recommendations")


def test_get_switch_controller_fsw_firmware_verify_structure():
    """Test: Verify FortiSwitch firmware response structure"""
    
    result = fgt.api.monitor.switch_controller.fsw_firmware.get(vdom="root")
    assert result is not None
    
    print(f"✓ Firmware response type: {type(result)}")
    
    # The response is a dict with switch IDs as keys
    if hasattr(result, '__iter__') and hasattr(result, 'keys'):
        result_dict = dict(result)
        print(f"✓ Firmware data for {len(result_dict)} switch(es)")
        
        for switch_id, firmware_info in list(result_dict.items())[:3]:
            print(f"\n  Switch: {switch_id}")
            
            if hasattr(firmware_info, '__dict__') or isinstance(firmware_info, dict):
                # Show available firmware info fields
                if isinstance(firmware_info, dict):
                    for key, value in list(firmware_info.items())[:5]:
                        print(f"    {key}: {str(value)[:60]}")
                else:
                    attrs = [attr for attr in dir(firmware_info) if not attr.startswith('_')]
                    for attr in attrs[:5]:
                        value = getattr(firmware_info, attr, None)
                        if value is not None:
                            print(f"    {attr}: {str(value)[:60]}")
            else:
                print(f"    Type: {type(firmware_info)}")
    else:
        print(f"  Response structure: {type(result)}")


def test_get_switch_controller_fsw_firmware_with_filter():
    """Test: Get firmware recommendations for specific FortiSwitch using mkey filter"""
    
    # First get a switch ID
    switches = fgt.api.monitor.switch_controller.managed_switch.status.get(vdom="root")
    
    if len(switches) == 0:
        skip_test("No managed switches available for firmware filter test")
    
    first_switch = switches[0]  # type: ignore
    switch_id = getattr(first_switch, 'switch_id', None)
    
    if not switch_id:
        skip_test("Switch does not have ID")
    
    # Get firmware recommendations for specific switch
    result = fgt.api.monitor.switch_controller.fsw_firmware.get(
        vdom="root",
        mkey=switch_id
    )
    
    assert result is not None
    assert result.http_status_code == 200
    print(f"✓ Got firmware recommendations for FortiSwitch: {switch_id}")
    
    # Check if we got data for the specific switch
    if hasattr(result, '__iter__') and hasattr(result, 'keys'):
        result_dict = dict(result)
        if switch_id in result_dict:
            print(f"  Firmware data available for requested switch")
        else:
            print(f"  Firmware data keys: {list(result_dict.keys())}")


def test_get_switch_controller_fsw_firmware_with_timeout():
    """Test: Get firmware recommendations with custom timeout parameter"""
    
    # Test with 5 second timeout
    result = fgt.api.monitor.switch_controller.fsw_firmware.get(
        vdom="root",
        timeout=5
    )
    
    assert result is not None
    assert result.http_status_code == 200
    print(f"✓ Retrieved firmware recommendations with 5s timeout")


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
    test_get_switch_controller_fsw_firmware()
    print("✓ test_get_switch_controller_fsw_firmware passed")
    test_get_switch_controller_fsw_firmware_verify_structure()
    print("✓ test_get_switch_controller_fsw_firmware_verify_structure passed")
    test_get_switch_controller_fsw_firmware_with_filter()
    print("✓ test_get_switch_controller_fsw_firmware_with_filter passed")
    test_get_switch_controller_fsw_firmware_with_timeout()
    print("✓ test_get_switch_controller_fsw_firmware_with_timeout passed")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
