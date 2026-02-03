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



def test_get_switch_controller_managed_switch_transceivers():
    """Test GET /monitor/switch-controller/managed-switch/transceivers - Get transceiver modules on FortiSwitches."""

    result = fgt.api.monitor.switch_controller.managed_switch.transceivers.get(vdom="root")
    assert result is not None
    assert result.http_status_code == 200
    
    print(f"✓ Retrieved {len(result)} transceiver module(s)")


def test_get_switch_controller_managed_switch_transceivers_verify_structure():
    """Test: Verify transceiver data structure."""

    result = fgt.api.monitor.switch_controller.managed_switch.transceivers.get(vdom="root")
    assert result is not None
    assert result.http_status_code == 200
    
    if len(result) > 0:
        # Check first transceiver
        transceiver = result[0]  # type: ignore
        
        # Verify required fields
        assert hasattr(transceiver, 'fortiswitch_id') or hasattr(transceiver, 'fortiswitch-id'), "Should have fortiswitch_id"
        assert hasattr(transceiver, 'port'), "Should have port field"
        assert hasattr(transceiver, 'status'), "Should have status field"
        
        fortiswitch_id = getattr(transceiver, 'fortiswitch_id', None) or getattr(transceiver, 'fortiswitch-id', None)
        port = transceiver.port
        status = transceiver.status
        
        print(f"✓ First transceiver:")
        print(f"  FortiSwitch: {fortiswitch_id}")
        print(f"  Port: {port}")
        print(f"  Status: {status}")
        
        # Optional fields
        transceiver_dict = transceiver.to_dict() if hasattr(transceiver, 'to_dict') else {}
        
        if 'type' in transceiver_dict:
            print(f"  Type: {transceiver_dict['type']}")
        if 'vendor' in transceiver_dict:
            print(f"  Vendor: {transceiver_dict['vendor']}")
        if 'vendor_part_number' in transceiver_dict or 'vendor-part-number' in transceiver_dict:
            part_num = transceiver_dict.get('vendor_part_number') or transceiver_dict.get('vendor-part-number')
            print(f"  Part Number: {part_num}")
        if 'vendor_serial_number' in transceiver_dict or 'vendor-serial-number' in transceiver_dict:
            serial_num = transceiver_dict.get('vendor_serial_number') or transceiver_dict.get('vendor-serial-number')
            print(f"  Serial Number: {serial_num}")
    else:
        print("✓ No transceiver modules found (no modules connected to FortiSwitches)")


def test_get_switch_controller_managed_switch_transceivers_by_switch():
    """Test: Group transceivers by FortiSwitch."""

    result = fgt.api.monitor.switch_controller.managed_switch.transceivers.get(vdom="root")
    assert result is not None
    
    # Group transceivers by switch
    transceivers_by_switch = {}
    
    for transceiver in result:
        fortiswitch_id = getattr(transceiver, 'fortiswitch_id', None) or getattr(transceiver, 'fortiswitch-id', None)
        
        if fortiswitch_id not in transceivers_by_switch:
            transceivers_by_switch[fortiswitch_id] = []
        
        transceivers_by_switch[fortiswitch_id].append(transceiver)
    
    print(f"✓ Found transceivers on {len(transceivers_by_switch)} FortiSwitch(es)")
    
    for switch_id, transceivers in transceivers_by_switch.items():
        ports = [t.port for t in transceivers]
        print(f"  Switch {switch_id}: {len(transceivers)} transceiver(s) on ports {', '.join(ports)}")


def test_get_switch_controller_managed_switch_transceivers_by_status():
    """Test: Categorize transceivers by link status."""

    result = fgt.api.monitor.switch_controller.managed_switch.transceivers.get(vdom="root")
    assert result is not None
    
    # Categorize by status
    by_status = {}
    
    for transceiver in result:
        status = transceiver['status'] if 'status' in transceiver else 'unknown'
        
        if status not in by_status:
            by_status[status] = []
        
        by_status[status].append(transceiver)
    
    print(f"✓ Transceiver status breakdown:")
    
    for status, transceivers in by_status.items():
        print(f"  {status}: {len(transceivers)} transceiver(s)")


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
    test_get_switch_controller_managed_switch_transceivers()
    print("✓ test_get_switch_controller_managed_switch_transceivers passed")
    
    test_get_switch_controller_managed_switch_transceivers_verify_structure()
    print("✓ test_get_switch_controller_managed_switch_transceivers_verify_structure passed")
    
    test_get_switch_controller_managed_switch_transceivers_by_switch()
    print("✓ test_get_switch_controller_managed_switch_transceivers_by_switch passed")
    
    test_get_switch_controller_managed_switch_transceivers_by_status()
    print("✓ test_get_switch_controller_managed_switch_transceivers_by_status passed")
    
    print("✓ All switch-controller/managed-switch/transceivers tests passed")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
