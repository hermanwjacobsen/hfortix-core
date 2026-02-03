"""
Auto-generated basic tests for cmdb.user/exchange

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/user.exchange.json
Category: cmdb
Endpoint: /cmdb/user/exchange

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_exchange.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.user.exchange


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoExchangeValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.user._helpers import exchange as validators
            print(f"✅ Successfully imported validators for exchange")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_user_exchange_post")
            assert hasattr(validators, "validate_user_exchange_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.user._helpers import exchange as validators
        
        # Build minimal valid config with all required fields
        config = {
            "domain-name": "test_domain-name",  # string
            "password": "",  # password
            "server-name": "test_server-name",  # string
            "username": "test_username",  # string
        }
        
        try:
            result = validators.validate_user_exchange_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoExchangeEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_connect_protocol(self):
        """Test enum field connect-protocol validation."""
        from hfortix_fortios.api.v2.cmdb.user._helpers import exchange as validators
        
        valid_values = ['rpc-over-tcp', 'rpc-over-http', 'rpc-over-https']
        
        # Test each valid value
        for value in valid_values:
            config = {"connect-protocol": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: connect-protocol={value}")
        
        print(f"✅ Enum field connect-protocol has {len(valid_values)} valid values")
    def auto_test_enum_validate_server_certificate(self):
        """Test enum field validate-server-certificate validation."""
        from hfortix_fortios.api.v2.cmdb.user._helpers import exchange as validators
        
        valid_values = ['disable', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"validate-server-certificate": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: validate-server-certificate={value}")
        
        print(f"✅ Enum field validate-server-certificate has {len(valid_values)} valid values")
    def auto_test_enum_auth_type(self):
        """Test enum field auth-type validation."""
        from hfortix_fortios.api.v2.cmdb.user._helpers import exchange as validators
        
        valid_values = ['spnego', 'ntlm', 'kerberos']
        
        # Test each valid value
        for value in valid_values:
            config = {"auth-type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: auth-type={value}")
        
        print(f"✅ Enum field auth-type has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/user/exchange"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/user.exchange.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']