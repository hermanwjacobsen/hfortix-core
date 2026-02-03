import argparse
import sys
from pathlib import Path
from ipaddress import ip_address, IPv6Network


# Add project root to path
project_root = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(project_root))
from fgtclient import fgt


# NOTE: BFD6 (IPv6 Bidirectional Forwarding Detection) endpoint structure:
# - GET /router/bfd6 - Get IPv6 BFD configuration (neighbors and multihop-templates)
# - PUT /router/bfd6 - Update IPv6 BFD configuration
# - No POST/DELETE for individual neighbors (part of BFD6 config structure)

def cleanup():
    """Cleanup IPv6 BFD configuration after tests."""
    fgt.api.cmdb.router.bfd6.put(
        neighbor=[],
        multihop_template=[]
    )
    verify = fgt.api.cmdb.router.bfd6.get()
    assert len(verify.neighbor) == 0
    assert len(verify.multihop_template) == 0
    


def test_get_router_bfd6():
    """Test: Get IPv6 BFD configuration."""
    result = fgt.api.cmdb.router.bfd6.get()
    assert result is not None
    assert result.http_status_code == 200
    # BFD6 config may be empty if not configured
    # Check for expected structure (neighbor and multihop-template lists)
    assert hasattr(result, "neighbor") or hasattr(result, "multihop_template")


def test_put_router_bfd6():
    """Test: Update IPv6 BFD configuration - simplified test."""
    
    # Use a simple, known-good test configuration
    # BFD6 expects valid IPv6 addresses that could be BFD neighbors
    interfaces = fgt.api.cmdb.system.interface.get()
    test_ipv6 = None
    test_interface = None
    for intf in interfaces:
        if intf.ipv6.ip6_address != "::/0":
            ip_only = intf.ipv6.ip6_address.split('/')[0]
            if ip_address(ip_only).is_private:
                test_ipv6 = str(ip_address(ip_only) + 1)  # Next IP in subnet
                test_interface = intf.name
                break
    
    # Ensure we found a valid interface with IPv6
    assert test_ipv6 is not None, "No interface with private IPv6 address found"
    assert test_interface is not None, "No suitable interface found"

    result = fgt.api.cmdb.router.bfd6.put(
        neighbor=[
            {
                "ip6_address": test_ipv6,  # API uses hyphen, not underscore
                "interface": test_interface
            }
        ]
    )
    
    assert result is not None
    assert result.http_status == "success"
    
    # Verify the configuration
    verify = fgt.api.cmdb.router.bfd6.get()
    assert len(verify.neighbor) == 1
    assert verify.neighbor[0].get("ip6_address") == test_ipv6
    assert verify.neighbor[0].get("interface") == test_interface




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

    test_get_router_bfd6()
    print("✓ test_get_router_bfd6 passed")
    
    test_put_router_bfd6()
    print("✓ test_put_router_bfd6 passed")
    
    cleanup()
    print("✓ Post-Cleanup passed")

    print("\n✓ All router/bfd6 tests passed")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
