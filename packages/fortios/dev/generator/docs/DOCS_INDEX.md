# Generator Documentation Index

**Last Updated:** January 2026  
**Schema Version:** v1.7.0 for FortiOS 7.6.5  
**Total Endpoints:** 1,348 (CMDB: 561, Monitor: 490, Log: 286, Service: 11)

---

## 📚 Primary Documentation

### Getting Started

| Document | Description |
|----------|-------------|
| [README.md](README.md) | Generator overview and basic usage |
| [QUICK_REFERENCE.md](QUICK_REFERENCE.md) | **⭐ Start here** - Commands, patterns, quick lookup |
| [WORKFLOW_GUIDE.md](WORKFLOW_GUIDE.md) | Step-by-step development workflow |
| [QUICK_START.md](QUICK_START.md) | Using validator metadata |

### API Reference

| Document | Description |
|----------|-------------|
| [FORTIOS_API_GUIDE.md](FORTIOS_API_GUIDE.md) | FortiOS API: filtering, sorting, pagination, responses |
| [VALIDATOR_API_REFERENCE.md](VALIDATOR_API_REFERENCE.md) | Validator functions and constants |
| [VALIDATOR_CAPABILITIES.md](VALIDATOR_CAPABILITIES.md) | What validators can do |

### Technical Deep-Dives

| Document | Description |
|----------|-------------|
| [GENERATOR_DESIGN.md](GENERATOR_DESIGN.md) | Architecture and design decisions |
| [EDGE_CASES.md](EDGE_CASES.md) | Path patterns, naming, edge case handling |
| [MKEY_COMPLEXITY.md](MKEY_COMPLEXITY.md) | Primary key (mkey) handling |
| [LOG_CATEGORY_NOTES.md](LOG_CATEGORY_NOTES.md) | LOG category special implementation |
| [ACTION_METHODS_IMPLEMENTATION.md](ACTION_METHODS_IMPLEMENTATION.md) | move(), clone(), exists() methods |
| [QUERY_PARAMS_AND_SCHEMA_FEATURES.md](QUERY_PARAMS_AND_SCHEMA_FEATURES.md) | Query params and get_schema() |

### Project Management

| Document | Description |
|----------|-------------|
| [CHANGELOG.md](CHANGELOG.md) | Change history |
| [CORE_FEATURES_REFERENCE.md](CORE_FEATURES_REFERENCE.md) | Feature checklist and status |

---

## 📁 Data Files

| File | Description |
|------|-------------|
| `endpoints_all.json` | Complete endpoint inventory (JSON) |
| `endpoints_cmdb.txt` | CMDB endpoints list |
| `endpoints_monitor.txt` | Monitor endpoints list |
| `endpoints_log.txt` | Log endpoints list |
| `endpoints_service.txt` | Service endpoints list |
| `dependency_graph.json` | Endpoint dependency analysis |

---

## 📂 Archive

Historical and superseded documentation is preserved in `archive/`:

- `QUICKREF.md` → Superseded by `QUICK_REFERENCE.md`
- `QUICK_REFERENCE_QUERY_PARAMS.md` → Merged into `QUICK_REFERENCE.md`
- `GENERATOR_QUICK_REFERENCE.md` → Merged into `QUICK_REFERENCE.md`
- `FORTIOS_FILTERING.md` → Merged into `FORTIOS_API_GUIDE.md`
- `FORTIOS_RESPONSE_STRUCTURE.md` → Merged into `FORTIOS_API_GUIDE.md`
- `FORTIOS_ADVANCED_FEATURES.md` → Merged into `FORTIOS_API_GUIDE.md`
- `EXECUTIVE_SUMMARY.md` → Historical overview
- `OUT_OF_SCOPE.md` → v0.5.0 scope decisions
- `ADDITIONAL_SUGGESTIONS.md` → Feature ideas
- `CLEANUP_SUMMARY.md` → Refactoring history
- `AUTO_DETECTION_UPDATE.md` → Implementation history
- `SCHEMA_ONLY_MIGRATION.md` → Migration history
- `NAMING_COLLISION_SOLUTION.md` → Design decision
- `METADATA_MIXIN_REFACTOR.md` → Refactoring history

---

## 🔗 Related Documentation

- **Root Documentation**
  - `/README.md` - Project overview
  - `/QUICKSTART.md` - User quick start
  - `/CHANGELOG.md` - Release notes

- **Package Documentation**
  - `/packages/fortios/README.md` - FortiOS package
  - `/packages/core/README.md` - Core package
  - `/docs/fortios/` - User-facing API documentation
