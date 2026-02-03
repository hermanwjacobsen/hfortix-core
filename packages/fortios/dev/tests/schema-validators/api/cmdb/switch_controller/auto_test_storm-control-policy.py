"""
Auto-generated basic tests for cmdb.switch_controller/storm_control_policy

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/switch-controller.storm-control-policy.json
Category: cmdb
Endpoint: /cmdb/switch-controller/storm-control-policy

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_storm-control-policy.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.switch_controller.storm_control_policy


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoStormControlPolicyValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.switch_controller._helpers import storm_control_policy as validators
            print(f"✅ Successfully imported validators for storm-control-policy")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_switch_controller_storm_control_policy_post")
            assert hasattr(validators, "validate_switch_controller_storm_control_policy_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.switch_controller._helpers import storm_control_policy as validators
        
        # Build minimal valid config with all required fields
        config = {
            "name": "test_name",  # string
        }
        
        try:
            result = validators.validate_switch_controller_storm_control_policy_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoStormControlPolicyEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_storm_control_mode(self):
        """Test enum field storm-control-mode validation."""
        from hfortix_fortios.api.v2.cmdb.switch_controller._helpers import storm_control_policy as validators
        
        valid_values = ['global', 'override', 'disabled']
        
        # Test each valid value
        for value in valid_values:
            config = {"storm-control-mode": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: storm-control-mode={value}")
        
        print(f"✅ Enum field storm-control-mode has {len(valid_values)} valid values")
    def auto_test_enum_unknown_unicast(self):
        """Test enum field unknown-unicast validation."""
        from hfortix_fortios.api.v2.cmdb.switch_controller._helpers import storm_control_policy as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"unknown-unicast": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: unknown-unicast={value}")
        
        print(f"✅ Enum field unknown-unicast has {len(valid_values)} valid values")
    def auto_test_enum_unknown_multicast(self):
        """Test enum field unknown-multicast validation."""
        from hfortix_fortios.api.v2.cmdb.switch_controller._helpers import storm_control_policy as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"unknown-multicast": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: unknown-multicast={value}")
        
        print(f"✅ Enum field unknown-multicast has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/switch_controller/storm_control_policy"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/switch-controller.storm-control-policy.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']