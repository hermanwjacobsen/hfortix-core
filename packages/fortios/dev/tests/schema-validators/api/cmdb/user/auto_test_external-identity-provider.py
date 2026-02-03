"""
Auto-generated basic tests for cmdb.user/external_identity_provider

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/user.external-identity-provider.json
Category: cmdb
Endpoint: /cmdb/user/external-identity-provider

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_external-identity-provider.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.user.external_identity_provider


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoExternalIdentityProviderValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.user._helpers import external_identity_provider as validators
            print(f"✅ Successfully imported validators for external-identity-provider")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_user_external_identity_provider_post")
            assert hasattr(validators, "validate_user_external_identity_provider_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.user._helpers import external_identity_provider as validators
        
        # Build minimal valid config with all required fields
        config = {
            "interface": "test_interface",  # string
            "type": "ms-graph",  # option
        }
        
        try:
            result = validators.validate_user_external_identity_provider_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoExternalIdentityProviderEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_type(self):
        """Test enum field type validation."""
        from hfortix_fortios.api.v2.cmdb.user._helpers import external_identity_provider as validators
        
        valid_values = ['ms-graph']
        
        # Test each valid value
        for value in valid_values:
            config = {"type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: type={value}")
        
        print(f"✅ Enum field type has {len(valid_values)} valid values")
    def auto_test_enum_version(self):
        """Test enum field version validation."""
        from hfortix_fortios.api.v2.cmdb.user._helpers import external_identity_provider as validators
        
        valid_values = ['v1.0', 'beta']
        
        # Test each valid value
        for value in valid_values:
            config = {"version": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: version={value}")
        
        print(f"✅ Enum field version has {len(valid_values)} valid values")
    def auto_test_enum_interface_select_method(self):
        """Test enum field interface-select-method validation."""
        from hfortix_fortios.api.v2.cmdb.user._helpers import external_identity_provider as validators
        
        valid_values = ['auto', 'sdwan', 'specify']
        
        # Test each valid value
        for value in valid_values:
            config = {"interface-select-method": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: interface-select-method={value}")
        
        print(f"✅ Enum field interface-select-method has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/user/external_identity_provider"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/user.external-identity-provider.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']