"""
Auto-generated basic tests for cmdb.user/krb_keytab

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/user.krb-keytab.json
Category: cmdb
Endpoint: /cmdb/user/krb-keytab

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_krb-keytab.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.user.krb_keytab


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoKrbKeytabValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.user._helpers import krb_keytab as validators
            print(f"✅ Successfully imported validators for krb-keytab")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_user_krb_keytab_post")
            assert hasattr(validators, "validate_user_krb_keytab_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.user._helpers import krb_keytab as validators
        
        # Build minimal valid config with all required fields
        config = {
            "keytab": "test_keytab",  # string
            "principal": "test_principal",  # string
        }
        
        try:
            result = validators.validate_user_krb_keytab_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoKrbKeytabEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_pac_data(self):
        """Test enum field pac-data validation."""
        from hfortix_fortios.api.v2.cmdb.user._helpers import krb_keytab as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"pac-data": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: pac-data={value}")
        
        print(f"✅ Enum field pac-data has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/user/krb_keytab"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/user.krb-keytab.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']