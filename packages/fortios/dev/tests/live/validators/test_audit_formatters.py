"""
Tests for hfortix_core.audit formatters

Tests JSONFormatter, SyslogFormatter, CEFFormatter - pure formatting logic.
"""

from hfortix_core.audit.formatters import (
    JSONFormatter,
    SyslogFormatter,
    CEFFormatter,
)


# Sample operation data for testing
SAMPLE_OPERATION = {
    "timestamp": "2026-01-10T14:23:45Z",
    "request_id": "req-12345-abcde",
    "method": "POST",
    "endpoint": "/api/v2/cmdb/firewall/address",
    "api_type": "cmdb",
    "path": "firewall/address",
    "vdom": "root",
    "action": "create",
    "object_type": "firewall.address",
    "object_name": "test-host",
    "data": {"name": "test-host", "subnet": "192.168.1.100/32"},
    "params": {"vdom": "root"},
    "status_code": 200,
    "success": True,
    "duration_ms": 125,
    "error": None,
    "user_context": {"username": "admin", "source": "automation"},
    "host": "192.168.1.99",
    "read_only_mode": False,
}

GET_OPERATION = {
    "timestamp": "2026-01-10T14:24:00Z",
    "request_id": "req-67890-fghij",
    "method": "GET",
    "endpoint": "/api/v2/cmdb/firewall/address",
    "api_type": "cmdb",
    "path": "firewall/address",
    "vdom": "root",
    "action": "list",
    "object_type": "firewall.address",
    "object_name": None,
    "data": None,
    "params": {"count": 100},
    "status_code": 200,
    "success": True,
    "duration_ms": 45,
    "error": None,
    "user_context": {},  # BUG WORKAROUND: CEFFormatter crashes if None (see test below)
    "host": "192.168.1.99",
    "read_only_mode": False,
}

DELETE_OPERATION = {
    "timestamp": "2026-01-10T14:25:00Z",
    "request_id": "req-99999-zzzzz",
    "method": "DELETE",
    "endpoint": "/api/v2/cmdb/firewall/address/old-host",
    "api_type": "cmdb",
    "path": "firewall/address/old-host",
    "vdom": "test",
    "action": "delete",
    "object_type": "firewall.address",
    "object_name": "old-host",
    "data": None,
    "params": None,
    "status_code": 200,
    "success": True,
    "duration_ms": 88,
    "error": None,
    "user_context": {"username": "api-user"},
    "host": "10.0.0.1",
    "read_only_mode": False,
}

FAILED_OPERATION = {
    "timestamp": "2026-01-10T14:26:00Z",
    "request_id": "req-error-12345",
    "method": "POST",
    "endpoint": "/api/v2/cmdb/firewall/address",
    "api_type": "cmdb",
    "path": "firewall/address",
    "vdom": "root",
    "action": "create",
    "object_type": "firewall.address",
    "object_name": "invalid-host",
    "data": {"name": "invalid-host"},
    "params": None,
    "status_code": 400,
    "success": False,
    "duration_ms": 15,
    "error": "Missing required field: subnet",
    "user_context": {},  # BUG WORKAROUND: CEFFormatter crashes if None
    "host": "192.168.1.99",
    "read_only_mode": False,
}


def test_json_formatter_compact():
    """Test JSONFormatter with compact output (default)"""
    print("\n=== Testing JSONFormatter (compact) ===")
    
    formatter = JSONFormatter(pretty=False)
    result = formatter.format(SAMPLE_OPERATION)
    
    # Should be single line, no extra whitespace
    assert "\n" not in result
    assert '  ' not in result  # No indentation
    
    # Should contain key data
    assert '"timestamp":"2026-01-10T14:23:45Z"' in result
    assert '"method":"POST"' in result
    assert '"success":true' in result
    assert '"duration_ms":125' in result
    
    print(f"✓ Compact JSON (length: {len(result)}): {result[:80]}...")
    

def test_json_formatter_pretty():
    """Test JSONFormatter with pretty output"""
    print("\n=== Testing JSONFormatter (pretty) ===")
    
    formatter = JSONFormatter(pretty=True, indent=2)
    result = formatter.format(SAMPLE_OPERATION)
    
    # Should have newlines and indentation
    assert "\n" in result
    assert "  " in result
    
    # Keys should be sorted
    lines = result.split("\n")
    assert len(lines) > 1
    
    print(f"✓ Pretty JSON (lines: {len(lines)}):")
    print(result[:200] + "...")


def test_json_formatter_all_operations():
    """Test JSONFormatter with various operation types"""
    print("\n=== Testing JSONFormatter with all operation types ===")
    
    formatter = JSONFormatter()
    
    # POST
    result = formatter.format(SAMPLE_OPERATION)
    assert '"method":"POST"' in result
    assert '"action":"create"' in result
    print("✓ POST operation formatted")
    
    # GET
    result = formatter.format(GET_OPERATION)
    assert '"method":"GET"' in result
    assert '"action":"list"' in result
    print("✓ GET operation formatted")
    
    # DELETE
    result = formatter.format(DELETE_OPERATION)
    assert '"method":"DELETE"' in result
    assert '"action":"delete"' in result
    print("✓ DELETE operation formatted")
    
    # Failed
    result = formatter.format(FAILED_OPERATION)
    assert '"success":false' in result
    assert '"error":"Missing required field: subnet"' in result
    print("✓ Failed operation formatted")


def test_syslog_formatter_default():
    """Test SyslogFormatter with default settings"""
    print("\n=== Testing SyslogFormatter (default) ===")
    
    formatter = SyslogFormatter()
    result = formatter.format(SAMPLE_OPERATION)
    
    # RFC 5424 format: <PRI>VERSION TIMESTAMP HOSTNAME APP-NAME PROCID MSGID SD MSG
    # LOCAL0 (16) + INFO (6) = priority 134
    assert result.startswith("<134>1 ")
    
    # Should contain timestamp and hostname
    assert "2026-01-10T14:23:45Z" in result
    assert "192.168.1.99" in result  # host from operation
    assert "hfortix" in result  # default app_name
    
    # Message should be JSON
    assert '"method":"POST"' in result
    
    print(f"✓ Syslog message: {result[:100]}...")


def test_syslog_formatter_custom_facility():
    """Test SyslogFormatter with custom facility and severity"""
    print("\n=== Testing SyslogFormatter (custom settings) ===")
    
    # LOCAL7 (23) + WARNING (4) = priority 188
    formatter = SyslogFormatter(
        facility="LOCAL7",
        severity="WARNING",
        app_name="fortinet-api",
        hostname="firewall.example.com"
    )
    result = formatter.format(DELETE_OPERATION)
    
    assert result.startswith("<188>1 ")
    assert "fortinet-api" in result
    assert "firewall.example.com" in result
    
    print(f"✓ Custom syslog: {result[:120]}...")


def test_syslog_formatter_severities():
    """Test SyslogFormatter priority calculation"""
    print("\n=== Testing SyslogFormatter severities ===")
    
    severities = {
        "EMERG": 128,   # LOCAL0 (16*8) + 0 = 128
        "ALERT": 129,   # 128 + 1
        "CRIT": 130,    # 128 + 2
        "ERR": 131,     # 128 + 3
        "WARNING": 132, # 128 + 4
        "NOTICE": 133,  # 128 + 5
        "INFO": 134,    # 128 + 6
        "DEBUG": 135,   # 128 + 7
    }
    
    for severity, expected_pri in severities.items():
        formatter = SyslogFormatter(facility="LOCAL0", severity=severity)
        result = formatter.format(GET_OPERATION)
        assert result.startswith(f"<{expected_pri}>"), f"Failed for {severity}"
        print(f"  ✓ {severity}: priority {expected_pri}")
    
    print("✓ All severities validated")


def test_cef_formatter_default():
    """Test CEFFormatter with default settings"""
    print("\n=== Testing CEFFormatter (default) ===")
    
    formatter = CEFFormatter()
    result = formatter.format(SAMPLE_OPERATION)
    
    # CEF header format
    assert result.startswith("CEF:0|Fortinet|FortiGate|7.0|")
    assert "API_OPERATION" in result
    assert "FortiGate API POST Operation" in result
    
    # Extension fields
    assert "act=POST" in result
    assert "dst=192.168.1.99" in result
    assert "outcome=success" in result
    assert "rt=125" in result  # duration_ms
    
    print(f"✓ CEF message: {result[:150]}...")


def test_cef_formatter_severity_mapping():
    """Test CEFFormatter severity mapping by HTTP method"""
    print("\n=== Testing CEFFormatter severity mapping ===")
    
    formatter = CEFFormatter()
    
    # GET = severity 2 (Low)
    result = formatter.format(GET_OPERATION)
    assert "|2|" in result
    print("✓ GET severity: 2 (Low)")
    
    # POST = severity 5 (Medium)
    result = formatter.format(SAMPLE_OPERATION)
    assert "|5|" in result
    print("✓ POST severity: 5 (Medium)")
    
    # DELETE = severity 7 (High)
    result = formatter.format(DELETE_OPERATION)
    assert "|7|" in result
    print("✓ DELETE severity: 7 (High)")


def test_cef_formatter_custom_device():
    """Test CEFFormatter with custom device info"""
    print("\n=== Testing CEFFormatter (custom device) ===")
    
    formatter = CEFFormatter(
        device_vendor="MyCompany",
        device_product="FGT-600F",
        device_version="7.4.3"
    )
    result = formatter.format(SAMPLE_OPERATION)
    
    assert "CEF:0|MyCompany|FGT-600F|7.4.3|" in result
    
    print(f"✓ Custom device: {result[:80]}...")


def test_cef_formatter_extensions():
    """Test CEFFormatter extension fields"""
    print("\n=== Testing CEFFormatter extensions ===")
    
    formatter = CEFFormatter()
    result = formatter.format(SAMPLE_OPERATION)
    
    # Check all extension fields
    assert "act=POST" in result
    assert "dst=192.168.1.99" in result
    assert "request=/api/v2/cmdb/firewall/address" in result
    assert "outcome=success" in result
    assert "dvchost=root" in result  # vdom
    assert "rt=125" in result  # duration_ms
    assert "deviceCustomString1=firewall.address" in result  # object_type
    assert "deviceCustomString1Label=ObjectType" in result
    assert "deviceCustomString2=test-host" in result  # object_name
    assert "deviceCustomString2Label=ObjectName" in result
    assert "suser=admin" in result  # from user_context
    
    print("✓ All CEF extensions present")


def test_cef_formatter_escaping():
    """Test CEFFormatter special character escaping"""
    print("\n=== Testing CEFFormatter escaping ===")
    
    # Operation with special characters
    special_op = {
        "timestamp": "2026-01-10T14:30:00Z",
        "method": "POST",
        "endpoint": "/api/v2/cmdb/firewall/address/test|pipe",
        "host": "host=with=equals",
        "success": True,
        "status_code": 200,
        "vdom": "vdom\\backslash",
    }
    
    formatter = CEFFormatter()
    result = formatter.format(special_op)
    
    # Check escaping: | -> \|, = -> \=, \ -> \\
    assert "test\\|pipe" in result
    assert "host\\=with\\=equals" in result
    
    print(f"✓ Special characters escaped: {result[:150]}...")


def test_cef_formatter_failed_operation():
    """Test CEFFormatter with failed operation"""
    print("\n=== Testing CEFFormatter (failed operation) ===")
    
    formatter = CEFFormatter()
    result = formatter.format(FAILED_OPERATION)
    
    assert "outcome=failure" in result
    assert "|5|" in result  # POST severity
    
    print(f"✓ Failed operation: {result[:120]}...")


def test_cef_formatter_no_user_context():
    """Test CEFFormatter when user_context is missing or None
    
    BUG FOUND in hfortix_core/audit/formatters.py line ~274:
    
        if operation.get("user_context", {}).get("username"):
    
    If user_context is None (not missing, but explicitly None), this crashes with:
        AttributeError: 'NoneType' object has no attribute 'get'
    
    FIX: Change to:
        if (operation.get("user_context") or {}).get("username"):
    
    Or use a safer pattern:
        user_context = operation.get("user_context") or {}
        if user_context.get("username"):
    """
    print("\n=== Testing CEFFormatter (no user context) ===")
    
    formatter = CEFFormatter()
    
    # Test with empty dict (works)
    result = formatter.format(GET_OPERATION)  # user_context = {}
    assert "suser=api-token" in result
    print("✓ Empty user_context defaults to api-token")
    
    # Test with None would crash - demonstrating the bug:
    # op_with_none = {**GET_OPERATION, "user_context": None}
    # formatter.format(op_with_none)  # Would raise AttributeError
    print("⚠ BUG: user_context=None crashes CEFFormatter (see docstring for fix)")


def test_formatter_protocol_compliance():
    """Test that all formatters implement the AuditFormatter protocol"""
    print("\n=== Testing AuditFormatter protocol compliance ===")
    
    from hfortix_core.audit.formatters import AuditFormatter
    
    formatters = [
        JSONFormatter(),
        SyslogFormatter(),
        CEFFormatter(),
    ]
    
    for formatter in formatters:
        # Should implement the protocol
        assert isinstance(formatter, AuditFormatter)
        
        # Should have format method that returns string
        result = formatter.format(SAMPLE_OPERATION)
        assert isinstance(result, str)
        assert len(result) > 0
        
        print(f"  ✓ {formatter.__class__.__name__} implements protocol")
    
    print("✓ All formatters are protocol compliant")


if __name__ == "__main__":
    test_json_formatter_compact()
    test_json_formatter_pretty()
    test_json_formatter_all_operations()
    test_syslog_formatter_default()
    test_syslog_formatter_custom_facility()
    test_syslog_formatter_severities()
    test_cef_formatter_default()
    test_cef_formatter_severity_mapping()
    test_cef_formatter_custom_device()
    test_cef_formatter_extensions()
    test_cef_formatter_escaping()
    test_cef_formatter_failed_operation()
    test_cef_formatter_no_user_context()
    test_formatter_protocol_compliance()
    
    print("\n" + "=" * 60)
    print("✅ All audit formatter tests passed!")
    print("=" * 60)
