import argparse
import sys
from pathlib import Path
import pytest

pytestmark = pytest.mark.xdist_group(Path(__file__).stem)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt

TEST_NAME = "test_protocol_options_9999980"
TEST_COMMENT = "Test protocol options profile"


def cleanup():
    try:
        profiles = fgt.api.cmdb.firewall.profile_protocol_options.get()
        for profile in profiles:
            if getattr(profile, "name", None) == TEST_NAME:
                fgt.api.cmdb.firewall.profile_protocol_options.delete(name=TEST_NAME)
                break
    except Exception:
        pass

def test_get_profile_protocol_options():
    result = fgt.api.cmdb.firewall.profile_protocol_options.get()
    assert result is not None
    assert result.http_status_code == 200

def test_post_profile_protocol_options():
    result = fgt.api.cmdb.firewall.profile_protocol_options.post(
        name=TEST_NAME,
        comment=TEST_COMMENT,
        oversize_log="enable",
        switching_protocols_log="enable",
        http={"ports": [80, 8080], "status": "enable", "inspect_all": "enable"},
        ftp={"ports": [21], "status": "enable"},
        smtp={"ports": [25], "status": "enable"},
        pop3={"ports": [110], "status": "enable"},
        imap={"ports": [143], "status": "enable"}
    )
    assert result is not None
    assert result.http_status == "success"

def test_put_profile_protocol_options():
    updated_comment = "Updated protocol options profile"
    result = fgt.api.cmdb.firewall.profile_protocol_options.put(
        name=TEST_NAME,
        comment=updated_comment,
        oversize_log="disable",
        switching_protocols_log="disable",
        http={"ports": [80, 8080, 8443], "status": "enable", "inspect_all": "enable"},
        ftp={"ports": [21], "status": "enable"},
        smtp={"ports": [25, 587], "status": "enable"},
        dns={"ports": [53], "status": "enable"}
    )
    assert result is not None
    assert result.http_status == "success"
    verify = fgt.api.cmdb.firewall.profile_protocol_options.get(name=TEST_NAME)
    assert verify is not None
    assert verify.http_status_code == 200
    assert verify.name == TEST_NAME
    assert verify.comment == updated_comment
    assert verify.oversize_log == "disable"
    assert verify.switching_protocols_log == "disable"

def test_get_specific_profile_protocol_options():
    result = fgt.api.cmdb.firewall.profile_protocol_options.get(name=TEST_NAME)
    assert result is not None
    assert result.name == TEST_NAME

def test_delete_profile_protocol_options():
    result = fgt.api.cmdb.firewall.profile_protocol_options.delete(name=TEST_NAME)
    assert result is not None
    assert result.http_status == "success"
    # Verify deletion
    profiles = fgt.api.cmdb.firewall.profile_protocol_options.get()
    names = [getattr(p, "name", None) for p in profiles]
    assert TEST_NAME not in names, "Profile protocol options should have been deleted"

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
    test_get_profile_protocol_options()
    print("✓ test_get_profile_protocol_options passed")
    test_post_profile_protocol_options()
    print("✓ test_post_profile_protocol_options passed")
    test_put_profile_protocol_options()
    print("✓ test_put_profile_protocol_options passed")
    test_get_specific_profile_protocol_options()
    print("✓ test_get_specific_profile_protocol_options passed")
    test_delete_profile_protocol_options()
    print("✓ test_delete_profile_protocol_options passed")
    cleanup()
    print("✓ post-Cleanup passed")
    print("\n✓ All tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
