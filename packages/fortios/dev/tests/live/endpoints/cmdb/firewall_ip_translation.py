import argparse
import sys
from pathlib import Path
import pytest

pytestmark = pytest.mark.xdist_group(Path(__file__).stem)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt

TEST_ID = 9999997
TEST_TYPE = "SCTP"
TEST_STARTIP = "10.10.10.1"
TEST_ENDIP = "10.10.10.2"
TEST_MAP_STARTIP = "10.20.20.1"


def cleanup():
    try:
        translations = fgt.api.cmdb.firewall.ip_translation.get()
        for translation in translations:
            if getattr(translation, "transid", None) == TEST_ID:
                fgt.api.cmdb.firewall.ip_translation.delete(transid=TEST_ID)
                break
    except Exception:
        pass

def test_get_ip_translation():
    result = fgt.api.cmdb.firewall.ip_translation.get()
    assert result is not None
    assert result.http_status_code == 200

def test_post_ip_translation():
    result = fgt.api.cmdb.firewall.ip_translation.post(
        transid=TEST_ID,
        type=TEST_TYPE,
        startip=TEST_STARTIP,
        endip=TEST_ENDIP,
        map_startip=TEST_MAP_STARTIP
    )
    assert result is not None
    assert result.http_status == "success"

def test_put_ip_translation():
    result = fgt.api.cmdb.firewall.ip_translation.put(
        transid=TEST_ID,
        type=TEST_TYPE,
        startip="10.10.10.3",
        endip="10.10.10.4",
        map_startip="10.20.20.2"
    )
    assert result is not None
    assert result.http_status == "success"
    verify = fgt.api.cmdb.firewall.ip_translation.get(transid=TEST_ID)
    assert verify is not None
    assert verify.http_status_code == 200
    assert verify.startip == "10.10.10.3"
    assert verify.endip == "10.10.10.4"
    assert verify.map_startip == "10.20.20.2"

def test_get_specific_ip_translation():
    result = fgt.api.cmdb.firewall.ip_translation.get(transid=TEST_ID)
    assert result is not None
    assert result.transid == TEST_ID

def test_delete_ip_translation():
    result = fgt.api.cmdb.firewall.ip_translation.delete(transid=TEST_ID)
    assert result is not None
    assert result.http_status == "success"
    # Verify deletion
    translations = fgt.api.cmdb.firewall.ip_translation.get()
    ids = [getattr(t, "transid", None) for t in translations]
    assert TEST_ID not in ids, "IP translation should have been deleted"

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
    test_get_ip_translation()
    print("✓ test_get_ip_translation passed")
    test_post_ip_translation()
    print("✓ test_post_ip_translation passed")
    test_put_ip_translation()
    print("✓ test_put_ip_translation passed")
    test_get_specific_ip_translation()
    print("✓ test_get_specific_ip_translation passed")
    test_delete_ip_translation()
    print("✓ test_delete_ip_translation passed")
    cleanup()
    print("✓ post-Cleanup passed")
    print("\n✓ All tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
