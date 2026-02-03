"""
Tests for log_operation decorator.

The log_operation decorator provides structured logging for operations.
"""

import sys
import logging
from io import StringIO


class Colors:
    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"
    BOLD = "\033[1m"


def print_test_result(name: str, passed: bool, error: str | None = None):
    status = f"{Colors.GREEN}PASS{Colors.RESET}" if passed else f"{Colors.RED}FAIL{Colors.RESET}"
    print(f"  [{status}] {name}")
    if error:
        print(f"         {Colors.RED}{error}{Colors.RESET}")


def run_tests():
    from hfortix_core import log_operation

    passed = 0
    failed = 0
    tests = []

    # =================================================================
    # Basic Usage Tests
    # =================================================================

    def test_log_operation_basic():
        """log_operation should log without raising errors."""
        # Capture log output
        log_capture = StringIO()
        handler = logging.StreamHandler(log_capture)
        handler.setLevel(logging.DEBUG)
        
        logger = logging.getLogger('test_logger')
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)
        
        try:
            log_operation('test_logger', 'test operation')
            # Should not raise
            return True, None
        finally:
            logger.removeHandler(handler)

    tests.append(("log_operation basic usage", test_log_operation_basic))

    def test_log_operation_with_level():
        """log_operation should respect log level."""
        log_capture = StringIO()
        handler = logging.StreamHandler(log_capture)
        handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        
        logger = logging.getLogger('test_level_logger')
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)
        
        try:
            log_operation('test_level_logger', 'info operation', level='INFO')
            log_operation('test_level_logger', 'debug operation', level='DEBUG')
            log_operation('test_level_logger', 'warning operation', level='WARNING')
            
            output = log_capture.getvalue()
            # Just verify it doesn't crash with different levels
            return True, None
        finally:
            logger.removeHandler(handler)

    tests.append(("log_operation with different levels", test_log_operation_with_level))

    def test_log_operation_with_kwargs():
        """log_operation should accept additional kwargs."""
        log_capture = StringIO()
        handler = logging.StreamHandler(log_capture)
        handler.setLevel(logging.DEBUG)
        
        logger = logging.getLogger('test_kwargs_logger')
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)
        
        try:
            log_operation('test_kwargs_logger', 'operation with data', 
                         level='INFO', 
                         user='admin',
                         action='create',
                         target='firewall_policy')
            return True, None
        finally:
            logger.removeHandler(handler)

    tests.append(("log_operation with kwargs", test_log_operation_with_kwargs))

    def test_log_operation_invalid_level():
        """log_operation with invalid level should handle gracefully."""
        try:
            # Invalid level might raise or use default
            log_operation('test_invalid', 'test', level='INVALID_LEVEL')
            # If it doesn't raise, that's acceptable
            return True, None
        except (ValueError, KeyError):
            # If it raises for invalid level, that's also acceptable
            return True, None

    tests.append(("log_operation invalid level handling", test_log_operation_invalid_level))

    def test_log_operation_empty_operation():
        """log_operation with empty operation string."""
        log_operation('test_empty', '')
        return True, None

    tests.append(("log_operation empty operation string", test_log_operation_empty_operation))

    def test_log_operation_special_characters():
        """log_operation should handle special characters."""
        log_operation('test_special', 'operation with <special> & "chars"')
        log_operation('test_special', 'unicode: 日本語 🔥')
        return True, None

    tests.append(("log_operation special characters", test_log_operation_special_characters))

    # =================================================================
    # Integration Tests
    # =================================================================

    def test_log_operation_logger_not_configured():
        """log_operation should not crash if logger not configured."""
        # Use a logger name that likely has no handlers
        log_operation('nonexistent_logger_12345', 'test operation')
        return True, None

    tests.append(("log_operation with unconfigured logger", test_log_operation_logger_not_configured))

    def test_log_operation_none_values():
        """log_operation should handle None in kwargs."""
        log_operation('test_none', 'operation', level='INFO', param=None)
        return True, None

    tests.append(("log_operation with None kwargs", test_log_operation_none_values))

    # =================================================================
    # Run All Tests
    # =================================================================

    print(f"\n{Colors.BOLD}log_operation Decorator Tests{Colors.RESET}")
    print("=" * 50)

    for name, test_func in tests:
        try:
            success, error = test_func()
            if success:
                passed += 1
                print_test_result(name, True)
            else:
                failed += 1
                print_test_result(name, False, error)
        except Exception as e:
            failed += 1
            print_test_result(name, False, str(e))

    print("=" * 50)
    total = passed + failed
    print(f"Results: {passed}/{total} passed", end="")
    if failed > 0:
        print(f" ({Colors.RED}{failed} failed{Colors.RESET})")
    else:
        print(f" ({Colors.GREEN}all passed{Colors.RESET})")

    return failed == 0


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
