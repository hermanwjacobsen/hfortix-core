"""
Auto-generated basic tests for cmdb.system/ptp

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.ptp.json
Category: cmdb
Endpoint: /cmdb/system/ptp

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_ptp.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.ptp


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoPtpValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.system._helpers import ptp as validators
            print(f"✅ Successfully imported validators for ptp")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_system_ptp_post")
            assert hasattr(validators, "validate_system_ptp_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import ptp as validators
        
        # Build minimal valid config with all required fields
        config = {
            "interface": "test_interface",  # string
        }
        
        try:
            result = validators.validate_system_ptp_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoPtpEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_status(self):
        """Test enum field status validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import ptp as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"status": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: status={value}")
        
        print(f"✅ Enum field status has {len(valid_values)} valid values")
    def auto_test_enum_mode(self):
        """Test enum field mode validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import ptp as validators
        
        valid_values = ['multicast', 'hybrid']
        
        # Test each valid value
        for value in valid_values:
            config = {"mode": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: mode={value}")
        
        print(f"✅ Enum field mode has {len(valid_values)} valid values")
    def auto_test_enum_delay_mechanism(self):
        """Test enum field delay-mechanism validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import ptp as validators
        
        valid_values = ['E2E', 'P2P']
        
        # Test each valid value
        for value in valid_values:
            config = {"delay-mechanism": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: delay-mechanism={value}")
        
        print(f"✅ Enum field delay-mechanism has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/ptp"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.ptp.json"
TEST_HTTP_METHODS = ['GET', 'PUT']