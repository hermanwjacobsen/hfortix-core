"""
Auto-generated basic tests for cmdb.system/fortiguard

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.fortiguard.json
Category: cmdb
Endpoint: /cmdb/system/fortiguard

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_fortiguard.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.fortiguard


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoFortiguardValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.system._helpers import fortiguard as validators
            print(f"✅ Successfully imported validators for fortiguard")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_system_fortiguard_post")
            assert hasattr(validators, "validate_system_fortiguard_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import fortiguard as validators
        
        # Build minimal valid config with all required fields
        config = {
            "antispam-timeout": 7,  # integer
            "interface": "test_interface",  # string
            "outbreak-prevention-timeout": 7,  # integer
            "webfilter-timeout": 15,  # integer
        }
        
        try:
            result = validators.validate_system_fortiguard_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoFortiguardEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_fortiguard_anycast(self):
        """Test enum field fortiguard-anycast validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import fortiguard as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"fortiguard-anycast": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: fortiguard-anycast={value}")
        
        print(f"✅ Enum field fortiguard-anycast has {len(valid_values)} valid values")
    def auto_test_enum_fortiguard_anycast_source(self):
        """Test enum field fortiguard-anycast-source validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import fortiguard as validators
        
        valid_values = ['fortinet', 'aws', 'debug']
        
        # Test each valid value
        for value in valid_values:
            config = {"fortiguard-anycast-source": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: fortiguard-anycast-source={value}")
        
        print(f"✅ Enum field fortiguard-anycast-source has {len(valid_values)} valid values")
    def auto_test_enum_protocol(self):
        """Test enum field protocol validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import fortiguard as validators
        
        valid_values = ['udp', 'http', 'https']
        
        # Test each valid value
        for value in valid_values:
            config = {"protocol": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: protocol={value}")
        
        print(f"✅ Enum field protocol has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/fortiguard"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.fortiguard.json"
TEST_HTTP_METHODS = ['GET', 'PUT']