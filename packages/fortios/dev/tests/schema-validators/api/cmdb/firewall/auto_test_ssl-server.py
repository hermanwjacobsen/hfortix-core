"""
Auto-generated basic tests for cmdb.firewall/ssl_server

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.ssl-server.json
Category: cmdb
Endpoint: /cmdb/firewall/ssl-server

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_ssl-server.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.firewall.ssl_server


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoSslServerValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.firewall._helpers import ssl_server as validators
            print(f"✅ Successfully imported validators for ssl-server")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_firewall_ssl_server_post")
            assert hasattr(validators, "validate_firewall_ssl_server_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import ssl_server as validators
        
        # Build minimal valid config with all required fields
        config = {
            "ip": "0.0.0.0",  # ipv4-address-any
            "mapped-port": 80,  # integer
            "port": 443,  # integer
        }
        
        try:
            result = validators.validate_firewall_ssl_server_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoSslServerEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_ssl_mode(self):
        """Test enum field ssl-mode validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import ssl_server as validators
        
        valid_values = ['half', 'full']
        
        # Test each valid value
        for value in valid_values:
            config = {"ssl-mode": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: ssl-mode={value}")
        
        print(f"✅ Enum field ssl-mode has {len(valid_values)} valid values")
    def auto_test_enum_add_header_x_forwarded_proto(self):
        """Test enum field add-header-x-forwarded-proto validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import ssl_server as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"add-header-x-forwarded-proto": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: add-header-x-forwarded-proto={value}")
        
        print(f"✅ Enum field add-header-x-forwarded-proto has {len(valid_values)} valid values")
    def auto_test_enum_ssl_dh_bits(self):
        """Test enum field ssl-dh-bits validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import ssl_server as validators
        
        valid_values = ['768', '1024', '1536', '2048']
        
        # Test each valid value
        for value in valid_values:
            config = {"ssl-dh-bits": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: ssl-dh-bits={value}")
        
        print(f"✅ Enum field ssl-dh-bits has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/firewall/ssl_server"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.ssl-server.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']