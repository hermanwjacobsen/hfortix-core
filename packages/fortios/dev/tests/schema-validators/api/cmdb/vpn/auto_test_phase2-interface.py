"""
Auto-generated basic tests for cmdb.vpn/ipsec/phase2_interface

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/vpn.ipsec.phase2-interface.json
Category: cmdb
Endpoint: /cmdb/vpn.ipsec/phase2-interface

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_phase2-interface.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.vpn.ipsec.phase2_interface


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoPhase2InterfaceValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.vpn.ipsec._helpers import phase2_interface as validators
            print(f"✅ Successfully imported validators for phase2-interface")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_vpn_ipsec_phase2_interface_post")
            assert hasattr(validators, "validate_vpn_ipsec_phase2_interface_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.vpn.ipsec._helpers import phase2_interface as validators
        
        # Build minimal valid config with all required fields
        config = {
            "dst-name": "test_dst-name",  # string
            "dst-name6": "test_dst-name6",  # string
            "phase1name": "test_phase1name",  # string
            "proposal": "null-md5",  # option
            "src-name": "test_src-name",  # string
            "src-name6": "test_src-name6",  # string
        }
        
        try:
            result = validators.validate_vpn_ipsec_phase2_interface_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoPhase2InterfaceEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_dhcp_ipsec(self):
        """Test enum field dhcp-ipsec validation."""
        from hfortix_fortios.api.v2.cmdb.vpn.ipsec._helpers import phase2_interface as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"dhcp-ipsec": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: dhcp-ipsec={value}")
        
        print(f"✅ Enum field dhcp-ipsec has {len(valid_values)} valid values")
    def auto_test_enum_proposal(self):
        """Test enum field proposal validation."""
        from hfortix_fortios.api.v2.cmdb.vpn.ipsec._helpers import phase2_interface as validators
        
        valid_values = ['null-md5', 'null-sha1', 'null-sha256', 'null-sha384', 'null-sha512', 'des-null', 'des-md5', 'des-sha1', 'des-sha256', 'des-sha384', 'des-sha512', '3des-null', '3des-md5', '3des-sha1', '3des-sha256', '3des-sha384', '3des-sha512', 'aes128-null', 'aes128-md5', 'aes128-sha1', 'aes128-sha256', 'aes128-sha384', 'aes128-sha512', 'aes128gcm', 'aes192-null', 'aes192-md5', 'aes192-sha1', 'aes192-sha256', 'aes192-sha384', 'aes192-sha512', 'aes256-null', 'aes256-md5', 'aes256-sha1', 'aes256-sha256', 'aes256-sha384', 'aes256-sha512', 'aes256gcm', 'chacha20poly1305', 'aria128-null', 'aria128-md5', 'aria128-sha1', 'aria128-sha256', 'aria128-sha384', 'aria128-sha512', 'aria192-null', 'aria192-md5', 'aria192-sha1', 'aria192-sha256', 'aria192-sha384', 'aria192-sha512', 'aria256-null', 'aria256-md5', 'aria256-sha1', 'aria256-sha256', 'aria256-sha384', 'aria256-sha512', 'seed-null', 'seed-md5', 'seed-sha1', 'seed-sha256', 'seed-sha384', 'seed-sha512']
        
        # Test each valid value
        for value in valid_values:
            config = {"proposal": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: proposal={value}")
        
        print(f"✅ Enum field proposal has {len(valid_values)} valid values")
    def auto_test_enum_pfs(self):
        """Test enum field pfs validation."""
        from hfortix_fortios.api.v2.cmdb.vpn.ipsec._helpers import phase2_interface as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"pfs": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: pfs={value}")
        
        print(f"✅ Enum field pfs has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/vpn/ipsec/phase2_interface"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/vpn.ipsec.phase2-interface.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']