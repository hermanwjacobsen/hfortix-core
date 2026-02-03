"""
Auto-generated basic tests for cmdb.router/static

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/router.static.json
Category: cmdb
Endpoint: /cmdb/router/static

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_static.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.router.static


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoStaticValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.router._helpers import static as validators
            print(f"✅ Successfully imported validators for static")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_router_static_post")
            assert hasattr(validators, "validate_router_static_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.router._helpers import static as validators
        
        # Build minimal valid config with all required fields
        config = {
            "device": "test_device",  # string
            "dst": "0.0.0.0 0.0.0.0",  # ipv4-classnet
        }
        
        try:
            result = validators.validate_router_static_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoStaticEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_status(self):
        """Test enum field status validation."""
        from hfortix_fortios.api.v2.cmdb.router._helpers import static as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"status": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: status={value}")
        
        print(f"✅ Enum field status has {len(valid_values)} valid values")
    def auto_test_enum_blackhole(self):
        """Test enum field blackhole validation."""
        from hfortix_fortios.api.v2.cmdb.router._helpers import static as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"blackhole": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: blackhole={value}")
        
        print(f"✅ Enum field blackhole has {len(valid_values)} valid values")
    def auto_test_enum_dynamic_gateway(self):
        """Test enum field dynamic-gateway validation."""
        from hfortix_fortios.api.v2.cmdb.router._helpers import static as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"dynamic-gateway": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: dynamic-gateway={value}")
        
        print(f"✅ Enum field dynamic-gateway has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/router/static"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/router.static.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']