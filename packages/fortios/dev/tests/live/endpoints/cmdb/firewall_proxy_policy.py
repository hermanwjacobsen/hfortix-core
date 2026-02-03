import argparse
import sys
from pathlib import Path
import pytest

pytestmark = pytest.mark.xdist_group(Path(__file__).stem)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt

TEST_POLICY_ID = 9999974
TEST_NAME = "test_proxy_policy_9999974"
TEST_PROXY_TYPE = "transparent-web"
TEST_INTERFACE = "port3"
TEST_SCHEDULE = "always"


def cleanup():
    try:
        policies = fgt.api.cmdb.firewall.proxy_policy.get()
        for policy in policies:
            if getattr(policy, "policyid", None) == TEST_POLICY_ID:
                fgt.api.cmdb.firewall.proxy_policy.delete(policyid=TEST_POLICY_ID)
                break
    except Exception:
        pass

def test_get_proxy_policy():
    """Test GET all proxy policies."""
    result = fgt.api.cmdb.firewall.proxy_policy.get()
    assert result is not None
    assert result.http_status_code == 200

def test_post_proxy_policy():
    result = fgt.api.cmdb.firewall.proxy_policy.post(
        policyid=TEST_POLICY_ID,
        name=TEST_NAME,
        proxy=TEST_PROXY_TYPE,
        srcintf=[{"name": TEST_INTERFACE}],
        dstintf=[{"name": TEST_INTERFACE}],
        srcaddr=[{"name": "all"}],
        dstaddr=[{"name": "all"}],
        service=[{"name": "webproxy"}],
        action="accept",
        schedule=TEST_SCHEDULE,
        logtraffic="all"
    )
    assert result is not None
    assert result.http_status == "success"

def test_put_proxy_policy():
    updated_name = "test_proxy_policy_updated"
    updated_comments = "Updated transparent proxy policy"
    result = fgt.api.cmdb.firewall.proxy_policy.put(
        policyid=TEST_POLICY_ID,
        name=updated_name,
        comments=updated_comments
    )
    assert result is not None
    assert result.http_status == "success"
    verify = fgt.api.cmdb.firewall.proxy_policy.get(policyid=TEST_POLICY_ID)
    assert verify is not None
    assert verify.http_status_code == 200
    assert verify.name == updated_name
    assert verify.comments == updated_comments

def test_get_specific_proxy_policy():
    result = fgt.api.cmdb.firewall.proxy_policy.get(policyid=TEST_POLICY_ID)
    assert result is not None
    assert result.policyid == TEST_POLICY_ID

def test_delete_proxy_policy():
    result = fgt.api.cmdb.firewall.proxy_policy.delete(policyid=TEST_POLICY_ID)
    assert result is not None
    assert result.http_status == "success"
    # Verify deletion
    policies = fgt.api.cmdb.firewall.proxy_policy.get()
    ids = [getattr(p, "policyid", None) for p in policies]
    assert TEST_POLICY_ID not in ids, "Proxy policy should have been deleted"

def test_normalizer_multiple_formats():
    """Test that normalizer handles different input formats correctly."""
    test_id = 9999973
    try:
        # Cleanup if exists
        policies = fgt.api.cmdb.firewall.proxy_policy.get()
        for policy in policies:
            if getattr(policy, "policyid", None) == test_id:
                fgt.api.cmdb.firewall.proxy_policy.delete(policyid=test_id)
                break
        
        # Test mixed format inputs
        result = fgt.api.cmdb.firewall.proxy_policy.post(
            policyid=test_id,
            name="test_proxy_multi_format",
            proxy=TEST_PROXY_TYPE,
            srcintf=["port3", "port4"],              # List of strings
            dstintf="port3",                          # Single string
            srcaddr=[{"name": "all"}],                # Already formatted
            dstaddr="all",                            # Single string
            service=["webproxy"],                     # List of strings
            action="accept",
            schedule=TEST_SCHEDULE,
            logtraffic="all"
        )
        assert result is not None
        assert result.http_status == "success"
        
        # Verify the policy was created correctly
        verify = fgt.api.cmdb.firewall.proxy_policy.get(policyid=test_id)
        assert verify is not None
        assert verify.policyid == test_id
        assert verify.name == "test_proxy_multi_format"
        
        # Cleanup
        fgt.api.cmdb.firewall.proxy_policy.delete(policyid=test_id)
    except Exception as e:
        # Cleanup on failure
        try:
            fgt.api.cmdb.firewall.proxy_policy.delete(policyid=test_id)
        except:
            pass
        raise e

def test_normalizer_string_to_list():
    """Test that single string values are normalized to list format."""
    test_id = 9999972
    try:
        # Cleanup if exists
        policies = fgt.api.cmdb.firewall.proxy_policy.get()
        for policy in policies:
            if getattr(policy, "policyid", None) == test_id:
                fgt.api.cmdb.firewall.proxy_policy.delete(policyid=test_id)
                break
        
        # Test all string inputs
        result = fgt.api.cmdb.firewall.proxy_policy.post(
            policyid=test_id,
            name="test_proxy_all_strings",
            proxy=TEST_PROXY_TYPE,
            srcintf="port3",                          # Single string
            dstintf="port4",                          # Single string
            srcaddr="all",                            # Single string
            dstaddr="all",                            # Single string
            service="webproxy",                       # Single string
            action="accept",
            schedule=TEST_SCHEDULE,
            logtraffic="all"
        )
        assert result is not None
        assert result.http_status == "success"
        
        # Cleanup
        fgt.api.cmdb.firewall.proxy_policy.delete(policyid=test_id)
    except Exception as e:
        # Cleanup on failure
        try:
            fgt.api.cmdb.firewall.proxy_policy.delete(policyid=test_id)
        except:
            pass
        raise e

def test_normalizer_list_format():
    """Test that list of strings are normalized correctly."""
    test_id = 9999971
    try:
        # Cleanup if exists
        policies = fgt.api.cmdb.firewall.proxy_policy.get()
        for policy in policies:
            if getattr(policy, "policyid", None) == test_id:
                fgt.api.cmdb.firewall.proxy_policy.delete(policyid=test_id)
                break
        
        # Test list inputs
        result = fgt.api.cmdb.firewall.proxy_policy.post(
            policyid=test_id,
            name="test_proxy_list_format",
            proxy=TEST_PROXY_TYPE,
            srcintf=["port3"],                        # List with single item
            dstintf=["port4"],                        # List with single item
            srcaddr=["all"],                          # List of strings
            dstaddr=["all"],                          # List of strings
            service=["webproxy"],                     # List of strings
            action="accept",
            schedule=TEST_SCHEDULE,
            logtraffic="all"
        )
        assert result is not None
        assert result.http_status == "success"
        
        # Cleanup
        fgt.api.cmdb.firewall.proxy_policy.delete(policyid=test_id)
    except Exception as e:
        # Cleanup on failure
        try:
            fgt.api.cmdb.firewall.proxy_policy.delete(policyid=test_id)
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
    test_get_proxy_policy()
    print("✓ test_get_proxy_policy passed")
    test_post_proxy_policy()
    print("✓ test_post_proxy_policy passed")
    test_put_proxy_policy()
    print("✓ test_put_proxy_policy passed")
    test_get_specific_proxy_policy()
    print("✓ test_get_specific_proxy_policy passed")
    test_delete_proxy_policy()
    print("✓ test_delete_proxy_policy passed")
    test_normalizer_multiple_formats()
    print("✓ test_normalizer_multiple_formats passed")
    test_normalizer_string_to_list()
    print("✓ test_normalizer_string_to_list passed")
    test_normalizer_list_format()
    print("✓ test_normalizer_list_format passed")
    cleanup()
    print("✓ post-Cleanup passed")
    print("\n✓ All tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
