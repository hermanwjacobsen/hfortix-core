import argparse
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(project_root))
from fgtclient import fgt

import pytest

# Run tests on a single worker to preserve state (group by filename)
pytestmark = pytest.mark.xdist_group(Path(__file__).stem)

# NOTE: Router policy endpoint structure:
# - GET /router/policy - Get all policy routes
# - GET /router/policy/{seq-num} - Get specific policy route
# - POST /router/policy - Create new policy route
# - PUT /router/policy/{seq-num} - Update policy route
# - DELETE /router/policy/{seq-num} - Delete policy route

def cleanup():
    """Cleanup all test policy routes (seq_num 1-100)."""
    try:
        policies = fgt.api.cmdb.router.policy.get()
        for policy in policies:
            # Only delete test policies (seq_num 1-100)
            if hasattr(policy, 'seq_num') and isinstance(policy.seq_num, int) and 1 <= policy.seq_num <= 100:
                try:
                    fgt.api.cmdb.router.policy.delete(seq_num=policy.seq_num)
                except Exception:
                    pass
    except Exception:
        pass


@pytest.fixture(scope="module", autouse=True)
def setup_and_teardown():
    """Auto-cleanup before and after all tests in this module."""
    # Cleanup before tests
    cleanup()
    yield
    # Cleanup after tests
    cleanup()


def test_get_router_policy():
    """Test: Get all policy routes"""
    result = fgt.api.cmdb.router.policy.get()
    assert result is not None
    assert result.http_status_code == 200


def test_post_router_policy_basic():
    """Test: Create basic policy route"""
    result = fgt.api.cmdb.router.policy.post(
        seq_num=10,
        action="permit",
        protocol=0,
        gateway="192.168.1.254",
        output_device="port3",
        status="enable",
        comments="Basic policy route test"
    )
    assert result is not None
    assert result.http_status == "success"


def test_get_router_policy_specific():
    """Test: Get specific policy route"""
    result = fgt.api.cmdb.router.policy.get(seq_num=10)
    assert result is not None
    assert result.http_status_code == 200
    assert result.seq_num == 10


def test_post_router_policy_with_source():
    """Test: Create policy route with source subnet"""
    result = fgt.api.cmdb.router.policy.post(
        seq_num=20,
        action="permit",
        src=[
            {
                "subnet": "10.0.0.0/24"
            }
        ],
        gateway="192.168.1.254",
        output_device="port3",
        status="enable",
        comments="Policy route with source subnet"
    )
    assert result is not None
    assert result.http_status == "success"


def test_post_router_policy_with_destination():
    """Test: Create policy route with destination subnet"""
    result = fgt.api.cmdb.router.policy.post(
        seq_num=30,
        action="permit",
        dst=[
            {
                "subnet": "172.16.0.0/16"
            }
        ],
        gateway="192.168.1.254",
        output_device="port3",
        status="enable",
        comments="Policy route with destination subnet"
    )
    assert result is not None
    assert result.http_status == "success"


def test_post_router_policy_with_ports():
    """Test: Create policy route with port matching"""
    result = fgt.api.cmdb.router.policy.post(
        seq_num=40,
        action="permit",
        protocol=6,  # TCP
        start_port=80,
        end_port=80,
        start_source_port=1024,
        end_source_port=65535,
        gateway="192.168.1.254",
        output_device="port3",
        status="enable",
        comments="Policy route with TCP port 80"
    )
    assert result is not None
    assert result.http_status == "success"


def test_post_router_policy_with_input_device():
    """Test: Create policy route with input device"""
    result = fgt.api.cmdb.router.policy.post(
        seq_num=50,
        action="permit",
        input_device=[
            {
                "name": "port3"
            }
        ],
        gateway="192.168.1.254",
        output_device="port3",
        status="enable",
        comments="Policy route with input device"
    )
    assert result is not None
    assert result.http_status == "success"


def test_post_router_policy_with_tos():
    """Test: Create policy route with TOS matching"""
    result = fgt.api.cmdb.router.policy.post(
        seq_num=60,
        action="permit",
        tos="0x10",
        tos_mask="0x3f",
        gateway="192.168.1.254",
        output_device="port3",
        status="enable",
        comments="Policy route with TOS matching"
    )
    assert result is not None
    assert result.http_status == "success"


def test_post_router_policy_deny():
    """Test: Create deny policy route"""
    result = fgt.api.cmdb.router.policy.post(
        seq_num=70,
        action="deny",
        src=[
            {
                "subnet": "192.168.100.0/24"
            }
        ],
        status="enable",
        comments="Deny policy route"
    )
    assert result is not None
    assert result.http_status == "success"


def test_post_router_policy_with_negation():
    """Test: Create policy route with source negation"""
    result = fgt.api.cmdb.router.policy.post(
        seq_num=80,
        action="permit",
        src=[
            {
                "subnet": "10.10.10.0/24"
            }
        ],
        src_negate="enable",
        gateway="192.168.1.254",
        output_device="port3",
        status="enable",
        comments="Policy route with source negation"
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_router_policy():
    """Test: Update policy route"""
    result = fgt.api.cmdb.router.policy.put(
        seq_num=10,
        action="permit",
        protocol=0,
        gateway="192.168.1.253",  # Changed gateway
        output_device="port3",
        status="enable",
        comments="Updated basic policy route test"
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_router_policy_disable():
    """Test: Disable policy route"""
    result = fgt.api.cmdb.router.policy.put(
        seq_num=20,
        action="permit",
        src=[
            {
                "subnet": "10.0.0.0/24"
            }
        ],
        gateway="192.168.1.254",
        output_device="port3",
        status="disable",  # Disabled
        comments="Disabled policy route"
    )
    assert result is not None
    assert result.http_status == "success"


def test_delete_router_policy():
    """Test: Delete specific policy route"""
    result = fgt.api.cmdb.router.policy.delete(seq_num=70)
    assert result is not None
    assert result.http_status == "success"
    verify = fgt.api.cmdb.router.policy.get()
    for policy in verify:
        assert policy.seq_num != 70



def test_get_router_policy_verify():
    """Test: Verify policy routes exist"""
    result = fgt.api.cmdb.router.policy.get()
    assert result is not None
    assert result.http_status_code == 200
    # Should have policies remaining (we deleted only seq 70)
    assert len(result) > 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run tests")
    parser.add_argument("--client", choices=["direct", "fmg_proxy"], default="direct",
                        help="Client to use: direct (default) or fmg_proxy")
    args = parser.parse_args()
    
    if args.client == "fmg_proxy":
        from fmgclient import fgt, fmg
        client_name = "FMG proxy"
    else:
        from fgtclient import fgt
        fmg = None
        client_name = "direct"
    
    print(f"Running tests with {client_name} client...")
    cleanup()
    print("✓ Pre-Cleanup passed")

    test_get_router_policy()
    print("✓ test_get_router_policy passed")
    
    test_post_router_policy_basic()
    print("✓ test_post_router_policy_basic passed")
    
    test_get_router_policy_specific()
    print("✓ test_get_router_policy_specific passed")
    
    test_post_router_policy_with_source()
    print("✓ test_post_router_policy_with_source passed")
    
    test_post_router_policy_with_destination()
    print("✓ test_post_router_policy_with_destination passed")
    
    test_post_router_policy_with_ports()
    print("✓ test_post_router_policy_with_ports passed")
    
    test_post_router_policy_with_input_device()
    print("✓ test_post_router_policy_with_input_device passed")
    
    test_post_router_policy_with_tos()
    print("✓ test_post_router_policy_with_tos passed")
    
    test_post_router_policy_deny()
    print("✓ test_post_router_policy_deny passed")
    
    test_post_router_policy_with_negation()
    print("✓ test_post_router_policy_with_negation passed")
    
    test_put_router_policy()
    print("✓ test_put_router_policy passed")
    
    test_put_router_policy_disable()
    print("✓ test_put_router_policy_disable passed")
    
    test_delete_router_policy()
    print("✓ test_delete_router_policy passed")
    
    test_get_router_policy_verify()
    print("✓ test_get_router_policy_verify passed")

    cleanup()
    print("✓ All router/policy tests passed")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
