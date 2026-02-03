import argparse
import sys
from pathlib import Path

import pytest

# Run tests on a single worker to preserve state (group by filename)
pytestmark = pytest.mark.xdist_group(Path(__file__).stem)

# Add pytest directory to path (go up from endpoints/cmdb/ to pytest/)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt


TEST_NAME = "test_per_ip_shaper1"


def cleanup():
    """Clean up test per-IP shapers."""
    try:
        shapers = fgt.api.cmdb.firewall.shaper.per_ip_shaper.get()
        for shaper in shapers:
            if shaper.name and str(shaper.name).startswith("test_"):
                try:
                    fgt.api.cmdb.firewall.shaper.per_ip_shaper.delete(name=shaper.name)
                except Exception:
                    pass
    except Exception:
        pass


def test_get_per_ip_shapers():
    """Test: Get all per-IP shapers."""
    result = fgt.api.cmdb.firewall.shaper.per_ip_shaper.get()
    assert result is not None
    assert result.http_status_code == 200


def test_post_per_ip_shaper():
    """Test: Create per-IP shaper with 10 Mbps bandwidth."""
    result = fgt.api.cmdb.firewall.shaper.per_ip_shaper.post(
        name=TEST_NAME,
        bandwidth_unit="kbps",
        max_bandwidth=10000,  # 10 Mbps in kbps
        max_concurrent_session=100,
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_per_ip_shaper():
    """Test: Update per-IP shaper - increase bandwidth to 20 Mbps."""
    result = fgt.api.cmdb.firewall.shaper.per_ip_shaper.put(
        name=TEST_NAME,
        max_bandwidth=20000,  # 20 Mbps in kbps
        max_concurrent_session=200,
    )
    assert result is not None
    assert result.http_status == "success"
    
    # Verify the update
    verify = fgt.api.cmdb.firewall.shaper.per_ip_shaper.get(name=TEST_NAME)
    assert verify is not None
    assert verify.max_bandwidth == 20000
    assert verify.max_concurrent_session == 200


def test_get_specific_per_ip_shaper():
    """Test: Get specific per-IP shaper."""
    result = fgt.api.cmdb.firewall.shaper.per_ip_shaper.get(name=TEST_NAME)
    assert result is not None
    assert result.name == TEST_NAME


def test_delete_per_ip_shaper():
    """Test: Delete per-IP shaper."""
    result = fgt.api.cmdb.firewall.shaper.per_ip_shaper.delete(name=TEST_NAME)
    assert result is not None
    assert result.http_status == "success"
    
    # Verify deletion
    shapers = fgt.api.cmdb.firewall.shaper.per_ip_shaper.get()
    shaper_names = [s.name for s in shapers]
    assert TEST_NAME not in shaper_names, "Per-IP shaper should have been deleted"


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
        
    test_get_per_ip_shapers()
    print("✓ test_get_per_ip_shapers passed")

    test_post_per_ip_shaper()
    print("✓ test_post_per_ip_shaper passed")

    test_put_per_ip_shaper()
    print("✓ test_put_per_ip_shaper passed")

    test_get_specific_per_ip_shaper()
    print("✓ test_get_specific_per_ip_shaper passed")

    test_delete_per_ip_shaper()
    print("✓ test_delete_per_ip_shaper passed")

    cleanup()
    print("✓ post-Cleanup passed")
    
    print("\n✓ All tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
