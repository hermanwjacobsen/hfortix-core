import argparse
import sys
from pathlib import Path
import pytest

# Add pytest directory to path (go up from endpoints/cmdb/ to pytest/)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt


def cleanup():
    """Teardown: Delete test diameter filter entries"""
    diameter_filters = fgt.api.cmdb.diameter_filter.profile.get()
    for df in diameter_filters:
        if df.name.startswith("test_"):
            try:
                fgt.api.cmdb.diameter_filter.profile.delete(name=df.name)
            except Exception:
                # Ignore if it was already removed or not found
                pass


@pytest.fixture(autouse=True, scope="module")
def _diameter_filter_cleanup():
    # Ensure we start and end with a clean slate so duplicate entries don't fail tests
    cleanup()
    yield
    cleanup()

def test_post_diamenter_filter():
    """Test: Create diameter filter entry"""
    result = fgt.api.cmdb.diameter_filter.profile.post(
        name="test_diameter_filter1",
        comment="Test diameter filter created by pytest"
    )
    assert result is not None
    assert result.http_status == "success"

def test_get_diameter_filter():
    """Test: Create diameter filter entry"""
    result = fgt.api.cmdb.diameter_filter.profile.get()
    assert result is not None
    assert isinstance(result, list)


def test_get_specific_diameter_filter():
    """Test: Get specific diameter filter entry"""
    result = fgt.api.cmdb.diameter_filter.profile.get(name="test_diameter_filter1")
    assert result is not None
    assert result.name == "test_diameter_filter1"
    assert result.comment == "Test diameter filter created by pytest"





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
    print("✓ Pre-cleanup passed (Diameter Filter)")

    test_post_diamenter_filter()
    print("✓ test_post_diameter_filter passed")
    

    test_get_diameter_filter()
    print("✓ test_post_diameter_filter passed")

    test_get_specific_diameter_filter()
    print("✓ test_get_specific_diameter_filter passed")

    cleanup()
    print("✓ final cleanup passed (Diameter Filter)")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
