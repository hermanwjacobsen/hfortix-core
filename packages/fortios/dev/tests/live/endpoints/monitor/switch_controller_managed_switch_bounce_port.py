import argparse
import sys
from pathlib import Path
import pytest
import time

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


        return



def test_post_switch_controller_managed_switch_port_bounce():
    """Test POST /monitor/switch-controller/managed-switch/port-bounce - Bounce a FortiSwitch port."""

    # First, get available FortiSwitches and their port status
    switches = fgt.api.monitor.switch_controller.managed_switch.status.get(vdom="root")
    
    if len(switches) > 0:
        switch = switches[0]  # type: ignore
        switch_id = getattr(switch, 'switch_id', None) or getattr(switch, 'switch-id', None)
        
        target_port = None
        
        # Look for a port that is down (safe to bounce)
        if hasattr(switch, 'ports') and len(switch.ports) > 0:
            for port in switch.ports:
                status = getattr(port, 'status', '').lower()
                port_dict = port.to_dict()
                
                # Look for ports that are down
                if status == 'down' or 'down' in status:
                    # Get port name from interface field
                    port_name = port_dict.get('interface', port_dict.get('name', port_dict.get('port-name')))
                    
                    if port_name:
                        target_port = port_name
                        print(f"✓ Found down port: {port_name} (status: {status})")
                        break
        
        # If we found a down port, bounce it
        if target_port:
            result = fgt.api.monitor.switch_controller.managed_switch.bounce_port.post(
                vdom="root",
                mkey=switch_id,
                port=target_port,
                duration=1  # 1 second bounce duration
            )
            assert result is not None
            assert result.http_status_code == 200
            
            print(f"✓ Bounced port on FortiSwitch {switch_id}, port {target_port} (1 second)")
        else:
            print("✓ No down ports found - skipping port bounce to avoid disrupting active connections")
            print(f"  (All ports on switch {switch_id} appear to be active)")
    else:
        print("✓ No FortiSwitches available to test port bounce")
        skip_test("No FortiSwitches connected")


def test_post_switch_controller_managed_switch_port_bounce_with_duration():
    """Test: Bounce a port with different durations (1-5 seconds)."""

    # Get available FortiSwitches
    switches = fgt.api.monitor.switch_controller.managed_switch.status.get(vdom="root")
    
    if len(switches) > 0:
        switch = switches[0]  # type: ignore
        switch_id = getattr(switch, 'switch_id', None) or getattr(switch, 'switch-id', None)
        
        # Find a down port
        target_port = None
        if hasattr(switch, 'ports') and len(switch.ports) > 0:
            for port in switch.ports:
                status = getattr(port, 'status', '').lower()
                if status == 'down' or 'down' in status:
                    port_dict = port.to_dict()
                    port_name = port_dict.get('interface')
                    if port_name:
                        target_port = port_name
                        break
        
        if target_port:
            # Test with 2 second duration
            result = fgt.api.monitor.switch_controller.managed_switch.bounce_port.post(
                vdom="root",
                mkey=switch_id,
                port=target_port,
                duration=2
            )
            assert result is not None
            assert result.http_status_code == 200
            
            print(f"✓ Bounced port {target_port} with 2 second duration")
            
            # Wait for bounce to complete
            time.sleep(2.5)
            
            # Test with default duration (should be 1 second if not specified)
            result = fgt.api.monitor.switch_controller.managed_switch.bounce_port.post(
                vdom="root",
                mkey=switch_id,
                port=target_port
            )
            assert result is not None
            assert result.http_status_code == 200
            
            print(f"✓ Bounced port {target_port} with default duration")
        else:
            print("✓ No down ports found - skipping duration test")
    else:
        print("✓ No FortiSwitches available")
        skip_test("No FortiSwitches connected")


def test_post_switch_controller_managed_switch_port_bounce_stop():
    """Test: Start and stop a port bounce operation."""

    # Get available FortiSwitches
    switches = fgt.api.monitor.switch_controller.managed_switch.status.get(vdom="root")
    
    if len(switches) > 0:
        switch = switches[0]  # type: ignore
        switch_id = getattr(switch, 'switch_id', None) or getattr(switch, 'switch-id', None)
        
        # Find a down port
        target_port = None
        if hasattr(switch, 'ports') and len(switch.ports) > 0:
            for port in switch.ports:
                status = getattr(port, 'status', '').lower()
                if status == 'down' or 'down' in status:
                    port_dict = port.to_dict()
                    port_name = port_dict.get('interface')
                    if port_name:
                        target_port = port_name
                        break
        
        if target_port:
            # Start a bounce with 5 second duration
            result = fgt.api.monitor.switch_controller.managed_switch.bounce_port.post(
                vdom="root",
                mkey=switch_id,
                port=target_port,
                duration=5
            )
            assert result is not None
            assert result.http_status_code == 200
            
            print(f"✓ Started 5-second bounce on port {target_port}")
            
            # Wait a moment
            time.sleep(1)
            
            # Stop the bounce
            result = fgt.api.monitor.switch_controller.managed_switch.bounce_port.post(
                vdom="root",
                mkey=switch_id,
                port=target_port,
                stop=True
            )
            assert result is not None
            assert result.http_status_code == 200
            
            print(f"✓ Stopped bounce on port {target_port}")
        else:
            print("✓ No down ports found - skipping stop test")
    else:
        print("✓ No FortiSwitches available")
        skip_test("No FortiSwitches connected")


def test_post_switch_controller_managed_switch_port_bounce_safe_ports():
    """Test: List safe (down) ports for bouncing."""

    # Get available FortiSwitches
    switches = fgt.api.monitor.switch_controller.managed_switch.status.get(vdom="root")
    
    if len(switches) > 0:
        switch = switches[0]  # type: ignore
        switch_id = getattr(switch, 'switch_id', None) or getattr(switch, 'switch-id', None)
        
        print(f"✓ FortiSwitch: {switch_id}")
        
        down_ports = []
        active_ports = []
        
        if hasattr(switch, 'ports') and len(switch.ports) > 0:
            for port in switch.ports:
                port_dict = port.to_dict()
                status = getattr(port, 'status', 'unknown').lower()
                port_name = port_dict.get('interface', 'unknown')
                
                if status == 'down' or 'down' in status:
                    down_ports.append(port_name)
                else:
                    active_ports.append(port_name)
            
            print(f"✓ Safe ports (down): {len(down_ports)}")
            if down_ports:
                print(f"  Ports: {', '.join(down_ports[:10])}")  # Show first 10
            
            print(f"✓ Risky ports (active): {len(active_ports)}")
            if active_ports:
                print(f"  Ports: {', '.join(active_ports[:10])}")  # Show first 10
            
            # Bounce a safe port
            if down_ports:
                test_port = down_ports[0]
                result = fgt.api.monitor.switch_controller.managed_switch.bounce_port.post(
                    vdom="root",
                    mkey=switch_id,
                    port=test_port,
                    duration=1
                )
                assert result is not None
                assert result.http_status_code == 200
                
                print(f"✓ Successfully bounced safe down port: {test_port}")
                print(f"  (Active ports were not touched: {len(active_ports)} ports safe)")
            else:
                print("✓ No down ports available - all ports are active")
                print(f"  Skipping port bounce to avoid disrupting {len(active_ports)} active connections")
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
    test_post_switch_controller_managed_switch_port_bounce()
    print("✓ test_post_switch_controller_managed_switch_port_bounce passed")
    
    test_post_switch_controller_managed_switch_port_bounce_with_duration()
    print("✓ test_post_switch_controller_managed_switch_port_bounce_with_duration passed")
    
    test_post_switch_controller_managed_switch_port_bounce_stop()
    print("✓ test_post_switch_controller_managed_switch_port_bounce_stop passed")
    
    test_post_switch_controller_managed_switch_port_bounce_safe_ports()
    print("✓ test_post_switch_controller_managed_switch_port_bounce_safe_ports passed")
    
    print("✓ All switch-controller/managed-switch/port-bounce tests passed")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
