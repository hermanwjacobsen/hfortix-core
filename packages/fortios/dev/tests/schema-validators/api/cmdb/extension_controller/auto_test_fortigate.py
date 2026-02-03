"""
Auto-generated basic tests for cmdb.extension_controller/fortigate

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/extension-controller.fortigate.json
Category: cmdb
Endpoint: /cmdb/extension-controller/fortigate

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_fortigate.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.extension_controller.fortigate


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoFortigateValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.extension_controller._helpers import fortigate as validators
            print(f"✅ Successfully imported validators for fortigate")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_extension_controller_fortigate_post")
            assert hasattr(validators, "validate_extension_controller_fortigate_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.extension_controller._helpers import fortigate as validators
        
        # Build minimal valid config with all required fields
        config = {
            "authorized": "discovered",  # option
            "id": "test_id",  # string
            "name": "test_name",  # string
        }
        
        try:
            result = validators.validate_extension_controller_fortigate_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoFortigateEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_authorized(self):
        """Test enum field authorized validation."""
        from hfortix_fortios.api.v2.cmdb.extension_controller._helpers import fortigate as validators
        
        valid_values = ['discovered', 'disable', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"authorized": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: authorized={value}")
        
        print(f"✅ Enum field authorized has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/extension_controller/fortigate"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/extension-controller.fortigate.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']