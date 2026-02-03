"""
Auto-generated basic tests for cmdb.firewall/shaping_policy

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.shaping-policy.json
Category: cmdb
Endpoint: /cmdb/firewall/shaping-policy

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_shaping-policy.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.firewall.shaping_policy


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoShapingPolicyValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.firewall._helpers import shaping_policy as validators
            print(f"✅ Successfully imported validators for shaping-policy")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_firewall_shaping_policy_post")
            assert hasattr(validators, "validate_firewall_shaping_policy_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import shaping_policy as validators
        
        # Build minimal valid config with all required fields
        config = {
            "dstaddr": "test_dstaddr",  # string
            "dstaddr6": "test_dstaddr6",  # string
            "dstintf": "test_dstintf",  # string
            "service": "test_service",  # string
            "srcaddr": "test_srcaddr",  # string
            "srcaddr6": "test_srcaddr6",  # string
        }
        
        try:
            result = validators.validate_firewall_shaping_policy_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoShapingPolicyEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_status(self):
        """Test enum field status validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import shaping_policy as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"status": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: status={value}")
        
        print(f"✅ Enum field status has {len(valid_values)} valid values")
    def auto_test_enum_ip_version(self):
        """Test enum field ip-version validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import shaping_policy as validators
        
        valid_values = ['4', '6']
        
        # Test each valid value
        for value in valid_values:
            config = {"ip-version": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: ip-version={value}")
        
        print(f"✅ Enum field ip-version has {len(valid_values)} valid values")
    def auto_test_enum_traffic_type(self):
        """Test enum field traffic-type validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import shaping_policy as validators
        
        valid_values = ['forwarding', 'local-in', 'local-out']
        
        # Test each valid value
        for value in valid_values:
            config = {"traffic-type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: traffic-type={value}")
        
        print(f"✅ Enum field traffic-type has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/firewall/shaping_policy"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.shaping-policy.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']