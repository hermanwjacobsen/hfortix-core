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

# NOTE: Router prefix-list6 endpoint structure:
# - GET /router/prefix-list6 - Get all IPv6 prefix lists
# - GET /router/prefix-list6/{name} - Get specific IPv6 prefix list
# - POST /router/prefix-list6 - Create new IPv6 prefix list
# - PUT /router/prefix-list6/{name} - Update IPv6 prefix list
# - DELETE /router/prefix-list6/{name} - Delete IPv6 prefix list

def cleanup():
    """Cleanup all IPv6 prefix lists after tests."""
    prefix_lists = fgt.api.cmdb.router.prefix_list6.get()
    for prefix_list in prefix_lists:
        fgt.api.cmdb.router.prefix_list6.delete(name=prefix_list.name)


def test_get_router_prefix_list6():
    """Test: Get all IPv6 prefix lists"""
    result = fgt.api.cmdb.router.prefix_list6.get()
    assert result is not None
    assert result.http_status_code == 200


def test_post_router_prefix_list6_basic():
    """Test: Create basic IPv6 prefix list"""
    result = fgt.api.cmdb.router.prefix_list6.post(
        name="TEST_PREFIX_LIST6_1",
        comments="Test IPv6 prefix list"
    )
    assert result is not None
    assert result.http_status == "success"


def test_get_router_prefix_list6_specific():
    """Test: Get specific IPv6 prefix list"""
    result = fgt.api.cmdb.router.prefix_list6.get(name="TEST_PREFIX_LIST6_1")
    assert result is not None
    assert result.http_status_code == 200
    assert result.name == "TEST_PREFIX_LIST6_1"


def test_post_router_prefix_list6_with_permit_rule():
    """Test: Create IPv6 prefix list with permit rule"""
    result = fgt.api.cmdb.router.prefix_list6.post(
        name="TEST_PREFIX_LIST6_2",
        comments="Permit specific IPv6 networks",
        rule=[
            {
                "id": 1,
                "action": "permit",
                "prefix6": "fd00::/8"
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"


def test_post_router_prefix_list6_with_deny_rule():
    """Test: Create IPv6 prefix list with deny rule"""
    result = fgt.api.cmdb.router.prefix_list6.post(
        name="TEST_PREFIX_LIST6_3",
        comments="Deny specific IPv6 networks",
        rule=[
            {
                "id": 1,
                "action": "deny",
                "prefix6": "fe80::/10"
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"


def test_post_router_prefix_list6_with_ge():
    """Test: Create IPv6 prefix list with GE (greater than or equal) matching"""
    result = fgt.api.cmdb.router.prefix_list6.post(
        name="TEST_PREFIX_LIST6_4",
        comments="Match IPv6 prefixes with GE",
        rule=[
            {
                "id": 1,
                "action": "permit",
                "prefix6": "2001:db8::/32",
                "ge": 48
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"


def test_post_router_prefix_list6_with_le():
    """Test: Create IPv6 prefix list with LE (less than or equal) matching"""
    result = fgt.api.cmdb.router.prefix_list6.post(
        name="TEST_PREFIX_LIST6_5",
        comments="Match IPv6 prefixes with LE",
        rule=[
            {
                "id": 1,
                "action": "permit",
                "prefix6": "fd00::/8",
                "le": 64
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"


def test_post_router_prefix_list6_with_ge_le():
    """Test: Create IPv6 prefix list with both GE and LE matching"""
    result = fgt.api.cmdb.router.prefix_list6.post(
        name="TEST_PREFIX_LIST6_6",
        comments="Match IPv6 prefixes with GE and LE range",
        rule=[
            {
                "id": 1,
                "action": "permit",
                "prefix6": "2001:db8::/32",
                "ge": 48,
                "le": 64
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"


def test_post_router_prefix_list6_multiple_rules():
    """Test: Create IPv6 prefix list with multiple rules"""
    result = fgt.api.cmdb.router.prefix_list6.post(
        name="TEST_PREFIX_LIST6_7",
        comments="Multiple IPv6 rules test",
        rule=[
            {
                "id": 1,
                "action": "permit",
                "prefix6": "fd00::/8"
            },
            {
                "id": 2,
                "action": "deny",
                "prefix6": "fd00:bad::/32"
            },
            {
                "id": 3,
                "action": "permit",
                "prefix6": "2001:db8::/32",
                "ge": 48,
                "le": 64
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_router_prefix_list6():
    """Test: Update IPv6 prefix list"""
    result = fgt.api.cmdb.router.prefix_list6.put(
        name="TEST_PREFIX_LIST6_1",
        comments="Updated test IPv6 prefix list",
        rule=[
            {
                "id": 1,
                "action": "permit",
                "prefix6": "fd12:3456::/32"
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_router_prefix_list6_add_rules():
    """Test: Add rules to existing IPv6 prefix list"""
    result = fgt.api.cmdb.router.prefix_list6.put(
        name="TEST_PREFIX_LIST6_2",
        comments="Permit specific IPv6 networks - updated",
        rule=[
            {
                "id": 1,
                "action": "permit",
                "prefix6": "fd00::/8"
            },
            {
                "id": 2,
                "action": "permit",
                "prefix6": "2001:db8::/32"
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"


def test_delete_router_prefix_list6():
    """Test: Delete specific IPv6 prefix list"""
    result = fgt.api.cmdb.router.prefix_list6.delete(name="TEST_PREFIX_LIST6_3")
    assert result is not None
    assert result.http_status == "success"


def test_get_router_prefix_list6_verify():
    """Test: Verify IPv6 prefix lists exist"""
    result = fgt.api.cmdb.router.prefix_list6.get()
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

    test_get_router_prefix_list6()
    print("✓ test_get_router_prefix_list6 passed")
    
    test_post_router_prefix_list6_basic()
    print("✓ test_post_router_prefix_list6_basic passed")
    
    test_get_router_prefix_list6_specific()
    print("✓ test_get_router_prefix_list6_specific passed")
    
    test_post_router_prefix_list6_with_permit_rule()
    print("✓ test_post_router_prefix_list6_with_permit_rule passed")
    
    test_post_router_prefix_list6_with_deny_rule()
    print("✓ test_post_router_prefix_list6_with_deny_rule passed")
    
    test_post_router_prefix_list6_with_ge()
    print("✓ test_post_router_prefix_list6_with_ge passed")
    
    test_post_router_prefix_list6_with_le()
    print("✓ test_post_router_prefix_list6_with_le passed")
    
    test_post_router_prefix_list6_with_ge_le()
    print("✓ test_post_router_prefix_list6_with_ge_le passed")
    
    test_post_router_prefix_list6_multiple_rules()
    print("✓ test_post_router_prefix_list6_multiple_rules passed")
    
    test_put_router_prefix_list6()
    print("✓ test_put_router_prefix_list6 passed")
    
    test_put_router_prefix_list6_add_rules()
    print("✓ test_put_router_prefix_list6_add_rules passed")
    
    test_delete_router_prefix_list6()
    print("✓ test_delete_router_prefix_list6 passed")
    
    test_get_router_prefix_list6_verify()
    print("✓ test_get_router_prefix_list6_verify passed")

    cleanup()
    print("✓ All router/prefix-list6 tests passed")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
