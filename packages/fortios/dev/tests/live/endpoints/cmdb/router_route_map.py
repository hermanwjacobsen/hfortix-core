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

# NOTE: Router route-map endpoint structure:
# - GET /router/route-map - Get all route maps
# - GET /router/route-map/{name} - Get specific route map
# - POST /router/route-map - Create new route map
# - PUT /router/route-map/{name} - Update route map
# - DELETE /router/route-map/{name} - Delete route map

def cleanup():
    """Cleanup all route maps after tests."""
    route_maps = fgt.api.cmdb.router.route_map.get()
    for route_map in route_maps:
        fgt.api.cmdb.router.route_map.delete(name=route_map.name)


def test_00_cleanup_before():
    """Test: Cleanup before starting tests"""
    cleanup()


def test_get_router_route_map():
    """Test: Get all route maps"""
    result = fgt.api.cmdb.router.route_map.get()
    assert result is not None
    assert result.http_status_code == 200


def test_post_router_route_map_basic():
    """Test: Create basic route map"""
    result = fgt.api.cmdb.router.route_map.post(
        name="TEST_ROUTE_MAP_1",
        comments="Basic route map test"
    )
    assert result is not None
    assert result.http_status == "success"


def test_get_router_route_map_specific():
    """Test: Get specific route map"""
    result = fgt.api.cmdb.router.route_map.get(name="TEST_ROUTE_MAP_1")
    assert result is not None
    assert result.http_status_code == 200
    assert result.name == "TEST_ROUTE_MAP_1"


def test_post_router_route_map_permit():
    """Test: Create route map with permit rule"""
    result = fgt.api.cmdb.router.route_map.post(
        name="TEST_ROUTE_MAP_2",
        comments="Permit routes",
        rule=[
            {
                "id": 10,
                "action": "permit"
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"


def test_post_router_route_map_deny():
    """Test: Create route map with deny rule"""
    result = fgt.api.cmdb.router.route_map.post(
        name="TEST_ROUTE_MAP_3",
        comments="Deny routes",
        rule=[
            {
                "id": 10,
                "action": "deny"
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"


def test_post_router_route_map_match_metric():
    """Test: Create route map matching metric"""
    result = fgt.api.cmdb.router.route_map.post(
        name="TEST_ROUTE_MAP_4",
        comments="Match metric",
        rule=[
            {
                "id": 10,
                "action": "permit",
                "match_metric": 100
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"


def test_post_router_route_map_match_tag():
    """Test: Create route map matching tag"""
    result = fgt.api.cmdb.router.route_map.post(
        name="TEST_ROUTE_MAP_5",
        comments="Match tag",
        rule=[
            {
                "id": 10,
                "action": "permit",
                "match_tag": 200
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"


def test_post_router_route_map_set_metric():
    """Test: Create route map setting metric"""
    result = fgt.api.cmdb.router.route_map.post(
        name="TEST_ROUTE_MAP_6",
        comments="Set metric",
        rule=[
            {
                "id": 10,
                "action": "permit",
                "set_metric": 50
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"


def test_post_router_route_map_set_metric_type():
    """Test: Create route map setting metric type"""
    result = fgt.api.cmdb.router.route_map.post(
        name="TEST_ROUTE_MAP_7",
        comments="Set metric type",
        rule=[
            {
                "id": 10,
                "action": "permit",
                "set_metric_type": "external-type1"
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"


def test_post_router_route_map_set_tag():
    """Test: Create route map setting tag"""
    result = fgt.api.cmdb.router.route_map.post(
        name="TEST_ROUTE_MAP_8",
        comments="Set tag",
        rule=[
            {
                "id": 10,
                "action": "permit",
                "set_tag": 300
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"


def test_post_router_route_map_set_local_preference():
    """Test: Create route map setting local preference"""
    result = fgt.api.cmdb.router.route_map.post(
        name="TEST_ROUTE_MAP_9",
        comments="Set local preference",
        rule=[
            {
                "id": 10,
                "action": "permit",
                "set_local_preference": 150
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"


def test_post_router_route_map_set_weight():
    """Test: Create route map setting weight"""
    result = fgt.api.cmdb.router.route_map.post(
        name="TEST_ROUTE_MAP_10",
        comments="Set weight",
        rule=[
            {
                "id": 10,
                "action": "permit",
                "set_weight": 1000
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"


def test_post_router_route_map_match_origin():
    """Test: Create route map matching origin"""
    result = fgt.api.cmdb.router.route_map.post(
        name="TEST_ROUTE_MAP_11",
        comments="Match origin",
        rule=[
            {
                "id": 10,
                "action": "permit",
                "match_origin": "igp"
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"


def test_post_router_route_map_set_origin():
    """Test: Create route map setting origin"""
    result = fgt.api.cmdb.router.route_map.post(
        name="TEST_ROUTE_MAP_12",
        comments="Set origin",
        rule=[
            {
                "id": 10,
                "action": "permit",
                "set_origin": "incomplete"
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"


def test_post_router_route_map_multiple_rules():
    """Test: Create route map with multiple rules"""
    result = fgt.api.cmdb.router.route_map.post(
        name="TEST_ROUTE_MAP_13",
        comments="Multiple rules",
        rule=[
            {
                "id": 10,
                "action": "permit",
                "match_metric": 100,
                "set_metric": 50
            },
            {
                "id": 20,
                "action": "permit",
                "match_tag": 200,
                "set_tag": 300
            },
            {
                "id": 30,
                "action": "deny"
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_router_route_map():
    """Test: Update route map"""
    result = fgt.api.cmdb.router.route_map.put(
        name="TEST_ROUTE_MAP_1",
        comments="Updated basic route map test",
        rule=[
            {
                "id": 10,
                "action": "permit",
                "set_metric": 25
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_router_route_map_add_rules():
    """Test: Add rules to existing route map"""
    result = fgt.api.cmdb.router.route_map.put(
        name="TEST_ROUTE_MAP_2",
        comments="Permit routes - updated",
        rule=[
            {
                "id": 10,
                "action": "permit",
                "set_local_preference": 200
            },
            {
                "id": 20,
                "action": "permit",
                "set_weight": 500
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"


def test_delete_router_route_map():
    """Test: Delete specific route map"""
    result = fgt.api.cmdb.router.route_map.delete(name="TEST_ROUTE_MAP_3")
    assert result is not None
    assert result.http_status == "success"


def test_get_router_route_map_verify():
    """Test: Verify route maps exist"""
    result = fgt.api.cmdb.router.route_map.get()
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

    test_get_router_route_map()
    print("✓ test_get_router_route_map passed")
    
    test_post_router_route_map_basic()
    print("✓ test_post_router_route_map_basic passed")
    
    test_get_router_route_map_specific()
    print("✓ test_get_router_route_map_specific passed")
    
    test_post_router_route_map_permit()
    print("✓ test_post_router_route_map_permit passed")
    
    test_post_router_route_map_deny()
    print("✓ test_post_router_route_map_deny passed")
    
    test_post_router_route_map_match_metric()
    print("✓ test_post_router_route_map_match_metric passed")
    
    test_post_router_route_map_match_tag()
    print("✓ test_post_router_route_map_match_tag passed")
    
    test_post_router_route_map_set_metric()
    print("✓ test_post_router_route_map_set_metric passed")
    
    test_post_router_route_map_set_metric_type()
    print("✓ test_post_router_route_map_set_metric_type passed")
    
    test_post_router_route_map_set_tag()
    print("✓ test_post_router_route_map_set_tag passed")
    
    test_post_router_route_map_set_local_preference()
    print("✓ test_post_router_route_map_set_local_preference passed")
    
    test_post_router_route_map_set_weight()
    print("✓ test_post_router_route_map_set_weight passed")
    
    test_post_router_route_map_match_origin()
    print("✓ test_post_router_route_map_match_origin passed")
    
    test_post_router_route_map_set_origin()
    print("✓ test_post_router_route_map_set_origin passed")
    
    test_post_router_route_map_multiple_rules()
    print("✓ test_post_router_route_map_multiple_rules passed")
    
    test_put_router_route_map()
    print("✓ test_put_router_route_map passed")
    
    test_put_router_route_map_add_rules()
    print("✓ test_put_router_route_map_add_rules passed")
    
    test_delete_router_route_map()
    print("✓ test_delete_router_route_map passed")
    
    test_get_router_route_map_verify()
    print("✓ test_get_router_route_map_verify passed")

    cleanup()
    print("✓ All router/route-map tests passed")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
