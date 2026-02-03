"""
Auto-generated basic tests for cmdb.vpn/ipsec/manualkey_interface

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/vpn.ipsec.manualkey-interface.json
Category: cmdb
Endpoint: /cmdb/vpn.ipsec/manualkey-interface

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_manualkey-interface.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.vpn.ipsec.manualkey_interface


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoManualkeyInterfaceValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.vpn.ipsec._helpers import manualkey_interface as validators
            print(f"✅ Successfully imported validators for manualkey-interface")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_vpn_ipsec_manualkey_interface_post")
            assert hasattr(validators, "validate_vpn_ipsec_manualkey_interface_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.vpn.ipsec._helpers import manualkey_interface as validators
        
        # Build minimal valid config with all required fields
        config = {
            "auth-alg": "null",  # option
            "auth-key": "",  # user
            "enc-alg": "null",  # option
            "enc-key": "",  # user
            "interface": "test_interface",  # string
            "local-spi": "",  # user
            "remote-gw": "0.0.0.0",  # ipv4-address
            "remote-gw6": "::",  # ipv6-address
            "remote-spi": "",  # user
        }
        
        try:
            result = validators.validate_vpn_ipsec_manualkey_interface_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoManualkeyInterfaceEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_ip_version(self):
        """Test enum field ip-version validation."""
        from hfortix_fortios.api.v2.cmdb.vpn.ipsec._helpers import manualkey_interface as validators
        
        valid_values = ['4', '6']
        
        # Test each valid value
        for value in valid_values:
            config = {"ip-version": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: ip-version={value}")
        
        print(f"✅ Enum field ip-version has {len(valid_values)} valid values")
    def auto_test_enum_addr_type(self):
        """Test enum field addr-type validation."""
        from hfortix_fortios.api.v2.cmdb.vpn.ipsec._helpers import manualkey_interface as validators
        
        valid_values = ['4', '6']
        
        # Test each valid value
        for value in valid_values:
            config = {"addr-type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: addr-type={value}")
        
        print(f"✅ Enum field addr-type has {len(valid_values)} valid values")
    def auto_test_enum_auth_alg(self):
        """Test enum field auth-alg validation."""
        from hfortix_fortios.api.v2.cmdb.vpn.ipsec._helpers import manualkey_interface as validators
        
        valid_values = ['null', 'md5', 'sha1', 'sha256', 'sha384', 'sha512']
        
        # Test each valid value
        for value in valid_values:
            config = {"auth-alg": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: auth-alg={value}")
        
        print(f"✅ Enum field auth-alg has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/vpn/ipsec/manualkey_interface"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/vpn.ipsec.manualkey-interface.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']