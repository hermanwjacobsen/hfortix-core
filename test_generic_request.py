"""
Test script for the new generic request() method
"""

# Test the request method accepts the GUI API preview format
def test_request_method():
    """Test that FortiOS.request() accepts GUI API preview JSON"""
    from hfortix_fortios import FortiOS
    
    # This is just a syntax/import test - would need real credentials to actually run
    print("Testing FortiOS.request() method signature...")
    
    # Example config from GUI API preview
    config = {
        "method": "POST",
        "url": "/api/v2/cmdb/firewall/address",
        "params": {
            "datasource": 1,
            "vdom": "test"
        },
        "data": {
            "name": "test999999",
            "subnet": "192.168.1.0/24",
            "color": "0"
        }
    }
    
    # Verify the method exists and accepts the config
    # Note: This will fail at runtime without valid credentials
    # but we can verify the method signature is correct
    try:
        fgt = FortiOS(host="test.example.com", token="x" * 32)
        # Check method exists
        assert hasattr(fgt, 'request'), "FortiOS.request() method not found"
        print("✓ FortiOS.request() method exists")
        
        # Check it's callable
        assert callable(fgt.request), "FortiOS.request() is not callable"
        print("✓ FortiOS.request() is callable")
        
        # Check method signature (won't execute without valid host)
        import inspect
        sig = inspect.signature(fgt.request)
        params = list(sig.parameters.keys())
        assert 'config' in params, "Missing 'config' parameter"
        assert 'raw_json' in params, "Missing 'raw_json' parameter"
        print("✓ FortiOS.request() has correct parameters: config, raw_json")
        
        print("\nAll tests passed! ✓")
        print("\nExample usage:")
        print("  config = {")
        print('    "method": "POST",')
        print('    "url": "/api/v2/cmdb/firewall/address",')
        print('    "params": {"vdom": "root"},')
        print('    "data": {"name": "test", "subnet": "192.168.1.0/24"}')
        print("  }")
        print("  result = fgt.request(config)")
        
    except Exception as e:
        print(f"✗ Error during test: {e}")
        raise

if __name__ == "__main__":
    test_request_method()
