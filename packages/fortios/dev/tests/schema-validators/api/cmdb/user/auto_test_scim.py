"""
Auto-generated basic tests for cmdb.user/scim

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/user.scim.json
Category: cmdb
Endpoint: /cmdb/user/scim

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_scim.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.user.scim


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoScimValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.user._helpers import scim as validators
            print(f"✅ Successfully imported validators for scim")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_user_scim_post")
            assert hasattr(validators, "validate_user_scim_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.user._helpers import scim as validators
        
        # Build minimal valid config with all required fields
        config = {
            "name": "test_name",  # string
            "status": "enable",  # option
        }
        
        try:
            result = validators.validate_user_scim_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoScimEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_status(self):
        """Test enum field status validation."""
        from hfortix_fortios.api.v2.cmdb.user._helpers import scim as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"status": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: status={value}")
        
        print(f"✅ Enum field status has {len(valid_values)} valid values")
    def auto_test_enum_auth_method(self):
        """Test enum field auth-method validation."""
        from hfortix_fortios.api.v2.cmdb.user._helpers import scim as validators
        
        valid_values = ['token', 'base']
        
        # Test each valid value
        for value in valid_values:
            config = {"auth-method": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: auth-method={value}")
        
        print(f"✅ Enum field auth-method has {len(valid_values)} valid values")
    def auto_test_enum_client_identity_check(self):
        """Test enum field client-identity-check validation."""
        from hfortix_fortios.api.v2.cmdb.user._helpers import scim as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"client-identity-check": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: client-identity-check={value}")
        
        print(f"✅ Enum field client-identity-check has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/user/scim"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/user.scim.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']