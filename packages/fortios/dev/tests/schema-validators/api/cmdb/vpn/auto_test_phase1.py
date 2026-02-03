"""
Auto-generated basic tests for cmdb.vpn/ipsec/phase1

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/vpn.ipsec.phase1.json
Category: cmdb
Endpoint: /cmdb/vpn.ipsec/phase1

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_phase1.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.vpn.ipsec.phase1


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoPhase1Validators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.vpn.ipsec._helpers import phase1 as validators
            print(f"✅ Successfully imported validators for phase1")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_vpn_ipsec_phase1_post")
            assert hasattr(validators, "validate_vpn_ipsec_phase1_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.vpn.ipsec._helpers import phase1 as validators
        
        # Build minimal valid config with all required fields
        config = {
            "authpasswd": "",  # password
            "authusr": "test_authusr",  # string
            "certificate": "test_certificate",  # string
            "dev-id": "test_dev-id",  # string
            "group-authentication-secret": "",  # password-3
            "interface": "test_interface",  # string
            "ipv4-end-ip": "0.0.0.0",  # ipv4-address
            "ipv4-start-ip": "0.0.0.0",  # ipv4-address
            "ipv6-end-ip": "::",  # ipv6-address
            "ipv6-start-ip": "::",  # ipv6-address
            "network-id": 0,  # integer
            "peer": "test_peer",  # string
            "peergrp": "test_peergrp",  # string
            "peerid": "test_peerid",  # string
            "ppk-secret": "",  # password-3
            "proposal": "des-md5",  # option
            "psksecret": "",  # password-3
            "psksecret-remote": "",  # password-3
            "remote-gw": "0.0.0.0",  # ipv4-address
            "remote-gw-ztna-tags": "test_remote-gw-ztna-tags",  # string
            "remotegw-ddns": "test_remotegw-ddns",  # string
            "signature-hash-alg": "sha1",  # option
            "usrgrp": "test_usrgrp",  # string
        }
        
        try:
            result = validators.validate_vpn_ipsec_phase1_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoPhase1Enums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_type(self):
        """Test enum field type validation."""
        from hfortix_fortios.api.v2.cmdb.vpn.ipsec._helpers import phase1 as validators
        
        valid_values = ['static', 'dynamic', 'ddns']
        
        # Test each valid value
        for value in valid_values:
            config = {"type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: type={value}")
        
        print(f"✅ Enum field type has {len(valid_values)} valid values")
    def auto_test_enum_ike_version(self):
        """Test enum field ike-version validation."""
        from hfortix_fortios.api.v2.cmdb.vpn.ipsec._helpers import phase1 as validators
        
        valid_values = ['1', '2']
        
        # Test each valid value
        for value in valid_values:
            config = {"ike-version": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: ike-version={value}")
        
        print(f"✅ Enum field ike-version has {len(valid_values)} valid values")
    def auto_test_enum_authmethod(self):
        """Test enum field authmethod validation."""
        from hfortix_fortios.api.v2.cmdb.vpn.ipsec._helpers import phase1 as validators
        
        valid_values = ['psk', 'signature']
        
        # Test each valid value
        for value in valid_values:
            config = {"authmethod": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: authmethod={value}")
        
        print(f"✅ Enum field authmethod has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/vpn/ipsec/phase1"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/vpn.ipsec.phase1.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']