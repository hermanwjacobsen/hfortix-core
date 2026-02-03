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



def test_post_switch_controller_managed_switch_poe_reset():
    """Test POST /monitor/switch-controller/managed-switch/poe-reset - Reset PoE on a FortiSwitch port."""

    # First, get available FortiSwitches and their port status
    switches = fgt.api.monitor.switch_controller.managed_switch.status.get(vdom="root")
    
    if len(switches) > 0:
        switch = switches[0]  # type: ignore
        switch_id = getattr(switch, 'switch_id', None) or getattr(switch, 'switch-id', None)
        
        target_port = None
        
        # Look for a port that is down AND PoE capable (safe to reset PoE)
        if hasattr(switch, 'ports') and len(switch.ports) > 0:
            for port in switch.ports:
                status = getattr(port, 'status', '').lower()
                port_dict = port.to_dict()
                poe_capable = port_dict.get('poe_capable', False)
                
                # Look for ports that are down AND PoE capable
                if (status == 'down' or 'down' in status) and poe_capable:
                    # Get port name from interface field
                    port_name = port_dict.get('interface', port_dict.get('name', port_dict.get('port-name')))
                    
                    if port_name:
                        target_port = port_name
                        print(f"✓ Found down PoE-capable port: {port_name} (status: {status}, PoE: {poe_capable})")
                        break
        
        # If we found a down PoE-capable port, reset PoE on it
        if target_port:
            result = fgt.api.monitor.switch_controller.managed_switch.poe_reset.post(
                vdom="root",
                mkey=switch_id,
                port=target_port
            )
            assert result is not None
            assert result.http_status_code == 200
            
            print(f"✓ Reset PoE on FortiSwitch {switch_id}, port {target_port}")
        else:
            print("✓ No down PoE-capable ports found - skipping PoE reset to avoid disrupting active connections")
            print(f"  (All PoE-capable ports on switch {switch_id} appear to be active)")
    else:
        print("✓ No FortiSwitches available to test PoE reset")
        skip_test("No FortiSwitches connected")


def test_post_switch_controller_managed_switch_poe_reset_verify_safe():
    """Test: Verify PoE reset only targets safe (down + PoE-capable) ports."""

    # Get available FortiSwitches
    switches = fgt.api.monitor.switch_controller.managed_switch.status.get(vdom="root")
    
    if len(switches) > 0:
        switch = switches[0]  # type: ignore
        switch_id = getattr(switch, 'switch_id', None) or getattr(switch, 'switch-id', None)
        
        down_poe_ports = []
        active_poe_ports = []
        down_no_poe = []
        
        if hasattr(switch, 'ports') and len(switch.ports) > 0:
            for port in switch.ports:
                port_dict = port.to_dict()
                status = getattr(port, 'status', '').lower()
                poe_capable = port_dict.get('poe_capable', False)
                port_name = port_dict.get('interface', 'unknown')
                
                if poe_capable:
                    if 'down' in status or status == 'down':
                        down_poe_ports.append(port_name)
                    else:
                        active_poe_ports.append(port_name)
                elif 'down' in status or status == 'down':
                    down_no_poe.append(port_name)
            
            print(f"✓ Port analysis:")
            print(f"  Down + PoE-capable (safe): {len(down_poe_ports)}")
            print(f"  Active + PoE-capable (risky): {len(active_poe_ports)}")
            print(f"  Down but no PoE: {len(down_no_poe)}")
            
            # Only reset PoE on down PoE-capable ports
            if down_poe_ports:
                # Reset PoE on the first down PoE-capable port
                target_port = down_poe_ports[0]
                
                result = fgt.api.monitor.switch_controller.managed_switch.poe_reset.post(
                    vdom="root",
                    mkey=switch_id,
                    port=target_port
                )
                assert result is not None
                assert result.http_status_code == 200
                
                print(f"✓ Safely reset PoE on down PoE-capable port: {target_port}")
                print(f"  (Active PoE ports were not touched: {len(active_poe_ports)} ports safe)")
            else:
                print("✓ No down PoE-capable ports found - all PoE ports are active")
                print(f"  Skipping PoE reset to avoid disrupting {len(active_poe_ports)} active PoE connections")
        else:
            print("✓ No port information available")
    else:
        print("✓ No FortiSwitches available")
        skip_test("No FortiSwitches connected")


def test_post_switch_controller_managed_switch_poe_reset_get_available_ports():
    """Test: List available ports and identify safe PoE-capable ports for PoE reset."""

    # Get available FortiSwitches
    switches = fgt.api.monitor.switch_controller.managed_switch.status.get(vdom="root")
    
    if len(switches) > 0:
        switch = switches[0]  # type: ignore
        switch_id = getattr(switch, 'switch_id', None) or getattr(switch, 'switch-id', None)
        
        print(f"✓ FortiSwitch: {switch_id}")
        
        if hasattr(switch, 'ports') and len(switch.ports) > 0:
            print(f"✓ Total ports: {len(switch.ports)}")
            
            # Categorize ports
            safe_poe_ports = []
            risky_poe_ports = []
            no_poe_ports = []
            
            for port in switch.ports:
                port_dict = port.to_dict()
                status = getattr(port, 'status', 'unknown').lower()
                poe_capable = port_dict.get('poe_capable', False)
                port_name = port_dict.get('interface', 'unknown')
                
                # Determine if port is safe to reset
                is_down = 'down' in status or status == 'down'
                
                if poe_capable:
                    if is_down:
                        safe_poe_ports.append(port_name)
                    else:
                        risky_poe_ports.append(port_name)
                else:
                    no_poe_ports.append(port_name)
            
            print(f"✓ Safe PoE ports (down + PoE-capable): {len(safe_poe_ports)}")
            if safe_poe_ports:
                print(f"  Ports: {', '.join(safe_poe_ports[:5])}")  # Show first 5
            
            print(f"✓ Risky PoE ports (active + PoE-capable): {len(risky_poe_ports)}")
            if risky_poe_ports:
                print(f"  Ports: {', '.join(risky_poe_ports[:5])}")  # Show first 5
            
            print(f"✓ Non-PoE ports: {len(no_poe_ports)}")
            
            # Test PoE reset only on safe PoE-capable ports
            if safe_poe_ports:
                test_port = safe_poe_ports[0]
                result = fgt.api.monitor.switch_controller.managed_switch.poe_reset.post(
                    vdom="root",
                    mkey=switch_id,
                    port=test_port
                )
                assert result is not None
                assert result.http_status_code == 200
                
                print(f"✓ Successfully reset PoE on safe port: {test_port}")
            else:
                print("✓ No safe (down + PoE-capable) ports available - skipping actual PoE reset")
        else:
            print("✓ No port details available")
    else:
        print("✓ No FortiSwitches available")
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
    test_post_switch_controller_managed_switch_poe_reset()
    print("✓ test_post_switch_controller_managed_switch_poe_reset passed")
    
    test_post_switch_controller_managed_switch_poe_reset_verify_safe()
    print("✓ test_post_switch_controller_managed_switch_poe_reset_verify_safe passed")
    
    test_post_switch_controller_managed_switch_poe_reset_get_available_ports()
    print("✓ test_post_switch_controller_managed_switch_poe_reset_get_available_ports passed")
    
    print("✓ All switch-controller/managed-switch/poe-reset tests passed")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
