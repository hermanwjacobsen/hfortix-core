import argparse
import sys
from pathlib import Path

import pytest

# Run tests on a single worker to preserve state (group by filename)
pytestmark = pytest.mark.xdist_group(Path(__file__).stem)

# Add pytest directory to path (go up from endpoints/cmdb/ to pytest/)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt


# NOTE: IPS rule endpoint is READ-ONLY - contains built-in FortiGuard IPS signatures
# Cannot POST, PUT, or DELETE - these are managed by FortiGuard updates
# For custom signatures, use ips.custom instead



def test_get_ips_rules():
    """Test: Get all IPS rules (read-only endpoint with FortiGuard signatures)."""
    result = fgt.api.cmdb.ips.rule.get()
    assert result is not None
    assert result.http_status_code == 200
    assert len(result) > 0, "Should have FortiGuard IPS signature rules"




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
    test_get_ips_rules()
    print("✓ test_get_ips_rules passed")
    
    print("\n✓ All IPS rule tests passed (read-only endpoint)!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
