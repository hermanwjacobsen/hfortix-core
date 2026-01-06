# 📋 hfortix TODO List

**Last Updated:** January 6, 2026  
**Branch:** `feature/validator-generation`  
**Overall Progress:** 60% Complete

This document combines all TODO items for the hfortix project, including Schema v1.7.0 implementation and future feature enhancements.

---

## 🔥 CRITICAL PRIORITY - Schema v1.7.0 Implementation (Next 1-2 Days)

### 1. ✅ Pydantic Model Generation [0% → 100%]
**Status:** ❌ NOT STARTED  
**Effort:** 1-2 days  
**Impact:** 🔴 CRITICAL

**Tasks:**
- [ ] Update endpoint generator to create Pydantic BaseModel classes
- [ ] Generate model classes in `/packages/fortios/hfortix_fortios/models/`
- [ ] Use schema `pydantic_class_name` for class names
- [ ] Import models in endpoint classes
- [ ] Update endpoint methods to accept/return Pydantic models

**Example Output:**
```python
# In /packages/fortios/hfortix_fortios/models/cmdb/firewall.py
from pydantic import BaseModel, Field

class FirewallPolicy(BaseModel):
    """Firewall Policy configuration model."""
    
    policyid: int = Field(
        ge=0,
        le=4294967294,
        description="Policy ID (mkey)"
    )
    
    name: str = Field(
        max_length=35,
        description="Policy name"
    )
```

**Files to Update:**
- `generators/endpoint_generator.py` (or equivalent)
- Add new `generators/model_generator.py`
- Update templates if using Jinja2

### 2. ✅ Field() Constraints from Schema [0% → 100%]
**Status:** ❌ NOT STARTED  
**Effort:** Included in task #1  
**Impact:** 🔴 CRITICAL

**Tasks:**
- [ ] Parse `validation.min` → `Field(ge=...)`
- [ ] Parse `validation.max` → `Field(le=...)`
- [ ] Parse `validation.max_length` → `Field(max_length=...)`
- [ ] Parse `validation.pattern` → `Field(pattern=r'...')`
- [ ] Parse `example` → `Field(example='...')`
- [ ] Parse `default_value` → `Field(default=...)`

**Schema Mapping:**
```python
# validation.min/max → Field(ge=, le=)
"policyid": {"validation": {"min": 0, "max": 4294967294}}
→ policyid: int = Field(ge=0, le=4294967294)

# validation.pattern → Field(pattern=)
"uuid": {"validation": {"pattern": "^[0-9a-f]{8}-..."}}
→ uuid: str = Field(pattern=r'^[0-9a-f]{8}-...')

# validation.max_length → Field(max_length=)
"name": {"validation": {"max_length": 35}}
→ name: str = Field(max_length=35)
```

### 3. ✅ Enum Generation for Allowed Values [0% → 100%]
**Status:** ❌ NOT STARTED  
**Effort:** 4-6 hours  
**Impact:** 🔴 HIGH

**Tasks:**
- [ ] Parse `allowed_values` from schema
- [ ] Generate Enum classes for fields with allowed values
- [ ] Use Literal[] for simple enums (2-3 values)
- [ ] Use str Enum for complex enums (4+ values)
- [ ] Reference enums in Pydantic models

**Example:**
```python
from enum import Enum
from typing import Literal

# For 4+ values, use Enum
class PolicyAction(str, Enum):
    ACCEPT = 'accept'
    DENY = 'deny'
    IPSEC = 'ipsec'
    
# For 2-3 values, use Literal
schedule_type: Literal['onetime', 'recurring']
```

### 4. ✅ Nested Models for Child Tables [0% → 100%]
**Status:** ❌ NOT STARTED  
**Effort:** 6-8 hours  
**Impact:** 🔴 HIGH

**Tasks:**
- [ ] Parse `child_tables` from schema
- [ ] Generate nested Pydantic models for each child table
- [ ] Use `List[ChildModel]` in parent model
- [ ] Set `default_factory=list` for child lists
- [ ] Handle recursive nesting (child of child)

**Example:**
```python
class PolicySrcAddr(BaseModel):
    """Source address child table."""
    name: str = Field(max_length=79)

class FirewallPolicy(BaseModel):
    """Firewall Policy configuration model."""
    srcaddr: list[PolicySrcAddr] = Field(
        default_factory=list,
        description="Source address objects"
    )
```

---

## 🎯 HIGH PRIORITY - Feature Development (Post v1.7.0)

### 19. ✅ Object Response Mode Implementation [0% → 100%]
**Status:** 📋 PLANNED  
**Effort:** 2-3 days  
**Impact:** 🔴 HIGH  
**Documentation:** `.dev/OBJECT_RESPONSE_DESIGN.md`

Add support for object-based responses from FortiOS API calls, allowing cleaner attribute access instead of dictionary lookups.

**Requirements:**
- Create `FortiObject` wrapper class for safe attribute access
- Add `response_mode` parameter to client initialization
- Support client-level default setting: `FortiOS(response_mode="object")`
- Support per-request override: `fgt.api.cmdb.firewall.policy.get(response_mode="object")`
- Auto-flatten member_table fields (e.g., `srcaddr` → list of names)
- Maintain full backward compatibility with dict responses
- Update all generated endpoint methods to support response modes

**Example Usage:**
```python
# Option 1: Set at client level
fgt = FortiOS(host="...", token="...", response_mode="object")
policies = fgt.api.cmdb.firewall.policy.get()
for policy in policies:
    print(policy.name, policy.srcaddr)

# Option 2: Override per request
fgt = FortiOS(host="...", token="...")  # defaults to dict mode
policies = fgt.api.cmdb.firewall.policy.get(response_mode="object")
for policy in policies:
    print(policy.name, policy.srcaddr)
```

**Subtasks:**
- [ ] Implement `FortiObject` wrapper class in `packages/fortios/hfortix_fortios/models.py`
- [ ] Add `response_mode` to HTTP client interface
- [ ] Update Jinja2 templates to include response_mode parameter
- [ ] Regenerate all API endpoints with new template
- [ ] Write unit tests for FortiObject wrapper
- [ ] Write integration tests with live API
- [ ] Update documentation and examples
- [ ] Add to CHANGELOG.md

**Phase 2 (Future):**
- [ ] Generate Pydantic models from schemas for type safety
- [ ] Add `response_mode="pydantic"` option (depends on Task #1-4 completion)
- [ ] Create model generator script
- [ ] Generate models for commonly-used endpoints

---

## 🟡 MEDIUM PRIORITY (Next 3-5 Days)

### 5. ✅ Datasource & Relationship Validation [0% → 100%]
**Status:** ❌ NOT STARTED  
**Effort:** 1 day  
**Impact:** 🟡 MEDIUM

**Tasks:**
- [ ] Parse `datasource` from schema fields
- [ ] Add datasource comments to Field() descriptions
- [ ] Create optional validators for foreign key checking
- [ ] Document relationships in docstrings
- [ ] Add helper methods for relationship navigation

**Example:**
```python
schedule: str = Field(
    description="Schedule name (datasource: firewall.schedule.name)",
    examples=["always", "business-hours"]
)

@field_validator('schedule')
def validate_schedule(cls, v, info):
    """Validate schedule exists."""
    # Optional: Check if schedule exists via API
    return v
```

### 6. ✅ Capabilities Metadata Integration [0% → 100%]
**Status:** ❌ NOT STARTED  
**Effort:** 1 day  
**Impact:** 🟡 MEDIUM

**Tasks:**
- [ ] Add capabilities as class attributes
- [ ] Generate `SUPPORTS_*` constants from schema
- [ ] Add capability checks to methods
- [ ] Document capabilities in docstrings
- [ ] Raise `NotSupportedError` for unsupported operations

**Example:**
```python
class PolicyEndpoint:
    """Firewall Policy endpoint."""
    
    # From schema.capabilities
    SUPPORTS_CREATE = True
    SUPPORTS_UPDATE = True
    SUPPORTS_DELETE = True
    SUPPORTS_MOVE = True
    SUPPORTS_CLONE = True
    SUPPORTS_FILTERING = True
    
    def move(self, ...):
        if not self.SUPPORTS_MOVE:
            raise NotSupportedError("Move not supported")
```

### 7. ✅ Related Endpoints Documentation [0% → 100%]
**Status:** ❌ NOT STARTED  
**Effort:** 4-6 hours  
**Impact:** 🟢 LOW-MEDIUM

**Tasks:**
- [ ] Parse `related_endpoints` from schema
- [ ] Add "See Also" sections to docstrings
- [ ] Link to related endpoint documentation
- [ ] Include relationship type (datasource/reference/child)

**Example:**
```python
def get(self, ...):
    """
    Retrieve firewall policy.
    
    Related Endpoints:
        - firewall.address - Source/destination address references
        - firewall.schedule - Schedule references
        - firewall.service.custom - Service references
    """
```

### 20. ✅ Schema Discovery Enhancement [0% → 100%]
**Status:** 📋 PLANNED  
**Effort:** 1 day  
**Impact:** 🟡 MEDIUM

Improve schema discovery and caching mechanisms.

**Tasks:**
- [ ] Add schema version detection
- [ ] Implement schema diff tool for version comparison
- [ ] Cache schemas locally with TTL
- [ ] Add schema validation for generated code
- [ ] Add schema upgrade notifications

**Files to Update:**
- Add new `packages/fortios/hfortix_fortios/schema_manager.py`
- Update discovery mechanisms

---

## 🟢 LOW PRIORITY (Next 1-2 Weeks)

### 8. ✅ Complexity Warnings in Documentation [0% → 100%]
**Status:** ❌ NOT STARTED  
**Effort:** 2-3 hours  
**Impact:** 🟢 LOW

**Tasks:**
- [ ] Parse `complexity` from schema
- [ ] Add complexity badges to docstrings
- [ ] Add performance warnings for complex endpoints
- [ ] Document field/child table counts

**Example:**
```python
"""
Retrieve firewall policy.

Complexity: VERY_COMPLEX
⚠️  184 fields, 43 child tables - use filtering for better performance
"""
```

### 9. ✅ Field & Query Parameter Examples [0% → 100%]
**Status:** ❌ NOT STARTED  
**Effort:** 4-6 hours  
**Impact:** 🟢 LOW

**Tasks:**
- [ ] Add field examples to docstrings
- [ ] Add query parameter examples
- [ ] Add more code examples to method docstrings
- [ ] Include common use cases

### 10. ✅ Migration Guide [0% → 100%]
**Status:** ❌ NOT STARTED  
**Effort:** 4-6 hours  
**Impact:** 🟢 LOW

**Tasks:**
- [ ] Document breaking changes (if any)
- [ ] Create before/after examples
- [ ] Document new Pydantic model usage
- [ ] Create upgrade checklist

---

## 🧪 TESTING & VALIDATION

### 11. ✅ Pydantic Model Tests [0% → 100%]
**Status:** ❌ NOT STARTED  
**Effort:** 1 day  

**Tasks:**
- [ ] Test model instantiation
- [ ] Test validation constraints
- [ ] Test enum validation
- [ ] Test nested model serialization
- [ ] Test invalid data rejection

### 12. ✅ Integration Tests [0% → 100%]
**Status:** ❌ NOT STARTED  
**Effort:** 1 day  

**Tasks:**
- [ ] Test models with real API responses
- [ ] Test serialization/deserialization
- [ ] Test validation with FortiGate API
- [ ] Test relationship validation

### 13. ✅ Update Existing Tests [0% → 100%]
**Status:** ❌ NOT STARTED  
**Effort:** 4-6 hours  

**Tasks:**
- [ ] Update tests to use Pydantic models
- [ ] Ensure all 260+ validator tests still pass
- [ ] Update monitor endpoint tests
- [ ] Update firewall policy tests

---

## 📚 DOCUMENTATION

### 14. ✅ API Documentation Update [20% → 100%]
**Status:** 🟡 IN PROGRESS  
**Effort:** 1 day  

**Tasks:**
- [x] Basic docstrings (done)
- [ ] Add Pydantic model documentation
- [ ] Add validation examples
- [ ] Add relationship documentation
- [ ] Generate API reference docs

### 15. ✅ User Guide Updates [0% → 100%]
**Status:** ❌ NOT STARTED  
**Effort:** 1 day  

**Tasks:**
- [ ] Document Pydantic model usage
- [ ] Add validation examples
- [ ] Add relationship navigation examples
- [ ] Add best practices guide

### 16. ✅ Developer Documentation [0% → 100%]
**Status:** ❌ NOT STARTED  
**Effort:** 4-6 hours  

**Tasks:**
- [ ] Document generator architecture
- [ ] Document schema v1.7.0 format
- [ ] Add contributing guide for models
- [ ] Document extension points

### 21. ✅ Performance Optimizations [0% → 100%]
**Status:** 📋 PLANNED  
**Effort:** 1-2 days  
**Impact:** 🟢 LOW-MEDIUM

**Tasks:**
- [ ] Benchmark current implementation
- [ ] Optimize bulk operations
- [ ] Add connection pooling
- [ ] Implement request batching where applicable
- [ ] Profile memory usage for large result sets
- [ ] Add performance metrics collection
- [ ] Document performance best practices

### 22. ✅ Developer Experience Improvements [0% → 100%]
**Status:** 📋 PLANNED  
**Effort:** 2-3 days  
**Impact:** 🟢 LOW

**Tasks:**
- [ ] Create VSCode extension for FortiOS development
- [ ] Add PyCharm plugin
- [ ] Provide code snippets for common operations
- [ ] Add debug mode with detailed logging
- [ ] Create interactive CLI tool
- [ ] Add shell auto-completion

---

## 🗑️ CLEANUP

### 17. ✅ Remove Old Schemas [0% → 100%]
**Status:** ❌ NOT STARTED  
**Effort:** 1 hour  

**Tasks:**
- [ ] Archive old schemas from `/.dev/generator/schemas/`
- [ ] Update all references to use `/schema/7.6.5/`
- [ ] Clean up obsolete generator code
- [ ] Update documentation

### 18. ✅ Code Review & Refactoring [0% → 100%]
**Status:** ❌ NOT STARTED  
**Effort:** 1 day  

**Tasks:**
- [ ] Review generated code quality
- [ ] Optimize generator performance
- [ ] Refactor duplicate code
- [ ] Improve error handling

---

## � FUTURE IDEAS & ENHANCEMENTS

### GraphQL-like Query Language
**Status:** 💡 IDEA STAGE  
**Complexity:** High

Investigate adding a GraphQL-style query interface for filtering:
```python
policies = fgt.query("""
    firewall.policy {
        name
        srcaddr
        dstaddr
        where: { status: "enable", action: "accept" }
    }
""")
```

**Tasks:**
- [ ] Research GraphQL integration options
- [ ] Design query syntax
- [ ] Implement query parser
- [ ] Add query optimization
- [ ] Write comprehensive tests

### Declarative Configuration Management
**Status:** 💡 IDEA STAGE  
**Complexity:** High

Add Terraform-like declarative config:
```python
fgt.declare({
    "firewall.policy": [
        {"name": "allow_web", "srcintf": "internal", ...},
        {"name": "allow_dns", "srcintf": "internal", ...},
    ]
})
fgt.apply()  # Creates/updates/deletes to match desired state
```

**Tasks:**
- [ ] Design declarative API
- [ ] Implement state diffing
- [ ] Add rollback support
- [ ] Create plan/apply workflow
- [ ] Add drift detection

### AI-Assisted Policy Analysis
**Status:** 💡 IDEA STAGE  
**Complexity:** High

Integrate with LLMs for policy analysis:
```python
fgt.analyze_policies("Find policies that allow unrestricted internet access")
fgt.suggest_optimizations()
fgt.explain_policy(policyid=1)
```

**Tasks:**
- [ ] Research LLM integration options
- [ ] Design AI analysis framework
- [ ] Add policy context extraction
- [ ] Implement suggestion engine
- [ ] Add security best practices checks

---

## ✅ COMPLETED WORK

### Schema v1.7.0 Generation
**Completed:** January 2026

- [x] Generated 1,348 enhanced schemas with v1.7.0 metadata
- [x] Added capabilities, complexity, relationships
- [x] Field validation rules (72% of fields)
- [x] Datasource mapping (20% of fields)
- [x] Related endpoints tracking (38 avg per endpoint)

### Code Generation System
**Completed:** January 2026

- [x] Schema-based code generator
- [x] Template system for endpoints
- [x] Automatic test generation
- [x] Support for CMDB, Monitor, Log, Service endpoints
- [x] 2,129 endpoint files generated
- [x] 260+ validator helper modules

### Monitor Endpoint Fixes
**Completed:** January 2026

- [x] Fixed 400+ monitor endpoint naming issues
- [x] Standardized underscore/hyphen conventions
- [x] Updated all test files
- [x] Regenerated .pyi stub files

### Initial Package Structure
**Completed:** December 2025

- [x] Multi-package architecture (core, fortios, meta)
- [x] Proper dependency management
- [x] CI/CD pipeline setup

---

## �📊 OVERALL PROGRESS TRACKING

### Phase 1: Core Validation (Days 1-2)
**Priority:** 🔴 CRITICAL  
**Progress:** 0%

- [ ] Task #1: Pydantic Model Generation
- [ ] Task #2: Field() Constraints
- [ ] Task #3: Enum Generation
- [ ] Task #4: Nested Models

**Deliverables:**
- Pydantic models for all 1,348 endpoints
- Runtime validation on all fields
- Type-safe API

### Phase 2: Metadata & Relationships (Days 3-4)
**Priority:** 🟡 HIGH  
**Progress:** 0%

- [ ] Task #5: Datasource Validation
- [ ] Task #6: Capabilities Integration
- [ ] Task #7: Related Endpoints

**Deliverables:**
- Relationship tracking
- Capabilities metadata
- Enhanced documentation

### Phase 3: Testing & Documentation (Days 5-7)
**Priority:** 🟢 MEDIUM  
**Progress:** 20%

- [ ] Task #8: Complexity Warnings
- [ ] Task #9: Examples
- [ ] Task #10: Migration Guide
- [ ] Task #11-13: Testing
- [ ] Task #14-16: Documentation

**Deliverables:**
- Full test coverage
- Comprehensive documentation
- Migration guide

### Phase 4: Cleanup & Release (Days 8-9)
**Priority:** 🟢 LOW  
**Progress:** 0%

- [ ] Task #17: Remove Old Schemas
- [ ] Task #18: Code Review
- [ ] Final testing
- [ ] Release v1.0.0

---

## 🎯 SUCCESS CRITERIA

### Must Have (v1.0.0 Release)
- ✅ All 1,348 endpoints have Pydantic models
- ✅ 90%+ fields have validation constraints
- ✅ All tests passing
- ✅ Documentation updated
- ✅ Migration guide complete

### Should Have (v1.1.0)
- ✅ Relationship validation working
- ✅ Capabilities fully integrated
- ✅ Related endpoints documented
- ✅ Enhanced examples

### Nice to Have (v1.2.0)
- ✅ Complexity analysis tools
- ✅ Performance optimization
- ✅ Advanced validation helpers
- ✅ Auto-suggest for relationships

---

## 📅 TIMELINE

### Week 1 (Current)
- Days 1-2: Phase 1 (Core Validation)
- Days 3-4: Phase 2 (Metadata)
- Day 5: Start Phase 3 (Testing)

### Week 2
- Days 1-3: Complete Phase 3 (Testing & Docs)
- Days 4-5: Phase 4 (Cleanup & Release)

### Week 3
- Release v1.0.0
- Gather feedback
- Plan v1.1.0

---

## 🔗 RELATED DOCUMENTS

- **`.dev/dev/IMPLEMENTATION_STATUS.md`** - Current status and detailed analysis
- **`.dev/OBJECT_RESPONSE_DESIGN.md`** - Object mode implementation design
- **CHANGELOG.md** - What's been completed
- **`.dev/REALITY_CHECK_ANALYSIS.md`** - Feature-by-feature comparison
- **`docs/fortios/VALIDATION_GUIDE.md`** - Validation documentation

---

## 📝 CONTRIBUTING TO THIS TODO

To add items to this TODO list:
1. Create a detailed description with clear deliverables
2. Assign priority (🔥 Critical / 🎯 High / 🟡 Medium / 🟢 Low / 💡 Idea)
3. Add complexity/effort estimate
4. Add impact rating (🔴 CRITICAL / 🟡 MEDIUM / 🟢 LOW)
5. Link to relevant documentation or issues
6. Break down into subtasks if large
7. Add example code if applicable

For major features, create a design document in `.dev/` directory first.

---

## 📌 LEGEND

**Status:**
- ❌ NOT STARTED - Planned but not started
- 🟡 IN PROGRESS - Currently being worked on
- ✅ COMPLETED - Finished
- 📋 PLANNED - Designed and ready to implement
- 💡 IDEA STAGE - Proposal/concept phase
- 🚫 BLOCKED - Waiting on dependencies

**Priority:**
- 🔥 CRITICAL - Must complete for v1.0.0
- 🎯 HIGH - Important for v1.0.0 or v1.1.0
- 🟡 MEDIUM - Nice to have for v1.x
- 🟢 LOW - Future enhancements
- 💡 IDEA - Long-term vision

**Impact:**
- 🔴 CRITICAL - Affects core functionality
- 🟡 MEDIUM - Improves usability
- 🟢 LOW - Nice to have enhancement

---

**Last Updated:** January 6, 2026  
**Next Review:** After Phase 1 completion (Pydantic models)  
**Questions?** See `.dev/dev/IMPLEMENTATION_STATUS.md` for detailed analysis
