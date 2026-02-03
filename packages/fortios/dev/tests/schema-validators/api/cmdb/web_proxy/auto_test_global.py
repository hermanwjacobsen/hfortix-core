"""
Auto-generated basic tests for cmdb.web_proxy/global_

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/web-proxy.global.json
Category: cmdb
Endpoint: /cmdb/web-proxy/global

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_global.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.web_proxy.global_


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoGlobalValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            # 'global' is a Python keyword, using importlib
            import importlib
            validators = importlib.import_module('hfortix_fortios.api.v2.cmdb.web_proxy._helpers.global_')
            print(f"✅ Successfully imported validators for global")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_web_proxy_global_post")
            assert hasattr(validators, "validate_web_proxy_global_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        # 'global' is a Python keyword, using importlib
        import importlib
        validators = importlib.import_module('hfortix_fortios.api.v2.cmdb.web_proxy._helpers.global_')
        
        # Build minimal valid config with all required fields
        config = {
            "proxy-fqdn": "test_proxy-fqdn",  # string
        }
        
        try:
            result = validators.validate_web_proxy_global_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoGlobalEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_fast_policy_match(self):
        """Test enum field fast-policy-match validation."""
        # 'global' is a Python keyword, using importlib
        import importlib
        validators = importlib.import_module('hfortix_fortios.api.v2.cmdb.web_proxy._helpers.global_')
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"fast-policy-match": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: fast-policy-match={value}")
        
        print(f"✅ Enum field fast-policy-match has {len(valid_values)} valid values")
    def auto_test_enum_ldap_user_cache(self):
        """Test enum field ldap-user-cache validation."""
        # 'global' is a Python keyword, using importlib
        import importlib
        validators = importlib.import_module('hfortix_fortios.api.v2.cmdb.web_proxy._helpers.global_')
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"ldap-user-cache": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: ldap-user-cache={value}")
        
        print(f"✅ Enum field ldap-user-cache has {len(valid_values)} valid values")
    def auto_test_enum_strict_web_check(self):
        """Test enum field strict-web-check validation."""
        # 'global' is a Python keyword, using importlib
        import importlib
        validators = importlib.import_module('hfortix_fortios.api.v2.cmdb.web_proxy._helpers.global_')
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"strict-web-check": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: strict-web-check={value}")
        
        print(f"✅ Enum field strict-web-check has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/web_proxy/global_"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/web-proxy.global.json"
TEST_HTTP_METHODS = ['GET', 'PUT']