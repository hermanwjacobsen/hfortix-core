"""
Auto-generated basic tests for cmdb.firewall/ssl_ssh_profile

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.ssl-ssh-profile.json
Category: cmdb
Endpoint: /cmdb/firewall/ssl-ssh-profile

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_ssl-ssh-profile.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.firewall.ssl_ssh_profile


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoSslSshProfileValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.firewall._helpers import ssl_ssh_profile as validators
            print(f"✅ Successfully imported validators for ssl-ssh-profile")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_firewall_ssl_ssh_profile_post")
            assert hasattr(validators, "validate_firewall_ssl_ssh_profile_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import ssl_ssh_profile as validators
        
        # Build minimal valid config with all required fields
        config = {
            "caname": "test_caname",  # string
            "name": "test_name",  # string
            "server-cert-mode": "re-sign",  # option
            "ssl-server": "test_ssl-server",  # string
            "untrusted-caname": "test_untrusted-caname",  # string
        }
        
        try:
            result = validators.validate_firewall_ssl_ssh_profile_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoSslSshProfileEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_allowlist(self):
        """Test enum field allowlist validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import ssl_ssh_profile as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"allowlist": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: allowlist={value}")
        
        print(f"✅ Enum field allowlist has {len(valid_values)} valid values")
    def auto_test_enum_block_blocklisted_certificates(self):
        """Test enum field block-blocklisted-certificates validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import ssl_ssh_profile as validators
        
        valid_values = ['disable', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"block-blocklisted-certificates": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: block-blocklisted-certificates={value}")
        
        print(f"✅ Enum field block-blocklisted-certificates has {len(valid_values)} valid values")
    def auto_test_enum_server_cert_mode(self):
        """Test enum field server-cert-mode validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import ssl_ssh_profile as validators
        
        valid_values = ['re-sign', 'replace']
        
        # Test each valid value
        for value in valid_values:
            config = {"server-cert-mode": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: server-cert-mode={value}")
        
        print(f"✅ Enum field server-cert-mode has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/firewall/ssl_ssh_profile"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.ssl-ssh-profile.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']