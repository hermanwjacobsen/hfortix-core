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

# NOTE: OSPF endpoint structure:
# - GET /router/ospf - Get OSPF configuration
# - PUT /router/ospf - Update OSPF configuration
# - No POST/DELETE (singleton resource)

def cleanup():
    """Cleanup OSPF configuration after tests."""
    fgt.api.cmdb.router.ospf.put(
        router_id="0.0.0.0",
        area=[],
        ospf_interface=[],
        network=[],
        neighbor=[],
        passive_interface=[],
        summary_address=[],
        distribute_list=[],
        redistribute=[]
    )


def test_get_router_ospf():
    """Test: Get OSPF configuration"""
    result = fgt.api.cmdb.router.ospf.get()
    assert result is not None
    assert result.http_status_code == 200


def test_put_router_ospf_basic():
    """Test: Configure basic OSPF settings"""
    result = fgt.api.cmdb.router.ospf.put(
        router_id="192.168.1.1",
        abr_type="standard",
        auto_cost_ref_bandwidth=1001,
        log_neighbour_changes="enable",
        bfd="disable",
        default_information_metric_type="2",
        area=[
            {
                "id": "0.0.0.0"
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"
    verify = fgt.api.cmdb.router.ospf.get()
    assert verify.router_id == "192.168.1.1"
    assert verify.abr_type == "standard"
    assert verify.auto_cost_ref_bandwidth == 1001
    assert verify.log_neighbour_changes == "enable"
    assert verify.bfd == "disable"
    assert verify.default_information_metric_type == "2"
    assert verify.area[0].id == "0.0.0.0"




def test_put_router_ospf_distances():
    """Test: Configure OSPF administrative distances"""
    result = fgt.api.cmdb.router.ospf.put(
        router_id="192.168.1.1",
        distance_external=110,
        distance_inter_area=110,
        distance_intra_area=110
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_router_ospf_timers():
    """Test: Configure OSPF timers and intervals"""
    result = fgt.api.cmdb.router.ospf.put(
        router_id="192.168.1.1",
        spf_timers="5 10",
        lsa_refresh_interval=0
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_router_ospf_default_route():
    """Test: Configure OSPF default route origination"""
    result = fgt.api.cmdb.router.ospf.put(
        router_id="192.168.1.1",
        default_information_originate="enable",
        default_information_metric=10,
        default_information_metric_type="2"
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_router_ospf_area():
    """Test: Configure OSPF area"""
    result = fgt.api.cmdb.router.ospf.put(
        router_id="192.168.1.1",
        area=[
            {
                "id": "0.0.0.0",
                "type": "regular",
                "shortcut": "disable",
                "authentication": "none",
                "default_cost": 10
            }
        ]  # type: ignore
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_router_ospf_network():
    """Test: Configure OSPF network"""
    result = fgt.api.cmdb.router.ospf.put(
        router_id="192.168.1.1",
        area=[
            {
                "id": "0.0.0.0",
                "type": "regular"
            }
        ],  # type: ignore
        network=[
            {
                "id": 1,
                "prefix": "192.168.1.0 255.255.255.0",
                "area": "0.0.0.0"
            }
        ]  # type: ignore
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_router_ospf_interface():
    """Test: Configure OSPF interface"""
    result = fgt.api.cmdb.router.ospf.put(
        router_id="192.168.1.1",
        ospf_interface=[
            {
                "name": "port3_ospf",
                "interface": "port3",
                "cost": 10,
                "priority": 1,
                "dead_interval": 40,
                "hello_interval": 10,
                "authentication": "none",
                "network_type": "broadcast",
                "bfd": "disable",
                "status": "enable"
            }
        ]  # type: ignore
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_router_ospf_passive_interface():
    """Test: Configure OSPF passive interface"""
    result = fgt.api.cmdb.router.ospf.put(
        router_id="192.168.1.1",
        passive_interface=[
            {
                "name": "port3"
            }
        ]  # type: ignore
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_router_ospf_redistribute():
    """Test: Configure OSPF route redistribution"""
    result = fgt.api.cmdb.router.ospf.put(
        router_id="192.168.1.1",
        redistribute=[
            {
                "name": "connected",
                "status": "enable",
                "metric": 20,
                "metric_type": "2",
                "tag": 0
            }
        ]  # type: ignore
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_router_ospf_summary():
    """Test: Configure OSPF summary address"""
    result = fgt.api.cmdb.router.ospf.put(
        router_id="192.168.1.1",
        summary_address=[
            {
                "id": 1,
                "prefix": "10.0.0.0 255.0.0.0",
                "tag": 0,
                "advertise": "enable"
            }
        ]  # type: ignore
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_router_ospf_graceful_restart():
    """Test: Configure OSPF graceful restart"""
    result = fgt.api.cmdb.router.ospf.put(
        router_id="192.168.1.1",
        restart_mode="graceful-restart",
        restart_period=120,
        restart_on_topology_change="disable"
    )
    assert result is not None
    assert result.http_status == "success"


def test_get_router_ospf_verify():
    """Test: Verify OSPF configuration"""
    result = fgt.api.cmdb.router.ospf.get()
    assert result is not None
    assert result.http_status_code == 200
    # Verify router ID is set
    assert hasattr(result, "router_id")


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

    test_get_router_ospf()
    print("✓ test_get_router_ospf passed")
    
    test_put_router_ospf_basic()
    print("✓ test_put_router_ospf_basic passed")
    
    test_put_router_ospf_distances()
    print("✓ test_put_router_ospf_distances passed")
    
    test_put_router_ospf_timers()
    print("✓ test_put_router_ospf_timers passed")
    
    test_put_router_ospf_default_route()
    print("✓ test_put_router_ospf_default_route passed")
    
    test_put_router_ospf_area()
    print("✓ test_put_router_ospf_area passed")
    
    test_put_router_ospf_network()
    print("✓ test_put_router_ospf_network passed")
    
    test_put_router_ospf_interface()
    print("✓ test_put_router_ospf_interface passed")
    
    test_put_router_ospf_passive_interface()
    print("✓ test_put_router_ospf_passive_interface passed")
    
    test_put_router_ospf_redistribute()
    print("✓ test_put_router_ospf_redistribute passed")
    
    test_put_router_ospf_summary()
    print("✓ test_put_router_ospf_summary passed")
    
    test_put_router_ospf_graceful_restart()
    print("✓ test_put_router_ospf_graceful_restart passed")
    
    test_get_router_ospf_verify()
    print("✓ test_get_router_ospf_verify passed")

    cleanup()
    print("✓ All router/ospf tests passed")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
