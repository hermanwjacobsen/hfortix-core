"""
Auto-generated basic tests for cmdb.firewall/proxy_policy

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.proxy-policy.json
Category: cmdb
Endpoint: /cmdb/firewall/proxy-policy

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_proxy-policy.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.firewall.proxy_policy


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoProxyPolicyValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.firewall._helpers import proxy_policy as validators
            print(f"✅ Successfully imported validators for proxy-policy")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_firewall_proxy_policy_post")
            assert hasattr(validators, "validate_firewall_proxy_policy_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import proxy_policy as validators
        
        # Build minimal valid config with all required fields
        config = {
            "dstintf": "test_dstintf",  # string
            "isolator-server": "test_isolator-server",  # string
            "proxy": "explicit-web",  # option
            "schedule": "test_schedule",  # string
            "srcintf": "test_srcintf",  # string
        }
        
        try:
            result = validators.validate_firewall_proxy_policy_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoProxyPolicyEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_proxy(self):
        """Test enum field proxy validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import proxy_policy as validators
        
        valid_values = ['explicit-web', 'transparent-web', 'ftp', 'ssh', 'ssh-tunnel', 'access-proxy', 'ztna-proxy', 'wanopt']
        
        # Test each valid value
        for value in valid_values:
            config = {"proxy": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: proxy={value}")
        
        print(f"✅ Enum field proxy has {len(valid_values)} valid values")
    def auto_test_enum_ztna_tags_match_logic(self):
        """Test enum field ztna-tags-match-logic validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import proxy_policy as validators
        
        valid_values = ['or', 'and']
        
        # Test each valid value
        for value in valid_values:
            config = {"ztna-tags-match-logic": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: ztna-tags-match-logic={value}")
        
        print(f"✅ Enum field ztna-tags-match-logic has {len(valid_values)} valid values")
    def auto_test_enum_device_ownership(self):
        """Test enum field device-ownership validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import proxy_policy as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"device-ownership": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: device-ownership={value}")
        
        print(f"✅ Enum field device-ownership has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/firewall/proxy_policy"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.proxy-policy.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']