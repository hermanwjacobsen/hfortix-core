# Minimal makefile for Sphinx documentation

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Convenience targets
.PHONY: clean livehtml doctest linkcheck coverage spelling

clean:
	rm -rf $(BUILDDIR)/*

livehtml:
	sphinx-autobuild "$(SOURCEDIR)" "$(BUILDDIR)/html" $(SPHINXOPTS) $(O)

# ============================================================================
# Documentation Quality Checks
# ============================================================================

doctest:
	@echo "Running doctests..."
	@$(SPHINXBUILD) -b doctest "$(SOURCEDIR)" "$(BUILDDIR)/doctest" $(SPHINXOPTS) $(O)
	@echo "Doctest complete. See $(BUILDDIR)/doctest/output.txt"

linkcheck:
	@echo "Checking for broken links..."
	@$(SPHINXBUILD) -b linkcheck "$(SOURCEDIR)" "$(BUILDDIR)/linkcheck" $(SPHINXOPTS) $(O)
	@echo "Link check complete. See $(BUILDDIR)/linkcheck/output.txt"

coverage:
	@echo "Checking documentation coverage..."
	@$(SPHINXBUILD) -b coverage "$(SOURCEDIR)" "$(BUILDDIR)/coverage" $(SPHINXOPTS) $(O)
	@echo "Coverage check complete. See $(BUILDDIR)/coverage/python.txt"

# Check spelling (requires sphinxcontrib-spelling)
spelling:
	@$(SPHINXBUILD) -b spelling "$(SOURCEDIR)" "$(BUILDDIR)/spelling" $(SPHINXOPTS) $(O)

# Run all quality checks
.PHONY: check
check: doctest linkcheck coverage
	@echo "All quality checks complete!"
