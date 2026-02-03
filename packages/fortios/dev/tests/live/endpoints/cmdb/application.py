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


pytestmark = pytest.mark.xdist_group("cmdb_application")


@pytest.fixture(autouse=True, scope="module")
def _application_cleanup():
    cleanup()
    yield
    cleanup()


def cleanup():
    try:
        lists = fgt.api.cmdb.application.list.get()
        for item in lists:
            name = _get(item, "name")
            if name and str(name).startswith("test_"):
                try:
                    fgt.api.cmdb.application.list.delete(name=name)
                except Exception:
                    pass
    except Exception:
        pass

    try:
        customs = fgt.api.cmdb.application.custom.get()
        for item in customs:
            tag = _get(item, "tag")
            if tag and str(tag).startswith("test_"):
                try:
                    fgt.api.cmdb.application.custom.delete(tag=tag)
                except Exception:
                    pass
    except Exception:
        pass

    try:
        groups = fgt.api.cmdb.application.group.get()
        for item in groups:
            name = _get(item, "name")
            if name and str(name).startswith("test_"):
                try:
                    fgt.api.cmdb.application.group.delete(name=name)
                except Exception:
                    pass
    except Exception:
        pass

def test_get_application_list():
    """Test: Get application list"""
    result = fgt.api.cmdb.application.list.get()
    assert result is not None
    assert isinstance(result, list)

def test_post_application_list():
    """Test: Create custom application list"""
    result = fgt.api.cmdb.application.list.post(
        name="test_app_list1",
        comment="Test application list created by pytest"
    )
    assert result is not None
    assert result.http_status == "success"

def test_get_specific_application_list():
    """Test: Get specific application list"""
    result = fgt.api.cmdb.application.list.get(name="test_app_list1")
    assert result is not None
    assert _get(result, "name") == "test_app_list1"
    assert _get(result, "comment") == "Test application list created by pytest"

def test_update_application_list():
    """Test: Update application list"""
    result = fgt.api.cmdb.application.list.put(
        name="test_app_list1",
        comment="Updated application list comment by pytest"
    )
    assert result is not None
    assert result.http_status == "success"
    
    # Verify update
    app_list = fgt.api.cmdb.application.list.get(name="test_app_list1")
    assert _get(app_list, "name") == "test_app_list1"
    assert _get(app_list, "comment") == "Updated application list comment by pytest"

def test_delete_application_list():
    """Test: Delete application list"""
    result = fgt.api.cmdb.application.list.delete(name="test_app_list1")
    assert result is not None
    assert result.http_status == "success"
    
    # Verify deletion
    lists = fgt.api.cmdb.application.list.get()
    list_names = [_get(a, 'name') for a in lists]
    assert "test_app_list1" not in list_names


def test_get_application_custom():
    """Test: Get custom applications"""
    result = fgt.api.cmdb.application.custom.get()
   
    assert result is not None
    assert isinstance(result, list)

def test_post_application_custom():
    """Test: Create custom application"""
    result = fgt.api.cmdb.application.custom.post(
        tag="test_custom_app1",
        signature='F-SBID( --name "test_custom_app1"; --protocol tcp; --flow from_client; --dst_port 8080; --pattern "test"; --context packet; --app_cat 5; --weight 10; )'
    )
    assert result is not None
    assert result.http_status == "success"

def test_get_specific_application_custom():
    """Test: Get specific custom application"""
    result = fgt.api.cmdb.application.custom.get(tag="test_custom_app1")
    assert result is not None
    assert _get(result, "tag") == "test_custom_app1"
    assert _get(result, "signature") is not None

def test_update_application_custom():
    """Test: Update custom application"""
    result = fgt.api.cmdb.application.custom.put(
        tag="test_custom_app1",
        signature='F-SBID( --name "test_custom_app1"; --protocol tcp; --flow from_client; --dst_port 9090; --pattern "updated"; --context packet; --app_cat 5; --weight 15; )'
    )
    assert result is not None
    assert result.http_status == "success"
    
    # Verify update
    app = fgt.api.cmdb.application.custom.get(tag="test_custom_app1")
    assert _get(app, "tag") == "test_custom_app1"

def test_delete_application_custom():
    """Test: Delete custom application"""
    result = fgt.api.cmdb.application.custom.delete(tag="test_custom_app1")
    assert result is not None
    assert result.http_status == "success"
    
    # Verify deletion
    apps = fgt.api.cmdb.application.custom.get()
    app_tags = [_get(a, 'tag') for a in apps]
    assert "test_custom_app1" not in app_tags


# Application Group CRUD Tests
def test_get_application_group():
    """Test: Get application groups"""
    result = fgt.api.cmdb.application.group.get()
    assert result is not None
    assert isinstance(result, list)

def test_post_application_group():
    """Test: Create application group"""
    result = fgt.api.cmdb.application.group.post(
        name="test_app_group1",
        comment="Test application group created by pytest",
        type="filter",  # Required: application or filter
        category=[{"id": 2}]  # Using category ID 2 (General Interest)
    )
    assert result is not None
    assert result.http_status == "success"

def test_get_specific_application_group():
    """Test: Get specific application group"""
    result = fgt.api.cmdb.application.group.get(name="test_app_group1")
    assert result is not None
    assert _get(result, "name") == "test_app_group1"
    assert _get(result, "comment") == "Test application group created by pytest"

def test_update_application_group():
    """Test: Update application group"""
    result = fgt.api.cmdb.application.group.put(
        name="test_app_group1",
        comment="Updated application group comment by pytest"
    )
    assert result is not None
    assert result.http_status == "success"
    
    # Verify update
    group = fgt.api.cmdb.application.group.get(name="test_app_group1")
    assert _get(group, "name") == "test_app_group1"
    assert _get(group, "comment") == "Updated application group comment by pytest"

def test_delete_application_group():
    """Test: Delete application group"""
    result = fgt.api.cmdb.application.group.delete(name="test_app_group1")
    assert result is not None
    assert result.http_status == "success"
    
    # Verify deletion
    groups = fgt.api.cmdb.application.group.get()
    group_names = [_get(g, 'name') for g in groups]
    assert "test_app_group1" not in group_names


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
    # Pre-cleanup: Check if test entries exist before attempting to delete
    try:
        app_lists = fgt.api.cmdb.application.list.get()
        if any(_get(a, 'name') == "test_app_list1" for a in app_lists):
            fgt.api.cmdb.application.list.delete(name="test_app_list1")
    except:
        pass
    
    try:
        custom_apps = fgt.api.cmdb.application.custom.get()
        if any(_get(a, 'tag') == "test_custom_app1" for a in custom_apps):
            fgt.api.cmdb.application.custom.delete(tag="test_custom_app1")
    except:
        pass
    
    try:
        app_groups = fgt.api.cmdb.application.group.get()
        if any(_get(g, 'name') == "test_app_group1" for g in app_groups):
            fgt.api.cmdb.application.group.delete(name="test_app_group1")
    except:
        pass
    
    test_get_application_list()
    print("✓ test_get_application_list passed")
    
    test_post_application_list()
    print("✓ test_post_application_list passed")
    
    test_get_specific_application_list()
    print("✓ test_get_specific_application_list passed")
    
    test_update_application_list()
    print("✓ test_update_application_list passed")
    
    test_delete_application_list()
    print("✓ test_delete_application_list passed")

    test_get_application_custom()
    print("✓ test_get_application_custom passed")

    test_post_application_custom()
    print("✓ test_post_application_custom passed")
    
    test_get_specific_application_custom()
    print("✓ test_get_specific_application_custom passed")
    
    test_update_application_custom()
    print("✓ test_update_application_custom passed")
    
    test_delete_application_custom()
    print("✓ test_delete_application_custom passed")
    
    # Application Group Tests
    test_get_application_group()
    print("✓ test_get_application_group passed")
    
    test_post_application_group()
    print("✓ test_post_application_group passed")
    
    test_get_specific_application_group()
    print("✓ test_get_specific_application_group passed")
    
    test_update_application_group()
    print("✓ test_update_application_group passed")
    
    test_delete_application_group()
    print("✓ test_delete_application_group passed")
    
    print("\n✓ All tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
