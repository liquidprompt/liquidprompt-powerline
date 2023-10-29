# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
import time
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Liquid Prompt Powerline theme'
copyright = '2020-%s, Liquid Prompt team' % time.strftime('%Y')
author = 'Mark Vander Stel'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_rtd_theme',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.spelling',
]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'venv', 'Thumbs.db', '.DS_Store']

highlight_language = 'shell'

# Enable linking to Liquid Prompt documentation by reference.
intersphinx_mapping = {
    'liquidprompt': ('https://liquidprompt.readthedocs.io/en/stable',
        ('../../liquidprompt/docs/_build/html/objects.inv', None)),
}

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# These paths are either relative to html_static_path
# # or fully qualified paths (eg. https://...)
html_css_files = [
     'liquid.css',
]

nitpick_ignore_regex = [
    # Environment variables are defined by external programs, so we do not
    # write documentation for them.
    ('envvar', r'.*'),
    # Our returned values are done in variables, not types.
    ('py:class', r'.*'),
]

# This is not Python code, so don't ignore Python specific things.
spelling_ignore_python_builtins=False
spelling_ignore_importable_modules=False
