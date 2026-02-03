import argparse
import sys
from pathlib import Path
import pytest

pytestmark = pytest.mark.xdist_group(Path(__file__).stem)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt

TEST_NAME = "test_sniffer_9999991"
TEST_INTERFACE = "port3"
TEST_MAX_PACKET_COUNT = 1000
TEST_HOST = "10.0.0.1"
TEST_PORT = 80
TEST_PROTOCOL = "tcp"


def cleanup():
    try:
        sniffers = fgt.api.cmdb.firewall.on_demand_sniffer.get()
        for sniffer in sniffers:
            if getattr(sniffer, "name", None) == TEST_NAME:
                fgt.api.cmdb.firewall.on_demand_sniffer.delete(name=TEST_NAME)
                break
    except Exception:
        pass

def test_get_on_demand_sniffer():
    result = fgt.api.cmdb.firewall.on_demand_sniffer.get()
    assert result is not None
    assert result.http_status_code == 200

def test_post_on_demand_sniffer():
    result = fgt.api.cmdb.firewall.on_demand_sniffer.post(
        name=TEST_NAME,
        interface=TEST_INTERFACE,
        max_packet_count=TEST_MAX_PACKET_COUNT,
        hosts=[{"host": TEST_HOST}],
        ports=[{"port": TEST_PORT}],
        protocols=[{"protocol": TEST_PROTOCOL}],
        non_ip_packet="disable"
    )
    assert result is not None
    assert result.http_status == "success"

def test_put_on_demand_sniffer():
    updated_max_packet = 2000
    updated_host = "10.0.0.2"
    result = fgt.api.cmdb.firewall.on_demand_sniffer.put(
        name=TEST_NAME,
        interface=TEST_INTERFACE,
        max_packet_count=updated_max_packet,
        hosts=[{"host": updated_host}],
        ports=[{"port": 443}],
        protocols=[{"protocol": "udp"}],
        non_ip_packet="enable"
    )
    assert result is not None
    assert result.http_status == "success"
    verify = fgt.api.cmdb.firewall.on_demand_sniffer.get(name=TEST_NAME)
    assert verify is not None
    assert verify.http_status_code == 200
    assert verify.max_packet_count == updated_max_packet
    assert verify.non_ip_packet == "enable"

def test_get_specific_on_demand_sniffer():
    result = fgt.api.cmdb.firewall.on_demand_sniffer.get(name=TEST_NAME)
    assert result is not None
    assert result.name == TEST_NAME

def test_delete_on_demand_sniffer():
    result = fgt.api.cmdb.firewall.on_demand_sniffer.delete(name=TEST_NAME)
    assert result is not None
    assert result.http_status == "success"
    # Verify deletion
    sniffers = fgt.api.cmdb.firewall.on_demand_sniffer.get()
    names = [getattr(s, "name", None) for s in sniffers]
    assert TEST_NAME not in names, "On-demand sniffer should have been deleted"

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
    test_get_on_demand_sniffer()
    print("✓ test_get_on_demand_sniffer passed")
    test_post_on_demand_sniffer()
    print("✓ test_post_on_demand_sniffer passed")
    test_put_on_demand_sniffer()
    print("✓ test_put_on_demand_sniffer passed")
    test_get_specific_on_demand_sniffer()
    print("✓ test_get_specific_on_demand_sniffer passed")
    test_delete_on_demand_sniffer()
    print("✓ test_delete_on_demand_sniffer passed")
    cleanup()
    print("✓ post-Cleanup passed")
    print("\n✓ All tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
