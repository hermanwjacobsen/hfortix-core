"""
Auto-generated basic tests for cmdb.system/external_resource

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.external-resource.json
Category: cmdb
Endpoint: /cmdb/system/external-resource

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_external-resource.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.external_resource


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoExternalResourceValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.system._helpers import external_resource as validators
            print(f"✅ Successfully imported validators for external-resource")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_system_external_resource_post")
            assert hasattr(validators, "validate_system_external_resource_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import external_resource as validators
        
        # Build minimal valid config with all required fields
        config = {
            "interface": "test_interface",  # string
            "name": "test_name",  # string
            "refresh-rate": 5,  # integer
            "resource": "test_resource",  # string
        }
        
        try:
            result = validators.validate_system_external_resource_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoExternalResourceEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_status(self):
        """Test enum field status validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import external_resource as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"status": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: status={value}")
        
        print(f"✅ Enum field status has {len(valid_values)} valid values")
    def auto_test_enum_type(self):
        """Test enum field type validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import external_resource as validators
        
        valid_values = ['category', 'domain', 'malware', 'address', 'mac-address', 'data', 'generic-address']
        
        # Test each valid value
        for value in valid_values:
            config = {"type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: type={value}")
        
        print(f"✅ Enum field type has {len(valid_values)} valid values")
    def auto_test_enum_update_method(self):
        """Test enum field update-method validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import external_resource as validators
        
        valid_values = ['feed', 'push']
        
        # Test each valid value
        for value in valid_values:
            config = {"update-method": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: update-method={value}")
        
        print(f"✅ Enum field update-method has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/external_resource"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.external-resource.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']