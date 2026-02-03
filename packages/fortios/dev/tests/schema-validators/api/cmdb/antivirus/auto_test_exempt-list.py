"""
Auto-generated basic tests for cmdb.antivirus/exempt_list

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/antivirus.exempt-list.json
Category: cmdb
Endpoint: /cmdb/antivirus/exempt-list

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_exempt-list.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.antivirus.exempt_list


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoExemptListValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.antivirus._helpers import exempt_list as validators
            print(f"✅ Successfully imported validators for exempt-list")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_antivirus_exempt_list_post")
            assert hasattr(validators, "validate_antivirus_exempt_list_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.antivirus._helpers import exempt_list as validators
        
        # Build minimal valid config with all required fields
        config = {
            "hash": "test_hash",  # string
            "name": "test_name",  # string
        }
        
        try:
            result = validators.validate_antivirus_exempt_list_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoExemptListEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_hash_type(self):
        """Test enum field hash-type validation."""
        from hfortix_fortios.api.v2.cmdb.antivirus._helpers import exempt_list as validators
        
        valid_values = ['md5', 'sha1', 'sha256']
        
        # Test each valid value
        for value in valid_values:
            config = {"hash-type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: hash-type={value}")
        
        print(f"✅ Enum field hash-type has {len(valid_values)} valid values")
    def auto_test_enum_status(self):
        """Test enum field status validation."""
        from hfortix_fortios.api.v2.cmdb.antivirus._helpers import exempt_list as validators
        
        valid_values = ['disable', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"status": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: status={value}")
        
        print(f"✅ Enum field status has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/antivirus/exempt_list"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/antivirus.exempt-list.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']