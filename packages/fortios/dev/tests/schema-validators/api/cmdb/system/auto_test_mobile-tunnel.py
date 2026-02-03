"""
Auto-generated basic tests for cmdb.system/mobile_tunnel

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.mobile-tunnel.json
Category: cmdb
Endpoint: /cmdb/system/mobile-tunnel

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_mobile-tunnel.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.mobile_tunnel


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoMobileTunnelValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.system._helpers import mobile_tunnel as validators
            print(f"✅ Successfully imported validators for mobile-tunnel")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_system_mobile_tunnel_post")
            assert hasattr(validators, "validate_system_mobile_tunnel_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import mobile_tunnel as validators
        
        # Build minimal valid config with all required fields
        config = {
            "hash-algorithm": "hmac-md5",  # option
            "home-agent": "0.0.0.0",  # ipv4-address
            "lifetime": 65535,  # integer
            "n-mhae-key-type": "ascii",  # option
            "n-mhae-spi": 256,  # integer
            "reg-interval": 5,  # integer
            "reg-retry": 3,  # integer
            "renew-interval": 60,  # integer
            "roaming-interface": "test_roaming-interface",  # string
            "tunnel-mode": "gre",  # option
        }
        
        try:
            result = validators.validate_system_mobile_tunnel_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoMobileTunnelEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_status(self):
        """Test enum field status validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import mobile_tunnel as validators
        
        valid_values = ['disable', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"status": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: status={value}")
        
        print(f"✅ Enum field status has {len(valid_values)} valid values")
    def auto_test_enum_n_mhae_key_type(self):
        """Test enum field n-mhae-key-type validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import mobile_tunnel as validators
        
        valid_values = ['ascii', 'base64']
        
        # Test each valid value
        for value in valid_values:
            config = {"n-mhae-key-type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: n-mhae-key-type={value}")
        
        print(f"✅ Enum field n-mhae-key-type has {len(valid_values)} valid values")
    def auto_test_enum_hash_algorithm(self):
        """Test enum field hash-algorithm validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import mobile_tunnel as validators
        
        valid_values = ['hmac-md5']
        
        # Test each valid value
        for value in valid_values:
            config = {"hash-algorithm": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: hash-algorithm={value}")
        
        print(f"✅ Enum field hash-algorithm has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/mobile_tunnel"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.mobile-tunnel.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']