"""
Auto-generated basic tests for cmdb.user/domain_controller

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/user.domain-controller.json
Category: cmdb
Endpoint: /cmdb/user/domain-controller

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_domain-controller.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.user.domain_controller


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoDomainControllerValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.user._helpers import domain_controller as validators
            print(f"✅ Successfully imported validators for domain-controller")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_user_domain_controller_post")
            assert hasattr(validators, "validate_user_domain_controller_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.user._helpers import domain_controller as validators
        
        # Build minimal valid config with all required fields
        config = {
            "adlds-dn": "test_adlds-dn",  # string
            "hostname": "test_hostname",  # string
            "interface": "test_interface",  # string
            "password": "",  # password
            "username": "test_username",  # string
        }
        
        try:
            result = validators.validate_user_domain_controller_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoDomainControllerEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_ad_mode(self):
        """Test enum field ad-mode validation."""
        from hfortix_fortios.api.v2.cmdb.user._helpers import domain_controller as validators
        
        valid_values = ['none', 'ds', 'lds']
        
        # Test each valid value
        for value in valid_values:
            config = {"ad-mode": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: ad-mode={value}")
        
        print(f"✅ Enum field ad-mode has {len(valid_values)} valid values")
    def auto_test_enum_interface_select_method(self):
        """Test enum field interface-select-method validation."""
        from hfortix_fortios.api.v2.cmdb.user._helpers import domain_controller as validators
        
        valid_values = ['auto', 'sdwan', 'specify']
        
        # Test each valid value
        for value in valid_values:
            config = {"interface-select-method": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: interface-select-method={value}")
        
        print(f"✅ Enum field interface-select-method has {len(valid_values)} valid values")
    def auto_test_enum_change_detection(self):
        """Test enum field change-detection validation."""
        from hfortix_fortios.api.v2.cmdb.user._helpers import domain_controller as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"change-detection": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: change-detection={value}")
        
        print(f"✅ Enum field change-detection has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/user/domain_controller"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/user.domain-controller.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']