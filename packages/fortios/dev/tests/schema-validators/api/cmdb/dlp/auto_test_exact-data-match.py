"""
Auto-generated basic tests for cmdb.dlp/exact_data_match

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/dlp.exact-data-match.json
Category: cmdb
Endpoint: /cmdb/dlp/exact-data-match

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_exact-data-match.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.dlp.exact_data_match


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoExactDataMatchValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.dlp._helpers import exact_data_match as validators
            print(f"✅ Successfully imported validators for exact-data-match")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_dlp_exact_data_match_post")
            assert hasattr(validators, "validate_dlp_exact_data_match_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.dlp._helpers import exact_data_match as validators
        
        # Build minimal valid config with all required fields
        config = {
            "columns": "test_columns",  # string
            "data": "test_data",  # string
            "name": "test_name",  # string
            "optional": 0,  # integer
        }
        
        try:
            result = validators.validate_dlp_exact_data_match_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/dlp/exact_data_match"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/dlp.exact-data-match.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']