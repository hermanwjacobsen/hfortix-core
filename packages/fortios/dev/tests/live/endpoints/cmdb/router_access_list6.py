import argparse
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(project_root))
from fgtclient import fgt


def cleanup():
    access_lists = fgt.api.cmdb.router.access_list6.get()
    for acl in access_lists:
        if acl.name.startswith("test_"):
            fgt.api.cmdb.router.access_list6.delete(name=acl.name)

def test_get_router_access_list6():
    """Test: Get all router access-list6"""
    result = fgt.api.cmdb.router.access_list6.get()
    assert result is not None

def test_post_router_access_list6():
    """Test: Create a router access-list6"""
    result = fgt.api.cmdb.router.access_list6.post(
        name="test_acl6_1",
        comments="Test IPv6 ACL 1",
        rule= [
            {
                "id": 1,
                "action": "permit",
                "prefix6": "2001:db8::/32",
                "exact-match": "disable"
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"
    
        
def test_put_router_access_list6():
    """Test: Update a router access-list6"""
    result = fgt.api.cmdb.router.access_list6.put(
        name="test_acl6_1",
        comments="Updated Test IPv6 ACL 1"
    )
    assert result is not None
    assert result.http_status == "success"
    
    # Verify the update
    verify = fgt.api.cmdb.router.access_list6.get(name="test_acl6_1")
    assert verify is not None
    assert verify.comments == "Updated Test IPv6 ACL 1"

def test_get_specific_router_access_list6():
    """Test: Get specific router access-list6"""
    result = fgt.api.cmdb.router.access_list6.get(name="test_acl6_1")
    assert result is not None
    assert result.name == "test_acl6_1"

def test_delete_router_access_list6():
    """Test: Delete a router access-list6"""
    result = fgt.api.cmdb.router.access_list6.delete(name="test_acl6_1")
    assert result is not None
    assert result.http_status == "success"




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

    test_get_router_access_list6()
    print("✓ test_get_router_access_list6 passed")
    test_post_router_access_list6()
    print("✓ test_post_router_access_list6 passed")
    test_put_router_access_list6()  
    print("✓ test_put_router_access_list6 passed")
    test_get_specific_router_access_list6()
    print("✓ test_get_specific_router_access_list6 passed")
    test_delete_router_access_list6()
    print("✓ test_delete_router_access_list6 passed")

    cleanup()
    print("✓ All router/access-list6 tests passed")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
