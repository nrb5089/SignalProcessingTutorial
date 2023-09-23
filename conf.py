import os
import sys
import shutil
from recommonmark.parser import CommonMarkParser

# -- Path setup --------------------------------------------------------------

sys.path.insert(0, os.path.abspath('.'))

def setup(app):
	app.add_config_value('recommonmark_config', {
		'auto_toc_tree_section': 'Contents',
		'enable_math': True,
		'enable_inline_math': True,
		'enable_eval_rst': True,
	}, True)
	app.add_transform(AutoStructify)
	
	# Copying figs directory to the _build directory
	dest_dir = os.path.join(app.outdir, 'figs')
	src_dir = os.path.abspath('figs')

	if not os.path.exists(dest_dir):
		shutil.copytree(src_dir, dest_dir)


# -- Project information -----------------------------------------------------

project = 'Your Project Name'
author = 'Your Name'
version = '1.0'
release = '1.0'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings.
extensions = ['
	'sphinx.ext.mathjax',
	'myst_parser'
]

# The master document, containing the table of contents.
master_doc = 'index'

# Using CommonMarkParser for markdown support
source_parsers = {
	'.md': CommonMarkParser,
}

# Adding Markdown suffix to source_suffix
source_suffix = ['.rst', '.md']

#Image storage
html_static_path = ['figs']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# -- Options for HTML output -------------------------------------------------

#html_theme = 'sphinx_rtd_theme'
html_theme = 'alabaster'

# -- Path settings for Read the Docs ----------------------------------------

# Check if on Read the Docs environment
on_rtd = os.environ.get('READTHEDOCS') == 'True'

if on_rtd:
	build_dir = os.path.join(os.environ.get('READTHEDOCS_OUTPUT'), 'html')
else:
	build_dir = '_build/html'

# Ensure 'figs' directory is copied to the expected build directory
if os.path.exists(os.path.join(build_dir, 'figs')):
	shutil.rmtree(os.path.join(build_dir, 'figs'))
shutil.copytree('figs', os.path.join(build_dir, 'figs'))
