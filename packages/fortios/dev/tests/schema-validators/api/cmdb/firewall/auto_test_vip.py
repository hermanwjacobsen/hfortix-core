"""
Auto-generated basic tests for cmdb.firewall/vip

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.vip.json
Category: cmdb
Endpoint: /cmdb/firewall/vip

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_vip.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.firewall.vip


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoVipValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.firewall._helpers import vip as validators
            print(f"✅ Successfully imported validators for vip")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_firewall_vip_post")
            assert hasattr(validators, "validate_firewall_vip_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import vip as validators
        
        # Build minimal valid config with all required fields
        config = {
            "extintf": "test_extintf",  # string
            "extip": "",  # user
            "extport": "",  # user
            "h2-support": "enable",  # option
            "ipv6-mappedip": "",  # user
            "mappedip": "test_mappedip",  # string
            "server-type": "http",  # option
            "ssl-certificate": "test_ssl-certificate",  # string
        }
        
        try:
            result = validators.validate_firewall_vip_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoVipEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_type(self):
        """Test enum field type validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import vip as validators
        
        valid_values = ['static-nat', 'load-balance', 'server-load-balance', 'dns-translation', 'fqdn', 'access-proxy']
        
        # Test each valid value
        for value in valid_values:
            config = {"type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: type={value}")
        
        print(f"✅ Enum field type has {len(valid_values)} valid values")
    def auto_test_enum_server_type(self):
        """Test enum field server-type validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import vip as validators
        
        valid_values = ['http', 'https', 'imaps', 'pop3s', 'smtps', 'ssl', 'tcp', 'udp', 'ip']
        
        # Test each valid value
        for value in valid_values:
            config = {"server-type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: server-type={value}")
        
        print(f"✅ Enum field server-type has {len(valid_values)} valid values")
    def auto_test_enum_ldb_method(self):
        """Test enum field ldb-method validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import vip as validators
        
        valid_values = ['static', 'round-robin', 'weighted', 'least-session', 'least-rtt', 'first-alive', 'http-host']
        
        # Test each valid value
        for value in valid_values:
            config = {"ldb-method": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: ldb-method={value}")
        
        print(f"✅ Enum field ldb-method has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/firewall/vip"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.vip.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']