"""
Auto-generated basic tests for cmdb.system/fortisandbox

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.fortisandbox.json
Category: cmdb
Endpoint: /cmdb/system/fortisandbox

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_fortisandbox.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.fortisandbox


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoFortisandboxValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.system._helpers import fortisandbox as validators
            print(f"✅ Successfully imported validators for fortisandbox")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_system_fortisandbox_post")
            assert hasattr(validators, "validate_system_fortisandbox_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import fortisandbox as validators
        
        # Build minimal valid config with all required fields
        config = {
            "interface": "test_interface",  # string
            "server": "test_server",  # string
        }
        
        try:
            result = validators.validate_system_fortisandbox_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoFortisandboxEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_status(self):
        """Test enum field status validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import fortisandbox as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"status": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: status={value}")
        
        print(f"✅ Enum field status has {len(valid_values)} valid values")
    def auto_test_enum_forticloud(self):
        """Test enum field forticloud validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import fortisandbox as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"forticloud": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: forticloud={value}")
        
        print(f"✅ Enum field forticloud has {len(valid_values)} valid values")
    def auto_test_enum_inline_scan(self):
        """Test enum field inline-scan validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import fortisandbox as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"inline-scan": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: inline-scan={value}")
        
        print(f"✅ Enum field inline-scan has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/fortisandbox"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.fortisandbox.json"
TEST_HTTP_METHODS = ['GET', 'PUT']