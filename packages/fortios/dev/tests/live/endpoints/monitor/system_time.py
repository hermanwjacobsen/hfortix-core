
import argparse
import sys
from pathlib import Path
import pytest
import base64
import requests
import os
from dotenv import load_dotenv
import urllib3

# Disable SSL warnings for test environment
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Load environment variables
load_dotenv()

# Run registration monitor tests on a single worker to preserve state
pytestmark = pytest.mark.xdist_group(Path(__file__).stem)

# Add pytest directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt

from datetime import datetime

def test_get_system_time():
    """Test: Get system time"""
    result = fgt.api.monitor.system.time.get()
    assert result is not None
    assert 'time' in result
    
    # Convert timestamp to readable format
    timestamp = result['time']
    readable_time = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
    print(f"✓ System time: {readable_time} (timestamp: {timestamp})")

def test_set_system_time():
    """Test: Set system time to current time (validates endpoint)"""
    # Get current system time
    current_result = fgt.api.monitor.system.time.get()
    timestamp = current_result['time']
    
    # Convert timestamp to date components
    dt = datetime.fromtimestamp(timestamp)
    
    # Set the time to the same value (safe test - doesn't actually change time)
    result = fgt.api.monitor.system.time.set.post(
        year=dt.year,
        month=dt.month - 1,  # API expects 0-11, Python datetime is 1-12
        day=dt.day,
        hour=dt.hour,
        minute=dt.minute,
        second=dt.second
    )
    
    assert result is not None
    assert result.http_status == "success"
    print(f"✓ Set system time endpoint validated (set to current time: {dt.strftime('%Y-%m-%d %H:%M:%S')})")

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
    test_get_system_time()
    print("✓ test_get_system_time passed")
    
    test_set_system_time()
    print("✓ test_set_system_time passed")
    
    print("\n✓ All system time tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
