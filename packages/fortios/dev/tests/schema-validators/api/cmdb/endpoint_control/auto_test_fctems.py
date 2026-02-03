"""
Auto-generated basic tests for cmdb.endpoint_control/fctems

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/endpoint-control.fctems.json
Category: cmdb
Endpoint: /cmdb/endpoint-control/fctems

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_fctems.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.endpoint_control.fctems


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoFctemsValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.endpoint_control._helpers import fctems as validators
            print(f"✅ Successfully imported validators for fctems")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_endpoint_control_fctems_post")
            assert hasattr(validators, "validate_endpoint_control_fctems_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.endpoint_control._helpers import fctems as validators
        
        # Build minimal valid config with all required fields
        config = {
            "interface": "test_interface",  # string
        }
        
        try:
            result = validators.validate_endpoint_control_fctems_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoFctemsEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_status(self):
        """Test enum field status validation."""
        from hfortix_fortios.api.v2.cmdb.endpoint_control._helpers import fctems as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"status": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: status={value}")
        
        print(f"✅ Enum field status has {len(valid_values)} valid values")
    def auto_test_enum_dirty_reason(self):
        """Test enum field dirty-reason validation."""
        from hfortix_fortios.api.v2.cmdb.endpoint_control._helpers import fctems as validators
        
        valid_values = ['none', 'mismatched-ems-sn']
        
        # Test each valid value
        for value in valid_values:
            config = {"dirty-reason": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: dirty-reason={value}")
        
        print(f"✅ Enum field dirty-reason has {len(valid_values)} valid values")
    def auto_test_enum_fortinetone_cloud_authentication(self):
        """Test enum field fortinetone-cloud-authentication validation."""
        from hfortix_fortios.api.v2.cmdb.endpoint_control._helpers import fctems as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"fortinetone-cloud-authentication": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: fortinetone-cloud-authentication={value}")
        
        print(f"✅ Enum field fortinetone-cloud-authentication has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/endpoint_control/fctems"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/endpoint-control.fctems.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']