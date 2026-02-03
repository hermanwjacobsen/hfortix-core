import argparse
import sys
from pathlib import Path

import pytest

# Run tests on a single worker to preserve state (group by filename)
pytestmark = pytest.mark.xdist_group(Path(__file__).stem)

# Add pytest directory to path (go up from endpoints/cmdb/ to pytest/)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt


TEST_NAME = "test_traffic_shaper1"


def cleanup():
    """Clean up test traffic shapers."""
    try:
        shapers = fgt.api.cmdb.firewall.shaper.traffic_shaper.get()
        for shaper in shapers:
            if shaper.name and str(shaper.name).startswith("test_"):
                try:
                    fgt.api.cmdb.firewall.shaper.traffic_shaper.delete(name=shaper.name)
                except Exception:
                    pass
    except Exception:
        pass


def test_get_traffic_shapers():
    """Test: Get all traffic shapers."""
    result = fgt.api.cmdb.firewall.shaper.traffic_shaper.get()
    assert result is not None
    assert result.http_status_code == 200


def test_post_traffic_shaper():
    """Test: Create traffic shaper with guaranteed and max bandwidth."""
    result = fgt.api.cmdb.firewall.shaper.traffic_shaper.post(
        name=TEST_NAME,
        bandwidth_unit="kbps",
        guaranteed_bandwidth=5000,   # 5 Mbps guaranteed
        maximum_bandwidth=10000,     # 10 Mbps max
        priority="medium",
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_traffic_shaper():
    """Test: Update traffic shaper - increase bandwidth and priority."""
    result = fgt.api.cmdb.firewall.shaper.traffic_shaper.put(
        name=TEST_NAME,
        guaranteed_bandwidth=10000,  # 10 Mbps guaranteed
        maximum_bandwidth=20000,     # 20 Mbps max
        priority="high",
    )
    assert result is not None
    assert result.http_status == "success"
    
    # Verify the update
    verify = fgt.api.cmdb.firewall.shaper.traffic_shaper.get(name=TEST_NAME)
    assert verify is not None
    assert verify.guaranteed_bandwidth == 10000
    assert verify.maximum_bandwidth == 20000
    assert verify.priority == "high"


def test_get_specific_traffic_shaper():
    """Test: Get specific traffic shaper."""
    result = fgt.api.cmdb.firewall.shaper.traffic_shaper.get(name=TEST_NAME)
    assert result is not None
    assert result.name == TEST_NAME


def test_delete_traffic_shaper():
    """Test: Delete traffic shaper."""
    result = fgt.api.cmdb.firewall.shaper.traffic_shaper.delete(name=TEST_NAME)
    assert result is not None
    assert result.http_status == "success"
    
    # Verify deletion
    shapers = fgt.api.cmdb.firewall.shaper.traffic_shaper.get()
    shaper_names = [s.name for s in shapers]
    assert TEST_NAME not in shaper_names, "Traffic shaper should have been deleted"


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
    cleanup()
    print("✓ Pre-Cleanup passed")
        
    test_get_traffic_shapers()
    print("✓ test_get_traffic_shapers passed")

    test_post_traffic_shaper()
    print("✓ test_post_traffic_shaper passed")

    test_put_traffic_shaper()
    print("✓ test_put_traffic_shaper passed")

    test_get_specific_traffic_shaper()
    print("✓ test_get_specific_traffic_shaper passed")

    test_delete_traffic_shaper()
    print("✓ test_delete_traffic_shaper passed")

    cleanup()
    print("✓ post-Cleanup passed")
    
    print("\n✓ All tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
