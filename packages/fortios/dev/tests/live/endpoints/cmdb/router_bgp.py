import argparse
import sys
from pathlib import Path
from typing import TYPE_CHECKING
import hfortix_fortios
if TYPE_CHECKING:
    from hfortix_fortios.api.v2.cmdb.router.bgp import BgpNeighborItem


# Add project root to path
project_root = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(project_root))
from fgtclient import fgt


def cleanup():
    """Cleanup BGP configuration after tests."""
    fgt.api.cmdb.router.bgp.put(
        asn="0",
        router_id="0.0.0.0",
        neighbor=[],
        neighbor_group=[],
        neighbor_range=[],
        neighbor_range6= [],
    )
    fgt.api.cmdb.router.bgp.put(
        asn="0",
        router_id="0.0.0.0",
        neighbor=[],
        neighbor_group=[],
        neighbor_range=[],
        neighbor_range6= [],
    )
    ## need to run this twice to fully clear all fields ##

    verify = fgt.api.cmdb.router.bgp.get()
    assert str(verify.asn) == ""
    assert str(verify.router_id) == ""  
    assert verify.neighbor == []
    assert verify.neighbor_group == []
    assert verify.neighbor_range == []
    assert verify.neighbor_range6 == []



def test_get_router_bgp():
    """Test: Get BGP configuration."""
    result = fgt.api.cmdb.router.bgp.get()
    assert result is not None
    assert result.http_status_code == 200

def test_put_router_bgp_as():
    """Test: Update BGP AS number."""
    current_config = fgt.api.cmdb.router.bgp.get()

    original_asn = current_config.asn
    if str(original_asn) == "65001":
        new_asn = "65002"
    else:
        new_asn = "65001"

    update = fgt.api.cmdb.router.bgp.put(
        asn=new_asn,
        router_id="0.0.0.0"
    )
    verify = fgt.api.cmdb.router.bgp.get()
    assert str(verify.asn) == new_asn   

def test_put_router_bgp_router_id():
    """Test: Update BGP Router ID."""
    current_config = fgt.api.cmdb.router.bgp.get()

    original_router_id = current_config.router_id
    if str(original_router_id) == "1.1.1.1":
        new_router_id = "2.2.2.2"
    else:
        new_router_id = "1.1.1.1"
    update = fgt.api.cmdb.router.bgp.put(
        asn=str(current_config.asn),
        router_id=new_router_id
    )

    verify = fgt.api.cmdb.router.bgp.get()
    assert str(verify.router_id) == new_router_id

def test_put_router_bgp_neighbor():
    """Test: Update BGP Neighbor - Not implemented (part of BGP config structure)."""
    current_config = fgt.api.cmdb.router.bgp.get()
    result = fgt.api.cmdb.router.bgp.put(
        asn=str(current_config.asn),
        router_id=str(current_config.router_id),
        neighbor=[
            {
                "ip": "1.1.1.1",
                "remote_as": "65010",
                "activate": "enable",
                "allowas_in_enable": "enable",
                "allowas_in": 10,
                "description": "Test Neighbor 1",
                "next_hop_self": "enable",
                "route_map_in": "",
                "route_map_out": "",
                "soft_reconfiguration": "enable",
                "shutdown": "enable",
                "local_as": "65003",
                "restart_time": 300,
                "weight": 65535
            }
        ]
    )
    verify = fgt.api.cmdb.router.bgp.get()
    # Verification of neighbor addition would go here
    assert result is not None
    assert result.http_status == "success"
    for neighbor in verify.neighbor:
        if neighbor.get("ip") == "1.1.1.1":
            assert str(neighbor.get("remote_as")) == "65010"
            assert neighbor.get("activate") == "enable"
            assert str(neighbor.get("allowas_in")) == "10"
            assert neighbor.get("description") == "Test Neighbor 1"
            assert neighbor.get("next_hop_self") == "enable"
            assert neighbor.get("route_map_in") == ""
            assert neighbor.get("route_map_out") == ""
            assert neighbor.get("soft_reconfiguration") == "enable"
            assert neighbor.get("shutdown") == "enable"
            assert str(neighbor.get("local_as")) == "65003"
            assert str(neighbor.get("restart_time")) == "300"
            assert str(neighbor.get("weight")) == "65535"
            break
    else:
        assert False, "Neighbor with IP 1.1.1.1 not found"  

def test_put_router_bgp_second_neighbor():
    """Test: Update BGP Neighbor - Add second neighbor."""
    current_config = fgt.api.cmdb.router.bgp.get()
    
    # Convert existing neighbors to dict format for combining
    existing_neighbors = []
    if current_config.neighbor:
        for n in current_config.neighbor:
            # Convert neighbor object to dict
            neighbor_dict = dict(n) if hasattr(n, 'items') else n
            existing_neighbors.append(neighbor_dict)
    
        new_neighbor: BgpNeighborItem = {
        "ip": "2.2.2.2",
        "remote_as": "65020"
    }
    
    # Add new neighbor to existing list
    all_neighbors = existing_neighbors + [new_neighbor]

    result = fgt.api.cmdb.router.bgp.put(
        asn=str(current_config.asn),
        router_id=str(current_config.router_id),
        neighbor=all_neighbors  
    )   
    verify = fgt.api.cmdb.router.bgp.get()
    assert result is not None
    assert result.http_status == "success"
    
    # Verify the second neighbor was added
    assert len(verify.neighbor) == len(existing_neighbors) + 1
    found_second = False
    for neighbor in verify.neighbor:
        if neighbor.ip == "1.1.1.1":
            first_found = True
        if neighbor.get("ip") == "2.2.2.2":
            found_second = True
    
    assert first_found, "First neighbor with IP 1.1.1.1 not found"        
    assert found_second, "Second neighbor with IP 2.2.2.2 not found"

def test_put_neighbor_group():
    """Test: Update BGP Neighbor Group - Not implemented (part of BGP config structure)."""
    result = fgt.api.cmdb.router.bgp.put(
        neighbor_group=[
            {
                "name": "test_group1",
                "remote_as": "65100",
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"
    verify = fgt.api.cmdb.router.bgp.get()
    found = False
    for group in verify.neighbor_group:
        if group.name == "test_group1":
            assert str(group.get("remote_as")) == "65100"
            found = True
            break
    assert found, "Neighbor group test_group1 not found"

def test_put_neighbor_range():
    """Test: Update BGP Neighbor Range - Not implemented (part of BGP config structure)."""
    result = fgt.api.cmdb.router.bgp.put(
        neighbor_range=[
            {
                "prefix": "192.168.1.0/24",
                "neighbor_group": "test_group1"
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"
    verify = fgt.api.cmdb.router.bgp.get()
    for range in verify.neighbor_range:
        if range.prefix == "192.168.1.0 255.255.255.0":
            assert str(range.get("neighbor_group")) == "test_group1"
            break
    else:
        assert False, "Neighbor range not found"    



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

    test_get_router_bgp()
    print("✓ test_get_router_bgp passed")
    
    test_put_router_bgp_as()    
    print("✓ test_put_router_bgp_as passed")
    
    test_put_router_bgp_router_id()
    print("✓ test_put_router_bgp_router_id passed")

    test_put_router_bgp_neighbor()
    print("✓ test_put_router_bgp_neighbor passed")

    test_put_router_bgp_second_neighbor()
    print("✓ test_put_router_bgp_second_neighbor passed")

    test_put_neighbor_group()
    print("✓ test_put_neighbor_group passed")

    test_put_neighbor_range()
    print("✓ test_put_neighbor_range passed")

    print("\n✓ All router/bgp tests passed")

    cleanup()
    print("✓ Post-Cleanup passed")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
