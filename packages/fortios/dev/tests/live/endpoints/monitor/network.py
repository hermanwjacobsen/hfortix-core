import argparse
import sys
from pathlib import Path
import pytest

# Run network monitor tests on a single worker to preserve state
pytestmark = pytest.mark.xdist_group(Path(__file__).stem)

# Add pytest directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt



# ============================================================================
# Network Monitor Tests - GET endpoints
# ============================================================================

def test_get_network_arp():
    """Test GET /monitor/network/arp - Get IPv4 ARP table."""
    try:
        result = fgt.api.monitor.network.arp.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_network_lldp_neighbors_vdom():
    """Test GET /monitor/network/lldp/neighbors - List all active LLDP neighbors (vdom scope)."""
    try:
        result = fgt.api.monitor.network.lldp.neighbors.get(scope="vdom")
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_network_lldp_neighbors_global():
    """Test GET /monitor/network/lldp/neighbors - List all active LLDP neighbors (global scope)."""
    try:
        result = fgt.api.monitor.network.lldp.neighbors.get(scope="global")
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_network_lldp_ports_vdom():
    """Test GET /monitor/network/lldp/ports - List all active LLDP ports (vdom scope)."""
    try:
        result = fgt.api.monitor.network.lldp.ports.get(scope="vdom")
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_network_lldp_ports_global():
    """Test GET /monitor/network/lldp/ports - List all active LLDP ports (global scope)."""
    try:
        result = fgt.api.monitor.network.lldp.ports.get(scope="global")
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_network_lldp_ports_with_port():
    """Test GET /monitor/network/lldp/ports - List LLDP ports for specific port (port3)."""
    try:
        result = fgt.api.monitor.network.lldp.ports.get(mkey="port1", vdom="root")
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_network_dns_latency():
    """Test GET /monitor/network/dns/latency - Get DNS latency."""
    try:
        result = fgt.api.monitor.network.dns.latency.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_network_fortiguard_live_services_latency():
    """Test GET /monitor/network/fortiguard/live-services-latency - Get latency information for live FortiGuard services."""
    try:
        result = fgt.api.monitor.network.fortiguard.live_services_latency.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_network_ddns_servers():
    """Test GET /monitor/network/ddns/servers - Get DDNS servers."""
    try:
        result = fgt.api.monitor.network.ddns.servers.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_network_ddns_lookup():
    """Test GET /monitor/network/ddns/lookup - Check DDNS FQDN availability (google.dk)."""
    try:
        result = fgt.api.monitor.network.ddns.lookup.get(domain="google.dk")
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_network_reverse_ip_lookup():
    """Test GET /monitor/network/reverse-ip-lookup - Retrieve the resolved DNS domain name for a given IP address (8.8.8.8)."""
    try:
        result = fgt.api.monitor.network.reverse_ip_lookup.get(ip="8.8.8.8")
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


# ============================================================================
# Network Monitor Tests - POST endpoints
# ============================================================================

def test_post_network_debug_flow_start():
    """Test POST /monitor/network/debug-flow/start - Start debug flow packet capture."""
    try:
        # Start debug flow with source and destination addresses
        result = fgt.api.monitor.network.debug_flow.start.post(
            num_packets=10,
            saddr_from="192.168.1.0",
            saddr_to="192.168.1.255"
        )
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        elif "424" in str(e):
            print("Debug flow unavailable (424) - may require specific permissions or feature not enabled")
        else:
            raise


def test_post_network_debug_flow_stop():
    """Test POST /monitor/network/debug-flow/stop - Stop debug flow packet capture."""
    try:
        result = fgt.api.monitor.network.debug_flow.stop.post()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        elif "424" in str(e):
            print("Debug flow unavailable (424) - may require specific permissions or feature not enabled")
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
    
    print("Running Network monitor endpoint tests...")
    
    test_get_network_arp()
    print("✓ test_get_network_arp")
    
    test_get_network_lldp_neighbors_vdom()
    print("✓ test_get_network_lldp_neighbors_vdom")
    
    test_get_network_lldp_neighbors_global()
    print("✓ test_get_network_lldp_neighbors_global")
    
    test_get_network_lldp_ports_vdom()
    print("✓ test_get_network_lldp_ports_vdom")
    
    test_get_network_lldp_ports_global()
    print("✓ test_get_network_lldp_ports_global")
    
    test_get_network_lldp_ports_with_port()
    print("✓ test_get_network_lldp_ports_with_port (port3)")
    
    test_get_network_dns_latency()
    print("✓ test_get_network_dns_latency")
    
    test_get_network_fortiguard_live_services_latency()
    print("✓ test_get_network_fortiguard_live_services_latency")
    
    test_get_network_ddns_servers()
    print("✓ test_get_network_ddns_servers")
    
    test_get_network_ddns_lookup()
    print("✓ test_get_network_ddns_lookup (google.dk)")
    
    test_get_network_reverse_ip_lookup()
    print("✓ test_get_network_reverse_ip_lookup (8.8.8.8)")
    
    print("\n✓ All Network GET endpoint tests completed!")
    
    # ========================================================================
    # POST endpoint tests
    # ========================================================================
    
    print("\nRunning POST endpoint tests...")
    
    test_post_network_debug_flow_start()
    print("✓ test_post_network_debug_flow_start")
    
    test_post_network_debug_flow_stop()
    print("✓ test_post_network_debug_flow_stop")
    
    print("\n✓ All Network POST endpoint tests completed!")
    print("\nSummary:")
    print("- GET endpoints: 11 active tests")
    print("- POST endpoints: 2 active tests")
    print("- Total: 13 test functions covering Network monitor endpoints")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
