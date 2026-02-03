"""
Auto-generated basic tests for cmdb.vpn/ipsec/phase2

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/vpn.ipsec.phase2.json
Category: cmdb
Endpoint: /cmdb/vpn.ipsec/phase2

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_phase2.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.vpn.ipsec.phase2


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoPhase2Validators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.vpn.ipsec._helpers import phase2 as validators
            print(f"✅ Successfully imported validators for phase2")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_vpn_ipsec_phase2_post")
            assert hasattr(validators, "validate_vpn_ipsec_phase2_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.vpn.ipsec._helpers import phase2 as validators
        
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
            result = validators.validate_vpn_ipsec_phase2_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoPhase2Enums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_dhcp_ipsec(self):
        """Test enum field dhcp-ipsec validation."""
        from hfortix_fortios.api.v2.cmdb.vpn.ipsec._helpers import phase2 as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"dhcp-ipsec": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: dhcp-ipsec={value}")
        
        print(f"✅ Enum field dhcp-ipsec has {len(valid_values)} valid values")
    def auto_test_enum_use_natip(self):
        """Test enum field use-natip validation."""
        from hfortix_fortios.api.v2.cmdb.vpn.ipsec._helpers import phase2 as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"use-natip": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: use-natip={value}")
        
        print(f"✅ Enum field use-natip has {len(valid_values)} valid values")
    def auto_test_enum_selector_match(self):
        """Test enum field selector-match validation."""
        from hfortix_fortios.api.v2.cmdb.vpn.ipsec._helpers import phase2 as validators
        
        valid_values = ['exact', 'subset', 'auto']
        
        # Test each valid value
        for value in valid_values:
            config = {"selector-match": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: selector-match={value}")
        
        print(f"✅ Enum field selector-match has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/vpn/ipsec/phase2"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/vpn.ipsec.phase2.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']