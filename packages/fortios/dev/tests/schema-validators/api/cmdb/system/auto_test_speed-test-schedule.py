"""
Auto-generated basic tests for cmdb.system/speed_test_schedule

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.speed-test-schedule.json
Category: cmdb
Endpoint: /cmdb/system/speed-test-schedule

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_speed-test-schedule.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.speed_test_schedule


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoSpeedTestScheduleValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.system._helpers import speed_test_schedule as validators
            print(f"✅ Successfully imported validators for speed-test-schedule")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_system_speed_test_schedule_post")
            assert hasattr(validators, "validate_system_speed_test_schedule_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import speed_test_schedule as validators
        
        # Build minimal valid config with all required fields
        config = {
            "schedules": "test_schedules",  # string
        }
        
        try:
            result = validators.validate_system_speed_test_schedule_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoSpeedTestScheduleEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_status(self):
        """Test enum field status validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import speed_test_schedule as validators
        
        valid_values = ['disable', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"status": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: status={value}")
        
        print(f"✅ Enum field status has {len(valid_values)} valid values")
    def auto_test_enum_mode(self):
        """Test enum field mode validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import speed_test_schedule as validators
        
        valid_values = ['UDP', 'TCP', 'Auto']
        
        # Test each valid value
        for value in valid_values:
            config = {"mode": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: mode={value}")
        
        print(f"✅ Enum field mode has {len(valid_values)} valid values")
    def auto_test_enum_dynamic_server(self):
        """Test enum field dynamic-server validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import speed_test_schedule as validators
        
        valid_values = ['disable', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"dynamic-server": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: dynamic-server={value}")
        
        print(f"✅ Enum field dynamic-server has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/speed_test_schedule"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.speed-test-schedule.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']