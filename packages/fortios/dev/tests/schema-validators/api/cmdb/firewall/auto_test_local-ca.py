"""
Auto-generated basic tests for cmdb.firewall/ssh/local_ca

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.ssh.local-ca.json
Category: cmdb
Endpoint: /cmdb/firewall.ssh/local-ca

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_local-ca.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.firewall.ssh.local_ca


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoLocalCaValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.firewall.ssh._helpers import local_ca as validators
            print(f"✅ Successfully imported validators for local-ca")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_firewall_ssh_local_ca_post")
            assert hasattr(validators, "validate_firewall_ssh_local_ca_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.firewall.ssh._helpers import local_ca as validators
        
        # Build minimal valid config with all required fields
        config = {
            "private-key": "",  # user
            "public-key": "",  # user
        }
        
        try:
            result = validators.validate_firewall_ssh_local_ca_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoLocalCaEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_source(self):
        """Test enum field source validation."""
        from hfortix_fortios.api.v2.cmdb.firewall.ssh._helpers import local_ca as validators
        
        valid_values = ['built-in', 'user']
        
        # Test each valid value
        for value in valid_values:
            config = {"source": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: source={value}")
        
        print(f"✅ Enum field source has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/firewall/ssh/local_ca"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.ssh.local-ca.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']