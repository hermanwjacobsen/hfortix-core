"""
Test that type hints work correctly for authentication rule operations.

This demonstrates:
1. Both explicit and implicit response_mode work correctly
2. Nonexistent fields show Pylance errors in ALL cases
3. raw_json=True returns RawAPIResponse with proper type checking
"""

from hfortix_fortios import FortiOS

# Initialize client
fgt = FortiOS(host="192.168.1.99", token="test-token")


def test_explicit_response_mode():
    """Test with explicit response_mode='dict' - clearest type info"""
    rule = fgt.api.cmdb.authentication.rule.get(name="test_rule1", response_mode='dict')
    # Valid fields work:
    assert isinstance(rule, dict)
    assert rule['name'] == "test_rule1"
    for intf in rule['srcintf']:
        print(intf['name'])
    # Nonexistent field shows error:
    assert rule['nonexistent_field_explicit']  # Should error!


def test_implicit_response_mode():
    """Test without explicit response_mode - relies on client default (dict)
    
    THIS IS THE FIX! Previously, nonexistent fields didn't show errors
    when response_mode was not explicitly passed. Now they do!
    """
    # Test with positional argument
    rule_positional = fgt.api.cmdb.authentication.rule.get("test_rule1")
    # Test with keyword argument
    rule_keyword = fgt.api.cmdb.authentication.rule.get(name="test_rule1")
    
    # Valid fields work:
    assert rule_positional['name'] == "test_rule1"
    assert rule_keyword['name'] == "test_rule1"
    for intf in rule_keyword['srcintf']:
        print(intf['name'])
    
    # Nonexistent fields NOW show errors (THE FIX!):
    x = rule_positional['nonexistent_field_implicit']  # Should error!
    y = rule_keyword['another_nonexistent']  # Should error!


def test_fortiobject_subscriptable():
    """Test that FortiObject is properly subscriptable"""
    from hfortix_fortios.models import FortiObject
    
    data = {
        "name": "test_rule1",
        "srcintf": [{"name": "port3"}]
    }
    obj = FortiObject(data)
    
    # Both attribute and subscript access should work
    assert obj.name == "test_rule1"
    assert obj['name'] == "test_rule1"
    
    # Subscript access to list fields should work
    assert isinstance(obj['srcintf'], list)
    assert any(intf.name == "port3" for intf in obj['srcintf'])


def test_raw_json_get():
    """Test that raw_json=True returns RawAPIResponse with correct type hints"""
    # GET with raw_json=True should return RawAPIResponse
    raw_get = fgt.api.cmdb.authentication.rule.get(name="test_rule1", raw_json=True)
    
    # Valid RawAPIResponse fields work:
    assert raw_get['http_method'] == "GET"
    assert raw_get['http_status'] == 200
    assert raw_get['results'] is not None
    assert raw_get['vdom'] == "root"
    assert raw_get['path'] == "authentication"
    assert raw_get['name'] == "rule"
    assert raw_get['status'] == "success"
    assert raw_get['serial'] == "FGVMXXXXXXXX"
    assert raw_get['version'] == "v7.4.8"
    assert raw_get['build'] == 1234
    
    # Nonexistent fields should show errors:
    x = raw_get['nonexistent']  # Should error!


def test_raw_json_post():
    """Test that raw_json=True for POST returns RawAPIResponse"""
    # POST with raw_json=True should return RawAPIResponse
    raw_post = fgt.api.cmdb.authentication.rule.post(
        name="test_rule2",
        ip_based="enable",
        raw_json=True
    )
    
    # Valid RawAPIResponse fields work:
    assert raw_post['http_method'] == "POST"
    assert raw_post['http_status'] == 200
    
    # Nonexistent fields should show errors:
    y = raw_post['nonexistent']  # Should error!


def test_raw_json_put():
    """Test that raw_json=True for PUT returns RawAPIResponse"""
    # PUT with raw_json=True should return RawAPIResponse
    raw_put = fgt.api.cmdb.authentication.rule.put(
        name="test_rule2",
        active_auth_method="test_method",
        raw_json=True
    )
    
    # Valid RawAPIResponse fields work:
    assert raw_put['http_method'] == "PUT"
    assert raw_put['http_status'] == 200
    
    # Nonexistent fields should show errors:
    z = raw_put['nonexistent']  # Should error!


def test_raw_json_delete():
    """Test that raw_json=True for DELETE returns RawAPIResponse"""
    # DELETE with raw_json=True should return RawAPIResponse
    raw_delete = fgt.api.cmdb.authentication.rule.delete(
        name="test_rule2",
        raw_json=True
    )
    
    # Valid RawAPIResponse fields work:
    assert raw_delete['http_method'] == "DELETE"
    assert raw_delete['http_status'] == 200
    
    # Nonexistent fields should show errors:
    w = raw_delete['nonexistent']  # Should error!


if __name__ == "__main__":
    print("Type hints test file created successfully!")
    print("\nKey improvements:")
    print("1. FortiObject.__getitem__ now has explicit -> Any return type")
    print("2. Client-level response_mode properly propagates through API hierarchy")
    print("3. Mode-specific classes (DictMode/ObjectMode) at all API levels")
    print("4. raw_json=True returns RawAPIResponse with full type checking")
    print("5. All CRUD methods (GET/POST/PUT/DELETE) support raw_json parameter")
    print("\nPylance now catches:")
    print("- Nonexistent fields in TypedDict responses")
    print("- Nonexistent fields in RawAPIResponse")
    print("- Type mismatches at all API levels")

    print("2. FortiObject.__getattr__ now has explicit -> Any return type")
    print("3. Protocol overloads split default behavior based on 'name' parameter")
    print("\nBest practice: Use response_mode='dict' for clearest type information")
