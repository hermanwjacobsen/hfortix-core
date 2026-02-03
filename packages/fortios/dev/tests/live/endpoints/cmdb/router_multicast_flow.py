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
    """Remove all test multicast flows"""
    flows = fgt.api.cmdb.router.multicast_flow.get()
    for flow in flows:
        if flow.name.startswith("test_"):
            fgt.api.cmdb.router.multicast_flow.delete(name=flow.name)


def test_get_router_multicast_flow():
    """Test: Get all multicast flows"""
    result = fgt.api.cmdb.router.multicast_flow.get()
    assert result is not None


def test_post_router_multicast_flow_basic():
    """Test: Create a basic multicast flow"""
    result = fgt.api.cmdb.router.multicast_flow.post(
        name="test_flow1",
        comments="Test multicast flow 1",
        flows=[
            {
                "id": 1,
                "group_addr": "224.0.1.1",
                "source_addr": "192.168.1.100"
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"
    verify = fgt.api.cmdb.router.multicast_flow.get(name="test_flow1")
    assert len(verify.flows) == 1
    assert verify.flows[0].id == 1
    assert verify.flows[0].group_addr == "224.0.1.1"
    assert verify.flows[0].source_addr == "192.168.1.100"

def test_post_router_multicast_flow_multiple():
    """Test: Create multicast flow with multiple entries"""
    result = fgt.api.cmdb.router.multicast_flow.post(
        name="test_flow_multi",
        comments="Test multicast flow with multiple entries",
        flows=[
            {
                "id": 1,
                "group_addr": "224.0.1.10",
                "source_addr": "192.168.1.10"
            },
            {
                "id": 2,
                "group_addr": "224.0.1.20",
                "source_addr": "192.168.1.20"
            },
            {
                "id": 3,
                "group_addr": "224.0.1.30",
                "source_addr": "192.168.1.30"
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"


def test_post_router_multicast_flow_range():
    """Test: Create multicast flow"""
    result = fgt.api.cmdb.router.multicast_flow.post(
        name="test_flow_range",
        comments="Multicast flow entry",
        flows=[
            {
                "id": 1,
                "group_addr": "239.0.0.1",
                "source_addr": "10.0.0.1"
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_router_multicast_flow():
    """Test: Update a multicast flow"""
    result = fgt.api.cmdb.router.multicast_flow.put(
        name="test_flow1",
        comments="Updated multicast flow 1",
        flows=[
            {
                "id": 1,
                "group_addr": "224.0.2.1",
                "source_addr": "192.168.2.100"
            },
            {
                "id": 2,
                "group_addr": "224.0.2.2",
                "source_addr": "192.168.2.101"
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"


def test_get_specific_router_multicast_flow():
    """Test: Get specific multicast flow"""
    result = fgt.api.cmdb.router.multicast_flow.get(name="test_flow1")
    assert result is not None
    assert result.name == "test_flow1"
    assert result.comments == "Updated multicast flow 1"
    # Should have 2 flows after update
    assert len(result.flows) == 2


def test_delete_router_multicast_flow():
    """Test: Delete multicast flows"""
    result = fgt.api.cmdb.router.multicast_flow.delete(name="test_flow1")
    assert result is not None
    assert result.http_status == "success"
    
    result = fgt.api.cmdb.router.multicast_flow.delete(name="test_flow_multi")
    assert result is not None
    assert result.http_status == "success"
    
    result = fgt.api.cmdb.router.multicast_flow.delete(name="test_flow_range")
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

    test_get_router_multicast_flow()
    print("✓ test_get_router_multicast_flow passed")
    
    test_post_router_multicast_flow_basic()
    print("✓ test_post_router_multicast_flow_basic passed")
    
    test_post_router_multicast_flow_multiple()
    print("✓ test_post_router_multicast_flow_multiple passed")
    
    test_post_router_multicast_flow_range()
    print("✓ test_post_router_multicast_flow_range passed")
    
    test_put_router_multicast_flow()
    print("✓ test_put_router_multicast_flow passed")
    
    test_get_specific_router_multicast_flow()
    print("✓ test_get_specific_router_multicast_flow passed")
    
    test_delete_router_multicast_flow()
    print("✓ test_delete_router_multicast_flow passed")

    cleanup()
    print("✓ All router/multicast-flow tests passed")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
