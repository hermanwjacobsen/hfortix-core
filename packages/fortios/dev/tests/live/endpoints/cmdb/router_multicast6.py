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

# NOTE: Multicast6 endpoint structure:
# - GET /router/multicast6 - Get IPv6 multicast configuration
# - PUT /router/multicast6 - Update IPv6 multicast configuration
# - No POST/DELETE (singleton resource)

def cleanup():
    """Cleanup IPv6 multicast configuration after tests."""
    fgt.api.cmdb.router.multicast6.put(
        multicast_routing="disable",
        interface=[],
        pim_sm_global={}
    )


def test_get_router_multicast6():
    """Test: Get IPv6 multicast configuration"""
    result = fgt.api.cmdb.router.multicast6.get()
    assert result is not None
    assert result.http_status_code == 200


def test_put_router_multicast6_enable():
    """Test: Enable IPv6 multicast routing"""
    result = fgt.api.cmdb.router.multicast6.put(
        multicast_routing="enable"
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_router_multicast6_pmtu():
    """Test: Configure IPv6 multicast PMTU"""
    result = fgt.api.cmdb.router.multicast6.put(
        multicast_routing="enable",
        multicast_pmtu="enable"
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_router_multicast6_interface():
    """Test: Configure PIM on IPv6 interface"""
    result = fgt.api.cmdb.router.multicast6.put(
        multicast_routing="enable",
        interface=[
            {
                "name": "port3",
                "hello_interval": 30,
                "hello_holdtime": 105
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_router_multicast6_pim_global():
    """Test: Configure IPv6 PIM sparse-mode global settings"""
    result = fgt.api.cmdb.router.multicast6.put(
        multicast_routing="enable",
        pim_sm_global={
            "register_rate_limit": 0
        }
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_router_multicast6_rp_address():
    """Test: Configure IPv6 PIM RP address"""
    result = fgt.api.cmdb.router.multicast6.put(
        multicast_routing="enable",
        pim_sm_global={
            "rp_address": [
                {
                    "id": 1,
                    "ip6_address": "fd12:3456:789a:1::100"
                }
            ]
        }
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_router_multicast6_combined():
    """Test: Configure IPv6 multicast with interface and PIM settings"""
    result = fgt.api.cmdb.router.multicast6.put(
        multicast_routing="enable",
        multicast_pmtu="enable",
        interface=[
            {
                "name": "port3",
                "hello_interval": 30,
                "hello_holdtime": 105
            }
        ],
        pim_sm_global={
            "register_rate_limit": 0
        }
    )
    assert result is not None
    assert result.http_status == "success"


def test_get_router_multicast6_verify():
    """Test: Verify IPv6 multicast configuration"""
    result = fgt.api.cmdb.router.multicast6.get()
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

    test_get_router_multicast6()
    print("✓ test_get_router_multicast6 passed")
    
    test_put_router_multicast6_enable()
    print("✓ test_put_router_multicast6_enable passed")
    
    test_put_router_multicast6_pmtu()
    print("✓ test_put_router_multicast6_pmtu passed")
    
    test_put_router_multicast6_interface()
    print("✓ test_put_router_multicast6_interface passed")
    
    test_put_router_multicast6_pim_global()
    print("✓ test_put_router_multicast6_pim_global passed")
    
    test_put_router_multicast6_rp_address()
    print("✓ test_put_router_multicast6_rp_address passed")
    
    test_put_router_multicast6_combined()
    print("✓ test_put_router_multicast6_combined passed")
    
    test_get_router_multicast6_verify()
    print("✓ test_get_router_multicast6_verify passed")

    cleanup()
    print("✓ All router/multicast6 tests passed")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
