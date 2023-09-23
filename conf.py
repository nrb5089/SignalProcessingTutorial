import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------
project = 'Signal Processing Tutorial'
copyright = '2023, Nate Blinn'
author = 'Nate Blinn'
release = '1.0.0'

# -- General configuration ---------------------------------------------------

extensions = [
    'recommonmark',
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx'
]

templates_path = ['_templates']
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}
master_doc = 'index'  # The main toc tree is on 'index.md'

# -- Options for HTML output -------------------------------------------------
html_theme = 'alabaster'
html_static_path = ['_static']

# -- Extension configuration -------------------------------------------------
intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
}
