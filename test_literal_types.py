"""Test Literal types for enum parameters."""
import os
from dotenv import load_dotenv
from hfortix_fortios import FortiOS

# Load environment
load_dotenv()

# Connect to FortiGate
fgt = FortiOS(
    host=os.getenv("FORTIGATE_HOST"),
    token=os.getenv("FORTIGATE_TOKEN"),
    vdom=os.getenv("FORTIGATE_VDOM", "test")
)

def test_literal_types_autocomplete():
    """
    Test that Literal types provide IDE autocomplete.
    
    In your IDE, when you type:
        result = fgt.api.monitor.system.fortiguard.test_availability.post(
            protocol="<-- HERE, you should see: https, udp, http
            service="<-- HERE, you should see: emailfilter, webfilter
        )
    """
    
    # Test with valid literal values
    print("\n=== Testing Literal Types ===")
    print("Testing protocol='http' and service='webfilter'...")
    
    result = fgt.api.monitor.system.fortiguard.test_availability.post(
        protocol="http",  # Should autocomplete: "https" | "udp" | "http"
        service="webfilter",  # Should autocomplete: "emailfilter" | "webfilter"
        port=443
    )
    
    assert result is not None
    assert result.http_status_code == 200
    print(f"✓ Success! Response: {result.json}")
    
    # If you uncomment this, your IDE should show a type error:
    # result = fgt.api.monitor.system.fortiguard.test_availability.post(
    #     protocol="invalid",  # ❌ Type error: "invalid" is not assignable to Literal["https", "udp", "http"]
    #     service="webfilter"
    # )
    
    print("\n✓ Literal types are working!")
    print("✓ IDE should provide autocomplete for protocol and service parameters")


if __name__ == "__main__":
    test_literal_types_autocomplete()
