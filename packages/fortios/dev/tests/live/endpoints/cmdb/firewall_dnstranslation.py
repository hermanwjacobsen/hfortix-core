import argparse
import sys
from pathlib import Path

import pytest

# Run tests on a single worker to preserve state (group by filename)
pytestmark = pytest.mark.xdist_group(Path(__file__).stem)

# Add pytest directory to path (go up from endpoints/cmdb/ to pytest/)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt


TEST_ID = 10001


def cleanup():
    """Clean up test DNS translations."""
    try:
        entries = fgt.api.cmdb.firewall.dnstranslation.get()
        for entry in entries:
            if entry.id == TEST_ID:
                try:
                    fgt.api.cmdb.firewall.dnstranslation.delete(id=entry.id)
                except Exception:
                    pass
    except Exception:
        pass


def test_get_dnstranslations():
    """Test: Get all DNS translations."""
    result = fgt.api.cmdb.firewall.dnstranslation.get()
    assert result is not None
    assert result.http_status_code == 200


def test_post_dnstranslation():
    """Test: Create DNS translation entry."""
    result = fgt.api.cmdb.firewall.dnstranslation.post(
        id=TEST_ID,
        src="10.10.10.10",
        dst="20.20.20.20",
        netmask="255.255.255.255",
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_dnstranslation():
    """Test: Update DNS translation entry."""
    result = fgt.api.cmdb.firewall.dnstranslation.put(
        id=TEST_ID,
        dst="20.20.20.21",
    )
    assert result is not None
    assert result.http_status == "success"
    
    # Verify the update
    verify = fgt.api.cmdb.firewall.dnstranslation.get(id=TEST_ID)
    assert verify is not None
    assert verify.dst == "20.20.20.21"


def test_get_specific_dnstranslation():
    """Test: Get specific DNS translation entry."""
    result = fgt.api.cmdb.firewall.dnstranslation.get(id=TEST_ID)
    assert result is not None
    assert result.id == TEST_ID


def test_delete_dnstranslation():
    """Test: Delete DNS translation entry."""
    result = fgt.api.cmdb.firewall.dnstranslation.delete(id=TEST_ID)
    assert result is not None
    assert result.http_status == "success"
    
    # Verify deletion
    entries = fgt.api.cmdb.firewall.dnstranslation.get()
    ids = [e.id for e in entries]
    assert TEST_ID not in ids, "DNS translation entry should have been deleted"


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
        
    test_get_dnstranslations()
    print("✓ test_get_dnstranslations passed")

    test_post_dnstranslation()
    print("✓ test_post_dnstranslation passed")

    test_put_dnstranslation()
    print("✓ test_put_dnstranslation passed")

    test_get_specific_dnstranslation()
    print("✓ test_get_specific_dnstranslation passed")

    test_delete_dnstranslation()
    print("✓ test_delete_dnstranslation passed")

    cleanup()
    print("✓ post-Cleanup passed")
    
    print("\n✓ All tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
