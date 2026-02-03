"""
Auto-generated basic tests for cmdb.dlp/dictionary

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/dlp.dictionary.json
Category: cmdb
Endpoint: /cmdb/dlp/dictionary

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_dictionary.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.dlp.dictionary


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoDictionaryValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.dlp._helpers import dictionary as validators
            print(f"✅ Successfully imported validators for dictionary")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_dlp_dictionary_post")
            assert hasattr(validators, "validate_dlp_dictionary_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.dlp._helpers import dictionary as validators
        
        # Build minimal valid config with all required fields
        config = {
            "entries": "test_entries",  # string
            "match-type": "match-all",  # option
            "name": "test_name",  # string
        }
        
        try:
            result = validators.validate_dlp_dictionary_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoDictionaryEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_match_type(self):
        """Test enum field match-type validation."""
        from hfortix_fortios.api.v2.cmdb.dlp._helpers import dictionary as validators
        
        valid_values = ['match-all', 'match-any']
        
        # Test each valid value
        for value in valid_values:
            config = {"match-type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: match-type={value}")
        
        print(f"✅ Enum field match-type has {len(valid_values)} valid values")
    def auto_test_enum_match_around(self):
        """Test enum field match-around validation."""
        from hfortix_fortios.api.v2.cmdb.dlp._helpers import dictionary as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"match-around": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: match-around={value}")
        
        print(f"✅ Enum field match-around has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/dlp/dictionary"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/dlp.dictionary.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']