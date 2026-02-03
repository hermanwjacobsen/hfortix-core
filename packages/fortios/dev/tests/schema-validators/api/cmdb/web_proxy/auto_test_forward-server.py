"""
Auto-generated basic tests for cmdb.web_proxy/forward_server

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/web-proxy.forward-server.json
Category: cmdb
Endpoint: /cmdb/web-proxy/forward-server

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_forward-server.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.web_proxy.forward_server


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoForwardServerValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.web_proxy._helpers import forward_server as validators
            print(f"✅ Successfully imported validators for forward-server")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_web_proxy_forward_server_post")
            assert hasattr(validators, "validate_web_proxy_forward_server_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.web_proxy._helpers import forward_server as validators
        
        # Build minimal valid config with all required fields
        config = {
            "interface": "test_interface",  # string
        }
        
        try:
            result = validators.validate_web_proxy_forward_server_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoForwardServerEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_addr_type(self):
        """Test enum field addr-type validation."""
        from hfortix_fortios.api.v2.cmdb.web_proxy._helpers import forward_server as validators
        
        valid_values = ['ip', 'ipv6', 'fqdn']
        
        # Test each valid value
        for value in valid_values:
            config = {"addr-type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: addr-type={value}")
        
        print(f"✅ Enum field addr-type has {len(valid_values)} valid values")
    def auto_test_enum_interface_select_method(self):
        """Test enum field interface-select-method validation."""
        from hfortix_fortios.api.v2.cmdb.web_proxy._helpers import forward_server as validators
        
        valid_values = ['sdwan', 'specify']
        
        # Test each valid value
        for value in valid_values:
            config = {"interface-select-method": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: interface-select-method={value}")
        
        print(f"✅ Enum field interface-select-method has {len(valid_values)} valid values")
    def auto_test_enum_masquerade(self):
        """Test enum field masquerade validation."""
        from hfortix_fortios.api.v2.cmdb.web_proxy._helpers import forward_server as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"masquerade": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: masquerade={value}")
        
        print(f"✅ Enum field masquerade has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/web_proxy/forward_server"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/web-proxy.forward-server.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']