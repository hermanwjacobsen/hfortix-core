import argparse
import sys
from pathlib import Path
import pytest

pytestmark = pytest.mark.xdist_group(Path(__file__).stem)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt

TEST_GROUP_NAME = "test_inet_svc_custom_group1"
TEST_GROUP_COMMENT = "pytest custom internet service group"
TEST_MEMBER_NAME = "test_inet_svc_custom_member1"


def cleanup():
    # Cleanup test objects
    try:
        fgt.api.cmdb.firewall.internet_service_custom_group.delete(name=TEST_GROUP_NAME)
    except Exception:
        pass
    try:
        fgt.api.cmdb.firewall.internet_service_custom.delete(name=TEST_MEMBER_NAME)
    except Exception:
        pass

def test_get_internet_service_custom_group():
    result = fgt.api.cmdb.firewall.internet_service_custom_group.get()
    assert result is not None
    assert result.http_status_code == 200

def test_post_internet_service_custom_group():
    # Create a custom internet service to use as member
    member_result = fgt.api.cmdb.firewall.internet_service_custom.post(
        name=TEST_MEMBER_NAME,
        comment="pytest custom member",
        entry=[]
    )
    assert member_result is not None
    assert member_result.http_status == "success"
    # Now create the group
    result = fgt.api.cmdb.firewall.internet_service_custom_group.post(
        name=TEST_GROUP_NAME,
        comment=TEST_GROUP_COMMENT,
        member=[{"name": TEST_MEMBER_NAME}]
    )
    assert result is not None
    assert result.http_status == "success"

def test_put_internet_service_custom_group():
    result = fgt.api.cmdb.firewall.internet_service_custom_group.put(
        name=TEST_GROUP_NAME,
        comment="pytest custom internet service group updated"
    )
    assert result is not None
    assert result.http_status == "success"
    verify = fgt.api.cmdb.firewall.internet_service_custom_group.get(name=TEST_GROUP_NAME)
    assert verify is not None
    assert verify.http_status_code == 200
    assert verify.comment == "pytest custom internet service group updated"

def test_get_specific_internet_service_custom_group():
    result = fgt.api.cmdb.firewall.internet_service_custom_group.get(name=TEST_GROUP_NAME)
    assert result is not None
    assert result.name == TEST_GROUP_NAME

def test_delete_internet_service_custom_group():
    result = fgt.api.cmdb.firewall.internet_service_custom_group.delete(name=TEST_GROUP_NAME)
    assert result is not None
    assert result.http_status == "success"
    # Verify deletion
    groups = fgt.api.cmdb.firewall.internet_service_custom_group.get()
    names = [getattr(g, "name", None) for g in groups]
    assert TEST_GROUP_NAME not in names, "Custom internet service group should have been deleted"
    # Cleanup member
    member_del = fgt.api.cmdb.firewall.internet_service_custom.delete(name=TEST_MEMBER_NAME)
    assert member_del is not None
    assert member_del.http_status == "success"

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
    test_get_internet_service_custom_group()
    print("✓ test_get_internet_service_custom_group passed")
    test_post_internet_service_custom_group()
    print("✓ test_post_internet_service_custom_group passed")
    test_put_internet_service_custom_group()
    print("✓ test_put_internet_service_custom_group passed")
    test_get_specific_internet_service_custom_group()
    print("✓ test_get_specific_internet_service_custom_group passed")
    test_delete_internet_service_custom_group()
    print("✓ test_delete_internet_service_custom_group passed")
    cleanup()
    print("✓ post-Cleanup passed")
    print("\n✓ All tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
