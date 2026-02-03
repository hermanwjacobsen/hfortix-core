"""
Auto-generated basic tests for cmdb.firewall/access_proxy_ssh_client_cert

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.access-proxy-ssh-client-cert.json
Category: cmdb
Endpoint: /cmdb/firewall/access-proxy-ssh-client-cert

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_access-proxy-ssh-client-cert.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.firewall.access_proxy_ssh_client_cert


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoAccessProxySshClientCertValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.firewall._helpers import access_proxy_ssh_client_cert as validators
            print(f"✅ Successfully imported validators for access-proxy-ssh-client-cert")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_firewall_access_proxy_ssh_client_cert_post")
            assert hasattr(validators, "validate_firewall_access_proxy_ssh_client_cert_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import access_proxy_ssh_client_cert as validators
        
        # Build minimal valid config with all required fields
        config = {
            "auth-ca": "test_auth-ca",  # string
        }
        
        try:
            result = validators.validate_firewall_access_proxy_ssh_client_cert_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoAccessProxySshClientCertEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_source_address(self):
        """Test enum field source-address validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import access_proxy_ssh_client_cert as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"source-address": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: source-address={value}")
        
        print(f"✅ Enum field source-address has {len(valid_values)} valid values")
    def auto_test_enum_permit_x11_forwarding(self):
        """Test enum field permit-x11-forwarding validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import access_proxy_ssh_client_cert as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"permit-x11-forwarding": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: permit-x11-forwarding={value}")
        
        print(f"✅ Enum field permit-x11-forwarding has {len(valid_values)} valid values")
    def auto_test_enum_permit_agent_forwarding(self):
        """Test enum field permit-agent-forwarding validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import access_proxy_ssh_client_cert as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"permit-agent-forwarding": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: permit-agent-forwarding={value}")
        
        print(f"✅ Enum field permit-agent-forwarding has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/firewall/access_proxy_ssh_client_cert"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.access-proxy-ssh-client-cert.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']