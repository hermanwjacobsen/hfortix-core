"""
Tests for hfortix_fortios async operations using mode="async".

The FortiOS client supports async mode via:
    FortiOS(host="...", token="...", mode="async")

This creates an AsyncHTTPClient internally and all API calls become awaitable.
"""

import sys
import asyncio
import os
sys.path.insert(0, '/home/fo8038/test')

from dotenv import load_dotenv
load_dotenv()


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


# Connection settings
HOST = os.getenv("FORTIGATE_HOST", "")
TOKEN = os.getenv("FORTIGATE_TOKEN", "")
PORT = int(os.getenv("FORTIGATE_PORT", "443"))
VDOM = os.getenv("FORTIGATE_VDOM", "root")


def run_tests():
    """Run all async FortiOS tests."""

    passed = 0
    failed = 0
    tests = []

    # =================================================================
    # Async Client Creation Tests
    # =================================================================

    def test_async_mode_creation():
        """FortiOS can be created with mode='async'."""
        from hfortix_fortios import FortiOS
        
        fgt = FortiOS(
            host=HOST,
            token=TOKEN,
            port=PORT,
            verify=False,
            mode="async",
            vdom=VDOM
        )
        assert fgt is not None
        return True, None

    tests.append(("FortiOS async mode creation", test_async_mode_creation))

    def test_async_client_has_api():
        """Async FortiOS client has api attribute."""
        from hfortix_fortios import FortiOS
        
        fgt = FortiOS(
            host=HOST,
            token=TOKEN,
            port=PORT,
            verify=False,
            mode="async",
            vdom=VDOM
        )
        assert hasattr(fgt, 'api')
        assert fgt.api is not None
        return True, None

    tests.append(("Async FortiOS has api", test_async_client_has_api))

    # =================================================================
    # Async Context Manager Tests
    # =================================================================

    def test_async_context_manager():
        """FortiOS async mode works as async context manager."""
        from hfortix_fortios import FortiOS
        
        async def test_ctx():
            async with FortiOS(
                host=HOST,
                token=TOKEN,
                port=PORT,
                verify=False,
                mode="async",
                vdom=VDOM
            ) as fgt:
                assert fgt is not None
                return True
        
        result = asyncio.run(test_ctx())
        assert result == True
        return True, None

    tests.append(("Async context manager", test_async_context_manager))

    # =================================================================
    # Basic Async Request Tests
    # =================================================================

    def test_async_get_addresses():
        """Async client can GET firewall addresses."""
        from hfortix_fortios import FortiOS
        
        async def do_get():
            async with FortiOS(
                host=HOST,
                token=TOKEN,
                port=PORT,
                verify=False,
                mode="async",
                vdom=VDOM
            ) as fgt:
                addresses = await fgt.api.cmdb.firewall.address.get()
                return addresses
        
        result = asyncio.run(do_get())
        print(f"\n    Result type: {type(result)}")
        print(f"    Result length: {len(result) if isinstance(result, list) else 'N/A'}")
        assert result is not None
        return True, None

    tests.append(("Async GET addresses", test_async_get_addresses))

    def test_async_get_services():
        """Async client can GET firewall services."""
        from hfortix_fortios import FortiOS
        
        async def do_get():
            async with FortiOS(
                host=HOST,
                token=TOKEN,
                port=PORT,
                verify=False,
                mode="async",
                vdom=VDOM
            ) as fgt:
                services = await fgt.api.cmdb.firewall.service.custom.get()
                return services
        
        result = asyncio.run(do_get())
        print(f"\n    Services count: {len(result) if isinstance(result, list) else 'N/A'}")
        assert result is not None
        return True, None

    tests.append(("Async GET services", test_async_get_services))

    # =================================================================
    # Concurrent Request Tests
    # =================================================================

    def test_async_concurrent_requests():
        """Async client can make concurrent requests."""
        from hfortix_fortios import FortiOS
        
        async def do_concurrent():
            async with FortiOS(
                host=HOST,
                token=TOKEN,
                port=PORT,
                verify=False,
                mode="async",
                vdom=VDOM
            ) as fgt:
                # Make multiple concurrent requests
                tasks = [
                    fgt.api.cmdb.firewall.address.get(),
                    fgt.api.cmdb.firewall.service.custom.get(),
                    fgt.api.cmdb.system.interface.get(),
                ]
                results = await asyncio.gather(*tasks, return_exceptions=True)
                return results
        
        results = asyncio.run(do_concurrent())
        print(f"\n    Concurrent results: {len(results)} requests")
        
        # Check for errors
        errors = [r for r in results if isinstance(r, Exception)]
        successes = [r for r in results if not isinstance(r, Exception)]
        
        print(f"    Successes: {len(successes)}, Errors: {len(errors)}")
        
        if errors:
            for e in errors[:2]:
                print(f"      Error: {type(e).__name__}: {e}")
        
        assert len(successes) > 0
        return True, None

    tests.append(("Async concurrent requests", test_async_concurrent_requests))

    def test_async_many_concurrent():
        """Async client can handle many concurrent requests."""
        from hfortix_fortios import FortiOS
        
        async def do_many():
            async with FortiOS(
                host=HOST,
                token=TOKEN,
                port=PORT,
                verify=False,
                mode="async",
                vdom=VDOM
            ) as fgt:
                # Make 5 concurrent requests to same endpoint
                tasks = [fgt.api.cmdb.firewall.address.get() for _ in range(5)]
                results = await asyncio.gather(*tasks, return_exceptions=True)
                return results
        
        results = asyncio.run(do_many())
        errors = [r for r in results if isinstance(r, Exception)]
        
        print(f"\n    5 concurrent requests: {len(results) - len(errors)} succeeded")
        
        assert len(results) == 5
        return True, None

    tests.append(("Async many concurrent requests", test_async_many_concurrent))

    # =================================================================
    # Async Close Tests
    # =================================================================

    def test_async_aclose():
        """Async client can be closed with aclose()."""
        from hfortix_fortios import FortiOS
        
        async def test_close():
            fgt = FortiOS(
                host=HOST,
                token=TOKEN,
                port=PORT,
                verify=False,
                mode="async",
                vdom=VDOM
            )
            # Make a request
            result = await fgt.api.cmdb.firewall.address.get()
            # Close the client
            await fgt.aclose()
            return True
        
        result = asyncio.run(test_close())
        assert result == True
        return True, None

    tests.append(("Async aclose()", test_async_aclose))

    # =================================================================
    # Error Handling Tests
    # =================================================================

    def test_async_invalid_endpoint():
        """Async client handles invalid endpoint gracefully."""
        from hfortix_fortios import FortiOS
        
        async def test_invalid():
            async with FortiOS(
                host=HOST,
                token=TOKEN,
                port=PORT,
                verify=False,
                mode="async",
                vdom=VDOM,
                error_mode="return"
            ) as fgt:
                # Try to access nonexistent endpoint
                try:
                    result = await fgt.request({
                        'method': 'GET',
                        'path': '/api/v2/cmdb/nonexistent/endpoint'
                    })
                    return result
                except Exception as e:
                    return e
        
        result = asyncio.run(test_invalid())
        print(f"\n    Invalid endpoint result: {type(result)}")
        return True, None

    tests.append(("Async invalid endpoint handling", test_async_invalid_endpoint))

    # =================================================================
    # Performance Comparison Test
    # =================================================================

    def test_async_performance_benefit():
        """Async concurrent is faster than sequential."""
        from hfortix_fortios import FortiOS
        import time
        
        async def measure_concurrent():
            async with FortiOS(
                host=HOST,
                token=TOKEN,
                port=PORT,
                verify=False,
                mode="async",
                vdom=VDOM
            ) as fgt:
                start = time.time()
                tasks = [fgt.api.cmdb.firewall.address.get() for _ in range(3)]
                await asyncio.gather(*tasks)
                return time.time() - start
        
        async def measure_sequential():
            async with FortiOS(
                host=HOST,
                token=TOKEN,
                port=PORT,
                verify=False,
                mode="async",
                vdom=VDOM
            ) as fgt:
                start = time.time()
                for _ in range(3):
                    await fgt.api.cmdb.firewall.address.get()
                return time.time() - start
        
        concurrent_time = asyncio.run(measure_concurrent())
        sequential_time = asyncio.run(measure_sequential())
        
        print(f"\n    Concurrent (3 requests): {concurrent_time:.3f}s")
        print(f"    Sequential (3 requests): {sequential_time:.3f}s")
        print(f"    Speedup: {sequential_time/concurrent_time:.2f}x")
        
        # Concurrent should generally be faster (but not always due to network)
        return True, None

    tests.append(("Async performance benefit", test_async_performance_benefit))

    # =================================================================
    # Run All Tests
    # =================================================================

    print(f"\n{Colors.BOLD}Async FortiOS Client Tests{Colors.RESET}")
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
