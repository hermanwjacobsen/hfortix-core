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



def test_get_switch_controller_managed_switch_models():
    """Test GET /monitor/switch-controller/managed-switch/models - Retrieve FortiSwitch models for pre-provisioning."""

    result = fgt.api.monitor.switch_controller.managed_switch.models.get(vdom="root")
    assert result is not None
    assert result.http_status_code == 200
    print(f"✓ Retrieved {len(result)} FortiSwitch model(s) supported for pre-provisioning")


def test_get_switch_controller_managed_switch_models_verify_structure():
    """Test: Verify FortiSwitch models response structure"""
    
    result = fgt.api.monitor.switch_controller.managed_switch.models.get(vdom="root")
    assert result is not None
    
    if len(result) > 0:
        print(f"✓ Total FortiSwitch models available: {len(result)}")
        
        # Show first few models
        for idx, model in enumerate(result[:5]):  # type: ignore
            name = getattr(model, 'name', None)
            full_name = getattr(model, 'full_name', None) or getattr(model, 'full-name', None)
            
            print(f"  Model {idx+1}: {name} - {full_name}")
    else:
        print("✓ No FortiSwitch models available (unexpected)")


def test_get_switch_controller_managed_switch_models_search_current_model():
    """Test: Search for the currently connected FortiSwitch model in the list"""
    
    # Get current switches
    switches = fgt.api.monitor.switch_controller.managed_switch.status.get(vdom="root")
    
    if len(switches) == 0:
        skip_test("No managed switches connected to search for model")
    
    # Get first switch
    first_switch = switches[0]  # type: ignore
    
    # Try to extract model from switch data
    # The model might be in various fields
    switch_model = None
    if hasattr(first_switch, 'model'):
        switch_model = first_switch.model
    elif hasattr(first_switch, 'switch_id') or hasattr(first_switch, 'switch-id'):
        switch_id = getattr(first_switch, 'switch_id', None) or getattr(first_switch, 'switch-id', None)
        # Model might be in first 6 chars of switch ID
        if switch_id:
            switch_model = switch_id[:6] if len(switch_id) >= 6 else switch_id
    
    if not switch_model:
        print("⚠ Could not determine current switch model")
        return
    
    # Get all models
    models = fgt.api.monitor.switch_controller.managed_switch.models.get(vdom="root")
    
    # Search for matching model
    found = False
    for model in models:  # type: ignore
        name = getattr(model, 'name', None)
        if name and switch_model.startswith(name):
            full_name = getattr(model, 'full_name', None) or getattr(model, 'full-name', None)
            print(f"✓ Found current switch model in list: {name} - {full_name}")
            found = True
            break
    
    if not found:
        print(f"⚠ Current switch model '{switch_model}' not found in models list (might be already provisioned)")


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
    test_get_switch_controller_managed_switch_models()
    print("✓ test_get_switch_controller_managed_switch_models passed")
    test_get_switch_controller_managed_switch_models_verify_structure()
    print("✓ test_get_switch_controller_managed_switch_models_verify_structure passed")
    test_get_switch_controller_managed_switch_models_search_current_model()
    print("✓ test_get_switch_controller_managed_switch_models_search_current_model passed")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
