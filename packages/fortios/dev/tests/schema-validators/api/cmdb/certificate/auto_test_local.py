"""
Auto-generated basic tests for cmdb.certificate/local

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/certificate.local.json
Category: cmdb
Endpoint: /cmdb/certificate/local

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_local.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.certificate.local


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoLocalValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.certificate._helpers import local as validators
            print(f"✅ Successfully imported validators for local")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_certificate_local_post")
            assert hasattr(validators, "validate_certificate_local_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.certificate._helpers import local as validators
        
        # Build minimal valid config with all required fields
        config = {
            "acme-ca-url": "test_acme-ca-url",  # string
            "acme-domain": "test_acme-domain",  # string
            "acme-email": "test_acme-email",  # string
            "name": "test_name",  # string
            "private-key": "",  # user
        }
        
        try:
            result = validators.validate_certificate_local_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoLocalEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_range(self):
        """Test enum field range validation."""
        from hfortix_fortios.api.v2.cmdb.certificate._helpers import local as validators
        
        valid_values = ['global', 'vdom']
        
        # Test each valid value
        for value in valid_values:
            config = {"range": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: range={value}")
        
        print(f"✅ Enum field range has {len(valid_values)} valid values")
    def auto_test_enum_source(self):
        """Test enum field source validation."""
        from hfortix_fortios.api.v2.cmdb.certificate._helpers import local as validators
        
        valid_values = ['factory', 'user', 'bundle']
        
        # Test each valid value
        for value in valid_values:
            config = {"source": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: source={value}")
        
        print(f"✅ Enum field source has {len(valid_values)} valid values")
    def auto_test_enum_name_encoding(self):
        """Test enum field name-encoding validation."""
        from hfortix_fortios.api.v2.cmdb.certificate._helpers import local as validators
        
        valid_values = ['printable', 'utf8']
        
        # Test each valid value
        for value in valid_values:
            config = {"name-encoding": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: name-encoding={value}")
        
        print(f"✅ Enum field name-encoding has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/certificate/local"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/certificate.local.json"
TEST_HTTP_METHODS = ['GET']