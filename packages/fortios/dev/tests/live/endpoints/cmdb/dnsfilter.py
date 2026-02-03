import argparse
import sys
from pathlib import Path

import pytest

# Run DLP tests on a single worker to preserve state
pytestmark = pytest.mark.xdist_group("dnsfilter")

# Add pytest directory to path (go up from endpoints/cmdb/ to pytest/)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt


def cleanup():
    try:
        domain_filters = fgt.api.cmdb.dnsfilter.domain_filter.get()
        for df in domain_filters:
            name = df.name
            if name and str(name).startswith("test_"):
                try:
                    fgt.api.cmdb.dnsfilter.domain_filter.delete(id=df.id)
                except Exception:
                    pass
    except Exception:
        pass

    try:
        dnsfilter_profiles = fgt.api.cmdb.dnsfilter.profile.get()
        for profile in dnsfilter_profiles:
            name = profile.name
            if name and str(name).startswith("test_"):
                try:
                    fgt.api.cmdb.dnsfilter.profile.delete(name=name)
                except Exception:
                    pass
    except Exception:
        pass

def test_get_domain_filter_list():  
    domain_filter = fgt.api.cmdb.dnsfilter.domain_filter.get()
    assert domain_filter is not None
    assert domain_filter.http_status_code == 200

def test_post_domain_filter():
    domain_filter = fgt.api.cmdb.dnsfilter.domain_filter.post(
        name="test_dnsfilter1",
        comment="Test DNS Filter",
        entries=[
            {
                "action": "block",
                "domain": "example.com"
            }
        ]
    )
    assert domain_filter is not None
    assert domain_filter.http_status == "success"

def test_get_specific_domain_filter():
    domain_filter = fgt.api.cmdb.dnsfilter.domain_filter.get()
    for df in domain_filter:
        if df.name == "test_dnsfilter1":
            test_dnsfilter1_id = df.id

    assert test_dnsfilter1_id is not None
    specific_filter = fgt.api.cmdb.dnsfilter.domain_filter.get(id=test_dnsfilter1_id)
    assert specific_filter is not None
    assert specific_filter.name == "test_dnsfilter1"

def test_put_domain_filter():
    domain_filter = fgt.api.cmdb.dnsfilter.domain_filter.get()
    for df in domain_filter:
        if df.name == "test_dnsfilter1":
            test_dnsfilter1_id = df.id

    assert test_dnsfilter1_id is not None
    updated_filter = fgt.api.cmdb.dnsfilter.domain_filter.put(
        id=test_dnsfilter1_id,
        comment="Updated Test DNS Filter"
    )
    assert updated_filter is not None
    assert updated_filter.http_status == "success"
    
    domain_filter_updates = fgt.api.cmdb.dnsfilter.domain_filter.get(id=test_dnsfilter1_id)
    assert domain_filter_updates is not None
    assert domain_filter_updates.comment == "Updated Test DNS Filter"   

def test_delete_domain_filter():
    domain_filter = fgt.api.cmdb.dnsfilter.domain_filter.get()
    for df in domain_filter:
        if df.name == "test_dnsfilter1":
            test_dnsfilter1_id = df.id

    assert test_dnsfilter1_id is not None
    deleted_filter = fgt.api.cmdb.dnsfilter.domain_filter.delete(id=test_dnsfilter1_id)
    assert deleted_filter is not None
    assert deleted_filter.http_status == "success"
    
    # Verify deletion
    domain_filters_after_deletion = fgt.api.cmdb.dnsfilter.domain_filter.get()
    filter_names = [df.name for df in domain_filters_after_deletion]
    assert "test_dnsfilter1" not in filter_names


def test_get_dnsfilter_profile():
    dnsfilter_profiles = fgt.api.cmdb.dnsfilter.profile.get()
    assert dnsfilter_profiles is not None
    assert isinstance(dnsfilter_profiles, list)
    assert dnsfilter_profiles.http_status_code == 200

def test_post_dnsfilter_profile():
    dnsfilter_profile = fgt.api.cmdb.dnsfilter.profile.post(
        name="test_dnsfilter_profile1",
        comment="Test DNS Filter Profile"
    )
    assert dnsfilter_profile is not None
    assert dnsfilter_profile.http_status == "success"

def test_get_specific_dnsfilter_profile():
    dnsfilter_profile = fgt.api.cmdb.dnsfilter.profile.get(name="test_dnsfilter_profile1")
    assert dnsfilter_profile is not None
    assert dnsfilter_profile.name == "test_dnsfilter_profile1"  

def test_put_dnsfilter_profile():
    updated_profile = fgt.api.cmdb.dnsfilter.profile.put(
        name="test_dnsfilter_profile1",
        comment="Updated Test DNS Filter Profile"
    )
    assert updated_profile is not None
    assert updated_profile.http_status == "success"
    
    dnsfilter_profile_updates = fgt.api.cmdb.dnsfilter.profile.get(name="test_dnsfilter_profile1")
    assert dnsfilter_profile_updates is not None
    assert dnsfilter_profile_updates.comment == "Updated Test DNS Filter Profile"

def test_delete_dnsfilter_profile():
    deleted_profile = fgt.api.cmdb.dnsfilter.profile.delete(name="test_dnsfilter_profile1")
    assert deleted_profile is not None
    assert deleted_profile.http_status == "success"

    
    # Verify deletion
    dnsfilter_profiles_after_deletion = fgt.api.cmdb.dnsfilter.profile.get()
    profile_names = [dp.name for dp in dnsfilter_profiles_after_deletion]
    assert "test_dnsfilter_profile1" not in profile_names

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
    print("Pre-Cleanup done")
    test_get_domain_filter_list()
    print("✓ test_get_domain_filter_list passed")
    test_post_domain_filter()
    print("✓ test_post_domain_filter passed")
    test_get_specific_domain_filter()
    print("✓ get_specific_domain_filter passed")
    test_put_domain_filter()
    print("✓ test_put_domain_filter passed")
    test_delete_domain_filter()
    print("✓ test_delete_domain_filter passed")
    test_get_dnsfilter_profile()
    print("✓ DNS Filter Profile list test passed")
    test_post_dnsfilter_profile()
    print("✓ DNS Filter Profile creation test passed")
    test_get_specific_dnsfilter_profile()
    print("✓ DNS Filter Profile tests passed")
    test_put_dnsfilter_profile()
    print("✓ DNS Filter Profile update test passed")
    test_delete_dnsfilter_profile()
    print("✓ DNS Filter Profile deletion test passed") 
    cleanup()
    print("Post-Cleanup done")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
