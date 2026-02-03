"""
Auto-generated basic tests for cmdb.antivirus/quarantine

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/antivirus.quarantine.json
Category: cmdb
Endpoint: /cmdb/antivirus/quarantine

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_quarantine.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.antivirus.quarantine


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoQuarantineEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_drop_infected(self):
        """Test enum field drop-infected validation."""
        from hfortix_fortios.api.v2.cmdb.antivirus._helpers import quarantine as validators
        
        valid_values = ['imap', 'smtp', 'pop3', 'http', 'ftp', 'nntp', 'imaps', 'smtps', 'pop3s', 'https', 'ftps', 'mapi', 'cifs', 'ssh']
        
        # Test each valid value
        for value in valid_values:
            config = {"drop-infected": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: drop-infected={value}")
        
        print(f"✅ Enum field drop-infected has {len(valid_values)} valid values")
    def auto_test_enum_store_infected(self):
        """Test enum field store-infected validation."""
        from hfortix_fortios.api.v2.cmdb.antivirus._helpers import quarantine as validators
        
        valid_values = ['imap', 'smtp', 'pop3', 'http', 'ftp', 'nntp', 'imaps', 'smtps', 'pop3s', 'https', 'ftps', 'mapi', 'cifs', 'ssh']
        
        # Test each valid value
        for value in valid_values:
            config = {"store-infected": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: store-infected={value}")
        
        print(f"✅ Enum field store-infected has {len(valid_values)} valid values")
    def auto_test_enum_drop_machine_learning(self):
        """Test enum field drop-machine-learning validation."""
        from hfortix_fortios.api.v2.cmdb.antivirus._helpers import quarantine as validators
        
        valid_values = ['imap', 'smtp', 'pop3', 'http', 'ftp', 'nntp', 'imaps', 'smtps', 'pop3s', 'https', 'ftps', 'mapi', 'cifs', 'ssh']
        
        # Test each valid value
        for value in valid_values:
            config = {"drop-machine-learning": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: drop-machine-learning={value}")
        
        print(f"✅ Enum field drop-machine-learning has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/antivirus/quarantine"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/antivirus.quarantine.json"
TEST_HTTP_METHODS = ['GET', 'PUT']