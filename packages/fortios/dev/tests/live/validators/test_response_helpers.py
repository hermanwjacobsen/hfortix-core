"""
Tests for hfortix_fortios response helpers.

Tests get_name, get_mkey, get_results, and is_success functions.
"""

from hfortix_fortios._helpers.response import (
    get_name,
    get_mkey,
    get_results,
    is_success,
)


# ============================================================================
# get_name tests
# ============================================================================

def test_get_name_with_mkey():
    """Test getting name from response with mkey."""
    response = {"status": "success", "mkey": "test-object"}
    result = get_name(response)
    assert result == "test-object"
    print("✅ get_name - with mkey")


def test_get_name_without_mkey():
    """Test getting name from response without mkey."""
    response = {"status": "success", "results": []}
    result = get_name(response)
    assert result is None
    print("✅ get_name - without mkey")


def test_get_name_non_dict():
    """Test getting name from non-dict response."""
    result = get_name("not a dict")
    assert result is None
    print("✅ get_name - non-dict")


def test_get_name_none():
    """Test getting name from None."""
    result = get_name(None)
    assert result is None
    print("✅ get_name - None")


def test_get_name_integer_mkey():
    """Test getting name when mkey is integer."""
    response = {"status": "success", "mkey": 123}
    result = get_name(response)
    assert result == 123
    print("✅ get_name - integer mkey")


# ============================================================================
# get_mkey tests (alias for get_name)
# ============================================================================

def test_get_mkey_with_mkey():
    """Test get_mkey as alias for get_name."""
    response = {"status": "success", "mkey": "test-object"}
    result = get_mkey(response)
    assert result == "test-object"
    print("✅ get_mkey - basic")


def test_get_mkey_without_mkey():
    """Test get_mkey without mkey."""
    response = {"status": "success"}
    result = get_mkey(response)
    assert result is None
    print("✅ get_mkey - without mkey")


# ============================================================================
# get_results tests
# ============================================================================

def test_get_results_list():
    """Test getting list results."""
    response = {
        "status": "success",
        "results": [
            {"name": "obj1", "status": "enable"},
            {"name": "obj2", "status": "disable"}
        ]
    }
    result = get_results(response)
    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0]["name"] == "obj1"
    print("✅ get_results - list results")


def test_get_results_dict():
    """Test getting dict results."""
    response = {
        "status": "success",
        "results": {"name": "single-object", "status": "enable"}
    }
    result = get_results(response)
    assert isinstance(result, dict)
    assert result["name"] == "single-object"
    print("✅ get_results - dict results")


def test_get_results_empty_list():
    """Test getting empty list results."""
    response = {"status": "success", "results": []}
    result = get_results(response)
    assert result == []
    print("✅ get_results - empty list")


def test_get_results_no_results_key():
    """Test response without results key."""
    response = {"status": "success", "mkey": "test"}
    result = get_results(response)
    assert result is None
    print("✅ get_results - no results key")


def test_get_results_non_dict():
    """Test getting results from non-dict."""
    result = get_results("not a dict")
    assert result is None
    print("✅ get_results - non-dict")


def test_get_results_none():
    """Test getting results from None."""
    result = get_results(None)
    assert result is None
    print("✅ get_results - None")


def test_get_results_nested():
    """Test getting nested results."""
    response = {
        "status": "success",
        "results": {
            "name": "test",
            "members": [
                {"name": "member1"},
                {"name": "member2"}
            ]
        }
    }
    result = get_results(response)
    assert isinstance(result, dict)
    assert result["name"] == "test"
    assert len(result["members"]) == 2
    print("✅ get_results - nested structure")


# ============================================================================
# is_success tests
# ============================================================================

def test_is_success_true():
    """Test success response."""
    response = {"status": "success", "results": []}
    result = is_success(response)
    assert result is True
    print("✅ is_success - success")


def test_is_success_false_error():
    """Test error response."""
    response = {"status": "error", "error": "Object not found"}
    result = is_success(response)
    assert result is False
    print("✅ is_success - error")


def test_is_success_false_fail():
    """Test fail response."""
    response = {"status": "fail", "message": "Invalid parameter"}
    result = is_success(response)
    assert result is False
    print("✅ is_success - fail")


def test_is_success_no_status():
    """Test response without status."""
    response = {"results": []}
    result = is_success(response)
    assert result is False
    print("✅ is_success - no status")


def test_is_success_non_dict():
    """Test non-dict response."""
    result = is_success("not a dict")
    assert result is False
    print("✅ is_success - non-dict")


def test_is_success_none():
    """Test None response."""
    result = is_success(None)
    assert result is False
    print("✅ is_success - None")


def test_is_success_http_status():
    """Test response with HTTP status code."""
    response = {"status": "success", "http_status": 200}
    result = is_success(response)
    assert result is True
    print("✅ is_success - with http_status")


def test_is_success_real_create_response():
    """Test with realistic create response."""
    response = {
        "status": "success",
        "http_status": 200,
        "vdom": "root",
        "mkey": "test-address",
        "revision_changed": True
    }
    result = is_success(response)
    assert result is True
    print("✅ is_success - realistic create response")


def test_is_success_real_error_response():
    """Test with realistic error response."""
    response = {
        "status": "error",
        "http_status": 500,
        "vdom": "root",
        "error": -651,
        "cli_error": "entry_not_found"
    }
    result = is_success(response)
    assert result is False
    print("✅ is_success - realistic error response")


def run_all_tests():
    """Run all response helper tests."""
    print("\n" + "=" * 60)
    print("RESPONSE HELPER TESTS")
    print("=" * 60 + "\n")

    # get_name tests
    test_get_name_with_mkey()
    test_get_name_without_mkey()
    test_get_name_non_dict()
    test_get_name_none()
    test_get_name_integer_mkey()

    # get_mkey tests
    test_get_mkey_with_mkey()
    test_get_mkey_without_mkey()

    # get_results tests
    test_get_results_list()
    test_get_results_dict()
    test_get_results_empty_list()
    test_get_results_no_results_key()
    test_get_results_non_dict()
    test_get_results_none()
    test_get_results_nested()

    # is_success tests
    test_is_success_true()
    test_is_success_false_error()
    test_is_success_false_fail()
    test_is_success_no_status()
    test_is_success_non_dict()
    test_is_success_none()
    test_is_success_http_status()
    test_is_success_real_create_response()
    test_is_success_real_error_response()

    print("\n" + "=" * 60)
    print("ALL RESPONSE HELPER TESTS PASSED!")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    run_all_tests()
