from __future__ import annotations

import sys
from pathlib import Path
from typing import Iterable

# Add local package to path FIRST (before any installed versions)
# This ensures tests use the development version
# Path: packages/fortios/dev/tests/live/conftest.py
# Go up to workspace root: live -> tests -> dev -> fortios -> packages -> workspace root (6 parents)
workspace_root = Path(__file__).parent.parent.parent.parent.parent.parent
fortios_src = workspace_root / "packages" / "fortios" / "src"
core_src = workspace_root / "packages" / "core" / "src"

# Insert at beginning of sys.path to override installed versions
sys.path.insert(0, str(fortios_src))
sys.path.insert(0, str(core_src))

# Add tests directory to path so fgtclient/fmgclient can be imported
sys.path.insert(0, str(Path(__file__).parent))

import pytest

SEQUENTIAL_ROOTS: set[str] = {"endpoints", "other"}
PARALLEL_ROOTS: set[str] = {"validators", "integration", "unit"}


def _top_level_segment(path: Path, tests_root: Path) -> str | None:
    """Return the first segment under tests/ for a path, or None."""
    try:
        rel = path.relative_to(tests_root)
    except ValueError:
        return None
    parts: Iterable[str] = rel.parts
    for part in parts:
        return part
    return None


def pytest_collect_file(file_path: Path, parent: pytest.Collector):
    """Collect non-standard test modules under endpoints/ and other/.

    The files in these folders don't follow the default test_*.py naming
    convention, so we opt-in to collecting any Python file beneath them.
    """
    if file_path.suffix != ".py":
        return

    tests_root = Path(__file__).parent
    segment = _top_level_segment(file_path, tests_root)
    if segment in SEQUENTIAL_ROOTS:
        return pytest.Module.from_parent(parent=parent, path=file_path)


def pytest_collection_modifyitems(config: pytest.Config, items: list[pytest.Item]):
    """Mark tests for sequential vs parallel execution based on their folder."""
    tests_root = Path(__file__).parent
    has_xdist = config.pluginmanager.hasplugin("xdist")

    for item in items:
        segment = _top_level_segment(Path(item.fspath), tests_root)
        if segment in SEQUENTIAL_ROOTS:
            item.add_marker("sequential")
            if has_xdist:
                # Keep all sequential tests on the same worker when using xdist
                item.add_marker(pytest.mark.xdist_group("sequential"))
        elif segment in PARALLEL_ROOTS:
            item.add_marker("parallel")


@pytest.fixture(scope="session", autouse=True)
def close_fgt_client():
    """Close the FortiOS client connection at the end of the test session."""
    yield
    # Close connections to avoid ResourceWarning
    try:
        from fgtclient import fgt
        if hasattr(fgt, 'close'):
            fgt.close()
        elif hasattr(fgt, 'logout'):
            fgt.logout()
        # Force close underlying connection if it exists
        if hasattr(fgt, '_session') and fgt._session:
            fgt._session.close()
    except Exception:
        pass
    try:
        from fmgclient import fmg
        if hasattr(fmg, 'logout'):
            fmg.logout()
        elif hasattr(fmg, 'close'):
            fmg.close()
        # Force close underlying connection if it exists
        if hasattr(fmg, '_session') and fmg._session:
            fmg._session.close()
    except Exception:
        pass


def pytest_addoption(parser):
    """Add command line options for client selection."""
    parser.addoption(
        "--client",
        action="store",
        default="direct",
        choices=["direct", "fmg_proxy", "both"],
        help="Client to use: direct (default), fmg_proxy, or both"
    )


def pytest_generate_tests(metafunc):
    """Parameterize tests that use the fgt fixture based on --client option."""
    if "fgt" in metafunc.fixturenames:
        client_option = metafunc.config.getoption("--client")
        if client_option == "both":
            metafunc.parametrize("fgt", ["direct", "fmg_proxy"], indirect=True)
        elif client_option == "fmg_proxy":
            metafunc.parametrize("fgt", ["fmg_proxy"], indirect=True)
        else:
            metafunc.parametrize("fgt", ["direct"], indirect=True)


@pytest.fixture
def fgt(request):
    """
    FortiGate client fixture - returns direct or FMG proxy client.
    
    Usage in tests:
        def test_something(fgt):
            result = fgt.api.cmdb.system.global_.get()
    
    Run with:
        pytest tests/                          # Direct (default)
        pytest tests/ --client=fmg_proxy       # FMG proxy only
        pytest tests/ --client=both            # Both clients
    """
    if request.param == "fmg_proxy":
        from fmgclient import fgt as fmg_fgt
        return fmg_fgt
    else:
        from fgtclient import fgt as direct_fgt
        return direct_fgt


@pytest.fixture
def fmg():
    """FortiManager client fixture - only available when using FMG proxy."""
    from fmgclient import fmg
    return fmg
