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



def test_get_switch_controller_managed_switch_dhcp_snooping():
    """Test GET /monitor/switch-controller/managed-switch/dhcp-snooping - Retrieve DHCP servers monitored by FortiSwitches."""

    result = fgt.api.monitor.switch_controller.managed_switch.dhcp_snooping.get(vdom="root")
    assert result is not None
    assert result.http_status_code == 200
    
    print(f"✓ Retrieved DHCP snooping data for {len(result)} FortiSwitch(es)")


def test_get_switch_controller_managed_switch_dhcp_snooping_verify_structure():
    """Test: Verify DHCP snooping data structure."""

    result = fgt.api.monitor.switch_controller.managed_switch.dhcp_snooping.get(vdom="root")
    assert result is not None
    assert result.http_status_code == 200
    
    if len(result) > 0:
        # Check first entry
        entry = result[0]  # type: ignore
        
        # Verify required fields
        assert hasattr(entry, 'switch_id') or hasattr(entry, 'switch-id'), "Entry should have switch_id field"
        
        switch_id = getattr(entry, 'switch_id', None) or getattr(entry, 'switch-id', None)
        print(f"✓ DHCP snooping data for switch: {switch_id}")
        
        # Check for snooping_entries
        if hasattr(entry, 'snooping_entries') or hasattr(entry, 'snooping-entries'):
            snooping_entries = getattr(entry, 'snooping_entries', None) or getattr(entry, 'snooping-entries', None)
            
            if snooping_entries and len(snooping_entries) > 0:
                print(f"  ✓ Found {len(snooping_entries)} DHCP server(s) detected")
                
                # Show first DHCP server info
                first_server = snooping_entries[0]
                server_dict = first_server.to_dict() if hasattr(first_server, 'to_dict') else {}
                print(f"  First DHCP server keys: {list(server_dict.keys())[:5]}")
            else:
                print(f"  No DHCP servers detected by this switch")
        else:
            print(f"  No snooping_entries field found")
    else:
        print("✓ No DHCP snooping data available (no FortiSwitches or no DHCP servers detected)")


def test_get_switch_controller_managed_switch_dhcp_snooping_list_all():
    """Test: List all detected DHCP servers across all switches."""
    result = fgt.api.monitor.switch_controller.managed_switch.dhcp_snooping.get(vdom="root")
    assert result is not None
    
    total_dhcp_servers = 0
    switches_with_dhcp = 0
    
    for entry in result:  
        switch_id = getattr(entry, 'switch_id', None) or getattr(entry, 'switch-id', None)
        snooping_entries = getattr(entry, 'snooping_entries', None) or getattr(entry, 'snooping-entries', None)
        
        if snooping_entries and len(snooping_entries) > 0:
            switches_with_dhcp += 1
            total_dhcp_servers += len(snooping_entries)
            print(f"  Switch {switch_id}: {len(snooping_entries)} DHCP server(s)")
    
    print(f"✓ Summary: {switches_with_dhcp} switch(es) detected DHCP servers")
    print(f"  Total DHCP servers detected: {total_dhcp_servers}")


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
    test_get_switch_controller_managed_switch_dhcp_snooping()
    print("✓ test_get_switch_controller_managed_switch_dhcp_snooping passed")
    
    test_get_switch_controller_managed_switch_dhcp_snooping_verify_structure()
    print("✓ test_get_switch_controller_managed_switch_dhcp_snooping_verify_structure passed")
    
    test_get_switch_controller_managed_switch_dhcp_snooping_list_all()
    print("✓ test_get_switch_controller_managed_switch_dhcp_snooping_list_all passed")
    
    print("✓ All switch-controller/managed-switch/dhcp-snooping tests passed")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
