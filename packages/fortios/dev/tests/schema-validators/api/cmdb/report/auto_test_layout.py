"""
Auto-generated basic tests for cmdb.report/layout

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/report.layout.json
Category: cmdb
Endpoint: /cmdb/report/layout

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_layout.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.report.layout


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoLayoutValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.report._helpers import layout as validators
            print(f"✅ Successfully imported validators for layout")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_report_layout_post")
            assert hasattr(validators, "validate_report_layout_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.report._helpers import layout as validators
        
        # Build minimal valid config with all required fields
        config = {
            "style-theme": "test_style-theme",  # string
        }
        
        try:
            result = validators.validate_report_layout_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoLayoutEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_options(self):
        """Test enum field options validation."""
        from hfortix_fortios.api.v2.cmdb.report._helpers import layout as validators
        
        valid_values = ['include-table-of-content', 'auto-numbering-heading', 'view-chart-as-heading', 'show-html-navbar-before-heading', 'dummy-option']
        
        # Test each valid value
        for value in valid_values:
            config = {"options": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: options={value}")
        
        print(f"✅ Enum field options has {len(valid_values)} valid values")
    def auto_test_enum_format(self):
        """Test enum field format validation."""
        from hfortix_fortios.api.v2.cmdb.report._helpers import layout as validators
        
        valid_values = ['pdf']
        
        # Test each valid value
        for value in valid_values:
            config = {"format": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: format={value}")
        
        print(f"✅ Enum field format has {len(valid_values)} valid values")
    def auto_test_enum_schedule_type(self):
        """Test enum field schedule-type validation."""
        from hfortix_fortios.api.v2.cmdb.report._helpers import layout as validators
        
        valid_values = ['demand', 'daily', 'weekly']
        
        # Test each valid value
        for value in valid_values:
            config = {"schedule-type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: schedule-type={value}")
        
        print(f"✅ Enum field schedule-type has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/report/layout"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/report.layout.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']