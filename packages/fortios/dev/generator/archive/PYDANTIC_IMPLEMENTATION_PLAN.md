# Pydantic Model Generator Implementation Plan

**Date:** January 6, 2026  
**Branch:** feature/validator-generation  
**Archive:** pre-pydantic-20260106_190731

## Overview

We're implementing three major enhancements to the code generator:
1. **Pydantic Model Generation** - Runtime validation models
2. **Field Validation** - Constraints from schema metadata  
3. **Capabilities Integration** - Expose capabilities as constants

## Phase 1: Pydantic Model Generator (NEW)

### 1.1 Create Model Generator Module
**File:** `generators/model_generator.py`

**Responsibilities:**
- Generate Pydantic BaseModel classes from schemas
- Parse field validation rules (min/max/pattern/length)
- Handle nested models for child tables
- Generate Enum classes for complex option sets
- Use Literal types for simple enums (2-3 values)

**Key Methods:**
```python
class ModelGenerator:
    def __init__(self, template_dir: Path)
    def generate(self, schema: EndpointSchema, output_dir: Path) -> Path
    def _generate_field_definition(self, field: FieldMetadata) -> str
    def _generate_child_model(self, child_table: dict) -> str
    def _should_use_enum(self, allowed_values: list) -> bool  # 4+ values
```

### 1.2 Create Model Template
**File:** `templates/pydantic_model.py.j2`

**Structure:**
```python
"""Pydantic models for {{ schema.path }}"""
from pydantic import BaseModel, Field
from typing import Literal
from enum import Enum
from uuid import UUID

# Child table models (if any)
{% for child in schema.child_tables %}
class {{ child.class_name }}(BaseModel):
    """{{ child.help }}"""
    {% for field in child.fields %}
    {{ field.python_name }}: {{ field.pydantic_type }} = Field(
        {{ field.constraints }},
        description="{{ field.help }}"
    )
    {% endfor %}
{% endfor %}

# Main model
class {{ schema.pydantic_class_name }}(BaseModel):
    """{{ schema.help }}"""
    {% for field in schema.fields %}
    {{ field.python_name }}: {{ field.pydantic_type }} = Field(
        {{ field.constraints }},
        description="{{ field.help }}"
    )
    {% endfor %}
```

**Output Location:**
- `packages/fortios/hfortix_fortios/models/cmdb/firewall/policy.py`
- `packages/fortios/hfortix_fortios/models/monitor/...`
- etc.

## Phase 2: Endpoint Generator Enhancements

### 2.1 Add Capabilities Constants
**Update:** `templates/endpoint_class.py.j2`

**Add to class definition:**
```python
class {{ schema.class_name }}(MetadataMixin):
    """{{ schema.class_name }} Operations."""
    
    # Capabilities from schema
    SUPPORTS_CREATE = {{ schema.capabilities.crud.create|default(false)|lower }}
    SUPPORTS_READ = {{ schema.capabilities.crud.read|default(true)|lower }}
    SUPPORTS_UPDATE = {{ schema.capabilities.crud.update|default(false)|lower }}
    SUPPORTS_DELETE = {{ schema.capabilities.crud.delete|default(false)|lower }}
    SUPPORTS_MOVE = {{ schema.capabilities.actions.move|default(false)|lower }}
    SUPPORTS_CLONE = {{ schema.capabilities.actions.clone|default(false)|lower }}
    SUPPORTS_FILTERING = {{ schema.capabilities.features.filtering|default(false)|lower }}
    SUPPORTS_PAGINATION = {{ schema.capabilities.features.pagination|default(false)|lower }}
    
    # Metadata
    ENDPOINT_TYPE = "{{ schema.capabilities.endpoint_type|default('unknown') }}"
    MAX_TABLE_SIZE = {{ schema.capabilities.limits.max_table_size_vdom|default(0) }}
```

### 2.2 Add Action Methods
**Update:** `templates/endpoint_class.py.j2`

**Add move() method** (if `capabilities.actions.move == true`):
```python
{% if schema.capabilities.actions.move %}
def move(
    self,
    {{ schema.mkey|kebab_to_snake }}: {{ schema.mkey_type|to_python_type }},
    action: Literal["before", "after"],
    reference_id: {{ schema.mkey_type|to_python_type }},
    vdom: str | bool | None = None,
    **kwargs: Any,
) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
    """
    Move {{ schema.path }} object relative to another.
    
    Args:
        {{ schema.mkey|kebab_to_snake }}: Object identifier to move
        action: Position relative to reference ("before" or "after")
        reference_id: Reference object identifier
        vdom: Virtual domain
        **kwargs: Additional parameters
        
    Returns:
        API response
    """
    if not self.SUPPORTS_MOVE:
        raise NotSupportedError(f"Move operation not supported for {self.__class__.__name__}")
    
    params = {"action": "move", action: reference_id}
    params.update(kwargs)
    
    return self._client.put(
        "{{ schema.category }}",
        f"/{{ schema.path }}/{{ '{' }}{{ schema.mkey }}{{ '}' }}".format(
            {{ schema.mkey }}={{ schema.mkey|kebab_to_snake }}
        ),
        params=params,
        vdom=vdom,
    )
{% endif %}
```

**Add clone() method** (if `capabilities.actions.clone == true`):
```python
{% if schema.capabilities.actions.clone %}
def clone(
    self,
    {{ schema.mkey|kebab_to_snake }}: {{ schema.mkey_type|to_python_type }},
    new_{{ schema.mkey|kebab_to_snake }}: {{ schema.mkey_type|to_python_type }},
    vdom: str | bool | None = None,
    **kwargs: Any,
) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
    """
    Clone {{ schema.path }} object.
    
    Args:
        {{ schema.mkey|kebab_to_snake }}: Source object identifier
        new_{{ schema.mkey|kebab_to_snake }}: New object identifier
        vdom: Virtual domain
        **kwargs: Additional parameters
        
    Returns:
        API response with cloned object
    """
    if not self.SUPPORTS_CLONE:
        raise NotSupportedError(f"Clone operation not supported for {self.__class__.__name__}")
    
    params = {"action": "clone", "nkey": str(new_{{ schema.mkey|kebab_to_snake }})}
    params.update(kwargs)
    
    return self._client.post(
        "{{ schema.category }}",
        f"/{{ schema.path }}/{{ '{' }}{{ schema.mkey }}{{ '}' }}".format(
            {{ schema.mkey }}={{ schema.mkey|kebab_to_snake }}
        ),
        params=params,
        vdom=vdom,
    )
{% endif %}
```

### 2.3 Add exists() Helper
**Add to all endpoints:**
```python
def exists(
    self,
{% if schema.mkey %}
    {{ schema.mkey|kebab_to_snake }}: {{ schema.mkey_type|to_python_type }},
{% else %}
    name: str,
{% endif %}
    vdom: str | bool | None = None,
) -> Union[bool, Coroutine[Any, Any, bool]]:
    """
    Check if {{ schema.path }} object exists.
    
    Args:
{% if schema.mkey %}
        {{ schema.mkey|kebab_to_snake }}: Object identifier
{% else %}
        name: Object name
{% endif %}
        vdom: Virtual domain
        
    Returns:
        True if object exists, False otherwise
    """
    try:
{% if schema.mkey %}
        result = self.get({{ schema.mkey|kebab_to_snake }}={{ schema.mkey|kebab_to_snake }}, vdom=vdom)
{% else %}
        result = self.get(name=name, vdom=vdom)
{% endif %}
        return is_success(result)
    except Exception:
        return False
```

## Phase 3: Schema Parser Updates

### 3.1 Parse Capabilities
**Update:** `schema_management/schema_parser.py`

**Add capabilities to EndpointSchema:**
```python
@dataclass
class EndpointSchema:
    # ... existing fields ...
    capabilities: dict[str, Any] | None = None
    
    @classmethod
    def from_dict(cls, data: dict) -> "EndpointSchema":
        # ... existing code ...
        capabilities = data.get("capabilities", {})
        # ... add to return statement ...
```

### 3.2 Parse Field Validation
**Update:** `schema_management/schema_parser.py`

**Enhance FieldMetadata:**
```python
@dataclass
class FieldMetadata:
    # ... existing fields ...
    validation: dict[str, Any] | None = None  # min, max, max_length, pattern
    datasource: str | None = None
    child_tables: list[dict] | None = None
    
    def get_pydantic_constraints(self) -> str:
        """Generate Pydantic Field() constraints."""
        constraints = []
        
        if self.validation:
            if "min" in self.validation:
                constraints.append(f"ge={self.validation['min']}")
            if "max" in self.validation:
                constraints.append(f"le={self.validation['max']}")
            if "max_length" in self.validation:
                constraints.append(f"max_length={self.validation['max_length']}")
            if "pattern" in self.validation:
                constraints.append(f'pattern=r"{self.validation["pattern"]}"')
        
        if self.default_value is not None:
            if isinstance(self.default_value, str):
                constraints.append(f'default="{self.default_value}"')
            else:
                constraints.append(f"default={self.default_value}")
        
        if self.help:
            constraints.append(f'description="{self.help}"')
        
        return ", ".join(constraints) if constraints else ""
```

## Phase 4: Integration & Testing

### 4.1 Update Main Generator Script
**Update:** `generate.py`

**Add model generation:**
```python
from generators.model_generator import ModelGenerator

# Initialize generators
model_gen = ModelGenerator(templates_dir)
endpoint_gen = EndpointGenerator(templates_dir)

# Generate for each schema
for schema_file in schema_files:
    schema = EndpointSchema.from_file(schema_file)
    
    # Generate Pydantic model
    model_file = model_gen.generate(schema, models_dir)
    print(f"✅ Model: {model_file}")
    
    # Generate endpoint class
    endpoint_file = endpoint_gen.generate(schema, endpoints_dir)
    print(f"✅ Endpoint: {endpoint_file}")
```

### 4.2 Test with Sample Schema
**Test with:** `schema/7.6.5/cmdb/firewall.policy.json`

**Expected Output:**
```
packages/fortios/hfortix_fortios/
├── models/
│   └── cmdb/
│       └── firewall/
│           └── policy.py  # Pydantic models
└── api/
    └── v2/
        └── cmdb/
            └── firewall/
                └── policy.py  # Endpoint with capabilities
```

### 4.3 Validation Tests
**Create:** `tests/test_pydantic_models.py`

```python
def test_firewall_policy_model():
    """Test FirewallPolicy Pydantic model."""
    from hfortix_fortios.models.cmdb.firewall.policy import FirewallPolicy
    
    # Valid policy
    policy = FirewallPolicy(
        policyid=1,
        name="test-policy",
        action="accept",
    )
    assert policy.policyid == 1
    
    # Test validation - policyid out of range
    with pytest.raises(ValidationError):
        FirewallPolicy(policyid=9999999999, name="test")
    
    # Test validation - name too long
    with pytest.raises(ValidationError):
        FirewallPolicy(policyid=1, name="x" * 100)
```

## Phase 5: Documentation

### 5.1 Update TODO.md
- Mark Pydantic Models as 100% complete
- Mark Validation as 100% complete  
- Mark Capabilities as 100% complete

### 5.2 Create User Guide
**File:** `docs/fortios/PYDANTIC_MODELS_GUIDE.md`

**Content:**
- How to use Pydantic models
- Validation examples
- Capabilities constants usage
- Action methods (move/clone)
- Migration from dict-based to model-based

### 5.3 Update CHANGELOG.md
```markdown
## [0.6.0] - 2026-01-06

### Added
- **Pydantic Models** - Runtime validation for all 1,348 endpoints
- **Field Constraints** - min/max/length/pattern validation from schemas
- **Capabilities Constants** - SUPPORTS_* flags for all endpoints
- **Action Methods** - move() and clone() where supported
- **exists() Helper** - Check object existence on all endpoints

### Changed
- Generator now creates Pydantic models alongside endpoint classes
- Endpoint classes now include capabilities metadata
- Validation happens at instantiation time, not just API call time
```

## Timeline

**Day 1 (Today):**
- ✅ Archive current generator
- ⬜ Create ModelGenerator class
- ⬜ Create Pydantic model template
- ⬜ Test with firewall.policy schema

**Day 2:**
- ⬜ Update endpoint template with capabilities
- ⬜ Add move()/clone() methods
- ⬜ Add exists() helper
- ⬜ Update schema parser

**Day 3:**
- ⬜ Integrate into main generator
- ⬜ Regenerate all 1,348 endpoints
- ⬜ Run tests
- ⬜ Update documentation

## Success Criteria

- ✅ All 1,348 endpoints have Pydantic models
- ✅ 90%+ fields have validation constraints
- ✅ All endpoints have capabilities constants
- ✅ move()/clone() methods where supported
- ✅ exists() helper on all endpoints
- ✅ All tests passing
- ✅ Documentation updated

## Risks & Mitigation

**Risk:** Breaking changes to existing code
**Mitigation:** Pydantic models are optional - existing dict-based usage still works

**Risk:** Package size increase
**Mitigation:** Models in separate module, can be lazy-loaded

**Risk:** Performance impact of validation
**Mitigation:** Pydantic is fast, validation optional via model_validate()

## Notes

- Keep backward compatibility - existing code must continue to work
- Pydantic models are opt-in enhancement
- Focus on cmdb endpoints first (most complex)
- Monitor endpoints may need special handling
- Archive created at: `archive/pre-pydantic-20260106_190731/`
