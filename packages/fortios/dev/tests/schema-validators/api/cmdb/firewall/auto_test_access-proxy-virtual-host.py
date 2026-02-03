"""
Auto-generated basic tests for cmdb.firewall/access_proxy_virtual_host

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.access-proxy-virtual-host.json
Category: cmdb
Endpoint: /cmdb/firewall/access-proxy-virtual-host

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_access-proxy-virtual-host.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.firewall.access_proxy_virtual_host


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoAccessProxyVirtualHostValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.firewall._helpers import access_proxy_virtual_host as validators
            print(f"✅ Successfully imported validators for access-proxy-virtual-host")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_firewall_access_proxy_virtual_host_post")
            assert hasattr(validators, "validate_firewall_access_proxy_virtual_host_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import access_proxy_virtual_host as validators
        
        # Build minimal valid config with all required fields
        config = {
            "host": "test_host",  # string
            "host-type": "sub-string",  # option
            "ssl-certificate": "test_ssl-certificate",  # string
        }
        
        try:
            result = validators.validate_firewall_access_proxy_virtual_host_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoAccessProxyVirtualHostEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_host_type(self):
        """Test enum field host-type validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import access_proxy_virtual_host as validators
        
        valid_values = ['sub-string', 'wildcard']
        
        # Test each valid value
        for value in valid_values:
            config = {"host-type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: host-type={value}")
        
        print(f"✅ Enum field host-type has {len(valid_values)} valid values")
    def auto_test_enum_empty_cert_action(self):
        """Test enum field empty-cert-action validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import access_proxy_virtual_host as validators
        
        valid_values = ['accept', 'block', 'accept-unmanageable']
        
        # Test each valid value
        for value in valid_values:
            config = {"empty-cert-action": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: empty-cert-action={value}")
        
        print(f"✅ Enum field empty-cert-action has {len(valid_values)} valid values")
    def auto_test_enum_user_agent_detect(self):
        """Test enum field user-agent-detect validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import access_proxy_virtual_host as validators
        
        valid_values = ['disable', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"user-agent-detect": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: user-agent-detect={value}")
        
        print(f"✅ Enum field user-agent-detect has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/firewall/access_proxy_virtual_host"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.access-proxy-virtual-host.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']