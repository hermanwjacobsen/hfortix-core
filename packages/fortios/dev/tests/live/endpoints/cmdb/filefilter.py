import argparse
import sys
from pathlib import Path

import pytest

# Run DLP tests on a single worker to preserve state
pytestmark = pytest.mark.xdist_group("file-filter")

# Add pytest directory to path (go up from endpoints/cmdb/ to pytest/)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt


def cleanup():
    ## Cleanup ##
    try:
        filefilter_profiles = fgt.api.cmdb.file_filter.profile.get()
        for profile in filefilter_profiles:
            name = profile.name
            if name and str(name).startswith("test_"):
                try:
                    fgt.api.cmdb.file_filter.profile.delete(name=name)
                except Exception:
                    pass
    except Exception:
        pass


def test_get_filefilter_profile():
    """Test: Get filefilter settings"""
    result = fgt.api.cmdb.file_filter.profile.get()
    assert result is not None
    assert result.http_status_code == 200

def test_post_filefilter_profile():
    """Test: Create filefilter profile"""
    result = fgt.api.cmdb.file_filter.profile.post(
        name="test_filefilter_profile1",
        comment="Test File Filter Profile"
    )
    assert result is not None
    assert result.http_status == "success"

def test_put_filefilter_profile():
    """Test: Update filefilter profile"""
    result = fgt.api.cmdb.file_filter.profile.put(
        name="test_filefilter_profile1",
        comment="Updated Test File Filter Profile"
    )
    assert result is not None
    assert result.http_status == "success"
    verify = fgt.api.cmdb.file_filter.profile.get(name="test_filefilter_profile1")
    assert verify is not None
    assert verify.http_status_code == 200
    assert verify.comment == "Updated Test File Filter Profile"

def test_get_specific_filefilter_profile():
    """Test: Get specific filefilter profile"""
    result = fgt.api.cmdb.file_filter.profile.get(name="test_filefilter_profile1")
    assert result is not None
    assert result.name == "test_filefilter_profile1"
    assert result.comment == "Updated Test File Filter Profile"

def test_delete_filefilter_profile():
    """Test: Delete filefilter profile"""
    result = fgt.api.cmdb.file_filter.profile.delete(name="test_filefilter_profile1")
    assert result is not None
    assert result.http_status == "success"
    
    # Verify deletion - get all and check it's not in list
    profiles = fgt.api.cmdb.file_filter.profile.get()
    profile_names = [p.name for p in profiles]
    assert "test_filefilter_profile1" not in profile_names, "Profile should have been deleted"


    
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

    test_get_filefilter_profile()
    print("✓ test_get_filefilter_profile passed")

    test_post_filefilter_profile()
    print("✓ test_post_filefilter_profile passed")

    test_put_filefilter_profile()
    print("✓ test_put_filefilter_profile passed")

    test_get_specific_filefilter_profile()
    print("✓ test_get_specific_filefilter_profile passed")

    test_delete_filefilter_profile()
    print("✓ test_delete_filefilter_profile passed")
        
    cleanup()
    print("✓ post-Cleanup passed")
    
    print("\n✓ All tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
