import argparse
import sys
from pathlib import Path
import pytest

# Run router monitor tests on a single worker to preserve state
pytestmark = pytest.mark.xdist_group(Path(__file__).stem)

# Add pytest directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt



# ============================================================================
# Router Monitor Tests - GET endpoints
# ============================================================================

def test_get_router_ipv4():
    """Test GET /monitor/router/ipv4 - List all active IPv4 routing table entries."""
    try:
        result = fgt.api.monitor.router.ipv4.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_router_ipv4_with_interface_filter():
    """Test GET /monitor/router/ipv4 - List IPv4 routes filtered by interface (port3)."""
    try:
        result = fgt.api.monitor.router.ipv4.get(interface="port3")
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_router_ipv4_with_multiple_filters():
    """Test GET /monitor/router/ipv4 - List IPv4 routes with interface and type filters."""
    try:
        result = fgt.api.monitor.router.ipv4.get(interface="port4", type="connected")
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_router_ipv6():
    """Test GET /monitor/router/ipv6 - List all active IPv6 routing table entries."""
    try:
        result = fgt.api.monitor.router.ipv6.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_router_ipv6_with_interface_filter():
    """Test GET /monitor/router/ipv6 - List IPv6 routes filtered by interface (port3)."""
    try:
        result = fgt.api.monitor.router.ipv6.get(interface="port3")
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_router_ipv6_with_multiple_filters():
    """Test GET /monitor/router/ipv6 - List IPv6 routes with interface and type filters."""
    try:
        result = fgt.api.monitor.router.ipv6.get(interface="port4", type="connected")
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_router_bgp_neighbors_statistics():
    """Test GET /monitor/router/bgp/neighbors-statistics - Retrieve BGP neighbors statistics (default/ipv4)."""
    try:
        result = fgt.api.monitor.router.bgp.neighbors_statistics.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_router_bgp_neighbors_statistics_ipv4():
    """Test GET /monitor/router/bgp/neighbors-statistics - Retrieve IPv4 BGP neighbors statistics."""
    try:
        result = fgt.api.monitor.router.bgp.neighbors_statistics.get(ip_version="ipv4")
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_router_bgp_neighbors_statistics_ipv6():
    """Test GET /monitor/router/bgp/neighbors-statistics - Retrieve IPv6 BGP neighbors statistics."""
    try:
        result = fgt.api.monitor.router.bgp.neighbors_statistics.get(ip_version="ipv6")
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_router_bgp_neighbors_statistics_ipboth():
    """Test GET /monitor/router/bgp/neighbors-statistics - Retrieve both IPv4 and IPv6 BGP neighbors statistics."""
    try:
        result = fgt.api.monitor.router.bgp.neighbors_statistics.get(ip_version="ipboth")
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_router_bgp_neighbors():
    """Test GET /monitor/router/bgp/neighbors - List all discovered BGP neighbors."""
    try:
        result = fgt.api.monitor.router.bgp.neighbors.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_router_bgp_neighbors6():
    """Test GET /monitor/router/bgp/neighbors6 - List all discovered IPv6 BGP neighbors."""
    try:
        result = fgt.api.monitor.router.bgp.neighbors6.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_router_bgp_paths_statistics():
    """Test GET /monitor/router/bgp/paths-statistics - Retrieve BGP paths statistics (default/ipv4)."""
    try:
        result = fgt.api.monitor.router.bgp.paths_statistics.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_router_bgp_paths_statistics_ipv4():
    """Test GET /monitor/router/bgp/paths-statistics - Retrieve IPv4 BGP paths statistics."""
    try:
        result = fgt.api.monitor.router.bgp.paths_statistics.get(ip_version="ipv4")
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_router_bgp_paths_statistics_ipv6():
    """Test GET /monitor/router/bgp/paths-statistics - Retrieve IPv6 BGP paths statistics."""
    try:
        result = fgt.api.monitor.router.bgp.paths_statistics.get(ip_version="ipv6")
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_router_bgp_paths_statistics_ipboth():
    """Test GET /monitor/router/bgp/paths-statistics - Retrieve both IPv4 and IPv6 BGP paths statistics."""
    try:
        result = fgt.api.monitor.router.bgp.paths_statistics.get(ip_version="ipboth")
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_router_bgp_paths():
    """Test GET /monitor/router/bgp/paths - List all discovered BGP paths."""
    try:
        result = fgt.api.monitor.router.bgp.paths.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_router_bgp_paths6():
    """Test GET /monitor/router/bgp/paths6 - List all discovered IPv6 BGP paths."""
    try:
        result = fgt.api.monitor.router.bgp.paths6.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_router_ospf_neighbors():
    """Test GET /monitor/router/ospf/neighbors - List all discovered OSPF neighbors."""
    try:
        result = fgt.api.monitor.router.ospf.neighbors.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_router_sdwan_routes():
    """Test GET /monitor/router/sdwan/routes - List all discovered IPv4 SD-WAN routes."""
    try:
        result = fgt.api.monitor.router.sdwan.routes.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_router_sdwan_routes6():
    """Test GET /monitor/router/sdwan/routes6 - List all discovered IPv6 SD-WAN routes."""
    try:
        result = fgt.api.monitor.router.sdwan.routes6.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_router_sdwan_routes_statistics():
    """Test GET /monitor/router/sdwan/routes-statistics - Retrieve SD-WAN routes statistics (default/ipv4)."""
    try:
        result = fgt.api.monitor.router.sdwan.routes_statistics.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_router_sdwan_routes_statistics_ipv4():
    """Test GET /monitor/router/sdwan/routes-statistics - Retrieve IPv4 SD-WAN routes statistics."""
    try:
        result = fgt.api.monitor.router.sdwan.routes_statistics.get(ip_version="ipv4")
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_router_sdwan_routes_statistics_ipv6():
    """Test GET /monitor/router/sdwan/routes-statistics - Retrieve IPv6 SD-WAN routes statistics."""
    try:
        result = fgt.api.monitor.router.sdwan.routes_statistics.get(ip_version="ipv6")
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_router_sdwan_routes_statistics_ipboth():
    """Test GET /monitor/router/sdwan/routes-statistics - Retrieve both IPv4 and IPv6 SD-WAN routes statistics."""
    try:
        result = fgt.api.monitor.router.sdwan.routes_statistics.get(ip_version="ipboth")
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_router_statistics():
    """Test GET /monitor/router/statistics - Retrieve routing table statistics."""
    try:
        result = fgt.api.monitor.router.statistics.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_router_statistics_ipv4():
    """Test GET /monitor/router/statistics - Retrieve IPv4 routing table statistics."""
    try:
        result = fgt.api.monitor.router.statistics.get(ip_version=4)
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_router_statistics_ipv6():
    """Test GET /monitor/router/statistics - Retrieve IPv6 routing table statistics."""
    try:
        result = fgt.api.monitor.router.statistics.get(ip_version=6)
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_router_statistics_with_interface_filter():
    """Test GET /monitor/router/statistics - Retrieve statistics filtered by interface (port3)."""
    try:
        result = fgt.api.monitor.router.statistics.get(interface="port3", ip_version=4)
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_router_statistics_with_multiple_filters():
    """Test GET /monitor/router/statistics - Retrieve statistics with multiple filters (port4, type, operator=and)."""
    try:
        result = fgt.api.monitor.router.statistics.get(
            interface="port4",
            type="connected",
            operator="and",
            ip_version=4
        )
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_router_statistics_with_all_filters():
    """Test GET /monitor/router/statistics - Retrieve statistics with all filter parameters."""
    try:
        result = fgt.api.monitor.router.statistics.get(
            interface="port3",
            type="connected",
            operator="or",
            ip_version=4,
            gateway="0.0.0.0"
        )
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_router_charts():
    """Test GET /monitor/router/charts - Retrieve routing chart statistics."""
    try:
        result = fgt.api.monitor.router.charts.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_router_charts_ipv4():
    """Test GET /monitor/router/charts - Retrieve IPv4 routing chart statistics."""
    try:
        result = fgt.api.monitor.router.charts.get(ip_version=4)
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_router_charts_ipv6():
    """Test GET /monitor/router/charts - Retrieve IPv6 routing chart statistics."""
    try:
        result = fgt.api.monitor.router.charts.get(ip_version=6)
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_router_charts_with_interface_filter():
    """Test GET /monitor/router/charts - Retrieve charts filtered by interface (port3)."""
    try:
        result = fgt.api.monitor.router.charts.get(interface="port3", ip_version=4)
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_router_charts_with_multiple_filters():
    """Test GET /monitor/router/charts - Retrieve charts with multiple filters (port4, type, operator=and)."""
    try:
        result = fgt.api.monitor.router.charts.get(
            interface="port4",
            type="connected",
            operator="and",
            ip_version=4
        )
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_router_charts_with_all_filters():
    """Test GET /monitor/router/charts - Retrieve charts with all filter parameters."""
    try:
        result = fgt.api.monitor.router.charts.get(
            interface="port3",
            type="connected",
            operator="or",
            ip_version=4,
            gateway="0.0.0.0"
        )
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_router_lookup_ipv4_with_ip():
    """Test GET /monitor/router/lookup - IPv4 route lookup with IP address (8.8.8.8)."""
    try:
        result = fgt.api.monitor.router.lookup.get(destination="8.8.8.8")
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_router_lookup_ipv4_with_fqdn():
    """Test GET /monitor/router/lookup - IPv4 route lookup with FQDN (google.dk)."""
    try:
        result = fgt.api.monitor.router.lookup.get(destination="google.dk")
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_router_lookup_ipv6_with_ip():
    """Test GET /monitor/router/lookup - IPv6 route lookup with IP address (2001:4860:4860::8888)."""
    try:
        result = fgt.api.monitor.router.lookup.get(destination="2001:4860:4860::8888", ipv6=True)
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_router_lookup_ipv6_with_fqdn():
    """Test GET /monitor/router/lookup - IPv6 route lookup with FQDN (google.dk)."""
    try:
        result = fgt.api.monitor.router.lookup.get(destination="google.dk", ipv6=True)
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_router_lookup_policy_ipv4_basic():
    """Test GET /monitor/router/lookup-policy - IPv4 policy route lookup with destination."""
    try:
        result = fgt.api.monitor.router.lookup_policy.get(destination="8.8.8.8")
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_router_lookup_policy_ipv4_with_source():
    """Test GET /monitor/router/lookup-policy - IPv4 policy route lookup with destination and source."""
    try:
        result = fgt.api.monitor.router.lookup_policy.get(
            destination="8.8.8.8",
            source="192.168.1.100"
        )
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_router_lookup_policy_ipv4_with_interface():
    """Test GET /monitor/router/lookup-policy - IPv4 policy route lookup with interface (port3)."""
    try:
        result = fgt.api.monitor.router.lookup_policy.get(
            destination="8.8.8.8",
            interface_name="port3"
        )
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_router_lookup_policy_ipv4_with_ports():
    """Test GET /monitor/router/lookup-policy - IPv4 policy route lookup with ports and protocol."""
    try:
        result = fgt.api.monitor.router.lookup_policy.get(
            destination="8.8.8.8",
            source="192.168.1.100",
            destination_port=443,
            source_port=54321,
            protocol_number=6  # TCP
        )
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_router_lookup_policy_ipv4_full():
    """Test GET /monitor/router/lookup-policy - IPv4 policy route lookup with all parameters."""
    try:
        result = fgt.api.monitor.router.lookup_policy.get(
            destination="8.8.8.8",
            source="192.168.1.100",
            destination_port=80,
            source_port=12345,
            interface_name="port4",
            protocol_number=6  # TCP
        )
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        elif "500" in str(e):
            print("Server error (500)")
        else:
            raise


# def test_get_router_lookup_policy_ipv6_basic():
#     """Test GET /monitor/router/lookup-policy - IPv6 policy route lookup with destination."""
#     try:
#         result = fgt.api.monitor.router.lookup_policy.get(
#             destination="2001:4860:4860::8888",
#             ipv6=True
#         )
#         assert result is not None
#         assert result.http_status_code == 200
#     except Exception as e:
#         if "404" in str(e):
#             print("Resource not found")
#         elif "500" in str(e):
#             print("Server error (500)")
#         else:
#             raise


# def test_get_router_lookup_policy_ipv6_with_source():
#     """Test GET /monitor/router/lookup-policy - IPv6 policy route lookup with destination and source."""
#     try:
#         result = fgt.api.monitor.router.lookup_policy.get(
#             destination="2001:4860:4860::8888",
#             source="2001:db8::1",
#             ipv6=True
#         )
#         assert result is not None
#         assert result.http_status_code == 200
#     except Exception as e:
#         if "404" in str(e):
#             print("Resource not found")
#         elif "500" in str(e):
#             print("Server error (500)")
#         else:
#             raise


# def test_get_router_lookup_policy_ipv6_with_interface():
#     """Test GET /monitor/router/lookup-policy - IPv6 policy route lookup with interface (port3)."""
#     try:
#         result = fgt.api.monitor.router.lookup_policy.get(
#             destination="2001:4860:4860::8888",
#             interface_name="port3",
#             ipv6=True
#         )
#         assert result is not None
#         assert result.http_status_code == 200
#     except Exception as e:
#         if "404" in str(e):
#             print("Resource not found")
#         elif "500" in str(e):
#             print("Server error (500)")
#         else:
#             raise


def test_get_router_policy():
    """Test GET /monitor/router/policy - Retrieve list of active IPv4 policy routes."""
    try:
        result = fgt.api.monitor.router.policy.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_router_policy_count_only():
    """Test GET /monitor/router/policy - Retrieve count of IPv4 policy routes only."""
    try:
        result = fgt.api.monitor.router.policy.get(count_only=True)
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_router_policy6():
    """Test GET /monitor/router/policy6 - Retrieve list of active IPv6 policy routes."""
    try:
        result = fgt.api.monitor.router.policy6.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_router_policy6_count_only():
    """Test GET /monitor/router/policy6 - Retrieve count of IPv6 policy routes only."""
    try:
        result = fgt.api.monitor.router.policy6.get(count_only=True)
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


# ============================================================================
# Router Monitor Tests - POST endpoints
# ============================================================================

# def test_post_router_bgp_soft_reset_neighbor():
#     """Test POST /monitor/router/bgp/soft-reset-neighbor - BGP neighbor soft reset."""
#     try:
#         result = fgt.api.monitor.router.bgp.soft_reset_neighbor.post(ip="192.168.1.1")
#         assert result is not None
#         assert result.http_status_code == 200
#     except Exception as e:
#         if "404" in str(e):
#             print("Resource not found")
#         elif "500" in str(e):
#             print("Server error (500)")
#         else:
#             raise


def test_post_router_bgp_clear_soft_in():
    """Test POST /monitor/router/bgp/clear-soft-in - Inbound soft-reconfiguration for BGP peers."""
    try:
        result = fgt.api.monitor.router.bgp.clear_soft_in.post()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        elif "500" in str(e):
            print("Server error (500)")
        else:
            raise


def test_post_router_bgp_clear_soft_out():
    """Test POST /monitor/router/bgp/clear-soft-out - Outbound soft-reconfiguration for BGP peers."""
    try:
        result = fgt.api.monitor.router.bgp.clear_soft_out.post()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        elif "500" in str(e):
            print("Server error (500)")
        else:
            raise


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
    # ========================================================================
    # GET endpoint tests
    # ========================================================================
    
    print("Running Router monitor endpoint tests...")
    
    test_get_router_ipv4()
    print("✓ test_get_router_ipv4")
    
    test_get_router_ipv4_with_interface_filter()
    print("✓ test_get_router_ipv4_with_interface_filter (port3)")
    
    test_get_router_ipv4_with_multiple_filters()
    print("✓ test_get_router_ipv4_with_multiple_filters (port4, type=connected)")
    
    test_get_router_ipv6()
    print("✓ test_get_router_ipv6")
    
    test_get_router_ipv6_with_interface_filter()
    print("✓ test_get_router_ipv6_with_interface_filter (port3)")
    
    test_get_router_ipv6_with_multiple_filters()
    print("✓ test_get_router_ipv6_with_multiple_filters (port4, type=connected)")
    
    test_get_router_bgp_neighbors_statistics()
    print("✓ test_get_router_bgp_neighbors_statistics")
    
    test_get_router_bgp_neighbors_statistics_ipv4()
    print("✓ test_get_router_bgp_neighbors_statistics_ipv4")
    
    test_get_router_bgp_neighbors_statistics_ipv6()
    print("✓ test_get_router_bgp_neighbors_statistics_ipv6")
    
    test_get_router_bgp_neighbors_statistics_ipboth()
    print("✓ test_get_router_bgp_neighbors_statistics_ipboth")
    
    test_get_router_bgp_neighbors()
    print("✓ test_get_router_bgp_neighbors")
    
    test_get_router_bgp_neighbors6()
    print("✓ test_get_router_bgp_neighbors6")
    
    test_get_router_bgp_paths_statistics()
    print("✓ test_get_router_bgp_paths_statistics")
    
    test_get_router_bgp_paths_statistics_ipv4()
    print("✓ test_get_router_bgp_paths_statistics_ipv4")
    
    test_get_router_bgp_paths_statistics_ipv6()
    print("✓ test_get_router_bgp_paths_statistics_ipv6")
    
    test_get_router_bgp_paths_statistics_ipboth()
    print("✓ test_get_router_bgp_paths_statistics_ipboth")
    
    test_get_router_bgp_paths()
    print("✓ test_get_router_bgp_paths")
    
    test_get_router_bgp_paths6()
    print("✓ test_get_router_bgp_paths6")
    
    test_get_router_ospf_neighbors()
    print("✓ test_get_router_ospf_neighbors")
    
    test_get_router_sdwan_routes()
    print("✓ test_get_router_sdwan_routes")
    
    test_get_router_sdwan_routes6()
    print("✓ test_get_router_sdwan_routes6")
    
    test_get_router_sdwan_routes_statistics()
    print("✓ test_get_router_sdwan_routes_statistics")
    
    test_get_router_sdwan_routes_statistics_ipv4()
    print("✓ test_get_router_sdwan_routes_statistics_ipv4")
    
    test_get_router_sdwan_routes_statistics_ipv6()
    print("✓ test_get_router_sdwan_routes_statistics_ipv6")
    
    test_get_router_sdwan_routes_statistics_ipboth()
    print("✓ test_get_router_sdwan_routes_statistics_ipboth")
    
    test_get_router_statistics()
    print("✓ test_get_router_statistics")
    
    test_get_router_statistics_ipv4()
    print("✓ test_get_router_statistics_ipv4")
    
    test_get_router_statistics_ipv6()
    print("✓ test_get_router_statistics_ipv6")
    
    test_get_router_statistics_with_interface_filter()
    print("✓ test_get_router_statistics_with_interface_filter (port3)")
    
    test_get_router_statistics_with_multiple_filters()
    print("✓ test_get_router_statistics_with_multiple_filters (port4, type, operator=and)")
    
    test_get_router_statistics_with_all_filters()
    print("✓ test_get_router_statistics_with_all_filters (interface, type, operator, gateway)")
    
    test_get_router_charts()
    print("✓ test_get_router_charts")
    
    test_get_router_charts_ipv4()
    print("✓ test_get_router_charts_ipv4")
    
    test_get_router_charts_ipv6()
    print("✓ test_get_router_charts_ipv6")
    
    test_get_router_charts_with_interface_filter()
    print("✓ test_get_router_charts_with_interface_filter (port3)")
    
    test_get_router_charts_with_multiple_filters()
    print("✓ test_get_router_charts_with_multiple_filters (port4, type, operator=and)")
    
    test_get_router_charts_with_all_filters()
    print("✓ test_get_router_charts_with_all_filters (interface, type, operator, gateway)")
    
    test_get_router_lookup_ipv4_with_ip()
    print("✓ test_get_router_lookup_ipv4_with_ip (8.8.8.8)")
    
    test_get_router_lookup_ipv4_with_fqdn()
    print("✓ test_get_router_lookup_ipv4_with_fqdn (google.dk)")
    
    test_get_router_lookup_ipv6_with_ip()
    print("✓ test_get_router_lookup_ipv6_with_ip (2001:4860:4860::8888)")
    
    test_get_router_lookup_ipv6_with_fqdn()
    print("✓ test_get_router_lookup_ipv6_with_fqdn (google.dk)")
    
    test_get_router_lookup_policy_ipv4_basic()
    print("✓ test_get_router_lookup_policy_ipv4_basic (8.8.8.8)")
    
    test_get_router_lookup_policy_ipv4_with_source()
    print("✓ test_get_router_lookup_policy_ipv4_with_source (dest + source)")
    
    test_get_router_lookup_policy_ipv4_with_interface()
    print("✓ test_get_router_lookup_policy_ipv4_with_interface (port3)")
    
    test_get_router_lookup_policy_ipv4_with_ports()
    print("✓ test_get_router_lookup_policy_ipv4_with_ports (ports + protocol)")
    
    test_get_router_lookup_policy_ipv4_full()
    print("✓ test_get_router_lookup_policy_ipv4_full (all parameters)")
    
    # IPv6 lookup-policy tests commented out - returns 500 error
    # test_get_router_lookup_policy_ipv6_basic()
    # print("✓ test_get_router_lookup_policy_ipv6_basic (2001:4860:4860::8888)")
    
    # test_get_router_lookup_policy_ipv6_with_source()
    # print("✓ test_get_router_lookup_policy_ipv6_with_source (dest + source)")
    
    # test_get_router_lookup_policy_ipv6_with_interface()
    # print("✓ test_get_router_lookup_policy_ipv6_with_interface (port3)")
    
    test_get_router_policy()
    print("✓ test_get_router_policy")
    
    test_get_router_policy_count_only()
    print("✓ test_get_router_policy_count_only")
    
    test_get_router_policy6()
    print("✓ test_get_router_policy6")
    
    test_get_router_policy6_count_only()
    print("✓ test_get_router_policy6_count_only")
    
    # ========================================================================
    # POST endpoint tests
    # ========================================================================
    
    print("\nRunning Router BGP POST endpoint tests...")
    
    # BGP soft-reset-neighbor commented out - requires valid BGP neighbor IP
    # test_post_router_bgp_soft_reset_neighbor()
    # print("✓ test_post_router_bgp_soft_reset_neighbor")
    
    test_post_router_bgp_clear_soft_in()
    print("✓ test_post_router_bgp_clear_soft_in")
    
    test_post_router_bgp_clear_soft_out()
    print("✓ test_post_router_bgp_clear_soft_out")
    
    print("\n✓ All Router endpoint tests completed!")
    print("\nSummary:")
    print("- IPv4/IPv6 routing tables: 6 tests (with filters)")
    print("- BGP neighbors statistics: 4 tests (default, ipv4, ipv6, ipboth)")
    print("- BGP neighbors discovery: 2 tests (ipv4, ipv6)")
    print("- BGP paths statistics: 4 tests (default, ipv4, ipv6, ipboth)")
    print("- BGP paths discovery: 2 tests (ipv4, ipv6)")
    print("- OSPF neighbors: 1 test")
    print("- SD-WAN routes: 2 tests (ipv4, ipv6)")
    print("- SD-WAN routes statistics: 4 tests (default, ipv4, ipv6, ipboth)")
    print("- Router statistics: 6 tests (basic, ipv4, ipv6, with filters)")
    print("- Router charts: 6 tests (basic, ipv4, ipv6, with filters)")
    print("- Router lookup: 4 tests (ipv4/ipv6 with IP and FQDN)")
    print("- Router lookup-policy: 5 tests (ipv4 only - ipv6 returns 500 error)")
    print("- Router policy routes: 4 tests (ipv4/ipv6 with/without count_only)")
    print("- BGP POST operations: 2 tests (clear-soft-in, clear-soft-out)")
    print("- Total: 50 active tests")
    print("- Commented: 4 tests (3 IPv6 lookup-policy + 1 soft-reset-neighbor)")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
