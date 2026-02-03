import argparse
import sys
from pathlib import Path

import pytest

# Run DLP tests on a single worker to preserve state
pytestmark = pytest.mark.xdist_group("dlp")

# Add pytest directory to path (go up from endpoints/cmdb/ to pytest/)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt



def _get(obj, key):
    if isinstance(obj, dict):
        return obj.get(key)
    return getattr(obj, key, None)

def cleanup(module):
    """Teardown: Reset DLP settings after tests"""
    # Delete test DLP dictionaries
    dictionaries = fgt.api.cmdb.dlp.dictionary.get()
    for dictionary in dictionaries:
        name = _get(dictionary, 'name')
        if name and str(name).startswith("test_"):
            try:
                fgt.api.cmdb.dlp.dictionary.delete(name=name)
            except Exception:
                pass
    
    # Delete test DLP sensors
    sensors = fgt.api.cmdb.dlp.sensor.get()
    for sensor in sensors:
        name = _get(sensor, 'name')
        if name and str(name).startswith("test_"):
            try:
                fgt.api.cmdb.dlp.sensor.delete(name=name)
            except Exception:
                pass
    
    # Delete test DLP filepatterns
    filepatterns = fgt.api.cmdb.dlp.filepattern.get()
    for fp in filepatterns:
        name = _get(fp, 'name')
        if name and str(name).startswith("test_"):
            try:
                fgt.api.cmdb.dlp.filepattern.delete(id=_get(fp, 'id'))
            except Exception:
                pass
    
    # Delete test DLP data-types
    data_types = fgt.api.cmdb.dlp.data_type.get()
    for dt in data_types:
        name = _get(dt, 'name')
        if name and str(name).startswith("test_"):
            try:
                fgt.api.cmdb.dlp.data_type.delete(name=name)
            except Exception:
                pass
    
    # Reset DLP settings
    try:
        fgt.api.cmdb.dlp.settings.put(
            cache_mem_percent=2
        )
        settings = fgt.api.cmdb.dlp.settings.get()
        assert _get(settings, 'cache_mem_percent') == 2
    except Exception:
        pass


@pytest.fixture(autouse=True, scope="module")
def _dlp_cleanup():
    # Ensure duplicates don't fail tests under pytest/xdist
    cleanup(None)
    yield
    cleanup(None)

def verify_cleanup(module):
    """Verify teardown"""
    settings = fgt.api.cmdb.dlp.settings.get()
    assert _get(settings, 'cache_mem_percent') == 2

def test_get_dlp_settings():
    """Test: Get DLP settings"""
    result = fgt.api.cmdb.dlp.settings.get()
    assert result is not None
    assert _get(result, 'cache_mem_percent') is not None


def test_update_dlp_settings():
    """Test: Update DLP settings"""
    result = fgt.api.cmdb.dlp.settings.put(
        cache_mem_percent=1
    )

    assert result is not None  
    assert result.http_status == "success"

    # Verify update
    settings = fgt.api.cmdb.dlp.settings.get()
    assert _get(settings, 'cache_mem_percent') == 1


def test_post_dlp_sensor():
    """Test: Create DLP sensor"""
    result = fgt.api.cmdb.dlp.sensor.post(
        name="test_dlp_sensor1",
    )
    assert result is not None
    assert result.http_status == "success"

def test_put_dlp_sensor():
    """Test: Update DLP sensor"""
    result = fgt.api.cmdb.dlp.sensor.put(
        name="test_dlp_sensor1",
        comment="Updated by test"
    )
    assert result is not None
    assert result.http_status == "success"

    # Verify update
    sensor = fgt.api.cmdb.dlp.sensor.get(name="test_dlp_sensor1")
    assert sensor.comment == "Updated by test"

def test_get_dlp_sensor():
    """Test: Get DLP sensors"""
    result = fgt.api.cmdb.dlp.sensor.get()
    assert result is not None
    assert isinstance(result, list)

    assert any(sensor.name == "test_dlp_sensor1" for sensor in result)

def test_delete_dlp_sensor():
    """Test: Delete DLP sensor"""
    result = fgt.api.cmdb.dlp.sensor.delete(
        name="test_dlp_sensor1"
    )
    assert result is not None
    assert result.http_status == "success"

    # Verify deletion
    sensors = fgt.api.cmdb.dlp.sensor.get()
    assert all(sensor.name != "test_dlp_sensor1" for sensor in sensors)

def test_post_dlp_dictionary():
    """Test: Create DLP dictionary"""
    result = fgt.api.cmdb.dlp.dictionary.post(
        name="test_dlp_dict1",
        entries=[
            {
                "id": 1,
                "type": "g-credit-card",
                "pattern": "",
                "repeat": "enable",
                "status": "enable",
                "comment": "",
                "ignore_case": "enable"
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"

def test_get_dlp_dictionary():
    """Test: Get DLP dictionaries"""
    result = fgt.api.cmdb.dlp.dictionary.get()
    assert result is not None
    assert isinstance(result, list)
    assert any(d.name == "test_dlp_dict1" for d in result)

def test_get_specific_dlp_dictionary():
    """Test: Get specific DLP dictionary"""
    result = fgt.api.cmdb.dlp.dictionary.get(name="test_dlp_dict1")
    assert result is not None
    assert result.name == "test_dlp_dict1"

def test_put_dlp_dictionary():
    """Test: Update DLP dictionary"""
    result = fgt.api.cmdb.dlp.dictionary.put(
        name="test_dlp_dict1",
        comment="Updated by test"
    )
    assert result is not None
    assert result.http_status == "success"

    # Verify update
    dictionary = fgt.api.cmdb.dlp.dictionary.get(name="test_dlp_dict1")
    assert dictionary.comment == "Updated by test"

def test_delete_dlp_dictionary():
    """Test: Delete DLP dictionary"""
    result = fgt.api.cmdb.dlp.dictionary.delete(
        name="test_dlp_dict1"
    )
    assert result is not None
    assert result.http_status == "success"

    # Verify deletion
    dictionaries = fgt.api.cmdb.dlp.dictionary.get()
    assert all(d.name != "test_dlp_dict1" for d in dictionaries)

def test_post_dlp_filepattern():
    """Test: Create DLP filepattern"""
    result = fgt.api.cmdb.dlp.filepattern.post(
        name="test_dlp_filepattern1"
    )
    assert result is not None
    assert result.http_status == "success"

def test_put_dlp_filepattern():
    """Test: Update DLP filepattern"""
    # Get the filepattern to find its ID
    filepattern_list = fgt.api.cmdb.dlp.filepattern.get()
    test_fp = next(fp for fp in filepattern_list if fp.name == "test_dlp_filepattern1")
    
    result = fgt.api.cmdb.dlp.filepattern.put(
        id=test_fp.id,
        comment="Updated by test"
    )
    assert result is not None
    assert result.http_status == "success"

def test_get_specific_dlp_filepattern():
    """Test: Get specific DLP filepattern"""
    # Get all filepatterns to find the test one
    filepattern_list = fgt.api.cmdb.dlp.filepattern.get()
    test_fp = next(fp for fp in filepattern_list if fp.name == "test_dlp_filepattern1")
    
    # Get specific filepattern by ID
    filepattern = fgt.api.cmdb.dlp.filepattern.get(id=test_fp.id)
    assert filepattern is not None
    assert filepattern.name == "test_dlp_filepattern1"


def test_get_dlp_filepattern():
    """Test: Get DLP filepatterns"""
    result = fgt.api.cmdb.dlp.filepattern.get()
    assert result is not None
    assert isinstance(result, list)
    assert any(fp.name == "test_dlp_filepattern1" for fp in result)

def test_delete_dlp_filepattern():
    """Test: Delete DLP filepattern"""
    # Get the filepattern to find its ID
    filepattern_list = fgt.api.cmdb.dlp.filepattern.get()
    test_fp = next(fp for fp in filepattern_list if fp.name == "test_dlp_filepattern1")
    
    result = fgt.api.cmdb.dlp.filepattern.delete(id=test_fp.id)
    assert result is not None
    assert result.http_status == "success"

    # Verify deletion
    filepatterns = fgt.api.cmdb.dlp.filepattern.get()
    assert all(fp.name != "test_dlp_filepattern1" for fp in filepatterns)

def test_get_dlp_exact_data_match():
    """Test: Get DLP exact-data-match (EDM) - Read-only test"""
    result = fgt.api.cmdb.dlp.exact_data_match.get()
    assert result is not None
    assert isinstance(result, list)

def test_post_dlp_data_type():
    """Test: Create DLP data-type"""
    result = fgt.api.cmdb.dlp.data_type.post(
        name="test_dlp_data_type1",
        pattern="\\btest\\d{4}\\b"
    )
    assert result is not None
    assert result.http_status == "success"

def test_put_dlp_data_type():
    """Test: Update DLP data-type"""
    result = fgt.api.cmdb.dlp.data_type.put(
        name="test_dlp_data_type1",
        comment="Updated by test"
    )
    assert result is not None
    assert result.http_status == "success"

    # Verify update
    data_type = fgt.api.cmdb.dlp.data_type.get(name="test_dlp_data_type1")
    assert data_type.comment == "Updated by test"

def test_get_specific_dlp_data_type():
    """Test: Get specific DLP data-type"""
    result = fgt.api.cmdb.dlp.data_type.get(name="test_dlp_data_type1")
    assert result is not None
    assert result.name == "test_dlp_data_type1"

def test_get_dlp_data_type():
    """Test: Get DLP data-types"""
    result = fgt.api.cmdb.dlp.data_type.get()
    assert result is not None
    assert isinstance(result, list)
    assert any(dt.name == "test_dlp_data_type1" for dt in result)

def test_delete_dlp_data_type():
    """Test: Delete DLP data-type"""
    result = fgt.api.cmdb.dlp.data_type.delete(
        name="test_dlp_data_type1"
    )
    assert result is not None
    assert result.http_status == "success"

    # Verify deletion
    data_types = fgt.api.cmdb.dlp.data_type.get()
    assert all(dt.name != "test_dlp_data_type1" for dt in data_types)


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
    print("✓ Pre-cleanup passed (DLP)")

    test_get_dlp_settings()
    print("✓ test_get_dlp_settings passed")   
    test_update_dlp_settings()
    print("✓ test_update_dlp_settings passed")

    test_post_dlp_sensor()
    print("✓ test_post_dlp_sensor passed")

    test_put_dlp_sensor()
    print("✓ test_put_dlp_sensor passed")

    test_get_dlp_sensor()
    print("✓ test_get_dlp_sensor passed")

    test_delete_dlp_sensor()
    print("✓ test_delete_dlp_sensor passed")

    test_post_dlp_dictionary()
    print("✓ test_post_dlp_dictionary passed")

    test_get_dlp_dictionary()
    print("✓ test_get_dlp_dictionary passed")

    test_get_specific_dlp_dictionary()
    print("✓ test_get_specific_dlp_dictionary passed")

    test_put_dlp_dictionary()
    print("✓ test_put_dlp_dictionary passed")

    test_delete_dlp_dictionary()
    print("✓ test_delete_dlp_dictionary passed")

    test_post_dlp_filepattern()
    print("✓ test_post_dlp_filepattern passed")

    test_put_dlp_filepattern()
    print("✓ test_put_dlp_filepattern passed")

    test_get_specific_dlp_filepattern()
    print("✓ test_get_specific_dlp_filepattern passed")

    test_get_dlp_filepattern()
    print("✓ test_get_dlp_filepattern passed")

    test_delete_dlp_filepattern()
    print("✓ test_delete_dlp_filepattern passed")

    test_get_dlp_exact_data_match()
    print("✓ test_get_dlp_exact_data_match passed")

    test_post_dlp_data_type()
    print("✓ test_post_dlp_data_type passed")

    test_put_dlp_data_type()
    print("✓ test_put_dlp_data_type passed")

    test_get_specific_dlp_data_type()
    print("✓ test_get_specific_dlp_data_type passed")

    test_get_dlp_data_type()
    print("✓ test_get_dlp_data_type passed")

    test_delete_dlp_data_type()
    print("✓ test_delete_dlp_data_type passed")

    cleanup(None)
    print("✓ cleanup passed")
    verify_cleanup(None)
    print("✓ verify_cleanup passed")
    print("\n✓ All tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
