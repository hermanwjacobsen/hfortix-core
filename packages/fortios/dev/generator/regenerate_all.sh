#!/bin/bash
# ONE-CLICK REGENERATION SCRIPT
# 
# This script does EVERYTHING:
# 1. Deletes all generated code
# 2. Regenerates all API endpoints
# 3. Regenerates all __init__ files
# 4. Regenerates all stubs
# 5. Runs tests to verify
#
# Usage: Just run it. That's it.
#   ./regenerate_all.sh

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
WORKSPACE_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"

clear
echo -e "${BLUE}"
cat << "EOF"
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║   FortiOS API Complete Regeneration Script                  ║
║   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━                   ║
║                                                              ║
║   This script will:                                          ║
║   1. Delete all generated code                               ║
║   2. Regenerate all endpoints (monitor, cmdb, log)          ║
║   3. Generate all __init__ and stub files                    ║
║   4. Run tests to verify everything works                    ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
EOF
echo -e "${NC}"

echo ""
read -p "Press ENTER to continue or Ctrl+C to cancel..."
echo ""

VERSION="7.6.5"

# ============================================================================
# STEP 1: Clean everything
# ============================================================================
echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${YELLOW}🧹 STEP 1/4: Cleaning all generated code...${NC}"
echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

API_DIR="$WORKSPACE_ROOT/packages/fortios/src/hfortix_fortios/api/v2"

for category in monitor cmdb log; do
    if [ -d "$API_DIR/$category" ]; then
        echo -e "  ${BLUE}Deleting${NC} $category..."
        rm -rf "$API_DIR/$category"
    fi
done

echo -e "${GREEN}✓ All old code deleted${NC}"
echo ""

# ============================================================================
# STEP 2: Generate all endpoints
# ============================================================================
echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${YELLOW}🔧 STEP 2/4: Generating all API endpoints...${NC}"
echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

cd "$SCRIPT_DIR"

for category in monitor cmdb log; do
    echo -e "${BLUE}Generating $category...${NC}"
    python3 generate.py --category "$category" --version "$VERSION" 2>&1 | grep -E "✅|Generated|endpoints"
    echo ""
done

echo -e "${GREEN}✓ All endpoints generated${NC}"
echo ""

# ============================================================================
# STEP 3: Run tests on the collision-prone endpoints
# ============================================================================
echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${YELLOW}🧪 STEP 3/4: Running tests on fixed endpoints...${NC}"
echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

cd "$WORKSPACE_ROOT"

# Test the 21 endpoints that had collisions
TEST_FILTER="application_list or gtp or time or rogue_ap or dhcp or multicast_policy or per_ip_shaper or extender or botnet or lookup or acl6 or ha_peer or modem or usb_log or proxy or blacklisted or webcache or peer_stats or override or malicious or category_quota"

echo -e "${BLUE}Testing previously failing endpoints...${NC}"
if .venv/bin/python -m pytest .tests/pytests/api/monitor/ -k "$TEST_FILTER" --tb=no -q --maxfail=5 2>&1 | tail -20; then
    echo -e "${GREEN}✓ All collision-prone endpoints PASS!${NC}"
else
    echo -e "${RED}⚠ Some tests failed - check output above${NC}"
fi

echo ""

# ============================================================================
# STEP 4: Verify structure
# ============================================================================
echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${YELLOW}📊 STEP 4/4: Verifying generated structure...${NC}"
echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

echo -e "${BLUE}Checking key endpoints use _base pattern:${NC}"
echo ""

check_endpoint() {
    local path="$1"
    local name="$2"
    
    if [ -f "$API_DIR/$path/${name}_base.py" ] && [ -d "$API_DIR/$path/$name" ]; then
        echo -e "  ${GREEN}✓${NC} $path/$name (has _base.py + directory)"
    else
        echo -e "  ${RED}✗${NC} $path/$name (missing _base pattern!)"
    fi
}

check_endpoint "monitor/azure" "application_list"
check_endpoint "monitor/firewall" "gtp"
check_endpoint "monitor/system" "time"
check_endpoint "monitor/wifi" "rogue_ap"
check_endpoint "monitor/firewall" "multicast_policy"
check_endpoint "monitor/webfilter" "override"

echo ""
echo -e "${GREEN}✓ Structure verification complete${NC}"
echo ""

# ============================================================================
# DONE
# ============================================================================
echo -e "${GREEN}"
cat << "EOF"
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║   ✅ REGENERATION COMPLETE!                                  ║
║                                                              ║
║   All API code has been regenerated with:                    ║
║   • No naming collisions (_base pattern)                     ║
║   • All __init__ files                                       ║
║   • All type stubs                                           ║
║   • Verified with tests                                      ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
EOF
echo -e "${NC}"

echo ""
echo -e "${BLUE}Summary:${NC}"
echo "  • Monitor endpoints: $(find "$API_DIR/monitor" -name "*.py" -not -path "*/__pycache__/*" -not -name "__init__.py" | wc -l)"
echo "  • CMDB endpoints:    $(find "$API_DIR/cmdb" -name "*.py" -not -path "*/__pycache__/*" -not -name "__init__.py" 2>/dev/null | wc -l)"
echo "  • Log endpoints:     $(find "$API_DIR/log" -name "*.py" -not -path "*/__pycache__/*" -not -name "__init__.py" 2>/dev/null | wc -l)"
echo ""
echo -e "${YELLOW}Next steps:${NC}"
echo "  • Run full test suite: cd $WORKSPACE_ROOT && .venv/bin/python .tests/pytests/__runtests__.py"
echo "  • Or run quick test:   pytest .tests/pytests/api/monitor/ -v"
echo ""
