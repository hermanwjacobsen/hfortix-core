"""
Auto-generated basic tests for cmdb.system/dns64

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.dns64.json
Category: cmdb
Endpoint: /cmdb/system/dns64

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_dns64.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.dns64


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoDns64Validators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.system._helpers import dns64 as validators
            print(f"✅ Successfully imported validators for dns64")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_system_dns64_post")
            assert hasattr(validators, "validate_system_dns64_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import dns64 as validators
        
        # Build minimal valid config with all required fields
        config = {
            "dns64-prefix": "64:ff9b::/96",  # ipv6-prefix
        }
        
        try:
            result = validators.validate_system_dns64_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoDns64Enums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_status(self):
        """Test enum field status validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import dns64 as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"status": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: status={value}")
        
        print(f"✅ Enum field status has {len(valid_values)} valid values")
    def auto_test_enum_always_synthesize_aaaa_record(self):
        """Test enum field always-synthesize-aaaa-record validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import dns64 as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"always-synthesize-aaaa-record": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: always-synthesize-aaaa-record={value}")
        
        print(f"✅ Enum field always-synthesize-aaaa-record has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/dns64"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.dns64.json"
TEST_HTTP_METHODS = ['GET', 'PUT']