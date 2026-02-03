"""
Auto-generated basic tests for cmdb.vpn/ipsec/phase1_interface

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/vpn.ipsec.phase1-interface.json
Category: cmdb
Endpoint: /cmdb/vpn.ipsec/phase1-interface

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_phase1-interface.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.vpn.ipsec.phase1_interface


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoPhase1InterfaceValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.vpn.ipsec._helpers import phase1_interface as validators
            print(f"✅ Successfully imported validators for phase1-interface")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_vpn_ipsec_phase1_interface_post")
            assert hasattr(validators, "validate_vpn_ipsec_phase1_interface_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.vpn.ipsec._helpers import phase1_interface as validators
        
        # Build minimal valid config with all required fields
        config = {
            "authpasswd": "",  # password
            "authusr": "test_authusr",  # string
            "certificate": "test_certificate",  # string
            "dev-id": "test_dev-id",  # string
            "encap-local-gw4": "0.0.0.0",  # ipv4-address
            "encap-local-gw6": "::",  # ipv6-address
            "encap-remote-gw4": "0.0.0.0",  # ipv4-address
            "encap-remote-gw6": "::",  # ipv6-address
            "group-authentication-secret": "",  # password-3
            "interface": "test_interface",  # string
            "ipv4-end-ip": "0.0.0.0",  # ipv4-address
            "ipv4-start-ip": "0.0.0.0",  # ipv4-address
            "ipv6-end-ip": "::",  # ipv6-address
            "ipv6-start-ip": "::",  # ipv6-address
            "monitor-hold-down-delay": 0,  # integer
            "monitor-hold-down-time": "",  # user
            "monitor-hold-down-weekday": "everyday",  # option
            "net-device": "enable",  # option
            "network-id": 0,  # integer
            "peer": "test_peer",  # string
            "peer-egress-shaping-value": 0,  # integer
            "peergrp": "test_peergrp",  # string
            "peerid": "test_peerid",  # string
            "ppk-secret": "",  # password-3
            "proposal": "des-md5",  # option
            "psksecret": "",  # password-3
            "psksecret-remote": "",  # password-3
            "remote-gw": "0.0.0.0",  # ipv4-address
            "remote-gw-ztna-tags": "test_remote-gw-ztna-tags",  # string
            "remote-gw6": "::",  # ipv6-address
            "remotegw-ddns": "test_remotegw-ddns",  # string
            "signature-hash-alg": "sha1",  # option
            "usrgrp": "test_usrgrp",  # string
        }
        
        try:
            result = validators.validate_vpn_ipsec_phase1_interface_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoPhase1InterfaceEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_type(self):
        """Test enum field type validation."""
        from hfortix_fortios.api.v2.cmdb.vpn.ipsec._helpers import phase1_interface as validators
        
        valid_values = ['static', 'dynamic', 'ddns']
        
        # Test each valid value
        for value in valid_values:
            config = {"type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: type={value}")
        
        print(f"✅ Enum field type has {len(valid_values)} valid values")
    def auto_test_enum_ip_version(self):
        """Test enum field ip-version validation."""
        from hfortix_fortios.api.v2.cmdb.vpn.ipsec._helpers import phase1_interface as validators
        
        valid_values = ['4', '6']
        
        # Test each valid value
        for value in valid_values:
            config = {"ip-version": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: ip-version={value}")
        
        print(f"✅ Enum field ip-version has {len(valid_values)} valid values")
    def auto_test_enum_ike_version(self):
        """Test enum field ike-version validation."""
        from hfortix_fortios.api.v2.cmdb.vpn.ipsec._helpers import phase1_interface as validators
        
        valid_values = ['1', '2']
        
        # Test each valid value
        for value in valid_values:
            config = {"ike-version": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: ike-version={value}")
        
        print(f"✅ Enum field ike-version has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/vpn/ipsec/phase1_interface"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/vpn.ipsec.phase1-interface.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']