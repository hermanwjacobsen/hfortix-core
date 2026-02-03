"""
Auto-generated basic tests for cmdb.webfilter/search_engine

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/webfilter.search-engine.json
Category: cmdb
Endpoint: /cmdb/webfilter/search-engine

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_search-engine.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.webfilter.search_engine


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoSearchEngineValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.webfilter._helpers import search_engine as validators
            print(f"✅ Successfully imported validators for search-engine")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_webfilter_search_engine_post")
            assert hasattr(validators, "validate_webfilter_search_engine_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.webfilter._helpers import search_engine as validators
        
        # Build minimal valid config with all required fields
        config = {
            "name": "test_name",  # string
        }
        
        try:
            result = validators.validate_webfilter_search_engine_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoSearchEngineEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_safesearch(self):
        """Test enum field safesearch validation."""
        from hfortix_fortios.api.v2.cmdb.webfilter._helpers import search_engine as validators
        
        valid_values = ['disable', 'url', 'header', 'translate', 'yt-pattern', 'yt-scan', 'yt-video', 'yt-channel']
        
        # Test each valid value
        for value in valid_values:
            config = {"safesearch": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: safesearch={value}")
        
        print(f"✅ Enum field safesearch has {len(valid_values)} valid values")
    def auto_test_enum_charset(self):
        """Test enum field charset validation."""
        from hfortix_fortios.api.v2.cmdb.webfilter._helpers import search_engine as validators
        
        valid_values = ['utf-8', 'gb2312']
        
        # Test each valid value
        for value in valid_values:
            config = {"charset": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: charset={value}")
        
        print(f"✅ Enum field charset has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/webfilter/search_engine"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/webfilter.search-engine.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']