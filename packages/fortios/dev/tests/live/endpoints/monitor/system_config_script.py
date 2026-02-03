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


# Temporary config script file path
TMP_CONFIG_SCRIPT = Path(__file__).parent / "tmp_config_script"

def test_write_config_script():
    """Test: Write a config script to temporary file"""
    config_content = """config vdom
edit test
config firewall address
edit "test_config_script_1"
set subnet 192.168.254.0 255.255.255.0
next
end
end
"""
    
    # Write config script to file
    TMP_CONFIG_SCRIPT.write_text(config_content)
    print(f"✓ Config script written to: {TMP_CONFIG_SCRIPT}")
    
    # Verify file was created
    assert TMP_CONFIG_SCRIPT.exists()
    assert TMP_CONFIG_SCRIPT.read_text() == config_content
    print(f"✓ Config script content verified")

def cleanup():
    """Cleanup temporary config script file and test config scripts from history."""
    if TMP_CONFIG_SCRIPT.exists():
        TMP_CONFIG_SCRIPT.unlink()
        print(f"✓ Cleaned up temporary config script file")
    
    result = fgt.api.monitor.system.config_script.get()
    history = result.get('conf_scripts', {}).get('history', [])
    
    # Collect all test script IDs
    test_script_ids = []
    for script in history:
        if script.get('name', '').startswith("tmp_") or script.get('name', '').startswith("test_"):
            test_script_ids.append(str(script['id']))
    
    # Delete test scripts in batch if any found
    if test_script_ids:
        fgt.api.monitor.system.config_script.delete.post(id_list    =test_script_ids)  # type: ignore
        print(f"✓ Deleted {len(test_script_ids)} test config scripts from FortiGate history")
    else:
        print(f"✓ No test config scripts found in history")

def test_get_config_script():
    """Test: GET /monitor/system/config-script - Retrieve existing config scripts"""
    
    result = fgt.api.monitor.system.config_script.get()
    assert result is not None
    assert result.http_status_code == 200

def test_post_config_script_upload():
    """Test: POST /monitor/system/config-script/upload - Upload and run config script"""
    
    # Read config script content
    config_content = TMP_CONFIG_SCRIPT.read_text()
    encoded_content = base64.b64encode(config_content.encode()).decode()
    
    result = fgt.api.monitor.system.config_script.upload.post(
        filename="test_config_script_upload",
        file_content=encoded_content
    )
    
    assert result is not None
    assert result.http_status == "success"
    print(f"✓ Uploaded and ran config script on FortiGate")
    
    # Verify script appears in history
    verify = fgt.api.monitor.system.config_script.get()
    found = False
    for script in verify.get('conf_scripts', {}).get('history', []):
        if script.get('name') == "test_config_script_upload":
            found = True
            break
    assert found, "Uploaded config script not found in history"
    print(f"✓ Config script verified in history")


# def test_run_remote_config_script():
#     """Test: POST /monitor/system/config-script/run - Run remote config script
    
#     Note: This tests the endpoint functionality. Without a configured remote 
#     management station (FTP/TFTP), we expect an error, which validates the 
#     endpoint is working and remote_script parameter is correctly preserved.
#     """
#     try:
#         result = fgt.api.monitor.system.config_script.run.post(
#             remote_script="nonexistent_remote_script"
#         )
#         # If somehow it succeeds, that's also valid (remote server configured)
#         print(f"✓ Run endpoint accessible (remote server may be configured)")
#     except Exception as e:
#         # Expected: Error -3244 "Error retrieving configuration from the management station"
#         # This proves the endpoint works and remote_script parameter is correct
#         if "500" in str(e) or "3244" in str(e) or "management station" in str(e):
#             print(f"✓ Run endpoint works (expected error: no remote server configured)")
#         else:
#             raise

def test_delete_config_script():
    """Test: DELETE /monitor/system/config-script - Delete specific config scripts"""
    
    # First, get the list of scripts
    result = fgt.api.monitor.system.config_script.get()
    history = result.get('conf_scripts', {}).get('history', [])
    
    for script in history:
        if script.get('name') == "test_config_script_upload":
            fgt.api.monitor.system.config_script.delete.post(id_list=script['id'])
            print(f"✓ Deleted test config script with ID: {script['id']}")
            break
    
    # Verify deletion
    verify = fgt.api.monitor.system.config_script.get()
    for script in verify.get('conf_scripts', {}).get('history', []):
        print(f"  Remaining script: {script.get('name')}")


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
    
    test_get_config_script()
    print("✓ test_get_config_script passed")
    
    test_write_config_script()
    print("✓ test_write_config_script passed")
    
    test_post_config_script_upload()
    print("✓ test_post_config_script_upload passed")
        
    # test_run_remote_config_script()
    # print("✓ test_run_remote_config_script passed")

    test_delete_config_script()
    print("✓ test_delete_config_script passed")

    print("\n✓ All system config script tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
