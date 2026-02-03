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

# NOTE: Router prefix-list endpoint structure:
# - GET /router/prefix-list - Get all prefix lists
# - GET /router/prefix-list/{name} - Get specific prefix list
# - POST /router/prefix-list - Create new prefix list
# - PUT /router/prefix-list/{name} - Update prefix list
# - DELETE /router/prefix-list/{name} - Delete prefix list

def cleanup():
    """Cleanup all prefix lists after tests."""
    prefix_lists = fgt.api.cmdb.router.prefix_list.get()
    for prefix_list in prefix_lists:
        fgt.api.cmdb.router.prefix_list.delete(name=prefix_list.name)

def test_get_router_prefix_list():
    """Test: Get all prefix lists"""
    result = fgt.api.cmdb.router.prefix_list.get()
    assert result is not None
    assert result.http_status_code == 200


def test_post_router_prefix_list_basic():
    """Test: Create basic prefix list"""
    result = fgt.api.cmdb.router.prefix_list.post(
        name="TEST_PREFIX_LIST_1",
        comments="Test prefix list"
    )
    assert result is not None
    assert result.http_status == "success"


def test_get_router_prefix_list_specific():
    """Test: Get specific prefix list"""
    result = fgt.api.cmdb.router.prefix_list.get(name="TEST_PREFIX_LIST_1")
    assert result is not None
    assert result.http_status_code == 200
    assert result.name == "TEST_PREFIX_LIST_1"


def test_post_router_prefix_list_with_permit_rule():
    """Test: Create prefix list with permit rule"""
    result = fgt.api.cmdb.router.prefix_list.post(
        name="TEST_PREFIX_LIST_2",
        comments="Permit specific networks",
        rule=[
            {
                "id": 1,
                "action": "permit",
                "prefix": "10.0.0.0/8"
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"


def test_post_router_prefix_list_with_deny_rule():
    """Test: Create prefix list with deny rule"""
    result = fgt.api.cmdb.router.prefix_list.post(
        name="TEST_PREFIX_LIST_3",
        comments="Deny specific networks",
        rule=[
            {
                "id": 1,
                "action": "deny",
                "prefix": "192.168.0.0/16"
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"


def test_post_router_prefix_list_with_ge():
    """Test: Create prefix list with GE (greater than or equal) matching"""
    result = fgt.api.cmdb.router.prefix_list.post(
        name="TEST_PREFIX_LIST_4",
        comments="Match prefixes with GE",
        rule=[
            {
                "id": 1,
                "action": "permit",
                "prefix": "172.16.0.0/12",
                "ge": 16
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"


def test_post_router_prefix_list_with_le():
    """Test: Create prefix list with LE (less than or equal) matching"""
    result = fgt.api.cmdb.router.prefix_list.post(
        name="TEST_PREFIX_LIST_5",
        comments="Match prefixes with LE",
        rule=[
            {
                "id": 1,
                "action": "permit",
                "prefix": "10.0.0.0/8",
                "le": 24
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"


def test_post_router_prefix_list_with_ge_le():
    """Test: Create prefix list with both GE and LE matching"""
    result = fgt.api.cmdb.router.prefix_list.post(
        name="TEST_PREFIX_LIST_6",
        comments="Match prefixes with GE and LE range",
        rule=[
            {
                "id": 1,
                "action": "permit",
                "prefix": "192.168.0.0/16",
                "ge": 20,
                "le": 28
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"


def test_post_router_prefix_list_multiple_rules():
    """Test: Create prefix list with multiple rules"""
    result = fgt.api.cmdb.router.prefix_list.post(
        name="TEST_PREFIX_LIST_7",
        comments="Multiple rules test",
        rule=[
            {
                "id": 1,
                "action": "permit",
                "prefix": "10.0.0.0/8"
            },
            {
                "id": 2,
                "action": "deny",
                "prefix": "10.1.0.0/16"
            },
            {
                "id": 3,
                "action": "permit",
                "prefix": "172.16.0.0/12",
                "ge": 16,
                "le": 24
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_router_prefix_list():
    """Test: Update prefix list"""
    result = fgt.api.cmdb.router.prefix_list.put(
        name="TEST_PREFIX_LIST_1",
        comments="Updated test prefix list",
        rule=[
            {
                "id": 1,
                "action": "permit",
                "prefix": "10.10.0.0/16"
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_router_prefix_list_add_rules():
    """Test: Add rules to existing prefix list"""
    result = fgt.api.cmdb.router.prefix_list.put(
        name="TEST_PREFIX_LIST_2",
        comments="Permit specific networks - updated",
        rule=[
            {
                "id": 1,
                "action": "permit",
                "prefix": "10.0.0.0/8"
            },
            {
                "id": 2,
                "action": "permit",
                "prefix": "192.168.0.0/16"
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"


def test_delete_router_prefix_list():
    """Test: Delete specific prefix list"""
    result = fgt.api.cmdb.router.prefix_list.delete(name="TEST_PREFIX_LIST_3")
    assert result is not None
    assert result.http_status == "success"


def test_get_router_prefix_list_verify():
    """Test: Verify prefix lists exist"""
    result = fgt.api.cmdb.router.prefix_list.get()
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

    test_get_router_prefix_list()
    print("✓ test_get_router_prefix_list passed")
    
    test_post_router_prefix_list_basic()
    print("✓ test_post_router_prefix_list_basic passed")
    
    test_get_router_prefix_list_specific()
    print("✓ test_get_router_prefix_list_specific passed")
    
    test_post_router_prefix_list_with_permit_rule()
    print("✓ test_post_router_prefix_list_with_permit_rule passed")
    
    test_post_router_prefix_list_with_deny_rule()
    print("✓ test_post_router_prefix_list_with_deny_rule passed")
    
    test_post_router_prefix_list_with_ge()
    print("✓ test_post_router_prefix_list_with_ge passed")
    
    test_post_router_prefix_list_with_le()
    print("✓ test_post_router_prefix_list_with_le passed")
    
    test_post_router_prefix_list_with_ge_le()
    print("✓ test_post_router_prefix_list_with_ge_le passed")
    
    test_post_router_prefix_list_multiple_rules()
    print("✓ test_post_router_prefix_list_multiple_rules passed")
    
    test_put_router_prefix_list()
    print("✓ test_put_router_prefix_list passed")
    
    test_put_router_prefix_list_add_rules()
    print("✓ test_put_router_prefix_list_add_rules passed")
    
    test_delete_router_prefix_list()
    print("✓ test_delete_router_prefix_list passed")
    
    test_get_router_prefix_list_verify()
    print("✓ test_get_router_prefix_list_verify passed")

    cleanup()
    print("✓ All router/prefix-list tests passed")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
