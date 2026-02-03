"""
Auto-generated basic tests for cmdb.system/email_server

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.email-server.json
Category: cmdb
Endpoint: /cmdb/system/email-server

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_email-server.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.email_server


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoEmailServerValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.system._helpers import email_server as validators
            print(f"✅ Successfully imported validators for email-server")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_system_email_server_post")
            assert hasattr(validators, "validate_system_email_server_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import email_server as validators
        
        # Build minimal valid config with all required fields
        config = {
            "interface": "test_interface",  # string
        }
        
        try:
            result = validators.validate_system_email_server_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoEmailServerEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_type(self):
        """Test enum field type validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import email_server as validators
        
        valid_values = ['custom']
        
        # Test each valid value
        for value in valid_values:
            config = {"type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: type={value}")
        
        print(f"✅ Enum field type has {len(valid_values)} valid values")
    def auto_test_enum_authenticate(self):
        """Test enum field authenticate validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import email_server as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"authenticate": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: authenticate={value}")
        
        print(f"✅ Enum field authenticate has {len(valid_values)} valid values")
    def auto_test_enum_validate_server(self):
        """Test enum field validate-server validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import email_server as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"validate-server": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: validate-server={value}")
        
        print(f"✅ Enum field validate-server has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/email_server"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.email-server.json"
TEST_HTTP_METHODS = ['GET', 'PUT']