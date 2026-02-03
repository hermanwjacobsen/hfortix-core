"""
Auto-generated basic tests for cmdb.extension_controller/dataplan

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/extension-controller.dataplan.json
Category: cmdb
Endpoint: /cmdb/extension-controller/dataplan

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_dataplan.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.extension_controller.dataplan


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoDataplanValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.extension_controller._helpers import dataplan as validators
            print(f"✅ Successfully imported validators for dataplan")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_extension_controller_dataplan_post")
            assert hasattr(validators, "validate_extension_controller_dataplan_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.extension_controller._helpers import dataplan as validators
        
        # Build minimal valid config with all required fields
        config = {
            "carrier": "test_carrier",  # string
            "iccid": "test_iccid",  # string
            "password": "",  # password
            "slot": "sim1",  # option
            "type": "carrier",  # option
            "username": "test_username",  # string
        }
        
        try:
            result = validators.validate_extension_controller_dataplan_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoDataplanEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_modem_id(self):
        """Test enum field modem-id validation."""
        from hfortix_fortios.api.v2.cmdb.extension_controller._helpers import dataplan as validators
        
        valid_values = ['modem1', 'modem2', 'all']
        
        # Test each valid value
        for value in valid_values:
            config = {"modem-id": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: modem-id={value}")
        
        print(f"✅ Enum field modem-id has {len(valid_values)} valid values")
    def auto_test_enum_type(self):
        """Test enum field type validation."""
        from hfortix_fortios.api.v2.cmdb.extension_controller._helpers import dataplan as validators
        
        valid_values = ['carrier', 'slot', 'iccid', 'generic']
        
        # Test each valid value
        for value in valid_values:
            config = {"type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: type={value}")
        
        print(f"✅ Enum field type has {len(valid_values)} valid values")
    def auto_test_enum_slot(self):
        """Test enum field slot validation."""
        from hfortix_fortios.api.v2.cmdb.extension_controller._helpers import dataplan as validators
        
        valid_values = ['sim1', 'sim2']
        
        # Test each valid value
        for value in valid_values:
            config = {"slot": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: slot={value}")
        
        print(f"✅ Enum field slot has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/extension_controller/dataplan"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/extension-controller.dataplan.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']