"""
Tests for router/static6 endpoint - IPv6 static routing tables
This endpoint configures IPv6 static routes.

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

# NOTE: Router static6 endpoint structure:
# - GET /router/static6 - Get all static routes
# - GET /router/static6/{seq-num} - Get specific static route
# - POST /router/static6 - Create new static route
# - PUT /router/static6/{seq-num} - Update static route
# - DELETE /router/static6/{seq-num} - Delete static route

def cleanup():
    """Cleanup all test static routes."""
    routes = fgt.api.cmdb.router.static6.get()
    for route in routes:
        # Only delete routes with seq-num >= 100 (test routes)
        if route.seq_num >= 100:
            fgt.api.cmdb.router.static6.delete(seq_num=route.seq_num)


def test_get_router_static6():
    """Test: Get all static routes"""
    result = fgt.api.cmdb.router.static6.get()
    assert result is not None
    assert result.http_status_code == 200


def test_post_router_static6_basic():
    """Test: Create basic static route"""
    result = fgt.api.cmdb.router.static6.post(
        seq_num=100,
        dst="2001:db8:1::/64",
        gateway="fd12:3456:789a:bcde::254",
        device="port3",
        comment="Test static route"
    )
    assert result is not None
    assert result.http_status == "success"


def test_get_router_static6_specific():
    """Test: Get specific static route"""
    result = fgt.api.cmdb.router.static6.get(seq_num=100)
    assert result is not None
    assert result.http_status_code == 200
    assert result.seq_num == 100


def test_post_router_static6_with_distance():
    """Test: Create static route with custom distance"""
    result = fgt.api.cmdb.router.static6.post(
        seq_num=101,
        dst="2001:db8:2::/64",
        gateway="fd12:3456:789a:bcde::254",
        device="port3",
        distance=10,
        comment="Route with distance 10"
    )
    assert result is not None
    assert result.http_status == "success"


def test_post_router_static6_with_weight():
    """Test: Create static route with weight"""
    result = fgt.api.cmdb.router.static6.post(
        seq_num=102,
        dst="2001:db8:3::/64",
        gateway="fd12:3456:789a:bcde::254",
        device="port3",
        weight=50,
        comment="Route with weight 50"
    )
    assert result is not None
    assert result.http_status == "success"


def test_post_router_static6_with_priority():
    """Test: Create static route with priority"""
    result = fgt.api.cmdb.router.static6.post(
        seq_num=103,
        dst="2001:db8:4::/64",
        gateway="fd12:3456:789a:bcde::254",
        device="port3",
        priority=100,
        comment="Route with priority 100"
    )
    assert result is not None
    assert result.http_status == "success"


def test_post_router_static6_blackhole():
    """Test: Create blackhole route"""
    result = fgt.api.cmdb.router.static6.post(
        seq_num=104,
        dst="2001:db8:5::/64",
        blackhole="enable",
        comment="Blackhole route"
    )
    assert result is not None
    assert result.http_status == "success"


def test_post_router_static6_disabled():
    """Test: Create disabled static route"""
    result = fgt.api.cmdb.router.static6.post(
        seq_num=105,
        status="disable",
        dst="2001:db8:6::/64",
        gateway="fd12:3456:789a:bcde::254",
        device="port3",
        comment="Disabled route"
    )
    assert result is not None
    assert result.http_status == "success"


def test_post_router_static6_with_tag():
    """Test: Create static route with tag"""
    result = fgt.api.cmdb.router.static6.post(
        seq_num=106,
        dst="2001:db8:7::/64",
        gateway="fd12:3456:789a:bcde::254",
        device="port3",
        tag=100,
        comment="Route with tag 100"
    )
    assert result is not None
    assert result.http_status == "success"


def test_post_router_static6_with_bfd():
    """Test: Create static route with BFD enabled"""
    result = fgt.api.cmdb.router.static6.post(
        seq_num=107,
        dst="2001:db8:8::/64",
        gateway="fd12:3456:789a:bcde::254",
        device="port3",
        bfd="enable",
        comment="Route with BFD"
    )
    assert result is not None
    assert result.http_status == "success"


def test_post_router_static6_link_local_gateway():
    """Test: Create static route with link-local gateway"""
    result = fgt.api.cmdb.router.static6.post(
        seq_num=108,
        dst="2001:db8:9::/64",
        gateway="fe80::1",
        device="port3",
        comment="Route with link-local gateway"
    )
    assert result is not None
    assert result.http_status == "success"


def test_post_router_static6_multiple_routes():
    """Test: Create multiple static routes"""
    result = fgt.api.cmdb.router.static6.post(
        seq_num=109,
        dst="2001:db8:10::/64",
        gateway="fd12:3456:789a:bcde::254",
        device="port3",
        distance=5,
        weight=100,
        priority=50,
        comment="Multi-parameter route"
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_router_static6():
    """Test: Update static route"""
    result = fgt.api.cmdb.router.static6.put(
        seq_num=100,
        dst="2001:db8:1::/64",
        gateway="fd12:3456:789a:bcde::254",
        device="port3",
        distance=15,
        comment="Updated test static route"
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_router_static6_change_gateway():
    """Test: Update static route gateway"""
    result = fgt.api.cmdb.router.static6.put(
        seq_num=101,
        dst="2001:db8:2::/64",
        gateway="fd12:3456:789a:bcde::253",
        device="port3",
        distance=10,
        comment="Route with updated gateway"
    )
    assert result is not None
    assert result.http_status == "success"


def test_delete_router_static6():
    """Test: Delete specific static route"""
    result = fgt.api.cmdb.router.static6.delete(seq_num=102)
    assert result is not None
    assert result.http_status == "success"


def test_get_router_static6_verify():
    """Test: Verify static routes exist"""
    result = fgt.api.cmdb.router.static6.get()
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

    test_get_router_static6()
    print("✓ test_get_router_static6 passed")
    
    test_post_router_static6_basic()
    print("✓ test_post_router_static6_basic passed")
    
    test_get_router_static6_specific()
    print("✓ test_get_router_static6_specific passed")
    
    test_post_router_static6_with_distance()
    print("✓ test_post_router_static6_with_distance passed")
    
    test_post_router_static6_with_weight()
    print("✓ test_post_router_static6_with_weight passed")
    
    test_post_router_static6_with_priority()
    print("✓ test_post_router_static6_with_priority passed")
    
    test_post_router_static6_blackhole()
    print("✓ test_post_router_static6_blackhole passed")
    
    test_post_router_static6_disabled()
    print("✓ test_post_router_static6_disabled passed")
    
    test_post_router_static6_with_tag()
    print("✓ test_post_router_static6_with_tag passed")
    
    test_post_router_static6_with_bfd()
    print("✓ test_post_router_static6_with_bfd passed")
    
    test_post_router_static6_link_local_gateway()
    print("✓ test_post_router_static6_link_local_gateway passed")
    
    test_post_router_static6_multiple_routes()
    print("✓ test_post_router_static6_multiple_routes passed")
    
    test_put_router_static6()
    print("✓ test_put_router_static6 passed")
    
    test_put_router_static6_change_gateway()
    print("✓ test_put_router_static6_change_gateway passed")
    
    test_delete_router_static6()
    print("✓ test_delete_router_static6 passed")
    
    test_get_router_static6_verify()
    print("✓ test_get_router_static6_verify passed")

    cleanup()
    print("✓ All router/static6 tests passed")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
