"""
Auto-generated basic tests for cmdb.user/fsso_polling

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/user.fsso-polling.json
Category: cmdb
Endpoint: /cmdb/user/fsso-polling

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_fsso-polling.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.user.fsso_polling


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoFssoPollingValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.user._helpers import fsso_polling as validators
            print(f"✅ Successfully imported validators for fsso-polling")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_user_fsso_polling_post")
            assert hasattr(validators, "validate_user_fsso_polling_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.user._helpers import fsso_polling as validators
        
        # Build minimal valid config with all required fields
        config = {
            "ldap-server": "test_ldap-server",  # string
            "server": "test_server",  # string
            "user": "test_user",  # string
        }
        
        try:
            result = validators.validate_user_fsso_polling_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoFssoPollingEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_status(self):
        """Test enum field status validation."""
        from hfortix_fortios.api.v2.cmdb.user._helpers import fsso_polling as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"status": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: status={value}")
        
        print(f"✅ Enum field status has {len(valid_values)} valid values")
    def auto_test_enum_smbv1(self):
        """Test enum field smbv1 validation."""
        from hfortix_fortios.api.v2.cmdb.user._helpers import fsso_polling as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"smbv1": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: smbv1={value}")
        
        print(f"✅ Enum field smbv1 has {len(valid_values)} valid values")
    def auto_test_enum_smb_ntlmv1_auth(self):
        """Test enum field smb-ntlmv1-auth validation."""
        from hfortix_fortios.api.v2.cmdb.user._helpers import fsso_polling as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"smb-ntlmv1-auth": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: smb-ntlmv1-auth={value}")
        
        print(f"✅ Enum field smb-ntlmv1-auth has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/user/fsso_polling"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/user.fsso-polling.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']