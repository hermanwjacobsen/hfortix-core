#!/bin/bash
# Run all code quality checks and generate a report
# Usage: ./scripts/run_quality_checks.sh [output_dir]

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
OUTPUT_DIR="${1:-.dev/reports}"
REPORT="$OUTPUT_DIR/quality_report_$(date +%Y%m%d_%H%M%S).txt"

cd "$PROJECT_ROOT"

# Ensure output directory exists
mkdir -p "$OUTPUT_DIR"

echo "Running code quality checks..."
echo "Report will be saved to: $REPORT"
echo ""

# Start report
echo "=== Code Quality Report - $(date) ===" > "$REPORT"
echo "Project: $(basename "$PROJECT_ROOT")" >> "$REPORT"
echo "" >> "$REPORT"

# ISORT - Import sorting
echo "Running isort..."
echo "=== ISORT (import sorting) ===" >> "$REPORT"
isort --check-only --diff packages/core packages/fortios packages/meta 2>&1 >> "$REPORT" || true
echo "" >> "$REPORT"

# FLAKE8 - Style/syntax
echo "Running flake8..."
echo "=== FLAKE8 (style/syntax) ===" >> "$REPORT"
flake8 packages/core packages/fortios packages/meta 2>&1 >> "$REPORT" || true
FLAKE8_ERRORS=$(flake8 packages/core packages/fortios packages/meta 2>&1 | wc -l)
echo "Flake8 issues: $FLAKE8_ERRORS" >> "$REPORT"
echo "" >> "$REPORT"

# MYPY - Type checking
echo "Running mypy (this may take a while)..."
echo "=== MYPY (type checking) ===" >> "$REPORT"
mypy packages/core/hfortix_core packages/fortios/hfortix_fortios packages/meta/hfortix 2>&1 >> "$REPORT" || true
echo "" >> "$REPORT"

# MYPY Summary
echo "=== MYPY ERROR SUMMARY ===" >> "$REPORT"
grep -oP '\[.*?\]' "$REPORT" 2>/dev/null | sort | uniq -c | sort -rn >> "$REPORT" || true
echo "" >> "$REPORT"

# BANDIT - Security
echo "Running bandit..."
echo "=== BANDIT (security) ===" >> "$REPORT"
bandit -r packages/core packages/meta packages/fortios/hfortix_fortios \
    -x packages/fortios/hfortix_fortios/api --quiet 2>&1 >> "$REPORT" || true
echo "" >> "$REPORT"

# PYLINT - Errors only
echo "Running pylint..."
echo "=== PYLINT (errors only) ===" >> "$REPORT"
pylint packages/core/hfortix_core packages/fortios/hfortix_fortios packages/meta/hfortix \
    --disable=all --enable=E --max-line-length=120 --ignore=api 2>&1 >> "$REPORT" || true
echo "" >> "$REPORT"

# Summary
echo "=== SUMMARY ===" >> "$REPORT"
echo "Report generated: $(date)" >> "$REPORT"
echo "" >> "$REPORT"

echo ""
echo "=== Quality Check Complete ==="
echo "Report saved to: $REPORT"
echo ""
echo "Quick summary:"
echo "  - Flake8 issues: $FLAKE8_ERRORS"
grep "Found .* errors" "$REPORT" | head -1 || echo "  - Mypy: check report for details"
grep "Total issues" "$REPORT" | head -2 || true
echo ""
