import argparse
import sys
from pathlib import Path
import pytest

pytestmark = pytest.mark.xdist_group(Path(__file__).stem)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt

TEST_POLICY_ID = 9999989
TEST_NAME = "test_ipv6_policy_9999989"
TEST_SRC_INTERFACE = "port3"
TEST_DST_INTERFACE = "port4"
TEST_SCHEDULE = "always"


def cleanup():
    try:
        policies = fgt.api.cmdb.firewall.policy.get()
        for policy in policies:
            if getattr(policy, "policyid", None) == TEST_POLICY_ID:
                fgt.api.cmdb.firewall.policy.delete(policyid=TEST_POLICY_ID)
                break
    except Exception:
        pass

def test_get_firewall_policy6():
    result = fgt.api.cmdb.firewall.policy.get()
    assert result is not None
    assert result.http_status_code == 200

def test_post_firewall_policy6():
    result = fgt.api.cmdb.firewall.policy.post(
        policyid=TEST_POLICY_ID,
        name=TEST_NAME,
        srcintf=[{"name": TEST_SRC_INTERFACE}],
        dstintf=[{"name": TEST_DST_INTERFACE}],
        srcaddr6=[{"name": "all"}],
        dstaddr6=[{"name": "all"}],
        action="accept",
        schedule=TEST_SCHEDULE,
        service=[{"name": "ALL"}],
        nat="disable",
        status="enable",
        logtraffic="all"
    )
    assert result is not None
    assert result.http_status == "success"

def test_put_firewall_policy6():
    updated_name = "test_ipv6_policy_updated"
    updated_comments = "Updated IPv6 firewall policy"
    result = fgt.api.cmdb.firewall.policy.put(
        policyid=TEST_POLICY_ID,
        name=updated_name,
        comments=updated_comments
    )
    assert result is not None
    assert result.http_status == "success"
    verify = fgt.api.cmdb.firewall.policy.get(policyid=TEST_POLICY_ID)
    assert verify is not None
    assert verify.http_status_code == 200
    assert verify.name == updated_name
    assert verify.comments == updated_comments

def test_get_specific_firewall_policy6():
    result = fgt.api.cmdb.firewall.policy.get(policyid=TEST_POLICY_ID)
    assert result is not None
    assert result.policyid == TEST_POLICY_ID

def test_delete_firewall_policy6():
    result = fgt.api.cmdb.firewall.policy.delete(policyid=TEST_POLICY_ID)
    assert result is not None
    assert result.http_status == "success"
    # Verify deletion
    policies = fgt.api.cmdb.firewall.policy.get()
    ids = [getattr(p, "policyid", None) for p in policies]
    assert TEST_POLICY_ID not in ids, "IPv6 firewall policy should have been deleted"

def test_normalizer_multiple_formats_ipv6():
    """Test that normalizer handles different input formats correctly for IPv6."""
    test_id = 9999985
    try:
        # Cleanup if exists
        policies = fgt.api.cmdb.firewall.policy.get()
        for policy in policies:
            if getattr(policy, "policyid", None) == test_id:
                fgt.api.cmdb.firewall.policy.delete(policyid=test_id)
                break
        
        # Test mixed format inputs
        result = fgt.api.cmdb.firewall.policy.post(
            policyid=test_id,
            name="test_policy6_multi_format",
            srcintf=["port3", "port4"],              # List of strings
            dstintf="port3",                          # Single string
            srcaddr6=[{"name": "all"}],               # Already formatted
            dstaddr6="all",                           # Single string
            service=["HTTP", "HTTPS"],                # List of strings
            action="accept",
            schedule="always",
            nat="disable"
        )
        assert result is not None
        assert result.http_status == "success"
        
        # Verify the policy was created correctly
        verify = fgt.api.cmdb.firewall.policy.get(policyid=test_id)
        assert verify is not None
        assert verify.policyid == test_id
        assert verify.name == "test_policy6_multi_format"
        
        # Cleanup
        fgt.api.cmdb.firewall.policy.delete(policyid=test_id)
    except Exception as e:
        # Cleanup on failure
        try:
            fgt.api.cmdb.firewall.policy.delete(policyid=test_id)
        except:
            pass
        raise e

def test_normalizer_string_to_list_ipv6():
    """Test that single string values are normalized to list format for IPv6."""
    test_id = 9999984
    try:
        # Cleanup if exists
        policies = fgt.api.cmdb.firewall.policy.get()
        for policy in policies:
            if getattr(policy, "policyid", None) == test_id:
                fgt.api.cmdb.firewall.policy.delete(policyid=test_id)
                break
        
        # Test all string inputs
        result = fgt.api.cmdb.firewall.policy.post(
            policyid=test_id,
            name="test_policy6_all_strings",
            srcintf="port3",                          # Single string
            dstintf="port4",                          # Single string
            srcaddr6="all",                           # Single string
            dstaddr6="all",                           # Single string
            service="ALL",                            # Single string
            action="accept",
            schedule="always",
            nat="disable"
        )
        assert result is not None
        assert result.http_status == "success"
        
        # Cleanup
        fgt.api.cmdb.firewall.policy.delete(policyid=test_id)
    except Exception as e:
        # Cleanup on failure
        try:
            fgt.api.cmdb.firewall.policy.delete(policyid=test_id)
        except:
            pass
        raise e

def test_normalizer_list_format_ipv6():
    """Test that list of strings are normalized correctly for IPv6."""
    test_id = 9999983
    try:
        # Cleanup if exists
        policies = fgt.api.cmdb.firewall.policy.get()
        for policy in policies:
            if getattr(policy, "policyid", None) == test_id:
                fgt.api.cmdb.firewall.policy.delete(policyid=test_id)
                break
        
        # Test list inputs
        result = fgt.api.cmdb.firewall.policy.post(
            policyid=test_id,
            name="test_policy6_list_format",
            srcintf=["port3"],                        # List with single item
            dstintf=["port4"],                        # List with single item
            srcaddr6=["all"],                         # List of strings
            dstaddr6=["all"],                         # List of strings
            service=["HTTP", "HTTPS", "DNS"],         # List of multiple strings
            action="accept",
            schedule="always",
            nat="disable"
        )
        assert result is not None
        assert result.http_status == "success"
        
        # Cleanup
        fgt.api.cmdb.firewall.policy.delete(policyid=test_id)
    except Exception as e:
        # Cleanup on failure
        try:
            fgt.api.cmdb.firewall.policy.delete(policyid=test_id)
        except:
            pass
        raise e

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
    test_get_firewall_policy6()
    print("✓ test_get_firewall_policy6 passed")
    test_post_firewall_policy6()
    print("✓ test_post_firewall_policy6 passed")
    test_put_firewall_policy6()
    print("✓ test_put_firewall_policy6 passed")
    test_get_specific_firewall_policy6()
    print("✓ test_get_specific_firewall_policy6 passed")
    test_delete_firewall_policy6()
    print("✓ test_delete_firewall_policy6 passed")
    test_normalizer_multiple_formats_ipv6()
    print("✓ test_normalizer_multiple_formats_ipv6 passed")
    test_normalizer_string_to_list_ipv6()
    print("✓ test_normalizer_string_to_list_ipv6 passed")
    test_normalizer_list_format_ipv6()
    print("✓ test_normalizer_list_format_ipv6 passed")
    cleanup()
    print("✓ post-Cleanup passed")
    print("\n✓ All tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
