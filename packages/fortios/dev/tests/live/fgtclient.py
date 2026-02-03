"""FortiGate client configuration"""
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Add local package to path FIRST (before any installed versions)
# This ensures tests use the development version
# Path: packages/fortios/dev/tests/live/fgtclient.py
# Go up to workspace root: live -> tests -> dev -> fortios -> packages -> workspace root (6 parents)
workspace_root = Path(__file__).parent.parent.parent.parent.parent.parent
fortios_src = workspace_root / "packages" / "fortios" / "src"
core_src = workspace_root / "packages" / "core" / "src"

# Insert at beginning of sys.path to override installed versions
sys.path.insert(0, str(fortios_src))
sys.path.insert(0, str(core_src))

from hfortix_fortios import FortiOS

# Load environment variables from .env file
load_dotenv()

# Get connection settings from environment (with validation)
HOST = os.getenv("FORTIGATE_HOST", "")
TOKEN = os.getenv("FORTIGATE_TOKEN", "")
PORT = int(os.getenv("FORTIGATE_PORT", "443"))
VDOM = os.getenv("FORTIGATE_VDOM", "root")

if not HOST or not TOKEN:
    raise ValueError("FORTIGATE_HOST and FORTIGATE_TOKEN must be set in .env file")

fgt = FortiOS(
    host=HOST,
    token=TOKEN,
    port=PORT,
    verify=False,
    error_mode="return",
    vdom=VDOM,
)

fgt_object = fgt  # Backwards compatibility alias


