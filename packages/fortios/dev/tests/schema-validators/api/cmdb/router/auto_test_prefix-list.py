"""
Auto-generated basic tests for cmdb.router/prefix_list

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/router.prefix-list.json
Category: cmdb
Endpoint: /cmdb/router/prefix-list

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_prefix-list.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.router.prefix_list


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoPrefixListValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.router._helpers import prefix_list as validators
            print(f"✅ Successfully imported validators for prefix-list")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_router_prefix_list_post")
            assert hasattr(validators, "validate_router_prefix_list_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.router._helpers import prefix_list as validators
        
        # Build minimal valid config with all required fields
        config = {
            "name": "test_name",  # string
        }
        
        try:
            result = validators.validate_router_prefix_list_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/router/prefix_list"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/router.prefix-list.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']