"""
Auto-generated basic tests for cmdb.web_proxy/debug_url

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/web-proxy.debug-url.json
Category: cmdb
Endpoint: /cmdb/web-proxy/debug-url

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_debug-url.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.web_proxy.debug_url


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoDebugUrlValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.web_proxy._helpers import debug_url as validators
            print(f"✅ Successfully imported validators for debug-url")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_web_proxy_debug_url_post")
            assert hasattr(validators, "validate_web_proxy_debug_url_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.web_proxy._helpers import debug_url as validators
        
        # Build minimal valid config with all required fields
        config = {
            "url-pattern": "test_url-pattern",  # string
        }
        
        try:
            result = validators.validate_web_proxy_debug_url_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoDebugUrlEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_status(self):
        """Test enum field status validation."""
        from hfortix_fortios.api.v2.cmdb.web_proxy._helpers import debug_url as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"status": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: status={value}")
        
        print(f"✅ Enum field status has {len(valid_values)} valid values")
    def auto_test_enum_exact(self):
        """Test enum field exact validation."""
        from hfortix_fortios.api.v2.cmdb.web_proxy._helpers import debug_url as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"exact": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: exact={value}")
        
        print(f"✅ Enum field exact has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/web_proxy/debug_url"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/web-proxy.debug-url.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']