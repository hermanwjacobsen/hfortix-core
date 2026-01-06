# Publishing hfortix-fortios-stubs to PyPI

This guide explains how to publish the type stubs package to PyPI.

## Prerequisites

1. **Install build tools**:
   ```bash
   pip install build twine
   ```

2. **PyPI Account**:
   - Create account at https://pypi.org/account/register/
   - Set up 2FA (required)
   - Create API token at https://pypi.org/manage/account/token/

3. **Configure PyPI credentials**:
   Create `~/.pypirc`:
   ```ini
   [pypi]
   username = __token__
   password = pypi-AgE... # Your API token
   ```

## Build Process

1. **Clean previous builds**:
   ```bash
   cd packages/fortios-stubs
   rm -rf dist/ build/ *.egg-info
   ```

2. **Build distributions**:
   ```bash
   python -m build
   ```

   This creates:
   - `dist/hfortix_fortios_stubs-X.Y.Z-py3-none-any.whl` (wheel)
   - `dist/hfortix_fortios_stubs-X.Y.Z.tar.gz` (source)

3. **Verify the build**:
   ```bash
   # Check contents
   python -m zipfile -l dist/*.whl | head -50
   
   # Check metadata
   python -m twine check dist/*
   ```

## Publishing

### Test PyPI (Recommended First)

1. **Upload to Test PyPI**:
   ```bash
   python -m twine upload --repository testpypi dist/*
   ```

2. **Test installation**:
   ```bash
   pip install --index-url https://test.pypi.org/simple/ hfortix-fortios-stubs
   ```

### Production PyPI

1. **Upload to PyPI**:
   ```bash
   python -m twine upload dist/*
   ```

2. **Verify on PyPI**:
   - Visit https://pypi.org/project/hfortix-fortios-stubs/
   - Check metadata, description, and links

3. **Test installation**:
   ```bash
   pip install hfortix-fortios-stubs
   ```

## Version Management

Update version in `pyproject.toml` before building:

```toml
[project]
name = "hfortix-fortios-stubs"
version = "0.5.4"  # ← Update this
```

**Version must match `hfortix-fortios` version!**

## Automation

For automated releases, consider:

1. **GitHub Actions**:
   ```yaml
   - name: Build package
     run: python -m build
   
   - name: Publish to PyPI
     uses: pypa/gh-action-pypi-publish@release/v1
     with:
       password: ${{ secrets.PYPI_API_TOKEN }}
   ```

2. **Version sync**:
   Keep `hfortix-fortios` and `hfortix-fortios-stubs` versions in sync.

## Checklist

Before publishing:

- [ ] Update version in `pyproject.toml`
- [ ] Update README.md if needed
- [ ] Clean old builds (`rm -rf dist/ build/`)
- [ ] Build new distributions (`python -m build`)
- [ ] Check with twine (`twine check dist/*`)
- [ ] Test on Test PyPI first
- [ ] Tag release in git
- [ ] Upload to production PyPI
- [ ] Verify on PyPI website
- [ ] Update main `hfortix-fortios` to require new stubs version

## Troubleshooting

### "File already exists"
PyPI doesn't allow re-uploading the same version. Increment version number.

### "Invalid distribution"
Run `twine check dist/*` to see what's wrong.

### "Authentication failed"
Check your API token in `~/.pypirc`.

## Links

- PyPI Project: https://pypi.org/project/hfortix-fortios-stubs/
- Test PyPI: https://test.pypi.org/project/hfortix-fortios-stubs/
- PyPI Publishing Guide: https://packaging.python.org/tutorials/packaging-projects/
