import argparse
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(project_root))
from fgtclient import fgt


def cleanup():
    auth_paths = fgt.api.cmdb.router.auth_path.get()
    for ap in auth_paths:
        if ap.name.startswith("test_"):
            fgt.api.cmdb.router.auth_path.delete(name=ap.name)

def test_get_router_auth_path():
    """Test: Get all router auth-path"""
    result = fgt.api.cmdb.router.auth_path.get()
    assert result is not None

def test_post_router_auth_path():
    """Test: Create a router auth-path"""
    result = fgt.api.cmdb.router.auth_path.post(
        name="test_authp1",
        device="port3",
        gateway="192.168.1.1"
    )
    assert result is not None
    assert result.http_status == "success"
    
        
def test_put_router_auth_path():
    """Test: Update a router auth-path"""
    result = fgt.api.cmdb.router.auth_path.put(
        name="test_authp1",
        gateway="192.168.1.254"
    )
    assert result is not None
    assert result.http_status == "success"
    
    # Verify the update
    verify = fgt.api.cmdb.router.auth_path.get(name="test_authp1")
    assert verify is not None
    assert verify.gateway == "192.168.1.254"

def test_get_specific_router_auth_path():
    """Test: Get specific router auth-path"""
    result = fgt.api.cmdb.router.auth_path.get(name="test_authp1")
    assert result is not None
    assert result.name == "test_authp1"

def test_delete_router_auth_path():
    """Test: Delete a router auth-path"""
    result = fgt.api.cmdb.router.auth_path.delete(name="test_authp1")
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

    test_get_router_auth_path()
    print("✓ test_get_router_auth_path passed")
    test_post_router_auth_path()
    print("✓ test_post_router_auth_path passed")
    test_put_router_auth_path()  
    print("✓ test_put_router_auth_path passed")
    test_get_specific_router_auth_path()
    print("✓ test_get_specific_router_auth_path passed")
    test_delete_router_auth_path()
    print("✓ test_delete_router_auth_path passed")

    cleanup()
    print("✓ All router/auth-path tests passed")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
