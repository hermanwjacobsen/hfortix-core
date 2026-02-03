import argparse
import sys
from pathlib import Path
import pytest

pytestmark = pytest.mark.xdist_group(Path(__file__).stem)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt

# NOTE: This endpoint is GET-only because creating packet sniffers may require
# specific licensing, hardware capabilities, or system configuration settings.
# The firewall/sniffer endpoint allows configuration of network traffic capture
# but creation fails with "Input not as expected" errors in test environments,
# suggesting it may require NPU offload capabilities or specific feature licenses.


def test_get_sniffer():
    """Test GET all packet sniffers."""
    result = fgt.api.cmdb.firewall.sniffer.get()
    print(result.raw)
    assert result is not None
    assert result.http_status_code == 200

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
    test_get_sniffer()
    print("✓ test_get_sniffer passed")
    print("\n✓ All tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
