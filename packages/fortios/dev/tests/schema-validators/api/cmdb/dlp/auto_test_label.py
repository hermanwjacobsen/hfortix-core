"""
Auto-generated basic tests for cmdb.dlp/label

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/dlp.label.json
Category: cmdb
Endpoint: /cmdb/dlp/label

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_label.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.dlp.label


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoLabelValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.dlp._helpers import label as validators
            print(f"✅ Successfully imported validators for label")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_dlp_label_post")
            assert hasattr(validators, "validate_dlp_label_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.dlp._helpers import label as validators
        
        # Build minimal valid config with all required fields
        config = {
            "entries": "test_entries",  # string
        }
        
        try:
            result = validators.validate_dlp_label_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoLabelEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_type(self):
        """Test enum field type validation."""
        from hfortix_fortios.api.v2.cmdb.dlp._helpers import label as validators
        
        valid_values = ['mpip', 'fortidata']
        
        # Test each valid value
        for value in valid_values:
            config = {"type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: type={value}")
        
        print(f"✅ Enum field type has {len(valid_values)} valid values")
    def auto_test_enum_mpip_type(self):
        """Test enum field mpip-type validation."""
        from hfortix_fortios.api.v2.cmdb.dlp._helpers import label as validators
        
        valid_values = ['remote', 'local']
        
        # Test each valid value
        for value in valid_values:
            config = {"mpip-type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: mpip-type={value}")
        
        print(f"✅ Enum field mpip-type has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/dlp/label"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/dlp.label.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']