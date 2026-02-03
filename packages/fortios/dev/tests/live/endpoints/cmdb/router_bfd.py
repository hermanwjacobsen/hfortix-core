import argparse
import sys
from pathlib import Path
from ipaddress import ip_address, IPv4Network


# Add project root to path
project_root = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(project_root))
from fgtclient import fgt


# NOTE: BFD (Bidirectional Forwarding Detection) endpoint structure:
# - GET /router/bfd - Get BFD configuration (neighbors and multihop-templates)
# - PUT /router/bfd - Update BFD configuration
# - No POST/DELETE for individual neighbors (part of BFD config structure)

def cleanup():
    """Cleanup BFD configuration after tests."""
    fgt.api.cmdb.router.bfd.put(
        neighbor=[],
        multihop_template=[]
    )
    verify = fgt.api.cmdb.router.bfd.get()
    assert len(verify.neighbor) == 0
    assert len(verify.multihop_template) == 0
    


def test_get_router_bfd():
    """Test: Get BFD configuration."""
    result = fgt.api.cmdb.router.bfd.get()
    assert result is not None
    assert result.http_status_code == 200
    # BFD config may be empty if not configured
    # Check for expected structure (neighbor and multihop-template lists)
    assert hasattr(result, "neighbor") or hasattr(result, "multihop_template")


# This will validate all fields
def test_put_router_bfd():
    """Test: Update BFD configuration - full config."""
    get_interface = fgt.api.cmdb.system.interface.get(vdom="test")
    
    found_ip = None
    found_intf = None
    
    for intf in get_interface:
        if intf.name.startswith("port"):
            if hasattr(intf, 'ip') and intf.ip:
                # IP field contains "IP NETMASK", so split to get just the IP
                ip_only = intf.ip.split()[0]
                if ip_only != "0.0.0.0" and ip_address(ip_only).is_private:
                    found_ip = intf.ip
                    found_intf = intf.name
                    break
    
    if not found_ip:
        raise AssertionError("No suitable interface with private IP found for BFD neighbor test")

    # Calculate another IP in the same subnet
    ip_only = found_ip.split()[0]
    netmask = found_ip.split()[1]
    network = IPv4Network(f"{ip_only}/{netmask}", strict=False)
    
    # Get another IP in the subnet (not the network or broadcast address)
    other_ip = None
    for host in network.hosts():
        if str(host) != ip_only:
            other_ip = str(host)
            break
    
    if not other_ip:
        raise AssertionError(f"Could not find another IP in subnet {network}")
    
    assert found_intf is not None, "Interface name should not be None"
    
    result = fgt.api.cmdb.router.bfd.put(
        neighbor=[
            {
                "ip": other_ip, 
                "interface": found_intf
            }
        ]
    )
    verify = fgt.api.cmdb.router.bfd.get()
    assert result is not None
    assert result.http_status == "success"
    # Verify the update
    assert len(verify.neighbor) == 1
    assert verify.neighbor[0].get("ip") == other_ip
    assert verify.neighbor[0].get("interface") == found_intf


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

    test_get_router_bfd()
    print("✓ test_get_router_bfd passed")
    
    test_put_router_bfd()
    print("✓ test_put_router_bfd passed")
    
    cleanup()
    print("✓ Post-Cleanup passed")

    print("\n✓ All router/bfd tests passed")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
