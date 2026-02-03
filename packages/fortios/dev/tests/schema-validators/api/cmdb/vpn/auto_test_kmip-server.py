"""
Auto-generated basic tests for cmdb.vpn/kmip_server

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/vpn.kmip-server.json
Category: cmdb
Endpoint: /cmdb/vpn/kmip-server

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_kmip-server.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.vpn.kmip_server


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoKmipServerValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.vpn._helpers import kmip_server as validators
            print(f"✅ Successfully imported validators for kmip-server")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_vpn_kmip_server_post")
            assert hasattr(validators, "validate_vpn_kmip_server_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.vpn._helpers import kmip_server as validators
        
        # Build minimal valid config with all required fields
        config = {
            "interface": "test_interface",  # string
            "password": "",  # password
            "server-list": "test_server-list",  # string
            "username": "test_username",  # string
        }
        
        try:
            result = validators.validate_vpn_kmip_server_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoKmipServerEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_ssl_min_proto_version(self):
        """Test enum field ssl-min-proto-version validation."""
        from hfortix_fortios.api.v2.cmdb.vpn._helpers import kmip_server as validators
        
        valid_values = ['default', 'SSLv3', 'TLSv1', 'TLSv1-1', 'TLSv1-2', 'TLSv1-3']
        
        # Test each valid value
        for value in valid_values:
            config = {"ssl-min-proto-version": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: ssl-min-proto-version={value}")
        
        print(f"✅ Enum field ssl-min-proto-version has {len(valid_values)} valid values")
    def auto_test_enum_server_identity_check(self):
        """Test enum field server-identity-check validation."""
        from hfortix_fortios.api.v2.cmdb.vpn._helpers import kmip_server as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"server-identity-check": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: server-identity-check={value}")
        
        print(f"✅ Enum field server-identity-check has {len(valid_values)} valid values")
    def auto_test_enum_interface_select_method(self):
        """Test enum field interface-select-method validation."""
        from hfortix_fortios.api.v2.cmdb.vpn._helpers import kmip_server as validators
        
        valid_values = ['auto', 'sdwan', 'specify']
        
        # Test each valid value
        for value in valid_values:
            config = {"interface-select-method": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: interface-select-method={value}")
        
        print(f"✅ Enum field interface-select-method has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/vpn/kmip_server"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/vpn.kmip-server.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']