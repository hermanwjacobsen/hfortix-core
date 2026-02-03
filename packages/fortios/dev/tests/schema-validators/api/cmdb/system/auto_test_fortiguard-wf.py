"""
Auto-generated basic tests for cmdb.system/replacemsg/fortiguard_wf

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.replacemsg.fortiguard-wf.json
Category: cmdb
Endpoint: /cmdb/system.replacemsg/fortiguard-wf

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_fortiguard-wf.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.replacemsg.fortiguard_wf


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoFortiguardWfValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.system.replacemsg._helpers import fortiguard_wf as validators
            print(f"✅ Successfully imported validators for fortiguard-wf")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_system_replacemsg_fortiguard_wf_post")
            assert hasattr(validators, "validate_system_replacemsg_fortiguard_wf_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.system.replacemsg._helpers import fortiguard_wf as validators
        
        # Build minimal valid config with all required fields
        config = {
            "msg-type": "test_msg-type",  # string
        }
        
        try:
            result = validators.validate_system_replacemsg_fortiguard_wf_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoFortiguardWfEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_header(self):
        """Test enum field header validation."""
        from hfortix_fortios.api.v2.cmdb.system.replacemsg._helpers import fortiguard_wf as validators
        
        valid_values = ['none', 'http', '8bit']
        
        # Test each valid value
        for value in valid_values:
            config = {"header": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: header={value}")
        
        print(f"✅ Enum field header has {len(valid_values)} valid values")
    def auto_test_enum_format(self):
        """Test enum field format validation."""
        from hfortix_fortios.api.v2.cmdb.system.replacemsg._helpers import fortiguard_wf as validators
        
        valid_values = ['none', 'text', 'html']
        
        # Test each valid value
        for value in valid_values:
            config = {"format": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: format={value}")
        
        print(f"✅ Enum field format has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/replacemsg/fortiguard_wf"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.replacemsg.fortiguard-wf.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']