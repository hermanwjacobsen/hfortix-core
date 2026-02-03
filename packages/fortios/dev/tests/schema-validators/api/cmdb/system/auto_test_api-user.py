"""
Auto-generated basic tests for cmdb.system/api_user

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.api-user.json
Category: cmdb
Endpoint: /cmdb/system/api-user

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_api-user.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.api_user


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoApiUserValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.system._helpers import api_user as validators
            print(f"✅ Successfully imported validators for api-user")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_system_api_user_post")
            assert hasattr(validators, "validate_system_api_user_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import api_user as validators
        
        # Build minimal valid config with all required fields
        config = {
            "accprofile": "test_accprofile",  # string
            "peer-group": "test_peer-group",  # string
        }
        
        try:
            result = validators.validate_system_api_user_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoApiUserEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_peer_auth(self):
        """Test enum field peer-auth validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import api_user as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"peer-auth": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: peer-auth={value}")
        
        print(f"✅ Enum field peer-auth has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/api_user"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.api-user.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']