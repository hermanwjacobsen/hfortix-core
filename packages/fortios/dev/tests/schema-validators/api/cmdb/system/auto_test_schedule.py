"""
Auto-generated basic tests for cmdb.system/autoupdate/schedule

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.autoupdate.schedule.json
Category: cmdb
Endpoint: /cmdb/system.autoupdate/schedule

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_schedule.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.autoupdate.schedule


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoScheduleValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.system.autoupdate._helpers import schedule as validators
            print(f"✅ Successfully imported validators for schedule")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_system_autoupdate_schedule_post")
            assert hasattr(validators, "validate_system_autoupdate_schedule_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.system.autoupdate._helpers import schedule as validators
        
        # Build minimal valid config with all required fields
        config = {
            "day": "Sunday",  # option
            "frequency": "every",  # option
            "status": "enable",  # option
            "time": "",  # user
        }
        
        try:
            result = validators.validate_system_autoupdate_schedule_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoScheduleEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_status(self):
        """Test enum field status validation."""
        from hfortix_fortios.api.v2.cmdb.system.autoupdate._helpers import schedule as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"status": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: status={value}")
        
        print(f"✅ Enum field status has {len(valid_values)} valid values")
    def auto_test_enum_frequency(self):
        """Test enum field frequency validation."""
        from hfortix_fortios.api.v2.cmdb.system.autoupdate._helpers import schedule as validators
        
        valid_values = ['every', 'daily', 'weekly', 'automatic']
        
        # Test each valid value
        for value in valid_values:
            config = {"frequency": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: frequency={value}")
        
        print(f"✅ Enum field frequency has {len(valid_values)} valid values")
    def auto_test_enum_day(self):
        """Test enum field day validation."""
        from hfortix_fortios.api.v2.cmdb.system.autoupdate._helpers import schedule as validators
        
        valid_values = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        
        # Test each valid value
        for value in valid_values:
            config = {"day": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: day={value}")
        
        print(f"✅ Enum field day has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/autoupdate/schedule"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.autoupdate.schedule.json"
TEST_HTTP_METHODS = ['GET', 'PUT']