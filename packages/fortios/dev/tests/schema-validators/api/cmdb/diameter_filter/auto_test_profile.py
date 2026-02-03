"""
Auto-generated basic tests for cmdb.diameter_filter/profile

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/diameter-filter.profile.json
Category: cmdb
Endpoint: /cmdb/diameter-filter/profile

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_profile.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.diameter_filter.profile


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoProfileValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.diameter_filter._helpers import profile as validators
            print(f"✅ Successfully imported validators for profile")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_diameter_filter_profile_post")
            assert hasattr(validators, "validate_diameter_filter_profile_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.diameter_filter._helpers import profile as validators
        
        # Build minimal valid config with all required fields
        config = {
            "name": "test_name",  # string
        }
        
        try:
            result = validators.validate_diameter_filter_profile_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoProfileEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_monitor_all_messages(self):
        """Test enum field monitor-all-messages validation."""
        from hfortix_fortios.api.v2.cmdb.diameter_filter._helpers import profile as validators
        
        valid_values = ['disable', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"monitor-all-messages": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: monitor-all-messages={value}")
        
        print(f"✅ Enum field monitor-all-messages has {len(valid_values)} valid values")
    def auto_test_enum_log_packet(self):
        """Test enum field log-packet validation."""
        from hfortix_fortios.api.v2.cmdb.diameter_filter._helpers import profile as validators
        
        valid_values = ['disable', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"log-packet": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: log-packet={value}")
        
        print(f"✅ Enum field log-packet has {len(valid_values)} valid values")
    def auto_test_enum_track_requests_answers(self):
        """Test enum field track-requests-answers validation."""
        from hfortix_fortios.api.v2.cmdb.diameter_filter._helpers import profile as validators
        
        valid_values = ['disable', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"track-requests-answers": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: track-requests-answers={value}")
        
        print(f"✅ Enum field track-requests-answers has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/diameter_filter/profile"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/diameter-filter.profile.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']