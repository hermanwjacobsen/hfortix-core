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



def test_get_switch_controller_managed_switch_faceplate_xml():
    """Test GET /monitor/switch-controller/managed-switch/faceplate-xml - Retrieve FortiSwitch faceplate XML."""

    # First, get available FortiSwitches to find a valid switch ID
    switches = fgt.api.monitor.switch_controller.managed_switch.status.get(vdom="root")
    
    if len(switches) > 0:
        # Get the first switch's ID
        switch = switches[0]  # type: ignore
        switch_id = getattr(switch, 'switch_id', None) or getattr(switch, 'switch-id', None)
        
        # Get faceplate XML for the switch
        result = fgt.api.monitor.switch_controller.managed_switch.faceplate_xml.get(
            vdom="root",
            mkey=switch_id # type: ignore
        )
        assert result is not None
        assert result.http_status_code == 200
        
        print(f"✓ Retrieved faceplate XML for FortiSwitch: {switch_id}")
        
        # Check if result contains XML-like data
        if hasattr(result, 'to_dict'):
            data = result.to_dict()
            print(f"  Response type: {type(data)}")
            if isinstance(data, dict):
                print(f"  Keys in response: {list(data.keys())[:5]}")
        
    else:
        print("✓ No FortiSwitches available to test faceplate XML retrieval")
        skip_test("No FortiSwitches connected")


def test_get_switch_controller_managed_switch_faceplate_xml_verify_structure():
    """Test: Verify faceplate XML structure and content."""

    # Get available FortiSwitches
    switches = fgt.api.monitor.switch_controller.managed_switch.status.get(vdom="root")
    
    if len(switches) > 0:
        switch = switches[0]  # type: ignore
        switch_id = getattr(switch, 'switch_id', None) or getattr(switch, 'switch-id', None)
        
        # Get faceplate XML
        result = fgt.api.monitor.switch_controller.managed_switch.faceplate_xml.get(
            vdom="root",
            mkey=switch_id # type: ignore
        )
        assert result is not None
        assert result.http_status_code == 200
        
        print(f"✓ Retrieved faceplate XML for switch: {switch_id}")
        
        # Check the dict representation
        if hasattr(result, 'to_dict'):
            data = result.to_dict()
            
            # Should have 'xml' key with XML content
            if 'xml' in data:
                xml_content = data['xml']
                assert isinstance(xml_content, str), "XML content should be a string"
                assert len(xml_content) > 0, "XML content should not be empty"
                
                # Verify it's XML
                assert '<' in xml_content and '>' in xml_content, "Content should be XML format"
                
                print(f"  ✓ XML content length: {len(xml_content)} characters")
                print(f"  ✓ Content is valid XML format")
                
                # Check for expected XML elements
                if '<model' in xml_content:
                    print(f"  ✓ Contains <model> element")
                if '<portgroup' in xml_content:
                    print(f"  ✓ Contains <portgroup> element")
                if '<port' in xml_content:
                    print(f"  ✓ Contains <port> element")
                
                # Show first 150 characters
                print(f"  First 150 chars: {xml_content[:150]}...")
            else:
                print(f"  ⚠ No 'xml' key in response")
                print(f"  Available keys: {list(data.keys())}")
    else:
        print("✓ No FortiSwitches available")
        skip_test("No FortiSwitches connected")


def test_get_switch_controller_managed_switch_faceplate_xml_multiple_switches():
    """Test: Retrieve faceplate XML for multiple switches if available."""

    # Get all available FortiSwitches
    switches = fgt.api.monitor.switch_controller.managed_switch.status.get(vdom="root")
    
    if len(switches) > 0:
        print(f"✓ Found {len(switches)} FortiSwitch(es)")
        
        # Get faceplate XML for each switch (up to 3)
        for i, switch in enumerate(switches[:3]):  # type: ignore
            switch_id = getattr(switch, 'switch_id', None) or getattr(switch, 'switch-id', None)
            
            result = fgt.api.monitor.switch_controller.managed_switch.faceplate_xml.get(
                vdom="root",
                mkey=switch_id # type: ignore   
            )
            assert result is not None
            assert result.http_status_code == 200
            
            print(f"  [{i+1}] Retrieved faceplate XML for switch: {switch_id}")
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
    test_get_switch_controller_managed_switch_faceplate_xml()
    print("✓ test_get_switch_controller_managed_switch_faceplate_xml passed")
    
    test_get_switch_controller_managed_switch_faceplate_xml_verify_structure()
    print("✓ test_get_switch_controller_managed_switch_faceplate_xml_verify_structure passed")
    
    test_get_switch_controller_managed_switch_faceplate_xml_multiple_switches()
    print("✓ test_get_switch_controller_managed_switch_faceplate_xml_multiple_switches passed")
    
    print("✓ All switch-controller/managed-switch/faceplate-xml tests passed")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
