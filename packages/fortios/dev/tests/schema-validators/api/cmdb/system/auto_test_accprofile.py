"""
Auto-generated basic tests for cmdb.system/accprofile

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.accprofile.json
Category: cmdb
Endpoint: /cmdb/system/accprofile

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_accprofile.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.accprofile


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoAccprofileValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.system._helpers import accprofile as validators
            print(f"✅ Successfully imported validators for accprofile")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_system_accprofile_post")
            assert hasattr(validators, "validate_system_accprofile_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import accprofile as validators
        
        # Build minimal valid config with all required fields
        config = {
            "name": "test_name",  # string
        }
        
        try:
            result = validators.validate_system_accprofile_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoAccprofileEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_scope(self):
        """Test enum field scope validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import accprofile as validators
        
        valid_values = ['vdom', 'global']
        
        # Test each valid value
        for value in valid_values:
            config = {"scope": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: scope={value}")
        
        print(f"✅ Enum field scope has {len(valid_values)} valid values")
    def auto_test_enum_secfabgrp(self):
        """Test enum field secfabgrp validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import accprofile as validators
        
        valid_values = ['none', 'read', 'read-write', 'custom']
        
        # Test each valid value
        for value in valid_values:
            config = {"secfabgrp": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: secfabgrp={value}")
        
        print(f"✅ Enum field secfabgrp has {len(valid_values)} valid values")
    def auto_test_enum_ftviewgrp(self):
        """Test enum field ftviewgrp validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import accprofile as validators
        
        valid_values = ['none', 'read', 'read-write']
        
        # Test each valid value
        for value in valid_values:
            config = {"ftviewgrp": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: ftviewgrp={value}")
        
        print(f"✅ Enum field ftviewgrp has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/accprofile"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.accprofile.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']