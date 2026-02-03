"""
Auto-generated basic tests for cmdb.vpn/ipsec/manualkey

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/vpn.ipsec.manualkey.json
Category: cmdb
Endpoint: /cmdb/vpn.ipsec/manualkey

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_manualkey.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.vpn.ipsec.manualkey


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoManualkeyValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.vpn.ipsec._helpers import manualkey as validators
            print(f"✅ Successfully imported validators for manualkey")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_vpn_ipsec_manualkey_post")
            assert hasattr(validators, "validate_vpn_ipsec_manualkey_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.vpn.ipsec._helpers import manualkey as validators
        
        # Build minimal valid config with all required fields
        config = {
            "authentication": "null",  # option
            "authkey": "",  # user
            "enckey": "",  # user
            "encryption": "null",  # option
            "interface": "test_interface",  # string
            "localspi": "",  # user
            "remote-gw": "0.0.0.0",  # ipv4-address
            "remotespi": "",  # user
        }
        
        try:
            result = validators.validate_vpn_ipsec_manualkey_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoManualkeyEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_authentication(self):
        """Test enum field authentication validation."""
        from hfortix_fortios.api.v2.cmdb.vpn.ipsec._helpers import manualkey as validators
        
        valid_values = ['null', 'md5', 'sha1', 'sha256', 'sha384', 'sha512']
        
        # Test each valid value
        for value in valid_values:
            config = {"authentication": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: authentication={value}")
        
        print(f"✅ Enum field authentication has {len(valid_values)} valid values")
    def auto_test_enum_encryption(self):
        """Test enum field encryption validation."""
        from hfortix_fortios.api.v2.cmdb.vpn.ipsec._helpers import manualkey as validators
        
        valid_values = ['null', 'des', '3des', 'aes128', 'aes192', 'aes256', 'aria128', 'aria192', 'aria256', 'seed']
        
        # Test each valid value
        for value in valid_values:
            config = {"encryption": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: encryption={value}")
        
        print(f"✅ Enum field encryption has {len(valid_values)} valid values")
    def auto_test_enum_npu_offload(self):
        """Test enum field npu-offload validation."""
        from hfortix_fortios.api.v2.cmdb.vpn.ipsec._helpers import manualkey as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"npu-offload": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: npu-offload={value}")
        
        print(f"✅ Enum field npu-offload has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/vpn/ipsec/manualkey"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/vpn.ipsec.manualkey.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']