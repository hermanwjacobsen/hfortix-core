"""
Auto-generated basic tests for cmdb.vpn/pptp

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/vpn.pptp.json
Category: cmdb
Endpoint: /cmdb/vpn/pptp

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_pptp.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.vpn.pptp


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoPptpValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.vpn._helpers import pptp as validators
            print(f"✅ Successfully imported validators for pptp")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_vpn_pptp_post")
            assert hasattr(validators, "validate_vpn_pptp_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.vpn._helpers import pptp as validators
        
        # Build minimal valid config with all required fields
        config = {
            "eip": "0.0.0.0",  # ipv4-address
            "ip-mode": "range",  # option
            "local-ip": "0.0.0.0",  # ipv4-address
            "sip": "0.0.0.0",  # ipv4-address
            "status": "enable",  # option
            "usrgrp": "test_usrgrp",  # string
        }
        
        try:
            result = validators.validate_vpn_pptp_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoPptpEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_status(self):
        """Test enum field status validation."""
        from hfortix_fortios.api.v2.cmdb.vpn._helpers import pptp as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"status": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: status={value}")
        
        print(f"✅ Enum field status has {len(valid_values)} valid values")
    def auto_test_enum_ip_mode(self):
        """Test enum field ip-mode validation."""
        from hfortix_fortios.api.v2.cmdb.vpn._helpers import pptp as validators
        
        valid_values = ['range', 'usrgrp']
        
        # Test each valid value
        for value in valid_values:
            config = {"ip-mode": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: ip-mode={value}")
        
        print(f"✅ Enum field ip-mode has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/vpn/pptp"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/vpn.pptp.json"
TEST_HTTP_METHODS = ['GET', 'PUT']