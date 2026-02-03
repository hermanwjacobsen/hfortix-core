#!/usr/bin/env python3
"""
HFortix FortiGate Test Runner - v1.0.0

Automatically discovers and runs all test files under tests/ directory.
Tests run sequentially to avoid overwhelming the FortiGate API.

Usage:
    python run_tests.py                    # Run with direct client (default)
    python run_tests.py --client=direct    # Run with direct FortiGate client
    python run_tests.py --client=fmg_proxy # Run with FortiManager proxy client
    python run_tests.py --client=both      # Run with both clients
    python run_tests.py -q                 # Quiet mode, show dots and summary
    python run_tests.py --quiet            # Same as -q
    python run_tests.py --no-cleanup       # Skip cleanup before running tests

Features:
    - Client selection: Direct, FMG proxy, or both
    - Auto cleanup: Removes all test objects before running tests
    - Sequential execution: Prevents API overload
    - Two output modes: Normal (verbose) and Quiet (minimal)

Test Coverage:
    - CMDB API: Alert Email, Antivirus, Application, Authentication, Automation, CASB, 
                Certificate, Diameter Filter, DLP, Firewall Address
    - Endpoints: CMDB, Log, Monitor, Service
    - Validators: Custom validation utilities
    - Other: Formatting utilities (fmt module), Real-world scenarios
    
Total: Auto-discovered test files with __main__ blocks
"""
import argparse
import subprocess
import sys
from pathlib import Path
import time


EXCLUDE_NAMES = {
    "__init__.py",
    "conftest.py",
    "fgtclient.py",
    "cleanup.py",
}


def discover_test_files(test_dir: Path) -> list[Path]:
    """
    Discover runnable test files under a tests/ tree.

    Keeps backward compatibility with the previous runner behavior used by
    unit tests:
    - include any .py file containing a __main__ block
    - exclude __init__.py, conftest.py, fgtclient.py, cleanup.py
    - skip __pycache__ and x_egde_cases folders
    """

    candidates: list[Path] = []
    for py_file in test_dir.rglob("*.py"):
        if py_file.name in EXCLUDE_NAMES:
            continue
        if "__pycache__" in py_file.parts:
            continue
        if "x_egde_cases" in py_file.parts:
            continue

        try:
            content = py_file.read_text()
        except OSError:
            continue

        if "if __name__ == \"__main__\"" in content:
            candidates.append(py_file)

    return sorted(candidates)

def run_cleanup(quiet_mode=False):
    """Run the cleanup script before tests"""
    tests_dir = Path(__file__).parent
    cleanup_script = tests_dir / "cleanup.py"
    
    if not cleanup_script.exists():
        if not quiet_mode:
            print("⚠️  Cleanup script not found, skipping cleanup.\n")
        return
    
    if not quiet_mode:
        print("🧹 Running cleanup script...")
    
    try:
        # Import and run cleanup
        sys.path.insert(0, str(tests_dir))
        from cleanup import cleanup_test_objects  # type: ignore
        
        deleted = cleanup_test_objects()
        
        if not quiet_mode:
            if deleted > 0:
                print(f"✅ Cleanup complete! Removed {deleted} test objects.\n")
            else:
                print("✅ Cleanup complete! No test objects found.\n")
        else:
            if deleted > 0:
                print(f"Cleaned {deleted} objects. ", end="", flush=True)
    
    except KeyboardInterrupt:
        if not quiet_mode:
            print("\n⚠️  Cleanup interrupted by user")
        raise  # Re-raise to propagate to main
    
    except Exception as e:
        if not quiet_mode:
            print(f"⚠️  Cleanup failed: {e}\n")


def main():
    """Run the full pytest suite after optional cleanup."""
    parser = argparse.ArgumentParser(description="HFortix FortiGate Test Runner")
    parser.add_argument("--client", choices=["direct", "fmg_proxy", "both"], default="direct",
                        help="Client to use: direct (default), fmg_proxy, or both")
    parser.add_argument("-q", "--quiet", action="store_true", help="Quiet mode")
    parser.add_argument("--no-cleanup", action="store_true", help="Skip cleanup before tests")
    
    # Parse known args, pass the rest to pytest
    args, remaining = parser.parse_known_args()
    
    quiet_mode = args.quiet
    skip_cleanup = args.no_cleanup
    client_mode = args.client

    # Everything else is passed through to pytest (e.g., -k, -m, path filters)
    passthrough_args = remaining.copy()

    # Disable pytest-xdist parallelization by default to keep live/endpoint
    # tests from stepping on each other's FortiGate state. Users can still
    # override by passing their own -n/--numprocesses flag.
    has_xdist_n = any(arg.startswith('-n') or arg.startswith('--numprocesses') for arg in passthrough_args)
    if not has_xdist_n:
        passthrough_args.insert(0, '-n0')

    if quiet_mode and '-q' not in passthrough_args:
        passthrough_args.insert(0, '-q')

    tests_dir = Path(__file__).parent

    if not quiet_mode:
        print("=" * 80)
        print("🧪 HFortix FortiGate Test Runner - v1.0.0")
        print("=" * 80)

    if not skip_cleanup:
        run_cleanup(quiet_mode)

    start_time = time.time()
    
    # Determine which client modes to run
    if client_mode == "both":
        clients_to_run = ["direct", "fmg_proxy"]
    else:
        clients_to_run = [client_mode]
    
    total_passed = 0
    total_failed = 0
    final_returncode = 0
    interrupted = False
    
    try:
        for client in clients_to_run:
            if not quiet_mode:
                client_display = "Direct FortiGate" if client == "direct" else "FMG Proxy"
                print(f"\n🔌 Running tests with {client_display} client...")
                print("-" * 60)
            
            # Build pytest command with --client argument
            cmd = [sys.executable, '-m', 'pytest', f'--client={client}', *passthrough_args]
            if not quiet_mode:
                print(f"🚀 Running: {' '.join(cmd)}\n")

            # Run pytest from the tests directory so conftest.py is found
            result = subprocess.run(cmd, cwd=tests_dir)
            
            if result.returncode != 0:
                final_returncode = result.returncode
    
    except KeyboardInterrupt:
        interrupted = True
        print("\n\n" + "=" * 80)
        print("⚠️  TEST RUN INTERRUPTED BY USER (Ctrl+C)")
        print("=" * 80)
        final_returncode = 130  # Standard exit code for SIGINT
    
    total_time = time.time() - start_time

    # Always print summary (even in quiet mode if interrupted)
    if not quiet_mode or interrupted:
        print("\n" + "=" * 80)
        if interrupted:
            print("⚠️  TEST RUN INTERRUPTED")
            print("⏱️  Ran for: {:.2f}s before interruption".format(total_time))
            print("💡 Tip: Tests were stopped early. Re-run to complete the test suite.")
        else:
            print("⏱️  Elapsed: {:.2f}s".format(total_time))
            if client_mode == "both":
                print("📊 Ran tests with both Direct and FMG Proxy clients")
        print("=" * 80 + "\n")

    # Close the FortiOS client connection to avoid resource warnings
    try:
        from fgtclient import fgt
        if hasattr(fgt, 'close'):
            fgt.close()
    except Exception:
        pass
    
    try:
        from fmgclient import fmg
        if hasattr(fmg, 'logout'):
            fmg.logout()
    except Exception:
        pass

    return final_returncode


if __name__ == "__main__":
    sys.exit(main())
