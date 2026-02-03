"""
Pytest configuration for FortiOS API tests.

This conftest.py ensures that tests use the local development version
of the hfortix_fortios package instead of any pip-installed version.
"""

import sys
from pathlib import Path

# Add local package to sys.path FIRST (highest priority)
# This ensures we import from local development code, not pip-installed package
# Path: packages/fortios/dev/tests/conftest.py
# Go up to workspace root: tests -> dev -> fortios -> packages -> workspace root (5 parents)
workspace_root = Path(__file__).resolve().parent.parent.parent.parent.parent
fortios_src = workspace_root / "packages" / "fortios" / "src"
core_src = workspace_root / "packages" / "core" / "src"

sys.path.insert(0, str(fortios_src))
sys.path.insert(0, str(core_src))

# Add tests directory to path for __client__ import (where __client__.py is located)
tests_dir = Path(__file__).parent
sys.path.insert(0, str(tests_dir))

print(f"✓ Using FortiOS from: {fortios_src}")
print(f"✓ Using Core from: {core_src}")
print(f"✓ Tests directory: {tests_dir}")
