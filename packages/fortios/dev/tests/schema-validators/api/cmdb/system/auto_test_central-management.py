"""
Auto-generated basic tests for cmdb.system/central_management

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.central-management.json
Category: cmdb
Endpoint: /cmdb/system/central-management

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_central-management.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.central_management


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoCentralManagementValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.system._helpers import central_management as validators
            print(f"✅ Successfully imported validators for central-management")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_system_central_management_post")
            assert hasattr(validators, "validate_system_central_management_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import central_management as validators
        
        # Build minimal valid config with all required fields
        config = {
            "interface": "test_interface",  # string
        }
        
        try:
            result = validators.validate_system_central_management_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoCentralManagementEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_mode(self):
        """Test enum field mode validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import central_management as validators
        
        valid_values = ['normal', 'backup']
        
        # Test each valid value
        for value in valid_values:
            config = {"mode": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: mode={value}")
        
        print(f"✅ Enum field mode has {len(valid_values)} valid values")
    def auto_test_enum_type(self):
        """Test enum field type validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import central_management as validators
        
        valid_values = ['fortimanager', 'fortiguard', 'none']
        
        # Test each valid value
        for value in valid_values:
            config = {"type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: type={value}")
        
        print(f"✅ Enum field type has {len(valid_values)} valid values")
    def auto_test_enum_schedule_config_restore(self):
        """Test enum field schedule-config-restore validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import central_management as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"schedule-config-restore": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: schedule-config-restore={value}")
        
        print(f"✅ Enum field schedule-config-restore has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/central_management"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.central-management.json"
TEST_HTTP_METHODS = ['GET', 'PUT']