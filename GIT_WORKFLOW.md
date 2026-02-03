# Git Workflow - Private & Public Repos

## Repository Structure

This project uses a **dual-repository strategy**:

### 🔒 Private Repo: `hfortix-dev`
**URL:** https://github.com/hermanwjacobsen/hfortix-dev

Contains the **full development environment**:
- ✅ `packages/*/src/` - Public source code
- ✅ `packages/*/dev/` - Private dev assets (tests, generators, schemas, docs, examples)
- ✅ Development scripts
- ✅ Test suites
- ✅ Internal documentation
- ✅ Generator and schema files

### 📦 Public Repo: `hfortix`
**URL:** https://github.com/hermanwjacobsen/hfortix

Contains **only public source code**:
- ✅ `packages/*/src/` - Public source code
- ✅ Public documentation
- ✅ README, LICENSE, CHANGELOG
- ❌ No `packages/*/dev/` folders
- ❌ No private development assets

---

## Git Remote Configuration

```bash
# Private repo (main development)
origin  → https://github.com/hermanwjacobsen/hfortix-dev.git

# Public repo (filtered releases)
public  → https://github.com/hermanwjacobsen/hfortix.git
```

---

## Development Workflow

### 1. Daily Development (Private Repo)

All development happens in the **private repo** (`hfortix-dev`):

```bash
# Make changes
git add .
git commit -m "Your commit message"

# Push to private repo (default)
git push origin main
```

### 2. Sync to Public Repo

When ready to release to public:

```bash
# Run the sync script
./scripts/sync_to_public.sh
```

This script will:
1. ✅ Create a temporary branch
2. ✅ Remove all `packages/*/dev/` folders
3. ✅ Remove private scripts and files
4. ✅ Push to public repo
5. ✅ Clean up and return to main branch

### 3. Tag a Release (Optional)

After syncing to public, create a release tag:

```bash
# Tag in private repo
git tag v1.0.0
git push origin --tags

# Tag in public repo
git push public --tags
```

---

## What Gets Synced?

### ✅ Included in Public Repo:
- `packages/core/src/` - Core package source code
- `packages/fortios/src/` - FortiOS package source code
- `packages/meta/src/` - Meta package source code
- `packages/*/pyproject.toml` - Package configuration
- `README.md`, `LICENSE`, `CHANGELOG.md` - Documentation
- `docs/` - Public documentation
- `.github/workflows/` - CI/CD workflows (if any)

### ❌ Excluded from Public Repo:
- `packages/*/dev/` - All private development assets
  - `dev/tests/` - Test suites
  - `dev/generator/` - Code generators
  - `dev/schema/` - API schemas
  - `dev/docs/` - Internal documentation
  - `dev/examples/` - Example scripts
- `scripts/sync_to_public.sh` - Sync script itself
- `.github/prompts/` - GitHub Copilot prompts
- `.env` - Environment variables (already in .gitignore)

---

## Troubleshooting

### Sync script fails
```bash
# Ensure you're on main branch
git checkout main

# Ensure working directory is clean
git status

# If you have uncommitted changes, commit them first
git add .
git commit -m "Your changes"
```

### Force update public repo
If the sync gets out of sync:

```bash
# The sync script uses --force automatically
./scripts/sync_to_public.sh
```

### Manually push to public
If you need to manually sync:

```bash
# Create a temporary branch
git checkout -b public-temp

# Remove dev folders
find packages -type d -name "dev" -exec git rm -rf {} +
git rm -rf .github/prompts/
git rm -f scripts/sync_to_public.sh

# Commit and push
git commit -m "Public release"
git push public public-temp:main --force

# Return to main
git checkout main
git branch -D public-temp
```

---

## Quick Reference

```bash
# Push to private repo (daily work)
git push origin main

# Sync to public repo (releases)
./scripts/sync_to_public.sh

# Check remote configuration
git remote -v

# View what would be synced
git ls-files | grep -E "^packages/.*/src/"
```

---

## Notes

- **Always develop in the private repo** (`hfortix-dev`)
- **Never commit directly to public repo** - use the sync script
- **Keep .env files private** - never commit secrets
- The sync script is **safe** - it creates a temporary branch and doesn't affect your main branch
