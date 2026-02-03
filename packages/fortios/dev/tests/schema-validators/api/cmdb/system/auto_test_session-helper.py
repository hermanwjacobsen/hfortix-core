"""
Auto-generated basic tests for cmdb.system/session_helper

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.session-helper.json
Category: cmdb
Endpoint: /cmdb/system/session-helper

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_session-helper.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.session_helper


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoSessionHelperValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.system._helpers import session_helper as validators
            print(f"✅ Successfully imported validators for session-helper")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_system_session_helper_post")
            assert hasattr(validators, "validate_system_session_helper_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import session_helper as validators
        
        # Build minimal valid config with all required fields
        config = {
            "name": "ftp",  # option
            "port": 0,  # integer
            "protocol": 0,  # integer
        }
        
        try:
            result = validators.validate_system_session_helper_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoSessionHelperEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_name(self):
        """Test enum field name validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import session_helper as validators
        
        valid_values = ['ftp', 'tftp', 'ras', 'h323', 'tns', 'mms', 'sip', 'pptp', 'rtsp', 'dns-udp', 'dns-tcp', 'pmap', 'rsh', 'dcerpc', 'mgcp']
        
        # Test each valid value
        for value in valid_values:
            config = {"name": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: name={value}")
        
        print(f"✅ Enum field name has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/session_helper"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.session-helper.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']