"""
Tests for hfortix_core deprecation utilities.

Tests warn_deprecated_field and check_deprecated_fields functions.
"""

import warnings
from hfortix_core.deprecation import (
    warn_deprecated_field,
    check_deprecated_fields,
    DeprecationWarning,
)


# ============================================================================
# warn_deprecated_field tests
# ============================================================================

def test_warn_deprecated_field_basic():
    """Test basic deprecation warning."""
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        warn_deprecated_field("old_field", "firewall/address")
        
        assert len(w) == 1
        assert issubclass(w[0].category, DeprecationWarning)
        assert "old_field" in str(w[0].message)
        assert "firewall/address" in str(w[0].message)
        assert "deprecated" in str(w[0].message).lower()
    print("✅ warn_deprecated_field - basic")


def test_warn_deprecated_field_with_reason():
    """Test deprecation warning with reason."""
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        warn_deprecated_field(
            "old_field",
            "firewall/address",
            reason="No longer supported in FortiOS 7.0"
        )
        
        assert len(w) == 1
        assert "No longer supported in FortiOS 7.0" in str(w[0].message)
    print("✅ warn_deprecated_field - with reason")


def test_warn_deprecated_field_with_alternative():
    """Test deprecation warning with alternative field."""
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        warn_deprecated_field(
            "old_field",
            "firewall/address",
            alternative="new_field"
        )
        
        assert len(w) == 1
        assert "new_field" in str(w[0].message)
        assert "instead" in str(w[0].message).lower()
    print("✅ warn_deprecated_field - with alternative")


def test_warn_deprecated_field_with_removal_version():
    """Test deprecation warning with removal version."""
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        warn_deprecated_field(
            "old_field",
            "firewall/address",
            removal_version="8.0"
        )
        
        assert len(w) == 1
        assert "8.0" in str(w[0].message)
        assert "removed" in str(w[0].message).lower()
    print("✅ warn_deprecated_field - with removal version")


def test_warn_deprecated_field_full():
    """Test deprecation warning with all parameters."""
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        warn_deprecated_field(
            "sslvpn-enable",
            "vpn.ssl/settings",
            reason="SSLVPN has been deprecated",
            alternative="ztna-status",
            removal_version="7.6"
        )
        
        assert len(w) == 1
        msg = str(w[0].message)
        assert "sslvpn-enable" in msg
        assert "vpn.ssl/settings" in msg
        assert "SSLVPN has been deprecated" in msg
        assert "ztna-status" in msg
        assert "7.6" in msg
    print("✅ warn_deprecated_field - full")


# ============================================================================
# check_deprecated_fields tests
# ============================================================================

def test_check_deprecated_fields_no_deprecated():
    """Test checking payload with no deprecated fields."""
    payload = {"name": "test", "value": 123}
    deprecated_fields = {
        "old_field": {"reason": "No longer used"}
    }
    
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        check_deprecated_fields(payload, deprecated_fields, "test/endpoint")
        
        # No warnings should be issued
        assert len(w) == 0
    print("✅ check_deprecated_fields - no deprecated")


def test_check_deprecated_fields_with_deprecated():
    """Test checking payload with deprecated field."""
    payload = {"name": "test", "old_field": "value"}
    deprecated_fields = {
        "old_field": {"reason": "No longer used"}
    }
    
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        check_deprecated_fields(payload, deprecated_fields, "test/endpoint")
        
        assert len(w) == 1
        assert "old_field" in str(w[0].message)
    print("✅ check_deprecated_fields - with deprecated")


def test_check_deprecated_fields_multiple():
    """Test checking payload with multiple deprecated fields."""
    payload = {
        "name": "test",
        "old_field1": "value1",
        "old_field2": "value2",
        "new_field": "value3"
    }
    deprecated_fields = {
        "old_field1": {"reason": "Use new_field1 instead"},
        "old_field2": {"reason": "Use new_field2 instead", "alternative": "new_field2"},
        "unused": {"reason": "Not in payload"}
    }
    
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        check_deprecated_fields(payload, deprecated_fields, "test/endpoint")
        
        # Should get 2 warnings (old_field1 and old_field2)
        assert len(w) == 2
        messages = [str(warning.message) for warning in w]
        assert any("old_field1" in msg for msg in messages)
        assert any("old_field2" in msg for msg in messages)
    print("✅ check_deprecated_fields - multiple")


def test_check_deprecated_fields_with_all_info():
    """Test checking with full deprecation info."""
    payload = {"deprecated_setting": "value"}
    deprecated_fields = {
        "deprecated_setting": {
            "reason": "Feature removed",
            "alternative": "new_setting",
            "removal_version": "8.0"
        }
    }
    
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        check_deprecated_fields(payload, deprecated_fields, "system/settings")
        
        assert len(w) == 1
        msg = str(w[0].message)
        assert "deprecated_setting" in msg
        assert "system/settings" in msg
        # These parts are constructed in warn_deprecated_field
    print("✅ check_deprecated_fields - with all info")


def test_check_deprecated_fields_empty_payload():
    """Test checking empty payload."""
    payload = {}
    deprecated_fields = {"old": {"reason": "test"}}
    
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        check_deprecated_fields(payload, deprecated_fields, "test/endpoint")
        
        assert len(w) == 0
    print("✅ check_deprecated_fields - empty payload")


def test_check_deprecated_fields_empty_deprecated():
    """Test checking with no deprecated fields defined."""
    payload = {"name": "test", "value": 123}
    deprecated_fields = {}
    
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        check_deprecated_fields(payload, deprecated_fields, "test/endpoint")
        
        assert len(w) == 0
    print("✅ check_deprecated_fields - empty deprecated")


def test_deprecation_warning_is_user_warning():
    """Test that DeprecationWarning is a UserWarning subclass."""
    assert issubclass(DeprecationWarning, UserWarning)
    print("✅ DeprecationWarning - is UserWarning subclass")


def run_all_tests():
    """Run all deprecation tests."""
    print("\n" + "=" * 60)
    print("DEPRECATION TESTS")
    print("=" * 60 + "\n")

    # warn_deprecated_field tests
    test_warn_deprecated_field_basic()
    test_warn_deprecated_field_with_reason()
    test_warn_deprecated_field_with_alternative()
    test_warn_deprecated_field_with_removal_version()
    test_warn_deprecated_field_full()

    # check_deprecated_fields tests
    test_check_deprecated_fields_no_deprecated()
    test_check_deprecated_fields_with_deprecated()
    test_check_deprecated_fields_multiple()
    test_check_deprecated_fields_with_all_info()
    test_check_deprecated_fields_empty_payload()
    test_check_deprecated_fields_empty_deprecated()
    
    # DeprecationWarning class test
    test_deprecation_warning_is_user_warning()

    print("\n" + "=" * 60)
    print("ALL DEPRECATION TESTS PASSED!")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    run_all_tests()
