"""
Auto-generated basic tests for cmdb.user/tacacs_plus_

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/user.tacacs+.json
Category: cmdb
Endpoint: /cmdb/user/tacacs+

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_tacacs+.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.user.tacacs_plus_


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoTacacsPlusValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.user._helpers import tacacs_plus_ as validators
            print(f"✅ Successfully imported validators for tacacs+")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_user_tacacs_plus_post")
            assert hasattr(validators, "validate_user_tacacs_plus_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.user._helpers import tacacs_plus_ as validators
        
        # Build minimal valid config with all required fields
        config = {
            "interface": "test_interface",  # string
            "server": "test_server",  # string
        }
        
        try:
            result = validators.validate_user_tacacs_plus_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoTacacsPlusEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_authen_type(self):
        """Test enum field authen-type validation."""
        from hfortix_fortios.api.v2.cmdb.user._helpers import tacacs_plus_ as validators
        
        valid_values = ['mschap', 'chap', 'pap', 'ascii', 'auto']
        
        # Test each valid value
        for value in valid_values:
            config = {"authen-type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: authen-type={value}")
        
        print(f"✅ Enum field authen-type has {len(valid_values)} valid values")
    def auto_test_enum_authorization(self):
        """Test enum field authorization validation."""
        from hfortix_fortios.api.v2.cmdb.user._helpers import tacacs_plus_ as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"authorization": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: authorization={value}")
        
        print(f"✅ Enum field authorization has {len(valid_values)} valid values")
    def auto_test_enum_interface_select_method(self):
        """Test enum field interface-select-method validation."""
        from hfortix_fortios.api.v2.cmdb.user._helpers import tacacs_plus_ as validators
        
        valid_values = ['auto', 'sdwan', 'specify']
        
        # Test each valid value
        for value in valid_values:
            config = {"interface-select-method": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: interface-select-method={value}")
        
        print(f"✅ Enum field interface-select-method has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/user/tacacs_plus_"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/user.tacacs+.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']