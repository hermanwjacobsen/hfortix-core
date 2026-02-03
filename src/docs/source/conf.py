# Configuration file for the Sphinx documentation builder.
# For hfortix-core package

import os
import sys
from datetime import datetime

# Add the package to the Python path
sys.path.insert(0, os.path.abspath('../..'))

# -- Project information -----------------------------------------------------
project = 'HFortix-Core'
copyright = f'{datetime.now().year}, Herman W. Jacobsen'
author = 'Herman W. Jacobsen'

try:
    from hfortix_core import __version__
    release = __version__
    version = '.'.join(__version__.split('.')[:2])
except ImportError:
    release = '0.5.154-beta'
    version = '0.5'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'myst_parser',
    'sphinx_copybutton',
    'sphinx_design',
    'sphinx_autodoc_typehints',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

suppress_warnings = ['myst.header']
toctree_maxdepth = 3

# Performance optimizations
import multiprocessing
num_cores = max(1, multiprocessing.cpu_count() - 1)
parallel_read = num_cores
parallel_write = num_cores

autodoc_member_order = 'bysource'
autodoc_typehints = 'description'
autodoc_typehints_format = 'short'

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = ['custom.css']

html_theme_options = {
    'navigation_depth': 3,
    'collapse_navigation': False,
    'sticky_navigation': True,
}

html_context = {
    'display_github': True,
    'github_user': 'hermanwjacobsen',
    'github_repo': 'hfortix-core',
    'github_version': 'main',
    'conf_py_path': '/docs/source/',
}

# -- Intersphinx mapping -----------------------------------------------------

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
}

# -- Autosummary settings ----------------------------------------------------

autosummary_generate = True
autosummary_imported_members = False

# -- Napoleon settings -------------------------------------------------------

napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = True
napoleon_use_param = True
napoleon_use_rtype = True
