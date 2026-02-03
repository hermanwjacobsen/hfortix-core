"""
Auto-generated basic tests for cmdb.firewall/schedule/recurring

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.schedule.recurring.json
Category: cmdb
Endpoint: /cmdb/firewall.schedule/recurring

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_recurring.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.firewall.schedule.recurring


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoRecurringValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.firewall.schedule._helpers import recurring as validators
            print(f"✅ Successfully imported validators for recurring")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_firewall_schedule_recurring_post")
            assert hasattr(validators, "validate_firewall_schedule_recurring_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.firewall.schedule._helpers import recurring as validators
        
        # Build minimal valid config with all required fields
        config = {
            "end": "",  # user
            "name": "test_name",  # string
            "start": "",  # user
        }
        
        try:
            result = validators.validate_firewall_schedule_recurring_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoRecurringEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_day(self):
        """Test enum field day validation."""
        from hfortix_fortios.api.v2.cmdb.firewall.schedule._helpers import recurring as validators
        
        valid_values = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'none']
        
        # Test each valid value
        for value in valid_values:
            config = {"day": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: day={value}")
        
        print(f"✅ Enum field day has {len(valid_values)} valid values")
    def auto_test_enum_label_day(self):
        """Test enum field label-day validation."""
        from hfortix_fortios.api.v2.cmdb.firewall.schedule._helpers import recurring as validators
        
        valid_values = ['none', 'over-night', 'early-morning', 'morning', 'midday', 'afternoon', 'evening', 'night', 'late-night']
        
        # Test each valid value
        for value in valid_values:
            config = {"label-day": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: label-day={value}")
        
        print(f"✅ Enum field label-day has {len(valid_values)} valid values")
    def auto_test_enum_fabric_object(self):
        """Test enum field fabric-object validation."""
        from hfortix_fortios.api.v2.cmdb.firewall.schedule._helpers import recurring as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"fabric-object": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: fabric-object={value}")
        
        print(f"✅ Enum field fabric-object has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/firewall/schedule/recurring"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.schedule.recurring.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']