import argparse
import sys
from pathlib import Path

import pytest

# Run tests on a single worker to preserve state (group by filename)
pytestmark = pytest.mark.xdist_group(Path(__file__).stem)

# Add pytest directory to path (go up from endpoints/cmdb/ to pytest/)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt


# NOTE: IPS decoder endpoint is READ-ONLY
# Cannot POST, PUT, or DELETE decoders - they are built-in system objects


def test_get_ips_decoders():
    """Test: Get all IPS decoders (read-only endpoint)."""
    result = fgt.api.cmdb.ips.decoder.get()
    assert result is not None
    assert result.http_status_code == 200
    assert len(result) > 0, "Should have built-in decoders"


def test_get_specific_ips_decoder():
    """Test: Get specific IPS decoder by name."""
    # Test with a known built-in decoder
    result = fgt.api.cmdb.ips.decoder.get(name="DoS")
    assert result is not None
    assert result.name == "DoS"


def test_ips_decoder_has_parameters():
    """Test: Verify decoder has parameter information."""
    # Get a decoder and check it has parameters
    result = fgt.api.cmdb.ips.decoder.get(name="VoIP")
    assert result is not None
    assert hasattr(result, "parameter")


def test_list_common_decoders():
    """Test: Verify common built-in decoders exist."""
    result = fgt.api.cmdb.ips.decoder.get()
    decoder_names = [d.name for d in result]
    
    # Check for some common decoders
    common_decoders = ["DoS", "VoIP", "SCADA", "IoT"]
    for decoder in common_decoders:
        assert decoder in decoder_names, f"Expected {decoder} decoder to exist"


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
    test_get_ips_decoders()
    print("✓ test_get_ips_decoders passed")

    test_get_specific_ips_decoder()
    print("✓ test_get_specific_ips_decoder passed")

    test_ips_decoder_has_parameters()
    print("✓ test_ips_decoder_has_parameters passed")

    test_list_common_decoders()
    print("✓ test_list_common_decoders passed")
    
    print("\n✓ All IPS decoder tests passed (read-only endpoint)!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
