"""
Tests for hfortix_core.utils.normalize_keys

Tests the key normalization function that converts hyphen to underscore.
"""

from hfortix_core.utils import normalize_keys


def test_normalize_simple_dict():
    """Test normalizing a simple dict with hyphenated keys"""
    print("\n=== Testing normalize_keys (simple dict) ===")
    
    data = {"tcp-portrange": "8080", "name": "test", "src-addr": "10.0.0.1"}
    result = normalize_keys(data)
    
    assert result == {"tcp_portrange": "8080", "name": "test", "src_addr": "10.0.0.1"}
    assert "tcp-portrange" not in result
    
    print(f"✓ Converted: {data} -> {result}")


def test_normalize_nested_dict():
    """Test normalizing nested dicts"""
    print("\n=== Testing normalize_keys (nested dict) ===")
    
    data = {
        "policy-id": 1,
        "src-intf": {
            "interface-name": "port1",
            "zone-name": "lan"
        }
    }
    
    result = normalize_keys(data)
    
    assert result["policy_id"] == 1
    assert result["src_intf"]["interface_name"] == "port1"
    assert result["src_intf"]["zone_name"] == "lan"
    
    print("✓ Nested dicts normalized recursively")


def test_normalize_list_of_dicts():
    """Test normalizing a list of dicts"""
    print("\n=== Testing normalize_keys (list of dicts) ===")
    
    data = [
        {"policy-id": 1, "action": "accept"},
        {"policy-id": 2, "action": "deny"},
    ]
    
    result = normalize_keys(data)
    
    assert result[0]["policy_id"] == 1
    assert result[1]["policy_id"] == 2
    
    print("✓ List of dicts normalized")


def test_normalize_deeply_nested():
    """Test normalizing deeply nested structures"""
    print("\n=== Testing normalize_keys (deeply nested) ===")
    
    data = {
        "firewall-policy": {
            "src-address": [
                {"addr-name": "test-host", "subnet-mask": "255.255.255.0"}
            ],
            "dst-address": [
                {"addr-name": "all"}
            ]
        }
    }
    
    result = normalize_keys(data)
    
    assert "firewall_policy" in result
    assert "src_address" in result["firewall_policy"]
    assert result["firewall_policy"]["src_address"][0]["addr_name"] == "test-host"
    assert result["firewall_policy"]["src_address"][0]["subnet_mask"] == "255.255.255.0"
    
    print("✓ Deeply nested structures normalized")


def test_normalize_preserves_values():
    """Test that values with hyphens are NOT modified"""
    print("\n=== Testing normalize_keys (preserves values) ===")
    
    data = {
        "name": "test-host-01",
        "ip-address": "192.168.1.1",
        "comment": "This is a test-comment with hyphens"
    }
    
    result = normalize_keys(data)
    
    # Keys should be normalized
    assert "ip_address" in result
    
    # Values should be preserved exactly
    assert result["name"] == "test-host-01"
    assert result["ip_address"] == "192.168.1.1"
    assert result["comment"] == "This is a test-comment with hyphens"
    
    print("✓ Values with hyphens preserved")


def test_normalize_non_dict():
    """Test that non-dict/list types pass through unchanged"""
    print("\n=== Testing normalize_keys (non-dict types) ===")
    
    # String
    assert normalize_keys("test-string") == "test-string"
    print("  ✓ String passed through")
    
    # Integer
    assert normalize_keys(42) == 42
    print("  ✓ Integer passed through")
    
    # None
    assert normalize_keys(None) is None
    print("  ✓ None passed through")
    
    # Boolean
    assert normalize_keys(True) is True
    print("  ✓ Boolean passed through")
    
    # Float
    assert normalize_keys(3.14) == 3.14
    print("  ✓ Float passed through")
    
    print("✓ Non-dict types unchanged")


def test_normalize_empty_structures():
    """Test normalizing empty structures"""
    print("\n=== Testing normalize_keys (empty structures) ===")
    
    assert normalize_keys({}) == {}
    assert normalize_keys([]) == []
    
    print("✓ Empty structures handled")


def test_normalize_mixed_keys():
    """Test dict with mix of hyphenated and non-hyphenated keys"""
    print("\n=== Testing normalize_keys (mixed keys) ===")
    
    data = {
        "policyid": 1,  # No hyphen
        "src-intf": "port1",  # One hyphen
        "tcp-mss-sender": 1452,  # Multiple hyphens
        "UPPER-CASE": "test",  # Upper case
    }
    
    result = normalize_keys(data)
    
    assert result["policyid"] == 1
    assert result["src_intf"] == "port1"
    assert result["tcp_mss_sender"] == 1452
    assert result["UPPER_CASE"] == "test"
    
    print("✓ Mixed key types normalized correctly")


def test_normalize_complex_fortigate_response():
    """Test normalizing a realistic FortiGate API response"""
    print("\n=== Testing normalize_keys (FortiGate response) ===")
    
    # Simulated FortiGate firewall policy response
    response = {
        "http-status": 200,
        "results": [
            {
                "policyid": 1,
                "name": "Allow-Web",
                "srcintf": [{"name": "port1", "q-origin-key": "port1"}],
                "dstintf": [{"name": "port2", "q-origin-key": "port2"}],
                "srcaddr": [{"name": "all", "q-origin-key": "all"}],
                "dstaddr": [{"name": "all", "q-origin-key": "all"}],
                "action": "accept",
                "schedule": "always",
                "service": [{"name": "HTTP", "q-origin-key": "HTTP"}],
                "nat": "enable",
                "tcp-mss-sender": 0,
                "tcp-mss-receiver": 0,
                "ssl-ssh-profile": "certificate-inspection",
            }
        ],
        "vdom": "root",
        "serial": "FGT60F0000000000",
        "version": "v7.4.3",
        "build": 2573
    }
    
    result = normalize_keys(response)
    
    # Check top-level keys
    assert "http_status" in result
    assert result["http_status"] == 200
    
    # Check nested policy
    policy = result["results"][0]
    assert policy["policyid"] == 1
    assert "q_origin_key" in policy["srcintf"][0]
    assert policy["tcp_mss_sender"] == 0
    assert policy["ssl_ssh_profile"] == "certificate-inspection"
    
    print("✓ Complex FortiGate response normalized correctly")


def test_normalize_idempotent():
    """Test that normalizing twice gives same result"""
    print("\n=== Testing normalize_keys (idempotent) ===")
    
    data = {"src-addr": "test", "nested": {"dst-addr": "all"}}
    
    result1 = normalize_keys(data)
    result2 = normalize_keys(result1)
    
    assert result1 == result2
    
    print("✓ Normalization is idempotent")


if __name__ == "__main__":
    test_normalize_simple_dict()
    test_normalize_nested_dict()
    test_normalize_list_of_dicts()
    test_normalize_deeply_nested()
    test_normalize_preserves_values()
    test_normalize_non_dict()
    test_normalize_empty_structures()
    test_normalize_mixed_keys()
    test_normalize_complex_fortigate_response()
    test_normalize_idempotent()
    
    print("\n" + "=" * 60)
    print("✅ All normalize_keys tests passed!")
    print("=" * 60)
