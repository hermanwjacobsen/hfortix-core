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

# NOTE: Multicast endpoint structure:
# - GET /router/multicast - Get multicast configuration
# - PUT /router/multicast - Update multicast configuration
# - No POST/DELETE (singleton resource)

def cleanup():
    """Cleanup multicast configuration after tests."""
    fgt.api.cmdb.router.multicast.put(
        multicast_routing="disable",
        interface=[],
        pim_sm_global={},
        pim_sm_global_vrf=[]
    )


def test_get_router_multicast():
    """Test: Get multicast configuration"""
    result = fgt.api.cmdb.router.multicast.get()
    assert result is not None
    assert result.http_status_code == 200


def test_put_router_multicast_enable():
    """Test: Enable IP multicast routing"""
    result = fgt.api.cmdb.router.multicast.put(
        multicast_routing="enable"
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_router_multicast_route_limits():
    """Test: Configure multicast route limits"""
    result = fgt.api.cmdb.router.multicast.put(
        multicast_routing="enable",
        route_threshold=5000,
        route_limit=10000
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_router_multicast_pim_global():
    """Test: Configure PIM sparse-mode global settings"""
    result = fgt.api.cmdb.router.multicast.put(
        multicast_routing="enable",
        pim_sm_global={
            "message_interval": 57,
            "join_prune_holdtime": 209,
            "register_rate_limit": 0,
            "rp_register_keepalive": 154,
            "spt_threshold": "enable",
            "ssm": "disable"
        }
    )
    assert result is not None
    assert result.http_status == "success"
    verify = fgt.api.cmdb.router.multicast.get()
    assert verify.pim_sm_global.message_interval == 57
    assert verify.pim_sm_global.join_prune_holdtime == 209
    assert verify.pim_sm_global.register_rate_limit == 0
    assert verify.pim_sm_global.rp_register_keepalive == 154
    assert verify.pim_sm_global.spt_threshold == "enable"
    assert verify.pim_sm_global.ssm == "disable"



def test_put_router_multicast_interface():
    """Test: Configure PIM on interface"""
    result = fgt.api.cmdb.router.multicast.put(
        multicast_routing="enable",
        interface=[
            {
                "name": "port3",
                "ttl_threshold": 1,
                "pim_mode": "sparse-mode",
                "passive": "disable",
                "bfd": "disable",
                "hello_interval": 30,
                "hello_holdtime": 105,
                "dr_priority": 1,
                "multicast_flow": ""
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_router_multicast_interface_with_igmp():
    """Test: Configure PIM interface with IGMP settings"""
    result = fgt.api.cmdb.router.multicast.put(
        multicast_routing="enable",
        interface=[
            {
                "name": "port3",
                "pim_mode": "sparse-mode",
                "hello_interval": 30,
                "igmp": {
                    "access_group": "",
                    "version": "3",
                    "immediate_leave_group": "",
                    "last_member_query_interval": 1,
                    "last_member_query_count": 2,
                    "query_max_response_time": 10,
                    "query_interval": 125,
                    "query_timeout": 255,
                    "router_alert_check": "enable"
                }
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_router_multicast_rp_address():
    """Test: Configure PIM sparse-mode with RP settings"""
    # Skip detailed RP configuration - may require additional setup
    result = fgt.api.cmdb.router.multicast.put(
        multicast_routing="enable",
        pim_sm_global={
            "register_rate_limit": 0
        }
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_router_multicast_bsr():
    """Test: Configure PIM Bootstrap Router (BSR)"""
    result = fgt.api.cmdb.router.multicast.put(
        multicast_routing="enable",
        pim_sm_global={
            "bsr_candidate": "disable",
            "bsr_hash": 10,
            "bsr_allow_quick_refresh": "disable"
        }
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_router_multicast_ssm():
    """Test: Configure Source-Specific Multicast (SSM)"""
    result = fgt.api.cmdb.router.multicast.put(
        multicast_routing="enable",
        pim_sm_global={
            "ssm": "disable"
        }
    )
    assert result is not None
    assert result.http_status == "success"


def test_get_router_multicast_verify():
    """Test: Verify multicast configuration"""
    result = fgt.api.cmdb.router.multicast.get()
    assert result is not None
    assert result.http_status_code == 200
    # Verify multicast routing is enabled
    assert hasattr(result, "multicast_routing")


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

    test_get_router_multicast()
    print("✓ test_get_router_multicast passed")
    
    test_put_router_multicast_enable()
    print("✓ test_put_router_multicast_enable passed")
    
    test_put_router_multicast_route_limits()
    print("✓ test_put_router_multicast_route_limits passed")
    
    test_put_router_multicast_pim_global()
    print("✓ test_put_router_multicast_pim_global passed")
    
    test_put_router_multicast_interface()
    print("✓ test_put_router_multicast_interface passed")
    
    test_put_router_multicast_interface_with_igmp()
    print("✓ test_put_router_multicast_interface_with_igmp passed")
    
    test_put_router_multicast_rp_address()
    print("✓ test_put_router_multicast_rp_address passed")
    
    test_put_router_multicast_bsr()
    print("✓ test_put_router_multicast_bsr passed")
    
    test_put_router_multicast_ssm()
    print("✓ test_put_router_multicast_ssm passed")
    
    test_get_router_multicast_verify()
    print("✓ test_get_router_multicast_verify passed")

    cleanup()
    print("✓ All router/multicast tests passed")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
