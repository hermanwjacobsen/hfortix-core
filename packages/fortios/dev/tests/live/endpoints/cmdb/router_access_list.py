import argparse
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(project_root))
from fgtclient import fgt


def cleanup():
    access_lists = fgt.api.cmdb.router.access_list.get()
    for acl in access_lists:
        if acl.name.startswith("test_"):
            fgt.api.cmdb.router.access_list.delete(name=acl.name)

def test_get_router_access_lists():
    """Test: Get all router access-lists"""
    result = fgt.api.cmdb.router.access_list.get()
    assert result is not None

def test_post_router_access_lists():
    """Test: Create a router access-list"""
    result = fgt.api.cmdb.router.access_list.post(
        name="test_acl1",
        comments="Test ACL 1",
        rule= [
            {
                "id": 1,
                "action": "permit",
                "prefix": "10.0.0.0 255.255.255.0",
                "exact-match": "disable"
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"
    
        
def test_put_router_access_lists():
    """Test: Update a router access-list"""
    result = fgt.api.cmdb.router.access_list.put(
        name="test_acl1",
        comments="Updated Test ACL 1"
    )
    assert result is not None
    assert result.http_status == "success"
    
    # Verify the update
    verify = fgt.api.cmdb.router.access_list.get(name="test_acl1")
    assert verify is not None
    assert verify.comments == "Updated Test ACL 1"

def test_get_specific_router_access_lists():
    """Test: Get specific router access-list"""
    result = fgt.api.cmdb.router.access_list.get(name="test_acl1")
    assert result is not None
    assert result.name == "test_acl1"

def test_delete_router_access_lists():
    """Test: Delete a router access-list"""
    result = fgt.api.cmdb.router.access_list.delete(name="test_acl1")
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

    test_get_router_access_lists()
    print("✓ test_get_router_access_lists passed")
    test_post_router_access_lists()
    print("✓ test_post_router_access_lists passed")
    test_put_router_access_lists()  
    print("✓ test_put_router_access_lists passed")
    test_get_specific_router_access_lists()
    print("✓ test_get_specific_router_access_lists passed")
    test_delete_router_access_lists()
    print("✓ test_delete_router_access_lists passed")

    cleanup()
    print("✓ All router/access-list tests passed")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
