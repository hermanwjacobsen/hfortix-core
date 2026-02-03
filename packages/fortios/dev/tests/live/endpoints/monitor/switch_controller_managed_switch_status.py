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



def test_get_switch_controller_managed_switch_status():
    """Test GET /monitor/switch-controller/managed-switch/status - Retrieve the status of managed switches."""

    result = fgt.api.monitor.switch_controller.managed_switch.status.get(vdom="root")
    assert result is not None
    assert result.http_status_code == 200
    assert isinstance(result, list), "Expected a list of managed switch statuses"
    assert len(result) > 0, "Expected at least one managed switch status entry"
    for switch in result:
        assert hasattr(switch, "switch-id"), "Managed switch entry should have a 'switch-id' attribute"
        assert hasattr(switch, "status"), "Managed switch entry should have a 'status' attribute"



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
    test_get_switch_controller_managed_switch_status()
    print("✓ test_get_switch_controller_managed_switch_status passed")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
