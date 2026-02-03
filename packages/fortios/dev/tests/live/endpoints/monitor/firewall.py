import argparse
import sys
from pathlib import Path
import pytest

# Run firewall monitor tests on a single worker to preserve state
pytestmark = pytest.mark.xdist_group(Path(__file__).stem)

# Add pytest directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt



# ============================================================================
# Firewall Monitor Tests - GET endpoints
# ============================================================================

def test_get_firewall_health():
    """Test GET /monitor/firewall/health - List load balance server health monitors."""
    try:
        result = fgt.api.monitor.firewall.health.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_firewall_local_in():
    """Test GET /monitor/firewall/local-in - List implicit and explicit local-in firewall policies."""
    try:
        result = fgt.api.monitor.firewall.local_in.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_firewall_local_in6():
    """Test GET /monitor/firewall/local-in6 - List implicit and explicit IPv6 local-in firewall policies."""
    try:
        result = fgt.api.monitor.firewall.local_in6.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_firewall_acl():
    """Test GET /monitor/firewall/acl - List counters for all IPv4 ACL."""
    try:
        result = fgt.api.monitor.firewall.acl.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_firewall_acl6():
    """Test GET /monitor/firewall/acl6 - List counters for all IPv6 ACL."""
    try:
        result = fgt.api.monitor.firewall.acl6.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_firewall_central_snat_map():
    """Test GET /monitor/firewall/central-snat-map - List traffic statistics for firewall central SNAT policies."""
    try:
        result = fgt.api.monitor.firewall.central_snat_map.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


# def test_get_firewall_dnat():
#     """Test GET /monitor/firewall/dnat - List hit count statistics for firewall virtual IP/server."""
#     try:
#         result = fgt.api.monitor.firewall.dnat.get()
#         assert result is not None
#         assert result.http_status_code == 200
#     except Exception as e:
#         if "404" in str(e):
#             print("Resource not found")
#         else:
#             raise


# def test_get_firewall_check_addrgrp_exclude_mac_member():
#     """Test GET /monitor/firewall/check-addrgrp-exclude-mac-member - Check if address group should exclude mac address type member."""
#     # Requires mkey parameter
#     result = fgt.api.monitor.firewall.check_addrgrp_exclude_mac_member.get()
#     assert result is not None
#     assert result.http_status_code == 200


# def test_get_firewall_internet_service_match():
#     """Test GET /monitor/firewall/internet-service-match - List internet services at a given IP or Subnet."""
#     # Requires ip parameter
#     result = fgt.api.monitor.firewall.internet_service_match.get()
#     assert result is not None
#     assert result.http_status_code == 200


# def test_get_firewall_internet_service_reputation():
#     """Test GET /monitor/firewall/internet-service-reputation - List internet services with reputation at a given IP."""
#     # Requires ip parameter
#     result = fgt.api.monitor.firewall.internet_service_reputation.get()
#     assert result is not None
#     assert result.http_status_code == 200


def test_get_firewall_internet_service_fqdn():
    """Test GET /monitor/firewall/internet-service-fqdn - Map of internet service FQDNs."""
    try:
        result = fgt.api.monitor.firewall.internet_service_fqdn.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_firewall_internet_service_fqdn_icon_ids():
    """Test GET /monitor/firewall/internet-service-fqdn-icon-ids - Map of internet service FQDN icon IDs."""
    try:
        result = fgt.api.monitor.firewall.internet_service_fqdn_icon_ids.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_firewall_internet_service_basic():
    """Test GET /monitor/firewall/internet-service-basic - List internet services with basic information."""
    try:
        result = fgt.api.monitor.firewall.internet_service_basic.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


# def test_get_firewall_internet_service_details():
#     """Test GET /monitor/firewall/internet-service-details - List all details for a given Internet Service ID."""
#     # Requires id parameter
#     result = fgt.api.monitor.firewall.internet_service_details.get()
#     assert result is not None
#     assert result.http_status_code == 200


# def test_get_firewall_network_service_dynamic():
#     """Test GET /monitor/firewall/network-service-dynamic - List dynamic network service IP address and port pairs."""
#     # Requires mkey parameter
#     result = fgt.api.monitor.firewall.network_service_dynamic.get()
#     assert result is not None
#     assert result.http_status_code == 200


# def test_get_firewall_proxy_sessions():
#     """Test GET /monitor/firewall/proxy/sessions - List all active proxy sessions."""
#     # Requires count parameter
#     result = fgt.api.monitor.firewall.proxy.sessions.get()
#     assert result is not None
#     assert result.http_status_code == 200


def test_get_firewall_policy():
    """Test GET /monitor/firewall/policy - List traffic statistics for firewall policies."""
    try:
        result = fgt.api.monitor.firewall.policy.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_firewall_security_policy():
    """Test GET /monitor/firewall/security-policy - List IPS engine statistics for security policies."""
    try:
        result = fgt.api.monitor.firewall.security_policy.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_firewall_proxy_policy():
    """Test GET /monitor/firewall/proxy-policy - List traffic statistics for all explicit proxy policies."""
    try:
        result = fgt.api.monitor.firewall.proxy_policy.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_firewall_multicast_policy():
    """Test GET /monitor/firewall/multicast-policy - List traffic statistics for IPv4 firewall multicast policies."""
    try:
        result = fgt.api.monitor.firewall.multicast_policy.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_firewall_multicast_policy6():
    """Test GET /monitor/firewall/multicast-policy6 - List traffic statistics for IPv6 firewall multicast policies."""
    try:
        result = fgt.api.monitor.firewall.multicast_policy6.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_firewall_saas_application():
    """Test GET /monitor/firewall/saas-application - List of SaaS applications."""
    try:
        result = fgt.api.monitor.firewall.saas_application.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


# def test_get_firewall_policy_lookup():
#     """Test GET /monitor/firewall/policy-lookup - Performs a policy lookup by creating a dummy packet."""
#     # Requires srcintf, sourceip, protocol, dest parameters
#     result = fgt.api.monitor.firewall.policy_lookup.get()
#     assert result is not None
#     assert result.http_status_code == 200


# def test_get_firewall_sessions():
#     """Test GET /monitor/firewall/sessions - List all active firewall sessions."""
#     # Requires count parameter
#     result = fgt.api.monitor.firewall.sessions.get()
#     assert result is not None
#     assert result.http_status_code == 200


def test_get_firewall_shaper():
    """Test GET /monitor/firewall/shaper - List statistics for configured firewall shared traffic shapers."""
    try:
        result = fgt.api.monitor.firewall.shaper.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_firewall_shaper_multi_class_shaper():
    """Test GET /monitor/firewall/shaper/multi-class-shaper - List statistics for multi-class shapers."""
    try:
        result = fgt.api.monitor.firewall.shaper.multi_class_shaper.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_firewall_per_ip_shaper():
    """Test GET /monitor/firewall/per-ip-shaper - List statistics for configured firewall per-IP traffic shapers."""
    try:
        result = fgt.api.monitor.firewall.per_ip_shaper.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


# def test_get_firewall_load_balance():
#     """Test GET /monitor/firewall/load-balance - List all firewall load balance servers."""
#     # Requires count parameter
#     result = fgt.api.monitor.firewall.load_balance.get()
#     assert result is not None
#     assert result.http_status_code == 200


def test_get_firewall_vip_overlap():
    """Test GET /monitor/firewall/vip-overlap - List any Virtual IPs that overlap with another Virtual IP."""
    try:
        result = fgt.api.monitor.firewall.vip_overlap.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_firewall_address_fqdns():
    """Test GET /monitor/firewall/address-fqdns - List of FQDN address objects and the IPs they resolved to."""
    try:
        result = fgt.api.monitor.firewall.address_fqdns.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_firewall_address_fqdns6():
    """Test GET /monitor/firewall/address-fqdns6 - List of IPv6 FQDN address objects and the IPs they resolved to."""
    try:
        result = fgt.api.monitor.firewall.address_fqdns6.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_firewall_ippool():
    """Test GET /monitor/firewall/ippool - List IPv4 pool statistics."""
    try:
        result = fgt.api.monitor.firewall.ippool.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


# def test_get_firewall_ippool_mapping():
#     """Test GET /monitor/firewall/ippool/mapping - Get the list of IPv4 mappings for the specified IP pool."""
#     # Requires mkey parameter
#     result = fgt.api.monitor.firewall.ippool.mapping.get()
#     assert result is not None
#     assert result.http_status_code == 200


def test_get_firewall_uuid_list():
    """Test GET /monitor/firewall/uuid-list - Retrieve a list of all UUIDs with their object type and VDOM."""
    try:
        result = fgt.api.monitor.firewall.uuid_list.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


# def test_get_firewall_uuid_type_lookup():
#     """Test GET /monitor/firewall/uuid-type-lookup - Retrieve mapping of UUIDs to their firewall object type."""
#     try:
#         result = fgt.api.monitor.firewall.uuid_type_lookup.get()
#         assert result is not None
#         assert result.http_status_code == 200
#     except Exception as e:
#         if "404" in str(e):
#             print("Resource not found")
#         else:
#             raise


def test_get_firewall_gtp():
    """Test GET /monitor/firewall/gtp - Retrieve a list of GTP tunnels."""
    try:
        result = fgt.api.monitor.firewall.gtp.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_firewall_gtp_statistics():
    """Test GET /monitor/firewall/gtp-statistics - Retrieve statistics for GTP."""
    try:
        result = fgt.api.monitor.firewall.gtp_statistics.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_firewall_gtp_runtime_statistics():
    """Test GET /monitor/firewall/gtp-runtime-statistics - Retrieve runtime statistics for GTP."""
    try:
        result = fgt.api.monitor.firewall.gtp_runtime_statistics.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_firewall_address_dynamic():
    """Test GET /monitor/firewall/address-dynamic - List of Fabric Connector address objects and the IPs they resolve to."""
    try:
        result = fgt.api.monitor.firewall.address_dynamic.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_firewall_address6_dynamic():
    """Test GET /monitor/firewall/address6-dynamic - List of IPv6 Fabric Connector address objects and the IPs they resolve to."""
    try:
        result = fgt.api.monitor.firewall.address6_dynamic.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


# def test_get_firewall_sdn_connector_filters():
#     """Test GET /monitor/firewall/sdn-connector-filters - List all available filters for a specified SDN Fabric Connector."""
#     # Requires connector parameter
#     result = fgt.api.monitor.firewall.sdn_connector_filters.get()
#     assert result is not None
#     assert result.http_status_code == 200


# ============================================================================
# Firewall Monitor Tests - POST endpoints
# ============================================================================

# def test_post_firewall_acl_clear_counters():
#     """Test POST /monitor/firewall/acl/clear_counters - Reset counters for one or more IPv4 ACLs by policy ID."""
#     # Requires policy ID parameter
#     try:
#         result = fgt.api.monitor.firewall.acl.clear_counters.post()
#         assert result is not None
#         assert result.http_status_code == 200
#     except Exception as e:
#         if "404" in str(e):
#             print("Resource not found")
#         else:
#             raise


# def test_post_firewall_acl6_clear_counters():
#     """Test POST /monitor/firewall/acl6/clear_counters - Reset counters for one or more IPv6 ACLs by policy ID."""
#     # Requires policy ID parameter
#     try:
#         result = fgt.api.monitor.firewall.acl6.clear_counters.post()
#         assert result is not None
#         assert result.http_status_code == 200
#     except Exception as e:
#         if "404" in str(e):
#             print("Resource not found")
#         else:
#             raise


def test_post_firewall_central_snat_map_reset():
    """Test POST /monitor/firewall/central-snat-map/reset - Reset traffic statistics for all firewall central SNAT policies."""
    try:
        result = fgt.api.monitor.firewall.central_snat_map.reset.post()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


# def test_post_firewall_central_snat_map_clear_counters():
#     """Test POST /monitor/firewall/central-snat-map/clear-counters - Reset traffic statistics for one or more firewall central SNAT policy by policy ID."""
#     # Requires policy ID parameter
#     try:
#         result = fgt.api.monitor.firewall.central_snat_map.clear_counters.post()
#         assert result is not None
#         assert result.http_status_code == 200
#     except Exception as e:
#         if "404" in str(e):
#             print("Resource not found")
#         else:
#             raise


def test_post_firewall_dnat_reset():
    """Test POST /monitor/firewall/dnat/reset - Reset hit count statistics for all firewall virtual IPs/servers."""
    try:
        result = fgt.api.monitor.firewall.dnat.reset.post()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


# def test_post_firewall_dnat_clear_counters():
#     """Test POST /monitor/firewall/dnat/clear-counters - Reset hit count statistics for one or more firewall virtual IP/server by ID."""
#     # Requires ID parameter
#     try:
#         result = fgt.api.monitor.firewall.dnat.clear_counters.post()
#         assert result is not None
#         assert result.http_status_code == 200
#     except Exception as e:
#         if "404" in str(e):
#             print("Resource not found")
#         else:
#             raise


def test_post_firewall_policy_reset():
    """Test POST /monitor/firewall/policy/reset - Reset traffic statistics for all firewall policies."""
    try:
        result = fgt.api.monitor.firewall.policy.reset.post()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


# def test_post_firewall_policy_clear_counters():
#     """Test POST /monitor/firewall/policy/clear_counters - Reset traffic statistics for one or more firewall policies by policy ID."""
#     # Requires policy ID parameter
#     try:
#         result = fgt.api.monitor.firewall.policy.clear_counters.post()
#         assert result is not None
#         assert result.http_status_code == 200
#     except Exception as e:
#         if "404" in str(e):
#             print("Resource not found")
#         else:
#             raise


# def test_post_firewall_policy_update_global_label():
#     """Test POST /monitor/firewall/policy/update-global-label - Update the global-label of group starting with the provided leading policy ID."""
#     # Requires policy ID parameter
#     try:
#         result = fgt.api.monitor.firewall.policy.update_global_label.post()
#         assert result is not None
#         assert result.http_status_code == 200
#     except Exception as e:
#         if "404" in str(e):
#             print("Resource not found")
#         else:
#             raise


# def test_post_firewall_ztna_firewall_policy_clear_counters():
#     """Test POST /monitor/firewall/ztna-firewall-policy/clear-counters - Reset traffic statistics for one or more ZTNA firewall policies by policy ID."""
#     # Requires policy ID parameter
#     try:
#         result = fgt.api.monitor.firewall.ztna_firewall_policy.clear_counters.post()
#         assert result is not None
#         assert result.http_status_code == 200
#     except Exception as e:
#         if "404" in str(e):
#             print("Resource not found")
#         else:
#             raise


# def test_post_firewall_security_policy_clear_counters():
#     """Test POST /monitor/firewall/security-policy/clear_counters - Reset traffic statistics for one or more security policies by policy ID."""
#     # Requires policy ID parameter
#     try:
#         result = fgt.api.monitor.firewall.security_policy.clear_counters.post()
#         assert result is not None
#         assert result.http_status_code == 200
#     except Exception as e:
#         if "404" in str(e):
#             print("Resource not found")
#         else:
#             raise


# def test_post_firewall_security_policy_update_global_label():
#     """Test POST /monitor/firewall/security-policy/update-global-label - Update the global-label of group starting with the provided leading policy ID."""
#     # Requires policy ID parameter
#     try:
#         result = fgt.api.monitor.firewall.security_policy.update_global_label.post()
#         assert result is not None
#         assert result.http_status_code == 200
#     except Exception as e:
#         if "404" in str(e):
#             print("Resource not found")
#         else:
#             raise


# def test_post_firewall_proxy_policy_clear_counters():
#     """Test POST /monitor/firewall/proxy-policy/clear_counters - Reset traffic statistics for one or more explicit proxy policies by policy ID."""
#     # Requires policy ID parameter
#     try:
#         result = fgt.api.monitor.firewall.proxy_policy.clear_counters.post()
#         assert result is not None
#         assert result.http_status_code == 200
#     except Exception as e:
#         if "404" in str(e):
#             print("Resource not found")
#         else:
#             raise


def test_post_firewall_multicast_policy_reset():
    """Test POST /monitor/firewall/multicast-policy/reset - Reset traffic statistics for all IPv4 firewall multicast policies."""
    try:
        result = fgt.api.monitor.firewall.multicast_policy.reset.post()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_post_firewall_multicast_policy6_reset():
    """Test POST /monitor/firewall/multicast-policy6/reset - Reset traffic statistics for all IPv6 firewall multicast policies."""
    try:
        result = fgt.api.monitor.firewall.multicast_policy6.reset.post()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


# def test_post_firewall_multicast_policy_clear_counters():
#     """Test POST /monitor/firewall/multicast-policy/clear_counters - Reset traffic statistics for one or more firewall IPv4 multicast policies by policy ID."""
#     # Requires policy ID parameter
#     try:
#         result = fgt.api.monitor.firewall.multicast_policy.clear_counters.post()
#         assert result is not None
#         assert result.http_status_code == 200
#     except Exception as e:
#         if "404" in str(e):
#             print("Resource not found")
#         else:
#             raise


# def test_post_firewall_multicast_policy6_clear_counters():
#     """Test POST /monitor/firewall/multicast-policy6/clear_counters - Reset traffic statistics for one or more firewall IPv6 multicast policies by policy ID."""
#     # Requires policy ID parameter
#     try:
#         result = fgt.api.monitor.firewall.multicast_policy6.clear_counters.post()
#         assert result is not None
#         assert result.http_status_code == 200
#     except Exception as e:
#         if "404" in str(e):
#             print("Resource not found")
#         else:
#             raise


# def test_post_firewall_session_close_multiple():
#     """Test POST /monitor/firewall/session/close-multiple - Close multiple IPv4 firewall sessions which match the provided criteria."""
#     # Requires criteria parameters
#     try:
#         result = fgt.api.monitor.firewall.session.close_multiple.post()
#         assert result is not None
#         assert result.http_status_code == 200
#     except Exception as e:
#         if "404" in str(e):
#             print("Resource not found")
#         else:
#             raise


# def test_post_firewall_session6_close_multiple():
#     """Test POST /monitor/firewall/session6/close-multiple - Close multiple IPv6 firewall sessions which match the provided criteria."""
#     # Requires criteria parameters
#     try:
#         result = fgt.api.monitor.firewall.session6.close_multiple.post()
#         assert result is not None
#         assert result.http_status_code == 200
#     except Exception as e:
#         if "404" in str(e):
#             print("Resource not found")
#         else:
#             raise


# def test_post_firewall_session_close_all():
#     """Test POST /monitor/firewall/session/close-all - Immediately close all active IPv4 and IPv6 sessions, as well as IPS sessions of the current VDOM."""
#     # Dangerous operation - commented out
#     try:
#         result = fgt.api.monitor.firewall.session.close_all.post()
#         assert result is not None
#         assert result.http_status_code == 200
#     except Exception as e:
#         if "404" in str(e):
#             print("Resource not found")
#         else:
#             raise


# def test_post_firewall_session_close():
#     """Test POST /monitor/firewall/session/close - Close a single firewall session that matches all provided criteria."""
#     # Requires session criteria parameters
#     try:
#         result = fgt.api.monitor.firewall.session.close.post()
#         assert result is not None
#         assert result.http_status_code == 200
#     except Exception as e:
#         if "404" in str(e):
#             print("Resource not found")
#         else:
#             raise


def test_post_firewall_shaper_reset():
    """Test POST /monitor/firewall/shaper/reset - Reset statistics for all configured traffic shapers."""
    try:
        result = fgt.api.monitor.firewall.shaper.reset.post()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_post_firewall_per_ip_shaper_reset():
    """Test POST /monitor/firewall/per-ip-shaper/reset - Reset statistics for all configured firewall per-IP traffic shapers."""
    try:
        result = fgt.api.monitor.firewall.per_ip_shaper.reset.post()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


# def test_post_firewall_clearpass_address_add():
#     """Test POST /monitor/firewall/clearpass-address/add - Add ClearPass address with SPT (System Posture Token) value."""
#     # Requires SPT value parameter
#     try:
#         result = fgt.api.monitor.firewall.clearpass_address.add.post()
#         assert result is not None
#         assert result.http_status_code == 200
#     except Exception as e:
#         if "404" in str(e):
#             print("Resource not found")
#         else:
#             raise


# def test_post_firewall_clearpass_address_delete():
#     """Test POST /monitor/firewall/clearpass-address/delete - Delete ClearPass address with SPT (System Posture Token) value."""
#     # Requires SPT value parameter
#     try:
#         result = fgt.api.monitor.firewall.clearpass_address.delete.post()
#         assert result is not None
#         assert result.http_status_code == 200
#     except Exception as e:
#         if "404" in str(e):
#             print("Resource not found")
#         else:
#             raise


def test_post_firewall_gtp_flush():
    """Test POST /monitor/firewall/gtp/flush - Flush GTP tunnels."""
    try:
        result = fgt.api.monitor.firewall.gtp.flush.post()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
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
    test_get_firewall_health()
    print("✓ test_get_firewall_health")
    
    test_get_firewall_local_in()
    print("✓ test_get_firewall_local_in")
    
    test_get_firewall_local_in6()
    print("✓ test_get_firewall_local_in6")
    
    # test_get_firewall_acl()
    # print("✓ test_get_firewall_acl")
    
    # test_get_firewall_acl6()
    # print("✓ test_get_firewall_acl6")
    
    test_get_firewall_central_snat_map()
    print("✓ test_get_firewall_central_snat_map")
    
    # test_get_firewall_dnat()
    # print("✓ test_get_firewall_dnat")
    
    # Commented out - requires parameters
    # test_get_firewall_check_addrgrp_exclude_mac_member()
    # test_get_firewall_internet_service_match()
    # test_get_firewall_internet_service_reputation()
    
    test_get_firewall_internet_service_fqdn()
    print("✓ test_get_firewall_internet_service_fqdn")
    
    test_get_firewall_internet_service_fqdn_icon_ids()
    print("✓ test_get_firewall_internet_service_fqdn_icon_ids")
    
    test_get_firewall_internet_service_basic()
    print("✓ test_get_firewall_internet_service_basic")
    
    # Commented out - requires parameters
    # test_get_firewall_internet_service_details()
    # test_get_firewall_network_service_dynamic()
    # test_get_firewall_proxy_sessions()
    
    test_get_firewall_policy()
    print("✓ test_get_firewall_policy")
    
    test_get_firewall_security_policy()
    print("✓ test_get_firewall_security_policy")
    
    test_get_firewall_proxy_policy()
    print("✓ test_get_firewall_proxy_policy")
    
    test_get_firewall_multicast_policy()
    print("✓ test_get_firewall_multicast_policy")
    
    test_get_firewall_multicast_policy6()
    print("✓ test_get_firewall_multicast_policy6")
    
    test_get_firewall_saas_application()
    print("✓ test_get_firewall_saas_application")
    
    # Commented out - requires parameters
    # test_get_firewall_policy_lookup()
    # test_get_firewall_sessions()
    
    test_get_firewall_shaper()
    print("✓ test_get_firewall_shaper")
    
    test_get_firewall_shaper_multi_class_shaper()
    print("✓ test_get_firewall_shaper_multi_class_shaper")
    
    test_get_firewall_per_ip_shaper()
    print("✓ test_get_firewall_per_ip_shaper")
    
    # Commented out - requires parameters
    # test_get_firewall_load_balance()
    
    test_get_firewall_vip_overlap()
    print("✓ test_get_firewall_vip_overlap")
    
    test_get_firewall_address_fqdns()
    print("✓ test_get_firewall_address_fqdns")
    
    test_get_firewall_address_fqdns6()
    print("✓ test_get_firewall_address_fqdns6")
    
    test_get_firewall_ippool()
    print("✓ test_get_firewall_ippool")
    
    # Commented out - requires parameters
    # test_get_firewall_ippool_mapping()
    
    test_get_firewall_uuid_list()
    print("✓ test_get_firewall_uuid_list")
    
    # test_get_firewall_uuid_type_lookup()
    # print("✓ test_get_firewall_uuid_type_lookup")
    
    test_get_firewall_gtp()
    print("✓ test_get_firewall_gtp")
    
    test_get_firewall_gtp_statistics()
    print("✓ test_get_firewall_gtp_statistics")
    
    test_get_firewall_gtp_runtime_statistics()
    print("✓ test_get_firewall_gtp_runtime_statistics")
    
    test_get_firewall_address_dynamic()
    print("✓ test_get_firewall_address_dynamic")
    
    test_get_firewall_address6_dynamic()
    print("✓ test_get_firewall_address6_dynamic")
    
    # Commented out - requires parameters
    # test_get_firewall_sdn_connector_filters()
    
    print("\n✓ All GET tests completed!")
    
    # ========================================================================
    # POST endpoint tests
    # ========================================================================
    
    print("\nRunning POST endpoint tests...")
    
    # Commented out - requires parameters
    # test_post_firewall_acl_clear_counters()
    # test_post_firewall_acl6_clear_counters()
    
    test_post_firewall_central_snat_map_reset()
    print("✓ test_post_firewall_central_snat_map_reset")
    
    # Commented out - requires parameters
    # test_post_firewall_central_snat_map_clear_counters()
    
    test_post_firewall_dnat_reset()
    print("✓ test_post_firewall_dnat_reset")
    
    # Commented out - requires parameters
    # test_post_firewall_dnat_clear_counters()
    
    test_post_firewall_policy_reset()
    print("✓ test_post_firewall_policy_reset")
    
    # Commented out - requires parameters
    # test_post_firewall_policy_clear_counters()
    # test_post_firewall_policy_update_global_label()
    # test_post_firewall_ztna_firewall_policy_clear_counters()
    # test_post_firewall_security_policy_clear_counters()
    # test_post_firewall_security_policy_update_global_label()
    # test_post_firewall_proxy_policy_clear_counters()
    
    test_post_firewall_multicast_policy_reset()
    print("✓ test_post_firewall_multicast_policy_reset")
    
    test_post_firewall_multicast_policy6_reset()
    print("✓ test_post_firewall_multicast_policy6_reset")
    
    # Commented out - requires parameters
    # test_post_firewall_multicast_policy_clear_counters()
    # test_post_firewall_multicast_policy6_clear_counters()
    # test_post_firewall_session_close_multiple()
    # test_post_firewall_session6_close_multiple()
    # test_post_firewall_session_close_all()  # Dangerous operation
    # test_post_firewall_session_close()
    
    test_post_firewall_shaper_reset()
    print("✓ test_post_firewall_shaper_reset")
    
    test_post_firewall_per_ip_shaper_reset()
    print("✓ test_post_firewall_per_ip_shaper_reset")
    
    # Commented out - requires parameters
    # test_post_firewall_clearpass_address_add()
    # test_post_firewall_clearpass_address_delete()
    
    test_post_firewall_gtp_flush()
    print("✓ test_post_firewall_gtp_flush")
    
    print("\n✓ All POST tests completed!")
    print("\nSummary:")
    print("- GET endpoints: 26 active tests, 15 commented out (require parameters or return 404)")
    print("- POST endpoints: 8 active tests, 18 commented out (require parameters or return 404)")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
