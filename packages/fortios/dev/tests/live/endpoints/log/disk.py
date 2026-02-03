#!/usr/bin/env python
"""Test log/disk API endpoints (both raw and formatted versions)."""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt

# ============================================================================
# LOG TYPE TESTS - Formatted (non-raw)
# ============================================================================

def test_disk_virus():
    """Test: Get disk virus logs (formatted)"""
    result = fgt.api.log.disk.virus.get()
    assert result.http_status == "success"

def test_disk_webfilter():
    """Test: Get disk webfilter logs (formatted)"""
    result = fgt.api.log.disk.webfilter.get()
    assert result.http_status == "success"

def test_disk_waf():
    """Test: Get disk WAF logs (formatted)"""
    result = fgt.api.log.disk.waf.get()
    assert result.http_status == "success"

def test_disk_ips():
    """Test: Get disk IPS logs (formatted)"""
    result = fgt.api.log.disk.ips.get()
    assert result.http_status == "success"

def test_disk_anomaly():
    """Test: Get disk anomaly logs (formatted)"""
    result = fgt.api.log.disk.anomaly.get()
    assert result.http_status == "success"

def test_disk_app_ctrl():
    """Test: Get disk app-ctrl logs (formatted)"""
    result = fgt.api.log.disk.app_ctrl.get()
    assert result.http_status == "success"

def test_disk_emailfilter():
    """Test: Get disk emailfilter logs (formatted)"""
    result = fgt.api.log.disk.emailfilter.get()
    assert result.http_status == "success"

def test_disk_dlp():
    """Test: Get disk DLP logs (formatted)"""
    result = fgt.api.log.disk.dlp.get()
    assert result.http_status == "success"

def test_disk_voip():
    """Test: Get disk VoIP logs (formatted)"""
    result = fgt.api.log.disk.voip.get()
    assert result.http_status == "success"

def test_disk_gtp():
    """Test: Get disk GTP logs (formatted)"""
    result = fgt.api.log.disk.gtp.get()
    assert result.http_status == "success"

def test_disk_dns():
    """Test: Get disk DNS logs (formatted)"""
    result = fgt.api.log.disk.dns.get()
    assert result.http_status == "success"

def test_disk_ssh():
    """Test: Get disk SSH logs (formatted)"""
    result = fgt.api.log.disk.ssh.get()
    assert result.http_status == "success"

def test_disk_ssl():
    """Test: Get disk SSL logs (formatted)"""
    result = fgt.api.log.disk.ssl.get()
    assert result.http_status == "success"

def test_disk_file_filter():
    """Test: Get disk file-filter logs (formatted)"""
    result = fgt.api.log.disk.file_filter.get()
    assert result.http_status == "success"

# ============================================================================
# LOG TYPE TESTS - Raw format
# ============================================================================

def test_disk_virus_raw():
    """Test: Get disk virus logs (raw)"""
    result = fgt.api.log.disk.virus.raw.get()
    assert result.http_status == "success"

def test_disk_webfilter_raw():
    """Test: Get disk webfilter logs (raw)"""
    result = fgt.api.log.disk.webfilter.raw.get()
    assert result.http_status == "success"

def test_disk_waf_raw():
    """Test: Get disk WAF logs (raw)"""
    result = fgt.api.log.disk.waf.raw.get()
    assert result.http_status == "success"

def test_disk_ips_raw():
    """Test: Get disk IPS logs (raw)"""
    result = fgt.api.log.disk.ips.raw.get()
    assert result.http_status == "success"

def test_disk_anomaly_raw():
    """Test: Get disk anomaly logs (raw)"""
    result = fgt.api.log.disk.anomaly.raw.get()
    assert result.http_status == "success"

def test_disk_app_ctrl_raw():
    """Test: Get disk app-ctrl logs (raw)"""
    result = fgt.api.log.disk.app_ctrl.raw.get()
    assert result.http_status == "success"

def test_disk_emailfilter_raw():
    """Test: Get disk emailfilter logs (raw)"""
    result = fgt.api.log.disk.emailfilter.raw.get()
    assert result.http_status == "success"

def test_disk_dlp_raw():
    """Test: Get disk DLP logs (raw)"""
    result = fgt.api.log.disk.dlp.raw.get()
    assert result.http_status == "success"

def test_disk_voip_raw():
    """Test: Get disk VoIP logs (raw)"""
    result = fgt.api.log.disk.voip.raw.get()
    assert result.http_status == "success"

def test_disk_gtp_raw():
    """Test: Get disk GTP logs (raw)"""
    result = fgt.api.log.disk.gtp.raw.get()
    assert result.http_status == "success"

def test_disk_dns_raw():
    """Test: Get disk DNS logs (raw)"""
    result = fgt.api.log.disk.dns.raw.get()
    assert result.http_status == "success"

def test_disk_ssh_raw():
    """Test: Get disk SSH logs (raw)"""
    result = fgt.api.log.disk.ssh.raw.get()
    assert result.http_status == "success"

def test_disk_ssl_raw():
    """Test: Get disk SSL logs (raw)"""
    result = fgt.api.log.disk.ssl.raw.get()
    assert result.http_status == "success"

def test_disk_file_filter_raw():
    """Test: Get disk file-filter logs (raw)"""
    result = fgt.api.log.disk.file_filter.raw.get()
    assert result.http_status == "success"

# ============================================================================
# TRAFFIC SUBTYPE TESTS - Formatted (non-raw)
# ============================================================================

def test_disk_traffic_forward():
    """Test: Get disk traffic/forward logs (formatted)"""
    result = fgt.api.log.disk.traffic.forward.get(rows=5)
    assert result.http_status == "success"

def test_disk_traffic_local():
    """Test: Get disk traffic/local logs (formatted)"""
    result = fgt.api.log.disk.traffic.local.get(rows=5)
    assert result.http_status == "success"

def test_disk_traffic_multicast():
    """Test: Get disk traffic/multicast logs (formatted)"""
    result = fgt.api.log.disk.traffic.multicast.get(rows=5)
    assert result.http_status == "success"

def test_disk_traffic_sniffer():
    """Test: Get disk traffic/sniffer logs (formatted)"""
    result = fgt.api.log.disk.traffic.sniffer.get(rows=5)
    assert result.http_status == "success"

def test_disk_traffic_fortiview():
    """Test: Get disk traffic/fortiview logs (formatted)"""
    result = fgt.api.log.disk.traffic.fortiview.get(rows=5)
    assert result.http_status == "success"

def test_disk_traffic_threat():
    """Test: Get disk traffic/threat logs (formatted)"""
    result = fgt.api.log.disk.traffic.threat.get(rows=5)
    assert result.http_status == "success"

# ============================================================================
# TRAFFIC SUBTYPE TESTS - Raw format
# ============================================================================

def test_disk_traffic_forward_raw():
    """Test: Get disk traffic/forward logs (raw)"""
    result = fgt.api.log.disk.traffic.forward.raw.get(rows=5)
    assert result.http_status == "success"

def test_disk_traffic_local_raw():
    """Test: Get disk traffic/local logs (raw)"""
    result = fgt.api.log.disk.traffic.local.raw.get(rows=5)
    assert result.http_status == "success"

def test_disk_traffic_multicast_raw():
    """Test: Get disk traffic/multicast logs (raw)"""
    result = fgt.api.log.disk.traffic.multicast.raw.get(rows=5)
    assert result.http_status == "success"

def test_disk_traffic_sniffer_raw():
    """Test: Get disk traffic/sniffer logs (raw)"""
    result = fgt.api.log.disk.traffic.sniffer.raw.get(rows=5)
    assert result.http_status == "success"

def test_disk_traffic_fortiview_raw():
    """Test: Get disk traffic/fortiview logs (raw)"""
    result = fgt.api.log.disk.traffic.fortiview.raw.get(rows=5)
    assert result.http_status == "success"

def test_disk_traffic_threat_raw():
    """Test: Get disk traffic/threat logs (raw)"""
    result = fgt.api.log.disk.traffic.threat.raw.get(rows=5)
    assert result.http_status == "success"

# ============================================================================
# EVENT SUBTYPE TESTS - Formatted (non-raw)
# ============================================================================

def test_disk_event_system():
    """Test: Get disk event/system logs (formatted)"""
    result = fgt.api.log.disk.event.system.get(rows=5)
    assert result.http_status == "success"

def test_disk_event_vpn():
    """Test: Get disk event/vpn logs (formatted)"""
    result = fgt.api.log.disk.event.vpn.get(rows=5)
    assert result.http_status == "success"

def test_disk_event_user():
    """Test: Get disk event/user logs (formatted)"""
    result = fgt.api.log.disk.event.user.get(rows=5)
    assert result.http_status == "success"

def test_disk_event_router():
    """Test: Get disk event/router logs (formatted)"""
    result = fgt.api.log.disk.event.router.get(rows=5)
    assert result.http_status == "success"

def test_disk_event_wireless():
    """Test: Get disk event/wireless logs (formatted)"""
    result = fgt.api.log.disk.event.wireless.get(rows=5)
    assert result.http_status == "success"

def test_disk_event_endpoint():
    """Test: Get disk event/endpoint logs (formatted)"""
    result = fgt.api.log.disk.event.endpoint.get(rows=5)
    assert result.http_status == "success"

def test_disk_event_ha():
    """Test: Get disk event/ha logs (formatted)"""
    result = fgt.api.log.disk.event.ha.get(rows=5)
    assert result.http_status == "success"

def test_disk_event_security_rating():
    """Test: Get disk event/security-rating logs (formatted)"""
    result = fgt.api.log.disk.event.security_rating.get(rows=5)
    assert result.http_status == "success"

def test_disk_event_fortiextender():
    """Test: Get disk event/fortiextender logs (formatted)"""
    result = fgt.api.log.disk.event.fortiextender.get(rows=5)
    assert result.http_status == "success"

def test_disk_event_connector():
    """Test: Get disk event/connector logs (formatted)"""
    result = fgt.api.log.disk.event.connector.get(rows=5)
    assert result.http_status == "success"

# ============================================================================
# EVENT SUBTYPE TESTS - Raw format
# ============================================================================

def test_disk_event_system_raw():
    """Test: Get disk event/system logs (raw)"""
    result = fgt.api.log.disk.event.system.raw.get(rows=5)
    assert result.http_status == "success"

def test_disk_event_vpn_raw():
    """Test: Get disk event/vpn logs (raw)"""
    result = fgt.api.log.disk.event.vpn.raw.get(rows=5)
    assert result.http_status == "success"

def test_disk_event_user_raw():
    """Test: Get disk event/user logs (raw)"""
    result = fgt.api.log.disk.event.user.raw.get(rows=5)
    assert result.http_status == "success"

def test_disk_event_router_raw():
    """Test: Get disk event/router logs (raw)"""
    result = fgt.api.log.disk.event.router.raw.get(rows=5)
    assert result.http_status == "success"

def test_disk_event_wireless_raw():
    """Test: Get disk event/wireless logs (raw)"""
    result = fgt.api.log.disk.event.wireless.raw.get(rows=5)
    assert result.http_status == "success"

def test_disk_event_endpoint_raw():
    """Test: Get disk event/endpoint logs (raw)"""
    result = fgt.api.log.disk.event.endpoint.raw.get(rows=5)
    assert result.http_status == "success"

def test_disk_event_ha_raw():
    """Test: Get disk event/ha logs (raw)"""
    result = fgt.api.log.disk.event.ha.raw.get(rows=5)
    assert result.http_status == "success"

def test_disk_event_security_rating_raw():
    """Test: Get disk event/security-rating logs (raw)"""
    result = fgt.api.log.disk.event.security_rating.raw.get(rows=5)
    assert result.http_status == "success"

def test_disk_event_fortiextender_raw():
    """Test: Get disk event/fortiextender logs (raw)"""
    result = fgt.api.log.disk.event.fortiextender.raw.get(rows=5)
    assert result.http_status == "success"

def test_disk_event_connector_raw():
    """Test: Get disk event/connector logs (raw)"""
    result = fgt.api.log.disk.event.connector.raw.get(rows=5)
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
    print("Testing log/disk API endpoints (raw and formatted)...")
    print("=" * 60)
    
    passed = 0
    failed = 0
    skipped = 0
    
    # All test functions grouped by category
    log_type_tests = [
        ("virus", test_disk_virus, test_disk_virus_raw),
        ("webfilter", test_disk_webfilter, test_disk_webfilter_raw),
        ("waf", test_disk_waf, test_disk_waf_raw),
        ("ips", test_disk_ips, test_disk_ips_raw),
        ("anomaly", test_disk_anomaly, test_disk_anomaly_raw),
        ("app-ctrl", test_disk_app_ctrl, test_disk_app_ctrl_raw),
        ("emailfilter", test_disk_emailfilter, test_disk_emailfilter_raw),
        ("dlp", test_disk_dlp, test_disk_dlp_raw),
        ("voip", test_disk_voip, test_disk_voip_raw),
        ("gtp", test_disk_gtp, test_disk_gtp_raw),
        ("dns", test_disk_dns, test_disk_dns_raw),
        ("ssh", test_disk_ssh, test_disk_ssh_raw),
        ("ssl", test_disk_ssl, test_disk_ssl_raw),
        ("file-filter", test_disk_file_filter, test_disk_file_filter_raw),
    ]
    
    traffic_tests = [
        ("forward", test_disk_traffic_forward, test_disk_traffic_forward_raw),
        ("local", test_disk_traffic_local, test_disk_traffic_local_raw),
        ("multicast", test_disk_traffic_multicast, test_disk_traffic_multicast_raw),
        ("sniffer", test_disk_traffic_sniffer, test_disk_traffic_sniffer_raw),
        ("fortiview", test_disk_traffic_fortiview, test_disk_traffic_fortiview_raw),
        ("threat", test_disk_traffic_threat, test_disk_traffic_threat_raw),
    ]
    
    event_tests = [
        ("system", test_disk_event_system, test_disk_event_system_raw),
        ("vpn", test_disk_event_vpn, test_disk_event_vpn_raw),
        ("user", test_disk_event_user, test_disk_event_user_raw),
        ("router", test_disk_event_router, test_disk_event_router_raw),
        ("wireless", test_disk_event_wireless, test_disk_event_wireless_raw),
        ("endpoint", test_disk_event_endpoint, test_disk_event_endpoint_raw),
        ("ha", test_disk_event_ha, test_disk_event_ha_raw),
        ("security-rating", test_disk_event_security_rating, test_disk_event_security_rating_raw),
        ("fortiextender", test_disk_event_fortiextender, test_disk_event_fortiextender_raw),
        ("connector", test_disk_event_connector, test_disk_event_connector_raw),
    ]
    
    print("\n=== Log Types ===")
    for name, formatted_fn, raw_fn in log_type_tests:
        # Test formatted
        try:
            formatted_fn()
            print(f"  ✓ disk/{name} (formatted)")
            passed += 1
        except Exception as e:
            if "404" in str(e):
                print(f"  ○ disk/{name} (formatted): Not available")
                skipped += 1
            else:
                print(f"  ✗ disk/{name} (formatted): {e}")
                failed += 1
        # Test raw
        try:
            raw_fn()
            print(f"  ✓ disk/{name} (raw)")
            passed += 1
        except Exception as e:
            if "404" in str(e):
                print(f"  ○ disk/{name} (raw): Not available")
                skipped += 1
            else:
                print(f"  ✗ disk/{name} (raw): {e}")
                failed += 1
    
    print("\n=== Traffic Subtypes ===")
    for name, formatted_fn, raw_fn in traffic_tests:
        try:
            formatted_fn()
            print(f"  ✓ disk/traffic/{name} (formatted)")
            passed += 1
        except Exception as e:
            if "404" in str(e):
                print(f"  ○ disk/traffic/{name} (formatted): Not available")
                skipped += 1
            else:
                print(f"  ✗ disk/traffic/{name} (formatted): {e}")
                failed += 1
        try:
            raw_fn()
            print(f"  ✓ disk/traffic/{name} (raw)")
            passed += 1
        except Exception as e:
            if "404" in str(e):
                print(f"  ○ disk/traffic/{name} (raw): Not available")
                skipped += 1
            else:
                print(f"  ✗ disk/traffic/{name} (raw): {e}")
                failed += 1
    
    print("\n=== Event Subtypes ===")
    for name, formatted_fn, raw_fn in event_tests:
        try:
            formatted_fn()
            print(f"  ✓ disk/event/{name} (formatted)")
            passed += 1
        except Exception as e:
            if "404" in str(e):
                print(f"  ○ disk/event/{name} (formatted): Not available")
                skipped += 1
            else:
                print(f"  ✗ disk/event/{name} (formatted): {e}")
                failed += 1
        try:
            raw_fn()
            print(f"  ✓ disk/event/{name} (raw)")
            passed += 1
        except Exception as e:
            if "404" in str(e):
                print(f"  ○ disk/event/{name} (raw): Not available")
                skipped += 1
            else:
                print(f"  ✗ disk/event/{name} (raw): {e}")
                failed += 1
    
    print("\n" + "=" * 60)
    print(f"Results: {passed} passed, {failed} failed, {skipped} skipped")
    print(f"Total: {passed + failed + skipped} tests")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
