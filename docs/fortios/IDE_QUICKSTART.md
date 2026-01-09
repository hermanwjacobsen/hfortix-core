# 🚀 Quick Start Guide - IDE Enhancements

**New in v0.5.x:** Massive improvements to IDE autocomplete and type safety!

---

## ✨ What's New

### 1. Response Types - Know What You're Getting
```python
from hfortix_fortios import FortiOS, FortiOSSuccessResponse

fgt = FortiOS(host="...", token="...")
result: FortiOSSuccessResponse = fgt.api.cmdb.firewall.policy.get()

# ✅ IDE autocompletes all response fields!
print(result["status"])        # "success"
print(result["http_status"])   # 200
print(result["results"])       # list or dict
print(result["vdom"])          # "root"
```

### 2. Dynamic Object Access - Clean Attribute Syntax
```python
# Enable object mode for clean syntax
fgt = FortiOS(..., response_mode="object")
policy = fgt.api.cmdb.firewall.policy.get(policyid=1)

# ✅ Dynamic attribute access with auto-flattening!
policy.name       # "Allow-Web"
policy.policyid   # 1
policy.action     # "accept"
policy.status     # "enable"
policy.srcaddr    # ["addr1", "addr2"] - auto-flattened!

# ✅ NEW in v0.5.17: Access raw JSON with .json property
policy.json       # Complete dict: {'name': 'Allow-Web', 'policyid': 1, ...}
delete_result = fgt.api.cmdb.firewall.policy.delete(policyid=1, response_mode="object")
delete_result.json  # {'http_method': 'DELETE', 'status': 'success', 'http_status': 200, ...}

# Access any field dynamically - works for ALL endpoints
address = fgt.api.cmdb.firewall.address.get(name="web-server")
address.name      # "web-server"
address.subnet    # "192.168.1.100/32"
address.type      # "ipmask"
```

### 3. Literal Types - No More Typos!
```python
from hfortix_fortios import ActionType, StatusType

def create_policy(
    name: str,
    action: ActionType,   # ✅ IDE shows: "accept" | "deny" | "ipsec"
    status: StatusType = "enable",  # ✅ IDE shows: "enable" | "disable"
):
    fgt.api.cmdb.firewall.policy.post(
        name=name,
        action=action,  # ✅ Type checker validates!
        status=status,
    )

# ✅ Autocomplete suggests valid values
create_policy("test", action="accept", status="enable")

# ❌ Type checker catches errors
create_policy("test", action="allow")  # Error: "allow" not valid!
```

---

## 📦 Available Types

### Response Types
```python
from hfortix_fortios import (
    FortiOSSuccessResponse,  # Successful API call
    FortiOSErrorResponse,    # Error response
    FortiOSResponse,         # Generic (success or error)
)
```

### Common Literal Types
```python
from hfortix_fortios import (
    ActionType,      # "accept" | "deny" | "ipsec"
    StatusType,      # "enable" | "disable"
    LogSeverity,     # Log levels
    ScheduleType,    # "onetime" | "recurring"
    ProtocolType,    # "tcp" | "udp" | "icmp" | ...
)
```

### Object Model
```python
from hfortix_fortios import FortiObject

# Universal wrapper for any API response
obj = FortiObject(data)
obj.name        # Dynamic access to any field
obj.status      # Works for any endpoint with these fields
obj.srcaddr     # Auto-flattened member tables
```

---

## 🎯 Usage Patterns

### Pattern 1: Type-Safe API Calls
```python
from hfortix_fortios import FortiOS, FortiOSSuccessResponse, ActionType

def manage_policy(
    fgt: FortiOS,
    name: str,
    action: ActionType = "accept",
) -> FortiOSSuccessResponse:
    """Create policy with full type safety."""
    result = fgt.api.cmdb.firewall.policy.post(
        name=name,
        action=action,
    )
    return result  # type: ignore  # (until endpoints regenerated)
```

### Pattern 2: Object Mode for Clean Code
```python
fgt = FortiOS(..., response_mode="object")

# All responses automatically wrapped with FortiObject
policies = fgt.api.cmdb.firewall.policy.get()
for policy in policies:
    if policy.status == "enable":
        print(f"{policy.name}: {policy.action}")
    # Auto-flattened member tables
    print(f"  Source addresses: {policy.srcaddr}")
```

### Pattern 3: Error Handling with Types
```python
from hfortix_core import ResourceNotFoundError
from hfortix_fortios import FortiOSErrorResponse

try:
    result = fgt.api.cmdb.firewall.address.get(name="missing")
except ResourceNotFoundError as e:
    error: FortiOSErrorResponse = e.response  # type: ignore
    print(f"Error {error['error']}: {error.get('message')}")
```

### Pattern 4: Custom Aliases with Autocomplete (NEW in v0.5.17)
```python
from hfortix_fortios import FortiOS

fgt = FortiOS(..., response_mode="object")

# Create shortcuts - autocomplete still works!
fgt.createFirewallPolicy = fgt.api.cmdb.firewall.policy.post
fgt.getFirewallPolicies = fgt.api.cmdb.firewall.policy.get
fgt.deleteFirewallPolicy = fgt.api.cmdb.firewall.policy.delete

# Use shortcuts with full autocomplete
policies = fgt.getFirewallPolicies()  # ✅ All params autocomplete

new_policy = fgt.createFirewallPolicy(  # ✅ All params autocomplete
    name="test",
    srcaddr="all",
    dstaddr="all",
    service="ALL",
    schedule="always"
)

# Access raw JSON
delete_result = fgt.deleteFirewallPolicy(policyid=123)
print(delete_result.json)  # {'status': 'success', 'http_status': 200, ...}
```

### Pattern 5: Custom Helper Class (Advanced)
```python
from typing import overload, Literal, Any
from hfortix_fortios import FortiOS
from hfortix_fortios.api.v2.cmdb.firewall.policy import PolicyObject

class MyFortiGate:
    """Custom FortiGate client with shortcuts and autocomplete"""
    
    def __init__(self, host: str, token: str, **kwargs):
        self.fgt = FortiOS(host=host, token=token, **kwargs)
        self.api = self.fgt.api  # Full API still available
    
    @overload
    def createFirewallPolicy(
        self, *, name: str, srcaddr: str = "all",
        dstaddr: str = "all", service: str = "ALL",
        response_mode: Literal["object"] = ..., **kwargs
    ) -> PolicyObject: ...
    
    def createFirewallPolicy(self, **kwargs):
        """Create policy with sensible defaults"""
        return self.fgt.api.cmdb.firewall.policy.post(**kwargs)
    
    def getFirewallPolicies(self) -> list[PolicyObject]:
        """Get all firewall policies"""
        return self.fgt.api.cmdb.firewall.policy.get()

# Perfect autocomplete on custom methods!
fgt = MyFortiGate(host="...", token="...")
policies = fgt.getFirewallPolicies()  # ✅ Autocompletes
```

---

## 🔍 IDE Features

### Autocomplete
- **Response fields**: Type `.` after result and IDE shows all fields
- **Object properties**: Type `.` after FortiObject and IDE shows properties
- **Literal values**: IDE suggests valid enum values as you type
- **Method parameters**: Hover over method to see full signature

### Type Checking (mypy)
```bash
# Install mypy
pip install mypy

# Check your code
mypy your_script.py

# Catches:
# - Invalid enum values
# - Wrong types (str instead of int)
# - Missing required fields
# - Typos in response field access
```

### Hover Documentation
Hover over any method/type to see:
- Parameter descriptions
- Example values
- Return type details
- Usage examples

---

## 🎓 Migration Guide

### From Untyped to Typed (No Breaking Changes!)

**Option 1: Gradual Adoption (Recommended)**
```python
# Works today - no changes needed
result = fgt.api.cmdb.firewall.policy.get()

# Add type hints when convenient
result: FortiOSSuccessResponse = fgt.api.cmdb.firewall.policy.get()
```

**Option 2: Enable Strict Mode**
```python
# mypy.ini
[mypy]
strict = True

# Forces type annotations on all functions
```

**Option 3: Use Object Mode**
```python
# Global setting
fgt = FortiOS(..., response_mode="object")

# Per-call override
result = fgt.api.cmdb.firewall.policy.get(response_mode="object")
```

---

## 📊 Before vs After

### Before: Guesswork
```python
result = fgt.api.cmdb.firewall.policy.get()
# 🤷 What fields exist?
# 🤷 What type is status?
# 🤷 What values are valid for action?

status = result["status"]  # Hope this exists!
data = result["results"]   # Hope this is a list!
```

### After: Confidence
```python
result: FortiOSSuccessResponse = fgt.api.cmdb.firewall.policy.get()
# ✅ IDE shows all 11 fields
# ✅ Type checker knows the types
# ✅ Autocomplete suggests valid values

status = result["status"]  # ✅ Type: Literal["success"]
data = result["results"]   # ✅ Type: list[dict] | dict

# Object mode for clean access
policy = FortiObject(data[0])
policy.name                # ✅ Dynamic attribute access
policy.srcaddr            # ✅ Auto-flattened member table
```

---

## 🔗 See Also

- **Full Documentation**: `.dev/IDE_ENHANCEMENT_SUMMARY.md`
- **Live Demo**: `examples/ide_demo.py`
- **Type Definitions**: `packages/fortios/hfortix_fortios/types.py`
- **Object Model**: `packages/fortios/hfortix_fortios/models.py`

---

## ❓ FAQ

**Q: Do I need to change existing code?**  
A: No! All changes are backward compatible. Types are optional.

**Q: Will this slow down my code?**  
A: No! Type hints are removed at runtime. Zero performance impact.

**Q: What about endpoints not yet regenerated?**  
A: They still work! Use `# type: ignore` comments until regeneration.

**Q: How do I enable strict type checking?**  
A: Install mypy (`pip install mypy`) and configure `mypy.ini`

**Q: Can I mix dict and object modes?**  
A: Yes! Set globally or override per-call with `response_mode` parameter.

**Q: How do I access raw JSON when using object mode?**  
A: Use the `.json` property: `obj.json` returns the complete dict.

**Q: Do custom aliases keep autocomplete?**  
A: Yes! `fgt.myShortcut = fgt.api.some.method` preserves all type hints and autocomplete.

**Q: Can I create my own autocomplete?**  
A: Yes! Create a custom class with type hints, or use TypedDict for configurations. See Pattern 4 & 5 above.

---

**🎉 Result: 10x Better Developer Experience!**

- ✅ Autocomplete on all response fields
- ✅ Type checking catches errors before runtime
- ✅ IDE shows valid enum values
- ✅ Clean object-style access
- ✅ Rich inline documentation
