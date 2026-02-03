import argparse
import sys
from pathlib import Path

import pytest

# Add pytest directory to path (go up from endpoints/cmdb/ to pytest/)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt



def _get(obj, key):
    if isinstance(obj, dict):
        return obj.get(key)
    return getattr(obj, key, None)


pytestmark = pytest.mark.xdist_group("cmdb_authentication")


def test_get_authentication_setting():
    """Test: Get authentication settings"""
    result = fgt.api.cmdb.authentication.setting.get()
    assert result is not None

def test_update_authentication_setting():
    """Test: Update authentication setting"""
    result = fgt.api.cmdb.authentication.setting.put(persistent_cookie="enable")
    assert result is not None
    assert result.http_status == "success"
    
    # Verify update
    settings = fgt.api.cmdb.authentication.setting.get()
    assert _get(settings, 'persistent_cookie') == "enable"

def test_reset_authentication_setting():
    """Test: Reset authentication setting"""
    result = fgt.api.cmdb.authentication.setting.put(persistent_cookie="disable")
    assert result is not None
    assert result.http_status == "success"
    
    # Verify reset
    settings = fgt.api.cmdb.authentication.setting.get()
    assert _get(settings, 'persistent_cookie') == "disable"

def test_get_authentication_scheme():
    """Test: Get authentication schemes"""
    result = fgt.api.cmdb.authentication.scheme.get()
    assert result is not None
    assert isinstance(result, list)

def test_post_authentication_scheme():
    """Test: Create authentication scheme"""
    result = fgt.api.cmdb.authentication.scheme.post(
        name="test_scheme1",
        method="basic",
        user_database=[{"name": "local-user-db"}]
    )
    assert result is not None
    assert result.http_status == "success"

def test_get_specific_authentication_scheme():
    """Test: Get specific authentication scheme"""
    result = fgt.api.cmdb.authentication.scheme.get(name="test_scheme1")
    assert result is not None
    assert _get(result, 'name') == "test_scheme1"
    assert _get(result, 'method') == "basic"

def test_update_authentication_scheme():
    """Test: Update authentication scheme"""
    result = fgt.api.cmdb.authentication.scheme.put(
        name="test_scheme1",
        method="basic",
        user_database=[{"name": "local-user-db"}],
        require_tfa="enable"
    )
    assert result is not None
    assert result.http_status == "success"
    
    # Verify update
    scheme = fgt.api.cmdb.authentication.scheme.get(name="test_scheme1")
    assert _get(scheme, 'name') == "test_scheme1"
    assert _get(scheme, 'require_tfa') == "enable"

def test_delete_authentication_scheme():
    """Test: Delete authentication scheme"""
    result = fgt.api.cmdb.authentication.scheme.delete(name="test_scheme1")
    assert result is not None
    assert result.http_status == "success"
    
    # Verify deletion
    schemes = fgt.api.cmdb.authentication.scheme.get()
    scheme_names = [s.name for s in schemes]
    assert "test_scheme1" not in scheme_names


def test_get_authentication_rule():
    """Test: Get authentication rules"""
    result = fgt.api.cmdb.authentication.rule.get()
    assert result is not None
    assert isinstance(result, list)

def test_get_authentication_rule_defaults():
    """Test: Get authentication rule defaults"""
    result = fgt.api.cmdb.authentication.rule.defaults()
    assert result is not None

def test_post_authentication_rule():
    """Test: Create authentication rule"""
    result = fgt.api.cmdb.authentication.rule.post(
        name="test_rule1",
        srcaddr=[{"name": "all"}],
        srcintf=[{"name": "any"}]
    )
    assert result is not None
    assert result.http_status == "success"

def test_get_specific_authentication_rule():
    """Test: Get specific authentication rule"""
    result = fgt.api.cmdb.authentication.rule.get(name="test_rule1")
    assert result is not None
    assert _get(result, 'name') == "test_rule1"

def test_update_authentication_rule1():
    """Test: Update authentication rule"""
    result = fgt.api.cmdb.authentication.rule.put(
        name="test_rule1",
        srcaddr=[{"name": "all"}],
        srcintf=[{"name": "port3"}]
    )
    assert result is not None
    assert result.http_status == "success"
    
    # Verify update
    rule = fgt.api.cmdb.authentication.rule.get(name="test_rule1")
    assert _get(rule, 'name') == "test_rule1"
    srcintf = _get(rule, 'srcintf') or []
    assert any(_get(intf, 'name') == "port3" for intf in srcintf)

def test_update_authentication_rule2():
    """Test: Update authentication rule"""
    result = fgt.api.cmdb.authentication.rule.put(
        name="test_rule1",
        srcaddr=[{"name": "all"}],
        srcintf=[{"name": "port3"}]
    )
    assert result is not None
    assert result.http_status == "success"
    
    # Verify update
    rule = fgt.api.cmdb.authentication.rule.get(name="test_rule1")
    assert _get(rule, 'name') == "test_rule1"
    srcintf = _get(rule, 'srcintf') or []
    assert any(_get(intf, 'name') == "port3" for intf in srcintf)



def test_delete_authentication_rule():
    """Test: Delete authentication rule"""
    result = fgt.api.cmdb.authentication.rule.delete(name="test_rule1")
    assert result is not None
    assert result.http_status == "success"
    
    # Verify deletion
    rules = fgt.api.cmdb.authentication.rule.get()
    rule_names = [r.name     for r in rules]
    assert "test_rule1" not in rule_names


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
    # Pre-cleanup: Remove test scheme if it exists
    try:
        schemes = fgt.api.cmdb.authentication.scheme.get()
        if any(s.name == "test_scheme1" for s in schemes):
            fgt.api.cmdb.authentication.scheme.delete(name="test_scheme1")
            print("Pre-cleanup: Removed existing test_scheme1")
    except:
        pass

    try:
        rules = fgt.api.cmdb.authentication.rule.get()
        if any(r.name == "test_rule1" for r in rules):
            fgt.api.cmdb.authentication.rule.delete(name="test_rule1")
            print("Pre-cleanup: Removed existing test_rule1")
    except:
        pass
    
    test_get_authentication_setting()
    print("✓ test_get_authentication_setting passed")
    
    test_update_authentication_setting()
    print("✓ test_update_authentication_setting passed")
    
    test_reset_authentication_setting()
    print("✓ test_reset_authentication_setting passed")
    
    test_get_authentication_scheme()
    print("✓ test_get_authentication_scheme passed")
    
    test_post_authentication_scheme()
    print("✓ test_post_authentication_scheme passed")
    
    test_get_specific_authentication_scheme()
    print("✓ test_get_specific_authentication_scheme passed")
    
    test_update_authentication_scheme()
    print("✓ test_update_authentication_scheme passed")
    
    test_delete_authentication_scheme()
    print("✓ test_delete_authentication_scheme passed")
    
    test_get_authentication_rule()
    print("✓ test_get_authentication_rule passed")
    
    test_get_authentication_rule_defaults()
    print("✓ test_get_authentication_rule_defaults passed")
    
    test_post_authentication_rule()
    print("✓ test_post_authentication_rule passed")
    
    test_get_specific_authentication_rule()
    print("✓ test_get_specific_authentication_rule passed")
    
    test_delete_authentication_rule()
    print("✓ test_delete_authentication_rule passed")
    
    print("\n✓ All tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
