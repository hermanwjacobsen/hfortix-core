import argparse
import sys
from pathlib import Path
import pytest

pytestmark = pytest.mark.xdist_group(Path(__file__).stem)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt

TEST_NAME = "test_inet_svc_custom1"
TEST_COMMENT = "pytest custom internet service"


def cleanup():
    # Cleanup test objects
    try:
        customs = fgt.api.cmdb.firewall.internet_service_custom.get()
        for obj in customs:
            if getattr(obj, "name", None) == TEST_NAME:
                try:
                    fgt.api.cmdb.firewall.internet_service_custom.delete(name=TEST_NAME)
                except Exception:
                    pass
    except Exception:
        pass

def test_get_internet_service_custom():
    """Test: Get internet service custom entries"""
    result = fgt.api.cmdb.firewall.internet_service_custom.get()
    assert result is not None
    assert result.http_status_code == 200

def test_post_internet_service_custom():
    """Test: Create custom internet service"""
    result = fgt.api.cmdb.firewall.internet_service_custom.post(
        name=TEST_NAME,
        comment=TEST_COMMENT,
        entry=[]
    )
    assert result is not None
    assert result.http_status == "success"

def test_put_internet_service_custom():
    """Test: Update custom internet service"""
    result = fgt.api.cmdb.firewall.internet_service_custom.put(
        name=TEST_NAME,
        comment="pytest custom internet service updated"
    )
    assert result is not None
    assert result.http_status == "success"
    verify = fgt.api.cmdb.firewall.internet_service_custom.get(name=TEST_NAME)
    assert verify is not None
    assert verify.http_status_code == 200
    assert verify.comment == "pytest custom internet service updated"

def test_get_specific_internet_service_custom():
    """Test: Get specific custom internet service"""
    result = fgt.api.cmdb.firewall.internet_service_custom.get(name=TEST_NAME)
    assert result is not None
    assert result.name == TEST_NAME

def test_delete_internet_service_custom():
    """Test: Delete custom internet service"""
    result = fgt.api.cmdb.firewall.internet_service_custom.delete(name=TEST_NAME)
    assert result is not None
    assert result.http_status == "success"
    # Verify deletion
    customs = fgt.api.cmdb.firewall.internet_service_custom.get()
    names = [getattr(c, "name", None) for c in customs]
    assert TEST_NAME not in names, "Custom internet service should have been deleted"

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
    test_get_internet_service_custom()
    print("✓ test_get_internet_service_custom passed")
    test_post_internet_service_custom()
    print("✓ test_post_internet_service_custom passed")
    test_put_internet_service_custom()
    print("✓ test_put_internet_service_custom passed")
    test_get_specific_internet_service_custom()
    print("✓ test_get_specific_internet_service_custom passed")
    test_delete_internet_service_custom()
    print("✓ test_delete_internet_service_custom passed")
    cleanup()
    print("✓ post-Cleanup passed")
    print("\n✓ All tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
