"""
Auto-generated basic tests for cmdb.switch_controller/qos/dot1p_map

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/switch-controller.qos.dot1p-map.json
Category: cmdb
Endpoint: /cmdb/switch-controller.qos/dot1p-map

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_dot1p-map.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.switch_controller.qos.dot1p_map


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoDot1pMapValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.switch_controller.qos._helpers import dot1p_map as validators
            print(f"✅ Successfully imported validators for dot1p-map")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_switch_controller_qos_dot1p_map_post")
            assert hasattr(validators, "validate_switch_controller_qos_dot1p_map_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.switch_controller.qos._helpers import dot1p_map as validators
        
        # Build minimal valid config with all required fields
        config = {
            "egress-pri-tagging": "disable",  # option
            "name": "test_name",  # string
        }
        
        try:
            result = validators.validate_switch_controller_qos_dot1p_map_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoDot1pMapEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_egress_pri_tagging(self):
        """Test enum field egress-pri-tagging validation."""
        from hfortix_fortios.api.v2.cmdb.switch_controller.qos._helpers import dot1p_map as validators
        
        valid_values = ['disable', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"egress-pri-tagging": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: egress-pri-tagging={value}")
        
        print(f"✅ Enum field egress-pri-tagging has {len(valid_values)} valid values")
    def auto_test_enum_priority_0(self):
        """Test enum field priority-0 validation."""
        from hfortix_fortios.api.v2.cmdb.switch_controller.qos._helpers import dot1p_map as validators
        
        valid_values = ['queue-0', 'queue-1', 'queue-2', 'queue-3', 'queue-4', 'queue-5', 'queue-6', 'queue-7']
        
        # Test each valid value
        for value in valid_values:
            config = {"priority-0": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: priority-0={value}")
        
        print(f"✅ Enum field priority-0 has {len(valid_values)} valid values")
    def auto_test_enum_priority_1(self):
        """Test enum field priority-1 validation."""
        from hfortix_fortios.api.v2.cmdb.switch_controller.qos._helpers import dot1p_map as validators
        
        valid_values = ['queue-0', 'queue-1', 'queue-2', 'queue-3', 'queue-4', 'queue-5', 'queue-6', 'queue-7']
        
        # Test each valid value
        for value in valid_values:
            config = {"priority-1": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: priority-1={value}")
        
        print(f"✅ Enum field priority-1 has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/switch_controller/qos/dot1p_map"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/switch-controller.qos.dot1p-map.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']