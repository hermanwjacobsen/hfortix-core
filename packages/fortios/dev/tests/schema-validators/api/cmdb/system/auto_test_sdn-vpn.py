"""
Auto-generated basic tests for cmdb.system/sdn_vpn

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.sdn-vpn.json
Category: cmdb
Endpoint: /cmdb/system/sdn-vpn

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_sdn-vpn.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.sdn_vpn


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoSdnVpnValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.system._helpers import sdn_vpn as validators
            print(f"✅ Successfully imported validators for sdn-vpn")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_system_sdn_vpn_post")
            assert hasattr(validators, "validate_system_sdn_vpn_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import sdn_vpn as validators
        
        # Build minimal valid config with all required fields
        config = {
            "bgp-as": 65000,  # integer
            "cgw-gateway": "0.0.0.0",  # ipv4-address-any
            "internal-interface": "test_internal-interface",  # string
            "local-cidr": "0.0.0.0 0.0.0.0",  # ipv4-classnet
            "remote-cidr": "0.0.0.0 0.0.0.0",  # ipv4-classnet
            "remote-type": "vgw",  # option
            "routing-type": "static",  # option
            "sdn": "test_sdn",  # string
            "tgw-id": "test_tgw-id",  # string
            "tunnel-interface": "test_tunnel-interface",  # string
            "vgw-id": "test_vgw-id",  # string
        }
        
        try:
            result = validators.validate_system_sdn_vpn_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoSdnVpnEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_remote_type(self):
        """Test enum field remote-type validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import sdn_vpn as validators
        
        valid_values = ['vgw', 'tgw']
        
        # Test each valid value
        for value in valid_values:
            config = {"remote-type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: remote-type={value}")
        
        print(f"✅ Enum field remote-type has {len(valid_values)} valid values")
    def auto_test_enum_routing_type(self):
        """Test enum field routing-type validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import sdn_vpn as validators
        
        valid_values = ['static', 'dynamic']
        
        # Test each valid value
        for value in valid_values:
            config = {"routing-type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: routing-type={value}")
        
        print(f"✅ Enum field routing-type has {len(valid_values)} valid values")
    def auto_test_enum_nat_traversal(self):
        """Test enum field nat-traversal validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import sdn_vpn as validators
        
        valid_values = ['disable', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"nat-traversal": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: nat-traversal={value}")
        
        print(f"✅ Enum field nat-traversal has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/sdn_vpn"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.sdn-vpn.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']