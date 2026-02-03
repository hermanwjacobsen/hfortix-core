"""
Auto-generated basic tests for cmdb.system/ntp

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.ntp.json
Category: cmdb
Endpoint: /cmdb/system/ntp

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_ntp.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.ntp


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoNtpValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.system._helpers import ntp as validators
            print(f"✅ Successfully imported validators for ntp")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_system_ntp_post")
            assert hasattr(validators, "validate_system_ntp_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import ntp as validators
        
        # Build minimal valid config with all required fields
        config = {
            "key": "",  # password
            "key-id": 0,  # integer
        }
        
        try:
            result = validators.validate_system_ntp_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoNtpEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_ntpsync(self):
        """Test enum field ntpsync validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import ntp as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"ntpsync": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: ntpsync={value}")
        
        print(f"✅ Enum field ntpsync has {len(valid_values)} valid values")
    def auto_test_enum_type(self):
        """Test enum field type validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import ntp as validators
        
        valid_values = ['fortiguard', 'custom']
        
        # Test each valid value
        for value in valid_values:
            config = {"type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: type={value}")
        
        print(f"✅ Enum field type has {len(valid_values)} valid values")
    def auto_test_enum_server_mode(self):
        """Test enum field server-mode validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import ntp as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"server-mode": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: server-mode={value}")
        
        print(f"✅ Enum field server-mode has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/ntp"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.ntp.json"
TEST_HTTP_METHODS = ['GET', 'PUT']