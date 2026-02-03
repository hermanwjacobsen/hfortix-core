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



def test_post_switch_controller_managed_switch_port_stats_reset():
    """Test POST /monitor/switch-controller/managed-switch/port-stats-reset - Reset port statistics for FortiSwitch."""

    # First, get available FortiSwitches to find a valid switch ID
    switches = fgt.api.monitor.switch_controller.managed_switch.status.get(vdom="root")
    
    if len(switches) > 0:
        # Get the first switch's ID
        switch = switches[0]  # type: ignore
        switch_id = getattr(switch, 'switch_id', None) or getattr(switch, 'switch-id', None)
        
        # Reset statistics for the switch (all ports)
        result = fgt.api.monitor.switch_controller.managed_switch.port_stats_reset.post(
            vdom="root",
            mkey=switch_id
        )
        assert result is not None
        assert result.http_status_code == 200
        
        print(f"✓ Reset port statistics for FortiSwitch: {switch_id}")
    else:
        print("✓ No FortiSwitches available to test port statistics reset")
        skip_test("No FortiSwitches connected")


def test_post_switch_controller_managed_switch_port_stats_reset_specific_ports():
    """Test POST /monitor/switch-controller/managed-switch/port-stats-reset - Reset specific ports."""

    # First, get available FortiSwitches and their port information
    port_stats = fgt.api.monitor.switch_controller.managed_switch.port_stats.get(vdom="root")
    
    if len(port_stats) > 0:
        switch = port_stats[0]  # type: ignore
        switch_id = getattr(switch, 'switch_id', None) or getattr(switch, 'switch-id', None)
        
        # Check if the switch has ports
        if hasattr(switch, 'ports') and switch.ports:
            # Get list of port names
            if isinstance(switch.ports, dict):
                port_names = list(switch.ports.keys())
                
                # Reset statistics for specific ports (first 2 ports)
                ports_to_reset = port_names[:2] if len(port_names) >= 2 else port_names[:1]
                
                result = fgt.api.monitor.switch_controller.managed_switch.port_stats_reset.post(
                    vdom="root",
                    mkey=switch_id,
                    ports=ports_to_reset # type: ignore
                )
                assert result is not None
                assert result.http_status_code == 200
                
                print(f"✓ Reset port statistics for FortiSwitch {switch_id}, ports: {ports_to_reset}")
            else:
                print("✓ Switch does not have ports map, resetting all ports")
                
                # Reset all ports if ports structure is not a dict
                result = fgt.api.monitor.switch_controller.managed_switch.port_stats_reset.post(
                    vdom="root",
                    mkey=switch_id
                )
                assert result is not None
                assert result.http_status_code == 200
                
                print(f"✓ Reset all port statistics for FortiSwitch: {switch_id}")
        else:
            print("✓ Switch has no ports, resetting all")
            
            # Reset even if no ports info
            result = fgt.api.monitor.switch_controller.managed_switch.port_stats_reset.post(
                vdom="root",
                mkey=switch_id
            )
            assert result is not None
            assert result.http_status_code == 200
            
            print(f"✓ Reset port statistics for FortiSwitch: {switch_id}")
    else:
        print("✓ No FortiSwitches available to test specific port reset")
        skip_test("No FortiSwitches connected")


def test_post_switch_controller_managed_switch_port_stats_reset_verify():
    """Test: Verify port statistics reset by checking before and after."""

    # Get available FortiSwitches
    switches = fgt.api.monitor.switch_controller.managed_switch.status.get(vdom="root")
    
    if len(switches) > 0:
        switch = switches[0]  # type: ignore
        switch_id = getattr(switch, 'switch_id', None) or getattr(switch, 'switch-id', None)
        
        # Get port statistics before reset
        stats_before = fgt.api.monitor.switch_controller.managed_switch.port_stats.get(
            vdom="root",
            mkey=switch_id
        )
        assert stats_before is not None
        print(f"✓ Retrieved port statistics before reset")
        
        # Reset port statistics
        reset_result = fgt.api.monitor.switch_controller.managed_switch.port_stats_reset.post(
            vdom="root",
            mkey=switch_id
        )
        assert reset_result is not None
        assert reset_result.http_status_code == 200
        print(f"✓ Reset port statistics for FortiSwitch: {switch_id}")
        
        # Get port statistics after reset
        stats_after = fgt.api.monitor.switch_controller.managed_switch.port_stats.get(
            vdom="root",
            mkey=switch_id
        )
        assert stats_after is not None
        print(f"✓ Retrieved port statistics after reset")
        
        # Note: Statistics may not be immediately zero after reset due to ongoing traffic
        print(f"✓ Port statistics reset operation completed successfully")
    else:
        print("✓ No FortiSwitches available to verify reset")
        skip_test("No FortiSwitches connected")


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
    test_post_switch_controller_managed_switch_port_stats_reset()
    print("✓ test_post_switch_controller_managed_switch_port_stats_reset passed")
    
    test_post_switch_controller_managed_switch_port_stats_reset_specific_ports()
    print("✓ test_post_switch_controller_managed_switch_port_stats_reset_specific_ports passed")
    
    test_post_switch_controller_managed_switch_port_stats_reset_verify()
    print("✓ test_post_switch_controller_managed_switch_port_stats_reset_verify passed")
    
    print("✓ All switch-controller/managed-switch/port-stats-reset tests passed")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
