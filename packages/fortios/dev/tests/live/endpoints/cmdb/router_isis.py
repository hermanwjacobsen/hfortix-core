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

# NOTE: IS-IS endpoint structure:
# - GET /router/isis - Get IS-IS configuration
# - PUT /router/isis - Update IS-IS configuration
# - No POST/DELETE (singleton resource)

def cleanup():
    """Cleanup IS-IS configuration after tests."""
    # Reset to minimal IS-IS configuration
    fgt.api.cmdb.router.isis.put(
        isis_net=[],
        isis_interface=[],
        summary_address=[],
        summary_address6=[],
        redistribute=[],
        redistribute6=[]
    )


def test_get_router_isis():
    """Test: Get IS-IS configuration"""
    result = fgt.api.cmdb.router.isis.get()
    assert result is not None
    assert result.http_status_code == 200


def test_put_router_isis_basic():
    """Test: Update basic IS-IS configuration"""
    result = fgt.api.cmdb.router.isis.put(
        is_type="level-1-2",
        dynamic_hostname="enable",
        adjacency_check="enable",
        metric_style="wide"
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_router_isis_with_net():
    """Test: Configure IS-IS NET (Network Entity Title)"""
    result = fgt.api.cmdb.router.isis.put(
        is_type="level-1-2",
        isis_net=[
            {
                "id": 1,
                "net": "49.0001.1921.6800.1001.00"
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_router_isis_with_interface():
    """Test: Configure IS-IS interface settings"""
    # Get current IS-IS configuration
    current_isis = fgt.api.cmdb.router.isis.get()
    
    # Use port3 for IS-IS interface testing
    test_interface = "port3"
    
    # Preserve existing NET configuration
    isis_net_list = []
    if hasattr(current_isis, 'isis_net') and current_isis.isis_net:
        isis_net_list = [{"id": net.id, "net": net.net} for net in current_isis.isis_net]
    elif not isis_net_list:
        # If no NET configured, add a default one
        isis_net_list = [{"id": 1, "net": "49.0001.1921.6800.1001.00"}]
    
    result = fgt.api.cmdb.router.isis.put(
        is_type="level-1-2",
        isis_net=isis_net_list,  # type: ignore
        isis_interface=[
            {
                "name": test_interface,
                "status": "enable",
                "network_type": "broadcast",
                "circuit_type": "level-1-2",
                "metric_l1": 10,
                "metric_l2": 10
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_router_isis_with_authentication():
    """Test: Configure IS-IS authentication"""
    result = fgt.api.cmdb.router.isis.put(
        is_type="level-1-2",
        auth_mode_l1="md5",
        auth_mode_l2="md5",
        auth_password_l1="test_password_l1",
        auth_password_l2="test_password_l2",
        auth_sendonly_l1="disable",
        auth_sendonly_l2="disable"
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_router_isis_with_timers():
    """Test: Configure IS-IS timers and intervals"""
    result = fgt.api.cmdb.router.isis.put(
        is_type="level-1-2",
        lsp_gen_interval_l1=10,
        lsp_gen_interval_l2=10,
        lsp_refresh_interval=900,
        max_lsp_lifetime=1200,
        spf_interval_exp_l1="1 50 50 50 50 50",
        spf_interval_exp_l2="1 50 50 50 50 50"
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_router_isis_with_redistribution():
    """Test: Configure IS-IS route redistribution"""
    result = fgt.api.cmdb.router.isis.put(
        is_type="level-1-2",
        redistribute_l1="enable",
        redistribute_l2="disable",
        redistribute=[
            {
                "protocol": "connected",
                "status": "enable",
                "metric": 10,
                "metric_type": "external",
                "level": "level-1-2"
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_router_isis_with_summary():
    """Test: Configure IS-IS summary addresses"""
    result = fgt.api.cmdb.router.isis.put(
        is_type="level-1-2",
        summary_address=[
            {
                "id": 1,
                "prefix": "10.0.0.0 255.0.0.0",
                "level": "level-1-2"
            }
        ],
        summary_address6=[
            {
                "id": 1,
                "prefix6": "2001:db8::/32",
                "level": "level-1-2"
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_router_isis_overload_bit():
    """Test: Configure IS-IS overload bit settings"""
    result = fgt.api.cmdb.router.isis.put(
        is_type="level-1-2",
        overload_bit="enable",
        overload_bit_suppress="external",
        overload_bit_on_startup=300
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_router_isis_ipv6():
    """Test: Configure IS-IS IPv6 settings"""
    result = fgt.api.cmdb.router.isis.put(
        is_type="level-1-2",
        adv_passive_only6="disable",
        adjacency_check6="enable",
        default_originate6="disable",
        redistribute6_l1="enable",
        redistribute6_l2="disable"
    )
    assert result is not None
    assert result.http_status == "success"


def test_get_router_isis_verify():
    """Test: Verify IS-IS configuration after updates"""
    result = fgt.api.cmdb.router.isis.get()
    assert result is not None
    assert result.http_status_code == 200
    # Verify some configured settings persist
    assert hasattr(result, "is_type")


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

    test_get_router_isis()
    print("✓ test_get_router_isis passed")
    
    test_put_router_isis_basic()
    print("✓ test_put_router_isis_basic passed")
    
    test_put_router_isis_with_net()
    print("✓ test_put_router_isis_with_net passed")
    
    test_put_router_isis_with_interface()
    print("✓ test_put_router_isis_with_interface passed")
    
    test_put_router_isis_with_authentication()
    print("✓ test_put_router_isis_with_authentication passed")
    
    test_put_router_isis_with_timers()
    print("✓ test_put_router_isis_with_timers passed")
    
    test_put_router_isis_with_redistribution()
    print("✓ test_put_router_isis_with_redistribution passed")
    
    test_put_router_isis_with_summary()
    print("✓ test_put_router_isis_with_summary passed")
    
    test_put_router_isis_overload_bit()
    print("✓ test_put_router_isis_overload_bit passed")
    
    test_put_router_isis_ipv6()
    print("✓ test_put_router_isis_ipv6 passed")
    
    test_get_router_isis_verify()
    print("✓ test_get_router_isis_verify passed")

    cleanup()
    print("✓ All router/isis tests passed")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
