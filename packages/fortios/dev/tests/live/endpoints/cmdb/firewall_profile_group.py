import argparse
import sys
from pathlib import Path
import pytest

pytestmark = pytest.mark.xdist_group(Path(__file__).stem)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt

TEST_NAME = "test_profile_group_9999982"
TEST_AV_PROFILE = "g-default"
TEST_WEBFILTER_PROFILE = "g-default"
TEST_APPLICATION_LIST = "g-default"
TEST_IPS_SENSOR = "g-default"
TEST_FILE_FILTER_PROFILE = "g-default"
TEST_DLP_PROFILE = "g-default"
TEST_VIRTUAL_PATCH_PROFILE = "g-default"
TEST_SSL_SSH_PROFILE = "certificate-inspection"


def cleanup():
    try:
        groups = fgt.api.cmdb.firewall.profile_group.get()
        for group in groups:
            if getattr(group, "name", None) == TEST_NAME:
                fgt.api.cmdb.firewall.profile_group.delete(name=TEST_NAME)
                break
    except Exception:
        pass

def test_get_profile_group():
    result = fgt.api.cmdb.firewall.profile_group.get()
    assert result is not None
    assert result.http_status_code == 200

def test_post_profile_group():
    result = fgt.api.cmdb.firewall.profile_group.post(
        name=TEST_NAME,
        av_profile=TEST_AV_PROFILE,
        webfilter_profile=TEST_WEBFILTER_PROFILE,
        application_list=TEST_APPLICATION_LIST,
        ips_sensor=TEST_IPS_SENSOR,
        ssl_ssh_profile=TEST_SSL_SSH_PROFILE
    )
    assert result is not None
    assert result.http_status == "success"

def test_put_profile_group():
    result = fgt.api.cmdb.firewall.profile_group.put(
        name=TEST_NAME,
        av_profile=TEST_AV_PROFILE,
        webfilter_profile=TEST_WEBFILTER_PROFILE,
        application_list=TEST_APPLICATION_LIST,
        ips_sensor=TEST_IPS_SENSOR,
        file_filter_profile=TEST_FILE_FILTER_PROFILE,
        dlp_profile=TEST_DLP_PROFILE,
        virtual_patch_profile=TEST_VIRTUAL_PATCH_PROFILE,
        ssl_ssh_profile=TEST_SSL_SSH_PROFILE
    )
    assert result is not None
    assert result.http_status == "success"
    verify = fgt.api.cmdb.firewall.profile_group.get(name=TEST_NAME)
    assert verify is not None
    assert verify.http_status_code == 200
    assert verify.name == TEST_NAME
    assert verify.file_filter_profile == TEST_FILE_FILTER_PROFILE
    assert verify.dlp_profile == TEST_DLP_PROFILE
    assert verify.virtual_patch_profile == TEST_VIRTUAL_PATCH_PROFILE

def test_get_specific_profile_group():
    result = fgt.api.cmdb.firewall.profile_group.get(name=TEST_NAME)
    assert result is not None
    assert result.name == TEST_NAME

def test_delete_profile_group():
    result = fgt.api.cmdb.firewall.profile_group.delete(name=TEST_NAME)
    assert result is not None
    assert result.http_status == "success"
    # Verify deletion
    groups = fgt.api.cmdb.firewall.profile_group.get()
    names = [getattr(g, "name", None) for g in groups]
    assert TEST_NAME not in names, "Profile group should have been deleted"

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
    test_get_profile_group()
    print("✓ test_get_profile_group passed")
    test_post_profile_group()
    print("✓ test_post_profile_group passed")
    test_put_profile_group()
    print("✓ test_put_profile_group passed")
    test_get_specific_profile_group()
    print("✓ test_get_specific_profile_group passed")
    test_delete_profile_group()
    print("✓ test_delete_profile_group passed")
    cleanup()
    print("✓ post-Cleanup passed")
    print("\n✓ All tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
