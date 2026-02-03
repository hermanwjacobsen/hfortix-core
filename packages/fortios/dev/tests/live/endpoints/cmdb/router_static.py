"""
Tests for router/static endpoint - IPv4 static routing tables
This endpoint configures IPv4 static routes.

Key features tested:
- GET all static routes
- POST to create static routes with various configurations
- GET specific static route
- PUT to update static routes
- DELETE static routes
- Route parameters: dst, gateway, device, distance, weight, priority
- Special features: blackhole routes, dynamic-gateway, BFD
"""

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

# NOTE: Router static endpoint structure:
# - GET /router/static - Get all static routes
# - GET /router/static/{seq-num} - Get specific static route
# - POST /router/static - Create new static route
# - PUT /router/static/{seq-num} - Update static route
# - DELETE /router/static/{seq-num} - Delete static route

def cleanup():
    """Cleanup all test static routes."""
    routes = fgt.api.cmdb.router.static.get()
    for route in routes:
        # Only delete routes with seq-num >= 100 (test routes)
        if route.seq_num >= 100:
            fgt.api.cmdb.router.static.delete(seq_num=route.seq_num)


def test_get_router_static():
    """Test: Get all static routes"""
    result = fgt.api.cmdb.router.static.get()
    assert result is not None
    assert result.http_status_code == 200


def test_post_router_static_basic():
    """Test: Create basic static route"""
    result = fgt.api.cmdb.router.static.post(
        seq_num=100,
        dst="10.10.10.0/24",
        gateway="192.168.1.254",
        device="port3",
        comment="Test static route"
    )
    assert result is not None
    assert result.http_status == "success"


def test_get_router_static_specific():
    """Test: Get specific static route"""
    result = fgt.api.cmdb.router.static.get(seq_num=100)
    assert result is not None
    assert result.http_status_code == 200
    assert result.seq_num == 100
    assert result.dst == "10.10.10.0 255.255.255.0"  # API returns with space-separated mask


def test_post_router_static_with_distance():
    """Test: Create static route with custom distance"""
    result = fgt.api.cmdb.router.static.post(
        seq_num=101,
        dst="10.20.0.0/16",
        gateway="192.168.1.254",
        device="port3",
        distance=10,
        comment="Route with distance 10"
    )
    assert result is not None
    assert result.http_status == "success"


def test_post_router_static_with_weight():
    """Test: Create static route with weight"""
    result = fgt.api.cmdb.router.static.post(
        seq_num=102,
        dst="10.30.0.0/16",
        gateway="192.168.1.254",
        device="port3",
        weight=50,
        comment="Route with weight 50"
    )
    assert result is not None
    assert result.http_status == "success"


def test_post_router_static_with_priority():
    """Test: Create static route with priority"""
    result = fgt.api.cmdb.router.static.post(
        seq_num=103,
        dst="10.40.0.0/16",
        gateway="192.168.1.254",
        device="port3",
        priority=100,
        comment="Route with priority 100"
    )
    assert result is not None
    assert result.http_status == "success"


def test_post_router_static_blackhole():
    """Test: Create blackhole route"""
    result = fgt.api.cmdb.router.static.post(
        seq_num=104,
        dst="10.50.0.0/16",
        blackhole="enable",
        comment="Blackhole route"
    )
    assert result is not None
    assert result.http_status == "success"


def test_post_router_static_with_src():
    """Test: Create static route with source prefix"""
    result = fgt.api.cmdb.router.static.post(
        seq_num=105,
        dst="10.60.0.0/16",
        src="192.168.1.0/24",
        gateway="192.168.1.254",
        device="port3",
        comment="Route with source prefix"
    )
    assert result is not None
    assert result.http_status == "success"


def test_post_router_static_disabled():
    """Test: Create disabled static route"""
    result = fgt.api.cmdb.router.static.post(
        seq_num=106,
        status="disable",
        dst="10.70.0.0/16",
        gateway="192.168.1.254",
        device="port3",
        comment="Disabled route"
    )
    assert result is not None
    assert result.http_status == "success"


def test_post_router_static_with_tag():
    """Test: Create static route with tag"""
    result = fgt.api.cmdb.router.static.post(
        seq_num=107,
        dst="10.80.0.0/16",
        gateway="192.168.1.254",
        device="port3",
        tag=100,
        comment="Route with tag 100"
    )
    assert result is not None
    assert result.http_status == "success"


def test_post_router_static_with_bfd():
    """Test: Create static route with BFD enabled"""
    result = fgt.api.cmdb.router.static.post(
        seq_num=108,
        dst="10.90.0.0/16",
        gateway="192.168.1.254",
        device="port3",
        bfd="enable",
        comment="Route with BFD"
    )
    assert result is not None
    assert result.http_status == "success"


def test_post_router_static_multiple_routes():
    """Test: Create multiple static routes"""
    result = fgt.api.cmdb.router.static.post(
        seq_num=109,
        dst="10.100.0.0/16",
        gateway="192.168.1.254",
        device="port3",
        distance=5,
        weight=100,
        priority=50,
        comment="Multi-parameter route"
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_router_static():
    """Test: Update static route"""
    result = fgt.api.cmdb.router.static.put(
        seq_num=100,
        dst="10.10.10.0/24",
        gateway="192.168.1.254",
        device="port3",
        distance=15,
        comment="Updated test static route"
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_router_static_change_gateway():
    """Test: Update static route gateway"""
    result = fgt.api.cmdb.router.static.put(
        seq_num=101,
        dst="10.20.0.0/16",
        gateway="192.168.1.253",
        device="port3",
        distance=10,
        comment="Route with updated gateway"
    )
    assert result is not None
    assert result.http_status == "success"


def test_delete_router_static():
    """Test: Delete specific static route"""
    result = fgt.api.cmdb.router.static.delete(seq_num=102)
    assert result is not None
    assert result.http_status == "success"


def test_get_router_static_verify():
    """Test: Verify static routes exist"""
    result = fgt.api.cmdb.router.static.get()
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

    test_get_router_static()
    print("✓ test_get_router_static passed")
    
    test_post_router_static_basic()
    print("✓ test_post_router_static_basic passed")
    
    test_get_router_static_specific()
    print("✓ test_get_router_static_specific passed")
    
    test_post_router_static_with_distance()
    print("✓ test_post_router_static_with_distance passed")
    
    test_post_router_static_with_weight()
    print("✓ test_post_router_static_with_weight passed")
    
    test_post_router_static_with_priority()
    print("✓ test_post_router_static_with_priority passed")
    
    test_post_router_static_blackhole()
    print("✓ test_post_router_static_blackhole passed")
    
    test_post_router_static_with_src()
    print("✓ test_post_router_static_with_src passed")
    
    test_post_router_static_disabled()
    print("✓ test_post_router_static_disabled passed")
    
    test_post_router_static_with_tag()
    print("✓ test_post_router_static_with_tag passed")
    
    test_post_router_static_with_bfd()
    print("✓ test_post_router_static_with_bfd passed")
    
    test_post_router_static_multiple_routes()
    print("✓ test_post_router_static_multiple_routes passed")
    
    test_put_router_static()
    print("✓ test_put_router_static passed")
    
    test_put_router_static_change_gateway()
    print("✓ test_put_router_static_change_gateway passed")
    
    test_delete_router_static()
    print("✓ test_delete_router_static passed")
    
    test_get_router_static_verify()
    print("✓ test_get_router_static_verify passed")

    cleanup()
    print("✓ All router/static tests passed")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
