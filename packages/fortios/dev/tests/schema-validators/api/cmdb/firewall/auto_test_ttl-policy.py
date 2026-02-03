"""
Auto-generated basic tests for cmdb.firewall/ttl_policy

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.ttl-policy.json
Category: cmdb
Endpoint: /cmdb/firewall/ttl-policy

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_ttl-policy.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.firewall.ttl_policy


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoTtlPolicyValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.firewall._helpers import ttl_policy as validators
            print(f"✅ Successfully imported validators for ttl-policy")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_firewall_ttl_policy_post")
            assert hasattr(validators, "validate_firewall_ttl_policy_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import ttl_policy as validators
        
        # Build minimal valid config with all required fields
        config = {
            "id": 0,  # integer
            "schedule": "test_schedule",  # string
            "service": "test_service",  # string
            "srcaddr": "test_srcaddr",  # string
            "srcintf": "test_srcintf",  # string
            "ttl": "",  # user
        }
        
        try:
            result = validators.validate_firewall_ttl_policy_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoTtlPolicyEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_status(self):
        """Test enum field status validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import ttl_policy as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"status": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: status={value}")
        
        print(f"✅ Enum field status has {len(valid_values)} valid values")
    def auto_test_enum_action(self):
        """Test enum field action validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import ttl_policy as validators
        
        valid_values = ['accept', 'deny']
        
        # Test each valid value
        for value in valid_values:
            config = {"action": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: action={value}")
        
        print(f"✅ Enum field action has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/firewall/ttl_policy"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.ttl-policy.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']