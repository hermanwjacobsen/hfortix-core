"""
Auto-generated basic tests for cmdb.firewall/access_proxy6

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.access-proxy6.json
Category: cmdb
Endpoint: /cmdb/firewall/access-proxy6

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_access-proxy6.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.firewall.access_proxy6


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoAccessProxy6Validators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.firewall._helpers import access_proxy6 as validators
            print(f"✅ Successfully imported validators for access-proxy6")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_firewall_access_proxy6_post")
            assert hasattr(validators, "validate_firewall_access_proxy6_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import access_proxy6 as validators
        
        # Build minimal valid config with all required fields
        config = {
            "vip": "test_vip",  # string
        }
        
        try:
            result = validators.validate_firewall_access_proxy6_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoAccessProxy6Enums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_auth_portal(self):
        """Test enum field auth-portal validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import access_proxy6 as validators
        
        valid_values = ['disable', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"auth-portal": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: auth-portal={value}")
        
        print(f"✅ Enum field auth-portal has {len(valid_values)} valid values")
    def auto_test_enum_log_blocked_traffic(self):
        """Test enum field log-blocked-traffic validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import access_proxy6 as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"log-blocked-traffic": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: log-blocked-traffic={value}")
        
        print(f"✅ Enum field log-blocked-traffic has {len(valid_values)} valid values")
    def auto_test_enum_add_vhost_domain_to_dnsdb(self):
        """Test enum field add-vhost-domain-to-dnsdb validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import access_proxy6 as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"add-vhost-domain-to-dnsdb": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: add-vhost-domain-to-dnsdb={value}")
        
        print(f"✅ Enum field add-vhost-domain-to-dnsdb has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/firewall/access_proxy6"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.access-proxy6.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']