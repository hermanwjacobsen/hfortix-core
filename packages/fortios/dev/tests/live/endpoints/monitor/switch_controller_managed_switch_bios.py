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


def test_get_switch_controller_managed_switch_bios():
    """Test GET /monitor/switch-controller/managed-switch/bios - Get BIOS info for managed FortiSwitches."""

    result = fgt.api.monitor.switch_controller.managed_switch.bios.get(vdom="root")
    assert result is not None
    assert result.http_status_code == 200
    print(f"✓ Retrieved BIOS information for {len(result)} managed switch(es)")


def test_get_switch_controller_managed_switch_bios_verify_structure():
    """Test: Verify BIOS information structure if switches exist"""
    
    result = fgt.api.monitor.switch_controller.managed_switch.bios.get(vdom="root")
    assert result is not None
    
    # If FortiSwitches exist, verify their structure
    if len(result) > 0:
        switch = result[0]  # type: ignore
        
        # Verify expected fields exist
        switch_id = getattr(switch, 'switch_id', None) or getattr(switch, 'switch-id', None)
        
        print(f"✓ First switch ID: {switch_id}")
        
        # Check for BIOS details
        if hasattr(switch, 'bios'):
            bios = switch.bios
            print(f"✓ BIOS data available")
            
            # Check for BIOS fields
            if hasattr(bios, 'BIOS_version'):
                print(f"  BIOS Version: {bios.BIOS_version}")
            
            if hasattr(bios, 'version'):
                print(f"  Firmware Version: {bios.version}")
            
            if hasattr(bios, 'serial_number'):
                print(f"  Serial Number: {bios.serial_number}")
            
            if hasattr(bios, 'burn_in_mac'):
                print(f"  MAC Address: {bios.burn_in_mac}")
            
            if hasattr(bios, 'hostname'):
                print(f"  Hostname: {bios.hostname}")
            
            if hasattr(bios, 'distribution'):
                print(f"  Distribution: {bios.distribution}")
            
            if hasattr(bios, 'branch_point'):
                print(f"  Branch Point: {bios.branch_point}")
            
            if hasattr(bios, 'system_time'):
                print(f"  System Time: {bios.system_time}")
            
            if hasattr(bios, 'system_part_number'):
                print(f"  System Part Number: {bios.system_part_number}")
        else:
            print("⚠ No BIOS data available for this switch")
    else:
        print("✓ No FortiSwitches connected (BIOS information unavailable)")


def test_get_switch_controller_managed_switch_bios_with_filter():
    """Test: Get BIOS information for specific FortiSwitch using mkey filter"""
    
    # First get all switches to see if any exist
    all_switches = fgt.api.monitor.switch_controller.managed_switch.bios.get(vdom="root")
    
    if len(all_switches) == 0:
        skip_test("No managed switches to filter")
    
    # Get switch ID from first switch
    first_switch = all_switches[0]  # type: ignore
    switch_id = getattr(first_switch, 'switch_id', None) or getattr(first_switch, 'switch-id', None)
    
    if not switch_id:
        skip_test("Switch does not have ID")
    
    # Get BIOS info for specific switch
    result = fgt.api.monitor.switch_controller.managed_switch.bios.get(
        vdom="root",
        mkey=switch_id
    )
    
    assert result is not None
    assert result.http_status_code == 200
    
    # Verify we got the right switch
    if len(result) > 0:
        returned_switch = result[0]  # type: ignore
        returned_id = getattr(returned_switch, 'switch_id', None) or getattr(returned_switch, 'switch-id', None)
        assert returned_id == switch_id, f"Expected switch_id {switch_id}, got {returned_id}"
        print(f"✓ Got BIOS info for FortiSwitch ID: {switch_id}")


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
    test_get_switch_controller_managed_switch_bios()
    print("✓ test_get_switch_controller_managed_switch_bios passed")
    test_get_switch_controller_managed_switch_bios_verify_structure()
    print("✓ test_get_switch_controller_managed_switch_bios_verify_structure passed")
    test_get_switch_controller_managed_switch_bios_with_filter()
    print("✓ test_get_switch_controller_managed_switch_bios_with_filter passed")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
