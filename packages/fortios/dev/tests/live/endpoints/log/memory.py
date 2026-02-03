#!/usr/bin/env python
"""Test log/memory API endpoints (both raw and formatted versions)."""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt

# ============================================================================
# LOG TYPE TESTS - Formatted (non-raw)
# ============================================================================

def test_memory_virus():
    """Test: Get memory virus logs (formatted)"""
    result = fgt.api.log.memory.virus.get()
    assert result.http_status == "success"

def test_memory_webfilter():
    """Test: Get memory webfilter logs (formatted)"""
    result = fgt.api.log.memory.webfilter.get()
    assert result.http_status == "success"

def test_memory_waf():
    """Test: Get memory WAF logs (formatted)"""
    result = fgt.api.log.memory.waf.get()
    assert result.http_status == "success"

def test_memory_ips():
    """Test: Get memory IPS logs (formatted)"""
    result = fgt.api.log.memory.ips.get()
    assert result.http_status == "success"

def test_memory_anomaly():
    """Test: Get memory anomaly logs (formatted)"""
    result = fgt.api.log.memory.anomaly.get()
    assert result.http_status == "success"

def test_memory_app_ctrl():
    """Test: Get memory app-ctrl logs (formatted)"""
    result = fgt.api.log.memory.app_ctrl.get()
    assert result.http_status == "success"

def test_memory_emailfilter():
    """Test: Get memory emailfilter logs (formatted)"""
    result = fgt.api.log.memory.emailfilter.get()
    assert result.http_status == "success"

def test_memory_dlp():
    """Test: Get memory DLP logs (formatted)"""
    result = fgt.api.log.memory.dlp.get()
    assert result.http_status == "success"

def test_memory_voip():
    """Test: Get memory VoIP logs (formatted)"""
    result = fgt.api.log.memory.voip.get()
    assert result.http_status == "success"

def test_memory_gtp():
    """Test: Get memory GTP logs (formatted)"""
    result = fgt.api.log.memory.gtp.get()
    assert result.http_status == "success"

def test_memory_dns():
    """Test: Get memory DNS logs (formatted)"""
    result = fgt.api.log.memory.dns.get()
    assert result.http_status == "success"

def test_memory_ssh():
    """Test: Get memory SSH logs (formatted)"""
    result = fgt.api.log.memory.ssh.get()
    assert result.http_status == "success"

def test_memory_ssl():
    """Test: Get memory SSL logs (formatted)"""
    result = fgt.api.log.memory.ssl.get()
    assert result.http_status == "success"

def test_memory_file_filter():
    """Test: Get memory file-filter logs (formatted)"""
    result = fgt.api.log.memory.file_filter.get()
    assert result.http_status == "success"

# ============================================================================
# LOG TYPE TESTS - Raw format
# ============================================================================

def test_memory_virus_raw():
    """Test: Get memory virus logs (raw)"""
    result = fgt.api.log.memory.virus.raw.get()
    assert result.http_status == "success"

def test_memory_webfilter_raw():
    """Test: Get memory webfilter logs (raw)"""
    result = fgt.api.log.memory.webfilter.raw.get()
    assert result.http_status == "success"

def test_memory_waf_raw():
    """Test: Get memory WAF logs (raw)"""
    result = fgt.api.log.memory.waf.raw.get()
    assert result.http_status == "success"

def test_memory_ips_raw():
    """Test: Get memory IPS logs (raw)"""
    result = fgt.api.log.memory.ips.raw.get()
    assert result.http_status == "success"

def test_memory_anomaly_raw():
    """Test: Get memory anomaly logs (raw)"""
    result = fgt.api.log.memory.anomaly.raw.get()
    assert result.http_status == "success"

def test_memory_app_ctrl_raw():
    """Test: Get memory app-ctrl logs (raw)"""
    result = fgt.api.log.memory.app_ctrl.raw.get()
    assert result.http_status == "success"

def test_memory_emailfilter_raw():
    """Test: Get memory emailfilter logs (raw)"""
    result = fgt.api.log.memory.emailfilter.raw.get()
    assert result.http_status == "success"

def test_memory_dlp_raw():
    """Test: Get memory DLP logs (raw)"""
    result = fgt.api.log.memory.dlp.raw.get()
    assert result.http_status == "success"

def test_memory_voip_raw():
    """Test: Get memory VoIP logs (raw)"""
    result = fgt.api.log.memory.voip.raw.get()
    assert result.http_status == "success"

def test_memory_gtp_raw():
    """Test: Get memory GTP logs (raw)"""
    result = fgt.api.log.memory.gtp.raw.get()
    assert result.http_status == "success"

def test_memory_dns_raw():
    """Test: Get memory DNS logs (raw)"""
    result = fgt.api.log.memory.dns.raw.get()
    assert result.http_status == "success"

def test_memory_ssh_raw():
    """Test: Get memory SSH logs (raw)"""
    result = fgt.api.log.memory.ssh.raw.get()
    assert result.http_status == "success"

def test_memory_ssl_raw():
    """Test: Get memory SSL logs (raw)"""
    result = fgt.api.log.memory.ssl.raw.get()
    assert result.http_status == "success"

def test_memory_file_filter_raw():
    """Test: Get memory file-filter logs (raw)"""
    result = fgt.api.log.memory.file_filter.raw.get()
    assert result.http_status == "success"

# ============================================================================
# TRAFFIC SUBTYPE TESTS - Formatted (non-raw)
# ============================================================================

def test_memory_traffic_forward():
    """Test: Get memory traffic/forward logs (formatted)"""
    result = fgt.api.log.memory.traffic.forward.get(rows=5)
    assert result.http_status == "success"

def test_memory_traffic_local():
    """Test: Get memory traffic/local logs (formatted)"""
    result = fgt.api.log.memory.traffic.local.get(rows=5)
    assert result.http_status == "success"

def test_memory_traffic_multicast():
    """Test: Get memory traffic/multicast logs (formatted)"""
    result = fgt.api.log.memory.traffic.multicast.get(rows=5)
    assert result.http_status == "success"

def test_memory_traffic_sniffer():
    """Test: Get memory traffic/sniffer logs (formatted)"""
    result = fgt.api.log.memory.traffic.sniffer.get(rows=5)
    assert result.http_status == "success"

def test_memory_traffic_fortiview():
    """Test: Get memory traffic/fortiview logs (formatted)"""
    result = fgt.api.log.memory.traffic.fortiview.get(rows=5)
    assert result.http_status == "success"

def test_memory_traffic_threat():
    """Test: Get memory traffic/threat logs (formatted)"""
    result = fgt.api.log.memory.traffic.threat.get(rows=5)
    assert result.http_status == "success"

# ============================================================================
# TRAFFIC SUBTYPE TESTS - Raw format
# ============================================================================

def test_memory_traffic_forward_raw():
    """Test: Get memory traffic/forward logs (raw)"""
    result = fgt.api.log.memory.traffic.forward.raw.get(rows=5)
    assert result.http_status == "success"

def test_memory_traffic_local_raw():
    """Test: Get memory traffic/local logs (raw)"""
    result = fgt.api.log.memory.traffic.local.raw.get(rows=5)
    assert result.http_status == "success"

def test_memory_traffic_multicast_raw():
    """Test: Get memory traffic/multicast logs (raw)"""
    result = fgt.api.log.memory.traffic.multicast.raw.get(rows=5)
    assert result.http_status == "success"

def test_memory_traffic_sniffer_raw():
    """Test: Get memory traffic/sniffer logs (raw)"""
    result = fgt.api.log.memory.traffic.sniffer.raw.get(rows=5)
    assert result.http_status == "success"

def test_memory_traffic_fortiview_raw():
    """Test: Get memory traffic/fortiview logs (raw)"""
    result = fgt.api.log.memory.traffic.fortiview.raw.get(rows=5)
    assert result.http_status == "success"

def test_memory_traffic_threat_raw():
    """Test: Get memory traffic/threat logs (raw)"""
    result = fgt.api.log.memory.traffic.threat.raw.get(rows=5)
    assert result.http_status == "success"

# ============================================================================
# EVENT SUBTYPE TESTS - Formatted (non-raw)
# ============================================================================

def test_memory_event_system():
    """Test: Get memory event/system logs (formatted)"""
    result = fgt.api.log.memory.event.system.get(rows=5)
    assert result.http_status == "success"

def test_memory_event_vpn():
    """Test: Get memory event/vpn logs (formatted)"""
    result = fgt.api.log.memory.event.vpn.get(rows=5)
    assert result.http_status == "success"

def test_memory_event_user():
    """Test: Get memory event/user logs (formatted)"""
    result = fgt.api.log.memory.event.user.get(rows=5)
    assert result.http_status == "success"

def test_memory_event_router():
    """Test: Get memory event/router logs (formatted)"""
    result = fgt.api.log.memory.event.router.get(rows=5)
    assert result.http_status == "success"

def test_memory_event_wireless():
    """Test: Get memory event/wireless logs (formatted)"""
    result = fgt.api.log.memory.event.wireless.get(rows=5)
    assert result.http_status == "success"

def test_memory_event_endpoint():
    """Test: Get memory event/endpoint logs (formatted)"""
    result = fgt.api.log.memory.event.endpoint.get(rows=5)
    assert result.http_status == "success"

def test_memory_event_ha():
    """Test: Get memory event/ha logs (formatted)"""
    result = fgt.api.log.memory.event.ha.get(rows=5)
    assert result.http_status == "success"

def test_memory_event_security_rating():
    """Test: Get memory event/security-rating logs (formatted)"""
    result = fgt.api.log.memory.event.security_rating.get(rows=5)
    assert result.http_status == "success"

def test_memory_event_fortiextender():
    """Test: Get memory event/fortiextender logs (formatted)"""
    result = fgt.api.log.memory.event.fortiextender.get(rows=5)
    assert result.http_status == "success"

def test_memory_event_connector():
    """Test: Get memory event/connector logs (formatted)"""
    result = fgt.api.log.memory.event.connector.get(rows=5)
    assert result.http_status == "success"

# ============================================================================
# EVENT SUBTYPE TESTS - Raw format
# ============================================================================

def test_memory_event_system_raw():
    """Test: Get memory event/system logs (raw)"""
    result = fgt.api.log.memory.event.system.raw.get(rows=5)
    assert result.http_status == "success"

def test_memory_event_vpn_raw():
    """Test: Get memory event/vpn logs (raw)"""
    result = fgt.api.log.memory.event.vpn.raw.get(rows=5)
    assert result.http_status == "success"

def test_memory_event_user_raw():
    """Test: Get memory event/user logs (raw)"""
    result = fgt.api.log.memory.event.user.raw.get(rows=5)
    assert result.http_status == "success"

def test_memory_event_router_raw():
    """Test: Get memory event/router logs (raw)"""
    result = fgt.api.log.memory.event.router.raw.get(rows=5)
    assert result.http_status == "success"

def test_memory_event_wireless_raw():
    """Test: Get memory event/wireless logs (raw)"""
    result = fgt.api.log.memory.event.wireless.raw.get(rows=5)
    assert result.http_status == "success"

def test_memory_event_endpoint_raw():
    """Test: Get memory event/endpoint logs (raw)"""
    result = fgt.api.log.memory.event.endpoint.raw.get(rows=5)
    assert result.http_status == "success"

def test_memory_event_ha_raw():
    """Test: Get memory event/ha logs (raw)"""
    result = fgt.api.log.memory.event.ha.raw.get(rows=5)
    assert result.http_status == "success"

def test_memory_event_security_rating_raw():
    """Test: Get memory event/security-rating logs (raw)"""
    result = fgt.api.log.memory.event.security_rating.raw.get(rows=5)
    assert result.http_status == "success"

def test_memory_event_fortiextender_raw():
    """Test: Get memory event/fortiextender logs (raw)"""
    result = fgt.api.log.memory.event.fortiextender.raw.get(rows=5)
    assert result.http_status == "success"

def test_memory_event_connector_raw():
    """Test: Get memory event/connector logs (raw)"""
    result = fgt.api.log.memory.event.connector.raw.get(rows=5)
    assert result.http_status == "success"

# ============================================================================
# MAIN - Run all tests with output
# ============================================================================

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
    print("Testing log/memory API endpoints (raw and formatted)...")
    print("=" * 60)
    
    passed = 0
    failed = 0
    skipped = 0
    
    # All test functions grouped by category
    log_type_tests = [
        ("virus", test_memory_virus, test_memory_virus_raw),
        ("webfilter", test_memory_webfilter, test_memory_webfilter_raw),
        ("waf", test_memory_waf, test_memory_waf_raw),
        ("ips", test_memory_ips, test_memory_ips_raw),
        ("anomaly", test_memory_anomaly, test_memory_anomaly_raw),
        ("app-ctrl", test_memory_app_ctrl, test_memory_app_ctrl_raw),
        ("emailfilter", test_memory_emailfilter, test_memory_emailfilter_raw),
        ("dlp", test_memory_dlp, test_memory_dlp_raw),
        ("voip", test_memory_voip, test_memory_voip_raw),
        ("gtp", test_memory_gtp, test_memory_gtp_raw),
        ("dns", test_memory_dns, test_memory_dns_raw),
        ("ssh", test_memory_ssh, test_memory_ssh_raw),
        ("ssl", test_memory_ssl, test_memory_ssl_raw),
        ("file-filter", test_memory_file_filter, test_memory_file_filter_raw),
    ]
    
    traffic_tests = [
        ("forward", test_memory_traffic_forward, test_memory_traffic_forward_raw),
        ("local", test_memory_traffic_local, test_memory_traffic_local_raw),
        ("multicast", test_memory_traffic_multicast, test_memory_traffic_multicast_raw),
        ("sniffer", test_memory_traffic_sniffer, test_memory_traffic_sniffer_raw),
        ("fortiview", test_memory_traffic_fortiview, test_memory_traffic_fortiview_raw),
        ("threat", test_memory_traffic_threat, test_memory_traffic_threat_raw),
    ]
    
    event_tests = [
        ("system", test_memory_event_system, test_memory_event_system_raw),
        ("vpn", test_memory_event_vpn, test_memory_event_vpn_raw),
        ("user", test_memory_event_user, test_memory_event_user_raw),
        ("router", test_memory_event_router, test_memory_event_router_raw),
        ("wireless", test_memory_event_wireless, test_memory_event_wireless_raw),
        ("endpoint", test_memory_event_endpoint, test_memory_event_endpoint_raw),
        ("ha", test_memory_event_ha, test_memory_event_ha_raw),
        ("security-rating", test_memory_event_security_rating, test_memory_event_security_rating_raw),
        ("fortiextender", test_memory_event_fortiextender, test_memory_event_fortiextender_raw),
        ("connector", test_memory_event_connector, test_memory_event_connector_raw),
    ]
    
    print("\n=== Log Types ===")
    for name, formatted_fn, raw_fn in log_type_tests:
        # Test formatted
        try:
            formatted_fn()
            print(f"  ✓ memory/{name} (formatted)")
            passed += 1
        except Exception as e:
            if "404" in str(e):
                print(f"  ○ memory/{name} (formatted): Not available")
                skipped += 1
            else:
                print(f"  ✗ memory/{name} (formatted): {e}")
                failed += 1
        # Test raw
        try:
            raw_fn()
            print(f"  ✓ memory/{name} (raw)")
            passed += 1
        except Exception as e:
            if "404" in str(e):
                print(f"  ○ memory/{name} (raw): Not available")
                skipped += 1
            else:
                print(f"  ✗ memory/{name} (raw): {e}")
                failed += 1
    
    print("\n=== Traffic Subtypes ===")
    for name, formatted_fn, raw_fn in traffic_tests:
        try:
            formatted_fn()
            print(f"  ✓ memory/traffic/{name} (formatted)")
            passed += 1
        except Exception as e:
            if "404" in str(e):
                print(f"  ○ memory/traffic/{name} (formatted): Not available")
                skipped += 1
            else:
                print(f"  ✗ memory/traffic/{name} (formatted): {e}")
                failed += 1
        try:
            raw_fn()
            print(f"  ✓ memory/traffic/{name} (raw)")
            passed += 1
        except Exception as e:
            if "404" in str(e):
                print(f"  ○ memory/traffic/{name} (raw): Not available")
                skipped += 1
            else:
                print(f"  ✗ memory/traffic/{name} (raw): {e}")
                failed += 1
    
    print("\n=== Event Subtypes ===")
    for name, formatted_fn, raw_fn in event_tests:
        try:
            formatted_fn()
            print(f"  ✓ memory/event/{name} (formatted)")
            passed += 1
        except Exception as e:
            if "404" in str(e):
                print(f"  ○ memory/event/{name} (formatted): Not available")
                skipped += 1
            else:
                print(f"  ✗ memory/event/{name} (formatted): {e}")
                failed += 1
        try:
            raw_fn()
            print(f"  ✓ memory/event/{name} (raw)")
            passed += 1
        except Exception as e:
            if "404" in str(e):
                print(f"  ○ memory/event/{name} (raw): Not available")
                skipped += 1
            else:
                print(f"  ✗ memory/event/{name} (raw): {e}")
                failed += 1
    
    print("\n" + "=" * 60)
    print(f"Results: {passed} passed, {failed} failed, {skipped} skipped")
    print(f"Total: {passed + failed + skipped} tests")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
