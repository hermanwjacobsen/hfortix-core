"""Test multiple format parameters in POST."""

from hfortix_fortios import FortiOS

# Create client with response_mode="object" at client level
fgt_object = FortiOS(
    host="192.168.1.99",
    token="your-api-token",
    response_mode="object"
)

def multiple_format_test():
    result = fgt_object.api.cmdb.firewall.policy.post(
        name="test_policy_multi_format",
        srcintf=["port3", "port4"],              # List of strings
        dstintf="port3",                          # Single string
        srcaddr=[{"name": "all"}],             # Already formatted
        dstaddr="all",                          # Single string
        service=["HTTP", "HTTPS"],               # List of strings
        action="accept",
        schedule="always"
    )
    # Should show: (variable) result: MutationResponse
    print(f"Created policy: {result}")

multiple_format_test()
