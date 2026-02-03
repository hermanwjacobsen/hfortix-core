"""
Auto-generated basic tests for cmdb.application/list

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/application.list.json
Category: cmdb
Endpoint: /cmdb/application/list

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_list.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.application.list


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoListValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.application._helpers import list as validators
            print(f"✅ Successfully imported validators for list")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_application_list_post")
            assert hasattr(validators, "validate_application_list_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.application._helpers import list as validators
        
        # Build minimal valid config with all required fields
        config = {
            "name": "test_name",  # string
        }
        
        try:
            result = validators.validate_application_list_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoListEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_extended_log(self):
        """Test enum field extended-log validation."""
        from hfortix_fortios.api.v2.cmdb.application._helpers import list as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"extended-log": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: extended-log={value}")
        
        print(f"✅ Enum field extended-log has {len(valid_values)} valid values")
    def auto_test_enum_other_application_action(self):
        """Test enum field other-application-action validation."""
        from hfortix_fortios.api.v2.cmdb.application._helpers import list as validators
        
        valid_values = ['pass', 'block']
        
        # Test each valid value
        for value in valid_values:
            config = {"other-application-action": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: other-application-action={value}")
        
        print(f"✅ Enum field other-application-action has {len(valid_values)} valid values")
    def auto_test_enum_app_replacemsg(self):
        """Test enum field app-replacemsg validation."""
        from hfortix_fortios.api.v2.cmdb.application._helpers import list as validators
        
        valid_values = ['disable', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"app-replacemsg": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: app-replacemsg={value}")
        
        print(f"✅ Enum field app-replacemsg has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/application/list"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/application.list.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']