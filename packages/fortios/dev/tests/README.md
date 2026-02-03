# HFortix Test Suite

Complete test suite for the HFortix SDK, including both schema validators and live integration tests.

## Test Suites

### 1. Schema Validators (1,447 tests)
- **Location**: `.tests/schema-validators/`
- **Purpose**: Validate generated code structure and validators
- **Requirements**: No live FortiGate/FortiManager needed
- **Execution**: Parallel (fast)
- **Coverage**:
  - Validator function imports (561 CMDB, 490 Monitor, 286 Log, 11 Service endpoints)
  - Required field validation
  - Enum value validation
  - Type checking
  - API request inspection properties (`http_api_request`, `fmg_api_request`)

**Special Tests**:
- `test_api_request_properties.py` - Validates `http_api_request` and `fmg_api_request` properties (8 comprehensive tests)
- `example_api_request_inspection.py` - Demonstrates HTTP request inspection feature with examples

### 2. Live Integration Tests
- **Location**: `.tests/live/`
- **Purpose**: Test real API calls against live devices
- **Requirements**: Live FortiGate and/or FortiManager access
- **Execution**: Sequential (respects API rate limits)
- **Coverage**:
  - FortiGate Direct Client
  - FortiManager Proxy Client
  - CMDB, Monitor, Log, and Service APIs
  - Real-world scenarios

## Quick Start

### Run All Tests
```bash
cd .tests
python3 run_all_tests.py
```

### Run Only Schema Validators (Fast, No API Calls)
```bash
python3 run_all_tests.py --schema-only
```

### Run Only Live Integration Tests
```bash
# Both FGT and FMG clients
python3 run_all_tests.py --live-only

# FGT client only
python3 run_all_tests.py --live-only --live-client=fgt

# FMG proxy client only
python3 run_all_tests.py --live-only --live-client=fmg
```

### Skip Cleanup Before Live Tests
```bash
python3 run_all_tests.py --no-cleanup
```

### Verbose Output
```bash
python3 run_all_tests.py --verbose
```

## Individual Test Runners

### Schema Validators
```bash
cd .tests/schema-validators
python3 __runtests__.py              # All tests
python3 __runtests__.py --cmdb       # Only CMDB
python3 __runtests__.py --monitor    # Only Monitor
```

### Live Integration Tests
```bash
cd .tests/live
python3 __runtests__.py                    # FGT client (default)
python3 __runtests__.py --client=fgt       # FGT client
python3 __runtests__.py --client=fmg_proxy # FMG proxy client
python3 __runtests__.py --client=both      # Both clients
python3 __runtests__.py --quiet            # Minimal output
```

## Exit Codes

- `0` - All tests passed
- `1` - Some tests failed
- `2` - Configuration/environment error

## Test Configuration

### For Live Tests
Configure FortiGate/FortiManager connection in `.tests/__client__.py`:

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

## Test Coverage Summary

| Test Suite             | Files            | Tests  | Duration | API Calls |
| ---------------------- | ---------------- | ------ | -------- | --------- |
| Schema Validators      | 786              | 1,447  | ~5s      | None      |
| Live Integration (FGT) | Auto-discovered  | Varies | Varies   | Yes       |
| Live Integration (FMG) | Auto-discovered  | Varies | Varies   | Yes       |

## CI/CD Integration

### GitHub Actions Example
```yaml
name: Tests

on: [push, pull_request]

jobs:
  schema-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - run: pip install -e packages/fortios
      - run: cd .tests && python3 run_all_tests.py --schema-only

  integration-tests:
    runs-on: ubuntu-latest
    # Only run on main branch or specific conditions
    if: github.ref == 'refs/heads/main'
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - run: pip install -e packages/fortios
      - run: cd .tests && python3 run_all_tests.py --live-only
        env:
          FORTIOS_HOST: ${{ secrets.FORTIOS_HOST }}
          FORTIOS_TOKEN: ${{ secrets.FORTIOS_TOKEN }}
```

## Troubleshooting

### Schema Validators Fail
- Ensure packages are installed: `pip install -e packages/fortios`
- Check Python version: `python3 --version` (requires 3.10+)
- Run with verbose: `python3 run_all_tests.py --schema-only --verbose`

### Live Tests Fail
- Verify FortiGate/FortiManager connectivity
- Check credentials in `.tests/__client__.py`
- Run cleanup: `cd .tests/live && python3 cleanup.py`
- Check API permissions for the API user

### Permission Errors
```bash
chmod +x .tests/run_all_tests.py
chmod +x .tests/schema-validators/__runtests__.py
chmod +x .tests/live/__runtests__.py
```

## Development Workflow

1. **Before commits**: Run schema validators (fast)
   ```bash
   python3 run_all_tests.py --schema-only
   ```

2. **Before releases**: Run all tests
   ```bash
   python3 run_all_tests.py
   ```

3. **During development**: Run specific suites
   ```bash
   python3 run_all_tests.py --live-only --live-client=fgt
   ```

## Notes

- `.tests/` directory is gitignored
- Schema validators can run offline
- Live tests require network access to FortiGate/FortiManager
- Tests run sequentially by default to avoid overwhelming devices
- Cleanup runs automatically before live tests (use `--no-cleanup` to skip)
