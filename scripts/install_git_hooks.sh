#!/bin/bash
# Install git hooks for security protection

echo "================================================================"
echo "🔒 Installing Git Security Hooks"
echo "================================================================"
echo ""

# Install pre-push hook
HOOK_SOURCE="$(dirname "$0")/../.git/hooks/pre-push"
HOOK_DEST=".git/hooks/pre-push"

if [ -f "$HOOK_DEST" ]; then
    echo "✅ Pre-push hook already installed"
else
    echo "📦 Installing pre-push hook to prevent accidental public pushes..."
    
    cat > "$HOOK_DEST" << 'HOOK_CONTENT'
#!/bin/bash
# Git pre-push hook to prevent accidental pushes to public repo
# Only allow pushes through the sync script

# Colors
RED='\033[0;31m'
YELLOW='\033[1;33m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

# Get the remote name being pushed to
remote="$1"
url="$2"

# Check if pushing to public remote
if [ "$remote" = "public" ]; then
    # Check if this push is from the sync script
    if [ -z "$ALLOW_PUBLIC_PUSH" ]; then
        echo ""
        echo -e "${RED}════════════════════════════════════════════════════════════════${NC}"
        echo -e "${RED}🚨 BLOCKED: Direct push to public repo!${NC}"
        echo -e "${RED}════════════════════════════════════════════════════════════════${NC}"
        echo ""
        echo -e "${YELLOW}You attempted to push directly to the PUBLIC repository:${NC}"
        echo "  Remote: $remote"
        echo "  URL: $url"
        echo ""
        echo -e "${RED}⚠️  SECURITY RISK:${NC}"
        echo "  This would expose private dev/ folders, tests, and secrets!"
        echo ""
        echo -e "${GREEN}✅ SAFE METHOD:${NC}"
        echo "  Use the sync script instead:"
        echo ""
        echo "     ./scripts/sync_to_public.sh"
        echo ""
        echo "  This script automatically:"
        echo "    - Removes all packages/*/dev/ folders"
        echo "    - Removes private scripts"
        echo "    - Only syncs public source code"
        echo ""
        echo -e "${RED}════════════════════════════════════════════════════════════════${NC}"
        echo ""
        exit 1
    fi
fi

# Allow push to private repo (origin)
exit 0
HOOK_CONTENT

    chmod +x "$HOOK_DEST"
    echo "✅ Pre-push hook installed successfully!"
fi

echo ""
echo "================================================================"
echo "✅ Security Hooks Installed"
echo "================================================================"
echo ""
echo "Protection enabled:"
echo "  🚫 Direct pushes to 'public' remote are blocked"
echo "  ✅ Pushes to 'origin' (private) are allowed"
echo "  ✅ Use ./scripts/sync_to_public.sh to sync to public"
echo ""
