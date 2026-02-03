# HFortix Test Suite Index

## Directory Structure

```text
.tests/
├── run_all_tests.py          # Unified test runner for all suites
├── __client__.py             # Client configuration for live tests
├── conftest.py               # Root pytest configuration
├── README.md                 # Test suite documentation
├── INDEX.md                  # This file
├── TESTCOVERAGE.md           # Detailed test coverage report
│
├── schema-validators/        # Schema and validator tests (NO API CALLS)
│   ├── __runtests__.py       # Schema validator test runner
│   ├── conftest.py           # Pytest configuration
│   ├── README.md             # Schema validator documentation
│   ├── test_api_request_properties.py  # API request inspection tests (8 tests)
│   ├── example_api_request_inspection.py  # Request inspection examples
│   └── api/                  # Generated validator tests (786 files)
│       ├── cmdb/             # CMDB endpoint validators (561 files)
│       ├── monitor/          # Monitor endpoint validators (490 files)
│       ├── log/              # Log endpoint validators (286 files)
│       └── service/          # Service endpoint validators (11 files)
│
└── live/                     # Live integration tests (REQUIRES API ACCESS)
    ├── __runtests__.py       # Live test runner
    ├── cleanup.py            # Test object cleanup utility
    ├── conftest.py           # Pytest configuration
    ├── fgtclient.py          # FortiGate client fixture
    ├── fmgclient.py          # FortiManager client fixture
    │
    ├── endpoints/            # Endpoint-specific integration tests
    │   ├── cmdb/             # CMDB API tests
    │   ├── monitor/          # Monitor API tests
    │   ├── log/              # Log API tests
    │   └── service/          # Service API tests
    │
    ├── fmgproxy/             # FortiManager proxy client tests
    │   └── test_client.py
    │
    ├── integration/          # Integration scenario tests
    │   ├── test_fortios_client.py
    │   ├── test_hooks.py
    │   └── test_http_client_stats.py
    │
    ├── unit/                 # Unit tests for SDK components
    │   ├── test_api_utils.py
    │   ├── test_async_client.py
    │   ├── test_encode_path.py
    │   ├── test_exception_utils.py
    │   ├── test_format_utils.py
    │   ├── test_forti_object_types.py
    │   ├── test_http_client_advanced.py
    │   ├── test_http_client_utils.py
    │   ├── test_log_operation.py
    │   ├── test_print_debug.py
    │   ├── test_process_response.py
    │   ├── test_response_types.py
    │   └── test_runner_and_cleanup.py
    │
    ├── validators/           # Validator component tests
    │   ├── test_audit_formatters.py
    │   ├── test_audit_handlers.py
    │   ├── test_builders.py
    │   ├── test_cache.py
    │   ├── test_configure_logging.py
    │   ├── test_converters.py
    │   ├── test_core_types.py
    │   ├── test_credential_validation.py
    │   ├── test_debug_formatters.py
    │   ├── test_debug_session.py
    │   ├── test_debug_timer.py
    │   ├── test_deprecation.py
    │   ├── test_endpoint_validators.py
    │   ├── test_exceptions.py
    │   ├── test_firewall_validators.py
    │   ├── test_fmt.py
    │   ├── test_formatting_validators.py
    │   ├── test_forti_object.py
    │   ├── test_fortios_formatting.py
    │   ├── test_fortios_types.py
    │   ├── test_generic_validators.py
    │   ├── test_help_function.py
    │   ├── test_helpers.py
    │   ├── test_logging_formatters.py
    │   ├── test_metadata_functions.py
    │   ├── test_metadata_mixin.py
    │   ├── test_metadata.py
    │   ├── test_network_validators.py
    │   ├── test_normalize_keys.py
    │   ├── test_normalizers.py
    │   ├── test_readonly_cache.py
    │   ├── test_request_logger.py
    │   ├── test_response_helpers_extra.py
    │   ├── test_response_helpers.py
    │   ├── test_schedule_validators.py
    │   ├── test_ssh_ssl_validators.py
    │   └── (40+ more validator test files)
    │
    ├── other/                # Miscellaneous test scenarios
    │   ├── kwargs.py
    │   ├── object.py
    │   ├── realw_object1.py
    │   └── test_formatting.py
    │
    └── x_edge_cases/         # Edge case tests
        └── (various edge case scenarios)
```

## Test Categories

### 1. Schema Validators (`schema-validators/`)
**Purpose**: Validate generated code structure and validator functions  
**API Calls**: ❌ None (offline tests)  
**Execution Time**: ~5 seconds  
**Test Count**: 1,447 tests across 786 files  

**Coverage**:
- CMDB endpoint validators (561 files)
- Monitor endpoint validators (490 files)
- Log endpoint validators (286 files)
- Service endpoint validators (11 files)

**What's Tested**:
- Validator function imports and availability
- Required field validation logic
- Enum value validation
- Type checking for all parameters
- Generated code syntax and structure

### 2. Live Integration Tests (`live/`)
**Purpose**: Test real API interactions with FortiGate/FortiManager  
**API Calls**: ✅ Yes (requires live devices)  
**Execution Time**: Varies (respects rate limits)  
**Test Count**: Auto-discovered  

**Coverage Areas**:

#### a. Endpoint Tests (`endpoints/`)
- **CMDB**: Configuration database operations (GET, POST, PUT, DELETE)
- **Monitor**: System monitoring and status queries
- **Log**: Log retrieval and filtering
- **Service**: Service-level operations

#### b. Client Tests (`fmgproxy/`, `integration/`)
- FortiGate direct client functionality
- FortiManager proxy client functionality
- HTTP client statistics and performance
- Request/response hooks and callbacks

#### c. Unit Tests (`unit/`)
- API utility functions
- Async client operations
- Path encoding and URL handling
- Exception handling and error recovery
- Response processing and formatting
- Type conversion and validation
- Debug and logging functionality

#### d. Validator Tests (`validators/`)
- Audit logging and formatters
- Debug session management
- Cache implementations
- Credential validation
- Network parameter validators
- Firewall object validators
- Schedule and time validators
- SSH/SSL configuration validators
- Metadata handling
- Object normalization
- Response helpers

## Quick Reference

### Run All Tests
```bash
cd .tests
python3 run_all_tests.py
```

### Run Specific Suite
```bash
# Schema validators only (fast, no API)
python3 run_all_tests.py --schema-only

# Live tests only (requires API access)
python3 run_all_tests.py --live-only

# Live tests - specific client
python3 run_all_tests.py --live-only --live-client=fgt
python3 run_all_tests.py --live-only --live-client=fmg
```

### Run Individual Test Files
```bash
# Schema validators
cd schema-validators
python3 __runtests__.py --cmdb      # Only CMDB
python3 __runtests__.py --monitor   # Only Monitor

# Live tests
cd live
python3 __runtests__.py --client=fgt
pytest endpoints/cmdb/               # Specific endpoint
pytest unit/test_api_utils.py        # Specific file
```

## Test Markers

### Schema Validators
- `@pytest.mark.validator` - Validator function tests

### Live Tests
- `@pytest.mark.api_call` - Requires live API access
- `@pytest.mark.fgt` - FortiGate direct client
- `@pytest.mark.fmg` - FortiManager proxy client
- `@pytest.mark.cmdb` - CMDB endpoint tests
- `@pytest.mark.monitor` - Monitor endpoint tests
- `@pytest.mark.log` - Log endpoint tests

## Configuration

### Client Configuration (`__client__.py`)
```python
# FortiGate Direct Connection
FGT_HOST = "192.168.1.99"
FGT_TOKEN = "your-api-token"

# FortiManager Proxy Connection
FMG_HOST = "192.168.1.98"
FMG_TOKEN = "your-fmg-token"
FMG_ADOM = "root"
FMG_DEVICE = "FGT-001"
```

### Environment Variables (Optional)
```bash
export FORTIOS_HOST="192.168.1.99"
export FORTIOS_TOKEN="your-api-token"
export FMG_HOST="192.168.1.98"
export FMG_TOKEN="your-fmg-token"
```

## Related Documentation

- **README.md**: Test suite overview and quick start guide
- **TESTCOVERAGE.md**: Detailed test coverage metrics and analysis
- **schema-validators/README.md**: Schema validator specific documentation
- **live/validators/README.md**: Validator component documentation

## Notes

- The `others/` directory contains experimental/scratch tests and is not part of the main test suite
- All tests in `.tests/` are gitignored
- Schema validators can run completely offline
- Live tests require network access to FortiGate/FortiManager devices
- Test cleanup runs automatically before live tests (use `--no-cleanup` to skip)
