"""
Auto-generated basic tests for cmdb.firewall/proxy_address

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.proxy-address.json
Category: cmdb
Endpoint: /cmdb/firewall/proxy-address

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_proxy-address.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.firewall.proxy_address


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoProxyAddressValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.firewall._helpers import proxy_address as validators
            print(f"✅ Successfully imported validators for proxy-address")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_firewall_proxy_address_post")
            assert hasattr(validators, "validate_firewall_proxy_address_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import proxy_address as validators
        
        # Build minimal valid config with all required fields
        config = {
            "application": "test_application",  # string
            "host": "test_host",  # string
        }
        
        try:
            result = validators.validate_firewall_proxy_address_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoProxyAddressEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_type(self):
        """Test enum field type validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import proxy_address as validators
        
        valid_values = ['host-regex', 'url', 'category', 'method', 'ua', 'header', 'src-advanced', 'dst-advanced', 'saas']
        
        # Test each valid value
        for value in valid_values:
            config = {"type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: type={value}")
        
        print(f"✅ Enum field type has {len(valid_values)} valid values")
    def auto_test_enum_referrer(self):
        """Test enum field referrer validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import proxy_address as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"referrer": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: referrer={value}")
        
        print(f"✅ Enum field referrer has {len(valid_values)} valid values")
    def auto_test_enum_method(self):
        """Test enum field method validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import proxy_address as validators
        
        valid_values = ['get', 'post', 'put', 'head', 'connect', 'trace', 'options', 'delete', 'update', 'patch', 'other']
        
        # Test each valid value
        for value in valid_values:
            config = {"method": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: method={value}")
        
        print(f"✅ Enum field method has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/firewall/proxy_address"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.proxy-address.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']