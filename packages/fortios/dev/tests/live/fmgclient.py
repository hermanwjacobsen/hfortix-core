"""FortiManager Proxy client configuration"""
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Add local package to path FIRST (before any installed versions)
# This ensures tests use the development version
# Path: packages/fortios/dev/tests/live/fmgclient.py
# Go up to workspace root: live -> tests -> dev -> fortios -> packages -> workspace root (6 parents)
workspace_root = Path(__file__).parent.parent.parent.parent.parent.parent
fortios_src = workspace_root / "packages" / "fortios" / "src"
core_src = workspace_root / "packages" / "core" / "src"

# Insert at beginning of sys.path to override installed versions
sys.path.insert(0, str(fortios_src))
sys.path.insert(0, str(core_src))

from hfortix_fortios import FortiManagerProxy

# Load environment variables from .env file
load_dotenv()

# Get connection settings from environment (with validation)
FMG_HOST = os.getenv("FMG_HOST", "")
FMG_USER = os.getenv("FMG_USER", "")
FMG_PASS = os.getenv("FMG_PASS", "")
FMG_ADOM = os.getenv("FMG_ADOM", "HWJ")
FMG_DEVICE = os.getenv("FMG_DEVICE", "hwj-fw")
FMG_VDOM = os.getenv("FMG_VDOM", "test")  # Match direct FortiGate tests

if not FMG_HOST or not FMG_USER or not FMG_PASS:
    raise ValueError("FMG_HOST, FMG_USER, and FMG_PASS must be set in .env file")

# Connect to FortiManager
fmg = FortiManagerProxy(
    host=FMG_HOST,
    username=FMG_USER,
    password=FMG_PASS,
    verify=False,
    adom=FMG_ADOM,
)

# Login to FortiManager
fmg.login()

# Get proxied FortiGate connection with vdom
fgt = fmg.proxy(device=FMG_DEVICE, vdom=FMG_VDOM)
