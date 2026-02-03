#!/bin/bash
# Regenerate Category Script
# 
# Completely deletes and regenerates API code for a specific category.
# This ensures clean regeneration with the latest generator logic.
#
# Usage:
#   ./regenerate_category.sh monitor 7.6.5
#   ./regenerate_category.sh cmdb 7.6.5
#   ./regenerate_category.sh log 7.6.5
#   ./regenerate_category.sh --all 7.6.5

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Get script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
WORKSPACE_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
API_DIR="$WORKSPACE_ROOT/packages/fortios/src/hfortix_fortios/api/v2"

# Parse arguments
CATEGORY="${1:-monitor}"
VERSION="${2:-7.6.5}"

if [ "$CATEGORY" = "--help" ] || [ "$CATEGORY" = "-h" ]; then
    echo "Usage: $0 <category> [version]"
    echo ""
    echo "Arguments:"
    echo "  category    Category to regenerate (monitor, cmdb, log, or --all)"
    echo "  version     FortiOS version (default: 7.6.5)"
    echo ""
    echo "Examples:"
    echo "  $0 monitor 7.6.5     # Regenerate monitor category"
    echo "  $0 cmdb 7.6.5        # Regenerate cmdb category"
    echo "  $0 --all 7.6.5       # Regenerate all categories"
    exit 0
fi

echo -e "${BLUE}╔════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║        FortiOS API Code Regeneration Script               ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════════════════════════╝${NC}"
echo ""
echo -e "${YELLOW}Category:${NC} $CATEGORY"
echo -e "${YELLOW}Version:${NC}  $VERSION"
echo ""

# Function to regenerate a single category
regenerate_category() {
    local cat="$1"
    
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${YELLOW}🧹 Step 1: Deleting old ${cat} code...${NC}"
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    
    if [ -d "$API_DIR/$cat" ]; then
        rm -rf "$API_DIR/$cat"
        echo -e "${GREEN}✓${NC} Deleted $API_DIR/$cat"
    else
        echo -e "${YELLOW}⚠${NC} Directory $API_DIR/$cat does not exist (skipping)"
    fi
    
    # Recreate the base directory
    mkdir -p "$API_DIR/$cat"
    echo -e "${GREEN}✓${NC} Created clean directory"
    echo ""
    
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${YELLOW}🔧 Step 2: Regenerating ${cat} endpoints...${NC}"
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    
    cd "$SCRIPT_DIR"
    python3 generate.py --category "$cat" --version "$VERSION"
    
    echo ""
    echo -e "${GREEN}✓ ${cat} regeneration complete!${NC}"
    echo ""
}

# Function to verify the structure
verify_structure() {
    local cat="$1"
    
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${YELLOW}📊 Step 3: Verifying ${cat} structure...${NC}"
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    
    cd "$WORKSPACE_ROOT"
    
    if [ "$cat" = "monitor" ]; then
        # Check collision-prone endpoints in monitor category
        echo ""
        echo -e "${YELLOW}Checking collision-prone endpoints:${NC}"
        echo ""
        
        if [ -d "$API_DIR/monitor/azure" ]; then
            echo -e "${BLUE}Azure application_list:${NC}"
            ls -la "$API_DIR/monitor/azure/" | grep application | head -5 || echo "  (not found)"
        fi
        
        if [ -d "$API_DIR/monitor/firewall" ]; then
            echo ""
            echo -e "${BLUE}Firewall gtp:${NC}"
            ls -la "$API_DIR/monitor/firewall/" | grep gtp | head -5 || echo "  (not found)"
        fi
        
        if [ -d "$API_DIR/monitor/system" ]; then
            echo ""
            echo -e "${BLUE}System time:${NC}"
            ls -la "$API_DIR/monitor/system/" | grep -E "^d.*time|^-.*time" | head -5 || echo "  (not found)"
        fi
        
        if [ -d "$API_DIR/monitor/wifi" ]; then
            echo ""
            echo -e "${BLUE}Wifi rogue_ap:${NC}"
            ls -la "$API_DIR/monitor/wifi/" | grep rogue | head -5 || echo "  (not found)"
        fi
    fi
    
    echo ""
    echo -e "${GREEN}✓ Structure verification complete${NC}"
}

# Main execution
if [ "$CATEGORY" = "--all" ]; then
    echo -e "${YELLOW}Regenerating ALL categories...${NC}"
    echo ""
    
    for cat in monitor cmdb log; do
        regenerate_category "$cat"
    done
    
    echo ""
    echo -e "${GREEN}╔════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${GREEN}║   ✓ All categories regenerated successfully!              ║${NC}"
    echo -e "${GREEN}╚════════════════════════════════════════════════════════════╝${NC}"
else
    regenerate_category "$CATEGORY"
    verify_structure "$CATEGORY"
    
    echo ""
    echo -e "${GREEN}╔════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${GREEN}║   ✓ Regeneration complete!                                ║${NC}"
    echo -e "${GREEN}╚════════════════════════════════════════════════════════════╝${NC}"
fi

echo ""
echo -e "${BLUE}Next steps:${NC}"
echo "  1. Run tests: cd $WORKSPACE_ROOT && .venv/bin/python .tests/pytests/__runtests__.py"
echo "  2. Check specific endpoints: pytest .tests/pytests/api/$CATEGORY/ -v"
echo ""
