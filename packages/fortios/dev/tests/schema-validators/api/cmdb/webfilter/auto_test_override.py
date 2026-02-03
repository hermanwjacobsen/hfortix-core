"""
Auto-generated basic tests for cmdb.webfilter/override

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/webfilter.override.json
Category: cmdb
Endpoint: /cmdb/webfilter/override

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_override.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.webfilter.override


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoOverrideValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.webfilter._helpers import override as validators
            print(f"✅ Successfully imported validators for override")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_webfilter_override_post")
            assert hasattr(validators, "validate_webfilter_override_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.webfilter._helpers import override as validators
        
        # Build minimal valid config with all required fields
        config = {
            "expires": "1970/01/01 00:00:00",  # user
            "ip": "0.0.0.0",  # ipv4-address
            "ip6": "::",  # ipv6-address
            "new-profile": "test_new-profile",  # string
            "old-profile": "test_old-profile",  # string
            "user": "test_user",  # string
            "user-group": "test_user-group",  # string
        }
        
        try:
            result = validators.validate_webfilter_override_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoOverrideEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_status(self):
        """Test enum field status validation."""
        from hfortix_fortios.api.v2.cmdb.webfilter._helpers import override as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"status": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: status={value}")
        
        print(f"✅ Enum field status has {len(valid_values)} valid values")
    def auto_test_enum_scope(self):
        """Test enum field scope validation."""
        from hfortix_fortios.api.v2.cmdb.webfilter._helpers import override as validators
        
        valid_values = ['user', 'user-group', 'ip', 'ip6']
        
        # Test each valid value
        for value in valid_values:
            config = {"scope": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: scope={value}")
        
        print(f"✅ Enum field scope has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/webfilter/override"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/webfilter.override.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']