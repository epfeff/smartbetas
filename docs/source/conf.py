# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('../../smartbetas/'))


# -- Project information -----------------------------------------------------

project = 'SmartBetas'
copyright = '2019, Elena Pfefferlé'
author = 'Elena Pfefferlé'

# The full version, including alpha/beta/rc tags
release = '0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [ 'rinoh.frontend.sphinx', 'sphinx.ext.autodoc'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
'preamble': '',

# Latex figure (float) alignment
'figure_align': 'htbp',
}

# -- Options for rinohtype PDF output ----------------------------------------

rinoh_documents = [(
    'index.rst',           # top-level file (index.rst)
    'sphinx_minimal',     # output (target.pdf)
    project,              # document title
    author,               # document author
)]
rinoh_documents = [('index',                    # top-level file (index.rst)
                    'SmartBetas',                # output (target.pdf)
                    'SmartBetas Code Documentation',  # document title
                    'Elena Pfefferlé')]       # author
rinoh_paper_size='A4'                          # paper size
#rinoh_logo = '_logo/logo.pdf'                   # title logo
rinoh_domain_indices = True                     # if false no index generated
rinoh_stylesheet = '_wstyle.rts'
rinoh_template = 'book'
