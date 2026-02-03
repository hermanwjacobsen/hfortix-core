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

def cleanup():
    """Remove all test extended community lists"""
    extcommunity_lists = fgt.api.cmdb.router.extcommunity_list.get()
    for ecl in extcommunity_lists:
        if ecl.name.startswith("test_"):
            fgt.api.cmdb.router.extcommunity_list.delete(name=ecl.name)

def test_get_router_extcommunity_list():
    """Test: Get all router extcommunity-list"""
    result = fgt.api.cmdb.router.extcommunity_list.get()
    assert result is not None

def test_post_router_extcommunity_list_standard():
    """Test: Create a standard extended community-list"""
    result = fgt.api.cmdb.router.extcommunity_list.post(
        name="test_extcomm_std1",
        type="standard",
        rule=[
            {
                "id": 1,
                "action": "permit",
                "type": "rt",
                "match": "65000:100"
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"
    verify = fgt.api.cmdb.router.extcommunity_list.get(name="test_extcomm_std1")
    assert len(verify.rule) == 1
    assert verify.rule[0].id == 1
    assert verify.rule[0].action == "permit"
    assert verify.rule[0].type == "rt"
    assert verify.rule[0].match == "65000:100"
    

def test_post_router_extcommunity_list_expanded():
    """Test: Create an expanded extended community-list"""
    result = fgt.api.cmdb.router.extcommunity_list.post(
        name="test_extcomm_exp1",
        type="expanded",
        rule=[
            {
                "id": 1,
                "action": "permit",
                "regexp": "^RT:65[0-9]+:[0-9]+$"
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"
    
def test_put_router_extcommunity_list():
    """Test: Update a router extended community-list"""
    result = fgt.api.cmdb.router.extcommunity_list.put(
        name="test_extcomm_std1",
        type="standard",
        rule=[
            {
                "id": 1,
                "action": "deny",
                "type": "rt",
                "match": "65001:200"
            },
            {
                "id": 2,
                "action": "permit",
                "type": "soo",
                "match": "65000:100"
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"

def test_get_specific_router_extcommunity_list():
    """Test: Get specific router extended community-list"""
    result = fgt.api.cmdb.router.extcommunity_list.get(name="test_extcomm_std1")
    assert result is not None
    assert result.name == "test_extcomm_std1"
    assert result.type == "standard"

def test_delete_router_extcommunity_list():
    """Test: Delete router extended community-lists"""
    # Delete standard extended community list
    result = fgt.api.cmdb.router.extcommunity_list.delete(name="test_extcomm_std1")
    assert result is not None
    assert result.http_status == "success"
    
    # Delete expanded extended community list
    result = fgt.api.cmdb.router.extcommunity_list.delete(name="test_extcomm_exp1")
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

    test_get_router_extcommunity_list()
    print("✓ test_get_router_extcommunity_list passed")
    
    test_post_router_extcommunity_list_standard()
    print("✓ test_post_router_extcommunity_list_standard passed")
    
    test_post_router_extcommunity_list_expanded()
    print("✓ test_post_router_extcommunity_list_expanded passed")
    
    test_put_router_extcommunity_list()
    print("✓ test_put_router_extcommunity_list passed")
    
    test_get_specific_router_extcommunity_list()
    print("✓ test_get_specific_router_extcommunity_list passed")
    
    test_delete_router_extcommunity_list()
    print("✓ test_delete_router_extcommunity_list passed")

    cleanup()
    print("✓ All router/extcommunity-list tests passed")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
