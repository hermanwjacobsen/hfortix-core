#!/usr/bin/env python
"""Test log/forticloud API endpoints (both raw and formatted versions)."""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt

# ============================================================================
# LOG TYPE TESTS - Formatted (non-raw)
# ============================================================================

def test_forticloud_virus():
    """Test: Get forticloud virus logs (formatted)"""
    result = fgt.api.log.forticloud.virus.get()
    assert result.http_status == "success"

def test_forticloud_webfilter():
    """Test: Get forticloud webfilter logs (formatted)"""
    result = fgt.api.log.forticloud.webfilter.get()
    assert result.http_status == "success"

def test_forticloud_waf():
    """Test: Get forticloud WAF logs (formatted)"""
    result = fgt.api.log.forticloud.waf.get()
    assert result.http_status == "success"

def test_forticloud_ips():
    """Test: Get forticloud IPS logs (formatted)"""
    result = fgt.api.log.forticloud.ips.get()
    assert result.http_status == "success"

def test_forticloud_anomaly():
    """Test: Get forticloud anomaly logs (formatted)"""
    result = fgt.api.log.forticloud.anomaly.get()
    assert result.http_status == "success"

def test_forticloud_app_ctrl():
    """Test: Get forticloud app-ctrl logs (formatted)"""
    result = fgt.api.log.forticloud.app_ctrl.get()
    assert result.http_status == "success"

def test_forticloud_emailfilter():
    """Test: Get forticloud emailfilter logs (formatted)"""
    result = fgt.api.log.forticloud.emailfilter.get()
    assert result.http_status == "success"

def test_forticloud_dlp():
    """Test: Get forticloud DLP logs (formatted)"""
    result = fgt.api.log.forticloud.dlp.get()
    assert result.http_status == "success"

def test_forticloud_voip():
    """Test: Get forticloud VoIP logs (formatted)"""
    result = fgt.api.log.forticloud.voip.get()
    assert result.http_status == "success"

def test_forticloud_gtp():
    """Test: Get forticloud GTP logs (formatted)"""
    result = fgt.api.log.forticloud.gtp.get()
    assert result.http_status == "success"

def test_forticloud_dns():
    """Test: Get forticloud DNS logs (formatted)"""
    result = fgt.api.log.forticloud.dns.get()
    assert result.http_status == "success"

def test_forticloud_ssh():
    """Test: Get forticloud SSH logs (formatted)"""
    result = fgt.api.log.forticloud.ssh.get()
    assert result.http_status == "success"

def test_forticloud_ssl():
    """Test: Get forticloud SSL logs (formatted)"""
    result = fgt.api.log.forticloud.ssl.get()
    assert result.http_status == "success"

def test_forticloud_file_filter():
    """Test: Get forticloud file-filter logs (formatted)"""
    result = fgt.api.log.forticloud.file_filter.get()
    assert result.http_status == "success"

# ============================================================================
# LOG TYPE TESTS - Raw format
# ============================================================================

def test_forticloud_virus_raw():
    """Test: Get forticloud virus logs (raw)"""
    result = fgt.api.log.forticloud.virus.raw.get()
    assert result.http_status == "success"

def test_forticloud_webfilter_raw():
    """Test: Get forticloud webfilter logs (raw)"""
    result = fgt.api.log.forticloud.webfilter.raw.get()
    assert result.http_status == "success"

def test_forticloud_waf_raw():
    """Test: Get forticloud WAF logs (raw)"""
    result = fgt.api.log.forticloud.waf.raw.get()
    assert result.http_status == "success"

def test_forticloud_ips_raw():
    """Test: Get forticloud IPS logs (raw)"""
    result = fgt.api.log.forticloud.ips.raw.get()
    assert result.http_status == "success"

def test_forticloud_anomaly_raw():
    """Test: Get forticloud anomaly logs (raw)"""
    result = fgt.api.log.forticloud.anomaly.raw.get()
    assert result.http_status == "success"

def test_forticloud_app_ctrl_raw():
    """Test: Get forticloud app-ctrl logs (raw)"""
    result = fgt.api.log.forticloud.app_ctrl.raw.get()
    assert result.http_status == "success"

def test_forticloud_emailfilter_raw():
    """Test: Get forticloud emailfilter logs (raw)"""
    result = fgt.api.log.forticloud.emailfilter.raw.get()
    assert result.http_status == "success"

def test_forticloud_dlp_raw():
    """Test: Get forticloud DLP logs (raw)"""
    result = fgt.api.log.forticloud.dlp.raw.get()
    assert result.http_status == "success"

def test_forticloud_voip_raw():
    """Test: Get forticloud VoIP logs (raw)"""
    result = fgt.api.log.forticloud.voip.raw.get()
    assert result.http_status == "success"

def test_forticloud_gtp_raw():
    """Test: Get forticloud GTP logs (raw)"""
    result = fgt.api.log.forticloud.gtp.raw.get()
    assert result.http_status == "success"

def test_forticloud_dns_raw():
    """Test: Get forticloud DNS logs (raw)"""
    result = fgt.api.log.forticloud.dns.raw.get()
    assert result.http_status == "success"

def test_forticloud_ssh_raw():
    """Test: Get forticloud SSH logs (raw)"""
    result = fgt.api.log.forticloud.ssh.raw.get()
    assert result.http_status == "success"

def test_forticloud_ssl_raw():
    """Test: Get forticloud SSL logs (raw)"""
    result = fgt.api.log.forticloud.ssl.raw.get()
    assert result.http_status == "success"

def test_forticloud_file_filter_raw():
    """Test: Get forticloud file-filter logs (raw)"""
    result = fgt.api.log.forticloud.file_filter.raw.get()
    assert result.http_status == "success"

# ============================================================================
# TRAFFIC SUBTYPE TESTS - Formatted (non-raw)
# ============================================================================

def test_forticloud_traffic_forward():
    """Test: Get forticloud traffic/forward logs (formatted)"""
    result = fgt.api.log.forticloud.traffic.forward.get(rows=5)
    assert result.http_status == "success"

def test_forticloud_traffic_local():
    """Test: Get forticloud traffic/local logs (formatted)"""
    result = fgt.api.log.forticloud.traffic.local.get(rows=5)
    assert result.http_status == "success"

def test_forticloud_traffic_multicast():
    """Test: Get forticloud traffic/multicast logs (formatted)"""
    result = fgt.api.log.forticloud.traffic.multicast.get(rows=5)
    assert result.http_status == "success"

def test_forticloud_traffic_sniffer():
    """Test: Get forticloud traffic/sniffer logs (formatted)"""
    result = fgt.api.log.forticloud.traffic.sniffer.get(rows=5)
    assert result.http_status == "success"

def test_forticloud_traffic_fortiview():
    """Test: Get forticloud traffic/fortiview logs (formatted)"""
    result = fgt.api.log.forticloud.traffic.fortiview.get(rows=5)
    assert result.http_status == "success"

def test_forticloud_traffic_threat():
    """Test: Get forticloud traffic/threat logs (formatted)"""
    result = fgt.api.log.forticloud.traffic.threat.get(rows=5)
    assert result.http_status == "success"

# ============================================================================
# TRAFFIC SUBTYPE TESTS - Raw format
# ============================================================================

def test_forticloud_traffic_forward_raw():
    """Test: Get forticloud traffic/forward logs (raw)"""
    result = fgt.api.log.forticloud.traffic.forward.raw.get(rows=5)
    assert result.http_status == "success"

def test_forticloud_traffic_local_raw():
    """Test: Get forticloud traffic/local logs (raw)"""
    result = fgt.api.log.forticloud.traffic.local.raw.get(rows=5)
    assert result.http_status == "success"

def test_forticloud_traffic_multicast_raw():
    """Test: Get forticloud traffic/multicast logs (raw)"""
    result = fgt.api.log.forticloud.traffic.multicast.raw.get(rows=5)
    assert result.http_status == "success"

def test_forticloud_traffic_sniffer_raw():
    """Test: Get forticloud traffic/sniffer logs (raw)"""
    result = fgt.api.log.forticloud.traffic.sniffer.raw.get(rows=5)
    assert result.http_status == "success"

def test_forticloud_traffic_fortiview_raw():
    """Test: Get forticloud traffic/fortiview logs (raw)"""
    result = fgt.api.log.forticloud.traffic.fortiview.raw.get(rows=5)
    assert result.http_status == "success"

def test_forticloud_traffic_threat_raw():
    """Test: Get forticloud traffic/threat logs (raw)"""
    result = fgt.api.log.forticloud.traffic.threat.raw.get(rows=5)
    assert result.http_status == "success"

# ============================================================================
# EVENT SUBTYPE TESTS - Formatted (non-raw)
# ============================================================================

def test_forticloud_event_system():
    """Test: Get forticloud event/system logs (formatted)"""
    result = fgt.api.log.forticloud.event.system.get(rows=5)
    assert result.http_status == "success"

def test_forticloud_event_vpn():
    """Test: Get forticloud event/vpn logs (formatted)"""
    result = fgt.api.log.forticloud.event.vpn.get(rows=5)
    assert result.http_status == "success"

def test_forticloud_event_user():
    """Test: Get forticloud event/user logs (formatted)"""
    result = fgt.api.log.forticloud.event.user.get(rows=5)
    assert result.http_status == "success"

def test_forticloud_event_router():
    """Test: Get forticloud event/router logs (formatted)"""
    result = fgt.api.log.forticloud.event.router.get(rows=5)
    assert result.http_status == "success"

def test_forticloud_event_wireless():
    """Test: Get forticloud event/wireless logs (formatted)"""
    result = fgt.api.log.forticloud.event.wireless.get(rows=5)
    assert result.http_status == "success"

def test_forticloud_event_endpoint():
    """Test: Get forticloud event/endpoint logs (formatted)"""
    result = fgt.api.log.forticloud.event.endpoint.get(rows=5)
    assert result.http_status == "success"

def test_forticloud_event_ha():
    """Test: Get forticloud event/ha logs (formatted)"""
    result = fgt.api.log.forticloud.event.ha.get(rows=5)
    assert result.http_status == "success"

def test_forticloud_event_security_rating():
    """Test: Get forticloud event/security-rating logs (formatted)"""
    result = fgt.api.log.forticloud.event.security_rating.get(rows=5)
    assert result.http_status == "success"

def test_forticloud_event_fortiextender():
    """Test: Get forticloud event/fortiextender logs (formatted)"""
    result = fgt.api.log.forticloud.event.fortiextender.get(rows=5)
    assert result.http_status == "success"

def test_forticloud_event_connector():
    """Test: Get forticloud event/connector logs (formatted)"""
    result = fgt.api.log.forticloud.event.connector.get(rows=5)
    assert result.http_status == "success"

# ============================================================================
# EVENT SUBTYPE TESTS - Raw format
# ============================================================================

def test_forticloud_event_system_raw():
    """Test: Get forticloud event/system logs (raw)"""
    result = fgt.api.log.forticloud.event.system.raw.get(rows=5)
    assert result.http_status == "success"

def test_forticloud_event_vpn_raw():
    """Test: Get forticloud event/vpn logs (raw)"""
    result = fgt.api.log.forticloud.event.vpn.raw.get(rows=5)
    assert result.http_status == "success"

def test_forticloud_event_user_raw():
    """Test: Get forticloud event/user logs (raw)"""
    result = fgt.api.log.forticloud.event.user.raw.get(rows=5)
    assert result.http_status == "success"

def test_forticloud_event_router_raw():
    """Test: Get forticloud event/router logs (raw)"""
    result = fgt.api.log.forticloud.event.router.raw.get(rows=5)
    assert result.http_status == "success"

def test_forticloud_event_wireless_raw():
    """Test: Get forticloud event/wireless logs (raw)"""
    result = fgt.api.log.forticloud.event.wireless.raw.get(rows=5)
    assert result.http_status == "success"

def test_forticloud_event_endpoint_raw():
    """Test: Get forticloud event/endpoint logs (raw)"""
    result = fgt.api.log.forticloud.event.endpoint.raw.get(rows=5)
    assert result.http_status == "success"

def test_forticloud_event_ha_raw():
    """Test: Get forticloud event/ha logs (raw)"""
    result = fgt.api.log.forticloud.event.ha.raw.get(rows=5)
    assert result.http_status == "success"

def test_forticloud_event_security_rating_raw():
    """Test: Get forticloud event/security-rating logs (raw)"""
    result = fgt.api.log.forticloud.event.security_rating.raw.get(rows=5)
    assert result.http_status == "success"

def test_forticloud_event_fortiextender_raw():
    """Test: Get forticloud event/fortiextender logs (raw)"""
    result = fgt.api.log.forticloud.event.fortiextender.raw.get(rows=5)
    assert result.http_status == "success"

def test_forticloud_event_connector_raw():
    """Test: Get forticloud event/connector logs (raw)"""
    result = fgt.api.log.forticloud.event.connector.raw.get(rows=5)
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
    print("Testing log/forticloud API endpoints (raw and formatted)...")
    print("=" * 60)
    
    passed = 0
    failed = 0
    skipped = 0
    
    # All test functions grouped by category
    log_type_tests = [
        ("virus", test_forticloud_virus, test_forticloud_virus_raw),
        ("webfilter", test_forticloud_webfilter, test_forticloud_webfilter_raw),
        ("waf", test_forticloud_waf, test_forticloud_waf_raw),
        ("ips", test_forticloud_ips, test_forticloud_ips_raw),
        ("anomaly", test_forticloud_anomaly, test_forticloud_anomaly_raw),
        ("app-ctrl", test_forticloud_app_ctrl, test_forticloud_app_ctrl_raw),
        ("emailfilter", test_forticloud_emailfilter, test_forticloud_emailfilter_raw),
        ("dlp", test_forticloud_dlp, test_forticloud_dlp_raw),
        ("voip", test_forticloud_voip, test_forticloud_voip_raw),
        ("gtp", test_forticloud_gtp, test_forticloud_gtp_raw),
        ("dns", test_forticloud_dns, test_forticloud_dns_raw),
        ("ssh", test_forticloud_ssh, test_forticloud_ssh_raw),
        ("ssl", test_forticloud_ssl, test_forticloud_ssl_raw),
        ("file-filter", test_forticloud_file_filter, test_forticloud_file_filter_raw),
    ]
    
    traffic_tests = [
        ("forward", test_forticloud_traffic_forward, test_forticloud_traffic_forward_raw),
        ("local", test_forticloud_traffic_local, test_forticloud_traffic_local_raw),
        ("multicast", test_forticloud_traffic_multicast, test_forticloud_traffic_multicast_raw),
        ("sniffer", test_forticloud_traffic_sniffer, test_forticloud_traffic_sniffer_raw),
        ("fortiview", test_forticloud_traffic_fortiview, test_forticloud_traffic_fortiview_raw),
        ("threat", test_forticloud_traffic_threat, test_forticloud_traffic_threat_raw),
    ]
    
    event_tests = [
        ("system", test_forticloud_event_system, test_forticloud_event_system_raw),
        ("vpn", test_forticloud_event_vpn, test_forticloud_event_vpn_raw),
        ("user", test_forticloud_event_user, test_forticloud_event_user_raw),
        ("router", test_forticloud_event_router, test_forticloud_event_router_raw),
        ("wireless", test_forticloud_event_wireless, test_forticloud_event_wireless_raw),
        ("endpoint", test_forticloud_event_endpoint, test_forticloud_event_endpoint_raw),
        ("ha", test_forticloud_event_ha, test_forticloud_event_ha_raw),
        ("security-rating", test_forticloud_event_security_rating, test_forticloud_event_security_rating_raw),
        ("fortiextender", test_forticloud_event_fortiextender, test_forticloud_event_fortiextender_raw),
        ("connector", test_forticloud_event_connector, test_forticloud_event_connector_raw),
    ]
    
    print("\n=== Log Types ===")
    for name, formatted_fn, raw_fn in log_type_tests:
        # Test formatted
        try:
            formatted_fn()
            print(f"  ✓ forticloud/{name} (formatted)")
            passed += 1
        except Exception as e:
            if "404" in str(e):
                print(f"  ○ forticloud/{name} (formatted): Not available")
                skipped += 1
            else:
                print(f"  ✗ forticloud/{name} (formatted): {e}")
                failed += 1
        # Test raw
        try:
            raw_fn()
            print(f"  ✓ forticloud/{name} (raw)")
            passed += 1
        except Exception as e:
            if "404" in str(e):
                print(f"  ○ forticloud/{name} (raw): Not available")
                skipped += 1
            else:
                print(f"  ✗ forticloud/{name} (raw): {e}")
                failed += 1
    
    print("\n=== Traffic Subtypes ===")
    for name, formatted_fn, raw_fn in traffic_tests:
        try:
            formatted_fn()
            print(f"  ✓ forticloud/traffic/{name} (formatted)")
            passed += 1
        except Exception as e:
            if "404" in str(e):
                print(f"  ○ forticloud/traffic/{name} (formatted): Not available")
                skipped += 1
            else:
                print(f"  ✗ forticloud/traffic/{name} (formatted): {e}")
                failed += 1
        try:
            raw_fn()
            print(f"  ✓ forticloud/traffic/{name} (raw)")
            passed += 1
        except Exception as e:
            if "404" in str(e):
                print(f"  ○ forticloud/traffic/{name} (raw): Not available")
                skipped += 1
            else:
                print(f"  ✗ forticloud/traffic/{name} (raw): {e}")
                failed += 1
    
    print("\n=== Event Subtypes ===")
    for name, formatted_fn, raw_fn in event_tests:
        try:
            formatted_fn()
            print(f"  ✓ forticloud/event/{name} (formatted)")
            passed += 1
        except Exception as e:
            if "404" in str(e):
                print(f"  ○ forticloud/event/{name} (formatted): Not available")
                skipped += 1
            else:
                print(f"  ✗ forticloud/event/{name} (formatted): {e}")
                failed += 1
        try:
            raw_fn()
            print(f"  ✓ forticloud/event/{name} (raw)")
            passed += 1
        except Exception as e:
            if "404" in str(e):
                print(f"  ○ forticloud/event/{name} (raw): Not available")
                skipped += 1
            else:
                print(f"  ✗ forticloud/event/{name} (raw): {e}")
                failed += 1
    
    print("\n" + "=" * 60)
    print(f"Results: {passed} passed, {failed} failed, {skipped} skipped")
    print(f"Total: {passed + failed + skipped} tests")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
