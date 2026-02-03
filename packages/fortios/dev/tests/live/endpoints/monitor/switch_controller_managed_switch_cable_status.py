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



def test_get_switch_controller_managed_switch_cable_status():
    """Test GET /monitor/switch-controller/managed-switch/cable-status - Diagnose cable information for a port."""

    # First get a managed switch to test with
    switches = fgt.api.monitor.switch_controller.managed_switch.status.get(vdom="root")
    
    if len(switches) == 0:
        skip_test("No managed switches available for cable status test")
    
    # Get first switch and a port to test
    first_switch = switches[0]  # type: ignore
    switch_id = getattr(first_switch, 'switch_id', None)
    
    if not switch_id:
        skip_test("Switch does not have ID")
    
    # Get a port name - try to use a down port to be safe
    test_port = None
    if hasattr(first_switch, 'ports') and first_switch.ports:
        for port in first_switch.ports:
            port_name = getattr(port, 'interface', None) or getattr(port, 'name', None)
            port_status = getattr(port, 'status', 'unknown')
            if port_name and port_status == 'down':
                test_port = port_name
                break
        
        # If no down port, use first port
        if not test_port and first_switch.ports:
            port = first_switch.ports[0]
            test_port = getattr(port, 'interface', None) or getattr(port, 'name', None)
    
    if not test_port:
        skip_test("Could not find a port to test")
    
    # Test cable status for the port
    result = fgt.api.monitor.switch_controller.managed_switch.cable_status.get(
        vdom="root",
        mkey=switch_id,
        port=test_port
    )
    
    assert result is not None
    assert result.http_status_code == 200
    print(f"✓ Retrieved cable status for switch {switch_id}, port {test_port}")


def test_get_switch_controller_managed_switch_cable_status_structure():
    """Test: Verify cable status response structure"""
    
    # Get a switch and port to test
    switches = fgt.api.monitor.switch_controller.managed_switch.status.get(vdom="root")
    
    if len(switches) == 0:
        skip_test("No managed switches available")
    
    first_switch = switches[0]  # type: ignore
    switch_id = getattr(first_switch, 'switch_id', None)
    
    # Get first available port
    test_port = None
    if hasattr(first_switch, 'ports') and first_switch.ports:
        port = first_switch.ports[0]
        test_port = getattr(port, 'interface', None) or getattr(port, 'name', None)
    
    if not test_port:
        skip_test("Could not find a port to test")
    
    result = fgt.api.monitor.switch_controller.managed_switch.cable_status.get(
        vdom="root",
        mkey=switch_id, # type: ignore
        port=test_port
    )
    
    assert result is not None
    print(f"✓ Cable status response type: {type(result)}")
    
    # Check for expected fields
    if hasattr(result, 'type'):
        print(f"  Connection Type: {getattr(result, 'type')}")
    
    if hasattr(result, 'port'):
        print(f"  Port Name: {getattr(result, 'port')}")
    
    if hasattr(result, 'error_range'):
        print(f"  Margin of Error: {getattr(result, 'error_range')}")
    
    if hasattr(result, 'unit'):
        print(f"  Unit of Measurement: {getattr(result, 'unit')}")
    
    pairs = getattr(result, 'pairs', None)
    if pairs:
        print(f"  Twisted Pairs: {len(pairs)}")
        # Show first pair details
        if len(pairs) > 0:
            pair = pairs[0]
            if hasattr(pair, 'name'):
                print(f"    First pair name: {getattr(pair, 'name')}")
            if hasattr(pair, 'state'):
                print(f"    First pair state: {getattr(pair, 'state')}")
            if hasattr(pair, 'length'):
                print(f"    First pair length: {getattr(pair, 'length')}")


def test_get_switch_controller_managed_switch_cable_status_multiple_ports():
    """Test: Get cable status for multiple ports"""
    
    switches = fgt.api.monitor.switch_controller.managed_switch.status.get(vdom="root")
    
    if len(switches) == 0:
        skip_test("No managed switches available")
    
    first_switch = switches[0]  # type: ignore
    switch_id = getattr(first_switch, 'switch_id', None)
    
    if not hasattr(first_switch, 'ports') or not first_switch.ports or len(first_switch.ports) < 2:
        skip_test("Not enough ports to test")
    
    # Test cable status for first 2 ports
    ports_tested = 0
    for port in first_switch.ports[:2]:
        port_name = getattr(port, 'interface', None) or getattr(port, 'name', None)
        if port_name:
            result = fgt.api.monitor.switch_controller.managed_switch.cable_status.get(
                vdom="root",
                mkey=switch_id, # type: ignore
                port=port_name
            )
            assert result is not None
            assert result.http_status_code == 200
            ports_tested += 1
            print(f"✓ Cable status for port {port_name}: OK")
    
    assert ports_tested >= 1, "Should have tested at least one port"


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
    test_get_switch_controller_managed_switch_cable_status()
    print("✓ test_get_switch_controller_managed_switch_cable_status passed")
    test_get_switch_controller_managed_switch_cable_status_structure()
    print("✓ test_get_switch_controller_managed_switch_cable_status_structure passed")
    test_get_switch_controller_managed_switch_cable_status_multiple_ports()
    print("✓ test_get_switch_controller_managed_switch_cable_status_multiple_ports passed")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
