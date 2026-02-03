import argparse
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(project_root))
from fgtclient import fgt

import pytest

# Run tests on a single worker to preserve state (group by filename)
pytestmark = pytest.mark.xdist_group(Path(__file__).stem)

# NOTE: RIPng endpoint structure:
# - GET /router/ripng - Get RIPng configuration
# - PUT /router/ripng - Update RIPng configuration
# - No POST/DELETE (singleton resource)

def cleanup():
    """Cleanup RIPng configuration after tests."""
    fgt.api.cmdb.router.ripng.put(
        default_information_originate="disable",
        default_metric=1,
        network=[],
        interface=[],
        neighbor=[],
        passive_interface=[],
        redistribute=[],
        distribute_list=[],
        distance=[],
        offset_list=[],
        aggregate_address=[]
    )

def test_get_router_ripng():
    """Test: Get RIPng configuration"""
    result = fgt.api.cmdb.router.ripng.get()
    assert result is not None
    assert result.http_status_code == 200


def test_put_router_ripng_basic():
    """Test: Configure basic RIPng settings"""
    result = fgt.api.cmdb.router.ripng.put(
        default_information_originate="enable",
        default_metric=5
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_router_ripng_timers():
    """Test: Configure RIPng timers"""
    result = fgt.api.cmdb.router.ripng.put(
        update_timer=30,
        timeout_timer=180,
        garbage_timer=120
    )
    assert result is not None
    assert result.http_status == "success"



def test_put_router_ripng_network():
    """Test: Configure RIPng network"""
    result = fgt.api.cmdb.router.ripng.put(
        network=[
            {
                "id": 1,
                "prefix": "fe80::1/128" # Needs link local ipv6 address format
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_router_ripng_multiple_networks():
    """Test: Configure multiple RIPng networks"""
    result = fgt.api.cmdb.router.ripng.put(
        network=[
            {
                "id": 1,
                "prefix": "fe80::1/128" # Needs link local ipv6 address format
            },
            {
                "id": 2,
                "prefix": "fe80::2/128" # Needs link local ipv6 address format
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_router_ripng_interface():
    """Test: Configure RIPng interface"""
    result = fgt.api.cmdb.router.ripng.put(
        interface=[
            {
                "name": "port3",
                "split_horizon_status": "enable"
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_router_ripng_passive_interface():
    """Test: Configure RIPng passive interface"""
    result = fgt.api.cmdb.router.ripng.put(
        passive_interface=[
            {
                "name": "port3"
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_router_ripng_neighbor():
    """Test: Configure RIPng neighbor"""
    result = fgt.api.cmdb.router.ripng.put(
        neighbor=[
            {
                "id": 1,
                "ip6": "fd12:3456:789a:bcde::ffff",
                "interface": "port3"
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_router_ripng_redistribute():
    """Test: Configure RIPng route redistribution"""
    result = fgt.api.cmdb.router.ripng.put(
        redistribute=[
            {
                "name": "connected",
                "status": "enable",
                "metric": 10
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_router_ripng_distance():
    """Test: Configure RIPng administrative distance"""
    result = fgt.api.cmdb.router.ripng.put(
        distance=[
            {
                "id": 1,
                "prefix6": "fd00::/8",
                "distance": 100
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_router_ripng_aggregate_address():
    """Test: Configure RIPng aggregate address"""
    result = fgt.api.cmdb.router.ripng.put(
        aggregate_address=[
            {
                "id": 1,
                "prefix6": "fd00::/8"
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_router_ripng_max_out_metric():
    """Test: Configure RIPng maximum output metric"""
    result = fgt.api.cmdb.router.ripng.put(
        max_out_metric=15
    )
    assert result is not None
    assert result.http_status == "success"


def test_get_router_ripng_verify():
    """Test: Verify RIPng configuration"""
    result = fgt.api.cmdb.router.ripng.get()
    assert result is not None
    assert result.http_status_code == 200


def test_zz_cleanup_after():
    """Test: Cleanup after all tests"""
    cleanup()


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

    test_get_router_ripng()
    print("✓ test_get_router_ripng passed")
    
    test_put_router_ripng_basic()
    print("✓ test_put_router_ripng_basic passed")
    
    test_put_router_ripng_timers()
    print("✓ test_put_router_ripng_timers passed")
    
    test_put_router_ripng_network()
    print("✓ test_put_router_ripng_network passed")
    
    test_put_router_ripng_multiple_networks()
    print("✓ test_put_router_ripng_multiple_networks passed")
    
    test_put_router_ripng_interface()
    print("✓ test_put_router_ripng_interface passed")
    
    test_put_router_ripng_passive_interface()
    print("✓ test_put_router_ripng_passive_interface passed")
    
    test_put_router_ripng_neighbor()
    print("✓ test_put_router_ripng_neighbor passed")
    
    test_put_router_ripng_redistribute()
    print("✓ test_put_router_ripng_redistribute passed")
    
    test_put_router_ripng_distance()
    print("✓ test_put_router_ripng_distance passed")
    
    test_put_router_ripng_aggregate_address()
    print("✓ test_put_router_ripng_aggregate_address passed")
    
    # NOTE: offset-list requires access-list6 to be configured first, skipping
    # test_put_router_ripng_offset_list()
    # print("✓ test_put_router_ripng_offset_list passed")
    
    test_put_router_ripng_max_out_metric()
    print("✓ test_put_router_ripng_max_out_metric passed")
    
    test_get_router_ripng_verify()
    print("✓ test_get_router_ripng_verify passed")

    cleanup()
    print("✓ All router/ripng tests passed")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
