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

# NOTE: OSPFv3 endpoint structure:
# - GET /router/ospf6 - Get OSPFv3 configuration
# - PUT /router/ospf6 - Update OSPFv3 configuration
# - No POST/DELETE (singleton resource)

def cleanup():
    """Cleanup OSPFv3 configuration after tests."""
    fgt.api.cmdb.router.ospf6.put(
        router_id="0.0.0.0",
        area=[],
        ospf6_interface=[],
        redistribute=[],
        passive_interface=[],
        summary_address=[]
    )


def test_get_router_ospf6():
    """Test: Get OSPFv3 configuration"""
    result = fgt.api.cmdb.router.ospf6.get()
    assert result is not None
    assert result.http_status_code == 200


def test_put_router_ospf6_basic():
    """Test: Configure basic OSPFv3 settings"""
    result = fgt.api.cmdb.router.ospf6.put(
        router_id="192.168.1.1",
        abr_type="standard",
        auto_cost_ref_bandwidth=1000,
        log_neighbour_changes="enable",
        bfd="disable"
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_router_ospf6_timers():
    """Test: Configure OSPFv3 timers"""
    result = fgt.api.cmdb.router.ospf6.put(
        router_id="192.168.1.1",
        spf_timers="5 10"
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_router_ospf6_default_route():
    """Test: Configure OSPFv3 default route origination"""
    result = fgt.api.cmdb.router.ospf6.put(
        router_id="192.168.1.1",
        default_information_originate="enable",
        default_information_metric=10,
        default_information_metric_type="2"
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_router_ospf6_area():
    """Test: Configure OSPFv3 area"""
    result = fgt.api.cmdb.router.ospf6.put(
        router_id="192.168.1.1",
        area=[
            {
                "id": "0.0.0.0",
                "type": "regular",
                "default_cost": 10,
                "authentication": "none"
            }
        ]  # type: ignore
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_router_ospf6_area_stub():
    """Test: Configure OSPFv3 stub area"""
    result = fgt.api.cmdb.router.ospf6.put(
        router_id="192.168.1.1",
        area=[
            {
                "id": "0.0.0.0",
                "type": "regular"
            },
            {
                "id": "0.0.0.1",
                "type": "stub",
                "stub_type": "summary",
                "default_cost": 20
            }
        ]  # type: ignore
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_router_ospf6_area_nssa():
    """Test: Configure OSPFv3 NSSA area"""
    result = fgt.api.cmdb.router.ospf6.put(
        router_id="192.168.1.1",
        area=[
            {
                "id": "0.0.0.0",
                "type": "regular"
            },
            {
                "id": "0.0.0.2",
                "type": "nssa",
                "nssa_translator_role": "candidate",
                "nssa_default_information_originate": "enable",
                "nssa_default_information_originate_metric": 10,
                "nssa_default_information_originate_metric_type": "2"
            }
        ]  # type: ignore
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_router_ospf6_interface():
    """Test: Configure OSPFv3 interface"""
    result = fgt.api.cmdb.router.ospf6.put(
        router_id="192.168.1.1",
        ospf6_interface=[
            {
                "name": "port3_ospf6",
                "area_id": "0.0.0.0",
                "interface": "port3",
                "cost": 10,
                "priority": 1,
                "dead_interval": 40,
                "hello_interval": 10,
                "retransmit_interval": 5,
                "transmit_delay": 1,
                "network_type": "broadcast",
                "bfd": "disable",
                "mtu_ignore": "disable",
                "authentication": "none",
                "status": "enable"
            }
        ]  # type: ignore
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_router_ospf6_passive_interface():
    """Test: Configure OSPFv3 passive interface"""
    result = fgt.api.cmdb.router.ospf6.put(
        router_id="192.168.1.1",
        passive_interface=[
            {
                "name": "port3"
            }
        ]  # type: ignore
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_router_ospf6_redistribute():
    """Test: Configure OSPFv3 route redistribution"""
    result = fgt.api.cmdb.router.ospf6.put(
        router_id="192.168.1.1",
        redistribute=[
            {
                "name": "connected",
                "status": "enable",
                "metric": 20,
                "metric_type": "2"
            }
        ]  # type: ignore
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_router_ospf6_summary():
    """Test: Configure OSPFv3 summary address"""
    result = fgt.api.cmdb.router.ospf6.put(
        router_id="192.168.1.1",
        summary_address=[
            {
                "id": 1,
                "prefix6": "fd00::/64",
                "advertise": "enable",
                "tag": 0
            }
        ]  # type: ignore
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_router_ospf6_graceful_restart():
    """Test: Configure OSPFv3 graceful restart"""
    result = fgt.api.cmdb.router.ospf6.put(
        router_id="192.168.1.1",
        restart_mode="graceful-restart",
        restart_period=120,
        restart_on_topology_change="disable"
    )
    assert result is not None
    assert result.http_status == "success"


def test_get_router_ospf6_verify():
    """Test: Verify OSPFv3 configuration"""
    result = fgt.api.cmdb.router.ospf6.get()
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

    test_get_router_ospf6()
    print("✓ test_get_router_ospf6 passed")
    
    test_put_router_ospf6_basic()
    print("✓ test_put_router_ospf6_basic passed")
    
    test_put_router_ospf6_timers()
    print("✓ test_put_router_ospf6_timers passed")
    
    test_put_router_ospf6_default_route()
    print("✓ test_put_router_ospf6_default_route passed")
    
    test_put_router_ospf6_area()
    print("✓ test_put_router_ospf6_area passed")
    
    test_put_router_ospf6_area_stub()
    print("✓ test_put_router_ospf6_area_stub passed")
    
    test_put_router_ospf6_area_nssa()
    print("✓ test_put_router_ospf6_area_nssa passed")
    
    test_put_router_ospf6_interface()
    print("✓ test_put_router_ospf6_interface passed")
    
    test_put_router_ospf6_passive_interface()
    print("✓ test_put_router_ospf6_passive_interface passed")
    
    test_put_router_ospf6_redistribute()
    print("✓ test_put_router_ospf6_redistribute passed")
    
    test_put_router_ospf6_summary()
    print("✓ test_put_router_ospf6_summary passed")
    
    test_put_router_ospf6_graceful_restart()
    print("✓ test_put_router_ospf6_graceful_restart passed")
    
    test_get_router_ospf6_verify()
    print("✓ test_get_router_ospf6_verify passed")

    cleanup()
    print("✓ All router/ospf6 tests passed")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
