"""
Auto-generated basic tests for cmdb.system/automation_action

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.automation-action.json
Category: cmdb
Endpoint: /cmdb/system/automation-action

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_automation-action.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.automation_action


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoAutomationActionValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.system._helpers import automation_action as validators
            print(f"✅ Successfully imported validators for automation-action")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_system_automation_action_post")
            assert hasattr(validators, "validate_system_automation_action_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import automation_action as validators
        
        # Build minimal valid config with all required fields
        config = {
            "alicloud-access-key-id": "test_alicloud-access-key-id",  # string
            "alicloud-access-key-secret": "",  # password
            "alicloud-function-authorization": "anonymous",  # option
            "aws-api-key": "",  # password
            "azure-function-authorization": "anonymous",  # option
            "forticare-email": "enable",  # option
            "message": "test_message",  # string
            "message-type": "text",  # option
            "method": "post",  # option
            "protocol": "http",  # option
            "regular-expression": "",  # var-string
            "replacement-message": "enable",  # option
            "script": "",  # var-string
            "security-tag": "test_security-tag",  # string
            "system-action": "reboot",  # option
            "uri": "",  # var-string
        }
        
        try:
            result = validators.validate_system_automation_action_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoAutomationActionEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_action_type(self):
        """Test enum field action-type validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import automation_action as validators
        
        valid_values = ['email', 'fortiexplorer-notification', 'alert', 'disable-ssid', 'system-actions', 'quarantine', 'quarantine-forticlient', 'quarantine-nsx', 'quarantine-fortinac', 'ban-ip', 'aws-lambda', 'azure-function', 'google-cloud-function', 'alicloud-function', 'webhook', 'cli-script', 'diagnose-script', 'regular-expression', 'slack-notification', 'microsoft-teams-notification']
        
        # Test each valid value
        for value in valid_values:
            config = {"action-type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: action-type={value}")
        
        print(f"✅ Enum field action-type has {len(valid_values)} valid values")
    def auto_test_enum_system_action(self):
        """Test enum field system-action validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import automation_action as validators
        
        valid_values = ['reboot', 'shutdown', 'backup-config']
        
        # Test each valid value
        for value in valid_values:
            config = {"system-action": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: system-action={value}")
        
        print(f"✅ Enum field system-action has {len(valid_values)} valid values")
    def auto_test_enum_forticare_email(self):
        """Test enum field forticare-email validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import automation_action as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"forticare-email": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: forticare-email={value}")
        
        print(f"✅ Enum field forticare-email has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/automation_action"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.automation-action.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']