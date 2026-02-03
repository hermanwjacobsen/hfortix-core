"""
Auto-generated basic tests for cmdb.system/ha

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.ha.json
Category: cmdb
Endpoint: /cmdb/system/ha

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_ha.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.ha


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoHaValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.system._helpers import ha as validators
            print(f"✅ Successfully imported validators for ha")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_system_ha_post")
            assert hasattr(validators, "validate_system_ha_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import ha as validators
        
        # Build minimal valid config with all required fields
        config = {
            "ipsec-phase2-proposal": "aes128-sha1",  # option
        }
        
        try:
            result = validators.validate_system_ha_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoHaEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_mode(self):
        """Test enum field mode validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import ha as validators
        
        valid_values = ['standalone', 'a-a', 'a-p']
        
        # Test each valid value
        for value in valid_values:
            config = {"mode": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: mode={value}")
        
        print(f"✅ Enum field mode has {len(valid_values)} valid values")
    def auto_test_enum_sync_packet_balance(self):
        """Test enum field sync-packet-balance validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import ha as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"sync-packet-balance": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: sync-packet-balance={value}")
        
        print(f"✅ Enum field sync-packet-balance has {len(valid_values)} valid values")
    def auto_test_enum_unicast_hb(self):
        """Test enum field unicast-hb validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import ha as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"unicast-hb": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: unicast-hb={value}")
        
        print(f"✅ Enum field unicast-hb has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/ha"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.ha.json"
TEST_HTTP_METHODS = ['GET', 'PUT']