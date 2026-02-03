import argparse
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(project_root))
from fgtclient import fgt


def cleanup():
    aspath_lists = fgt.api.cmdb.router.aspath_list.get()
    for aspl in aspath_lists:
        if aspl.name.startswith("test_"):
            fgt.api.cmdb.router.aspath_list.delete(name=aspl.name)

def test_get_router_aspath_list():
    """Test: Get all router aspath-list"""
    result = fgt.api.cmdb.router.aspath_list.get()
    assert result is not None

def test_post_router_aspath_list():
    """Test: Create a router aspath-list"""
    result = fgt.api.cmdb.router.aspath_list.post(
        name="test_aspl1",
        rule= [
            {
                "id": 1,
                "action": "permit",
                "regexp": "^65000_"
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"
    
        
def test_put_router_aspath_list():
    """Test: Update a router aspath-list"""
    result = fgt.api.cmdb.router.aspath_list.put(
        name="test_aspl1",
        rule= [
            {
                "id": 1,
                "action": "deny",
                "regexp": "^65001_"
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"

def test_get_specific_router_aspath_list():
    """Test: Get specific router aspath-list"""
    result = fgt.api.cmdb.router.aspath_list.get(name="test_aspl1")
    assert result is not None
    assert result.name == "test_aspl1"

def test_delete_router_aspath_list():
    """Test: Delete a router aspath-list"""
    result = fgt.api.cmdb.router.aspath_list.delete(name="test_aspl1")
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

    test_get_router_aspath_list()
    print("✓ test_get_router_aspath_list passed")
    test_post_router_aspath_list()
    print("✓ test_post_router_aspath_list passed")
    test_put_router_aspath_list()  
    print("✓ test_put_router_aspath_list passed")
    test_get_specific_router_aspath_list()
    print("✓ test_get_specific_router_aspath_list passed")
    test_delete_router_aspath_list()
    print("✓ test_delete_router_aspath_list passed")

    cleanup()
    print("✓ All router/aspath-list tests passed")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
