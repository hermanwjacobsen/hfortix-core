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
    """Remove all test community lists"""
    try:
        community_lists = fgt.api.cmdb.router.community_list.get()
        if community_lists:
            for cl in community_lists:
                if cl.name.startswith("test_"):
                    try:
                        fgt.api.cmdb.router.community_list.delete(name=cl.name)
                    except:
                        pass  # Ignore errors during cleanup
    except:
        pass  # Ignore if get fails

@pytest.fixture(scope="module", autouse=True)
def setup_cleanup():
    """Run cleanup before and after all tests in this module"""
    cleanup()  # Clean up before tests
    yield
    cleanup()  # Clean up after tests

def test_get_router_community_list():
    """Test: Get all router community-list"""
    result = fgt.api.cmdb.router.community_list.get()
    assert result is not None

def test_post_router_community_list_standard():
    """Test: Create a standard community-list"""
    result = fgt.api.cmdb.router.community_list.post(
        name="test_comm_std1",
        type="standard",
        rule=[
            {
                "id": 1,
                "action": "permit",
                "match": "65000:100"
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"

def test_post_router_community_list_expanded():
    """Test: Create an expanded community-list"""
    result = fgt.api.cmdb.router.community_list.post(
        name="test_comm_exp1",
        type="expanded",
        rule=[
            {
                "id": 1,
                "action": "permit",
                "regexp": "^65[0-9]+:[0-9]+$"
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"
    
def test_put_router_community_list():
    """Test: Update a router community-list (depends on test_post creating it first)"""
    # Update the community list created by test_post_router_community_list_standard
    result = fgt.api.cmdb.router.community_list.put(
        name="test_comm_std1",
        type="standard",
        rule=[
            {
                "id": 1,
                "action": "deny",
                "match": "65001:200"
            },
            {
                "id": 2,
                "action": "permit",
                "match": "65000:100"
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"
    verify = fgt.api.cmdb.router.community_list.get(name="test_comm_std1")
    
    assert len(verify.rule) == 2
    
    # Sort rules by ID to ensure consistent ordering
    rules_by_id = {rule.id: rule for rule in verify.rule}
    
    assert 1 in rules_by_id
    assert rules_by_id[1].action == "deny"
    # FortiOS inconsistency: returns 'match' OR 'regexp' depending on client
    # Direct API returns 'regexp', FMG proxy returns 'match'
    match_value = getattr(rules_by_id[1], 'match', None) or getattr(rules_by_id[1], 'regexp', None)
    assert match_value == "65001:200"
    
    assert 2 in rules_by_id
    assert rules_by_id[2].action == "permit"
    match_value = getattr(rules_by_id[2], 'match', None) or getattr(rules_by_id[2], 'regexp', None)
    assert match_value == "65000:100"

def test_get_specific_router_community_list():
    """Test: Get specific router community-list"""
    result = fgt.api.cmdb.router.community_list.get(name="test_comm_std1")
    assert result is not None
    assert result.name == "test_comm_std1"
    assert result.type == "standard"
    

def test_delete_router_community_list():
    """Test: Delete router community-lists"""
    # Delete standard community list
    result = fgt.api.cmdb.router.community_list.delete(name="test_comm_std1")
    assert result is not None
    assert result.http_status == "success"
    
    # Delete expanded community list
    result = fgt.api.cmdb.router.community_list.delete(name="test_comm_exp1")
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

    test_get_router_community_list()
    print("✓ test_get_router_community_list passed")
    
    test_post_router_community_list_standard()
    print("✓ test_post_router_community_list_standard passed")
    
    test_post_router_community_list_expanded()
    print("✓ test_post_router_community_list_expanded passed")
    
    test_put_router_community_list()
    print("✓ test_put_router_community_list passed")
    
    test_get_specific_router_community_list()
    print("✓ test_get_specific_router_community_list passed")
    
    test_delete_router_community_list()
    print("✓ test_delete_router_community_list passed")

    cleanup()
    print("✓ All router/community-list tests passed")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
