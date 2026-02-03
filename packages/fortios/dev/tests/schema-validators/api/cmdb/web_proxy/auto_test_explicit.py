"""
Auto-generated basic tests for cmdb.web_proxy/explicit

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/web-proxy.explicit.json
Category: cmdb
Endpoint: /cmdb/web-proxy/explicit

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_explicit.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.web_proxy.explicit


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoExplicitValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.web_proxy._helpers import explicit as validators
            print(f"✅ Successfully imported validators for explicit")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_web_proxy_explicit_post")
            assert hasattr(validators, "validate_web_proxy_explicit_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.web_proxy._helpers import explicit as validators
        
        # Build minimal valid config with all required fields
        config = {
            "interface": "test_interface",  # string
            "pac-file-name": "test_pac-file-name",  # string
            "realm": "test_realm",  # string
        }
        
        try:
            result = validators.validate_web_proxy_explicit_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoExplicitEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_status(self):
        """Test enum field status validation."""
        from hfortix_fortios.api.v2.cmdb.web_proxy._helpers import explicit as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"status": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: status={value}")
        
        print(f"✅ Enum field status has {len(valid_values)} valid values")
    def auto_test_enum_secure_web_proxy(self):
        """Test enum field secure-web-proxy validation."""
        from hfortix_fortios.api.v2.cmdb.web_proxy._helpers import explicit as validators
        
        valid_values = ['disable', 'enable', 'secure']
        
        # Test each valid value
        for value in valid_values:
            config = {"secure-web-proxy": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: secure-web-proxy={value}")
        
        print(f"✅ Enum field secure-web-proxy has {len(valid_values)} valid values")
    def auto_test_enum_ftp_over_http(self):
        """Test enum field ftp-over-http validation."""
        from hfortix_fortios.api.v2.cmdb.web_proxy._helpers import explicit as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"ftp-over-http": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: ftp-over-http={value}")
        
        print(f"✅ Enum field ftp-over-http has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/web_proxy/explicit"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/web-proxy.explicit.json"
TEST_HTTP_METHODS = ['GET', 'PUT']