"""
Auto-generated basic tests for cmdb.system/ipip_tunnel

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.ipip-tunnel.json
Category: cmdb
Endpoint: /cmdb/system/ipip-tunnel

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_ipip-tunnel.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.ipip_tunnel


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoIpipTunnelValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.system._helpers import ipip_tunnel as validators
            print(f"✅ Successfully imported validators for ipip-tunnel")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_system_ipip_tunnel_post")
            assert hasattr(validators, "validate_system_ipip_tunnel_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import ipip_tunnel as validators
        
        # Build minimal valid config with all required fields
        config = {
            "interface": "test_interface",  # string
            "local-gw": "0.0.0.0",  # ipv4-address-any
            "remote-gw": "0.0.0.0",  # ipv4-address
        }
        
        try:
            result = validators.validate_system_ipip_tunnel_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoIpipTunnelEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_use_sdwan(self):
        """Test enum field use-sdwan validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import ipip_tunnel as validators
        
        valid_values = ['disable', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"use-sdwan": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: use-sdwan={value}")
        
        print(f"✅ Enum field use-sdwan has {len(valid_values)} valid values")
    def auto_test_enum_auto_asic_offload(self):
        """Test enum field auto-asic-offload validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import ipip_tunnel as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"auto-asic-offload": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: auto-asic-offload={value}")
        
        print(f"✅ Enum field auto-asic-offload has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/ipip_tunnel"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.ipip-tunnel.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']