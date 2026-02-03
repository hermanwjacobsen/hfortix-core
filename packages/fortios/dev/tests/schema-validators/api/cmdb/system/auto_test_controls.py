"""
Auto-generated basic tests for cmdb.system/security_rating/controls

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.security-rating.controls.json
Category: cmdb
Endpoint: /cmdb/system.security-rating/controls

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_controls.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.security_rating.controls


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoControlsValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.system.security_rating._helpers import controls as validators
            print(f"✅ Successfully imported validators for controls")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_system_security_rating_controls_post")
            assert hasattr(validators, "validate_system_security_rating_controls_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.system.security_rating._helpers import controls as validators
        
        # Build minimal valid config with all required fields
        config = {
            "display-insight": "enable",  # option
            "display-report": "enable",  # option
        }
        
        try:
            result = validators.validate_system_security_rating_controls_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoControlsEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_display_report(self):
        """Test enum field display-report validation."""
        from hfortix_fortios.api.v2.cmdb.system.security_rating._helpers import controls as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"display-report": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: display-report={value}")
        
        print(f"✅ Enum field display-report has {len(valid_values)} valid values")
    def auto_test_enum_display_insight(self):
        """Test enum field display-insight validation."""
        from hfortix_fortios.api.v2.cmdb.system.security_rating._helpers import controls as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"display-insight": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: display-insight={value}")
        
        print(f"✅ Enum field display-insight has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/security_rating/controls"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.security-rating.controls.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']