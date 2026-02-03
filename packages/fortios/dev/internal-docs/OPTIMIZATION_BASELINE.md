# Helper Validation Centralization - Baseline Metrics

**Date**: January 7, 2026  
**Branch**: feature/validator-generation  
**Optimization**: Centralizing `validate_required_fields()`, enum validation, and query param validation

---

## 📦 BEFORE OPTIMIZATION

### Package Metrics
- **Total Package Size**: 108 MB
- **Helper Files Count**: 1,062 files
- **Total Lines in Helpers**: 370,493 lines
- **Average Lines per Helper**: 348 lines

### File Size Distribution
- **< 200 lines**: 0 files
- **200-300 lines**: 732 files (69%)
- **300-500 lines**: 195 files (18%)
- **> 500 lines**: 135 files (13%)

### Largest Helper Files
- 3,889 lines (max)
- 3,861 lines
- 3,786 lines
- 3,362 lines
- 3,260 lines

### Sample Files (10 random)
```
231 lines - monitor/webfilter/override/_helpers/delete.py
231 lines - monitor/webfilter/malicious_urls/_helpers/stat.py
231 lines - monitor/webfilter/category_quota/_helpers/reset.py
231 lines - monitor/webfilter/_helpers/category_quota.py
231 lines - monitor/webfilter/_helpers/fortiguard_categories.py
231 lines - monitor/webfilter/_helpers/override.py
231 lines - monitor/webfilter/_helpers/malicious_urls.py
231 lines - monitor/webfilter/_helpers/trusted_urls.py
231 lines - monitor/fortiguard/_helpers/answers.py
231 lines - monitor/fortiguard/_helpers/redirect_portal.py
```

---

## 🎯 Expected Impact

### Code Reduction (Estimates)
- **validate_required_fields()**: ~25 lines × 1,062 = ~26,550 lines
- **Enum validation pattern**: ~8 lines × 3 enums × 1,062 = ~25,488 lines
- **Query param validation**: ~8 lines × 1,062 = ~8,496 lines

**Total Expected Savings**: ~60,534 lines (16% reduction)

### File Size Reduction
- **Before Average**: 348 lines/file
- **Expected After**: ~290 lines/file (-17%)

### Package Size
- **Before**: 108 MB
- **Expected After**: ~90 MB (-17%)

---

## 📝 Optimization Steps

1. ✅ Baseline metrics collected
2. ⏳ Create central validation module (`hfortix_fortios/_helpers/validation.py`)
3. ⏳ Update generator templates to use central functions
4. ⏳ Regenerate all helper files
5. ⏳ Collect after metrics
6. ⏳ Compare and document improvements

---

## 🔧 Commands for After Comparison

```bash
# After regeneration, run:
cd /app/dev/classes/fortinet/packages/fortios

# Package size
du -sh hfortix_fortios/

# Total lines
find hfortix_fortios/api/v2 -path "*/_helpers/*.py" -type f | xargs wc -l | tail -1

# Average lines per file
find hfortix_fortios/api/v2 -path "*/_helpers/*.py" -type f -exec wc -l {} \; | \
  awk '{sum+=$1; count++} END {print int(sum/count) " lines (was 348)"}'

# Size distribution
find hfortix_fortios/api/v2 -path "*/_helpers/*.py" -type f -exec wc -l {} \; | \
  awk '{print $1}' | \
  awk '{if ($1<200) small++; else if ($1<300) medium++; else if ($1<500) large++; else huge++} \
  END {print "< 200 lines: " small; print "200-300 lines: " medium; \
  print "300-500 lines: " large; print "> 500 lines: " huge}'
```

---

## 📊 Metrics to Track

- [ ] Total lines saved
- [ ] Package size reduction (MB)
- [ ] Average file size reduction
- [ ] Import time improvement
- [ ] Memory usage improvement (if measurable)
- [ ] Number of duplicated validation functions eliminated
