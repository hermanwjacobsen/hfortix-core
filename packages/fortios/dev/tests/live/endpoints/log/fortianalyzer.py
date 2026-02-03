#!/usr/bin/env python
"""Test log/fortianalyzer API endpoints (both raw and formatted versions)."""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt

# ============================================================================
# LOG TYPE TESTS - Formatted (non-raw)
# ============================================================================

def test_fortianalyzer_virus():
    """Test: Get fortianalyzer virus logs (formatted)"""
    result = fgt.api.log.fortianalyzer.virus.get()
    assert result.http_status == "success"

def test_fortianalyzer_webfilter():
    """Test: Get fortianalyzer webfilter logs (formatted)"""
    result = fgt.api.log.fortianalyzer.webfilter.get()
    assert result.http_status == "success"

def test_fortianalyzer_waf():
    """Test: Get fortianalyzer WAF logs (formatted)"""
    result = fgt.api.log.fortianalyzer.waf.get()
    assert result.http_status == "success"

def test_fortianalyzer_ips():
    """Test: Get fortianalyzer IPS logs (formatted)"""
    result = fgt.api.log.fortianalyzer.ips.get()
    assert result.http_status == "success"

def test_fortianalyzer_anomaly():
    """Test: Get fortianalyzer anomaly logs (formatted)"""
    result = fgt.api.log.fortianalyzer.anomaly.get()
    assert result.http_status == "success"

def test_fortianalyzer_app_ctrl():
    """Test: Get fortianalyzer app-ctrl logs (formatted)"""
    result = fgt.api.log.fortianalyzer.app_ctrl.get()
    assert result.http_status == "success"

def test_fortianalyzer_emailfilter():
    """Test: Get fortianalyzer emailfilter logs (formatted)"""
    result = fgt.api.log.fortianalyzer.emailfilter.get()
    assert result.http_status == "success"

def test_fortianalyzer_dlp():
    """Test: Get fortianalyzer DLP logs (formatted)"""
    result = fgt.api.log.fortianalyzer.dlp.get()
    assert result.http_status == "success"

def test_fortianalyzer_voip():
    """Test: Get fortianalyzer VoIP logs (formatted)"""
    result = fgt.api.log.fortianalyzer.voip.get()
    assert result.http_status == "success"

def test_fortianalyzer_gtp():
    """Test: Get fortianalyzer GTP logs (formatted)"""
    result = fgt.api.log.fortianalyzer.gtp.get()
    assert result.http_status == "success"

def test_fortianalyzer_dns():
    """Test: Get fortianalyzer DNS logs (formatted)"""
    result = fgt.api.log.fortianalyzer.dns.get()
    assert result.http_status == "success"

def test_fortianalyzer_ssh():
    """Test: Get fortianalyzer SSH logs (formatted)"""
    result = fgt.api.log.fortianalyzer.ssh.get()
    assert result.http_status == "success"

def test_fortianalyzer_ssl():
    """Test: Get fortianalyzer SSL logs (formatted)"""
    result = fgt.api.log.fortianalyzer.ssl.get()
    assert result.http_status == "success"

def test_fortianalyzer_file_filter():
    """Test: Get fortianalyzer file-filter logs (formatted)"""
    result = fgt.api.log.fortianalyzer.file_filter.get()
    assert result.http_status == "success"

# ============================================================================
# LOG TYPE TESTS - Raw format
# ============================================================================

def test_fortianalyzer_virus_raw():
    """Test: Get fortianalyzer virus logs (raw)"""
    result = fgt.api.log.fortianalyzer.virus.raw.get()
    assert result.http_status == "success"

def test_fortianalyzer_webfilter_raw():
    """Test: Get fortianalyzer webfilter logs (raw)"""
    result = fgt.api.log.fortianalyzer.webfilter.raw.get()
    assert result.http_status == "success"

def test_fortianalyzer_waf_raw():
    """Test: Get fortianalyzer WAF logs (raw)"""
    result = fgt.api.log.fortianalyzer.waf.raw.get()
    assert result.http_status == "success"

def test_fortianalyzer_ips_raw():
    """Test: Get fortianalyzer IPS logs (raw)"""
    result = fgt.api.log.fortianalyzer.ips.raw.get()
    assert result.http_status == "success"

def test_fortianalyzer_anomaly_raw():
    """Test: Get fortianalyzer anomaly logs (raw)"""
    result = fgt.api.log.fortianalyzer.anomaly.raw.get()
    assert result.http_status == "success"

def test_fortianalyzer_app_ctrl_raw():
    """Test: Get fortianalyzer app-ctrl logs (raw)"""
    result = fgt.api.log.fortianalyzer.app_ctrl.raw.get()
    assert result.http_status == "success"

def test_fortianalyzer_emailfilter_raw():
    """Test: Get fortianalyzer emailfilter logs (raw)"""
    result = fgt.api.log.fortianalyzer.emailfilter.raw.get()
    assert result.http_status == "success"

def test_fortianalyzer_dlp_raw():
    """Test: Get fortianalyzer DLP logs (raw)"""
    result = fgt.api.log.fortianalyzer.dlp.raw.get()
    assert result.http_status == "success"

def test_fortianalyzer_voip_raw():
    """Test: Get fortianalyzer VoIP logs (raw)"""
    result = fgt.api.log.fortianalyzer.voip.raw.get()
    assert result.http_status == "success"

def test_fortianalyzer_gtp_raw():
    """Test: Get fortianalyzer GTP logs (raw)"""
    result = fgt.api.log.fortianalyzer.gtp.raw.get()
    assert result.http_status == "success"

def test_fortianalyzer_dns_raw():
    """Test: Get fortianalyzer DNS logs (raw)"""
    result = fgt.api.log.fortianalyzer.dns.raw.get()
    assert result.http_status == "success"

def test_fortianalyzer_ssh_raw():
    """Test: Get fortianalyzer SSH logs (raw)"""
    result = fgt.api.log.fortianalyzer.ssh.raw.get()
    assert result.http_status == "success"

def test_fortianalyzer_ssl_raw():
    """Test: Get fortianalyzer SSL logs (raw)"""
    result = fgt.api.log.fortianalyzer.ssl.raw.get()
    assert result.http_status == "success"

def test_fortianalyzer_file_filter_raw():
    """Test: Get fortianalyzer file-filter logs (raw)"""
    result = fgt.api.log.fortianalyzer.file_filter.raw.get()
    assert result.http_status == "success"

# ============================================================================
# TRAFFIC SUBTYPE TESTS - Formatted (non-raw)
# ============================================================================

def test_fortianalyzer_traffic_forward():
    """Test: Get fortianalyzer traffic/forward logs (formatted)"""
    result = fgt.api.log.fortianalyzer.traffic.forward.get(rows=5)
    assert result.http_status == "success"

def test_fortianalyzer_traffic_local():
    """Test: Get fortianalyzer traffic/local logs (formatted)"""
    result = fgt.api.log.fortianalyzer.traffic.local.get(rows=5)
    assert result.http_status == "success"

def test_fortianalyzer_traffic_multicast():
    """Test: Get fortianalyzer traffic/multicast logs (formatted)"""
    result = fgt.api.log.fortianalyzer.traffic.multicast.get(rows=5)
    assert result.http_status == "success"

def test_fortianalyzer_traffic_sniffer():
    """Test: Get fortianalyzer traffic/sniffer logs (formatted)"""
    result = fgt.api.log.fortianalyzer.traffic.sniffer.get(rows=5)
    assert result.http_status == "success"

def test_fortianalyzer_traffic_fortiview():
    """Test: Get fortianalyzer traffic/fortiview logs (formatted)"""
    result = fgt.api.log.fortianalyzer.traffic.fortiview.get(rows=5)
    assert result.http_status == "success"

def test_fortianalyzer_traffic_threat():
    """Test: Get fortianalyzer traffic/threat logs (formatted)"""
    result = fgt.api.log.fortianalyzer.traffic.threat.get(rows=5)
    assert result.http_status == "success"

# ============================================================================
# TRAFFIC SUBTYPE TESTS - Raw format
# ============================================================================

def test_fortianalyzer_traffic_forward_raw():
    """Test: Get fortianalyzer traffic/forward logs (raw)"""
    result = fgt.api.log.fortianalyzer.traffic.forward.raw.get(rows=5)
    assert result.http_status == "success"

def test_fortianalyzer_traffic_local_raw():
    """Test: Get fortianalyzer traffic/local logs (raw)"""
    result = fgt.api.log.fortianalyzer.traffic.local.raw.get(rows=5)
    assert result.http_status == "success"

def test_fortianalyzer_traffic_multicast_raw():
    """Test: Get fortianalyzer traffic/multicast logs (raw)"""
    result = fgt.api.log.fortianalyzer.traffic.multicast.raw.get(rows=5)
    assert result.http_status == "success"

def test_fortianalyzer_traffic_sniffer_raw():
    """Test: Get fortianalyzer traffic/sniffer logs (raw)"""
    result = fgt.api.log.fortianalyzer.traffic.sniffer.raw.get(rows=5)
    assert result.http_status == "success"

def test_fortianalyzer_traffic_fortiview_raw():
    """Test: Get fortianalyzer traffic/fortiview logs (raw)"""
    result = fgt.api.log.fortianalyzer.traffic.fortiview.raw.get(rows=5)
    assert result.http_status == "success"

def test_fortianalyzer_traffic_threat_raw():
    """Test: Get fortianalyzer traffic/threat logs (raw)"""
    result = fgt.api.log.fortianalyzer.traffic.threat.raw.get(rows=5)
    assert result.http_status == "success"

# ============================================================================
# EVENT SUBTYPE TESTS - Formatted (non-raw)
# ============================================================================

def test_fortianalyzer_event_system():
    """Test: Get fortianalyzer event/system logs (formatted)"""
    result = fgt.api.log.fortianalyzer.event.system.get(rows=5)
    assert result.http_status == "success"

def test_fortianalyzer_event_vpn():
    """Test: Get fortianalyzer event/vpn logs (formatted)"""
    result = fgt.api.log.fortianalyzer.event.vpn.get(rows=5)
    assert result.http_status == "success"

def test_fortianalyzer_event_user():
    """Test: Get fortianalyzer event/user logs (formatted)"""
    result = fgt.api.log.fortianalyzer.event.user.get(rows=5)
    assert result.http_status == "success"

def test_fortianalyzer_event_router():
    """Test: Get fortianalyzer event/router logs (formatted)"""
    result = fgt.api.log.fortianalyzer.event.router.get(rows=5)
    assert result.http_status == "success"

def test_fortianalyzer_event_wireless():
    """Test: Get fortianalyzer event/wireless logs (formatted)"""
    result = fgt.api.log.fortianalyzer.event.wireless.get(rows=5)
    assert result.http_status == "success"

def test_fortianalyzer_event_endpoint():
    """Test: Get fortianalyzer event/endpoint logs (formatted)"""
    result = fgt.api.log.fortianalyzer.event.endpoint.get(rows=5)
    assert result.http_status == "success"

def test_fortianalyzer_event_ha():
    """Test: Get fortianalyzer event/ha logs (formatted)"""
    result = fgt.api.log.fortianalyzer.event.ha.get(rows=5)
    assert result.http_status == "success"

def test_fortianalyzer_event_security_rating():
    """Test: Get fortianalyzer event/security-rating logs (formatted)"""
    result = fgt.api.log.fortianalyzer.event.security_rating.get(rows=5)
    assert result.http_status == "success"

def test_fortianalyzer_event_fortiextender():
    """Test: Get fortianalyzer event/fortiextender logs (formatted)"""
    result = fgt.api.log.fortianalyzer.event.fortiextender.get(rows=5)
    assert result.http_status == "success"

def test_fortianalyzer_event_connector():
    """Test: Get fortianalyzer event/connector logs (formatted)"""
    result = fgt.api.log.fortianalyzer.event.connector.get(rows=5)
    assert result.http_status == "success"

# ============================================================================
# EVENT SUBTYPE TESTS - Raw format
# ============================================================================

def test_fortianalyzer_event_system_raw():
    """Test: Get fortianalyzer event/system logs (raw)"""
    result = fgt.api.log.fortianalyzer.event.system.raw.get(rows=5)
    assert result.http_status == "success"

def test_fortianalyzer_event_vpn_raw():
    """Test: Get fortianalyzer event/vpn logs (raw)"""
    result = fgt.api.log.fortianalyzer.event.vpn.raw.get(rows=5)
    assert result.http_status == "success"

def test_fortianalyzer_event_user_raw():
    """Test: Get fortianalyzer event/user logs (raw)"""
    result = fgt.api.log.fortianalyzer.event.user.raw.get(rows=5)
    assert result.http_status == "success"

def test_fortianalyzer_event_router_raw():
    """Test: Get fortianalyzer event/router logs (raw)"""
    result = fgt.api.log.fortianalyzer.event.router.raw.get(rows=5)
    assert result.http_status == "success"

def test_fortianalyzer_event_wireless_raw():
    """Test: Get fortianalyzer event/wireless logs (raw)"""
    result = fgt.api.log.fortianalyzer.event.wireless.raw.get(rows=5)
    assert result.http_status == "success"

def test_fortianalyzer_event_endpoint_raw():
    """Test: Get fortianalyzer event/endpoint logs (raw)"""
    result = fgt.api.log.fortianalyzer.event.endpoint.raw.get(rows=5)
    assert result.http_status == "success"

def test_fortianalyzer_event_ha_raw():
    """Test: Get fortianalyzer event/ha logs (raw)"""
    result = fgt.api.log.fortianalyzer.event.ha.raw.get(rows=5)
    assert result.http_status == "success"

def test_fortianalyzer_event_security_rating_raw():
    """Test: Get fortianalyzer event/security-rating logs (raw)"""
    result = fgt.api.log.fortianalyzer.event.security_rating.raw.get(rows=5)
    assert result.http_status == "success"

def test_fortianalyzer_event_fortiextender_raw():
    """Test: Get fortianalyzer event/fortiextender logs (raw)"""
    result = fgt.api.log.fortianalyzer.event.fortiextender.raw.get(rows=5)
    assert result.http_status == "success"

def test_fortianalyzer_event_connector_raw():
    """Test: Get fortianalyzer event/connector logs (raw)"""
    result = fgt.api.log.fortianalyzer.event.connector.raw.get(rows=5)
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
    print("Testing log/fortianalyzer API endpoints (raw and formatted)...")
    print("=" * 60)
    
    passed = 0
    failed = 0
    skipped = 0
    
    # All test functions grouped by category
    log_type_tests = [
        ("virus", test_fortianalyzer_virus, test_fortianalyzer_virus_raw),
        ("webfilter", test_fortianalyzer_webfilter, test_fortianalyzer_webfilter_raw),
        ("waf", test_fortianalyzer_waf, test_fortianalyzer_waf_raw),
        ("ips", test_fortianalyzer_ips, test_fortianalyzer_ips_raw),
        ("anomaly", test_fortianalyzer_anomaly, test_fortianalyzer_anomaly_raw),
        ("app-ctrl", test_fortianalyzer_app_ctrl, test_fortianalyzer_app_ctrl_raw),
        ("emailfilter", test_fortianalyzer_emailfilter, test_fortianalyzer_emailfilter_raw),
        ("dlp", test_fortianalyzer_dlp, test_fortianalyzer_dlp_raw),
        ("voip", test_fortianalyzer_voip, test_fortianalyzer_voip_raw),
        ("gtp", test_fortianalyzer_gtp, test_fortianalyzer_gtp_raw),
        ("dns", test_fortianalyzer_dns, test_fortianalyzer_dns_raw),
        ("ssh", test_fortianalyzer_ssh, test_fortianalyzer_ssh_raw),
        ("ssl", test_fortianalyzer_ssl, test_fortianalyzer_ssl_raw),
        ("file-filter", test_fortianalyzer_file_filter, test_fortianalyzer_file_filter_raw),
    ]
    
    traffic_tests = [
        ("forward", test_fortianalyzer_traffic_forward, test_fortianalyzer_traffic_forward_raw),
        ("local", test_fortianalyzer_traffic_local, test_fortianalyzer_traffic_local_raw),
        ("multicast", test_fortianalyzer_traffic_multicast, test_fortianalyzer_traffic_multicast_raw),
        ("sniffer", test_fortianalyzer_traffic_sniffer, test_fortianalyzer_traffic_sniffer_raw),
        ("fortiview", test_fortianalyzer_traffic_fortiview, test_fortianalyzer_traffic_fortiview_raw),
        ("threat", test_fortianalyzer_traffic_threat, test_fortianalyzer_traffic_threat_raw),
    ]
    
    event_tests = [
        ("system", test_fortianalyzer_event_system, test_fortianalyzer_event_system_raw),
        ("vpn", test_fortianalyzer_event_vpn, test_fortianalyzer_event_vpn_raw),
        ("user", test_fortianalyzer_event_user, test_fortianalyzer_event_user_raw),
        ("router", test_fortianalyzer_event_router, test_fortianalyzer_event_router_raw),
        ("wireless", test_fortianalyzer_event_wireless, test_fortianalyzer_event_wireless_raw),
        ("endpoint", test_fortianalyzer_event_endpoint, test_fortianalyzer_event_endpoint_raw),
        ("ha", test_fortianalyzer_event_ha, test_fortianalyzer_event_ha_raw),
        ("security-rating", test_fortianalyzer_event_security_rating, test_fortianalyzer_event_security_rating_raw),
        ("fortiextender", test_fortianalyzer_event_fortiextender, test_fortianalyzer_event_fortiextender_raw),
        ("connector", test_fortianalyzer_event_connector, test_fortianalyzer_event_connector_raw),
    ]
    
    print("\n=== Log Types ===")
    for name, formatted_fn, raw_fn in log_type_tests:
        # Test formatted
        try:
            formatted_fn()
            print(f"  ✓ fortianalyzer/{name} (formatted)")
            passed += 1
        except Exception as e:
            if "404" in str(e):
                print(f"  ○ fortianalyzer/{name} (formatted): Not available")
                skipped += 1
            else:
                print(f"  ✗ fortianalyzer/{name} (formatted): {e}")
                failed += 1
        # Test raw
        try:
            raw_fn()
            print(f"  ✓ fortianalyzer/{name} (raw)")
            passed += 1
        except Exception as e:
            if "404" in str(e):
                print(f"  ○ fortianalyzer/{name} (raw): Not available")
                skipped += 1
            else:
                print(f"  ✗ fortianalyzer/{name} (raw): {e}")
                failed += 1
    
    print("\n=== Traffic Subtypes ===")
    for name, formatted_fn, raw_fn in traffic_tests:
        try:
            formatted_fn()
            print(f"  ✓ fortianalyzer/traffic/{name} (formatted)")
            passed += 1
        except Exception as e:
            if "404" in str(e):
                print(f"  ○ fortianalyzer/traffic/{name} (formatted): Not available")
                skipped += 1
            else:
                print(f"  ✗ fortianalyzer/traffic/{name} (formatted): {e}")
                failed += 1
        try:
            raw_fn()
            print(f"  ✓ fortianalyzer/traffic/{name} (raw)")
            passed += 1
        except Exception as e:
            if "404" in str(e):
                print(f"  ○ fortianalyzer/traffic/{name} (raw): Not available")
                skipped += 1
            else:
                print(f"  ✗ fortianalyzer/traffic/{name} (raw): {e}")
                failed += 1
    
    print("\n=== Event Subtypes ===")
    for name, formatted_fn, raw_fn in event_tests:
        try:
            formatted_fn()
            print(f"  ✓ fortianalyzer/event/{name} (formatted)")
            passed += 1
        except Exception as e:
            if "404" in str(e):
                print(f"  ○ fortianalyzer/event/{name} (formatted): Not available")
                skipped += 1
            else:
                print(f"  ✗ fortianalyzer/event/{name} (formatted): {e}")
                failed += 1
        try:
            raw_fn()
            print(f"  ✓ fortianalyzer/event/{name} (raw)")
            passed += 1
        except Exception as e:
            if "404" in str(e):
                print(f"  ○ fortianalyzer/event/{name} (raw): Not available")
                skipped += 1
            else:
                print(f"  ✗ fortianalyzer/event/{name} (raw): {e}")
                failed += 1
    
    print("\n" + "=" * 60)
    print(f"Results: {passed} passed, {failed} failed, {skipped} skipped")
    print(f"Total: {passed + failed + skipped} tests")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
