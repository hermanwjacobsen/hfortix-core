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

# NOTE: RIP endpoint structure:
# - GET /router/rip - Get RIP configuration
# - PUT /router/rip - Update RIP configuration
# - No POST/DELETE (singleton resource)

def cleanup():
    """Cleanup RIP configuration after tests."""
    fgt.api.cmdb.router.rip.put(
        default_information_originate="disable",
        default_metric=1,
        network=[],
        interface=[],
        neighbor=[],
        passive_interface=[],
        redistribute=[],
        distribute_list=[],
        distance=[],
        offset_list=[]
    )

def test_get_router_rip():
    """Test: Get RIP configuration"""
    result = fgt.api.cmdb.router.rip.get()
    assert result is not None
    assert result.http_status_code == 200


def test_put_router_rip_basic():
    """Test: Configure basic RIP settings"""
    result = fgt.api.cmdb.router.rip.put(
        default_information_originate="enable",
        default_metric=5,
        version="2"
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_router_rip_timers():
    """Test: Configure RIP timers"""
    result = fgt.api.cmdb.router.rip.put(
        update_timer=30,
        timeout_timer=180,
        garbage_timer=120,
        version="2"
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_router_rip_network():
    """Test: Configure RIP network"""
    result = fgt.api.cmdb.router.rip.put(
        version="2",
        network=[
            {
                "id": 1,
                "prefix": "192.168.1.0/24"
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_router_rip_multiple_networks():
    """Test: Configure multiple RIP networks"""
    result = fgt.api.cmdb.router.rip.put(
        version="2",
        network=[
            {
                "id": 1,
                "prefix": "192.168.1.0/24"
            },
            {
                "id": 2,
                "prefix": "10.0.0.0/8"
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_router_rip_interface():
    """Test: Configure RIP interface"""
    result = fgt.api.cmdb.router.rip.put(
        version="2",
        interface=[
            {
                "name": "port3",
                "auth_mode": "none",
                "send_version": "2",
                "receive_version": "2",
                "split_horizon_status": "enable"
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_router_rip_passive_interface():
    """Test: Configure RIP passive interface"""
    result = fgt.api.cmdb.router.rip.put(
        version="2",
        passive_interface=[
            {
                "name": "port3"
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_router_rip_neighbor():
    """Test: Configure RIP neighbor"""
    result = fgt.api.cmdb.router.rip.put(
        version="2",
        neighbor=[
            {
                "id": 1,
                "ip": "192.168.1.254"
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_router_rip_redistribute():
    """Test: Configure RIP route redistribution"""
    result = fgt.api.cmdb.router.rip.put(
        version="2",
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


def test_put_router_rip_distance():
    """Test: Configure RIP administrative distance"""
    result = fgt.api.cmdb.router.rip.put(
        version="2",
        distance=[
            {
                "id": 1,
                "prefix": "10.0.0.0/8",
                "distance": 100
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_router_rip_max_out_metric():
    """Test: Configure RIP maximum output metric"""
    result = fgt.api.cmdb.router.rip.put(
        version="2",
        max_out_metric=15
    )
    assert result is not None
    assert result.http_status == "success"


def test_get_router_rip_verify():
    """Test: Verify RIP configuration"""
    result = fgt.api.cmdb.router.rip.get()
    assert result is not None
    assert result.http_status_code == 200
    assert hasattr(result, "version")


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

    test_get_router_rip()
    print("✓ test_get_router_rip passed")
    
    test_put_router_rip_basic()
    print("✓ test_put_router_rip_basic passed")
    
    test_put_router_rip_timers()
    print("✓ test_put_router_rip_timers passed")
    
    test_put_router_rip_network()
    print("✓ test_put_router_rip_network passed")
    
    test_put_router_rip_multiple_networks()
    print("✓ test_put_router_rip_multiple_networks passed")
    
    test_put_router_rip_interface()
    print("✓ test_put_router_rip_interface passed")
    
    test_put_router_rip_passive_interface()
    print("✓ test_put_router_rip_passive_interface passed")
    
    test_put_router_rip_neighbor()
    print("✓ test_put_router_rip_neighbor passed")
    
    test_put_router_rip_redistribute()
    print("✓ test_put_router_rip_redistribute passed")
    
    test_put_router_rip_distance()
    print("✓ test_put_router_rip_distance passed")
    
    # NOTE: offset-list requires access-list to be configured first, skipping
    # test_put_router_rip_offset_list()
    # print("✓ test_put_router_rip_offset_list passed")
    
    test_put_router_rip_max_out_metric()
    print("✓ test_put_router_rip_max_out_metric passed")
    
    test_get_router_rip_verify()
    print("✓ test_get_router_rip_verify passed")

    cleanup()
    print("✓ All router/rip tests passed")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
