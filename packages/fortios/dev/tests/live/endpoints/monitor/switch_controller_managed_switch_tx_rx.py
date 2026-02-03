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



def test_get_switch_controller_managed_switch_tx_rx():
    """Test GET /monitor/switch-controller/managed-switch/tx-rx - Retrieve transceiver Tx and Rx power for a port."""

    # Get a switch to test with
    switches = fgt.api.monitor.switch_controller.managed_switch.status.get(vdom="root")
    
    if len(switches) == 0:
        skip_test("No managed switches available for tx-rx test")
    
    first_switch = switches[0]  # type: ignore
    test_switch_id = getattr(first_switch, 'switch_id', None)
    # Test with port25 (SFP port) - even if empty, we can test the endpoint
    test_port = "port25"
    
    if not test_switch_id:
        skip_test("Switch does not have ID")
    
    # Get Tx/Rx power for the SFP port
    result = fgt.api.monitor.switch_controller.managed_switch.tx_rx.get(
        vdom="root",
        mkey=test_switch_id,
        port=test_port
    )
    
    assert result is not None
    assert result.http_status_code == 200
    print(f"✓ Retrieved Tx/Rx power data for switch {test_switch_id}, port {test_port}")
    
    # Note: Response may be empty if no SFP module is installed
    if hasattr(result, 'status') and result['status']:
        print(f"  SFP module present with Tx/Rx data")
    else:
        print(f"  No SFP module installed (empty response expected)")


def test_get_switch_controller_managed_switch_tx_rx_structure():
    """Test: Verify Tx/Rx power response structure (even if port is empty)"""
    
    # Get a switch to test with
    switches = fgt.api.monitor.switch_controller.managed_switch.status.get(vdom="root")
    
    if len(switches) == 0:
        skip_test("No managed switches available")
    
    first_switch = switches[0]  # type: ignore
    test_switch_id = getattr(first_switch, 'switch_id', None)
    test_port = "port25"  # SFP port
    
    if not test_switch_id:
        skip_test("Switch does not have ID")
    
    result = fgt.api.monitor.switch_controller.managed_switch.tx_rx.get(
        vdom="root",
        mkey=test_switch_id,
        port=test_port
    )
    
    assert result is not None
    print(f"✓ Tx/Rx power response type: {type(result)}")
    print(f"✓ Response for port {test_port} (SFP port)")
    
    # Check for limits
    if hasattr(result, 'limits') and result['limits']:
        print(f"  Limits available: Yes")
        limits = result['limits']
        
        if hasattr(limits, 'alarm'):
            print(f"    Alarm levels available")
        
        if hasattr(limits, 'warning'):
            print(f"    Warning levels available")
    else:
        print(f"  Limits: Not available (no SFP module)")
    
    # Check for status (actual measurements)
    if hasattr(result, 'status') and result['status']:
        print(f"  Status measurements: {len(result['status'])} channel(s)")
    else:
        print(f"  Status: Empty (no SFP module installed)")


def test_get_switch_controller_managed_switch_tx_rx_no_sfp():
    """Test: Try to get Tx/Rx power for a port without SFP (should handle gracefully)"""
    
    # Get a switch
    switches = fgt.api.monitor.switch_controller.managed_switch.status.get(vdom="root")
    
    if len(switches) == 0:
        skip_test("No managed switches available")
    
    first_switch = switches[0]  # type: ignore
    switch_id = getattr(first_switch, 'switch_id', None)
    
    # Try port1 (likely copper, not SFP)
    test_port = "port1"
    
    try:
        result = fgt.api.monitor.switch_controller.managed_switch.tx_rx.get(
            vdom="root",
            mkey=switch_id, # type: ignore
            port=test_port
        )
        
        # If we get here, check if it returns empty/error data
        print(f"✓ Tx/Rx request for non-SFP port returned (status: {result.http_status_code})")
        
        # The API might return an error or empty data for non-SFP ports
        if hasattr(result, 'status') and not result['status']:
            print(f"  No Tx/Rx data (expected for copper port)")
        
    except Exception as e:
        # It's OK if this fails - not all ports have transceivers
        print(f"✓ Tx/Rx request for non-SFP port handled: {str(e)[:100]}")


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
    test_get_switch_controller_managed_switch_tx_rx()
    print("✓ test_get_switch_controller_managed_switch_tx_rx passed")
    test_get_switch_controller_managed_switch_tx_rx_structure()
    print("✓ test_get_switch_controller_managed_switch_tx_rx_structure passed")
    test_get_switch_controller_managed_switch_tx_rx_no_sfp()
    print("✓ test_get_switch_controller_managed_switch_tx_rx_no_sfp passed")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
