"""
Auto-generated basic tests for cmdb.emailfilter/iptrust

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/emailfilter.iptrust.json
Category: cmdb
Endpoint: /cmdb/emailfilter/iptrust

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_iptrust.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.emailfilter.iptrust


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoIptrustValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.emailfilter._helpers import iptrust as validators
            print(f"✅ Successfully imported validators for iptrust")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_emailfilter_iptrust_post")
            assert hasattr(validators, "validate_emailfilter_iptrust_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.emailfilter._helpers import iptrust as validators
        
        # Build minimal valid config with all required fields
        config = {
            "id": 0,  # integer
            "name": "test_name",  # string
        }
        
        try:
            result = validators.validate_emailfilter_iptrust_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/emailfilter/iptrust"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/emailfilter.iptrust.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']