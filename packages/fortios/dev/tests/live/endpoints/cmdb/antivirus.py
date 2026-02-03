import argparse
import sys
from pathlib import Path
from unicodedata import name

import pytest

# Ensure all tests in this module run on the same xdist worker to preserve state
pytestmark = pytest.mark.xdist_group("antivirus")

# Add pytest directory to path (go up from endpoints/cmdb/ to pytest/)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt



def _get(obj, key):
    """Get attribute from FortiObject or dict."""
    if isinstance(obj, dict):
        return obj.get(key)
    return getattr(obj, key, None)

def cleanup(_module=None):
    av_profile_list = fgt.api.cmdb.antivirus.profile.get()
    for profile in av_profile_list:
        name = _get(profile, 'name')
        if name and str(name).startswith('test_'):
            try:
                fgt.api.cmdb.antivirus.profile.delete(name=name)
            except Exception:
                pass
    
    av_exempt_list = fgt.api.cmdb.antivirus.exempt_list.get()
    for entry in av_exempt_list:
        name = _get(entry, 'name')
        if name and str(name).startswith('test_'):
            try:
                fgt.api.cmdb.antivirus.exempt_list.delete(name=name)
            except Exception:
                pass

    try:
        fgt.api.cmdb.antivirus.settings.put(grayware="disable")
    except Exception:
        pass


@pytest.fixture(autouse=True, scope="module")
def _antivirus_cleanup():
    # Ensure duplicates or dirty state don't leak between runs under pytest
    cleanup()
    yield
    cleanup()


def test_get_antivirus_settings():
    """Test: Get antivirus settings"""
    result = fgt.api.cmdb.antivirus.settings.get()
    assert result is not None
    assert _get(result, 'grayware') is not None

def test_update_antivirus_settings():
    """Test: Update antivirus grayware setting"""
    result = fgt.api.cmdb.antivirus.settings.put(grayware="enable")
    assert result is not None
    
    # Verify update
    settings = fgt.api.cmdb.antivirus.settings.get()
    assert _get(settings, 'grayware') == "enable"

def test_put_antivirus_settings():
    """Teardown: Reset antivirus settings after tests"""
    fgt.api.cmdb.antivirus.settings.put(grayware="disable")

def test_get_antivirus_quarantine():
    """Test: Get antivirus quarantine settings"""
    result = fgt.api.cmdb.antivirus.quarantine.get()
    assert result is not None   
    assert _get(result, 'maxfilesize') is not None

def test_put_antivirus_quarantine():
    """Test: Update antivirus quarantine settings"""
    result = fgt.api.cmdb.antivirus.quarantine.put(maxfilesize=500)
    assert result is not None
    
    # Verify update
    settings = fgt.api.cmdb.antivirus.quarantine.get()
    assert _get(settings, 'maxfilesize') == 500   

def test_get_antivirus_profile():
    """Test: Get antivirus profiles"""
    result = fgt.api.cmdb.antivirus.profile.get()
    assert result is not None
    assert isinstance(result, list)

def test_post_antivirus_profile():
    """Test: Create antivirus profile"""
    result = fgt.api.cmdb.antivirus.profile.post(name="test_profile1", comment="Test profile created by pytest")
    assert result is not None
    assert result.http_status == "success"


def test_get_specific_antivirus_profile():
    """Test: Get specific antivirus profile"""
    result = fgt.api.cmdb.antivirus.profile.get(name="test_profile1")
    assert result is not None
    assert _get(result, 'name') == "test_profile1"

def test_update_antivirus_profile():
    """Test: Update antivirus profile comment"""
    result = fgt.api.cmdb.antivirus.profile.put(name="test_profile1", comment="Updated comment by pytest")
    assert result is not None
    assert result.http_status == "success"
    
    # Verify update
    profile = fgt.api.cmdb.antivirus.profile.get(name="test_profile1")
    assert _get(profile, 'name') == "test_profile1"
    assert _get(profile, 'comment') == "Updated comment by pytest"

def test_delete_antivirus_profile():
    """Test: Delete antivirus profile"""
    result = fgt.api.cmdb.antivirus.profile.delete(name="test_profile1")
    assert result is not None
    assert result.http_status == "success" 
    
    # Verify deletion
    profiles = fgt.api.cmdb.antivirus.profile.get()
    profile_names = [_get(profile, 'name') for profile in profiles]
    assert "test_profile1" not in profile_names

def test_get_exempt_list():
    """Test: Get antivirus exempt list"""
    result = fgt.api.cmdb.antivirus.exempt_list.get()
    assert result is not None
    assert isinstance(result, list)

def test_post_antivirus_exempt_list():
    """Test: Create antivirus exempt list entry"""
    result = fgt.api.cmdb.antivirus.exempt_list.post(
        name="test_exempt1", 
        comment="Test exempt list entry created by pytest",
        hash_type="md5",
        hash="5d41402abc4b2a76b9719d911017c592",  # MD5 hash example (32 chars)
        status="enable"
    )
    assert result is not None
    assert result.http_status == "success"

def test_get_specific_exempt_list():
    """Test: Get specific exempt list entry"""
    result = fgt.api.cmdb.antivirus.exempt_list.get(name="test_exempt1")
    assert result is not None
    assert _get(result, 'name') == "test_exempt1"
    assert _get(result, 'hash_type') == "md5"

def test_update_exempt_list():
    """Test: Update exempt list entry"""
    result = fgt.api.cmdb.antivirus.exempt_list.put(
        name="test_exempt1",
        comment="Updated exempt list comment by pytest",
        hash_type="sha256",
        hash="e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",  # SHA256 hash (64 chars)
        status="disable"
    )
    assert result is not None
    assert result.http_status == "success"
    
    # Verify update
    entry = fgt.api.cmdb.antivirus.exempt_list.get(name="test_exempt1")
    assert _get(entry, 'name') == "test_exempt1"
    assert _get(entry, 'comment') == "Updated exempt list comment by pytest"
    assert _get(entry, 'hash_type') == "sha256"
    assert _get(entry, 'status') == "disable"

def test_delete_exempt_list():
    """Test: Delete exempt list entry"""
    result = fgt.api.cmdb.antivirus.exempt_list.delete(name="test_exempt1")
    assert result is not None
    assert result.http_status == "success"
    
    # Verify deletion
    entries = fgt.api.cmdb.antivirus.exempt_list.get()
    entry_names = [_get(entry, 'name') for entry in entries]
    assert "test_exempt1" not in entry_names

def cleanup_antivirus_quarantine(module):
    """Teardown: Reset antivirus quarantine settings after tests"""
    fgt.api.cmdb.antivirus.quarantine.put(maxfilesize=0)    

def verify_cleanup(module):
    """Verify teardown"""
    settings = fgt.api.cmdb.antivirus.settings.get()
    quarantine_settings = fgt.api.cmdb.antivirus.quarantine.get()
    assert _get(quarantine_settings, 'maxfilesize') == 0
    assert _get(settings, 'grayware') == "disable" 



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
    cleanup(None)
    print("✓ Pre-cleanup passed (Antivirus)")

    test_get_antivirus_settings()
    print("✓ test_get_antivirus_settings passed")

    test_update_antivirus_settings()
    print("✓ test_update_antivirus passed")

    test_put_antivirus_settings()
    print("✓ test_put_antivirus_settings passed")  
    
    test_get_antivirus_quarantine()
    print("✓ test_get_antivirus_quarantine passed")

    test_put_antivirus_quarantine()
    print("✓ test_put_antivirus_quarantine passed")

    test_get_antivirus_profile()
    print("✓ test_get_antivirus_profile passed")

    test_post_antivirus_profile()
    print("✓ test_post_antivirus_profile passed")

    test_get_specific_antivirus_profile()
    print("✓ test_get_specific_antivirus_profile passed")

    test_update_antivirus_profile()
    print("✓ test_update_antivirus_profile passed")

    test_delete_antivirus_profile()
    print("✓ test_delete_antivirus_profile passed")

    test_get_exempt_list()
    print("✓ test_get_exempt_list passed")

    test_post_antivirus_exempt_list()
    print("✓ test_post_antivirus_exempt_list passed")

    test_get_specific_exempt_list()
    print("✓ test_get_specific_exempt_list passed")

    test_update_exempt_list()
    print("✓ test_update_exempt_list passed")

    test_delete_exempt_list()
    print("✓ test_delete_exempt_list passed")

    cleanup_antivirus_quarantine(None)
    print("✓ cleanup and verify_cleanup passed")


    cleanup(None)
    verify_cleanup(None)     
    print("✓ final cleanup passed (Antivirus)")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
