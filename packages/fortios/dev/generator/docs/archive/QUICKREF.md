# Quick Reference - Generator Commands

**Last Updated:** January 3, 2026  
**Validated With:** cmdb.firewall.policy

---

## 🚀 Generate an Endpoint

```bash
cd /app/dev/classes/fortinet/.dev/generator
python generate_firewall_policy.py
```

**Output:**
- `packages/fortios/hfortix_fortios/api/v2/cmdb/firewall/policy.py`
- `packages/fortios/hfortix_fortios/api/v2/cmdb/firewall/_helpers/policy.py`

---

## 🧪 Run Tests

```bash
cd /app/dev/classes/fortinet

# All tests for firewall.policy
pytest .tests/pytests/api/cmdb/firewall/ -v

# Just API integration tests
pytest .tests/pytests/api/cmdb/firewall/test_policy.py -v

# Just validator tests
pytest .tests/pytests/api/cmdb/firewall/test_policy_validators.py -v

# Single test
pytest .tests/pytests/api/cmdb/firewall/test_policy.py::TestFirewallPolicy::test_1_list_all_policies -v
```

**Expected:** 38/38 passing

---

## 📝 Create Tests for New Endpoint

**Example: firewall.address**

```bash
# Create test directory structure (if needed)
mkdir -p .tests/pytests/api/cmdb/firewall

# Create __init__.py files
touch .tests/pytests/api/__init__.py
touch .tests/pytests/api/cmdb/__init__.py
touch .tests/pytests/api/cmdb/firewall/__init__.py

# Create test files
cp .tests/pytests/api/cmdb/firewall/test_policy.py \
   .tests/pytests/api/cmdb/firewall/test_address.py

cp .tests/pytests/api/cmdb/firewall/test_policy_validators.py \
   .tests/pytests/api/cmdb/firewall/test_address_validators.py

# Edit test files to match new endpoint
# Update: endpoint path, test data, field names
```

---

## 🔍 Check Generated Code

```bash
cd /app/dev/classes/fortinet

# Check for syntax errors with Pylance
# (Open in VS Code - should show 0 errors)

# Quick syntax check with Python
python -m py_compile packages/fortios/hfortix_fortios/api/v2/cmdb/firewall/policy.py
python -m py_compile packages/fortios/hfortix_fortios/api/v2/cmdb/firewall/_helpers/policy.py
```

**Expected:** No errors

---

## 📦 Import Generated Endpoint

```python
from hfortix_fortios import FortiOS

# Initialize client
fgt = FortiOS(
    host="192.168.1.99",
    token="your-api-token",
    vdom="root"
)

# Use generated endpoint
policies = fgt.api.cmdb.firewall.policy.get()
print(f"Found {len(policies)} policies")

# Create new policy
result = fgt.api.cmdb.firewall.policy.post(
    name="Test Policy",
    srcintf=[{"name": "port1"}],
    dstintf=[{"name": "port2"}],
    srcaddr=[{"name": "all"}],
    dstaddr=[{"name": "all"}],
    service=[{"name": "ALL"}],
    schedule="always",
    action="accept"
)

# Check if exists
exists = fgt.api.cmdb.firewall.policy.exists(policyid=100)

# Update
fgt.api.cmdb.firewall.policy.put(
    policyid=100,
    status="disable"
)

# Delete
fgt.api.cmdb.firewall.policy.delete(policyid=100)
```

---

## 🛠️ Troubleshooting

### Generator Issues

**Problem:** Template rendering fails

```bash
# Check template syntax
cd .dev/generator
python -c "from jinja2 import Environment, FileSystemLoader; \
    env = Environment(loader=FileSystemLoader('templates')); \
    env.get_template('endpoint_class.py.j2')"
```

**Problem:** Generated code has syntax errors

```bash
# Check for whitespace control markers in templates
grep -n "{%-\|-%}" templates/*.j2

# Should return nothing - these cause issues
```

### Test Issues

**Problem:** Tests fail to import endpoint

```bash
# Check PYTHONPATH includes packages/fortios
export PYTHONPATH=/app/dev/classes/fortinet/packages/fortios:$PYTHONPATH

# Or install in development mode
cd packages/fortios
pip install -e .
```

**Problem:** FortiGate connection fails

```bash
# Test connection
curl -k -H "Authorization: Bearer YOUR_TOKEN" \
  https://YOUR_FORTIGATE/api/v2/cmdb/system/status

# Check VDOM exists
curl -k -H "Authorization: Bearer YOUR_TOKEN" \
  https://YOUR_FORTIGATE/api/v2/cmdb/system/vdom
```

### Import Issues

**Problem:** Cannot import generated endpoint

```python
# Check sys.path
import sys
print('\n'.join(sys.path))

# Check file exists
import os
path = "packages/fortios/hfortix_fortios/api/v2/cmdb/firewall/policy.py"
print(f"Exists: {os.path.exists(path)}")
```

---

## 📊 Validation Checklist

Before moving to next endpoint:

- [ ] Generated endpoint has 0 Pylance errors
- [ ] Generated validator has 0 Pylance errors
- [ ] At least 5 API integration tests created
- [ ] At least 20 validator unit tests created
- [ ] All tests passing (100%)
- [ ] Cleanup mechanism working
- [ ] Documentation updated
- [ ] Example usage written

---

## 🔗 File Locations

**Generator Files:**
```
.dev/generator/
├── generate_firewall_policy.py       # Generator script
├── schema_parser.py                  # Schema parser
├── generators/
│   ├── endpoint_generator.py         # Endpoint generator
│   └── validator_generator.py        # Validator generator
└── templates/
    ├── endpoint_class.py.j2          # Endpoint template
    └── validator.py.j2               # Validator template
```

**Generated Files:**
```
packages/fortios/hfortix_fortios/api/v2/
└── cmdb/firewall/
    ├── policy.py                     # Generated endpoint
    └── _helpers/policy.py            # Generated validators
```

**Test Files:**
```
.tests/pytests/api/cmdb/firewall/
├── test_policy.py                    # API tests
└── test_policy_validators.py        # Validator tests
```

**Documentation:**
```
.dev/generator/
├── WORKFLOW_GUIDE.md                 # Complete workflow guide
├── CHANGELOG.md                      # Development changelog
├── README.md                         # Generator overview
└── QUICKREF.md                       # This file
```

---

## 💡 Common Tasks

### Generate New Endpoint

1. Get or create schema JSON file
2. Copy and modify generate script
3. Run generator
4. Create tests
5. Validate

### Update Existing Endpoint

1. Update schema JSON (if schema changed)
2. Re-run generator
3. Update tests (if needed)
4. Validate

### Debug Generated Code

1. Check Pylance errors in VS Code
2. Run syntax check: `python -m py_compile file.py`
3. Check imports work: `python -c "from module import Class"`
4. Run tests: `pytest test_file.py -v`

### Add New Validation

1. Update validator.py.j2 template
2. Regenerate endpoint
3. Add validator tests
4. Run tests

---

**Need Help?**
- See [WORKFLOW_GUIDE.md](WORKFLOW_GUIDE.md) for complete details
- Check [CHANGELOG.md](CHANGELOG.md) for lessons learned
- Review [test examples](.tests/pytests/api/cmdb/firewall/) for patterns
