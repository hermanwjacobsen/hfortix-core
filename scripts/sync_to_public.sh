#!/bin/bash
# Sync script to push packages to their dedicated public repositories
# Usage: ./sync_to_public.sh [core|fortios|meta|all]

set -e  # Exit on error

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Package to sync (or "all")
PACKAGE="${1:-all}"

# Validate package argument
if [[ ! "$PACKAGE" =~ ^(core|fortios|meta|all)$ ]]; then
    echo -e "${RED}❌ Error: Invalid package name${NC}"
    echo ""
    echo "Usage: $0 [core|fortios|meta|all]"
    echo ""
    echo "Examples:"
    echo "  $0 core      # Sync only hfortix-core"
    echo "  $0 fortios   # Sync only hfortix-fortios"
    echo "  $0 meta      # Sync only hfortix-meta"
    echo "  $0 all       # Sync all packages (default)"
    echo ""
    exit 1
fi

# Function to sync a single package
sync_package() {
    local pkg_name=$1
    local remote_name=$2
    local pkg_dir=$3
    
    echo ""
    echo "================================================================"
    echo -e "${BLUE}📦 Syncing ${pkg_name} to ${remote_name}${NC}"
    echo "================================================================"
    echo ""
    
    # Create temporary branch
    TEMP_BRANCH="sync-${pkg_name}-temp"
    echo -e "${YELLOW}� Creating temporary branch: ${TEMP_BRANCH}${NC}"
    git branch -D "$TEMP_BRANCH" 2>/dev/null || true
    git checkout -b "$TEMP_BRANCH"
    
    echo -e "${YELLOW}🗑️  Removing everything except ${pkg_dir}/src/...${NC}"
    
    # Keep only this package's src directory and essential files
    git ls-files | grep -v -E "^(LICENSE|${pkg_dir}/src/|${pkg_dir}/pyproject.toml|${pkg_dir}/README.md)" | xargs -r git rm -rf 2>/dev/null || true
    
    # Move package contents to root
    echo -e "${YELLOW}📁 Moving ${pkg_dir}/src/ contents to root...${NC}"
    if [ -d "${pkg_dir}/src" ]; then
        # Get the actual package directory name (e.g., hfortix_core, hfortix_fortios, hfortix)
        pkg_src_dir=$(ls -d ${pkg_dir}/src/*/ 2>/dev/null | head -1)
        if [ -n "$pkg_src_dir" ]; then
            pkg_basename=$(basename "$pkg_src_dir")
            git mv "${pkg_dir}/src/${pkg_basename}" . 2>/dev/null || true
        fi
        git mv "${pkg_dir}/pyproject.toml" . 2>/dev/null || true
        git mv "${pkg_dir}/README.md" . 2>/dev/null || true
    fi
    
    # Remove the now-empty packages directory
    git rm -rf packages/ 2>/dev/null || true
    
    # Also remove private scripts and folders
    git rm -rf scripts/ 2>/dev/null || true
    git rm -rf .github/prompts/ 2>/dev/null || true
    
    # Commit the changes
    echo -e "${YELLOW}💾 Committing public release...${NC}"
    git add -A
    git commit -m "Public release of ${pkg_name}" --allow-empty
    
    # Push to remote
    echo -e "${YELLOW}🚀 Pushing to ${remote_name}...${NC}"
    export ALLOW_PUBLIC_PUSH=1
    git push "${remote_name}" "${TEMP_BRANCH}:main" --force
    unset ALLOW_PUBLIC_PUSH
    
    echo -e "${GREEN}✅ ${pkg_name} synced successfully!${NC}"
    
    # Return to main
    git checkout main
    git branch -D "$TEMP_BRANCH"
}

# Main script
echo "================================================================"
echo -e "${BLUE}🚀 Multi-Repo Sync Script${NC}"
echo "================================================================"

# Get the current branch
CURRENT_BRANCH=$(git branch --show-current)
echo -e "${YELLOW}� Current branch: ${CURRENT_BRANCH}${NC}"

# Ensure we're on main branch
if [ "$CURRENT_BRANCH" != "main" ]; then
    echo -e "${RED}❌ Error: Must be on 'main' branch to sync${NC}"
    echo "   Current branch: $CURRENT_BRANCH"
    exit 1
fi

# Check for uncommitted changes
if ! git diff-index --quiet HEAD --; then
    echo -e "${RED}❌ Error: You have uncommitted changes${NC}"
    echo "   Please commit or stash your changes first"
    git status --short
    exit 1
fi

echo -e "${GREEN}✅ Working directory is clean${NC}"

# Sync packages based on argument
case "$PACKAGE" in
    core)
        sync_package "hfortix-core" "public-core" "packages/core"
        ;;
    fortios)
        sync_package "hfortix-fortios" "public-fortios" "packages/fortios"
        ;;
    meta)
        sync_package "hfortix-meta" "public-meta" "packages/meta"
        ;;
    all)
        sync_package "hfortix-core" "public-core" "packages/core"
        sync_package "hfortix-fortios" "public-fortios" "packages/fortios"
        sync_package "hfortix-meta" "public-meta" "packages/meta"
        ;;
esac

echo ""
echo "================================================================"
echo -e "${GREEN}✅ SYNC COMPLETE!${NC}"
echo "================================================================"
echo ""
echo "📦 Public repo (hfortix):"
echo "   - Contains: packages/*/src/ (public source code)"
echo "   - Excludes: packages/*/dev/ (private dev assets)"
echo ""
echo "🔒 Private repo (hfortix-dev):"
echo "   - Contains: Everything (full development environment)"
echo ""
echo "Next steps:"
echo "  1. Visit: https://github.com/hermanwjacobsen/hfortix"
echo "  2. Verify the sync worked correctly"
echo "  3. Tag a release if ready: git tag v1.0.0 && git push public --tags"
echo ""
echo "================================================================"
