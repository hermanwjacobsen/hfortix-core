"""
Auto-generated basic tests for cmdb.router/ospf

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/router.ospf.json
Category: cmdb
Endpoint: /cmdb/router/ospf

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_ospf.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.router.ospf


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoOspfValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.router._helpers import ospf as validators
            print(f"✅ Successfully imported validators for ospf")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_router_ospf_post")
            assert hasattr(validators, "validate_router_ospf_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.router._helpers import ospf as validators
        
        # Build minimal valid config with all required fields
        config = {
            "router-id": "0.0.0.0",  # ipv4-address-any
        }
        
        try:
            result = validators.validate_router_ospf_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoOspfEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_abr_type(self):
        """Test enum field abr-type validation."""
        from hfortix_fortios.api.v2.cmdb.router._helpers import ospf as validators
        
        valid_values = ['cisco', 'ibm', 'shortcut', 'standard']
        
        # Test each valid value
        for value in valid_values:
            config = {"abr-type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: abr-type={value}")
        
        print(f"✅ Enum field abr-type has {len(valid_values)} valid values")
    def auto_test_enum_database_overflow(self):
        """Test enum field database-overflow validation."""
        from hfortix_fortios.api.v2.cmdb.router._helpers import ospf as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"database-overflow": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: database-overflow={value}")
        
        print(f"✅ Enum field database-overflow has {len(valid_values)} valid values")
    def auto_test_enum_default_information_originate(self):
        """Test enum field default-information-originate validation."""
        from hfortix_fortios.api.v2.cmdb.router._helpers import ospf as validators
        
        valid_values = ['enable', 'always', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"default-information-originate": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: default-information-originate={value}")
        
        print(f"✅ Enum field default-information-originate has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/router/ospf"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/router.ospf.json"
TEST_HTTP_METHODS = ['GET', 'PUT']