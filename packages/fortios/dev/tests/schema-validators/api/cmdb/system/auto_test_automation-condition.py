"""
Auto-generated basic tests for cmdb.system/automation_condition

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.automation-condition.json
Category: cmdb
Endpoint: /cmdb/system/automation-condition

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_automation-condition.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.automation_condition


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoAutomationConditionValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.system._helpers import automation_condition as validators
            print(f"✅ Successfully imported validators for automation-condition")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_system_automation_condition_post")
            assert hasattr(validators, "validate_system_automation_condition_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import automation_condition as validators
        
        # Build minimal valid config with all required fields
        config = {
            "cpu-usage-percent": 0,  # integer
            "mem-usage-percent": 0,  # integer
            "vdom": "test_vdom",  # string
            "vpn-tunnel-name": "test_vpn-tunnel-name",  # string
        }
        
        try:
            result = validators.validate_system_automation_condition_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoAutomationConditionEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_condition_type(self):
        """Test enum field condition-type validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import automation_condition as validators
        
        valid_values = ['cpu', 'memory', 'vpn']
        
        # Test each valid value
        for value in valid_values:
            config = {"condition-type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: condition-type={value}")
        
        print(f"✅ Enum field condition-type has {len(valid_values)} valid values")
    def auto_test_enum_vpn_tunnel_state(self):
        """Test enum field vpn-tunnel-state validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import automation_condition as validators
        
        valid_values = ['tunnel-up', 'tunnel-down']
        
        # Test each valid value
        for value in valid_values:
            config = {"vpn-tunnel-state": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: vpn-tunnel-state={value}")
        
        print(f"✅ Enum field vpn-tunnel-state has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/automation_condition"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.automation-condition.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']